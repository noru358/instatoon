# AUTOMATION_TRANSITION.md

# MANUAL/CHAT → EXECUTABLE AUTOPIPELINE CONTRACT
Updated: 2026-09-05
Status: FUTURE IMPLEMENTATION AUTHORITY

## 0. Purpose

Convert the validated manual Instatoon workflow into a reproducible Python/CLI/server pipeline later.

Do not automate the chat itself.
Automate the production state machine that the chat is currently operating.

## 1. Ownership split

### Repository documents/config define WHAT is correct
Current project authorities:
- MASTER_PROMPTS.md
- STYLE_LOCK.md
- REFERENCE_SET.md
- SOURCE_STORY_PIPELINE.md
- VISUAL_GRAMMAR.md
- GENERATION_PROTOCOL.md

### Python defines WHEN/HOW execution proceeds
Code owns:
- stage order;
- input/output schemas;
- retries;
- timeouts;
- approval waits;
- budgets;
- tool adapters;
- prompt assembly;
- persistence;
- QC routing;
- artifact paths;
- publishing;
- analytics ingestion.

Docs/config = policy.
Python = orchestration/enforcement.

## 2. Target stage machine

Current conceptual flow:

SOURCE_CANDIDATES
→ HUMAN_SOURCE_SEED_CHECK
→ SOURCE_SELECTED
→ SOURCE_NORMALIZED
→ STORY_PLANNED
→ DIALOGUE_DRAFTED
→ DIALOGUE_HUMANIZED
→ USER_VOICE_GATE
→ STORYBOARD_PLANNED
→ CAST_ROUTED
→ EPISODE_IDENTITY_REQUIRED?
→ EPISODE_IDENTITY_READY
→ VISUAL_PLAN_READY
→ RASTER_RENDER
→ VECTOR_LETTER
→ FINAL_QC
→ HUMAN_TASTE_GATE
→ EXPORT_READY
→ PUBLISHED
→ PERFORMANCE_RECORDED

The episode-identity branch is required only for a new non-main person appearing in 2+ cuts. It is an internal state transition, not a human approval gate or mandatory standalone character-sheet render.

## 3. New mandatory runtime concepts

### A. EpisodeCharacterIdentity
Fields should eventually include:
- identity_id;
- episode_id;
- character_role;
- main_cast_or_episode_only;
- identity traits;
- compact identity digest;
- optional temporary anchor artifact path/hash only when continuity repair needs one;
- style version;
- status;
- last_known_good flag.

### B. LastKnownGood
Every repairable stage may point to an accepted prior artifact/state.

If a retry regresses:
- reject retry;
- restore last_known_good;
- do not chain future generation from the failed retry.

### C. VoiceGate
Dialogue cannot silently pass from draft into production while the project is still learning user voice.

Store:
- draft;
- humanized draft;
- user feedback;
- accepted dialogue;
- reusable voice rule when appropriate.

### D. StageExecutionReport
Every completed stage emits an auditable report.

Fields:
- stage_name;
- worker_role;
- execution_actor;
- input_artifact_ids;
- source_provenance;
- output_artifact_ids;
- status;
- qc_summary;
- blocker;
- next_stage;
- exact reference assets actually supplied when the stage is visual generation.

The runtime must not claim that separate agents ran when one orchestrator executed multiple bounded roles.

### E. OrderedBeat
Story order is data, never inferred from file creation time.

Each slide has:
- index;
- beat role;
- state_before;
- state_after;
- reader_question_after;
- landing/reveal relation.

## 4. Typed-stage philosophy

A model reasons inside a bounded stage.
It does not invent a new workflow after failure.

Examples:

HUMAN_SOURCE_SEED_CHECK
input: source candidates + user premise
output: selected human-produced base material, provenance class (literal source / inspiration base / composite seed / pure original fallback), and reason

SOURCE_NORMALIZE
input: raw source
output: source facts + source voice + provenance

STORY_PLAN
input: source pack + content grammar
output: ordered beats

DIALOGUE_HUMANIZE
input: beats + source voice + draft
output: humanized dialogue + flagged AI-like lines

CAST_ROUTE
input: story/context
output: selected main cast + episode-only roles + rationale

