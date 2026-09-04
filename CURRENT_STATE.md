# CURRENT_STATE.md

# Current state — 2026-09-04

## Project
Repository: `noru358/instatoon`

Purpose:
Build a semi-automated Instagram-toon production system whose durable identity comes from **the overall illustration style + visual grammar**, not from recurring-character identity.

This project is independent from the Talkshow video pipeline.

---

## Current phase

### Big flow
**Foundation → visual-language + sequential-grammar lock → prototype extraction**

### Current detailed step
The canonical art style is now hardened as `INSTATOON_STYLE_v1.1`, and the episode/page grammar is now locked as `INSTATOON_VISUAL_GRAMMAR_v0.1`.

The production architecture is defined in `TOON_SYSTEM_V0_1.md`.

---

## Canonical decisions

1. This project is separate from the Talkshow repository and video workflow.
2. **Recurring character identity is not the primary lock.**
3. The project identity is primarily:
   - overall illustration style;
   - sequential/page visual grammar;
   - editorial voice;
   - vector lettering/layout system.
4. `STYLE_LOCK.md` controls how illustrations look.
5. `VISUAL_GRAMMAR.md` controls how an episode reads across slides and how pages are structured.
6. The planning unit is the **entire episode**.
7. Individual slides are rendered only after the whole episode plan is coherent.
8. All important text, speech bubbles, labels, arrows, emphasis and SFX are separate editable vector layers.
9. Community/news/personal material is a **source mode**, not an output format.
10. v0.1 active narrative formats are deliberately narrow:
    - `STORY_ARC` — anecdotes / experiences / incidents
    - `RELATABLE_SCENARIO` — dramatized everyday relatability
    - `OBSERVATION_SET`, `EXPLAINER_CAUSAL`, and `CONTRAST_REFRAME` are dormant/future expansion.
11. Paid image generation is used only when illustration materially improves the slide.
12. Multi-agent debate/swarm architecture is not the default. One orchestrator + typed stages + deterministic validation is preferred to reduce token cost and drift.
13. Human taste approval stays explicit during v0.1.
14. Performance feedback may suggest experiments but cannot silently mutate style or visual grammar.

---

## Research-driven grammar notes

A 2024 Chosun University study of Instatoon visual direction identifies **simplicity** and **clarity** as the dominant visual characteristics: simplified character/background treatment, restrained visual elements, regular readable layouts, clear typography, and reduced clutter.

Observed Instagram carousel-comic practice also reinforces:
- slide 1 as a swipe hook rather than a summary;
- one meaningful beat per slide;
- sequential reveal across swipes;
- deliberate payoff/landing;
- high phone readability;
- avoiding over-dense multi-panel subdivision.

These findings align with the existing warm, low-density style lock.

---

## Current authoritative hierarchy

1. `STYLE_LOCK.md` — illustration style authority
2. `VISUAL_GRAMMAR.md` — episode/page/sequential grammar authority
3. `STORY_GRAMMAR.md` — active v0.1 anecdote/relatable editorial grammar
4. `SOURCE_STORY_PIPELINE.md` — source selection → whole-story planning flow
5. `TOON_SYSTEM_V0_1.md` — production-system architecture and data flow
6. `MASTER_PROMPTS.md` — canonical style prompt blocks
7. `GENERATION_PROTOCOL.md` — execution/QC procedure
8. `REFERENCE_ANALYSIS.md` — style-analysis rationale
9. `CURRENT_STATE.md` — current handoff / next action
10. episode-specific content and prompts

---

## Immediate next work

Do **not** build recurring character masters as the next mandatory step.

Instead:

1. Build three prototype episodes focused only on the active v0.1 editorial scope:
   - one sourced anecdote/incident using `STORY_ARC`;
   - one error/misunderstanding/embarrassment story using `STORY_ARC`;
   - one everyday `RELATABLE_SCENARIO`.
2. For each prototype:
   - create CONTENT_MASTER;
   - select angle;
   - route format;
   - write the entire swipe script;
   - create the entire visual plan;
   - assign page archetype + render mode per slide;
   - pass whole-episode preflight;
   - render cover + one representative body slide first;
   - if style/grammar passes, render remaining required art;
   - add vector lettering;
   - QC;
   - human taste review.
3. Use those prototypes to verify:
   - recurring page archetypes;
   - useful text-density ranges;
   - vector components;
   - actual image-generation count;
   - regeneration rate;
   - where automation saves time vs hurts taste.
4. Then finalize machine-readable JSON schemas and implement the deterministic vector renderer.

P002 is no longer the preferred first prototype because it is mainly a social/market phenomenon rather than the v0.1 target of anecdote/experience/incident/relatable storytelling. Keep it as a future-format candidate.


---

## Prototype execution update — 2026-09-04

First real source-gate run completed:
- research pool saved at `research/SOURCE_CANDIDATE_RUN_001.md`;
- E001 selected: convenience-store “poet” anecdote;
- `episodes/E001/STORY_SOURCE_PACK.md` created;
- `CONTENT_MASTER.json` created;
- `STORY_PLAN.json` created;
- `EPISODE_PLAN.json` created.

E001 whole-story / whole-visual plan passed into raster preflight, but Slide 1 and Slide 5 were **rejected for systemic visual-style drift**.

Current production state:
1. **STOP bulk generation.**
2. Preserve/verify the actual canonical style-reference image(s) as repository assets.
3. Retry Slide 1 with the canonical image as primary style authority + STYLE v1.1 hardening.
4. Only after Slide 1 passes, retry Slide 5 with canonical style reference + accepted Slide 1 as continuity aid.
5. Only then render remaining slides.


### E001 style-preflight diagnosis
The first two generated frames matched scene semantics but failed the visual identity:
- generic white-eye/pupil construction;
- textured/strand-heavy hair;
- paper/grain/pencil-like texture;
- excessive shading;
- atmospheric convenience-store lighting;
- over-detailed retail background;
- overall generic GPT/editorial/anime-adjacent finish.

Root cause: the production render used summarized text instead of the true canonical style reference; Slide 5 then inherited Slide 1's already-wrong style.

**Current blocker:** there is no verified canonical style-reference image binary in the inspected repository tree. Text-only style documentation is not considered lossless production authority.
