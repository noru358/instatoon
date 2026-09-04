# REFERENCE_SET.md

# Canonical visual reference set — INSTATOON_STYLE_v1.2

**Status:** APPROVED  
**Effective:** 2026-09-04

This file defines the approved visual anchor set used for production rendering.

These images are style authorities, not a requirement that unrelated episodes reuse the same recurring character.

## Approved assets

1. `assets/style_refs/INSTATOON_REF_01_CHARACTER.webp`
   - Role: primary face / hair / close-to-medium character anchor.
   - Use when facial grammar is at risk.
   - Strongest authority for tiny solid-dark eyes, rounded face, minimal nose/mouth, blush, and broad hair massing.

2. `assets/style_refs/INSTATOON_REF_02_FULLBODY.webp`
   - Role: full-body proportion / silhouette / outfit-scale anchor.
   - Use for standing full-body and medium-full scenes.

3. `assets/style_refs/INSTATOON_REF_03_INTERACTION.webp`
   - Role: two-person interaction + outdoor environment balance.
   - Use for social interaction, handoff gestures, and small-group staging.

4. `assets/style_refs/INSTATOON_REF_04_INDOOR.webp`
   - Role: indoor environment density / seated scene anchor.
   - Use for sofa, home, cafe, desk, and other interior scenes.

5. `assets/style_refs/INSTATOON_REF_05_OUTDOOR_APPROVED.webp`
   - Role: corrected outdoor full-body + side-gaze / environment-heavy anchor.
   - Use for residential streets, outdoor full-body framing, or scenes where the face is small in frame.

## Asset integrity

All five canonical files are 360×450 WebP images.

| Asset | SHA-256 |
|---|---|
| `INSTATOON_REF_01_CHARACTER.webp` | `6243d1d58d64f0752f64177b0228c5c0b5b32569c26bd30d5620d9d0a6c478e2` |
| `INSTATOON_REF_02_FULLBODY.webp` | `be289521db188e009541b8a36cb4dccd41b5ead7f8b8a296d5beed11819d720d` |
| `INSTATOON_REF_03_INTERACTION.webp` | `61bda2bb583d78013e12cc0e4521dd44379d9e0681a827ad457bc886b0b232fd` |
| `INSTATOON_REF_04_INDOOR.webp` | `fae356fcd276b28b39b9ad75a72b2f221be2dd215ccbe04bfcdb82cd0dda6412` |
| `INSTATOON_REF_05_OUTDOOR_APPROVED.webp` | `77fcc4ff830ea0d8efcbe34206ae2a19105c7d873b820e8f0b9ec4a5c9987b96` |

If a file's hash differs, do not treat it as the approved canonical binary until the change is explicitly reviewed and versioned.

## Reference selection rule

Use the most relevant scene anchor plus REF_01 when facial drift is plausible.

Recommended combinations:
- portrait / close character → REF_01
- full body → REF_02 + REF_01
- two-person interaction → REF_03 + REF_01
- indoor → REF_04 + REF_01 when needed
- outdoor / environment-heavy / side gaze → REF_05 + REF_01

## Validated drift lesson

The first outdoor full-body attempt was rejected.

Failure combination:
- distant/full-body face
- environment-heavy outdoor scene
- off-axis gaze

Observed result:
- generic GPT/editorial/webtoon facial prior
- eye redesign
- slightly more polished facial construction
- background detail competing with style control

Corrective rule:
> Farther character = simpler face, never more generic/detail-rich face.

And:
> As environment complexity rises, incidental background density should fall.

The corrected REF_05 is the approved outdoor anchor.

## Non-canonical material

The rejected first outdoor variant is intentionally not part of this set and must never be used as a production style anchor.

## Authority

When a production scene includes another continuity/reference image:
- canonical style refs control line, face grammar, hair rendering, palette, shading, texture, and density;
- continuity refs control identity/clothing/scene facts only;
- scene text may not override the canonical rendering language.
