# REFERENCE_SET.md

# CURRENT REFERENCE MAP — INSTATOON_STYLE_v2.0
Updated: 2026-09-07

## Legacy assets

The five INSTATOON_REF_* files directly under assets/style_refs/ belong to the retired pre-reset v1.x style. Files under v2_current/ are current, not legacy.

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

### REF_V2_SUB_01 — user-supplied supplemental v2 reference

Classification: **PROJECT_REUSABLE**  
Role: **SUPPLEMENTAL_STYLE_REFERENCE**

Binary:
- path: `assets/style_refs/v2_current/sub1.png`
- SHA-256: `1bd41fc701bc824ebe103954acb38f6d70e144886e48a152245af29f0c8c3486`
- size: 1,971,514 bytes

Authority:
- secondary/supplemental only;
- does not replace REF_V2_D / REF_V2_E;
- use it only when the active episode/render contract explicitly binds it as a supplemental style input.

Machine registry:
- `assets/style_refs/v2_current/registry.json` is the executable inventory for current v2 binaries;
- CI fails if a current reference binary is added, removed or changed without matching registry metadata.

## Reference asset classes and request policy

Reference requests are routed by **role and reuse scope**, not by episode improvisation.

### Class A — PROJECT_CANONICAL

Purpose:
- drawing language;
- recurring lead identity;
- reusable background/scene grammar.

Storage:
- materialized binary under the project asset tree;
- stable path + SHA-256 recorded in this reference map;
- reusable across episodes when the role matches.

Promotion:
- requires explicit user approval as a reusable project reference;
- never infer promotion merely because one episode used the image successfully.

### Class B — PROJECT_REUSABLE

Purpose:
- a recurring need not yet strong enough to redefine the canonical style, such as a reusable expression-range sample, extra/background-person diversity sample, recurring location, or recurrent prop grammar.

Storage:
- materialized binary in a reusable project asset area;
- role, intended scope and hash recorded before production relies on it.

Promotion:
- may later become PROJECT_CANONICAL only after repeated usefulness + explicit user approval;
- otherwise remains a bounded reusable library asset.

### Class C — EPISODE_LOCAL

Purpose:
- one-off location, person, food/object, outfit, device, spatial arrangement, or factual visual evidence needed only for one story.

Storage:
- bind to the episode package/work packet with actual bytes or a verified immutable source;
- hash and role are recorded;
- do not add it to the global style/reference set automatically.

Lifecycle:
- it may be archived with the episode;
- promote it only if a later cross-episode need appears and the user explicitly approves reuse.

### Class D — ACCEPTED_OUTPUT_ANCHOR

Purpose:
- last-known-good generated frame;
- episode-local identity/geometry/pose continuity.

Storage:
- artifact hash + exact accepted file;
- bound to the approval/QC record.

Authority:
- secondary only;
- never silently replaces PROJECT_CANONICAL style media.

### Class E — RESEARCH_ONLY

Purpose:
- external examples used to understand composition, behavior, culture, product UI, food state, or other real-world detail.

Authority:
- not renderer-conditioning media by default;
- must not be treated as a canonical style reference unless separately approved and registered.

### When to ask the user for a new reference

Before requesting a file, the visual preflight must answer:

1. **What visual role is missing?**
2. **Can current registered references already cover that role?**
3. **Can the requirement be solved deterministically by layout/vector/UI/scene contract instead of a new image reference?**
4. **Is the need project-reusable or episode-local?**
5. **Will lack of this reference materially reduce correctness or reproducibility?**

Ask the user only when the missing evidence is material and cannot be satisfied by current registered assets or deterministic construction.

When asking, state:
- the missing role;
- expected scope: PROJECT_CANONICAL / PROJECT_REUSABLE / EPISODE_LOCAL;
- why current assets are insufficient;
- where it will be registered if supplied.

Do **not** repeatedly ask the user to re-upload a reference that is already materialized and hash-verified in the repository/work packet and can be delivered to the active renderer.

If a supplied image should be reusable, register it once and reuse it by asset identity. If it is episode-only, keep it episode-scoped. Never solve a missing binary by copying its visual description into a prompt and pretending the reference requirement was satisfied.

## Episode-local character references

A new important non-main character appearing in 2+ cuts gets one internal identity digest before rendering, not a mandatory standalone character sheet.
After the first accepted episode image, reuse that actual image as a secondary style/identity anchor in later cuts. The canonical style image remains primary; the slide contract controls the new action and composition.
A separate character-sheet image is optional when continuity fails or the character is promoted for reuse.

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

EPISODE_PLAN / RENDER_MANIFEST declare this requirement. The guard checks local media integrity and caller-supplied evidence; actual delivery still requires a renderer adapter or an inspected manual tool call.


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
