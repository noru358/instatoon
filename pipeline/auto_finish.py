#!/usr/bin/env python3
"""Experimental anchor-gated auto-finish runner for Instatoon.

AUTO_FINISH changes only the approval topology:
- L8/storyboard approval remains human.
- Slide 1 (episode anchor) remains a human visual approval.
- After that approval, remaining raster frames are rendered sequentially,
  inspected by a vision QC model, lettered from a deterministic LETTERING_PLAN,
  final-QC'd, and exported without additional human approval.
- This intentionally BYPASSES the STANDARD manual full-raster-set user gate.
  STANDARD mode instead uses S01 user approval -> remaining internal QC ->
  complete raster-set user approval -> lettering/final.
- Any expected production failure fails closed into STANDARD mode at the nearest
  resumable stage. Existing manual render/qc commands remain authoritative.

No second mutable state store is introduced. Automation status is stored as an
optional object inside episodes/<ID>/PRODUCTION_STATE.json; detailed QC evidence
is immutable JSON beside the artifacts.
"""
from __future__ import annotations

import argparse
import base64
import datetime as _dt
import hashlib
import json
import os
import traceback
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

from pipeline import render as renderer
from pipeline import render_guard as guard
from pipeline import lettering

REPO_ROOT = Path(__file__).resolve().parent.parent

DEFAULT_QC_MODEL = os.environ.get("INSTATOON_QC_MODEL", "gpt-5.6-luna")
DEFAULT_MAX_ATTEMPTS = int(os.environ.get("INSTATOON_AUTO_MAX_ATTEMPTS", "3"))
DEFAULT_MAX_TOTAL_RENDER_ATTEMPTS = int(os.environ.get("INSTATOON_AUTO_MAX_TOTAL_RENDER_ATTEMPTS", "10"))
VISUAL_QC_MIN_CONFIDENCE = float(os.environ.get("INSTATOON_VISUAL_QC_MIN_CONFIDENCE", "0.88"))
FINAL_QC_MIN_CONFIDENCE = float(os.environ.get("INSTATOON_FINAL_QC_MIN_CONFIDENCE", "0.86"))


class AutoFinishError(RuntimeError):
    """Expected production failure that should roll back to STANDARD mode."""


class VisualQCResult(BaseModel):
    verdict: Literal["PASS", "FAIL"]
    confidence: float = Field(ge=0.0, le=1.0)
    retryability: Literal["STOCHASTIC", "PLAN_OR_PROMPT", "NOT_RETRYABLE"]
    critical_failures: list[str]
    observations: list[str]
    retry_hint: str = ""


class FinalQCResult(BaseModel):
    verdict: Literal["PASS", "FAIL"]
    confidence: float = Field(ge=0.0, le=1.0)
    critical_failures: list[str]
    observations: list[str]


def now_iso() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def episode_dir(episode_id: str) -> Path:
    return REPO_ROOT / "episodes" / episode_id


def qc_root(episode_id: str) -> Path:
    return episode_dir(episode_id) / "qc" / "auto_finish"


def lettering_plan_path(episode_id: str) -> Path:
    return episode_dir(episode_id) / "LETTERING_PLAN.json"


def event(state: dict, kind: str, **data) -> None:
    automation = state.setdefault("automation", {})
    events = automation.setdefault("events", [])
    events.append({"at": now_iso(), "kind": kind, **data})
    if len(events) > 40:
        del events[:-40]


def save_state(episode_id: str, state: dict) -> None:
    renderer.save_state(episode_id, state)


def activate(
    state: dict,
    episode_id: str,
    plan: dict,
    max_attempts: int,
    max_total_render_attempts: int,
) -> None:
    first_sid = plan["slides"][0]["slide_id"]
    first_qc = state.get("frame_qc", {}).get(first_sid)
    anchor = state.get("episode_anchor")
    if state.get("current_stage") != "REMAINING_RENDER":
        raise AutoFinishError(
            f"AUTO_FINISH requires REMAINING_RENDER immediately after anchor PASS; "
            f"got {state.get('current_stage')}"
        )
    if not first_qc or first_qc.get("status") != "PASS" or first_qc.get("inspected_output") is not True:
        raise AutoFinishError("slide 1 has no persisted human PASS")
    if not anchor or anchor.get("slide") != 1:
        raise AutoFinishError("slide 1 is not registered as the episode anchor")

    state["automation"] = {
        "mode": "AUTO_FINISH",
        "status": "RUNNING",
        "experiment_version": "1",
        "activated_at": now_iso(),
        "trigger": {
            "type": "USER_ANCHOR_PASS",
            "slide_id": first_sid,
            "artifact_sha256": first_qc.get("artifact_sha256"),
        },
        "policy": {
            "max_attempts_per_slide": max_attempts,
            "max_total_render_attempts": max_total_render_attempts,
            "visual_qc_min_confidence": VISUAL_QC_MIN_CONFIDENCE,
            "final_qc_min_confidence": FINAL_QC_MIN_CONFIDENCE,
        },
        "events": [],
        "last_error": None,
    }
    event(state, "ACTIVATED", stage=state["current_stage"])
    save_state(episode_id, state)


