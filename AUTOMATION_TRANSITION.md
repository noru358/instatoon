# AUTOMATION_TRANSITION.md

# INSTATOON — MANUAL/CHAT → EXECUTABLE AUTOPIPELINE TRANSITION CONTRACT

**Status:** FUTURE IMPLEMENTATION AUTHORITY  
**Effective:** 2026-09-04

## 0. Purpose

This document preserves the decisions required to convert the current structured-but-manually-operated Instagram-toon workflow into a reproducible Python/CLI/server pipeline later.

It is intentionally written now, while the production protocol, prompts, locks, failure lessons, and human gates are still being discovered manually.

This document **does not authorize skipping the current three-prototype extraction program** and does not replace the current human Gate A / Gate B / Gate C rules during v0.1.

When implementation begins, a clean coding agent/person should be able to read this file plus the authorities linked from `README.md` and know what must become code, what must remain configuration/locks, and what must never be left to chat memory.

---

## 1. Core migration thesis

Do **not** automate the ChatGPT conversation itself.

Automate the production system that the conversation is currently operating manually.

Target transformation:

```text
CURRENT

human/chat
  → read repo
  → remember rules
  → choose next stage
  → assemble prompts
  → call tools
  → inspect result
  → decide retry/repair
  → update state

TARGET

deterministic orchestrator
  → load canonical project authorities
  → execute typed stage
  → call model/tool adapter
  → validate structured output
  → run QC
  → bounded retry / targeted repair
  → persist state/evidence/cost
  → advance state machine
```

The orchestrator owns the flow.  
The model reasons **inside a stage**.

Do not give one supervisor model every tool and ask it to “make an episode end-to-end” without deterministic control.

---

## 2. What stays in documents/config vs what becomes Python

### Documents / YAML / JSON define **WHAT is correct**

Keep durable creative/product truth outside application code:

- project purpose;
- style/version locks;
- canonical reference identity and hashes;
- visual grammar;
- story grammar;
- source-selection rules;
- canonical prompt blocks;
- human gate policy;
- QC rubrics and hard-fail conditions;
- budget policy;
- project-specific workflow configuration.

Current authorities already provide most of this:

- `STYLE_LOCK.md`
- `REFERENCE_SET.md`
- `VISUAL_GRAMMAR.md`
- `STORY_GRAMMAR.md`
- `SOURCE_STORY_PIPELINE.md`
- `MASTER_PROMPTS.md`
- `GENERATION_PROTOCOL.md`
- `TOON_SYSTEM_V0_1.md`

Do not bury these rules as opaque Python strings unless a machine-readable mirror is explicitly introduced and version-linked to the human-readable authority.

### Python defines **WHEN / HOW execution proceeds**

The executable layer should own:

- stage order;
- input loading;
- prompt assembly;
- schema validation;
- tool/API invocation;
- timeouts;
- retry counts;
- retry routing;
- budget ceilings;
- approval waits;
- state transitions;
- manifest/event logging;
- deterministic QC;
- artifact paths;
- publishing calls;
- analytics ingestion.

Short rule:

> Docs/config = policy and truth.  
> Python = orchestration and enforcement.

---

## 3. Deterministic orchestration first

Target design is approximately:

- deterministic/state-machine control for stage order, retries, budgets, approvals, persistence;
- model reasoning only where semantic judgment or generation is actually needed.

This is **not** a multi-agent swarm or debate system.

A stage may use an LLM, vision model, image generator, or tool, but the stage must have a typed contract and a bounded outcome.

Bad:

```text
"Read everything and autonomously make the best Instagram toon."
```

Good:

```text
SOURCE_NORMALIZE
  input: raw source
  output: STORY_SOURCE_PACK schema
  validator: required fields + provenance

STORY_PLAN
  input: source pack + grammar versions
  output: STORY_PLAN schema
  validator: structural checks + Gate B routing

RASTER_RENDER
  input: one slide spec + exact canonical refs + assembled prompt
  output: artifact + generation metadata
  validator: dimensions/hash/provenance

QC_IMAGE
  input: slide spec + render + relevant locks
  output: typed pass/fail + defect codes + repair scope
```

The model must not choose an unbounded new workflow because one stage failed.

---

## 4. State machine

The executable system should represent a run explicitly.

Illustrative state flow:

