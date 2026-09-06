# CURRENT_STATE.md

Updated: 2026-09-07
Repository: noru358/instatoon

## Production state — fresh E001 active

Execution authorization: **RENDER_CONTEXT_BLOCKED_AFTER_S01_VISUAL_PASS**.

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

S01 visual direction is **USER PASS** in the active conversation, but it is not repository-bound as a machine-authoritative artifact.

After that approval, two consecutive native-chat S02 attempts violated slide isolation by producing multi-panel/full-episode outputs.

Blocker:
- `NATIVE_CONVERSATION_RENDER_ISOLATION`
- status: **OPEN**
- classification: renderer-context isolation failure, not story/style approval failure.

Do not retry S02 again in the same conversation context.

## Exact next action

1. Continue in a **clean dedicated render session/context**.
2. Re-attach/materialize the approved S01 image plus exact D/E/sub1 binaries as actual media.
3. Resume from **S02**, not S01.
4. Generate S02 → S03 → S04 sequentially with internal QC.
5. Return to the user only at the **complete text-free raster-set gate**, unless a new systemic blocker occurs.
