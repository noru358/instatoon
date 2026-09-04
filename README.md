# instatoon

Semi-automated Instagram-toon / shorts-toon production system.

This repository is intentionally built around **style reproducibility first**. The project may later automate ideation, scripting, panel planning, generation, QC, packaging, and distribution, but visual identity must not drift as automation increases.

## Authoritative hierarchy

When any prompt, agent, script, tool setting, handoff, or future document conflicts with another, use this precedence:

1. **STYLE_LOCK.md** — highest visual authority. Never override implicitly.
2. **MASTER_PROMPTS.md** — canonical reusable prompt blocks implementing the style lock.
3. **GENERATION_PROTOCOL.md** — required assembly order, generation procedure, and QC.
4. **REFERENCE_ANALYSIS.md** — detailed visual deconstruction and rationale.
5. **CURRENT_STATE.md** — current project state, decisions, next work.
6. Episode / scene / tool-specific prompts.
7. Ad-hoc generation wording.

A lower layer may add scene-specific content but may not weaken or reinterpret a higher layer.

## Core rule

> Preserve the visual language before optimizing beauty, detail, novelty, speed, or tool-specific aesthetics.

The target is **not** a polished romance-webtoon or anime look. It is a warm, restrained, low-detail Korean everyday anecdote-comic language with simple adult characters, thin charcoal-brown linework, muted warm colors, minimal shading, quiet low-detail backgrounds, and highly controlled visual density.

## Change control

Locked visual rules are versioned. Do not change them because a model or tool appears to produce a "prettier" result. A lock changes only after explicit review of generated comparisons and an explicit project decision.

Current canonical style version: **INSTATOON_STYLE_v1.0 — 2026-09-04**

## Files

- [STYLE_LOCK.md](STYLE_LOCK.md) — non-negotiable visual bible
- [MASTER_PROMPTS.md](MASTER_PROMPTS.md) — copy/paste master, negative, identity, and scene prompt blocks
- [GENERATION_PROTOCOL.md](GENERATION_PROTOCOL.md) — prompt assembly order + QC + drift handling
- [REFERENCE_ANALYSIS.md](REFERENCE_ANALYSIS.md) — detailed style anatomy
- [CURRENT_STATE.md](CURRENT_STATE.md) — live handoff/state

