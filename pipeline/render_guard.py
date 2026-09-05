#!/usr/bin/env python3
"""Fail-closed Instatoon episode/render validator.

Project-specific story/scene checks live here.
Media-conditioning authorization uses the same generic requirement model as
AutoPipeline MEDIA_INPUT_CONTRACT: declared requirements + renderer capability
+ actual supplied evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


class GuardError(RuntimeError):
    pass


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise GuardError(f"missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise GuardError(f"invalid JSON: {path}: {exc}") from exc


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def active_episode_id(repo_root: Path) -> str:
    state = (repo_root / "CURRENT_STATE.md").read_text(encoding="utf-8")
    matches = re.findall(r"^Active episode:\s+episodes/(E\d+)/README\.md\s*$", state, re.M)
    if len(matches) != 1:
        raise GuardError("CURRENT_STATE.md has no single parseable Active episode line")
    return matches[0]


def extract_markdown_section(path: Path, heading: str) -> str:
    text = path.read_text(encoding="utf-8")
    start = text.find(heading)
    if start < 0:
        raise GuardError(f"canonical prompt section missing: {heading}")
    body_start = text.find("\n", start)
    if body_start < 0:
        raise GuardError(f"empty canonical prompt section: {heading}")
    tail = text[body_start + 1:]
    next_heading = re.search(r"^##\s+", tail, re.M)
    if next_heading:
        tail = tail[:next_heading.start()]
    section = tail.strip()
    if not section:
        raise GuardError(f"empty canonical prompt section: {heading}")
    return section


def _require(condition: bool, message: str):
    if not condition:
        raise GuardError(message)


PRODUCTION_STAGES = {
    "L8_AWAITING_APPROVAL": 10,
    "CAST_RESOLVED": 20,
    "L8_APPROVED": 30,
    "STORYBOARD_READY": 40,
    "VISUAL_PLAN_READY": 50,
    "RENDER_CONTRACT_READY": 60,
    "FIRST_FRAME_QC_PENDING": 70,
    "REMAINING_RENDER": 80,
    "LETTERING": 90,
    "FINAL_QC": 100,
    "EXPORT_READY": 110,
}


def validate_production_state_shape(state: dict, expected_episode_id: str | None = None):
    for key in ("state_version", "episode_id", "current_stage", "voice_gate", "frame_qc"):
        _require(key in state, f"PRODUCTION_STATE missing {key}")
    _require(state["state_version"] == "1.0", "unsupported PRODUCTION_STATE version")
    if expected_episode_id is not None:
        _require(state["episode_id"] == expected_episode_id, "production-state episode mismatch")
    _require(state["current_stage"] in PRODUCTION_STAGES, "invalid production current_stage")
    _require(isinstance(state["voice_gate"], dict), "voice_gate must be an object")
    _require(isinstance(state["frame_qc"], dict), "frame_qc must be an object")


def validate_production_state(plan: dict, state: dict):
    validate_production_state_shape(state, plan["episode_id"])
    gate = state["voice_gate"]
    _require(
        gate.get("status") == "PASS",
        "L8 USER VOICE GATE is not fully approved"
    )
    _require(
        gate.get("approved_scope") == "L1_L7_FULL_PACKAGE",
        "partial decision/CAST approval is not L8 full-package approval"
    )
    _require(
        gate.get("approval_kind") == "USER_EXPLICIT",
        "L8 approval must be explicit user approval"
    )
    _require(bool(gate.get("evidence")), "L8 approval evidence is required")


def validate_active_state(repo_root: Path):
    eid = active_episode_id(repo_root)
    state = load_json(repo_root / "episodes" / eid / "PRODUCTION_STATE.json")
    validate_production_state_shape(state, eid)
    return eid, state


def _require_persisted_qc(plan: dict, state: dict, slide_index: int, prompt_binding: str):
    if slide_index <= 1:
        return

    qc_index = slide_index - 1 if prompt_binding == "CONVERSATION_INFERRED" else 1
    slide_id = plan["slides"][qc_index - 1]["slide_id"]
    record = state.get("frame_qc", {}).get(slide_id)
    _require(record is not None, f"{slide_id}: persisted QC record missing")
    _require(record.get("slide_id") == slide_id, f"{slide_id}: QC slide binding mismatch")
    _require(record.get("status") == "PASS", f"{slide_id}: persisted QC is not PASS")
    _require(record.get("inspected_output") is True, f"{slide_id}: QC is not bound to an inspected output")
    _require(bool(record.get("attempt_id")), f"{slide_id}: QC attempt_id missing")
    digest = record.get("artifact_sha256")
    _require(
        isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest),
        f"{slide_id}: QC artifact_sha256 missing/invalid"
    )


def validate_episode_plan(plan: dict):
    for key in ("schema_version","episode_id","title","status","source","continuity_mode","format","cast","style","slides"):
        _require(key in plan, f"EPISODE_PLAN missing {key}")

    _require(plan["schema_version"] == "1.0", "unsupported EPISODE_PLAN schema_version")

    fmt = plan["format"]
    _require(fmt.get("text_free_raster") is True, "canonical raster must be text-free")
    _require(type(fmt.get("panels_per_image")) is int and fmt["panels_per_image"] == 1,
             "production requires exactly one panel per image")
    _require(fmt.get("delivery_mode") == "SEPARATE_FILES", "production requires separate image files")
    slides = plan["slides"]
    _require(fmt.get("slide_count") == len(slides), "slide_count does not match slides")

    actual = [s.get("index") for s in slides]
    _require(actual == list(range(1, len(slides) + 1)), f"slide indices must be continuous: {actual}")

    for slide in slides:
        expected_id = f'{plan["episode_id"]}_S{slide["index"]:02d}'
        _require(slide.get("slide_id") == expected_id, f"bad slide_id: expected {expected_id}")
        for field in ("role","beat","location","action","scene_facts","story_clarity","required_entities","composition"):
            _require(slide.get(field), f'{slide["slide_id"]} missing {field}')
        _require("forbidden_entities" in slide, f'{slide["slide_id"]} missing forbidden_entities')

    for char in plan["cast"].get("episode_only", []):
        if len(char.get("appears_in", [])) >= 2:
            _require(
                len(char.get("identity_digest", "").strip()) >= 20,
                f'episode-only character {char.get("id")} needs a persistent identity digest'
            )

    style = plan["style"]
    required_refs = style.get("required_refs", [])
    forbidden_refs = set(style.get("forbidden_legacy_refs", []))
    conditioning = style.get("reference_conditioning_requirement")
    _require(required_refs, "required_refs must not be empty")
    _require(not (set(required_refs) & forbidden_refs), "required_refs contains a forbidden legacy ref")
    _require(
        conditioning in {"BINARY_REQUIRED","AUTHORITY_ONLY_ALLOWED"},
        "style.reference_conditioning_requirement missing or invalid"
    )


def validate_media_requirements(repo_root: Path, plan: dict, manifest: dict):
    reqs = manifest.get("media_requirements")
    _require(isinstance(reqs, list) and reqs, "manifest media_requirements must be non-empty")

    seen = set()
    for req in reqs:
        rid = req.get("requirement_id")
        _require(rid and rid not in seen, f"duplicate/invalid media requirement_id: {rid}")
        seen.add(rid)
        _require(req.get("role"), f"{rid}: media role missing")
        _require(req.get("media_type") in {"image","audio","video","other"}, f"{rid}: invalid media_type")
        _require(req.get("source_id"), f"{rid}: source_id missing")
        _require(
            req.get("conditioning") in {"MUST_SUPPLY_MEDIA","AUTHORITY_ONLY_ALLOWED"},
            f"{rid}: invalid conditioning"
        )
        _require(isinstance(req.get("required"), bool), f"{rid}: required must be boolean")

        source_id = req["source_id"]
        if not re.match(r"^[a-zA-Z]+://", source_id) and not source_id.startswith("connector:"):
            source_path = repo_root / source_id
            _require(source_path.is_file(), f"{rid}: required media source missing: {source_id}")
            if req.get("required") and req.get("conditioning") == "MUST_SUPPLY_MEDIA":
                expected_hash = req.get("expected_hash")
                _require(isinstance(expected_hash, str) and re.fullmatch(r"[0-9a-f]{64}", expected_hash),
                         f"{rid}: required local media needs a SHA-256 expected_hash")
                _require(hashlib.sha256(source_path.read_bytes()).hexdigest() == expected_hash,
                         f"{rid}: local media SHA-256 mismatch")

    # Compatibility/migration invariant: every current style_ref must be represented
    # through the generic requirement model. Authorization never reads style_refs directly.
    style_sources = {
        req["source_id"]
        for req in reqs
        if req.get("role") == "style" and req.get("required") is True
    }
    _require(
        set(manifest.get("style_refs", [])) <= style_sources,
        "every style_ref must map to a required generic media requirement"
    )

    desired = plan["style"]["reference_conditioning_requirement"]
    if desired == "BINARY_REQUIRED":
        for ref in manifest.get("style_refs", []):
            matching = [r for r in reqs if r.get("source_id") == ref and r.get("role") == "style"]
            _require(matching, f"style ref missing media requirement: {ref}")
            _require(
                all(r.get("conditioning") == "MUST_SUPPLY_MEDIA" for r in matching),
                f"binary-required style ref cannot allow authority-only conditioning: {ref}"
            )


def validate_manifest(repo_root: Path, episode_dir: Path, plan: dict, manifest: dict, require_active: bool = True):
    for key in (
        "manifest_version","episode_id","episode_plan_git_blob_sha","canonical_prompt_source",
        "output","style_refs","media_requirements","renderer_contract","batch_policy","slides"
    ):
        _require(key in manifest, f"RENDER_MANIFEST missing {key}")

    _require(manifest["manifest_version"] == "1.0", "unsupported RENDER_MANIFEST version")
    _require(manifest["episode_id"] == plan["episode_id"], "manifest/plan episode mismatch")
    _require(
        manifest["episode_plan_git_blob_sha"] == git_blob_sha(episode_dir / "EPISODE_PLAN.json"),
        "manifest is stale: EPISODE_PLAN git blob SHA mismatch"
    )

    if require_active:
        active = active_episode_id(repo_root)
        _require(
            active == plan["episode_id"],
            f"active episode mismatch: CURRENT_STATE={active}, requested={plan['episode_id']}"
        )

    out = manifest["output"]
    fmt = plan["format"]
    for key in ("aspect_ratio","width","height","text_free_raster","panels_per_image","delivery_mode"):
        _require(out.get(key) == fmt.get(key), f"output {key} differs from EPISODE_PLAN")

    _require(
        manifest["style_refs"] == plan["style"]["required_refs"],
        "manifest style_refs must exactly match EPISODE_PLAN required_refs"
    )

    source = manifest["canonical_prompt_source"]
    _require(source.get("path") == "MASTER_PROMPTS.md", "prompt source must be MASTER_PROMPTS.md")
    _require(
        source.get("section_heading") == "## 12. COMPILED PRODUCTION PROMPT",
        "prompt compiler must use the canonical compiled-production section"
    )

    contract = manifest["renderer_contract"]
    _require(contract.get("unexpected_concept_policy") == "FAIL_CLOSED", "unexpected concept policy must be FAIL_CLOSED")
    _require(
        contract.get("required_reference_conditioning") == plan["style"]["reference_conditioning_requirement"],
        "manifest reference-conditioning requirement must match EPISODE_PLAN"
    )
    _require(
        manifest["batch_policy"].get("conversation_inferred") == "SEQUENTIAL_EVERY_FRAME_GATE",
        "conversation-inferred rendering must be sequentially gated"
    )
    _require(
        manifest["batch_policy"].get("explicit_payload") == "FIRST_FRAME_GATE_THEN_BATCH",
        "explicit-payload rendering must first-frame gate"
    )

    validate_media_requirements(repo_root, plan, manifest)

    _require(len(manifest["slides"]) == len(plan["slides"]), "manifest/plan slide count mismatch")
    for p, m in zip(plan["slides"], manifest["slides"]):
        _require(m.get("index") == p.get("index"), f"slide index mismatch at {p.get('slide_id')}")
        _require(m.get("slide_id") == p.get("slide_id"), f"slide id mismatch at {p.get('slide_id')}")
        _require(m.get("required_entities") == p.get("required_entities"), f"required_entities drift at {p.get('slide_id')}")
        _require(m.get("forbidden_entities") == p.get("forbidden_entities"), f"forbidden_entities drift at {p.get('slide_id')}")
        _require(m.get("scene_contract") == p.get("scene_facts"), f"scene contract drift at {p.get('slide_id')}")


def validate_repository(repo_root: Path, episode_id: str | None = None, require_active: bool = True):
    active = active_episode_id(repo_root)
    eid = episode_id or active
    episode_dir = repo_root / "episodes" / eid
    plan = load_json(episode_dir / "EPISODE_PLAN.json")
    manifest = load_json(episode_dir / "RENDER_MANIFEST.json")
    state = load_json(episode_dir / "PRODUCTION_STATE.json")
    _require(plan.get("episode_id") == eid, "episode directory/plan id mismatch")
    validate_episode_plan(plan)
    validate_manifest(repo_root, episode_dir, plan, manifest, require_active=require_active)
    validate_production_state(plan, state)
    return plan, manifest


def compile_prompt(repo_root: Path, episode_id: str, slide_index: int) -> str:
    plan, manifest = validate_repository(repo_root, episode_id)
    _require(1 <= slide_index <= len(plan["slides"]), "requested slide index out of range")

    slide = plan["slides"][slide_index - 1]
    source = manifest["canonical_prompt_source"]
    base = extract_markdown_section(repo_root / source["path"], source["section_heading"])

    episode_only = "\n".join(
        f'- {c["id"]}: {c["identity_digest"]}'
        for c in plan["cast"].get("episode_only", [])
        if slide_index in c.get("appears_in", [])
    ) or "- none"

    main_cast = ", ".join(plan["cast"].get("main_cast", [])) or "none"
    facts = "\n".join(f"- {x}" for x in slide["scene_facts"])
    required = ", ".join(slide["required_entities"])
    forbidden = ", ".join(slide["forbidden_entities"]) or "none"
    media = "\n".join(
        f'- {r["requirement_id"]} | role={r["role"]} | type={r["media_type"]} | '
        f'source={r["source_id"]} | conditioning={r["conditioning"]}'
        for r in manifest["media_requirements"] if r.get("required") is True
    )

    return f"""{base}

