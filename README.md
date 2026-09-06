# instatoon

실제 사람이 쓴 인터넷 소재 → 대본/콘티 → 승인된 visual asset 조립 → 편집 가능한 대사/UI → QC/export.

## Canonical architecture

`source → story/dialogue → storyboard → asset resolve → ASSET_GAP authoring → approved registry → deterministic composition → lettering/UI → QC/export`

- final frame 기본 owner: AutoPipeline `pipeline/compositor.py`
- 생성 모델: missing asset author / explicit exception renderer
- production registry: `assets/production/registry.json`
- one slide = one image file
- final art raster is text-free by default

## Restore order

1. `README.md`
2. `CURRENT_STATE.md`
3. `ASSET_COMPOSITION_PROTOCOL.md`
4. task-relevant creative authority:
   - source/dialogue: `SOURCE_STORY_PIPELINE.md`
   - storyboard/layout: `VISUAL_GRAMMAR.md`
   - style: `STYLE_LOCK.md`
   - authoring prompts/QC: `MASTER_PROMPTS.md`, `GENERATION_PROTOCOL.md`
   - references: `REFERENCE_SET.md`
5. `assets/production/registry.json`

Do not restore retired episode/full-frame workflows from Git history unless the user explicitly asks for a historical experiment.

## Authority map

| Domain | Authority |
|---|---|
| source / story / dialogue | SOURCE_STORY_PIPELINE.md |
| storyboard / sequence / text-layout semantics | VISUAL_GRAMMAR.md |
| final-render boundary / asset routing | ASSET_COMPOSITION_PROTOCOL.md |
| drawing-language pass/fail | STYLE_LOCK.md |
| stochastic asset authoring prompt | MASTER_PROMPTS.md |
| stochastic asset/exception QC | GENERATION_PROTOCOL.md |
| current authoring references | REFERENCE_SET.md |
| approved production assets | assets/production/registry.json |
| current stage / next action | CURRENT_STATE.md |
| shared runtime / compositor | noru358/AutoPipeline |

## Episode length

Production episode length is **story-driven**. VISUAL_GRAMMAR currently treats roughly 5–9 slides as common, not mandatory.

The architecture calibration pilot is **fixed at 4 slides only to control test variables**. That number must never leak into production as a content rule.

## Visual production

For each planned slide:
1. resolve required visible elements against the approved registry;
2. reuse/reframe existing assets where semantically valid;
3. create ASSET_GAP only for truly missing visual capability;
4. author/QC/register the missing asset;
5. compose the scene deterministically;
6. apply editable lettering/UI separately.

A new slide is not, by itself, a reason to call an image generator.

## Full-frame exception

`pipeline/render.py` is retained only for an explicitly declared exceptional shot and fails closed without `--exception-lane`.

Old S01-anchor → S02..final full-frame generation, AUTO_FINISH, render/qc Actions workflows and retired E001 packages are not current production paths.

## Current state

Active episode: NONE.

Next task: fixed four-slide renderer pilot, then fresh E001 if the pilot passes.

Git history is the archive; obsolete working-tree handoffs/episodes are intentionally removed.