```text
SOURCE_CANDIDATES
→ SOURCE_SELECTED
→ SOURCE_NORMALIZED
→ STORY_PLANNED
→ GATE_B_WAIT
→ EPISODE_PLANNED
→ PREFLIGHT_READY
→ PREFLIGHT_RENDERED
→ PREFLIGHT_QC
→ PRODUCTION_RENDER
→ VECTOR_COMPOSE
→ FINAL_QC
→ GATE_C_WAIT
→ EXPORT_READY
→ PUBLISHED
→ PERFORMANCE_RECORDED
```

Failure transitions are explicit:

```text
PREFLIGHT_QC_FAIL_STYLE
  → repair shared prompt/reference assembly
  → rerun bounded preflight

SLIDE_QC_FAIL_LOCAL
  → targeted repair only
  → rerun affected slide QC

BUDGET_EXCEEDED
  → human approval / stop

SYSTEMIC_UNKNOWN_FAILURE
  → stop, preserve evidence, do not free-form loop
```

Never use an infinite “keep trying until it looks good” loop.

---

## 5. Typed stage contracts

Every generative stage should return machine-readable data first.

Example QC shape:

```json
{
  "episode_id": "E0002",
  "stage": "image_qc",
  "slide_index": 5,
  "status": "fail",
  "scores": {
    "style": 94,
    "story_clarity": 88,
    "anatomy": 61
  },
  "fail_codes": [
    "HAND_OBJECT_CONTACT"
  ],
  "repair_scope": [
    "right_hand",
    "held_object"
  ],
  "next_action": "TARGETED_IMAGE_REPAIR"
}
```

A free-form explanation may be stored as evidence, but routing must depend on stable typed fields/enums.

Finalize real JSON Schemas only after the three-prototype extraction program exposes the recurring fields and failure classes.

---

## 6. Prompt assembly must be code, not model improvisation

Do not ask an LLM to rediscover or rewrite the project style for every render.

The prompt assembler loads exact versioned blocks and exact selected references.

Production raster assembly remains conceptually:

```text
slide scene facts
+ story clarity
+ negative-space / no-text requirement
+ episode-local continuity when required
+ selected canonical reference paths + hashes
+ REFERENCE_OBEDIENCE_BLOCK
+ FACE_LOCK_BLOCK when applicable
+ IDENTITY_PRESERVATION_BLOCK only when applicable
+ BACKGROUND_DENSITY_LOCK when applicable
+ MASTER_STYLE_PROMPT
+ NEGATIVE_STYLE_PROMPT
+ ANTI_GPT_DEFAULT_BLOCK
```

The assembler records the exact prompt text/hash and selected reference hashes **before** the external generation call.

Chat history must never be the only source of a prompt fragment.

---

## 7. Source-of-truth split

### GitHub repository

Use Git for durable, reviewable, versioned project truth:

- locks;
- prompt blocks;
- schemas;
- workflow/config definitions;
- canonical references;
- source/story/episode plans that are part of the durable record;
- implementation code;
- migrations;
- tests.

### Runtime database

When automation is implemented, use a runtime DB such as PostgreSQL for mutable execution state:

- current run/stage;
- attempts;
- queued jobs;
- tool job IDs;
- costs;
- timestamps;
- approvals;
- publish IDs;
- analytics snapshots.

Git should not be abused as the live job queue.

### Object storage

Large generated/transient assets should move to an object store such as S3/R2 when server automation requires it.

Keep canonical visual references in the repository when practical.  
For large runtime outputs, store stable IDs/paths/hashes in manifests.

---

## 8. Tool integration hierarchy

Prefer integrations in this order:

1. official provider API;
2. stable MCP server when the capability should be shared across models/clients;
3. ordinary internal API wrapper/function when only AutoPipeline needs it;
4. browser automation (for example Playwright) only when no reliable API/MCP exists.

Do not turn every internal function into MCP by default.

Use MCP when interoperability is valuable.  
Use a normal adapter when it is simply an implementation detail of the pipeline.

Browser automation must be isolated behind an adapter because UI changes, login expiry, CAPTCHA, upload failures, and DOM drift are expected failure modes.

---

## 9. Target AutoPipeline ownership

Generic automation code belongs in the parent project, not duplicated independently in every content repository.

Target conceptual layout:

