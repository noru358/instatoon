# E001 — RESET START

Status: AWAITING_PRE_RASTER_PLAN_GATE
Created: 2026-09-06

This is the first episode after the user-directed episode reset.

## Reset boundary
- All prior concrete episode premises, dialogue, storyboards, render plans, production states, raster outputs, lettering outputs, and approvals from former E001-E007 are retired from current execution.
- Project-wide structural rules, style/reference authority, QC lessons, workflow contracts, and automation/pipeline improvements remain active.
- Git history preserves retired episode material; current production must not reuse it unless the user explicitly requests recovery.

## Current pipeline state
- Episode ID: E001
- L1-L7: APPROVED
- L8 USER VOICE GATE: PASS — user said "합격"
- L10 STORYBOARD + CAST ROUTER: COMPLETE, awaiting pre-raster review
- L11 EPISODE-LOCAL CHARACTER DESIGN: COMPLETE internally for worker_01
- L12 WHOLE-EPISODE VISUAL PLAN: COMPLETE
- L12.5 RENDER CONTRACT: MATERIALIZED, not yet raster-authorized
- Raster generation: BLOCKED until pre-raster user gate passes and state advances

## Cast
- recurring main cast: none
- worker_01: episode-only protagonist, mid-20s service worker, strict episode continuity
- customer: one-frame extra
- helper coworker: one-frame extra
- private coworker in S06: text-only sender, not a physical character

## Seven-slide storyboard
1. uncomfortable customer interaction; helper coworker steps in
2. worker_01 alone afterward, opens phone to tell friends
3. sends "오늘 우리 매장 애들 진짜 미쳤다"
4. realizes the header says workplace group; "...어?"
5. deletes immediately, but 43 people have already read it
6. private DM arrives: "괜찮아?" / "무슨 일 있었어?"
7. no reply, no narration, no text — only extreme embarrassment

## Current artifacts
- STORY_SOURCE_PACK.md
- EPISODE_PLAN.json
- RENDER_MANIFEST.json
- LETTERING_PLAN.json
- PRODUCTION_STATE.json

## Next action
User reviews the pre-raster cast/storyboard/visual/render package.
On explicit PASS:
1. advance plan/state to raster-ready;
2. rebind manifest/lettering if the EPISODE_PLAN blob changes;
3. run full render-guard validation;
4. restore/supply actual REF_V2_D + REF_V2_E media;
5. generate only E001_S01 as the USER visual anchor.
