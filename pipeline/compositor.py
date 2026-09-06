#!/usr/bin/env python3
"""Deterministic Instatoon raster compositor.

Final frames are assembled from APPROVED, hash-bound registry assets.
Meaning-bearing text/UI is intentionally out of scope and remains a later
editable lettering/composition layer.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Pillow is required: pip install pillow") from exc


class CompositionError(RuntimeError):
    pass


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise CompositionError(f"missing file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise CompositionError(f"invalid JSON: {path}: {exc}") from exc


def load_registry(project_root: Path, registry_path: Path) -> dict[str, dict]:
    raw = load_json(registry_path)
    if raw.get("schema_version") != "1.0":
        raise CompositionError("unsupported asset registry version")
    assets: dict[str, dict] = {}
    for item in raw.get("assets", []):
        asset_id = item.get("asset_id")
        if not asset_id or asset_id in assets:
            raise CompositionError(f"missing or duplicate asset_id: {asset_id!r}")
        if item.get("status") != "APPROVED":
            continue
        path = project_root / item["path"]
        if not path.is_file():
            raise CompositionError(f"{asset_id}: missing asset bytes at {item['path']}")
        digest = sha256_file(path)
        if digest != item.get("sha256"):
            raise CompositionError(f"{asset_id}: SHA-256 mismatch")
        with Image.open(path) as im:
            if [im.width, im.height] != [item.get("width"), item.get("height")]:
                raise CompositionError(f"{asset_id}: registered dimensions do not match file")
        assets[asset_id] = {**item, "_path": path}
    return assets


def _transform(asset: Image.Image, layer: dict) -> Image.Image:
    image = asset.convert("RGBA")
    scale = float(layer["scale"])
    if scale != 1:
        width = max(1, round(image.width * scale))
        height = max(1, round(image.height * scale))
        image = image.resize((width, height), Image.Resampling.LANCZOS)
    if layer.get("flip_x"):
        image = ImageOps.mirror(image)
    rotation = float(layer.get("rotation_deg", 0))
    if rotation:
        image = image.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True)
    opacity = float(layer.get("opacity", 1))
    if opacity < 1:
        alpha = image.getchannel("A").point(lambda value: round(value * opacity))
        image.putalpha(alpha)
    return image


def compose(project_root: Path, registry_path: Path, scene_path: Path, output_path: Path) -> str:
    registry = load_registry(project_root, registry_path)
    scene = load_json(scene_path)
    if scene.get("schema_version") != "1.0":
        raise CompositionError("unsupported scene version")

    canvas = scene["canvas"]
    width, height = int(canvas["width"]), int(canvas["height"])
    rgba = tuple(int(v) for v in canvas["background_rgba"])
    base = Image.new("RGBA", (width, height), rgba)

    indexed = list(enumerate(scene.get("layers", [])))
    for _, layer in sorted(indexed, key=lambda pair: (int(pair[1]["z"]), pair[0])):
        asset_id = layer["asset_id"]
        if asset_id not in registry:
            raise CompositionError(f"{asset_id}: not an APPROVED registered asset")
        x, y = int(layer["x"]), int(layer["y"])
        if x < 0 or y < 0:
            raise CompositionError("v1 compositor requires non-negative x/y")
        with Image.open(registry[asset_id]["_path"]) as raw:
            transformed = _transform(raw, layer)
        base.alpha_composite(transformed, dest=(x, y))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Convert to RGB to strip source metadata/profile variance. Explicit PNG
    # parameters keep repeated composition stable for identical inputs.
    base.convert("RGB").save(output_path, "PNG", optimize=False, compress_level=9)
    return sha256_file(output_path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--registry", default="assets/production/registry.json")
    parser.add_argument("--scene", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    try:
        digest = compose(
            root,
            (root / args.registry).resolve(),
            (root / args.scene).resolve(),
            (root / args.output).resolve(),
        )
    except CompositionError as exc:
        print(f"COMPOSITION_FAIL: {exc}")
        return 2
    print(f"COMPOSITION_PASS sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