```text
AutoPipeline/
├── engine/
│   ├── orchestrator/
│   ├── stages/
│   ├── state/
│   ├── qc/
│   └── adapters/
├── cli/
├── server/
├── dashboard/          # later
├── instatoon/          # child repository / project authority
└── talkshow/           # child repository / project authority
```

The `instatoon` repository remains the project-specific authority for its style, story grammar, prompts, references, plans, and project configuration.

The parent engine reads the child project; it must not silently fork a second conflicting copy of its locks.

---

## 10. CLI is the first executable product

Do not start by building a polished web dashboard.

First implementation milestone:

```bash
autopipeline run instatoon --source <input>
autopipeline status <run-id>
autopipeline approve <run-id> gate-b
autopipeline retry <run-id> --stage raster-render --slide 5
autopipeline export <run-id>
```

The exact command syntax may change, but the capability target is fixed:

> A clean environment can run one full currently-approved production cycle from a command, with explicit human gates, persisted state, bounded retries, provenance, and reproducible prompt/reference loading.

Only after the CLI path is stable should the same engine be exposed through FastAPI/web UI/scheduler.

---

## 11. Web/server end state

Later target:

```text
Web dashboard
  → start / stop / approve / repair / inspect

API server
  → run management

Durable workflow / workers
  → long-running image/tool jobs
  → retries/timeouts/recovery

DB + object storage
  → execution state + artifacts

Project repository
  → locks/prompts/config/versioned truth
```

A dashboard should display at minimum:

- project;
- episode/run ID;
- current stage;
- gate waits;
- QC result and failure codes;
- attempts;
- cost;
- artifact previews/paths;
- prompt/reference versions;
- publish state;
- analytics when available.

The dashboard is a control surface, not the source of truth for locked creative rules.

---

## 12. Durable execution and recovery

External image/video jobs can outlive one process.

The system must eventually support:

- job polling;
- timeout policy;
- idempotent retry;
- process restart;
- recovery without restarting the entire episode;
- no duplicate paid calls after an ambiguous timeout unless job state is checked first.

Start simple if necessary:

```text
Python + Pydantic + CLI + PostgreSQL
```

Then add a durable workflow engine such as Temporal only when long-running/recovery complexity justifies it.

Do not adopt infrastructure merely because it is fashionable.

---

## 13. QC and repair policy in code

Automation must preserve the existing hierarchy:

1. deterministic structural/file checks;
2. style / visual-grammar QC;
3. defect / continuity QC;
4. lettering/layout QC;
5. human editorial/taste gate.

Important invariant:

> QC diagnoses and routes. It does not get permission to reinvent the episode.

If one defect is local, the repair scope must stay local.

If a systemic style failure appears, stop the batch and repair the shared reference/prompt system before paying for more slides.

The minimal-change edit rule in `GENERATION_PROTOCOL.md` remains binding.

---

## 14. Cost controls

Every paid/external stage should have:

- estimated cost before call when possible;
- actual cost/credits after call;
- per-stage attempt limit;
- per-episode budget;
- stop/approval threshold;
- tool job ID;
- artifact hash.

Current prototype cost gates remain the baseline:

- plan whole episode first;
- two-slide preflight;
- one first pass per planned raster page;
- targeted repair;
- bounded additional generations.

Automation is not permission to spend unattended.

---

## 15. Human gates during migration

During the current v0.1 period, preserve:

- Gate A — candidate/premise;
- Gate B — whole story plan before substantial paid rendering;
- Gate C — final taste/publish;
- explicit approval for material style/grammar version changes;
- explicit approval immediately before external paid generation where the current protocol requires it.

Later automation may make some operational gates configurable **only after repeated prototype evidence shows they are safe to relax**.

The following must never be silently changed by performance automation:

- `STYLE_LOCK.md`;
- `REFERENCE_SET.md` canonical promotion;
- `VISUAL_GRAMMAR.md`;
- story-grammar version;
- core brand positioning.

---

## 16. Suggested implementation stack

This is a recommendation, not a creative authority:

- Python;
- Pydantic / JSON Schema;
- CLI first;
- FastAPI when remote/web control is needed;
- PostgreSQL for mutable run state;
- Redis only if queue/cache needs justify it;
- S3/R2-class object storage for large runtime artifacts;
- provider SDKs / HTTP adapters;
- MCP where cross-client interoperability matters;
- Playwright only as a fallback adapter;
- Docker for reproducible deployment;
- durable workflow engine later if required;
- Next.js or equivalent dashboard only after the engine is proven.

