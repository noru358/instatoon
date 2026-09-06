# CURRENT_STATE.md

Updated: 2026-09-06
Repository: noru358/instatoon

Active episode: episodes/E001/README.md

## Canonical operating mode — MANUAL_VALIDATION

Current STANDARD user-facing approval topology:

`pre-raster content/storyboard/contracts → S01 USER anchor → S02..final OPERATOR INTERNAL QC → complete text-free raster-set USER gate → lettering/final USER gate`.

Hard distinction:
- **one slide = one image file**;
- **one slide != one user approval gate**.

After S01 USER PASS, S02 through the final slide are produced sequentially as separate files and QC'd internally by the operator/runtime.

## User-directed episode reset — 2026-09-06

All concrete prior E001-E007 episode content is retired from current execution.
Repository-wide workflow, style/reference authority, visual grammar, QC/repair rules, sequence-direction/expression rules and automation improvements remain active.
Git history is the archive for retired episode-specific material.

## E001 current state

- L1-L7 revised package: PASS.
- L8 USER VOICE GATE: PASS; user explicitly replied "합격".
- L10 storyboard + cast routing: COMPLETE.
- L11 episode-local character design: COMPLETE internally.
- L12 whole-episode visual plan: COMPLETE.
- L12.5 EPISODE_PLAN / RENDER_MANIFEST / LETTERING_PLAN: MATERIALIZED.
- PRODUCTION_STATE.current_stage = VISUAL_PLAN_READY.
- Current checkpoint = PRE_RASTER_PLAN_USER_GATE.
- Raster generation remains fail-closed until this gate passes.

Cast:
- no recurring main cast forced into the premise;
- worker_01 is an episode-only mid-20s service worker across all seven slides;
- customer/helper coworker are one-frame extras.

Ending lock:
- no protagonist explanation after the private DM;
- no ending narration/internal monologue;
- S07 contains no lettering at all and lands only through extreme embarrassment body language.

## Reference binding

Canonical production references remain:
- `assets/style_refs/v2_current/REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg`
  - SHA-256 `dbddf458a97c89781075e6be03ab2c393eff75b95e8856f044bd81f29310ec07`
- `assets/style_refs/v2_current/REF_V2_E_3PERSON_INDOOR_SCENE.jpeg`
  - SHA-256 `b49683276f94ba5621e3602d7e3d714b0f2e637b2c41fc1fd132bdf6f336b049`

Both remain BINARY_REQUIRED for canonical L13 production.

## Exact next action

Present the seven-slide pre-raster package to the user.
STOP for explicit approval.
After PASS, advance/rebind the render contract, run full guard validation, then supply actual REF_V2_D + REF_V2_E media and generate only S01 for the USER anchor gate.