def rollback(episode_id: str, state: dict, stage: str, reason: str, detail: str = "") -> None:
    automation = state.setdefault("automation", {})
    event(state, "ROLLBACK", from_stage=state.get("current_stage"), to_stage=stage, reason=reason)
    automation["mode"] = "STANDARD"
    automation["status"] = "ROLLED_BACK"
    automation["rolled_back_at"] = now_iso()
    automation["last_error"] = {"reason": reason, "detail": detail}
    state["current_stage"] = stage
    save_state(episode_id, state)
    print(f"AUTO_FINISH_ROLLBACK: {reason}")
    if detail:
        print(detail)
    print(f"resume with standard mode at stage {stage}")


def _data_url(path: Path) -> str:
    suffix = path.suffix.lower()
    media = "image/png" if suffix == ".png" else "image/jpeg"
    return f"data:{media};base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"


def _openai_client():
    if not os.environ.get("OPENAI_API_KEY"):
        raise AutoFinishError("OPENAI_API_KEY is not set")
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise AutoFinishError("openai package is not installed") from exc
    return OpenAI()


def _slide_contract_text(plan: dict, slide: int) -> str:
    spec = plan["slides"][slide - 1]
    return json.dumps(
        {
            "slide_id": spec["slide_id"],
            "beat": spec["beat"],
            "location": spec["location"],
            "action": spec["action"],
            "composition": spec["composition"],
            "story_clarity": spec["story_clarity"],
            "scene_facts": spec["scene_facts"],
            "required_entities": spec["required_entities"],
            "forbidden_entities": spec["forbidden_entities"],
            "episode_only_cast": [
                c for c in plan["cast"].get("episode_only", [])
                if slide in c.get("appears_in", [])
            ],
        },
        ensure_ascii=False,
        indent=2,
    )


def inspect_art(
    episode_id: str,
    plan: dict,
    manifest: dict,
    state: dict,
    slide: int,
    model: str,
) -> tuple[VisualQCResult, Path]:
    output = renderer.art_path(episode_id, slide)
    if not output.is_file():
        raise AutoFinishError(f"rendered output missing: {output}")

    content = [
        {
            "type": "input_text",
            "text": (
                "You are a conservative production QC gate for a simple hand-drawn Instagram comic. "
                "Image 1 is the newly generated candidate. Image 2 is the already HUMAN-APPROVED "
                "episode anchor. Remaining images are canonical style references. "
                "PASS only when the candidate clearly satisfies the slide contract AND stays in the "
                "same drawing language as the anchor/references. Treat these as critical failures: "
                "multi-panel/grid/collage; baked readable text or speech bubbles; materially wrong "
                "cast/required entity/forbidden entity; identity drift for recurring people; major "
                "anatomy corruption; glossy anime/romance-webtoon/3D/cinematic rendering; style or "
                "detail density materially unlike the approved references. Small harmless variation "
                "is not a failure. If a failure looks like ordinary stochastic generation noise, mark "
                "retryability STOCHASTIC. If the scene contract/prompt itself likely needs a change, "
                "mark PLAN_OR_PROMPT. Do not PASS on uncertainty.\n\nSLIDE CONTRACT:\n"
                + _slide_contract_text(plan, slide)
            ),
        },
        {"type": "input_image", "image_url": _data_url(output)},
    ]

    anchor = state.get("episode_anchor")
    if not anchor:
        raise AutoFinishError("episode anchor missing during auto QC")
    content.append({"type": "input_image", "image_url": _data_url(REPO_ROOT / anchor["path"])})

    for req in manifest["media_requirements"]:
        if req.get("required") is True and req.get("role") == "style" and req.get("media_type") == "image":
            content.append({"type": "input_image", "image_url": _data_url(REPO_ROOT / req["source_id"])})

    client = _openai_client()
    response = client.responses.parse(
        model=model,
        input=[{"role": "user", "content": content}],
        text_format=VisualQCResult,
    )
    result = response.output_parsed
    if result is None:
        raise AutoFinishError("vision QC returned no structured result")

    attempt = renderer.latest_attempt(episode_id, plan["slides"][slide - 1]["slide_id"])
    attempt_id = attempt.get("attempt_id") if attempt else "unknown"
    directory = qc_root(episode_id) / "frames"
    directory.mkdir(parents=True, exist_ok=True)
    report_path = directory / f"{attempt_id}.json"
    payload = {
        "recorded_at": now_iso(),
        "episode_id": episode_id,
        "slide_id": plan["slides"][slide - 1]["slide_id"],
        "attempt_id": attempt_id,
        "artifact_path": str(output.relative_to(REPO_ROOT)),
        "artifact_sha256": sha256_file(output),
        "qc_model": model,
        "result": result.model_dump(),
        "threshold": VISUAL_QC_MIN_CONFIDENCE,
    }
    report_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result, report_path


