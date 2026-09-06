# CURRENT_STATE.md

Updated: 2026-09-07
Repository: noru358/instatoon
Operating mode: MANUAL_VALIDATION
Architecture: ASSET_COMPOSITION_v1

## Production state — architecture migration active

Execution authorization: **ASSET_SYSTEM_CALIBRATION_ONLY**.

The former E001 full-frame generative production run is **SUSPENDED / LEGACY EVIDENCE**.
Do not resume S02-S04 through the old per-slide full-frame generation path.
No legacy E001 raster is promoted into the new production asset registry automatically.

The next publishable episode number remains E001 after the asset/composition pilot proves the new renderer architecture. Episode content may be replaced; durable structural lessons remain.

## Canonical final-visual authority

Final visual path:

`story/storyboard → asset resolve → asset-gap authoring → APPROVED registry → deterministic compositor → editable lettering/UI → QC/export`

Primary authority:
- `ASSET_COMPOSITION_PROTOCOL.md`;
- `assets/production/registry.json`;
- `schemas/asset_registry.schema.json`;
- `schemas/composition_scene.schema.json`;
- `pipeline/compositor.py`.

Existing authorities remain active in narrower roles:
- `STYLE_LOCK.md`, `MASTER_PROMPTS.md`, `REFERENCE_SET.md`: asset-authoring/style/identity authority;
- `GENERATION_PROTOCOL.md`: generative asset/exception QC, reference binding, quarantine and repair rules;
- `VISUAL_GRAMMAR.md`: storyboard, shot semantics and composition planning;
- `pipeline/lettering.py`: deterministic editable text layer.

## Renderer ownership

Default final renderer: **DETERMINISTIC_COMPOSITOR**.

`pipeline/render.py` is no longer a normal final-frame renderer. It is retained only for an explicitly declared generative exception/legacy experiment and must not be used to continue the suspended E001 path.

A missing pose/expression/prop/background is an `ASSET_GAP`, not permission to regenerate the whole frame.

## Registry state

`assets/production/registry.json` currently contains **0 approved production assets**.

The existing style/cast/scene references are authoring authorities, not automatically composition-ready assets. They may be used to create the starter asset library, but must pass the new asset registration/approval contract before final composition.

## Current blockers

1. No composition-ready approved asset starter pack exists yet.
2. Existing recurring-character references are not yet normalized into production pose/view assets.
3. No four-slide pilot scene contracts exist for the compositor.
4. The new compositor requires Pillow in the execution environment.

These are calibration blockers, not reasons to fall back to full-frame generation.

## Exact next action

Build the minimum starter asset pack for one four-slide pilot, using the already-approved drawing style as authoring authority.

Target pack:
- one recurring character: a small set of story-useful view/pose/expression combinations;
- one supporting/extra character asset if the pilot needs one;
- 1–2 reusable background plates or local background components;
- only the props/FX needed by the pilot.

For every new asset:
1. generate/import the asset only;
2. user/QC approve it;
3. materialize exact bytes under `assets/production/`;
4. register SHA-256 + dimensions + scope;
5. compose a slide from registry IDs.

Pilot success criterion: four separate 4:5 frames assembled without full-frame generation except an explicitly approved exception, followed by deterministic lettering.
