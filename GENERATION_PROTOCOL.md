# GENERATION_PROTOCOL.md

# ASSET AUTHORING / EXCEPTION GENERATION / QC v3.0
Updated: 2026-09-07

ASSET_COMPOSITION_PROTOCOL.md owns the final-render architecture.
This file governs only stochastic visual work that still exists inside that architecture.

## 1. When generation is allowed

Generation is allowed for:
1. an unresolved ASSET_GAP;
2. repair/replacement of a rejected asset;
3. an explicitly declared full-frame exception.

Generation is not the default response to:
- a new slide;
- a dialogue change;
- a different crop;
- a new text/UI state;
- a missing layout arrangement that deterministic composition can solve.

## 2. Preflight

Before generation:
1. read the current storyboard/scene requirement;
2. resolve approved assets first;
3. identify the smallest missing visual element;
4. inspect STYLE_LOCK.md, MASTER_PROMPTS.md and REFERENCE_SET.md;
5. supply required reference binaries as actual media when supported;
6. define asset category/scope and intended composition use.

If a required reference is unavailable, fail closed. Do not compensate with more prose.

## 3. Scope

Default new generated asset scope:
- EPISODE_LOCAL unless reuse is intentionally requested;
- PROJECT_REUSABLE only after explicit approval;
- PROJECT_CANONICAL only after explicit visual-authority decision.

A generated result is not a production asset until registered with exact bytes/hash/dimensions and approval.

## 4. QC order

### QC-0 Output contract
- exactly one requested asset;
- no grid/collage/multi-panel result;
- no baked dialogue/caption/meaning-bearing UI;
- expected subject/category present;
- no unrelated scene/cast leakage.

### QC-1 Style / identity
- drawing language matches STYLE_LOCK;
- selected recurring identity is preserved;
- episode-only people remain distinct from recurring cast;
- no generic polished AI/webtoon drift.

### QC-2 Anatomy / geometry
Inspect only what the asset actually contains, with extra scrutiny for:
- shoulder→arm→wrist→hand continuity;
- fingers/grip;
- device front/back geometry;
- utensil/contact direction;
- reflection/mirror geometry;
- occluded joints that could hide impossible anatomy.

### QC-3 Semantic fitness
- pose/expression/prop state actually serves the requested beat;
- the asset has enough crop/placement flexibility for intended composition;
- background/prop does not accidentally encode a contradictory story state.

## 5. PASS / FAIL

PASS:
- materialize exact approved bytes;
- calculate SHA-256 and dimensions;
- register under assets/production/registry.json;
- record category/scope/identity/pose metadata;
- resume deterministic composition.

FAIL:
- do not register;
- do not use as a reference, repair base or continuity seed unless the repair explicitly starts from a last-known-good predecessor;
- retry only when the failure is plausibly stochastic and the request contract remains valid.

## 6. Retry policy

Do not loop until something looks acceptable.

For repeated failures:
- same local defect → targeted repair or new asset attempt;
- repeated identity/style failure → revisit reference binding/authoring prompt;
- repeated geometry failure → change asset decomposition or pose strategy;
- repeated whole-frame exception failure → return to composition design unless the user explicitly continues the exception experiment.

## 7. Repair

Minimum-scope repair only.

If one approved asset is replaced:
- new bytes receive a new version/ID;
- only scenes depending on the old asset are invalidated;
- unrelated approved assets/scenes remain valid.

## 8. Full-frame exception lane

Instatoon pipeline/render.py is exception-only and requires --exception-lane.

An exception record must state:
- scene ID;
- why composition is materially insufficient;
- required media bindings;
- retry/cost cap;
- output hash;
- approval scope.

Default promotion policy: EPISODE_LOCAL_ONLY.

No S01-anchor / S02-through-final generation topology is part of current normal production.