def record_auto_pass(
    episode_id: str,
    plan: dict,
    state: dict,
    slide: int,
    report_path: Path,
    result: VisualQCResult,
) -> None:
    sid = plan["slides"][slide - 1]["slide_id"]
    path = renderer.art_path(episode_id, slide)
    digest = sha256_file(path)
    attempt = renderer.latest_attempt(episode_id, sid)
    if not attempt or attempt.get("output_sha256") != digest:
        raise AutoFinishError(f"{sid}: output no longer matches latest renderer attempt")

    state.setdefault("frame_qc", {})[sid] = {
        "slide_id": sid,
        "status": "PASS",
        "inspected_output": True,
        "attempt_id": attempt["attempt_id"],
        "artifact_sha256": digest,
        "artifact_path": str(path.relative_to(REPO_ROOT)),
        "note": "AUTO_FINISH vision QC PASS",
        "recorded_at": now_iso(),
        "inspector": "AUTO_VISION",
        "qc_report_path": str(report_path.relative_to(REPO_ROOT)),
        "qc_confidence": result.confidence,
    }
    registered = renderer.register_episode_identity_anchors(
        plan, state, slide, path, digest
    )
    for cid in registered:
        event(state, "IDENTITY_ANCHOR_REGISTERED", character_id=cid, slide_id=sid)

    passed = {
        s["slide_id"] for s in plan["slides"]
        if state.get("frame_qc", {}).get(s["slide_id"], {}).get("status") == "PASS"
    }
    state["current_stage"] = (
        "LETTERING" if len(passed) == plan["format"]["slide_count"] else "REMAINING_RENDER"
    )
    event(state, "FRAME_AUTO_PASS", slide_id=sid, confidence=result.confidence)
    save_state(episode_id, state)


def render_remaining(
    episode_id: str,
    plan: dict,
    manifest: dict,
    state: dict,
    image_model: str,
    qc_model: str,
    max_attempts: int,
    max_total_render_attempts: int,
) -> dict:
    total_render_attempts = 0
    for slide in range(2, plan["format"]["slide_count"] + 1):
        sid = plan["slides"][slide - 1]["slide_id"]
        existing = state.get("frame_qc", {}).get(sid)
        if existing and existing.get("status") == "PASS":
            current = renderer.art_path(episode_id, slide)
            if current.is_file() and existing.get("artifact_sha256") == sha256_file(current):
                print(f"{sid}: already has current PASS, skipping")
                continue

        for attempt_no in range(1, max_attempts + 1):
            if total_render_attempts >= max_total_render_attempts:
                raise AutoFinishError(
                    f"episode render-attempt cap reached ({max_total_render_attempts}) before {sid}"
                )
            total_render_attempts += 1
            print(
                f"\nAUTO_FINISH render {sid}: slide attempt {attempt_no}/{max_attempts}; "
                f"episode attempt {total_render_attempts}/{max_total_render_attempts}"
            )
            args = argparse.Namespace(
                episode=episode_id,
                slide=slide,
                model=image_model,
                dry_run=False,
            )
            renderer.cmd_render(args)
            state = renderer.load_state(episode_id)

            result, report_path = inspect_art(
                episode_id, plan, manifest, state, slide, qc_model
            )
            clean_pass = (
                result.verdict == "PASS"
                and result.confidence >= VISUAL_QC_MIN_CONFIDENCE
                and not result.critical_failures
            )
            print(
                f"AUTO_QC {sid}: {result.verdict} confidence={result.confidence:.3f} "
                f"retryability={result.retryability}"
            )
            if clean_pass:
                record_auto_pass(episode_id, plan, state, slide, report_path, result)
                state = renderer.load_state(episode_id)
                break

            event(
                state,
                "FRAME_AUTO_FAIL",
                slide_id=sid,
                confidence=result.confidence,
                retryability=result.retryability,
                report=str(report_path.relative_to(REPO_ROOT)),
            )
            save_state(episode_id, state)

            if result.retryability != "STOCHASTIC":
                raise AutoFinishError(
                    f"{sid} auto QC failed and requires plan/prompt or human review: "
                    + "; ".join(result.critical_failures or result.observations[:2])
                )
            if attempt_no == max_attempts:
                raise AutoFinishError(
                    f"{sid} failed automatic visual QC after {max_attempts} stochastic attempts"
                )
    return renderer.load_state(episode_id)


