# CURRENT_STATE.md

# Current state — 2026-09-04

## Project

Repository: `noru358/instatoon`

Purpose: build a semi-automated Instagram-toon production system whose durable identity comes from **the overall illustration style + visual grammar**, not from recurring-character identity.

This project is independent from the Talkshow repository and video workflow.

---

## Current phase

### Big flow

**Foundation complete → style / story / visual grammar locked → Prototype 1 complete at Gate C → two more prototypes → implementation**

### Current detailed step

Prototype E001 now has a complete source pack, content master, whole-story plan, whole-episode visual plan, seven generated art layers, seven editable SVG narrative layers, seven canonical exports, a contact sheet, and a render manifest.

The clean Slide 1 retry passed; Slide 5 then passed the high-risk interaction/object-count check; the remaining five slides received one first pass each. The complete carousel passed technical and story-sequence QC with two style/continuity watch items documented in the manifest.

**Exact current position: E001 first complete carousel, awaiting Gate C human taste decision (`PUBLISH / REPAIR / KILL`).**

Do not silently promote the texture variation into a new style rule, start Prototype 2, or implement the renderer before the Gate C decision is recorded.

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

The repository currently contains the design baseline, canonical references, one research run, and one fully executed first prototype awaiting human taste approval.

### Proven at process level

- source candidate filtering and Human-interest Gate;
- source normalization;
- angle / format / story-shape routing;
- whole-episode beat planning;
- whole-episode visual direction;
- two-slide cost-protection preflight;
- manual visual failure diagnosis and stop-on-systemic-failure behavior;
- one full seven-slide raster-plus-vector carousel;
- episode-local SVG lettering and deterministic 1080×1350 export;
- manual `RENDER_MANIFEST.json` logging and deterministic file/dimension/vector-bound checks.

### Not yet implemented as software

- executable orchestrator;
- finalized machine-readable JSON Schemas;
- deterministic plan validator;
- prompt-assembler code;
- reusable vector letterer/composer (only the episode-local SVG proof exists);
- automated `RENDER_MANIFEST.json` production logging (the E001 manifest was written manually);
- automated deterministic QC;
- publishing and performance-feedback ingestion.

Therefore the current system is a **structured, manually operated production protocol under prototype validation**, not an end-to-end automation application.

---

## Prototype program

The v0.1 extraction program uses three prototypes:

1. a sourced anecdote/incident using `STORY_ARC` — **E001, first pass complete / Gate C pending**;
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
- `episodes/E001/EPISODE_PLAN.json`;
- `episodes/E001/RENDER_MANIFEST.json`;
- seven art layers under `episodes/E001/renders/`;
- seven editable SVG layers under `episodes/E001/vector/`;
- seven canonical exports plus a contact sheet under `episodes/E001/final/`.

Gate state:

- Gate A: E001 selected as `GO` in the research run.
- Gate B: the complete plan proceeded into an authorized two-slide render preflight; the exact approval wording was not preserved, so do not claim a verbatim approval record.
- Render preflight: first attempt rejected; clean Slide 1 and Slide 5 retries passed.
- First production pass: seven slides complete with vector lettering and QC.
- Gate C: reached; human decision pending.

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

The original style blocker was resolved through:

- `INSTATOON_STYLE_v1.2`;
- five approved assets under `assets/style_refs/`;
- `FACE_LOCK_BLOCK`;
- `BACKGROUND_DENSITY_LOCK`;
- production-wide `ANTI_GPT_DEFAULT_BLOCK`;
- prohibition on using a failed frame as the sole style anchor.

The two earlier recovered PNG candidates recorded in previous history were never promoted to repository-canonical assets. The current five-file set is defined by exact paths and hashes in `REFERENCE_SET.md`. REF_03 and REF_05 are now high-resolution PNGs; their faint texture/detail difference is a Gate C watch item, not a hidden blocker.

---

## Exact next execution

1. Review `episodes/E001/final/E001_contact_sheet.png` and the two watch items in `episodes/E001/RENDER_MANIFEST.json`.
2. Record one Gate C decision:
   - `PUBLISH` — accept E001 as the first prototype baseline;
   - `REPAIR` — name the exact slide/text/style defect and make a targeted change;
   - `KILL` — archive the execution evidence without using it as a baseline.
3. In the same decision, confirm whether faint surface texture is acceptable for v1.2 or whether the five canonical references must be normalized before Prototype 2.
4. If `PUBLISH`, select Prototype 2 and repeat the same typed sequence, capturing exact prompt/reference hashes before each image call.
5. Do not start the reusable vector renderer or executable orchestrator until all three prototypes have exposed stable patterns.

Current blocker: **none technical**. The next gate is the user's human taste/publish decision.
