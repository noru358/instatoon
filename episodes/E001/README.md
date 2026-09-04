# E001 — 편의점 음유시인

Status: **PREFLIGHT RETRY READY — CANONICAL STYLE BLOCKER RESOLVED**

This is the first real TOON SYSTEM v0.1 prototype.

## Why this episode

The source contains unusually strong human-specific details:
- troublesome regular;
- unexpectedly sincere sentence;
- two opened ice bars;
- one in each hand;
- insistence on taking a bite;
- deadpan aftermath.

It is therefore useful for testing whether the system preserves **source texture** rather than converting everything into generic AI storytelling.

## Current gate

The entire 7-slide story and visual plan exists and proceeded into a two-slide render preflight. This functionally moved the episode through Gate B, although the exact approval wording was not preserved in the repository.

The first preflight was rejected. The shared style blocker has since been resolved through `INSTATOON_STYLE_v1.2` and the five approved binary references in `REFERENCE_SET.md`.

Current action:
1. keep bulk generation stopped;
2. retry Slide 1 only;
3. run style/visual-grammar QC;
4. retry Slide 5 only if Slide 1 passes;
5. render the remaining slides only if both preflight slides pass.


---

## Preflight execution result — 2026-09-04

Generated:
- Slide 1 cover preflight
  - image_gen gen_id: `8b27651d-2cd4-4762-bcf3-bd41c538c303`
  - size: 1122×1402
  - SHA-256: `85457dbe9b47206e9dbfe900a2c1de8a5d54ca6612d6b6c1968f47ca4b11fe9c`
- Slide 5 high-risk interaction preflight
  - image_gen gen_id: `b392eb14-d6b0-4a98-83f0-6a29bb9b68ed`
  - size: 1122×1402
  - SHA-256: `b68b5bf5fafd80a9d8fe1b6705b8f845612ca2efbeab9b9cc2f73982f471bc79`

The failed PNG binaries are not claimed as GitHub-preserved; the identifiers/hashes are retained as execution evidence.

### Verdict
**REJECT BOTH — systemic style failure.**

Story semantics were mostly readable, but the rendering language drifted heavily toward a generic AI/GPT illustration look.

### Observed global style defects
1. **Eyes:** white sclera + separate pupils instead of tiny solid-dark eye grammar.
2. **Hair:** many internal strokes / textured hair rather than broad flat near-black masses.
3. **Texture:** pervasive paper/grain/pencil-like surface texture.
4. **Shading:** more modeled skin/clothing/background shading than the lock permits.
5. **Lighting:** convenience-store night scene became cozy/atmospheric with refrigerator/window/lamp glow.
6. **Background density:** products, refrigerators, lamps, window architecture and counter equipment were individually rendered too strongly.
7. **Finish:** image reads as polished editorial/anime-adjacent AI illustration rather than a modest low-density anecdote comic.
8. **Slide 5 compound error:** Slide 1, already style-failed, was reused as a style/continuity anchor, causing the wrong style to propagate.
9. **Slide 5 action error:** both ice bars appear already bitten/notched and the handoff is less clean than specified; this frame should precede the worker taking a bite.

### Root cause
The execution did **not** use the true canonical visual reference image as the primary style authority.

The first render used a summarized textual style description. That allowed the image model's generic illustration prior to fill ambiguous details.

The second render then used the first failed frame as the principal reference, compounding the drift.

### System correction
- STYLE_LOCK was first hardened to v1.1, then superseded by `INSTATOON_STYLE_v1.2` with validated face-distance/off-axis-gaze and background-density controls.
- MASTER_PROMPTS adds explicit anti-GPT-default flatness/texture/eye/hair/background rules plus mandatory face and environment controls.
- GENERATION_PROTOCOL requires an approved canonical binary style reference before production raster generation.
- Five approved WebP references are present under `assets/style_refs/` and registered in `REFERENCE_SET.md`.
- Failed preflight frames may not become style anchors.

### Blocker resolution

The previous missing-binary blocker is **resolved**. The failed render remains rejected, but the episode is ready for a clean preflight retry with the approved references.

### Next retry sequence
1. Before spending external tool credits, obtain explicit user approval.
2. Run Slide 1 only under `INSTATOON_STYLE_v1.2` using `INSTATOON_REF_04_INDOOR.webp` plus `INSTATOON_REF_01_CHARACTER.webp`.
3. Attach the production reference-obedience, face-lock, background-density, master-style, negative-style, and anti-GPT-default blocks. Preserve top title space and generate no semantic text.
4. QC the style fingerprint and visual grammar before anatomy/defect QC.
5. Only if Slide 1 passes, run Slide 5 using `INSTATOON_REF_03_INTERACTION.webp` plus `INSTATOON_REF_01_CHARACTER.webp`; accepted Slide 1 may support episode-local identity/location continuity only.
6. Slide 5 must show the customer placing exactly two opened, unbitten ice bars into the worker's hands, one bar per hand. Neither bar has a bite yet.
7. Do not bulk-render the remaining slides until both preflight slides pass.