def inspect_final_layout(
    episode_id: str,
    plan: dict,
    lettering_plan: dict,
    model: str,
) -> tuple[FinalQCResult, Path]:
    finals = []
    expected = {}
    for slide in lettering_plan["slides"]:
        idx = slide["index"]
        path = episode_dir(episode_id) / "exports" / f"slide_{idx:02d}_final.png"
        if not path.is_file():
            raise AutoFinishError(f"final export missing: {path}")
        finals.append(path)
        expected[slide["slide_id"]] = [item["text"] for item in slide.get("items", [])]

    content = [
        {
            "type": "input_text",
            "text": (
                "You are checking final Instagram carousel lettering layout, not rewriting copy. "
                "Each following image is one final slide in order. The text was rendered "
                "deterministically from the approved lettering plan, so assess layout only: "
                "no clipped/overflowing text, readable hierarchy and order, bubbles/captions do not "
                "obscure a face, hand, key prop, or the story-critical phone area, and the lettering "
                "looks like a clean overlay rather than baked AI text. PASS only if every slide is "
                "publishable without a human layout fix.\n\nEXPECTED COPY BY SLIDE:\n"
                + json.dumps(expected, ensure_ascii=False, indent=2)
            ),
        }
    ]
    for path in finals:
        content.append({"type": "input_image", "image_url": _data_url(path)})

    client = _openai_client()
    response = client.responses.parse(
        model=model,
        input=[{"role": "user", "content": content}],
        text_format=FinalQCResult,
    )
    result = response.output_parsed
    if result is None:
        raise AutoFinishError("final vision QC returned no structured result")

    directory = qc_root(episode_id) / "final"
    directory.mkdir(parents=True, exist_ok=True)
    report_path = directory / f"final_{_dt.datetime.now(_dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.json"
    report_path.write_text(
        json.dumps(
            {
                "recorded_at": now_iso(),
                "episode_id": episode_id,
                "qc_model": model,
                "threshold": FINAL_QC_MIN_CONFIDENCE,
                "result": result.model_dump(),
                "final_files": [
                    {
                        "path": str(p.relative_to(REPO_ROOT)),
                        "sha256": sha256_file(p),
                    }
                    for p in finals
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return result, report_path


def run_auto_finish(args) -> int:
    plan = manifest = None
    activated = False

    try:
        episode_id = renderer.resolve_episode(args.episode)
        state = renderer.load_state(episode_id)
        plan, manifest = guard.validate_repository(REPO_ROOT, episode_id)
        minimum_required = max(0, plan["format"]["slide_count"] - 1)
        if args.max_total_render_attempts < minimum_required:
            raise AutoFinishError(
                f"max total render attempts {args.max_total_render_attempts} is below "
                f"the {minimum_required} remaining slides"
            )
        activate(
            state,
            episode_id,
            plan,
            args.max_attempts,
            args.max_total_render_attempts,
        )
        activated = True
        state = renderer.load_state(episode_id)

        # AUTO_FINISH is allowed to start only when the approved storyboard package
        # already contains deterministic lettering copy + placement.
        lettering_plan = lettering.load_and_validate_plan(REPO_ROOT, episode_id, plan)

        state = render_remaining(
            episode_id,
            plan,
            manifest,
            state,
            args.image_model,
            args.qc_model,
            args.max_attempts,
            args.max_total_render_attempts,
        )
        if state.get("current_stage") != "LETTERING":
            raise AutoFinishError(
                f"remaining raster sweep ended at {state.get('current_stage')}, expected LETTERING"
            )

        event(state, "LETTERING_STARTED")
        save_state(episode_id, state)
        lettering.render_episode(REPO_ROOT, episode_id, plan, lettering_plan)

        state = renderer.load_state(episode_id)
        state["current_stage"] = "FINAL_QC"
        event(state, "LETTERING_COMPLETE")
        save_state(episode_id, state)

        result, report_path = inspect_final_layout(
            episode_id, plan, lettering_plan, args.qc_model
        )
        clean_pass = (
            result.verdict == "PASS"
            and result.confidence >= FINAL_QC_MIN_CONFIDENCE
            and not result.critical_failures
        )
        if not clean_pass:
            raise AutoFinishError(
                "final lettering/layout QC failed: "
                + "; ".join(result.critical_failures or result.observations[:2])
            )

        state = renderer.load_state(episode_id)
        state["current_stage"] = "EXPORT_READY"
        automation = state.setdefault("automation", {})
        automation["status"] = "COMPLETED"
        automation["completed_at"] = now_iso()
        automation["last_error"] = None
        automation["final_qc_report"] = str(report_path.relative_to(REPO_ROOT))
        automation["final_qc_confidence"] = result.confidence
        event(state, "COMPLETED", final_qc_confidence=result.confidence)
        save_state(episode_id, state)
        print(f"\nAUTO_FINISH_COMPLETE: {episode_id} -> EXPORT_READY")
        return 0

    except Exception as exc:
        # The experiment must fail back to the standard pipeline instead of
        # trapping the episode in a half-automatic state.
        detail = f"{type(exc).__name__}: {exc}"
        print(detail)
        if not isinstance(exc, AutoFinishError):
            traceback.print_exc()
        if not activated:
            print("AUTO_FINISH_NOT_ACTIVATED: precondition failed; production state left unchanged")
            return 2
        try:
            state = renderer.load_state(episode_id)
            current = state.get("current_stage")
            rollback_stage = "LETTERING" if current in {"LETTERING", "FINAL_QC", "EXPORT_READY"} else "REMAINING_RENDER"
            rollback(episode_id, state, rollback_stage, "AUTO_FINISH_FAILED", detail)
        except Exception as rollback_exc:
            print(f"AUTO_FINISH_ROLLBACK_WRITE_FAILED: {rollback_exc}")
            return 2
        return 0


def cmd_status(args) -> int:
    episode_id = renderer.resolve_episode(args.episode)
    state = renderer.load_state(episode_id)
    automation = state.get("automation") or {
        "mode": "STANDARD",
        "status": "NOT_ACTIVATED",
    }
    print(json.dumps({
        "episode_id": episode_id,
        "current_stage": state.get("current_stage"),
        "automation": automation,
    }, ensure_ascii=False, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Instatoon experimental auto-finish runner")
    sub = parser.add_subparsers(dest="cmd", required=True)

    run = sub.add_parser("run", help="activate after human anchor PASS and finish automatically")
    run.add_argument("--episode")
    run.add_argument("--image-model", default=renderer.DEFAULT_MODEL)
    run.add_argument("--qc-model", default=DEFAULT_QC_MODEL)
    run.add_argument("--max-attempts", type=int, default=DEFAULT_MAX_ATTEMPTS)
    run.add_argument(
        "--max-total-render-attempts",
        type=int,
        default=DEFAULT_MAX_TOTAL_RENDER_ATTEMPTS,
    )

    status = sub.add_parser("status", help="show automation state")
    status.add_argument("--episode")

    args = parser.parse_args()
    if getattr(args, "max_attempts", 1) < 1 or getattr(args, "max_attempts", 1) > 5:
        parser.error("--max-attempts must be between 1 and 5")
    if (
        getattr(args, "max_total_render_attempts", 1) < 1
        or getattr(args, "max_total_render_attempts", 1) > 30
    ):
        parser.error("--max-total-render-attempts must be between 1 and 30")
    return run_auto_finish(args) if args.cmd == "run" else cmd_status(args)


if __name__ == "__main__":
    raise SystemExit(main())
