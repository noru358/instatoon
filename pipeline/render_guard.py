#!/usr/bin/env python3
"""Fail-closed Instatoon render-contract validator and deterministic prompt compiler.

Stdlib-only so ChatGPT/Claude/local/CI can run the same guard.
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
    match = re.search(r"^Active episode:\s+episodes/(E\d+)/README\.md\s*$", state, re.M)
    if not match:
        raise GuardError("CURRENT_STATE.md has no single parseable Active episode line")
    return match.group(1)


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


def validate_episode_plan(plan: dict):
    for key in ("schema_version","episode_id","title","status","source","continuity_mode","format","cast","style","slides"):
        _require(key in plan, f"EPISODE_PLAN missing {key}")

    _require(plan["schema_version"] == "1.0", "unsupported EPISODE_PLAN schema_version")

    fmt = plan["format"]
    _require(fmt.get("text_free_raster") is True, "canonical raster must be text-free")
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

    required_refs = plan["style"].get("required_refs", [])
    forbidden_refs = set(plan["style"].get("forbidden_legacy_refs", []))
    _require(required_refs, "required_refs must not be empty")
    _require(not (set(required_refs) & forbidden_refs), "required_refs contains a forbidden legacy ref")


def validate_manifest(repo_root: Path, episode_dir: Path, plan: dict, manifest: dict):
    for key in (
        "manifest_version","episode_id","episode_plan_git_blob_sha","canonical_prompt_source",
        "output","style_refs","renderer_contract","batch_policy","slides"
    ):
        _require(key in manifest, f"RENDER_MANIFEST missing {key}")

    _require(manifest["manifest_version"] == "1.0", "unsupported RENDER_MANIFEST version")
    _require(manifest["episode_id"] == plan["episode_id"], "manifest/plan episode mismatch")
    _require(
        manifest["episode_plan_git_blob_sha"] == git_blob_sha(episode_dir / "EPISODE_PLAN.json"),
        "manifest is stale: EPISODE_PLAN git blob SHA mismatch"
    )

    active = active_episode_id(repo_root)
    _require(
        active == plan["episode_id"],
        f"active episode mismatch: CURRENT_STATE={active}, requested={plan['episode_id']}"
    )

    out = manifest["output"]
    fmt = plan["format"]
    for key in ("aspect_ratio","width","height","text_free_raster"):
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
    _require(
        contract.get("unexpected_concept_policy") == "FAIL_CLOSED",
        "unexpected concept policy must be FAIL_CLOSED"
    )
    _require(
        manifest["batch_policy"].get("conversation_inferred") == "SEQUENTIAL_EVERY_FRAME_GATE",
        "conversation-inferred rendering must be sequentially gated"
    )
    _require(
        manifest["batch_policy"].get("explicit_payload") == "FIRST_FRAME_GATE_THEN_BATCH",
        "explicit-payload rendering must first-frame gate"
    )

    _require(len(manifest["slides"]) == len(plan["slides"]), "manifest/plan slide count mismatch")

    for p, m in zip(plan["slides"], manifest["slides"]):
        _require(m.get("index") == p.get("index"), f"slide index mismatch at {p.get('slide_id')}")
        _require(m.get("slide_id") == p.get("slide_id"), f"slide id mismatch at {p.get('slide_id')}")
        _require(
            m.get("required_entities") == p.get("required_entities"),
            f"required_entities drift at {p.get('slide_id')}"
        )
        _require(
            m.get("forbidden_entities") == p.get("forbidden_entities"),
            f"forbidden_entities drift at {p.get('slide_id')}"
        )
        _require(
            m.get("scene_contract") == p.get("scene_facts"),
            f"scene contract drift at {p.get('slide_id')}"
        )

    for ref in manifest["style_refs"]:
        _require((repo_root / ref).is_file(), f"required visual ref missing: {ref}")


def validate_repository(repo_root: Path, episode_id: str | None = None):
    active = active_episode_id(repo_root)
    eid = episode_id or active
    episode_dir = repo_root / "episodes" / eid

    plan = load_json(episode_dir / "EPISODE_PLAN.json")
    manifest = load_json(episode_dir / "RENDER_MANIFEST.json")

    _require(plan.get("episode_id") == eid, "episode directory/plan id mismatch")
    validate_episode_plan(plan)
    validate_manifest(repo_root, episode_dir, plan, manifest)
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
    refs = "\n".join(f"- {x}" for x in manifest["style_refs"])

    return f"""{base}

RENDER CONTRACT — DO NOT DEVIATE
EPISODE_ID: {plan['episode_id']}
SLIDE_ID: {slide['slide_id']}
OUTPUT: {plan['format']['aspect_ratio']} {plan['format']['width']}x{plan['format']['height']}
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

STYLE REFERENCES REQUIRED BY CONTRACT:
{refs}

FAIL-CLOSED:
Do not substitute a different story, mascot, animal, productivity/self-help theme, coding/Git scene, collage, poster, or unrelated character.
If the renderer cannot follow this exact scene contract, return no production frame rather than inventing a replacement.
""".strip() + "\n"


def authorize(repo_root: Path, episode_id: str, slide_index: int, prompt_binding: str, previous_frame_qc: str) -> str:
    plan, manifest = validate_repository(repo_root, episode_id)

    _require(1 <= slide_index <= plan["format"]["slide_count"], "slide out of range")
    _require(
        prompt_binding in manifest["renderer_contract"]["allowed_prompt_bindings"],
        f"prompt binding not allowed: {prompt_binding}"
    )

    if prompt_binding == "CONVERSATION_INFERRED":
        if slide_index > 1:
            _require(
                previous_frame_qc == "PASS",
                "conversation-inferred renderer is fail-closed: previous frame semantic QC must PASS"
            )
        return "AUTHORIZED_SEQUENTIAL_SINGLE_FRAME"

    if slide_index > 1:
        _require(
            previous_frame_qc == "PASS",
            "explicit-payload batch may continue only after first-frame semantic QC PASS"
        )

    return "AUTHORIZED_FIRST_FRAME" if slide_index == 1 else "AUTHORIZED_POST_FIRST_FRAME"


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
    auth.add_argument(
        "--prompt-binding",
        required=True,
        choices=["EXPLICIT_COMPILED_PAYLOAD","CONVERSATION_INFERRED"]
    )
    auth.add_argument(
        "--previous-frame-qc",
        default="NOT_RUN",
        choices=["NOT_RUN","PASS","FAIL"]
    )

    args = parser.parse_args()
    root = Path(args.repo_root).resolve()

    try:
        if args.cmd == "validate":
            plan, _ = validate_repository(root, args.episode)
            print(json.dumps({
                "status":"PASS",
                "episode_id":plan["episode_id"],
                "slides":plan["format"]["slide_count"],
                "manifest_sha1":git_blob_sha(root / "episodes" / plan["episode_id"] / "RENDER_MANIFEST.json")
            }, ensure_ascii=False))
        elif args.cmd == "compile":
            print(compile_prompt(root, args.episode, args.slide), end="")
        else:
            print(authorize(
                root, args.episode, args.slide, args.prompt_binding, args.previous_frame_qc
            ))
    except GuardError as exc:
        print(f"RENDER_GUARD_FAIL: {exc}", file=sys.stderr)
        raise SystemExit(2)


if __name__ == "__main__":
    main()
