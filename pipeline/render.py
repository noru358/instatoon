#!/usr/bin/env python3
"""Instatoon generative exception renderer.\n\nThe default final visual path is deterministic asset composition via\npipeline/compositor.py. This adapter is retained for approved exception shots,\nasset-authoring experiments that intentionally use its frame contract, and\nhistorical compatibility.\n\nLegacy note: this was formerly the only sanctioned production image path.

Design rule: evidence is DERIVED, never submitted.
This process loads the reference bytes, builds the request, calls the image
model, and records what it actually sent. Nothing here accepts a caller's claim
that a reference was supplied or that a frame passed QC; both are read from
real files and real hashes.

State lives in episodes/<ID>/PRODUCTION_STATE.json, which render_guard already
owns and enforces. This adapter never invents a stage transition that a human
verdict has not earned.

Commands
--------
  render  --slide N [--episode E00X] [--dry-run]
  qc      --slide N --verdict PASS|FAIL [--note "..."]
  status  [--episode E00X]
"""
from __future__ import annotations

import argparse
import base64
import datetime as _dt
import hashlib
import io
import json
import os
import sys
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipeline import render_guard as guard  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent

DEFAULT_MODEL = os.environ.get("INSTATOON_IMAGE_MODEL", "gpt-image-2")
GEN_SIZE = "1024x1280"  # exact 4:5; GPT Image 2 accepts flexible valid resolutions

ANCHOR_ROLE_NOTE = """
SECONDARY EPISODE ANCHOR
One attached image is an already-approved frame from this same episode. Treat it
as the identity and drawing-language anchor for the people in this scene. Do not
copy its composition, pose, camera angle or background; the scene contract above
controls those.
""".strip()

IDENTITY_ANCHOR_ROLE_NOTE = """
EPISODE-LOCAL IDENTITY ANCHOR
Additional attached approved episode frames may be bound to specific recurring
episode-local characters. Use those frames only to preserve that character's
face/hair/clothing identity. The current slide contract still controls pose,
action, location and composition.
""".strip()


class RenderError(RuntimeError):
    pass


# --------------------------------------------------------------------------
# paths and small helpers
# --------------------------------------------------------------------------

def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def now_iso() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")


def episode_dir(episode_id: str) -> Path:
    return REPO_ROOT / "episodes" / episode_id


def state_path(episode_id: str) -> Path:
    return episode_dir(episode_id) / "PRODUCTION_STATE.json"


def load_state(episode_id: str) -> dict:
    return guard.load_json(state_path(episode_id))


def save_state(episode_id: str, state: dict) -> None:
    guard.validate_production_state_shape(state, episode_id)
    state_path(episode_id).write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def art_path(episode_id: str, slide: int) -> Path:
    return episode_dir(episode_id) / "renders" / f"slide_{slide:02d}_art.png"


def attempts_dir(episode_id: str) -> Path:
    return episode_dir(episode_id) / "renders" / "attempts"


def slide_id_for(plan: dict, slide: int) -> str:
    return plan["slides"][slide - 1]["slide_id"]


def resolve_episode(explicit: str | None) -> str:
    if explicit:
        return explicit
    episode_id = guard.active_episode_id(REPO_ROOT)
    if episode_id is None:
        raise RenderError("no active episode: production is idle until a fresh episode package is created")
    return episode_id


def latest_attempt(episode_id: str, slide_id: str) -> dict | None:
    directory = attempts_dir(episode_id)
    if not directory.is_dir():
        return None
    records = sorted(directory.glob(f"{slide_id}_*.json"))
    if not records:
        return None
    return json.loads(records[-1].read_text(encoding="utf-8"))


def render_input_snapshot(episode_id: str) -> dict[str, str]:
    """Hash the exact repository authorities this adapter reads before a render.

    The GitHub workflow independently rejects a push if these authorities changed
    on the remote branch while the provider call was in flight. Keeping the same
    hashes in the attempt record makes that decision auditable.
    """
    paths = [
        Path("CURRENT_STATE.md"),
        Path("MASTER_PROMPTS.md"),
        Path("pipeline/render_guard.py"),
        Path("pipeline/render.py"),
        Path("episodes") / episode_id / "EPISODE_PLAN.json",
        Path("episodes") / episode_id / "RENDER_MANIFEST.json",
        Path("episodes") / episode_id / "PRODUCTION_STATE.json",
    ]
    snapshot = {}
    for rel in paths:
        path = REPO_ROOT / rel
        if not path.is_file():
            raise RenderError(f"render input missing: {rel}")
        snapshot[str(rel)] = sha256_file(path)
    return snapshot


