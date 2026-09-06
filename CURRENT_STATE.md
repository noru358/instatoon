# CURRENT_STATE.md

Updated: 2026-09-06
Repository: noru358/instatoon

Active episode: episodes/E007/README.md

## Canonical operating mode — MANUAL_VALIDATION

Current STANDARD user-facing approval topology:

`pre-raster content/storyboard/contracts → S01 USER anchor → S02..final OPERATOR INTERNAL QC → complete text-free raster-set USER gate → lettering/final USER gate`.

Hard distinction:
- **one slide = one image file**;
- **one slide != one user approval gate**.

After S01 USER PASS, S02 through the final slide are produced sequentially as separate files and QC'd internally by the operator/runtime. The user normally returns only when the complete text-free raster set is ready.

If a local frame fails, repair/retry it internally. Ask the user before the full-set gate only when a material story/cast/style/contract decision cannot be resolved without taste input.

AUTO_FINISH remains experimental and separate: it keeps the S01 USER gate, then intentionally bypasses later STANDARD human gates using automatic QC/lettering/final QC.

## E007 current state

Approved:
- fresh L1-L7 source/story/dialogue package;
- Harin as protagonist;
- seven-slide storyboard;
- L11/L12 visual plan;
- L12.5 EPISODE_PLAN / RENDER_MANIFEST / LETTERING_PLAN;
- canonical reference authority REF_V2_D + REF_V2_E;
- S01 visual direction / Harin identity / overall quality;
- 2026-09-06 global visual-direction / expression rule lock.

S01 known exception:
- the user explicitly chose to proceed even though readable raster text/signage was baked into the native image;
- this remains a known contract defect and is NOT reclassified as text-free compliant;
- the chat-native S01 is a visual/taste anchor only because it has no repository attempt/artifact hash.

Clean-context recovery:
- the previous S02 WRONG_SCENE blocker was resolved in a clean session after actual REF_V2_D + REF_V2_E media were restored;
- S02-S07 chat-native prototypes were produced and used to validate/refine global visual rules;
- those prototypes are not being falsely recorded as machine-bound raster artifacts.

Approved structural visual rules:
- whole-episode shot direction is planned/QC'd as a viewer-perceived sequence;
- do NOT hard-code left/right/front quotas or a mandatory opposite-facing frame;
- when multiple story-valid shots exist, choose among alternatives using story clarity + continuity + redundancy awareness across camera side/height, shot distance, body orientation, face orientation and gaze;
- a frontal camera is not automatically direction-neutral if the rendered face still appears repeatedly turned the same way;
- expression amplitude is role-adaptive: anti-grotesque / anti-melodrama must not become a global low-energy acting lock;
- story-relevant mirrors/reflections require plausible geometry;
- supporting characters share the same flat local-color grammar as the main cast and do not receive an automatic yellow/sepia skin cast.

Machine state:
- PRODUCTION_STATE.current_stage = REMAINING_RENDER;
- no COMPLETE_TEXT_FREE_RASTER_SET USER PASS has been persisted;
- rule approval does not equal raster-set approval;
- next normal user gate remains COMPLETE_TEXT_FREE_RASTER_SET.

## Reference binding

Required canonical binaries for production raster:
- `assets/style_refs/v2_current/REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg`
  - SHA-256 `dbddf458a97c89781075e6be03ab2c393eff75b95e8856f044bd81f29310ec07`
- `assets/style_refs/v2_current/REF_V2_E_3PERSON_INDOOR_SCENE.jpeg`
  - SHA-256 `b49683276f94ba5621e3602d7e3d714b0f2e637b2c41fc1fd132bdf6f336b049`

Both are BINARY_REQUIRED for canonical production.
The user-uploaded copies supplied during E007 matched these repository binaries.

## Contract / state reconciliation completed

Current policy and implementation are aligned across:
- README.md;
- GENERATION_PROTOCOL.md;
- SETUP_RENDER.md;
- SOURCE_STORY_PIPELINE.md;
- VISUAL_GRAMMAR.md;
- WORKFLOW_PROTOCOL.md;
- AUTOMATION_TRANSITION.md;
- production/render schemas;
- render_guard / render / AUTO_FINISH paths;
- GitHub QC workflow;
- E007 README / manifest / lettering plan / production state.

Important implementation changes:
- new `RASTER_SET_QC_PENDING` machine stage;
- S01 frame PASS is distinguished as `inspector=USER`;
- S02+ standard manual frame QC may use `inspector=OPERATOR_INTERNAL`;
- all raster frame PASSes now lead to a complete-raster-set USER gate before LETTERING;
- conversation-inferred canonical policy is `FIRST_FRAME_USER_GATE_THEN_SEQUENTIAL_INTERNAL_QC`;
- E007 LETTERING_PLAN was rebound to the current EPISODE_PLAN blob after the S01 extra-identity contract changed.

Validation:
- render-guard unit tests: PASS;
- active E007 render-contract validation: PASS;
- pipeline-contract compile/regression/lettering smoke checks: PASS.

## Exact next action

Resume E007 from the current MANUAL_VALIDATION state using the newly locked visual-direction policy.

1. restore this file + E007 README / EPISODE_PLAN / RENDER_MANIFEST / LETTERING_PLAN / PRODUCTION_STATE;
2. restore actual REF_V2_D + REF_V2_E media;
3. use the active E007 visual_direction policy when producing/repairing any remaining canonical raster:
   - story-first shot selection;
   - no fixed direction quotas;
   - sequence-level perceptual redundancy check;
   - role-adaptive expression amplitude;
   - reflection geometry QC where relevant;
   - supporting-character skin/local-color coherence;
4. do not ask for per-slide user approval by default;
5. present the complete text-free raster set for USER review when canonical frame artifacts are ready;
6. only after that USER PASS, apply LETTERING_PLAN and present the finished episode for final USER review.
