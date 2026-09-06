# CURRENT_STATE.md

Updated: 2026-09-07
Repository: noru358/instatoon

## Production state — reset complete

Execution authorization: **PENDING_L8_USER_GATE**.

Active episode: NONE

Canonical reset:
- all concrete pre-redesign episode content is retired;
- legacy E001 is preserved at `archive/pre_redesign/E001/` only as non-authoritative failure/test evidence;
- production numbering restarts from a fresh E001;
- project-wide workflow, style, reference, screen/UI, cultural-context and QC rules remain active through their canonical authority files;
- render and auto-finish execution must fail closed while no active episode exists.

## Completed
- the approved creative baseline remains in the canonical project authority files;
- AutoPipeline durable artifact bridge and PROJECT/EPISODE work-scope separation are already merged;
- `Active episode: NONE` is supported as a valid idle state;
- the renderer explicitly refuses implicit execution while production is idle;
- the old E001 package has been removed from `episodes/` and archived without rewriting its evidence;
- canonical v2 style reference bytes remain materialized in `assets/style_refs/v2_current/`.

## Canonical operating mode — MANUAL_VALIDATION

Standard topology:
`pre-raster content/plan → S01 USER anchor → S02..final OPERATOR INTERNAL QC → complete text-free raster-set USER gate → lettering/final USER gate`.

One slide = one image file.
One slide != one user approval gate.

## Fresh E001 pending L8

- L1-L7 package: `research/PENDING_L8.md`
- Primary human source: https://theqoo.net/job/4123344083
- Status: **L1-L7 COMPLETE / NOT USER-APPROVED**.
- Active episode remains `NONE`.

Do not storyboard, render or create an active episode package before the L8 user gate.

## Exact next action

Present `research/PENDING_L8.md` to the user and wait for explicit L8 approval.
Only after L8 PASS continue to L10 storyboard/cast routing and create/activate the fresh `episodes/E001` package at the appropriate contract stage.
