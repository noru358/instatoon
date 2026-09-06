# CURRENT_STATE.md

Updated: 2026-09-07
Repository: noru358/instatoon

## Production state — fresh E001 active

Execution authorization: **CLEAN_RENDER_HANDOFF_REQUIRED**.

Active episode: episodes/E001/README.md

Fresh E001 authority:
- L8 full L1-L7 package: **USER PASS** (`통과`);
- four-slide storyboard/cast/visual plan: **USER PASS** (`ㄱ`);
- S01 visual direction: **USER PASS / CONTEXT-LOCAL TASTE ANCHOR** (`합격!`);
- S01 is not repository-bound as a machine-authoritative raster artifact;
- the S02-S04 images produced after the render context had already crossed the isolation-failure threshold are **REJECTED / QUARANTINED**;
- machine state remains `FIRST_FRAME_QC_PENDING`;
- machine-authoritative approved raster artifacts: **NONE**.

## Canonical visual/runtime authority

Current style: **INSTATOON_STYLE_v2.1**.
Canonical generation wording: **MASTER_PROMPTS v2.5**.
Canonical production/QC method: **GENERATION_PROTOCOL v2.6**.

Required production media for E001:
- `REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg`;
- `REF_V2_E_3PERSON_INDOOR_SCENE.jpeg`;
- `sub1.png` as the supplemental style reference required by the active render manifest;
- the exact user-approved S01 image when resuming S02+ as a context-local continuity/taste anchor.

Executable reference inventory:
- `assets/style_refs/v2_current/registry.json`.

Current production is **BINARY_REQUIRED**:
- repository presence or prompt descriptions do not count as renderer conditioning;
- every manifest-required reference must be supplied as actual media to the eligible renderer;
- screen-bearing slides must preserve physically valid subject/display/camera geometry.

## Canonical operating mode — MANUAL_VALIDATION

Standard topology:

`pre-raster content/plan → S01 USER anchor → S02..final OPERATOR INTERNAL QC → complete text-free raster-set USER gate → lettering/final USER gate`.

One slide = one image file.
One slide != one user approval gate.

## Latest rejected set — why it failed

The later S02-S04 candidates are not production assets.

Set-level failures:
- viewer-perceived camera/face/body rhythm remained too biased toward the same safe portrait family;
- S02 → S03 visual delta was weaker than the story-state change;
- S03's loss cue read too much like generic floating data/icons instead of a concrete accumulated archive being lost;
- S04 had a visible shoulder/torso/arm continuity failure on the character's right side;
- S04 changed the intended semantic acting from hollow, resigned crying-laughter into a brighter/cuter laugh;
- body language in S04 did not sufficiently carry depleted resignation.

The E001 plan/manifest has been revised so these are now explicit render/QC requirements rather than chat-only feedback.

## Current blocker

Blocker: `NATIVE_CONVERSATION_RENDER_ISOLATION`
Status: **OPEN / STICKY FOR THE OLD CONTEXT**

The prior render context crossed the hard-failure threshold after repeated multi-panel/full-episode reinterpretation of a single-slide request.

A later superficially valid single-panel output in that same context does **not** clear the blocker.
Outputs generated after the sticky-unsafe point are quarantined from anchor/QC promotion.

Context reset is not episode reset.

## Exact next action

1. Start a **clean dedicated render session/context**.
2. Read this file, `GENERATION_PROTOCOL.md`, `MASTER_PROMPTS.md`, the active E001 plan/manifest/state, and validate repository authority.
3. Supply the exact D/E/sub1 media plus the user-approved S01 image as actual media.
4. Resume at **S02**, not S01.
5. Compile/render **current-shot only**: S02 → internal QC → S03 → internal QC → S04 → internal QC.
6. Do not ask for intermediate user approval.
7. Present the complete four-image, text-free set only after S02-S04 all pass internal frame + sequence QC.

Do not use any rejected S02-S04 image as a reference, repair base, composition seed or continuity anchor.