# --------------------------------------------------------------------------
# QC read side — the recorded verdict must still match the file on disk
# --------------------------------------------------------------------------

def verify_recorded_qc(plan: dict, state: dict, episode_id: str, slide: int) -> str:
    """Confirm a persisted PASS still describes the image currently on disk."""
    record = state.get("frame_qc", {}).get(slide_id_for(plan, slide))
    if not record:
        return "NOT_RUN"
    path = art_path(episode_id, slide)
    if not path.is_file():
        raise RenderError(f"slide {slide} has a QC record but its image file is gone")
    if record.get("artifact_sha256") != sha256_file(path):
        raise RenderError(
            f"slide {slide} was re-rendered after its QC verdict; re-run qc on the new image"
        )
    return record.get("status", "NOT_RUN")


# --------------------------------------------------------------------------
# media binding
# --------------------------------------------------------------------------

def collect_required_media(manifest: dict) -> list[dict]:
    bound = []
    for req in manifest["media_requirements"]:
        if req.get("required") is not True or req.get("conditioning") != "MUST_SUPPLY_MEDIA":
            continue
        if req.get("media_type") != "image":
            raise RenderError(f"{req['requirement_id']}: this adapter only binds image media")
        path = REPO_ROOT / req["source_id"]
        if not path.is_file():
            raise RenderError(f"{req['requirement_id']}: missing file {req['source_id']}")
        actual = sha256_file(path)
        expected = req.get("expected_hash")
        if expected and actual != expected:
            raise RenderError(f"{req['requirement_id']}: SHA-256 mismatch, refusing to render")
        bound.append({
            "requirement_id": req["requirement_id"],
            "source_id": req["source_id"],
            "media_type": "image",
            "role": req["role"],
            "actual_hash": actual,
            "path": path,
        })
    if not bound:
        raise RenderError("no required image media bound; refusing to render")
    return bound


def collect_episode_anchor(state: dict, slide: int) -> dict | None:
    anchor = state.get("episode_anchor")
    if not anchor or anchor.get("slide") == slide:
        return None
    path = REPO_ROOT / anchor["path"]
    if not path.is_file():
        raise RenderError(f"registered episode anchor is missing: {anchor['path']}")
    if sha256_file(path) != anchor["artifact_sha256"]:
        raise RenderError("registered episode anchor changed on disk; re-run qc to re-register it")
    return {
        "requirement_id": "episode_anchor",
        "source_id": anchor["path"],
        "media_type": "image",
        "role": "episode_anchor",
        "actual_hash": anchor["artifact_sha256"],
        "path": path,
    }


def register_episode_identity_anchors(
    plan: dict,
    state: dict,
    slide: int,
    path: Path,
    digest: str,
) -> list[str]:
    """Promote a recurring episode-local character's first accepted appearance.

    This is generic cast continuity, not a per-episode special case. Only a PASS
    artifact may call this helper.
    """
    registered = []
    anchors = state.setdefault("identity_anchors", {})
    for char in plan["cast"].get("episode_only", []):
        appearances = char.get("appears_in", [])
        if len(appearances) < 2 or not appearances or min(appearances) != slide:
            continue
        cid = char.get("id")
        if not cid or cid in anchors:
            continue
        anchors[cid] = {
            "character_id": cid,
            "slide": slide,
            "slide_id": slide_id_for(plan, slide),
            "path": str(path.relative_to(REPO_ROOT)),
            "artifact_sha256": digest,
            "registered_at": now_iso(),
        }
        registered.append(cid)
    return registered


def collect_episode_identity_anchors(state: dict, plan: dict, slide: int) -> list[dict]:
    active_ids = {
        char.get("id")
        for char in plan["cast"].get("episode_only", [])
        if slide in char.get("appears_in", [])
    }
    bound = []
    for cid in sorted(x for x in active_ids if x):
        anchor = state.get("identity_anchors", {}).get(cid)
        if not anchor or anchor.get("slide") == slide:
            continue
        path = REPO_ROOT / anchor["path"]
        if not path.is_file():
            raise RenderError(f"identity anchor for {cid} is missing: {anchor['path']}")
        actual = sha256_file(path)
        if actual != anchor.get("artifact_sha256"):
            raise RenderError(f"identity anchor for {cid} changed on disk")
        bound.append({
            "requirement_id": f"episode_identity_anchor:{cid}",
            "source_id": anchor["path"],
            "media_type": "image",
            "role": "character_identity",
            "actual_hash": actual,
            "path": path,
        })
    return bound


