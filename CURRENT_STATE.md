# CURRENT_STATE.md

Updated: 2026-09-07
Repository: noru358/instatoon

## Production state — fresh E001 active

Execution authorization: **PRE_RASTER_DISPATCH_REQUIRED**.

Active episode: episodes/E001/README.md

Fresh E001 authority:
- L8 full L1-L7 package: **USER PASS** (`통과`);
- four-slide storyboard/cast/visual plan: **USER PASS** (`ㄱ`);
- current stage: **RENDER_CONTRACT_READY**;
- approved raster artifacts: **NONE**;
- the native-chat S01 generated outside the required state/media/geometry path is **REJECTED / NON-AUTHORITATIVE** and must not be reused as an anchor, repair source or QC artifact.

## Canonical render contract

Current style: **INSTATOON_STYLE_v2.0**.

Required production media for E001:
- `REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg`;
- `REF_V2_E_3PERSON_INDOOR_SCENE.jpeg`;
- `sub1.png` as a PROJECT_REUSABLE supplemental style reference.

The executable inventory is:
- `assets/style_refs/v2_current/registry.json`.

Current production is **BINARY_REQUIRED**:
- Git presence or prompt descriptions do not count as renderer conditioning;
- every required reference must be supplied as actual media to the eligible renderer;
- ASSET_PRODUCTION must pass the shared dispatch authorization contract before a provider/native renderer is called;
- screen-bearing slides must have physically valid subject/display/camera geometry before dispatch.

## Canonical operating mode — MANUAL_VALIDATION

Standard topology:
`pre-raster content/plan → S01 USER anchor → S02..final OPERATOR INTERNAL QC → complete text-free raster-set USER gate → lettering/final USER gate`.

One slide = one image file.
One slide != one user approval gate.

## Current blocker

`CHAT_NATIVE_REFERENCE_BRIDGE`: the repository contains and verifies the required D/E/sub1 binaries, but a native ChatGPT image render is canonical only if those exact binaries are actually supplied to the renderer in the active tool path.

Do not claim BINARY_CONDITIONED based on repository inspection alone.

## Exact next action

1. Validate this active E001 package and repository contracts in CI.
2. Make the exact D/E/sub1 reference binaries available to an eligible renderer.
3. Authorize the E001 S01 asset dispatch with bound media evidence and the physical phone geometry contract.
4. Generate **S01 only**.
5. Present S01 for the USER anchor gate.
