# instatoon

Semi-automated Instagram-toon production system.

The project is built around **style reproducibility + whole-episode visual grammar**. The durable identity is the overall drawing language and page/sequential grammar, not a requirement for recurring characters.

## Authoritative hierarchy

When documents conflict, use this precedence:

1. **STYLE_LOCK.md** — highest illustration-style authority.
2. **VISUAL_GRAMMAR.md** — episode/page/sequential-grammar authority.
3. **STORY_GRAMMAR.md** — active anecdote/experience/incident/relatable story grammar.
4. **SOURCE_STORY_PIPELINE.md** — source filtering, human-interest gate, and whole-story planning.
5. **TOON_SYSTEM_V0_1.md** — system architecture, data flow, automation/cost policy.
6. **MASTER_PROMPTS.md** — canonical reusable style prompt blocks.
7. **GENERATION_PROTOCOL.md** — generation, preflight, repair, and QC procedure.
8. **REFERENCE_ANALYSIS.md** — detailed visual deconstruction and rationale.
9. **CURRENT_STATE.md** — live handoff/state.
10. **WORKFLOW_PROTOCOL.md** — cross-environment continuity and `갱신` procedure.
11. Episode-specific content and tool prompts.

A lower layer may add content but may not weaken or reinterpret a higher layer.

## Core rules

> Plan the whole episode before rendering any individual slide.

> Preserve the visual language before optimizing beauty, detail, novelty, speed, or tool-specific aesthetics.

> Keep semantic text in editable vector layers rather than baking it into generated art.

The target illustration language is a warm, restrained, low-detail Korean everyday anecdote-comic style with thin charcoal-brown linework, muted warm colors, minimal shading, quiet low-detail backgrounds, and controlled visual density.

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
- **INSTATOON_STYLE_v1.1 — 2026-09-04**
- **INSTATOON_VISUAL_GRAMMAR_v0.1 — 2026-09-04**

## Files

- [STYLE_LOCK.md](STYLE_LOCK.md)
- [VISUAL_GRAMMAR.md](VISUAL_GRAMMAR.md)
- [STORY_GRAMMAR.md](STORY_GRAMMAR.md)
- [SOURCE_STORY_PIPELINE.md](SOURCE_STORY_PIPELINE.md)
- [TOON_SYSTEM_V0_1.md](TOON_SYSTEM_V0_1.md)
- [MASTER_PROMPTS.md](MASTER_PROMPTS.md)
- [GENERATION_PROTOCOL.md](GENERATION_PROTOCOL.md)
- [REFERENCE_ANALYSIS.md](REFERENCE_ANALYSIS.md)
- [CURRENT_STATE.md](CURRENT_STATE.md)
- [WORKFLOW_PROTOCOL.md](WORKFLOW_PROTOCOL.md)
