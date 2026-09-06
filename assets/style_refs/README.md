# STYLE REFERENCE ASSET MAP

## Current v2 assets

Use the files under `v2_current/` as current production authorities:

- `REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg` — canonical main-cast identity, full-body, gesture and expression sheet;
- `REF_V2_E_3PERSON_INDOOR_SCENE.jpeg` — positive scene-level reference for the three leads, interior background, furniture/props and multi-person interaction;
- `sub1.png` — user-supplied PROJECT_REUSABLE supplemental style reference. Secondary only; not a replacement for D/E.

The second file is not a contamination example.

## Legacy root assets

The five `INSTATOON_REF_*` image files stored directly in this directory belong to the retired pre-reset INSTATOON v1.x visual style.

Current production uses INSTATOON_STYLE_v2.0.

Do not:
- attach these files as current style authority;
- fall back to them when current v2 references are unavailable;
- infer current face/eye/color grammar from them.

See `../../REFERENCE_SET.md` for exact current paths, dimensions, hashes and remaining binary gaps.

These binaries are retained only as historical evidence until a future cleanup/migration explicitly relocates or removes them.

## Machine registry

`v2_current/registry.json` is the executable inventory of current v2 reference binaries.

Adding a file to `v2_current/` is not enough to make it silently usable. The file must have:
- an asset ID;
- reuse class;
- role;
- SHA-256;
- byte size.

CI fails on unregistered, missing, or modified current-reference binaries.
