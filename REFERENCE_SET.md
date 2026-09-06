# REFERENCE_SET.md

# CURRENT INSTATOON VISUAL REFERENCES
Updated: 2026-09-07

Git history is the archive. Retired v1 reference files are not kept in the working tree.

## Canonical current assets

### REF_V2_D — MAIN CAST / PERSON STYLE

Path:
`assets/style_refs/v2_current/REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg`

Role:
- current Gaeun / Harin / Taemin identity authority;
- person drawing-language evidence;
- recurring-character authoring reference.

SHA-256:
`dbddf458a97c89781075e6be03ab2c393eff75b95e8856f044bd81f29310ec07`

The three characters are reusable, not mandatory cast.

### REF_V2_E — MULTI-PERSON / SCENE STYLE

Path:
`assets/style_refs/v2_current/REF_V2_E_3PERSON_INDOOR_SCENE.jpeg`

Role:
- evidence that the person style extends coherently to a real environment;
- multi-person interaction and character/background style coherence;
- scene/background authoring reference.

SHA-256:
`b49683276f94ba5621e3602d7e3d714b0f2e637b2c41fc1fd132bdf6f336b049`

Do not copy its camera, pose or furniture layout unless the current scene actually requires them.

### REF_V2_SUB_01 — SUPPLEMENTAL

Path:
`assets/style_refs/v2_current/sub1.png`

Role: PROJECT_REUSABLE supplemental style evidence.

SHA-256:
`1bd41fc701bc824ebe103954acb38f6d70e144886e48a152245af29f0c8c3486`

It never overrides REF_V2_D / REF_V2_E.

Machine inventory:
`assets/style_refs/v2_current/registry.json`

## Authoring reference vs production asset

These reference images guide **new asset authoring**.

They are not automatically final-composition assets.

A character pose/background/prop may enter final frames only after:
1. exact bytes are materialized under the production asset area;
2. style/identity/anatomy/geometry QC passes;
3. user/authorized approval is bound to those bytes;
4. the file is registered in `assets/production/registry.json`.

## Reference scopes

- PROJECT_CANONICAL — stable style/identity authority.
- PROJECT_REUSABLE — reusable supporting evidence.
- EPISODE_LOCAL — one-episode authoring input.
- ACCEPTED_OUTPUT_ANCHOR — accepted generated asset used only within its declared scope.
- RESEARCH_ONLY — never renderer conditioning.

Do not promote a supplied image to a wider scope automatically.

## New-reference request policy

Before asking for another reference:
1. check current canonical/reusable references;
2. check whether the requirement is really an ASSET_GAP;
3. check whether deterministic composition/UI solves it;
4. ask only when missing visual evidence materially affects authoring correctness.

Text placement, messenger UI, read indicators and deterministic screen layout are not reasons to request a new raster reference.

## Binding rule

When generation is used for an ASSET_GAP or exception shot, every required image reference must be supplied as actual media if the renderer supports media input. A filename or prose description does not count as conditioning.

Rejected output is never a reference or registry asset.
