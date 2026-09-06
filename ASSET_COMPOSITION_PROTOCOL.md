# ASSET_COMPOSITION_PROTOCOL.md

Version: 1.0
Updated: 2026-09-07
Status: CANONICAL FOR FINAL VISUAL PRODUCTION

## 0. Architectural decision

Instatoon no longer treats full-frame generative image synthesis as the default final renderer.

Canonical visual path:

`story/storyboard → asset resolve → asset-gap authoring → approved asset registry → deterministic composition → editable lettering/UI → QC/export`

The generative model is an **asset author / exception tool**, not the default owner of the final frame.

This document supersedes older sections of GENERATION_PROTOCOL.md, MASTER_PROMPTS.md, STYLE_LOCK.md, REFERENCE_SET.md and episode packages wherever those sections assume that every final slide should be freshly synthesized as one complete raster. Their style, identity, anatomy, geometry, reference-binding and quarantine rules remain valid for **new asset authoring** and for the explicit exception lane.

## 1. Why this boundary exists

A final slide contains multiple independent requirements: identity, drawing language, pose, anatomy, camera, prop geometry, background, expression and later lettering. Re-sampling all of them on every slide makes previously accepted properties probabilistic again.

Therefore:
- do not regenerate an accepted character merely because a new scene is needed;
- do not regenerate an accepted background merely because dialogue changes;
- do not ask QC/retry loops to create determinism that the final-image sampler does not provide;
- move repeatable choices into files, IDs, transforms and code.

## 2. Asset classes

Production assets are immutable, hash-bound files registered by ID.

Minimum classes:
- `CHARACTER_POSE` — approved character body/pose/view asset, preferably transparent;
- `CHARACTER_EXPRESSION` — optional face/expression overlay when the art system supports safe modularity;
- `EXTRA_POSE` — reusable background/supporting-person asset;
- `PROP` — phone, bag, table object, etc.;
- `BACKGROUND` — reusable location or local background plate;
- `FX` — speed lines, tears, emphasis marks and similar non-text visual effects;
- `UI_SHELL` — deterministic device/UI shell without meaning-bearing text;
- `EPISODE_LOCAL` — any approved one-episode asset that should not become project-wide authority.

A single baked character pose+expression asset is allowed when modular face replacement would damage the drawing. Modularity is a means, not a quota.

## 3. Asset scope

Every asset has one scope:
- `PROJECT_CANONICAL` — stable recurring identity/style asset;
- `PROJECT_REUSABLE` — reusable but replaceable library asset;
- `EPISODE_LOCAL` — valid only for one episode;
- `EXCEPTION_OUTPUT` — approved full-frame generative output used only when composition cannot reasonably express the shot.

Promotion from episode-local to project-reusable requires explicit approval. A liked image is not automatically a reusable asset.

## 4. Approval and registry invariant

Only `APPROVED` assets may enter final composition.

The registry must bind:
- asset_id;
- category and scope;
- exact file path;
- SHA-256;
- dimensions;
- relevant identity/pose/view/expression descriptors;
- approval actor/evidence;
- status.

Rejected, stale or hash-mismatched assets are fail-closed and cannot be selected.

An approved asset is immutable. A replacement receives a new asset version/ID; approval does not float to changed bytes.

## 5. Scene contract

A final slide is a deterministic scene specification, not an image prompt.

At minimum it declares:
- canvas width/height;
- ordered layers;
- asset_id per raster layer;
- x/y;
- scale;
- rotation;
- optional horizontal flip when semantically valid;
- opacity;
- z-order;
- optional crop/mask data;
- separate lettering/UI plan.

The same registry + same scene contract must produce the same composition bytes, modulo explicitly documented encoder metadata.

Composition may vary framing by crop, scale, layer position, occlusion and asset selection. This is how sequence variety is produced without re-sampling accepted identities.

## 6. Asset-gap routing

Before any visual generation, resolve the storyboard against the approved registry.

For each required visible element:
1. reuse an approved asset if it expresses the beat without semantic compromise;
2. compose/reframe existing assets if transforms are sufficient;
3. if a necessary pose/expression/prop/background is missing, create an **ASSET_GAP**;
4. author only the missing asset, not the whole slide;
5. run the applicable style/identity/anatomy/geometry QC from the legacy generation protocol;
6. register only a USER/authorized PASS;
7. resume deterministic composition.

The library is self-expanding. Repeated production should decrease the fraction of pixels that require fresh generation.

Do not weaken a story beat merely to avoid one justified asset gap.

## 7. Generative exception lane

Full-frame generation is not deleted, but it is exceptional.

Use it only when:
- the shot materially depends on geometry/interaction that cannot be represented by the current asset system without visibly inferior results; or
- the user explicitly chooses a generative experiment.

An exception must record:
- why composition is insufficient;
- which accepted authorities are bound;
- retry/cost cap;
- whether the result is episode-local only.

A PASS exception frame may be used in final composition as a single `EXCEPTION_OUTPUT` background/full-frame layer. It must not silently become a new project style or identity authority.

## 8. Text and UI

Meaning-bearing text, speech bubbles, captions, messenger text, read/unread numbers and layout remain deterministic editable layers.

Do not bake them into generated character/background assets.

Existing lettering.py direction remains valid.

## 9. Sequence QC after the pivot

Sequence QC still matters, but repair ownership changes.

If a sequence feels repetitive:
- first change scene composition, crop, scale, asset choice or layer placement;
- if the beat genuinely needs a missing pose/view, open one asset gap;
- do not regenerate every accepted slide.

If anatomy/identity is wrong in an approved asset:
- invalidate that asset version and only scenes that depend on it;
- do not rerender unrelated scenes.

## 10. Migration state

Legacy full-frame render infrastructure remains in the repository only as the exception lane and as historical test infrastructure.

Fresh production must not resume E001 through the old S02→S04 full-frame generation path.

Migration completion criteria:
1. registry format exists and validates approved/hash-bound assets;
2. deterministic compositor can build one 4:5 slide from registered assets;
3. a small starter library covers at least one 4-slide pilot;
4. the pilot is completed without full-frame generation except explicitly approved exception shots;
5. lettering remains separate and deterministic.

Until 1–3 are satisfied, production state is `ASSET_SYSTEM_CALIBRATION`, not episode raster production.