# --------------------------------------------------------------------------
# provider call
# --------------------------------------------------------------------------

def call_image_api(prompt: str, media: list[dict], model: str) -> tuple[bytes, dict]:
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RenderError("the 'openai' package is not installed (pip install openai)") from exc

    if not os.environ.get("OPENAI_API_KEY"):
        raise RenderError("OPENAI_API_KEY is not set")

    client = OpenAI()
    handles = [open(m["path"], "rb") for m in media]
    try:
        # GPT Image 2 processes every image input at high fidelity automatically.
        # Do not send input_fidelity: the current API does not allow overriding it.
        result = client.images.edit(
            model=model,
            image=handles,
            prompt=prompt,
            size=GEN_SIZE,
            n=1,
        )
    finally:
        for handle in handles:
            handle.close()

    payload = result.data[0]
    if not getattr(payload, "b64_json", None):
        raise RenderError("provider returned no image payload")
    meta = {
        "model": model,
        "size": GEN_SIZE,
        "input_fidelity": "automatic_high" if model.startswith("gpt-image-2") else "provider_default",
        "provider_created": getattr(result, "created", None),
    }
    return base64.b64decode(payload.b64_json), meta


def to_contract_canvas(raw: bytes, width: int, height: int) -> bytes:
    try:
        from PIL import Image
    except ImportError as exc:
        raise RenderError("the 'pillow' package is not installed (pip install pillow)") from exc

    image = Image.open(io.BytesIO(raw)).convert("RGB")
    src_w, src_h = image.size
    if src_w * height != src_h * width:
        raise RenderError(
            f"provider returned {src_w}x{src_h}, not the required {width}:{height} aspect; "
            "refusing to crop a production frame"
        )
    image = image.resize((width, height), Image.LANCZOS)
    out = io.BytesIO()
    image.save(out, format="PNG")
    return out.getvalue()


# --------------------------------------------------------------------------
# render
# --------------------------------------------------------------------------

