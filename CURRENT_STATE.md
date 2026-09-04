# CURRENT_STATE.md

# Current state — 2026-09-04

## Project

Repository: `noru358/instatoon`

Purpose: build a semi-automated Instagram-toon production system whose durable identity comes from **the overall illustration style + visual grammar**, not from recurring-character identity.

This project is independent from the Talkshow repository and video workflow.

---

## Current phase

### Big flow

**Foundation complete → style / story / visual grammar locked → prototype extraction in progress → implementation later**

### Current detailed step

Prototype E001 has a complete source pack, content master, whole-story plan, and whole-episode visual plan.

Its first Slide 1 / Slide 5 raster preflight was rejected for systemic style drift. The root blocker is now resolved: `INSTATOON_STYLE_v1.2` and the five approved binary style references are present in the repository.

**Exact current position: E001 two-slide raster preflight, ready to retry Slide 1.**

Do not start bulk rendering, Prototype 2, or software implementation before the E001 retry gate is resolved.

---

## Canonical decisions

1. `STYLE_LOCK.md` defines the normative illustration language and pass/fail boundary.
2. `REFERENCE_SET.md` identifies the approved binary render anchors. A production render must attach the relevant approved reference; prose is reinforcement, not a substitute.
3. `VISUAL_GRAMMAR.md` controls how a complete episode reads across slides and how pages are structured.
4. The planning unit is the **entire episode**; the rendering unit is the **slide**.
5. The project identity is primarily:
   - overall illustration style;
   - sequential/page visual grammar;
   - editorial voice;
   - vector lettering/layout system.
6. Recurring characters are optional content assets, not the primary brand lock or the next mandatory build step.
7. All important text, speech bubbles, labels, arrows, emphasis, and SFX remain separate editable vector layers.
8. Community/news/personal material is a source mode, not an output format.
9. Active v0.1 formats are:
   - `STORY_ARC` — anecdotes / experiences / incidents;
   - `RELATABLE_SCENARIO` — dramatized everyday relatability.
10. `OBSERVATION_SET`, `EXPLAINER_CAUSAL`, and `CONTRAST_REFRAME` remain dormant/future formats.
11. Use paid image generation only when illustration materially improves the slide. Explicit user approval is required immediately before spending external tool credits.
12. v0.1 uses one orchestrator, typed stage outputs, and deterministic validation where possible. It is not a multi-agent debate/swarm system.
13. Human approval remains explicit for the topic/angle, whole-episode plan, final taste/publish decision, and any style/grammar version change.
14. Performance feedback may suggest experiments but may not silently mutate style or visual grammar.

The complete authority order is maintained once in `README.md`; do not duplicate or fork it here.

---

## Implementation reality

The repository currently contains the design baseline, canonical references, one research run, and one partially executed prototype.

### Proven at process level

- source candidate filtering and Human-interest Gate;
- source normalization;
- angle / format / story-shape routing;
- whole-episode beat planning;
- whole-episode visual direction;
- two-slide cost-protection preflight;
- manual visual failure diagnosis and stop-on-systemic-failure behavior.

### Not yet implemented as software

- executable orchestrator;
- finalized machine-readable JSON Schemas;
- deterministic plan validator;
- prompt-assembler code;
- vector letterer/composer;
- `RENDER_MANIFEST.json` production logging;
- automated deterministic QC;
- publishing and performance-feedback ingestion.

Therefore the current system is a **structured, manually operated production protocol under prototype validation**, not an end-to-end automation application.

---

## Prototype program

The v0.1 extraction program uses three prototypes:

1. a sourced anecdote/incident using `STORY_ARC` — **E001, active**;
2. an error/misunderstanding/embarrassment story using `STORY_ARC` — pending;
3. an everyday `RELATABLE_SCENARIO` — pending.

Use the three prototypes to discover stable page archetypes, useful text-density ranges, reusable vector components, real image-generation counts, regeneration rates, and the points where automation saves time or damages taste.

P002 is not the preferred first prototype because it is primarily a social/market phenomenon rather than a v0.1 anecdote/experience/incident/relatable story. Keep it as a future-format candidate.

After all three prototypes, finalize schemas and implement the deterministic vector renderer, prompt assembler, render manifest, and deterministic QC in the order defined by `TOON_SYSTEM_V0_1.md`.

---

## E001 — current production state

Episode: convenience-store “poet” anecdote

Completed artifacts:

- `research/SOURCE_CANDIDATE_RUN_001.md`;
- `episodes/E001/STORY_SOURCE_PACK.md`;
- `episodes/E001/CONTENT_MASTER.json`;
- `episodes/E001/STORY_PLAN.json`;
- `episodes/E001/EPISODE_PLAN.json`.

Gate state:

- Gate A: E001 selected as `GO` in the research run.
- Gate B: the complete plan proceeded into an authorized two-slide render preflight; the exact approval wording was not preserved, so do not claim a verbatim approval record.
- Render preflight: first attempt rejected; retry ready.
- Gate C: not reached.

### Historical failed preflight

Slide 1 and Slide 5 matched most scene semantics but failed the project visual identity:

- generic white-eye/pupil construction;
- textured/strand-heavy hair;
- paper/grain/pencil-like surface;
- excessive shading and atmospheric lighting;
- over-detailed convenience-store background;
- generic GPT/editorial/anime-adjacent finish;
- failed Slide 1 then contaminated Slide 5 as a style anchor;
- Slide 5 also showed two prematurely bitten/notched ice bars and a weak handoff.

Root cause: the renders used summarized style prose instead of an approved canonical binary style reference, then propagated the failed frame.

The failed output IDs, hashes, and detailed evidence remain in `episodes/E001/README.md`.

### Resolution

The blocker is resolved through:

- `INSTATOON_STYLE_v1.2`;
- five approved assets under `assets/style_refs/`;
- `FACE_LOCK_BLOCK`;
- `BACKGROUND_DENSITY_LOCK`;
- production-wide `ANTI_GPT_DEFAULT_BLOCK`;
- prohibition on using a failed frame as the sole style anchor.

The two earlier recovered PNG candidates recorded in previous history were never promoted to repository-canonical assets. They are superseded by the five approved WebP references in `REFERENCE_SET.md`; their old local-only status is not a current blocker.

---

## Exact next execution

1. Keep bulk generation stopped.
2. Before any external paid render, obtain explicit user approval for the spend.
3. Retry **Slide 1 only** under `INSTATOON_STYLE_v1.2`:
   - primary scene anchor: `INSTATOON_REF_04_INDOOR.webp`;
   - face support: `INSTATOON_REF_01_CHARACTER.webp`;
   - append reference-obedience, face-lock, background-density, master-style, negative-style, and anti-GPT-default blocks;
   - preserve the planned top negative space and generate no semantic text.
4. Run style/visual-grammar QC before defect QC.
5. If Slide 1 fails, diagnose and repair the shared prompt/reference system; do not generate Slide 5.
6. If Slide 1 passes, retry **Slide 5 only**:
   - primary scene anchor: `INSTATOON_REF_03_INTERACTION.webp`;
   - face support: `INSTATOON_REF_01_CHARACTER.webp`;
   - accepted Slide 1 may be used only as episode-local identity/location continuity support;
   - show the customer placing exactly two opened, unbitten ice bars into the worker's hands, one bar per hand.
7. Only after Slide 1 and Slide 5 both pass may the remaining raster slides receive a first pass.
8. Then add vector lettering, run QC, and request Gate C: `PUBLISH / REPAIR / KILL`.

Current blocker: **none inside the repository**. The next gate is execution approval and Slide 1 visual QC.
