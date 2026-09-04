# CURRENT_STATE.md

# Current state — 2026-09-04

Repository: `noru358/instatoon`

## Big flow

**Style reset complete → real omnibus pilot production → QC / voice learning → repeat prototypes → automation implementation**

## Current detailed step

The previous visual style has been abandoned.
INSTATOON_STYLE_v2.0 is now the approved visual direction.

Passed tests:
- two user-provided character-sheet references established the target face/line/color grammar;
- background-style sample passed;
- main-cast sheet passed after Harin sock correction and Taemin identity replacement;
- three-person interaction + indoor environment test passed.

Therefore visual-style exploration is closed unless a real production failure reveals a new systemic issue.

## Content definition

The channel is an omnibus short-story / situation comic system.
Sources may come from internet communities, SNS, comments, submissions, real-life observations, or limited original creation.

Main cast may recur but is not mandatory in every episode.
Episode-only characters are expected.

Default distribution:
- Instagram toon/carousel: 4:5, 1080×1350;
- Reels/Shorts: 9:16, 1080×1920;
- 16:9 only when explicitly needed.

Fixed background anchors are not a required production stage.
Story determines the environment; recurring locations may receive anchors later if continuity requires them.

## Story / dialogue architecture

Canonical layered flow:
source collection → selection → source facts + source voice → story beats → dialogue draft → dialogue humanization → USER VOICE GATE → Voice Ledger update → storyboard → image/video → QC → performance feedback.

The USER VOICE GATE is intentionally manual during the learning period because the user wants to remove AI-sounding dialogue structurally rather than repair it ad hoc forever.

## Active pilot episode

Working concept: blind-date phone self-follow anecdote.

Casting:
- female: Harin (main cast);
- male: episode-only one-off character.

Approved:
- concept;
- Harin + one-off male casting;
- 7-beat structure;
- 4:5 primary format;
- casual/unpolished dialogue direction.

A first-pass 4:5 art sequence has been generated.
It is NOT yet publish-locked.
Next action: perform whole-sequence QC for story logic, dialogue naturalness, Harin identity continuity, one-off male continuity, scene order, style drift, text accuracy, and composition; then repair only named failures.

## Visual authority

`MASTER_PROMPTS.md` = single canonical production prompt.
`STYLE_LOCK.md` = normative pass/fail style boundary.
`SOURCE_STORY_PIPELINE.md` = content + dialogue layer architecture.
`GENERATION_PROTOCOL.md` = render/QC procedure.

IMPORTANT:
The old files under `assets/style_refs/` belong to the pre-reset style unless REFERENCE_SET.md explicitly promotes a replacement asset.
Do not use legacy assets as current visual authority.

## Automation status

Still semi-manual.
The goal remains eventual Python/state-machine automation with repository locks/prompts as configuration and explicit stage outputs.
Do not automate away the USER VOICE GATE until enough preference data has accumulated.