EPISODE_CHARACTER_IDENTITY
input: episode-only role + style refs
output: identity digest + optional temporary internal anchor only when needed

RASTER_RENDER
input: slide spec + exact references + prompt + renderer capability profile
output: art artifact + metadata + reference-conditioning mode

Renderer selection rule:
- native/direct image generation is a valid first-class renderer;
- do not invoke an external provider merely because it is connected;
- external provider use requires explicit user request, a missing native capability, or a provider/automation test;
- one provider's credit failure does not block RASTER_RENDER if another valid renderer path exists.

QC
input: planned beat + refs + artifact
output: pass/fail + defect codes + repair scope + last-known-good action

## 5. Prompt assembly

Prompt assembly must be deterministic code.

Load exact current blocks from MASTER_PROMPTS.md or a version-linked machine-readable mirror.

Inputs:
- current restore-pack/version check;
- renderer capability profile;
- scene facts;
- story clarity;
- output ratio;
- text-safe region;
- selected main-character reference;
- episode-local identity digest;
- current style reference;
- last-known-good repair reference when needed;
- stable visual blocks.

The model must not rewrite the project style each time.

## 6. Reference-role separation

Runtime must distinguish:
- RENDERER;
- REFERENCE_CONDITIONING_MODE = BINARY_CONDITIONED | AUTHORITY_INFORMED_NON_BINARY_CONDITIONED;
- STYLE_REFERENCE;
- MAIN_CHARACTER_REFERENCE;
- EPISODE_CHARACTER_IDENTITY;
- LAST_KNOWN_GOOD_FRAME;
- LOCATION_CONTINUITY_REFERENCE when needed.

One role must not silently replace another.

Legacy v1 style assets must be excluded by version/status.

## 7. Repair routing

### Local defect
Examples:
- wrong one-off character identity;
- one hand;
- one prop;
- one expression;
- text placement.

Route:
TARGETED_REPAIR from last-known-good.

### Systemic defect
Examples:
- every background becomes over-rendered;
- every new-person face becomes generic;
- entire batch uses wrong style;
- typography system is unreadable.

Route:
repair shared prompt/reference/layout configuration, then rerun only dependent outputs.

No unbounded “try again”.

## 8. Deterministic validations

Prefer code for:
- required fields;
- slide indices;
- no duplicate/missing order;
- REVEAL before AFTERMATH;
- output dimensions;
- file hashes;
- text safe margins;
- text overflow;
- minimum font sizes;
- bubble ownership/tail metadata;
- reference status/version;
- episode-only identity digest presence when required;
- retry/budget limits.

Use model/vision judgment only where semantics or visual taste require it.

## 9. Runtime storage

GitHub:
- durable project authorities;
- versioned prompts;
- canonical references;
- schemas/config;
- approved episode artifacts when useful.

Runtime DB:
- run/stage state;
- stage execution reports with worker role / actual execution actor / provenance / outputs / QC;
- attempts;
- approvals;
- tool IDs;
- costs;
- timestamps;
- QC results.

Object storage:
- large/transient generated assets when server automation arrives.

Git is not the live job queue.

## 10. Integration hierarchy

Manual/chat production:
1. native/direct ChatGPT generation when it satisfies the required visual task;
2. connected external renderer only when explicitly requested or materially necessary.

Executable AutoPipeline:
1. official provider API;
2. MCP when cross-client interoperability matters;
3. internal adapter;
4. browser automation fallback.

Renderer choice is capability-driven, not habit-driven.

Browser/UI automation must be isolated behind adapters.

## 11. First executable product

CLI first, not dashboard.

Capability target:

autopipeline run instatoon --source <input>
autopipeline status <run-id>
autopipeline approve <run-id> voice-gate
autopipeline approve <run-id> taste-gate
autopipeline retry <run-id> --slide 5 --scope character
autopipeline export <run-id>

Exact syntax may change.

Success means one run can proceed without hidden chat memory.

## 12. Cost controls

Every generation stage records:
- renderer/tool;
- reference-conditioning mode;
- exact visual authorities inspected;
- exact media inputs supplied when supported;
- whether generation was paid, unlimited, or native;

