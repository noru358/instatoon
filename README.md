# instatoon

Semi-automated Instagram-toon production system.

The project is built around **style reproducibility + whole-episode visual grammar**. The durable identity is the overall drawing language and page/sequential grammar, not a requirement for recurring characters.

## Authoritative hierarchy

When documents conflict, use this precedence:

1. **STYLE_LOCK.md** — normative illustration-style authority: what counts as a pass or fail.
2. **REFERENCE_SET.md** — approved binary style anchors and their production roles. For an actual render, the selected binary reference is the primary visual input; it is interpreted under `STYLE_LOCK.md`.
3. **VISUAL_GRAMMAR.md** — episode/page/sequential-grammar authority.
4. **STORY_GRAMMAR.md** — active anecdote/experience/incident/relatable story grammar.
5. **SOURCE_STORY_PIPELINE.md** — source filtering, human-interest gate, and whole-story planning.
6. **TOON_SYSTEM_V0_1.md** — current semi-automated system architecture, data flow, automation/cost policy.
7. **AUTOMATION_TRANSITION.md** — future implementation contract for converting the validated manual/chat protocol into Python/CLI/server AutoPipeline execution. It does not override current prototype gates.
8. **MASTER_PROMPTS.md** — canonical reusable prompt blocks that implement the style lock.
9. **GENERATION_PROTOCOL.md** — generation, preflight, repair, and QC procedure.
10. **REFERENCE_ANALYSIS.md** — detailed visual deconstruction and test rationale.
11. **CURRENT_STATE.md** — live handoff, implementation status, blocker, and exact next action.
12. **WORKFLOW_PROTOCOL.md** — cross-environment continuity and `갱신` procedure.
13. Episode-specific source, plan, execution evidence, and tool prompts.

A lower layer may add content but may not weaken or reinterpret a higher layer.

## Core rules

> Plan the whole episode before rendering any individual slide.

> Preserve the visual language before optimizing beauty, detail, novelty, speed, or tool-specific aesthetics.

> Keep semantic text in editable vector layers rather than baking it into generated art.

The target illustration language is a warm, restrained, low-detail Korean everyday anecdote-comic style with thin charcoal-brown linework, muted warm colors, minimal shading, quiet low-detail backgrounds, and controlled visual density. Production rendering uses the approved five-image canonical reference set in `assets/style_refs/` together with an explicit face-distance/gaze lock.

The active v0.1 narrative formats are deliberately narrow:
- **STORY_ARC** — anecdotes, experiences, incidents
- **RELATABLE_SCENARIO** — one familiar behavior/situation dramatized as a mini-scene

Dormant for future expansion:
- OBSERVATION_SET
- EXPLAINER_CAUSAL
- CONTRAST_REFRAME

Community/news/personal material is a source type, not a visual format.

## Change control

Locked art-style and visual-grammar rules are versioned.

Do not mutate them because a model/tool appears to produce a “prettier” result or because one post performs differently.

Current versions:
- **INSTATOON_STYLE_v1.2 — 2026-09-04**
- **INSTATOON_VISUAL_GRAMMAR_v0.1 — 2026-09-04**
- **INSTATOON_STORY_GRAMMAR_v0.1 — 2026-09-04**

## Resume work

1. Read `CURRENT_STATE.md` for the live stage and exact next action.
2. Read the active episode's `README.md`, `CONTENT_MASTER.json`, `STORY_PLAN.json`, and `EPISODE_PLAN.json`.
3. Before production rendering, verify the selected files from `REFERENCE_SET.md` are available and use the current style version.
4. Do not infer current state from an older failure section when a later section explicitly marks the blocker resolved.
5. If the task is automation implementation / CLI / server conversion, also read `AUTOMATION_TRANSITION.md` before writing code.

## Files

- [STYLE_LOCK.md](STYLE_LOCK.md)
- [REFERENCE_SET.md](REFERENCE_SET.md) — approved canonical visual anchors, roles, and hashes
- [VISUAL_GRAMMAR.md](VISUAL_GRAMMAR.md)
- [STORY_GRAMMAR.md](STORY_GRAMMAR.md)
- [SOURCE_STORY_PIPELINE.md](SOURCE_STORY_PIPELINE.md)
- [TOON_SYSTEM_V0_1.md](TOON_SYSTEM_V0_1.md)
- [AUTOMATION_TRANSITION.md](AUTOMATION_TRANSITION.md) — future executable AutoPipeline migration contract
- [MASTER_PROMPTS.md](MASTER_PROMPTS.md)
- [GENERATION_PROTOCOL.md](GENERATION_PROTOCOL.md)
- [REFERENCE_ANALYSIS.md](REFERENCE_ANALYSIS.md)
- [CURRENT_STATE.md](CURRENT_STATE.md)
- [WORKFLOW_PROTOCOL.md](WORKFLOW_PROTOCOL.md)
