#!/usr/bin/env python3
"""Fail-closed registry validation for current style-reference binaries."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "assets/style_refs/v2_current/registry.json"
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}
ALLOWED_CLASSES = {
    "PROJECT_CANONICAL",
    "PROJECT_REUSABLE",
    "EPISODE_LOCAL",
    "ACCEPTED_OUTPUT_ANCHOR",
    "RESEARCH_ONLY",
}


class RegistryError(RuntimeError):
    pass


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _load_registry() -> dict:
    try:
        data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise RegistryError(f"missing registry: {REGISTRY_PATH.relative_to(ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise RegistryError(f"invalid registry JSON: {exc}") from exc
    if data.get("schema_version") != "1.0":
        raise RegistryError("unsupported registry schema_version")
    if data.get("directory") != "assets/style_refs/v2_current":
        raise RegistryError("registry directory mismatch")
    if not isinstance(data.get("assets"), list):
        raise RegistryError("registry assets must be a list")
    return data


def validate() -> None:
    registry = _load_registry()
    directory = ROOT / registry["directory"]
    if not directory.is_dir():
        raise RegistryError(f"reference directory missing: {directory.relative_to(ROOT)}")

    by_path: dict[str, dict] = {}
    ids: set[str] = set()
    for item in registry["assets"]:
        asset_id = item.get("asset_id")
        path = item.get("path")
        asset_class = item.get("asset_class")
        role = item.get("role")
        if not isinstance(asset_id, str) or not asset_id:
            raise RegistryError("asset_id is required")
        if asset_id in ids:
            raise RegistryError(f"duplicate asset_id: {asset_id}")
        ids.add(asset_id)
        if not isinstance(path, str) or not path:
            raise RegistryError(f"{asset_id}: path is required")
        if path in by_path:
            raise RegistryError(f"duplicate path: {path}")
        if asset_class not in ALLOWED_CLASSES:
            raise RegistryError(f"{asset_id}: invalid asset_class {asset_class}")
        if not isinstance(role, str) or not role:
            raise RegistryError(f"{asset_id}: role is required")
        expected_hash = item.get("sha256")
        if not isinstance(expected_hash, str) or len(expected_hash) != 64:
            raise RegistryError(f"{asset_id}: sha256 must be 64 hex chars")
        expected_size = item.get("size_bytes")
        if not isinstance(expected_size, int) or expected_size < 0:
            raise RegistryError(f"{asset_id}: invalid size_bytes")
        by_path[path] = item

    actual_paths = sorted(
        p.relative_to(ROOT).as_posix()
        for p in directory.iterdir()
        if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES
    )
    registered_paths = sorted(by_path)

    unregistered = sorted(set(actual_paths) - set(registered_paths))
    missing = sorted(set(registered_paths) - set(actual_paths))

    if unregistered:
        details = []
        for rel in unregistered:
            path = ROOT / rel
            details.append(f"{rel} sha256={_sha256(path)} size_bytes={path.stat().st_size}")
        raise RegistryError("unregistered current references: " + "; ".join(details))
    if missing:
        raise RegistryError("registered reference bytes missing: " + ", ".join(missing))

    for rel, item in by_path.items():
        path = ROOT / rel
        actual_hash = _sha256(path)
        actual_size = path.stat().st_size
        if actual_hash != item["sha256"]:
            raise RegistryError(
                f"{item['asset_id']}: sha256 mismatch expected={item['sha256']} actual={actual_hash}"
            )
        if actual_size != item["size_bytes"]:
            raise RegistryError(
                f"{item['asset_id']}: size mismatch expected={item['size_bytes']} actual={actual_size}"
            )

    canonical = {x["asset_id"] for x in registry["assets"] if x["asset_class"] == "PROJECT_CANONICAL"}
    for required in {"REF_V2_D", "REF_V2_E"}:
        if required not in canonical:
            raise RegistryError(f"required canonical reference not registered as PROJECT_CANONICAL: {required}")


def main() -> None:
    try:
        validate()
    except RegistryError as exc:
        print(f"REFERENCE_REGISTRY_FAIL: {exc}", file=sys.stderr)
        raise SystemExit(2)
    print("REFERENCE_REGISTRY_VALID")


if __name__ == "__main__":
    main()
