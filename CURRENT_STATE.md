# CURRENT_STATE.md

# LIVE STATE — 2026-09-05

Repository: noru358/instatoon

## Big flow

Style reset complete → E002 pilot lessons captured → E003 human-seeded production → native/direct coordinated raster pass → lettering/QC → first publishable episode → repeat prototypes → automation implementation.

## Current detailed position

Visual-style exploration itself is no longer the main task.

Approved:
- v2 character style from the two canonical character-sheet references;
- v2 background direction;
- Gaeun / Harin / Taemin main-cast sheet after corrections;
- the approved 3-person indoor interaction image is a POSITIVE reference showing the canonical style correctly extended to background + multi-person composition; it is NOT a contamination example;
- 4:5 feed/carousel as primary format;
- 9:16 Reels/Shorts derivative;
- omnibus content model;
- source-voice / dialogue-humanization / USER VOICE GATE workflow.

Active episode: episodes/E003/README.md

## E003 — current diagnosis

New-work request correctly routed to a fresh episode.

Human-seeded base:
- Reddit r/tifu "TIFU by being so socially awkward it's unreal"
- https://www.reddit.com/r/tifu/comments/178qnsy/
- used as inspiration/base, not literal adaptation.

Current story:
Gaeun meets a stranger on the way to a restroom, reflexively apologizes when told her shoelace is untied, then compounds the awkwardness by automatically saying "see you later" while both enter the same restroom.

L1-L12 are complete and recorded in episodes/E003/README.md.

L13 raster render is READY through native/direct image generation.

Historical external attempt:
- REF_V2_D and REF_V2_E were supplied as reference URLs to Higgsfield Nano Banana Pro;
- that optional provider rejected all six jobs before generation because its connected workspace had no credits;
- this is a provider-specific failure, not a project-stage blocker.

Current renderer rule:
- native/direct ChatGPT image generation is first-class and may be used without invoking Higgsfield;
- before direct generation, restore the full production pack and inspect the actual current visual binaries;
- use MASTER_PROMPTS + observed reference traits + episode visual plan;
- if a renderer cannot accept the repository binaries as explicit media inputs, report AUTHORITY-INFORMED / NON-BINARY-CONDITIONED honestly rather than pretending they were injected;
- never generate from chat memory alone.

## Current hard lesson

Do not solve one local problem by fully regenerating a good frame.

Use:
LAST_KNOWN_GOOD → local change only.

For a new non-main person appearing in 2+ cuts:
STORY/CONTEXT → INTERNAL IDENTITY DIGEST → COORDINATED EPISODE BATCH.

This internal continuity operation is not a separate user-facing character-sheet or approval stage.

This applies across future sessions and episodes.

## Exact next action

1. Keep E003 source/story/dialogue/storyboard as the current production package.
2. Before L13, restore CURRENT_STATE + MASTER_PROMPTS + VISUAL_GRAMMAR + GENERATION_PROTOCOL + REFERENCE_SET + E003 package and inspect REF_V2_D + REF_V2_E.
3. Use native/direct ChatGPT image generation first unless the user requests another renderer or a required capability is missing.
4. Generate six coordinated text-free frames while preserving Gaeun and the episode-only stranger identity digest.
5. Report exact docs/assets inspected, renderer used, and binary-conditioned vs authority-informed/non-binary-conditioned mode.
6. Run sequence/style/identity/spatial QC.
7. Apply editable lettering.
8. Present the complete sequence for user taste gate.

## Current visual risk to watch

The main remaining visual drift is not the core face grammar; it is:
- generic AI-like new-person face design;
- blanket beige/sepia atmosphere;
- soft global texture;
- over-rendered environment;
- full-scene regeneration during local repair.

## Current content / dialogue state

The rough story and dialogue direction passed.
The system now structurally separates:
source facts → source voice → story beats → dialogue draft → humanization → USER VOICE GATE → Voice Ledger.

Dialogue is not final until the user taste gate passes.

## Repository authority after cleanup

Read before production:
1. README.md
2. this file
3. SOURCE_STORY_PIPELINE.md
4. MASTER_PROMPTS.md
5. VISUAL_GRAMMAR.md
6. GENERATION_PROTOCOL.md
7. REFERENCE_SET.md
8. active episode package

Direct/native image generation does not waive this restore order.

Legacy overlapping root documents have been merged/retired; Git history preserves them.

## Binary reference note

The approved main-cast sheet and approved 3-person indoor scene are now committed under `assets/style_refs/v2_current/` as REF_V2_D and REF_V2_E.
Their exact paths, dimensions and SHA-256 hashes are recorded in `REFERENCE_SET.md`.

REF_V2_A, REF_V2_B and REF_V2_C remain pending binary ingest. Do not fall back to legacy v1 style references for them in a clean environment.


## Reference clarification — 2026-09-05

The three images re-shown by the user at session handoff must be interpreted as follows:

1. long-wavy-black-hair female character sheet = canonical character-style reference;
2. brown-bob female character sheet = canonical character-style reference;
3. living-room three-person scene = approved positive scene reference demonstrating how references 1/2 should extend to background + multi-person interaction.

The third image is NOT a failed/drifted example.

The actual contaminated examples are the later generations that drifted toward romance-webtoon / generic AI-pretty rendering, soft beige atmosphere, heavier shading, and altered face grammar.

Next-session restore must preserve this distinction before any new generation.
