# CURRENT_STATE.md

# LIVE STATE — 2026-09-05

Repository: noru358/instatoon

## Big flow

Style reset complete → source-first manual production → coordinated text-free raster pass → lettering/QC → publishable episodes → repeat prototypes → automation implementation.

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
- HUMAN-SOURCE-FIRST provenance;
- source-voice / dialogue-humanization / USER VOICE GATE workflow;
- native/direct ChatGPT image generation as a first-class raster path after authority preflight.

Active episode: episodes/E005/README.md

## E005 — current production package

Fresh NEW_EPISODE routing completed from L1.

Human-seeded base:
- Reddit r/tifu "TIFU by texting my date that I might end up marrying him seconds after we ended our date"
- https://www.reddit.com/r/tifu/comments/i4jtsd/
- later four-year update reports that the pair eventually married.

Current stage:
- L1-L7 complete;
- L8 USER VOICE GATE explicitly PASS by user;
- L10 STORYBOARD + CAST ROUTER PASS;
- L11 EPISODE-LOCAL CHARACTER DESIGN PASS;
- L12 WHOLE-EPISODE VISUAL PLAN PASS;
- E005 README + EPISODE_PLAN.json materialized;
- L12.5 render contract was hardened after the failed native S01 style pass;
- root cause: the old guard verified that canonical refs existed but did not verify that the renderer actually received them;
- current v2 episodes now declare reference_conditioning_requirement = BINARY_REQUIRED;
- render_guard authorization now requires BINARY_CONDITIONED plus evidence that every required canonical ref was actually supplied as renderer media;
- native/direct paths without a repository-binary reference bridge are BLOCKED before raster generation rather than allowed to fail after generation;
- prior E005_S01 remains INVALID; S02 is not authorized.

Cast:
- no recurring main-cast character is used;
- woman_01 and man_01 are both episode-only to avoid turning the sourced marriage outcome into recurring main-cast canon;
- both have STRICT_EPISODE identity digests in the E005 package.

Visual plan:
- seven 4:5 text-free raster slides;
- first-date medium two-shot → apartment-door goodbye → keys-in-hand impulsive text → wrong-recipient reaction → damage control → reply reaction → restrained wedding/update aftershock;
- final lettering will frame the ending as "4년 뒤 근황 / 진짜 결혼함." for source accuracy.

Exact next action:
1. select or expose a renderer path that can accept REF_V2_D and REF_V2_E as actual media inputs;
2. prove both required refs in the authorize supplied-ref evidence;
3. compile/authorize E005_S01 under BINARY_CONDITIONED;
4. render E005_S01 only;
5. run semantic/style/identity QC and authorize S02 only after PASS.

## E004 — current production package

Fresh new-work routing restarted from L1 and did NOT reuse E003.

Human-seeded base:
- Reddit r/tifu "TIFU by letting a girl off at the wrong floor like it was her stop"
- https://www.reddit.com/r/tifu/comments/1l8jkeq/
- used as inspiration/base, not literal adaptation.

Current story:
Taemin shares an apartment elevator with a woman he has never met, presses 21 for her and 17 for himself, then reflexively tells her "먼저 내리세요" when the doors open at his own 17th floor. She reminds him she is on 21; he realizes he has effectively tried to eject her at his floor and exits into concentrated awkwardness.

Current stage:
- L1-L7 complete;
- L8 USER VOICE GATE intentionally deferred until before final lettering because raster masters are text-free;
- L9 has no new durable voice rule yet;
- L10-L12 complete;
- L12.5 RENDER CONTRACT GATE complete;
- E004 EPISODE_PLAN.json + SHA-bound RENDER_MANIFEST.json materialized;
- executable render guard + regression tests + GitHub Actions are active;
- prior unrelated native outputs are INVALID/discarded and do not count as L13 artifacts;
- L13 is reset to FIRST-FRAME SEMANTIC GATE NEXT.

Cast:
- Taemin = recurring REF_V2_D main-cast identity.
- Episode-only woman = continuity digest recorded in E004; preserve across slides 01-05.

## E003 status

E003 remains preserved as prior human-seeded production work and is no longer the active new-work target unless the user explicitly returns to it.

Its source/story/dialogue/storyboard package remains valid in episodes/E003/README.md.
The historical Higgsfield no-credit failure was provider-specific and never invalidated native/direct generation.