Model/provider selection must stay replaceable behind adapters.

Do not make the pipeline dependent on one chat product, one model vendor, or one local machine.

---

## 17. Migration sequence from the current manual system

### Phase 0 — now: extract the real protocol

Complete the three prototypes.

Record:

- repeated page archetypes;
- real render-mode distribution;
- stable prompt blocks;
- stable QC fail codes;
- common repair routes;
- real generation counts;
- human decisions that could/could not be automated.

### Phase 1 — consolidate machine-readable contracts

- finalize CONTENT_MASTER schema;
- finalize STORY_PLAN schema;
- finalize EPISODE_PLAN schema;
- finalize RENDER_MANIFEST schema;
- add stage-result/QC schema;
- define project config and version identifiers.

### Phase 2 — executable local CLI

Implement:

- repository/context loader;
- deterministic state machine;
- source/story planning calls;
- prompt assembler;
- adapter interface;
- vector renderer/composer;
- manifest logging;
- deterministic QC;
- approval checkpoints.

Milestone:

`autopipeline run instatoon` can execute one episode through the current approved workflow without relying on hidden chat context.

### Phase 3 — external tool integration

Attach:

- research/source collectors;
- image-generation adapters;
- publishing adapters;
- analytics adapters.

Use API > MCP > browser fallback hierarchy.

### Phase 4 — durable server execution

Add:

- PostgreSQL run state;
- workers;
- job recovery;
- scheduler if needed;
- object storage;
- cost ledger;
- tracing/logging.

### Phase 5 — web control plane

Add:

- run dashboard;
- gate approval UI;
- artifact/QC inspection;
- manual repair controls;
- cost/analytics views.

### Phase 6 — controlled autonomy

Only after sufficient evidence:

- configurable automatic Gate A for low-risk source selection;
- automatic retries within explicit bounds;
- automatic publishing only for approved channels/policies;
- performance-driven experiment suggestions.

Do not permit automatic mutation of the core style/grammar locks.

---

## 18. Anti-patterns

Do not implement:

### A. One omnipotent supervisor prompt
“Here are 30 tools; make a post.”

### B. Chat-memory dependency
A new session should not be necessary to know the current production state.

### C. Prompt duplication
Do not keep slightly different copies of the master style prompt inside Python, an MCP server, a dashboard, and Markdown.

### D. Free-form retries
No “try again until good.”

### E. QC-as-writer
QC must not rewrite everything into a safe/bland average.

### F. Git-as-job-queue
Execution state belongs in runtime state storage.

### G. Browser-first integration
Do not scrape/click a provider UI when a stable API exists.

### H. Full web app before engine proof
The first success criterion is an executable reproducible pipeline, not a pretty dashboard.

---

## 19. Definition of automation-complete for Instatoon

The first genuinely automated Instatoon pipeline is complete when:

1. a clean environment can load the repository and discover every required authority without chat history;
2. one command/API request creates a persisted run;
3. each stage consumes/produces typed data;
4. exact prompt/reference/version provenance is recorded;
5. external calls are adapterized;
6. failures route through bounded explicit transitions;
7. process restart does not lose the run state once server persistence is introduced;
8. paid retries cannot loop indefinitely;
9. human gates are represented explicitly rather than handled through memory;
10. final artifacts and manifests can be reproduced/audited;
11. style/grammar locks cannot be silently changed by the execution engine;
12. the same generic engine can later load another project without copying Instatoon-specific logic into the engine.

---

## 20. Restore instructions for the future automation implementation session

When the user later asks to “automate Instatoon”, “code the pipeline”, “make the CLI”, or equivalent:

1. read `README.md`;
2. read `CURRENT_STATE.md`;
3. read this file;
4. read `TOON_SYSTEM_V0_1.md`;
5. read `WORKFLOW_PROTOCOL.md`;
6. follow the authority hierarchy for style/story/generation;
7. inspect the completed prototype evidence;
8. do **not** invent a new architecture from scratch unless verified prototype evidence requires a change;
9. implement the smallest end-to-end CLI slice first;
10. keep generic engine code in `AutoPipeline` and project truth in `instatoon`.

This file exists specifically so the automation work can resume later without reconstructing these decisions from this conversation.
