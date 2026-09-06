# CURRENT_STATE.md

Updated: 2026-09-07
Repository: noru358/instatoon
Architecture: ASSET_COMPOSITION_v1
Operating mode: CALIBRATION

## Active production

Active episode: NONE
Next publishable episode: **E001 after renderer pilot**

The old full-frame E001 experiment is retired from the working tree. Git history is the archive.

## Final-render boundary

`story → storyboard → asset resolve → ASSET_GAP authoring → approved registry → deterministic composition → editable lettering/UI → QC/export`

Default final renderer: AutoPipeline `pipeline/compositor.py`.

Full-frame generation is exception-only and is routed through the shared AutoPipeline asset-production/dispatch path. Instatoon keeps no legacy per-slide renderer/state machine.

## Pilot policy

Architecture calibration uses **exactly 4 slides**.

This is a TEST FIXTURE, not an Instatoon content rule.

Why fixed:
- enough frames to test asset reuse, sequence variation and dependency invalidation;
- small enough that new asset demand does not swamp the renderer test;
- keeps frame count from becoming another moving variable while the compositor is being validated.

After the pilot passes, production slide count is story-driven under VISUAL_GRAMMAR:
- no four-cut requirement;
- no fixed count inherited from the pilot;
- do not pad or cut a story merely to match the calibration fixture.

## Current approved visual inputs

Authoring/style authority:
- `assets/style_refs/v2_current/REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg`
- `assets/style_refs/v2_current/REF_V2_E_3PERSON_INDOOR_SCENE.jpeg`
- optional supplemental `assets/style_refs/v2_current/sub1.png`

Production registry:
- `assets/production/registry.json`
- current approved composition assets: **0**

Reference images are authoring authority, not automatically composition-ready assets.

## Next action

Build one fixed four-slide compositor pilot.

1. Choose a minimal pilot story that exercises at least:
   - one repeated character;
   - two meaningfully different framings/poses;
   - one reusable background/local plate;
   - one prop or interaction.
2. Resolve required assets against the registry.
3. Author only ASSET_GAP items and user-QC them.
4. Register approved bytes with hash/dimensions/scope.
5. Compose exactly four separate 4:5 art frames with the shared AutoPipeline compositor.
6. Apply lettering separately.
7. Review whether identity, style, framing variety and story readability survive without full-frame generation.

Pilot PASS authorizes fresh E001 preproduction. Pilot content itself does not become E001 unless explicitly chosen.
