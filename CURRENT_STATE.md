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

After S01 USER PASS, S02 through the final slide are produced sequentially as separate files and QC'd internally by the operator/runtime. The user normally returns only when the complete text-free raster set is ready.

If a local frame fails, repair/retry it internally. Ask the user before the full-set gate only when a material story/cast/style/contract decision cannot be resolved without taste input.

AUTO_FINISH remains experimental and separate.

## User-directed episode reset — 2026-09-06

The user reset all concrete episode content and restarted numbering from E001.

Retired from current execution:
- all prior E001-E007 premises and source packs;
- dialogue/storyboards/cast choices specific to those episodes;
- episode render contracts, production states, approvals, raster outputs, lettering outputs and final artifacts.

Preserved:
- repository-wide workflow;
- style and reference authority;
- visual grammar;
- QC/repair rules;
- sequence-direction/expression rules;
- automation/render-guard improvements;
- structural lessons from prior production.

Git history is the archive for retired episode-specific material. Current work must not recover or reuse a retired premise merely because an old episode directory existed.

## E001 current state

- Fresh reset episode.
- Stage = L1_SOURCE_DISCOVERY.
- HUMAN-SOURCE-FIRST applies.
- L8 USER VOICE GATE has not been reached.
- No current storyboard, cast routing, episode-local character design, visual plan, render contract or raster artifact exists.
- L13 raster generation is blocked until all canonical prior gates pass.

## Reference binding

Canonical production references remain:
- `assets/style_refs/v2_current/REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg`
- `assets/style_refs/v2_current/REF_V2_E_3PERSON_INDOOR_SCENE.jpeg`

These remain BINARY_REQUIRED where the renderer supports canonical production conditioning.

## Exact next action

1. Run fresh L1 SOURCE DISCOVERY / COLLECTION.
2. Continue L2-L7 in canonical order.
3. Present the accepted L1-L7 package at L8 and STOP for explicit user approval.
4. Only after L8 PASS proceed to L10-L12.5, then S01 anchor generation under MANUAL_VALIDATION.
