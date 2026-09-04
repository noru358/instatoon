# CURRENT_STATE.md

# Current state — 2026-09-04

## Project
Repository: `noru358/instatoon`

Purpose:
Build a semi-automated pipeline for Instagram-toon / shorts-toon content. The immediate focus is not full automation; it is first creating a stable, reproducible visual standard that can later survive automation.

---

## Current phase

### Big flow
**Foundation / visual-language lock**

### Current detailed step
The first canonical style has been reverse-engineered from supplied comic references and formalized as `INSTATOON_STYLE_v1.0`.

### Done this turn
- created authoritative repository hierarchy
- locked style DNA
- documented detailed reference analysis
- created canonical master prompt
- created negative prompt
- created identity-preservation block
- created reference-obedience block
- created scene template
- created generation/QC protocol
- added change-control / versioning rules

---

## Canonical decisions

1. This project is separate from the existing Talkshow repository and style.
2. The visual style is a warm, restrained, low-detail everyday anecdote comic.
3. Generic "Korean webtoon" prompting is prohibited as a primary style descriptor because it commonly causes romance-webtoon/anime drift.
4. The five most critical style variables are:
   - tiny/simple face grammar
   - thin charcoal-brown line
   - broad near-black hair masses
   - warm muted palette
   - almost-flat low-density rendering
5. "Prettier" is not automatically "better." Over-polish is a known failure mode.
6. STYLE_LOCK.md is the highest authority.
7. Lower-level prompts may add content but cannot redefine style.
8. Style changes require explicit versioned approval.

---

## Next logical work

1. Create one canonical recurring character in the locked style.
2. Generate a small A/B style test set across:
   - bust portrait
   - full body
   - two-person interaction
   - simple interior
   - simple exterior
3. QC against hard-fail rules.
4. Refine only if failures are systematic.
5. Lock character master sheet(s).
6. Then design the production pipeline:
   source/idea → story restructuring → script → panel plan → image generation → QC → lettering/layout → shorts adaptation → distribution/performance feedback.

The pipeline should be built only after visual reproducibility is demonstrated.