def cmd_render(args) -> int:
    if not args.exception_lane:
        raise RenderError(
            "direct full-frame generative rendering is retired as the default path. "
            "Resolve an ASSET_GAP and use the shared AutoPipeline compositor. "
            "Only an explicitly approved exceptional shot may use render --exception-lane."
        )
    episode_id = resolve_episode(args.episode)
    plan, manifest = guard.validate_repository(REPO_ROOT, episode_id)
    state = load_state(episode_id)

    slide = args.slide
    if not 1 <= slide <= plan["format"]["slide_count"]:
        raise RenderError(f"slide {slide} out of range for {episode_id}")

    sid = slide_id_for(plan, slide)
    if state.get("frame_qc", {}).get(sid, {}).get("status") == "PASS":
        raise RenderError(
            f"{sid} already has a PASS verdict. To redo it, first record a FAIL:\n"
            f"  qc --slide {slide} --verdict FAIL --note \"<reason>\""
        )

    prompt = guard.compile_prompt(REPO_ROOT, episode_id, slide)

    media = collect_required_media(manifest)
    anchor = collect_episode_anchor(state, slide)
    if anchor:
        media.append(anchor)
        prompt += "\n" + ANCHOR_ROLE_NOTE + "\n"

    identity_anchors = collect_episode_identity_anchors(state, plan, slide)
    existing_sources = {m["source_id"] for m in media}
    identity_anchors = [m for m in identity_anchors if m["source_id"] not in existing_sources]
    if identity_anchors:
        media.extend(identity_anchors)
        prompt += "\n" + IDENTITY_ANCHOR_ROLE_NOTE + "\n"

    prev_qc = verify_recorded_qc(plan, state, episode_id, slide - 1) if slide > 1 else "NOT_RUN"

    decision = guard.authorize(
        REPO_ROOT,
        episode_id,
        slide,
        prompt_binding="EXPLICIT_COMPILED_PAYLOAD",
        previous_frame_qc=prev_qc,
        renderer_supports_explicit_media_inputs=True,
        renderer_supported_media_types=["image"],
        supplied_media=[
            {k: m[k] for k in ("requirement_id", "source_id", "media_type", "actual_hash")}
            for m in media
        ],
    )

    print(f"episode      : {episode_id}")
    print(f"slide        : {sid}")
    print(f"stage        : {state['current_stage']}")
    print(f"guard        : {decision}")
    print(f"previous QC  : {prev_qc}")
    for m in media:
        print(f"bound media  : {m['role']:<15} {m['source_id']}  sha256={m['actual_hash'][:12]}")
    print(f"prompt sha256: {sha256_text(prompt)[:12]}  ({len(prompt)} chars)")

    if args.dry_run:
        print("\nDRY RUN — every gate passed. No provider call, no files written.")
        return 0

    source_snapshot = render_input_snapshot(episode_id)
    attempt_id = f"{sid}_{_dt.datetime.now(_dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')}_{uuid.uuid4().hex[:6]}"
    raw, meta = call_image_api(prompt, media, args.model)
    png = to_contract_canvas(raw, plan["format"]["width"], plan["format"]["height"])

    out = art_path(episode_id, slide)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(png)

    attempts_dir(episode_id).mkdir(parents=True, exist_ok=True)
    record = {
        "attempt_id": attempt_id,
        "episode_id": episode_id,
        "slide_id": sid,
        "rendered_at": now_iso(),
        "guard_decision": decision,
        "production_stage_at_render": state["current_stage"],
        "previous_frame_qc": prev_qc,
        "provider": meta,
        "source_snapshot": source_snapshot,
        "prompt_sha256": sha256_text(prompt),
        "prompt": prompt,
        "bound_media": [
            {k: m[k] for k in ("requirement_id", "role", "source_id", "actual_hash")}
            for m in media
        ],
        "output_path": str(out.relative_to(REPO_ROOT)),
        "output_sha256": hashlib.sha256(png).hexdigest(),
        "output_size": [plan["format"]["width"], plan["format"]["height"]],
    }
    (attempts_dir(episode_id) / f"{attempt_id}.json").write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    state.get("frame_qc", {}).pop(sid, None)  # a new render invalidates any old verdict
    if slide == 1 and state["current_stage"] == "RENDER_CONTRACT_READY":
        state["current_stage"] = "FIRST_FRAME_QC_PENDING"
    save_state(episode_id, state)

    print(f"\nwrote {out.relative_to(REPO_ROOT)}")
    print(f"attempt {attempt_id}")
    print(f"\nnext: look at the image, then run\n  qc --slide {slide} --verdict PASS")
    return 0


# --------------------------------------------------------------------------
# qc
# --------------------------------------------------------------------------