RENDER CONTRACT — DO NOT DEVIATE
EPISODE_ID: {plan['episode_id']}
SLIDE_ID: {slide['slide_id']}
STORY BEAT: {slide['beat']}
OUTPUT: {plan['format']['aspect_ratio']} {plan['format']['width']}x{plan['format']['height']}
DELIVERY: SEPARATE_FILES. Exactly ONE panel in ONE image for {slide['slide_id']} only.
No multi-panel page, comic strip, grid, collage, storyboard sheet or contact sheet.
Reference sheets are input references only; never copy their multi-view layout into the output.
RASTER_TEXT: NONE. No readable captions, dialogue, labels, logos, watermarks, or speech bubbles.

MAIN CAST: {main_cast}
EPISODE-LOCAL IDENTITIES:
{episode_only}

LOCATION: {slide['location']}
ACTION: {slide['action']}
COMPOSITION: {slide['composition']}
STORY CLARITY: {slide['story_clarity']}

SCENE FACTS — ALL MUST BE TRUE:
{facts}

REQUIRED ENTITIES: {required}
FORBIDDEN / UNPLANNED ENTITIES: {forbidden}

REQUIRED MEDIA INPUTS:
{media}

FAIL-CLOSED:
A source path being present here is not evidence of renderer media injection.
Every MUST_SUPPLY_MEDIA item must be supplied as actual renderer media before generation.
If the renderer cannot satisfy the scene or media-input contract, return no production frame rather than inventing a replacement.
""".strip() + "\n"


def authorize(
    repo_root: Path,
    episode_id: str,
    slide_index: int,
    prompt_binding: str,
    previous_frame_qc: str,
    renderer_supports_explicit_media_inputs: bool,
    renderer_supported_media_types: list[str] | None = None,
    supplied_media: list[dict] | None = None,
    require_active: bool = True,
) -> str:
    plan, manifest = validate_repository(repo_root, episode_id, require_active=require_active)
    state = load_json(repo_root / "episodes" / episode_id / "PRODUCTION_STATE.json")
    renderer_supported_media_types = renderer_supported_media_types or []
    supplied_media = supplied_media or []

    _require(1 <= slide_index <= plan["format"]["slide_count"], "slide out of range")
    contract = manifest["renderer_contract"]
    _require(prompt_binding in contract["allowed_prompt_bindings"], f"prompt binding not allowed: {prompt_binding}")

    stage = state["current_stage"]
    if slide_index == 1:
        _require(
            stage in {"RENDER_CONTRACT_READY", "FIRST_FRAME_QC_PENDING"},
            f"slide 1 render blocked at production stage {stage}"
        )
    else:
        _require(
            stage == "REMAINING_RENDER",
            f"slide {slide_index} render requires production stage REMAINING_RENDER, got {stage}"
        )

    supplied_by_id = {x.get("requirement_id"): x for x in supplied_media}
    supported_types = set(renderer_supported_media_types)

    for req in manifest["media_requirements"]:
        if req.get("required") is not True or req.get("conditioning") != "MUST_SUPPLY_MEDIA":
            continue
        rid = req["requirement_id"]
        _require(renderer_supports_explicit_media_inputs, f"{rid}: renderer cannot accept explicit media inputs")
        _require(req["media_type"] in supported_types, f"{rid}: renderer does not support media type {req['media_type']}")
        evidence = supplied_by_id.get(rid)
        _require(evidence is not None, f"{rid}: required media was not supplied")
        _require(evidence.get("source_id") == req["source_id"], f"{rid}: supplied source_id mismatch")
        _require(evidence.get("media_type") == req["media_type"], f"{rid}: supplied media_type mismatch")
        expected_hash = req.get("expected_hash")
        if expected_hash:
            _require(evidence.get("actual_hash") == expected_hash, f"{rid}: supplied media hash mismatch")

    # Backward-compatible CLI argument is deliberately non-authoritative.
    # A literal PASS cannot replace persisted QC bound to a specific artifact.
    _require_persisted_qc(plan, state, slide_index, prompt_binding)

    if prompt_binding == "CONVERSATION_INFERRED":
        return "AUTHORIZED_SEQUENTIAL_SINGLE_FRAME"
    return "AUTHORIZED_FIRST_FRAME" if slide_index == 1 else "AUTHORIZED_POST_FIRST_FRAME"

def parse_supplied_media(values: list[str]) -> list[dict]:
    parsed = []
    for value in values:
        parts = value.split("|", 3)
        if len(parts) not in (3, 4):
            raise GuardError("--supplied-media must be requirement_id|source_id|media_type[|actual_hash]")
        parsed.append({
            "requirement_id": parts[0],
            "source_id": parts[1],
            "media_type": parts[2],
            "actual_hash": parts[3] if len(parts) == 4 and parts[3] else None,
        })
    return parsed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    sub = parser.add_subparsers(dest="cmd", required=True)

    validate = sub.add_parser("validate")
    validate.add_argument("--episode")

    compile_cmd = sub.add_parser("compile")
    compile_cmd.add_argument("--episode", required=True)
    compile_cmd.add_argument("--slide", type=int, required=True)

    auth = sub.add_parser("authorize")
    auth.add_argument("--episode", required=True)
    auth.add_argument("--slide", type=int, required=True)
    auth.add_argument("--prompt-binding", required=True, choices=["EXPLICIT_COMPILED_PAYLOAD","CONVERSATION_INFERRED"])
    auth.add_argument("--previous-frame-qc", default="NOT_RUN", choices=["NOT_RUN","PASS","FAIL"])
    auth.add_argument("--renderer-explicit-media", action="store_true")
    auth.add_argument("--supported-media-type", action="append", default=[])
    auth.add_argument("--supplied-media", action="append", default=[])

    args = parser.parse_args()
    root = Path(args.repo_root).resolve()

    try:
        if args.cmd == "validate":
            eid = args.episode or active_episode_id(root)
            state = load_json(root / "episodes" / eid / "PRODUCTION_STATE.json")
            validate_production_state_shape(state, eid)
            if PRODUCTION_STAGES[state["current_stage"]] < PRODUCTION_STAGES["RENDER_CONTRACT_READY"]:
                print(json.dumps({
                    "status":"PASS",
                    "episode_id":eid,
                    "current_stage":state["current_stage"],
                    "render_ready":False
                }, ensure_ascii=False))
            else:
                plan, _ = validate_repository(root, eid)
                print(json.dumps({
                    "status":"PASS",
                    "episode_id":plan["episode_id"],
                    "current_stage":state["current_stage"],
                    "render_ready":True,
                    "slides":plan["format"]["slide_count"],
                    "manifest_sha1":git_blob_sha(root / "episodes" / plan["episode_id"] / "RENDER_MANIFEST.json")
                }, ensure_ascii=False))
        elif args.cmd == "compile":
            print(compile_prompt(root, args.episode, args.slide), end="")
        else:
            print(authorize(
                root,
                args.episode,
                args.slide,
                args.prompt_binding,
                args.previous_frame_qc,
                args.renderer_explicit_media,
                args.supported_media_type,
                parse_supplied_media(args.supplied_media),
            ))
    except GuardError as exc:
        print(f"RENDER_GUARD_FAIL: {exc}", file=sys.stderr)
        raise SystemExit(2)


if __name__ == "__main__":
    main()
