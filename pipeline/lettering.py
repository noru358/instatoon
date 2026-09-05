#!/usr/bin/env python3
"""Deterministic post-raster lettering for Instatoon.

The generated art is never overwritten. For each slide this module writes:
- lettering/slide_NN_overlay.png   transparent text/bubble layer
- exports/slide_NN_final.png      art + lettering composite
- lettering/manifest.json         source/output hashes and exact copy

LETTERING_PLAN.json is part of the user-approved storyboard package. It contains
final copy and normalized placement boxes; this runner never asks an image model
to draw text.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
from pathlib import Path


class LetteringError(RuntimeError):
    pass


def now_iso() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise LetteringError(message)


def _plan_path(repo_root: Path, episode_id: str) -> Path:
    return repo_root / "episodes" / episode_id / "LETTERING_PLAN.json"


def load_and_validate_plan(repo_root: Path, episode_id: str, episode_plan: dict) -> dict:
    path = _plan_path(repo_root, episode_id)
    if not path.is_file():
        raise LetteringError(
            f"{path.relative_to(repo_root)} missing; AUTO_FINISH requires lettering copy/placement "
            "to be locked with the storyboard before anchor approval"
        )
    try:
        plan = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise LetteringError(f"invalid LETTERING_PLAN.json: {exc}") from exc

    _require(plan.get("schema_version") == "1.0", "unsupported LETTERING_PLAN schema_version")
    _require(plan.get("episode_id") == episode_id, "LETTERING_PLAN episode mismatch")
    expected_blob = _git_blob_sha(repo_root / "episodes" / episode_id / "EPISODE_PLAN.json")
    _require(
        plan.get("episode_plan_git_blob_sha") == expected_blob,
        "LETTERING_PLAN is stale: EPISODE_PLAN git blob SHA mismatch",
    )

    canvas = plan.get("canvas", {})
    fmt = episode_plan["format"]
    _require(canvas.get("width") == fmt["width"], "LETTERING_PLAN canvas width mismatch")
    _require(canvas.get("height") == fmt["height"], "LETTERING_PLAN canvas height mismatch")

    slides = plan.get("slides")
    _require(isinstance(slides, list) and len(slides) == fmt["slide_count"],
             "LETTERING_PLAN slide count mismatch")

    expected_ids = [s["slide_id"] for s in episode_plan["slides"]]
    actual_ids = [s.get("slide_id") for s in slides]
    _require(actual_ids == expected_ids, "LETTERING_PLAN slide order/id mismatch")

    seen_text_ids = set()
    for idx, slide in enumerate(slides, start=1):
        _require(slide.get("index") == idx, f"LETTERING_PLAN bad slide index at {idx}")
        items = slide.get("items")
        _require(isinstance(items, list), f"{slide['slide_id']}: items must be a list")
        for item in items:
            tid = item.get("text_id")
            _require(isinstance(tid, str) and tid and tid not in seen_text_ids,
                     f"duplicate/invalid text_id: {tid}")
            seen_text_ids.add(tid)
            _require(item.get("kind") in {"caption", "speech", "chat", "sfx"},
                     f"{tid}: invalid lettering kind")
            _require(isinstance(item.get("text"), str) and item["text"].strip(),
                     f"{tid}: empty text")
            box = item.get("box")
            _require(isinstance(box, list) and len(box) == 4, f"{tid}: box must be [x,y,w,h]")
            _require(all(isinstance(v, (int, float)) for v in box), f"{tid}: box values must be numbers")
            x, y, w, h = box
            _require(0 <= x < 1 and 0 <= y < 1 and 0 < w <= 1 and 0 < h <= 1,
                     f"{tid}: normalized box out of range")
            _require(x + w <= 1.000001 and y + h <= 1.000001, f"{tid}: box exceeds canvas")
            if "tail_to" in item:
                tail = item["tail_to"]
                _require(isinstance(tail, list) and len(tail) == 2, f"{tid}: tail_to must be [x,y]")
                _require(all(isinstance(v, (int, float)) and 0 <= v <= 1 for v in tail),
                         f"{tid}: tail_to out of range")
    return plan


def _git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def _find_font(text: str, bold: bool = True) -> Path:
    candidates = []
    if bold:
        candidates.extend([
            Path("/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf"),
            Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"),
        ])
    candidates.extend([
        Path("/usr/share/fonts/truetype/nanum/NanumGothic.ttf"),
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ])
    for path in candidates:
        if path.is_file():
            if any(ord(ch) > 127 for ch in text) and "DejaVu" in path.name:
                continue
            return path
    raise LetteringError(
        "no Korean-capable font found. GitHub Actions must install fonts-nanum; "
        "do not commit font binaries into the repository"
    )


def _split_long_token(draw, token: str, font, max_width: int) -> list[str]:
    parts, current = [], ""
    for ch in token:
        test = current + ch
        if current and draw.textbbox((0, 0), test, font=font)[2] > max_width:
            parts.append(current)
            current = ch
        else:
            current = test
    if current:
        parts.append(current)
    return parts


def _wrap_text(draw, text: str, font, max_width: int) -> list[str]:
    paragraphs = text.split("\n")
    lines: list[str] = []
    for paragraph in paragraphs:
        if paragraph == "":
            lines.append("")
            continue
        words = paragraph.split(" ")
        current = ""
        for word in words:
            chunks = _split_long_token(draw, word, font, max_width)
            for chunk_idx, chunk in enumerate(chunks):
                candidate = chunk if not current else current + (" " if chunk_idx == 0 else "") + chunk
                if current and draw.textbbox((0, 0), candidate, font=font)[2] > max_width:
                    lines.append(current)
                    current = chunk
                else:
                    current = candidate
            if not chunks:
                continue
        if current:
            lines.append(current)
    return lines or [""]


def _fit_text(draw, text: str, font_path: Path, max_width: int, max_height: int,
              preferred: int, minimum: int, spacing: int):
    from PIL import ImageFont

    for size in range(preferred, minimum - 1, -2):
        font = ImageFont.truetype(str(font_path), size=size)
        lines = _wrap_text(draw, text, font, max_width)
        heights = []
        widths = []
        for line in lines:
            box = draw.textbbox((0, 0), line or " ", font=font)
            widths.append(box[2] - box[0])
            heights.append(box[3] - box[1])
        total_h = sum(heights) + spacing * max(0, len(lines) - 1)
        if max(widths or [0]) <= max_width and total_h <= max_height:
            return font, lines, total_h
    raise LetteringError(
        f"text does not fit its approved box even at {minimum}px: {text[:40]!r}"
    )


def _px_box(box, width: int, height: int) -> tuple[int, int, int, int]:
    x, y, w, h = box
    x0, y0 = round(x * width), round(y * height)
    x1, y1 = round((x + w) * width), round((y + h) * height)
    return x0, y0, x1, y1


def _draw_tail(draw, rect, tail_to, width: int, height: int) -> None:
    x0, y0, x1, y1 = rect
    tx, ty = round(tail_to[0] * width), round(tail_to[1] * height)
    cx = min(max(tx, x0 + 30), x1 - 30)
    if ty < y0:
        points = [(cx - 16, y0 + 4), (cx + 16, y0 + 4), (tx, ty)]
    elif ty > y1:
        points = [(cx - 16, y1 - 4), (cx + 16, y1 - 4), (tx, ty)]
    elif tx < x0:
        cy = min(max(ty, y0 + 30), y1 - 30)
        points = [(x0 + 4, cy - 16), (x0 + 4, cy + 16), (tx, ty)]
    else:
        cy = min(max(ty, y0 + 30), y1 - 30)
        points = [(x1 - 4, cy - 16), (x1 - 4, cy + 16), (tx, ty)]
    draw.polygon(points, fill=(255, 255, 255, 245), outline=(25, 25, 25, 255))


def _render_item(overlay, item: dict) -> dict:
    from PIL import ImageDraw

    draw = ImageDraw.Draw(overlay)
    width, height = overlay.size
    rect = _px_box(item["box"], width, height)
    x0, y0, x1, y1 = rect
    kind = item["kind"]
    padding = int(item.get("padding", 22))
    preferred = int(item.get("font_size", 52 if kind != "sfx" else 58))
    minimum = int(item.get("min_font_size", 32))
    spacing = int(item.get("line_spacing", 8))
    align = item.get("align", "center")
    if align not in {"left", "center", "right"}:
        raise LetteringError(f"{item['text_id']}: invalid align {align}")

    if kind in {"speech", "chat", "caption"}:
        radius = int(item.get("radius", 26))
        draw.rounded_rectangle(
            rect,
            radius=radius,
            fill=(255, 255, 255, 242),
            outline=(25, 25, 25, 255) if kind in {"speech", "chat"} else None,
            width=4 if kind in {"speech", "chat"} else 1,
        )
        if kind == "speech" and item.get("tail_to"):
            _draw_tail(draw, rect, item["tail_to"], width, height)

    font_path = _find_font(item["text"], bold=kind in {"caption", "sfx"})
    max_w = (x1 - x0) - 2 * padding
    max_h = (y1 - y0) - 2 * padding
    if max_w <= 0 or max_h <= 0:
        raise LetteringError(f"{item['text_id']}: lettering box is too small after padding")
    font, lines, total_h = _fit_text(
        draw, item["text"], font_path, max_w, max_h, preferred, minimum, spacing
    )

    metrics = []
    for line in lines:
        box = draw.textbbox((0, 0), line or " ", font=font)
        metrics.append((box[2] - box[0], box[3] - box[1]))
    y = y0 + padding + max(0, (max_h - total_h) // 2)
    for line, (line_w, line_h) in zip(lines, metrics):
        if align == "left":
            x = x0 + padding
        elif align == "right":
            x = x1 - padding - line_w
        else:
            x = x0 + (x1 - x0 - line_w) // 2
        if kind == "sfx":
            draw.text(
                (x, y),
                line,
                font=font,
                fill=(20, 20, 20, 255),
                stroke_width=3,
                stroke_fill=(255, 255, 255, 235),
            )
        else:
            draw.text((x, y), line, font=font, fill=(20, 20, 20, 255))
        y += line_h + spacing

    return {
        "text_id": item["text_id"],
        "text": item["text"],
        "kind": kind,
        "box": item["box"],
        "font_path": str(font_path),
        "font_size": font.size,
        "line_count": len(lines),
    }


def render_episode(repo_root: Path, episode_id: str, episode_plan: dict, lettering_plan: dict) -> dict:
    from PIL import Image

    ep_dir = repo_root / "episodes" / episode_id
    lettering_dir = ep_dir / "lettering"
    export_dir = ep_dir / "exports"
    lettering_dir.mkdir(parents=True, exist_ok=True)
    export_dir.mkdir(parents=True, exist_ok=True)

    width = episode_plan["format"]["width"]
    height = episode_plan["format"]["height"]
    records = []

    for slide in lettering_plan["slides"]:
        idx = slide["index"]
        sid = slide["slide_id"]
        art_path = ep_dir / "renders" / f"slide_{idx:02d}_art.png"
        if not art_path.is_file():
            raise LetteringError(f"{sid}: art file missing")
        art = Image.open(art_path).convert("RGBA")
        if art.size != (width, height):
            raise LetteringError(f"{sid}: art dimensions {art.size} != {(width, height)}")

        overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        item_records = [_render_item(overlay, item) for item in slide.get("items", [])]

        overlay_path = lettering_dir / f"slide_{idx:02d}_overlay.png"
        overlay.save(overlay_path, "PNG")

        final = Image.alpha_composite(art, overlay).convert("RGB")
        final_path = export_dir / f"slide_{idx:02d}_final.png"
        final.save(final_path, "PNG")

        records.append({
            "slide_id": sid,
            "index": idx,
            "source_art": str(art_path.relative_to(repo_root)),
            "source_art_sha256": sha256_file(art_path),
            "overlay": str(overlay_path.relative_to(repo_root)),
            "overlay_sha256": sha256_file(overlay_path),
            "final": str(final_path.relative_to(repo_root)),
            "final_sha256": sha256_file(final_path),
            "items": item_records,
        })

    manifest = {
        "schema_version": "1.0",
        "episode_id": episode_id,
        "rendered_at": now_iso(),
        "lettering_plan_path": str(_plan_path(repo_root, episode_id).relative_to(repo_root)),
        "lettering_plan_sha256": sha256_file(_plan_path(repo_root, episode_id)),
        "slides": records,
    }
    manifest_path = lettering_dir / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    export_manifest = {
        "schema_version": "1.0",
        "episode_id": episode_id,
        "exported_at": now_iso(),
        "format": episode_plan["format"],
        "slides": [
            {
                "slide_id": r["slide_id"],
                "path": r["final"],
                "sha256": r["final_sha256"],
            }
            for r in records
        ],
    }
    (export_dir / "manifest.json").write_text(
        json.dumps(export_manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return manifest