def cmd_qc(args) -> int:
    episode_id = resolve_episode(args.episode)
    plan, _ = guard.validate_repository(REPO_ROOT, episode_id)
    state = load_state(episode_id)
    inspector = args.inspector

    if args.verdict == "PASS" and args.slide == 1 and inspector != "USER":
        raise RenderError("S01 anchor PASS requires inspector=USER; later slides may use OPERATOR_INTERNAL")

    slide = args.slide
    if not 1 <= slide <= plan["format"]["slide_count"]:
        raise RenderError(f"slide {slide} out of range for {episode_id}")

    sid = slide_id_for(plan, slide)
    path = art_path(episode_id, slide)
    if not path.is_file():
        raise RenderError(f"no rendered image for {sid}: {path.relative_to(REPO_ROOT)}")

    digest = sha256_file(path)
    attempt = latest_attempt(episode_id, sid)
    if not attempt or attempt.get("output_sha256") != digest:
        raise RenderError(
            f"{sid}: the image on disk does not match any attempt record produced by this adapter. "
            "A verdict can only be recorded for an image this pipeline generated."
        )

    if args.verdict == "PASS":
        state.setdefault("frame_qc", {})[sid] = {
            "slide_id": sid,
            "status": "PASS",
            "inspected_output": True,
            "attempt_id": attempt["attempt_id"],
            "artifact_sha256": digest,
            "artifact_path": str(path.relative_to(REPO_ROOT)),
            "note": args.note or "",
            "recorded_at": now_iso(),
            "inspector": inspector,
        }
        if slide == 1 and state.get("episode_anchor") is None:
            state["episode_anchor"] = {
                "slide": slide,
                "slide_id": sid,
                "path": str(path.relative_to(REPO_ROOT)),
                "artifact_sha256": digest,
                "registered_at": now_iso(),
            }
            print(f"registered {sid} as the episode identity anchor")
        for cid in register_episode_identity_anchors(plan, state, slide, path, digest):
            print(f"registered {sid} as episode-local identity anchor for {cid}")
        if slide == 1 and state["current_stage"] == "FIRST_FRAME_QC_PENDING":
            state["current_stage"] = "REMAINING_RENDER"
        passed = {
            s["slide_id"] for s in plan["slides"]
            if state.get("frame_qc", {}).get(s["slide_id"], {}).get("status") == "PASS"
        }
        if len(passed) == plan["format"]["slide_count"]:
            state["current_stage"] = "RASTER_SET_QC_PENDING"
            state["raster_set_gate"] = {
                "status": "PENDING",
                "approval_kind": "NONE",
                "evidence": "All raster slides have artifact-bound QC PASS; awaiting full-set user review.",
                "approved_at": None,
                "artifacts": [
                    {
                        "slide_id": item["slide_id"],
                        "artifact_sha256": state["frame_qc"][item["slide_id"]]["artifact_sha256"],
                    }
                    for item in plan["slides"]
                ],
            }
    else:
        state.get("frame_qc", {}).pop(sid, None)
        anchor = state.get("episode_anchor")
        if anchor and anchor.get("slide") == slide:
            state["episode_anchor"] = None
        for cid, identity_anchor in list(state.get("identity_anchors", {}).items()):
            if identity_anchor.get("slide") == slide:
                del state["identity_anchors"][cid]
        state.pop("raster_set_gate", None)
        if slide == 1:
            # a failed first frame reopens the first-frame gate, nothing later may run
            state["current_stage"] = "RENDER_CONTRACT_READY"
        else:
            # a failed later frame reopens the normal remaining-frame render stage,
            # including when a previously complete episode had already reached the set gate.
            state["current_stage"] = "REMAINING_RENDER"

    save_state(episode_id, state)

    print(f"{sid}: {args.verdict}  sha256={digest[:12]}  attempt={attempt['attempt_id']}")
    print(f"stage: {state['current_stage']}")
    if args.verdict == "PASS" and state["current_stage"] == "RASTER_SET_QC_PENDING":
        print("next: user reviews the COMPLETE text-free raster set, then run raster-set-qc --verdict PASS")
    elif args.verdict == "PASS" and slide < plan["format"]["slide_count"]:
        print(f"next: render --slide {slide + 1}  (operator internal QC; no user gate required)")
    elif args.verdict == "PASS":
        print("next: full raster-set user review")
    else:
        print(f"next: fix the plan or the canonical prompt, then render --slide {slide} again")
    return 0


def cmd_raster_set_qc(args) -> int:
    episode_id = resolve_episode(args.episode)
    plan, _ = guard.validate_repository(REPO_ROOT, episode_id)
    state = load_state(episode_id)

    if state.get("current_stage") != "RASTER_SET_QC_PENDING":
        raise RenderError(
            f"full raster-set review requires RASTER_SET_QC_PENDING, got {state.get('current_stage')}"
        )

    artifacts = []
    for slide in plan["slides"]:
        index = slide["index"]
        sid = slide["slide_id"]
        if verify_recorded_qc(plan, state, episode_id, index) != "PASS":
            raise RenderError(f"{sid}: current artifact does not have a valid QC PASS")
        record = state.get("frame_qc", {}).get(sid, {})
        if record.get("inspected_output") is not True:
            raise RenderError(f"{sid}: QC is not bound to an inspected output")
        artifacts.append({
            "slide_id": sid,
            "artifact_sha256": record.get("artifact_sha256"),
        })

    first_sid = plan["slides"][0]["slide_id"]
    if state.get("frame_qc", {}).get(first_sid, {}).get("inspector") != "USER":
        raise RenderError("S01 must have a persisted USER visual PASS before full raster-set approval")

    if args.verdict == "PASS":
        state["raster_set_gate"] = {
            "status": "PASS",
            "approval_kind": "USER_EXPLICIT",
            "evidence": args.note or "User explicitly approved the complete text-free raster set.",
            "approved_at": now_iso(),
            "artifacts": artifacts,
        }
        state["current_stage"] = "LETTERING"
        print("full raster set: USER PASS")
        print("next: L14 lettering")
    else:
        state["raster_set_gate"] = {
            "status": "FAIL",
            "approval_kind": "USER_EXPLICIT",
            "evidence": args.note or "User rejected the complete raster set.",
            "approved_at": now_iso(),
            "artifacts": artifacts,
        }
        state["current_stage"] = "REMAINING_RENDER"
        print("full raster set: USER FAIL")
        print("next: mark the affected frame(s) FAIL, repair them, then rebuild the set")

    save_state(episode_id, state)
    return 0