Every paid stage additionally records:
- estimated cost if available;
- actual cost;
- provider/tool job ID;
- attempts;
- budget ceiling.

Use:
- whole-story planning;
- one internal context-derived identity digest per relevant one-off;
- one first pass;
- targeted repair;
- bounded retries.

Automation is not permission for unattended spend.

## 12.5 Human-source-first default

Unless the user explicitly requests pure invention, source discovery should attempt to attach real human-produced material before story planning.

The runtime may:
- use one human anecdote as a base;
- combine multiple human anecdotes/comments into a composite seed;
- heavily fictionalize/restructure after collection.

It must distinguish:
- literal-source adaptation;
- inspiration/base provenance;
- composite human-seeded premise;
- pure original fallback.

The purpose is not factual purity. The purpose is to preserve human specificity, cadence, social awkwardness, and non-generic detail while preventing the model from inventing an entire premise in a vacuum by default.

## 13. Human gates

Current learning-phase human ownership:
- source/premise approval when requested;
- USER VOICE GATE;
- final taste/publish decision;
- material style/visual-grammar changes.

Some operational gates may later become configurable after repeated evidence.

Performance data may NOT silently mutate:
- style;
- reference promotion;
- visual grammar;
- voice rules;
- mandatory main-cast policy.

## 14. AutoPipeline ownership

Generic orchestration belongs in noru358/AutoPipeline.

Instatoon child repository owns:
- creative rules;
- prompts;
- refs;
- content grammar;
- project config.

Do not duplicate Instatoon-specific truths into the generic engine.

## 15. Suggested implementation sequence

Phase 0 — continue manual evidence extraction.
Phase 1 — finalize schemas.
Phase 2 — local CLI + state machine.
Phase 3 — generation/research/publish adapters.
Phase 4 — persistent DB/workers/object storage.
Phase 5 — web control plane.
Phase 6 — controlled autonomy.

Do not build a polished dashboard before the engine works.

## 16. Anti-patterns

Do not:
- give one supervisor every tool and say “make a post”;
- depend on chat memory;
- duplicate prompts in many code locations;
- use a failed render as the next continuity base;
- improvise a one-off character independently panel by panel instead of carrying one identity digest;
- let file creation order define slide order;
- let QC rewrite the whole episode;
- loop paid generation indefinitely;
- use Git as a runtime queue;
- start browser-first when API/MCP exists.

## 17. Automation-complete definition

First automation milestone is complete when:
1. clean environment discovers all project authorities;
2. one command creates a persisted run;
3. stages use typed inputs/outputs;
4. episode-only identity-continuity requirements are enforced without adding a human gate;
5. exact refs/prompts/versions are recorded;
6. last-known-good repair works;
7. retries are bounded;
8. voice/taste gates are explicit;
9. story order is deterministic;
10. final assets are auditable;
11. core style/voice cannot silently mutate;
12. the generic engine can load another child project without copying Instatoon logic;
13. every completed stage is auditable by worker role, actual execution actor, provenance/input, output, QC verdict, and next stage.


## 16. RenderContract / PromptBinding runtime contract

Mandatory states now include:
VISUAL_PLAN_READY → EPISODE_PLAN_MATERIALIZED → RENDER_MANIFEST_BOUND → RENDER_PREFLIGHT_VALIDATED → FIRST_FRAME_RENDER → FIRST_FRAME_SEMANTIC_QC → RASTER_RENDER.

Runtime must persist the episode-plan Git blob SHA, render-manifest path, prompt-binding mode, per-slide required/forbidden entities, and semantic-QC continuation state.

Prompt-binding modes:
- EXPLICIT_COMPILED_PAYLOAD: first-frame semantic gate, then remaining batch may continue.
- CONVERSATION_INFERRED: one frame at a time; every next frame requires previous-frame semantic QC PASS.

Any plan mutation invalidates the prior manifest. No raster call may occur before preflight PASS. A semantic mismatch stops the run and cannot become LAST_KNOWN_GOOD.

Executable baseline is pipeline/render_guard.py with validate, compile, and authorize commands. CI must run its regression tests and validate the active episode.
