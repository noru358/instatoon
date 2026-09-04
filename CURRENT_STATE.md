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
The canonical art style is locked as `INSTATOON_STYLE_v1.0`, and the episode/page grammar is now locked as `INSTATOON_VISUAL_GRAMMAR_v0.1`.

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
10. v0.1 narrative formats are:
    - `STORY_ARC`
    - `OBSERVATION_SET`
    - `EXPLAINER_CAUSAL`
    - `CONTRAST_REFRAME`
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
3. `TOON_SYSTEM_V0_1.md` — production-system architecture and data flow
4. `MASTER_PROMPTS.md` — canonical style prompt blocks
5. `GENERATION_PROTOCOL.md` — execution/QC procedure
6. `REFERENCE_ANALYSIS.md` — style-analysis rationale
7. `CURRENT_STATE.md` — current handoff / next action
8. episode-specific content and prompts

---

## Immediate next work

Do **not** build recurring character masters as the next mandatory step.

Instead:

1. Build three prototype episodes representing different narrative topologies.
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

The first prototype may later use P002 material, but the system design is not coupled to P002.