## Current renderer rule

Native/direct ChatGPT image generation is first-class and may be used without invoking Higgsfield.

Before direct generation:
1. restore the canonical Markdown production pack;
2. inspect the current visual binaries when the runtime can expose them;
3. use MASTER_PROMPTS + observed reference traits + episode visual plan;
4. if the renderer cannot accept the repository binaries as explicit media inputs, report AUTHORITY-INFORMED / NON-BINARY-CONDITIONED honestly rather than pretending they were injected;
5. never fall back to retired v1 assets.

For E004 in the present chat:
- repository authorities and the exact REF_V2_D / REF_V2_E binary identities/paths were restored;
- native image generation does not expose those GitHub JPEG binaries as explicit renderer media inputs;
- therefore any direct pass must be logged as AUTHORITY-INFORMED / NON-BINARY-CONDITIONED unless the runtime gains a reference-media bridge.

## Current hard lessons

Do not solve one local problem by fully regenerating a good frame.

Use:
LAST_KNOWN_GOOD → local change only.

For a new non-main person appearing in 2+ cuts:
STORY/CONTEXT → INTERNAL IDENTITY DIGEST → COORDINATED EPISODE BATCH.

This internal continuity operation is not a separate user-facing character-sheet or approval stage.

New-work commands such as "새 만화" always restart from fresh human-source discovery unless the user explicitly requests continuation/repair.

## Exact next action

1. Run `python pipeline/render_guard.py validate`.
2. Compile and authorize E004_S01 from the structured contract.
3. Because the native/direct renderer is conversation-inferred, render exactly ONE frame only.
4. Run semantic/style/identity QC on S01.
5. Continue to S02 only if S01 PASS; repeat this gate for every frame.
6. Preserve Taemin and woman_01 continuity and the 17F/21F spatial logic.
7. Keep raster text-free; lettering remains after the voice gate.

## Current visual risk to watch

The main remaining visual drift risks are:
- generic AI-like new-person face design;
- blanket beige/sepia atmosphere;
- soft global texture;
- over-rendered environment;
- main-cast identity drift;
- full-scene regeneration during local repair.

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

## Binary reference note

The approved main-cast sheet and approved 3-person indoor scene are committed under `assets/style_refs/v2_current/` as REF_V2_D and REF_V2_E.
Their exact paths, dimensions and SHA-256 hashes are recorded in `REFERENCE_SET.md`.

REF_V2_A, REF_V2_B and REF_V2_C remain pending binary ingest. Do not fall back to legacy v1 style references for them in a clean environment.

## Reference clarification — 2026-09-05

The canonical interpretation remains:
1. long-wavy-black-hair female character sheet = canonical character-style reference;
2. brown-bob female character sheet = canonical character-style reference;
3. living-room three-person scene = approved positive scene reference demonstrating how the character style extends to background + multi-person interaction.

The third image is NOT a failed/drifted example.

Actual contamination means romance-webtoon / generic AI-pretty rendering, soft beige atmosphere, heavier shading, and altered face grammar.


## Render-contract hardening — 2026-09-05

The repeated wrong-story native-render failure is now treated as an orchestration defect, not a reminder problem.

Repository-wide controls now active:
- schemas/episode_plan.schema.json
- schemas/render_manifest.schema.json
- pipeline/render_guard.py
- pipeline/test_render_guard.py
- .github/workflows/render-guard.yml
- per-episode EPISODE_PLAN.json
- per-episode SHA-bound RENDER_MANIFEST.json

Global policy:
- no free-form render from chat memory;
- active episode / plan / manifest must match;
- plan mutation invalidates old manifest;
- required current reference paths must exist;
- unexpected concepts are FAIL_CLOSED;
- explicit compiled-payload renderers first-frame gate the batch;
- conversation-inferred renderers are sequential and gate every frame;
- semantic mismatch stops the run immediately and can never become LAST_KNOWN_GOOD/reference.

Verified regression coverage includes:
- active-episode mismatch rejection;
- stale-manifest rejection;
- deterministic E004 prompt binding;
- conversation-inferred next-frame rejection without prior QC PASS.

This materially reduces recurrence and, crucially, prevents a wrong output from propagating through the rest of the episode. Model/renderer misbehavior can still occur, so zero-error generation is not guaranteed; the system is designed to detect and contain it before continuation.
