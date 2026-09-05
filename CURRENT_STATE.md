# CURRENT_STATE.md

# LIVE STATE — 2026-09-05

Repository: noru358/instatoon

## Big flow

Style reset complete → real omnibus pilot E002 → fresh coordinated 7-slide visual pass → dialogue/layout refinement → first publishable episode → repeat prototypes → automation implementation.

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

Active episode: episodes/E002/README.md

## E002 — current diagnosis

Working story:
blind-date man borrows Harin's phone and uses her account to follow himself.

Casting:
- Harin = recurring main character;
- blind-date man = episode-only character in THIS episode.

Important clarification:
There is no global Taemin ban.
Future episodes may use Taemin when story/context calls for him.
E002 specifically uses a different one-off man.

### First visual pass

Strengths:
- scene composition;
- café staging;
- shot variety;
- Harin expression;
- overall comic-scene feel

were better than later retries.

Problems:
- male visually drifted too close to Taemin/main-cast solution;
- text was too small / too detached as top narration;
- coloring/background had some generic AI-like warm texture/atmosphere;
- final two beats were accidentally reversed.

Correct ending order:
REVEAL / self-follow → AFTERMATH / “아 집가고 싶다”.

### Later retry

Improved:
- larger mobile-readable text;
- more explicit speech-bubble treatment.

Regressed:
- male face became a generic smooth AI-like one-off face;
- character drawing became awkward;
- composition, scene design and visual rhythm became substantially worse than first pass;
- the retry should NOT become the new visual anchor.

## Current hard lesson

Do not solve one local problem by fully regenerating a good frame.

Use:
LAST_KNOWN_GOOD → local change only.

For a new non-main person appearing in 2+ cuts:
STORY/CONTEXT → INTERNAL IDENTITY DIGEST → COORDINATED EPISODE BATCH.

This internal continuity operation is not a separate user-facing character-sheet or approval stage.

This applies across future sessions and episodes.

## Exact next action

1. Do NOT depend on recovering either prior E002 pass; episode visuals may be prototyped fresh each run.
2. From the approved story/context, internally derive one E002-only blind-date-man identity digest.
   - fits a plausible blind-date context;
   - distinct from Taemin;
   - current v2 visual style;
   - no generic smooth AI face.
3. Use that same internal identity digest across a fresh, coordinated seven-slide visual pass; do not stop for a separate character-sheet approval.
4. Generate text-free raster production art with deliberate shot variation and coherent café continuity.
5. Apply the text system as editable layout:
   - larger type;
   - narration / speech bubble / reaction roles separated.
6. Enforce numeric slide order and correct last two beats.
7. Run whole-sequence QC.
8. Present the whole new sequence together for user taste gate.

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

Read:
1. README.md
2. this file
3. SOURCE_STORY_PIPELINE.md
4. MASTER_PROMPTS.md
5. VISUAL_GRAMMAR.md
6. GENERATION_PROTOCOL.md
7. REFERENCE_SET.md

Legacy overlapping root documents have been merged/retired; Git history preserves them.

## Binary reference note

The approved v2 image references from this session are not yet committed as binaries through the available GitHub connector.
Do not fall back to legacy v1 style references in a clean environment.


## Reference clarification — 2026-09-05

The three images re-shown by the user at session handoff must be interpreted as follows:

1. long-wavy-black-hair female character sheet = canonical character-style reference;
2. brown-bob female character sheet = canonical character-style reference;
3. living-room three-person scene = approved positive scene reference demonstrating how references 1/2 should extend to background + multi-person interaction.

The third image is NOT a failed/drifted example.

The actual contaminated examples are the later generations that drifted toward romance-webtoon / generic AI-pretty rendering, soft beige atmosphere, heavier shading, and altered face grammar.

Next-session restore must preserve this distinction before any new generation.
