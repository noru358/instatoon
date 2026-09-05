# REFERENCE_SET.md

# CURRENT REFERENCE MAP — INSTATOON_STYLE_v2.0
Updated: 2026-09-05

## Legacy assets

The files currently stored under assets/style_refs/ belong to the retired pre-reset v1.x style.

They are NON-CANONICAL for current production.
Do not use them as fallback references.

## Current approved v2 references

### REF_V2_A — brown-bob female character sheet
Controls the current face, eye, outline, flat-color, full-body, gesture and expression grammar.

### REF_V2_B — long-wavy-hair female character sheet
Confirms the same drawing grammar across a different identity and controls long-hair massing and clothing simplification.

### REF_V2_C — approved background-style sample
Contains multiple everyday environments and controls:
- same-artist character/background language;
- low background detail;
- flat local color;
- simple perspective.

### REF_V2_D — approved main-cast sheet
Contains Gaeun, Harin and Taemin.

Binary:
- path: `assets/style_refs/v2_current/REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg`
- dimensions: 1448 × 1086
- SHA-256: `dbddf458a97c89781075e6be03ab2c393eff75b95e8856f044bd81f29310ec07`

Notes:
- Harin uses black socks when visible.
- Taemin uses the approved current male identity.
- Story/context decides whether any main character appears.

### REF_V2_E — approved 3-person interaction / background application reference
This is a POSITIVE CURRENT REFERENCE, not a contamination example.

Binary:
- path: `assets/style_refs/v2_current/REF_V2_E_3PERSON_INDOOR_SCENE.jpeg`
- dimensions: 1536 × 864
- SHA-256: `b49683276f94ba5621e3602d7e3d714b0f2e637b2c41fc1fd132bdf6f336b049`

It is the approved result of applying REF_V2_A / REF_V2_B drawing language to:
- a real interior background;
- three characters together;
- seated multi-person interaction;
- props/furniture/environment in the same visual grammar.

Use it as evidence for how the v2 character style should extend into background + multi-person scenes.

It confirms:
- multi-person compatibility;
- indoor-environment compatibility;
- character/background style coherence;
- correct direction for scene-level application of the canonical style.

Do not classify this image as visual drift merely because it contains a full scene rather than a character sheet.

## Episode-local character references

A new important non-main character appearing in 2+ cuts must get an episode-local character anchor before story frames.

That anchor:
- fits the role/context;
- stays visually distinct from main cast;
- uses v2 style;
- becomes the identity source for that episode only.

## Last-known-good references

For a targeted repair, the latest accepted frame may control:
- camera;
- blocking;
- location;
- pose;
- accepted geometry.

It does not override the v2 style reference.

Never promote a visibly regressed retry into the new reference.

## Current binary status

REF_V2_D and REF_V2_E are materialized in this repository at the exact paths and hashes above.

REF_V2_A, REF_V2_B and REF_V2_C are still not materialized here. Until they are ingested:
- do not substitute legacy v1 assets;
- use their approved binaries only when present in the active environment;
- if a task specifically requires one of those missing references, stop rather than silently reverting.


## Reference-conditioning requirement

Current canonical v2 production requires BINARY_CONDITIONED reference use for L13.

Operational meaning:
- REF_V2_D and REF_V2_E must be supplied to the chosen renderer as actual media inputs when an episode lists them in required_refs;
- repository existence, hashes, prompt descriptions, or operator inspection alone are insufficient;
- a renderer without an explicit reference-media bridge is not eligible for canonical v2 raster production;
- AUTHORITY_INFORMED / NON-BINARY-CONDITIONED output may be used only when an episode explicitly declares AUTHORITY_ONLY_ALLOWED, never as an implicit fallback for v2 production.

This requirement is enforced machine-readably through EPISODE_PLAN, RENDER_MANIFEST, and pipeline/render_guard.py.


## Runtime binding requirement — SHORT-TERM PRODUCTION LOCK

Reference status and reference delivery are separate.

A canonical asset is not considered visually active for a production render merely because:
- it exists in GitHub;
- its path/hash was restored;
- the operator inspected it earlier;
- its traits were paraphrased into text.

For style-sensitive production, the canonical image must be supplied to the renderer as actual image media.

Primary current style/identity media:
- `assets/style_refs/v2_current/REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg`

Secondary scene/style media when available:
- `assets/style_refs/v2_current/REF_V2_E_3PERSON_INDOOR_SCENE.jpeg`

After an episode receives a human-approved style pass, that approved image becomes a secondary EPISODE STYLE/IDENTITY ANCHOR for later cuts. It supplements but never replaces the canonical style media.

If a client cannot bridge the GitHub binary into the renderer, production must use an equivalent actually attached copy of the same approved image (for example, the user-uploaded copy present in the active conversation). Text-only authority-informed generation is prototype-only under this short-term lock.