# --------------------------------------------------------------------------
# status
# --------------------------------------------------------------------------

def cmd_status(args) -> int:
    episode_id = resolve_episode(args.episode)
    plan, _ = guard.validate_repository(REPO_ROOT, episode_id)
    state = load_state(episode_id)
    anchor = state.get("episode_anchor")

    print(f"episode        : {episode_id} — {plan['title']}")
    print(f"stage          : {state['current_stage']}")
    print(f"slides         : {plan['format']['slide_count']}")
    print(f"episode anchor : {anchor['slide_id'] if anchor else 'not registered'}")
    raster_gate = state.get("raster_set_gate")
    print(f"raster set gate: {raster_gate.get('status') if raster_gate else 'not reached'}")
    identity_anchors = state.get("identity_anchors", {})
    print(
        "identity anchors: "
        + (", ".join(f"{cid}={item['slide_id']}" for cid, item in sorted(identity_anchors.items()))
           if identity_anchors else "none")
    )
    print()
    for slide in plan["slides"]:
        index = slide["index"]
        sid = slide["slide_id"]
        path = art_path(episode_id, index)
        record = state.get("frame_qc", {}).get(sid)
        if not path.is_file():
            cell = "not rendered"
        elif not record:
            cell = "rendered, awaiting QC"
        elif record.get("artifact_sha256") != sha256_file(path):
            cell = "re-rendered, QC stale"
        else:
            cell = f"QC {record.get('status')}"
        print(f"  {sid}  {cell:<24} {slide['beat'][:52]}")
    for blocker in state.get("blockers", []):
        print(f"\nblocker {blocker.get('blocker_id')}: {blocker.get('status')}")
        print(f"  {blocker.get('reason', '')[:160]}")
    return 0


def cmd_resolve(args) -> int:
    """Print the resolved episode id. Used by CI to scope `git add` precisely."""
    print(resolve_episode(args.episode))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Instatoon renderer adapter")
    sub = parser.add_subparsers(dest="cmd", required=True)

    render = sub.add_parser("render", help="render one slide")
    render.add_argument("--slide", type=int, required=True)
    render.add_argument("--episode")
    render.add_argument("--model", default=DEFAULT_MODEL)
    render.add_argument("--dry-run", action="store_true",
                        help="run every gate and print the binding, but do not call the provider")
    render.add_argument("--exception-lane", action="store_true",
                        help="explicitly authorize a declared full-frame generative exception")

    qc = sub.add_parser("qc", help="record a frame QC verdict bound to the actual rendered image")
    qc.add_argument("--slide", type=int, required=True)
    qc.add_argument("--verdict", required=True, choices=["PASS", "FAIL"])
    qc.add_argument("--note", default="")
    qc.add_argument("--episode")
    qc.add_argument("--inspector", choices=["USER", "OPERATOR_INTERNAL"], default="OPERATOR_INTERNAL",
                    help="S01 PASS must be USER; S02+ normally use OPERATOR_INTERNAL")

    raster_set_qc = sub.add_parser("raster-set-qc", help="record the user verdict for the complete text-free raster set")
    raster_set_qc.add_argument("--verdict", required=True, choices=["PASS", "FAIL"])
    raster_set_qc.add_argument("--note", default="")
    raster_set_qc.add_argument("--episode")

    status = sub.add_parser("status", help="show stage, what is rendered, passed and next")
    status.add_argument("--episode")

    resolve = sub.add_parser("resolve", help="print the resolved episode id and exit")
    resolve.add_argument("--episode")

    args = parser.parse_args()
    try:
        if args.cmd == "render":
            return cmd_render(args)
        if args.cmd == "qc":
            return cmd_qc(args)
        if args.cmd == "raster-set-qc":
            return cmd_raster_set_qc(args)
        if args.cmd == "resolve":
            return cmd_resolve(args)
        return cmd_status(args)
    except (RenderError, guard.GuardError) as exc:
        print(f"RENDER_FAIL: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
