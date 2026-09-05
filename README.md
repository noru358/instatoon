# instatoon

Semi-automated omnibus Instagram-toon / short-form production system.

The project turns anecdotes, community/SNS material, everyday situations, user stories, and selected original premises into short comics and vertical short-form adaptations.

The durable identity is:
1. the approved drawing language;
2. the page/sequential grammar;
3. the editorial voice;
4. recurring characters when the story calls for them.

Main characters are reusable assets, not mandatory cast. Episode-specific characters are normal.

## Mandatory restore order

A clean session must NOT start production after reading only one random file.

Minimum restore pack:
1. CURRENT_STATE.md — exact live stage and next action.
2. SOURCE_STORY_PIPELINE.md — content, dialogue, cast-routing, and agent/layer workflow.
3. MASTER_PROMPTS.md — single canonical visual-generation prompt authority.
4. VISUAL_GRAMMAR.md — 4:5 page, lettering, composition, and sequence rules.
5. GENERATION_PROTOCOL.md — anchor/render/edit/QC procedure.
6. REFERENCE_SET.md — which visual references are current vs legacy.

Read AUTOMATION_TRANSITION.md only when implementing the CLI/server pipeline.
Read WORKFLOW_PROTOCOL.md when restoring across environments or when the user says 갱신.

## Authority order

When current documents conflict:

1. MASTER_PROMPTS.md — canonical visual prompt implementation.
2. STYLE_LOCK.md — visual pass/fail boundary.
3. REFERENCE_SET.md — approved/legacy binary reference status.
4. SOURCE_STORY_PIPELINE.md — story/dialogue/cast/agent workflow.
5. VISUAL_GRAMMAR.md — sequential, composition, and text-layout grammar.
6. GENERATION_PROTOCOL.md — rendering, episode-only identity continuity, minimal-edit, and QC execution.
7. CURRENT_STATE.md — exact current episode and next action.
8. WORKFLOW_PROTOCOL.md — cross-session reconciliation.
9. AUTOMATION_TRANSITION.md — future executable implementation contract.
10. episode-local artifacts.

A lower file may add detail but may not silently override a higher current rule.

## Current production shape

### Content
- omnibus;
- STORY_ARC and RELATABLE_SCENARIO are active;
- source may be community/SNS/anecdote/observation/user story/original;
- source facts and source voice are separated;
- dialogue passes Humanization + USER VOICE GATE during the learning phase.

### Cast
Story/context decides cast per episode.
- use Gaeun/Harin/Taemin only when editorially appropriate;
- never insert a main character merely because a scene needs a person of that gender;
- new episode-only characters are allowed;
- episode-only people are designed internally from story/context before the batch render;
- their compact identity digest is reused across the episode for continuity;
- a separate visible character sheet or user approval gate is NOT required by default.

### Visual
- current style: INSTATOON_STYLE_v2.0;
- previous tiny-eye/thin-brown-line v1.x style is retired;
- 4:5 (1080×1350) is the feed/carousel master;
- 9:16 (1080×1920) is the Reels/Shorts derivative;
- 16:9 is not a default;
- final semantic text should be editable, not baked into the raster master;
- background is story-specific, not a mandatory fixed-set library.

### Production principle

Plan the whole story first. Internally derive any episode-only character from context and carry the same identity digest across the batch. Render the episode as one coordinated multi-slide production pass, not as separate taste gates. Add typography deterministically. Repair locally from the last known good frame when one exists.

## Root files

- CURRENT_STATE.md
- MASTER_PROMPTS.md
- STYLE_LOCK.md
- REFERENCE_SET.md
- SOURCE_STORY_PIPELINE.md
- VISUAL_GRAMMAR.md
- GENERATION_PROTOCOL.md
- WORKFLOW_PROTOCOL.md
- AUTOMATION_TRANSITION.md

Old overlapping root specifications are merged/retired; Git history is the archive.

## Current episode

See episodes/E002/README.md.

episodes/E001/ is preserved as a historical pre-v2 prototype and is not current style authority.
