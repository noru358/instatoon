# REFERENCE_SET.md

# Reference-set status — INSTATOON_STYLE_v2.0
Updated: 2026-09-04

## Critical status

The pre-reset assets currently stored under `assets/style_refs/` are LEGACY and NON-CANONICAL.
They must not be used to define the current style.

Current visual authority was approved in the 2026-09-04 style-reset session and consists conceptually of:

1. USER_REF_A — brown-bob female character sheet:
   - large round eyes;
   - simple black pupil/iris + tiny highlight;
   - simple nose/mouth;
   - black hand-drawn outline;
   - flat color;
   - minimal shading;
   - full body / gestures / seated / expression vocabulary.

2. USER_REF_B — long-wavy-black-hair female character sheet:
   - same drawing grammar as USER_REF_A;
   - confirms style across different hair/clothing identity.

3. APPROVED_BACKGROUND_STYLE_SAMPLE:
   - home, bedroom, desk, café, office, classroom, subway, street, restaurant, park, shop, night-city examples;
   - simple black outline;
   - flat muted fill;
   - low detail;
   - same-illustrator feel between character and environment.

4. APPROVED_MAIN_CAST_SHEET:
   - Gaeun / Harin / Taemin in v2 style;
   - Harin black socks;
   - Taemin replaced with the approved black-haired male identity.

5. APPROVED_3P_INTERACTION_TEST:
   - Gaeun + Harin + Taemin in an indoor conversation scene;
   - verified multi-character + background compatibility.

## Binary-asset note

The text locks have been updated immediately.
The approved v2 binary images from the current chat still need to be materialized into the repository before a future fully self-contained automated renderer can rely on GitHub alone.

Until that binary ingest is complete:
- do NOT fall back to the legacy `assets/style_refs/` images;
- use MASTER_PROMPTS.md + the approved v2 images when supplied in the active environment;
- if no approved v2 image is available and exact style fidelity is critical, stop rather than silently using legacy references.

## Future target paths

When binary ingest is available, use names such as:
- `assets/style_refs_v2/REF_A_BROWN_BOB_CHARACTER_SHEET.*`
- `assets/style_refs_v2/REF_B_WAVY_BLACK_CHARACTER_SHEET.*`
- `assets/style_refs_v2/REF_C_BACKGROUND_STYLE_SAMPLE.*`
- `assets/characters/MAIN_CAST_V2.*`
- `assets/style_refs_v2/REF_D_3P_INTERACTION_APPROVED.*`

After upload, record exact filenames + hashes here and remove the temporary binary-asset warning.
