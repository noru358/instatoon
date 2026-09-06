# E001 — RESET START

Status: AWAITING_REVISED_SCREEN_SEQUENCE_APPROVAL
Created: 2026-09-06

This is the first episode after the user-directed episode reset.

## Approved content
- L1-L7 package: PASS
- L8 USER VOICE GATE: PASS
- ending lock: no protagonist explanation, no narration/internal monologue, final landing is silent extreme embarrassment
- pre-raster package: user PASS
- corrected S01 with user-supplied style reference: USER PASS as visual/taste anchor only

## Invalid / retired current-episode prototypes
- the first S01 generated without actual required reference media is discarded and must never be reused
- old phone-centric prototype frames after S01 are non-authoritative because systemic screen/UI geometry defects were found
- do not promote those outputs into continuity anchors

## Structural fix applied
Project-wide rules now require:
- adjacent-beat visual-delta / merge review before slide locking
- one visual-information owner per slide
- explicit screen-bearing prop contract
- physically compatible character gaze / device face / camera view
- screen UI only on the real display face
- reaction-led phone scenes use a natural handset + UI inset when necessary
- screen-information-led scenes use POV/over-shoulder/other physically valid screen-readable views
- interface profile is context-routed
- contemporary Korean everyday messaging defaults to KakaoTalk-inspired grammar when no service is explicitly named
- meaning-bearing message text/read counts remain vector/layout by default
- missing required reference media is a hard stop before raster generation

## Revised E001 sequence — 6 slides
1. uncomfortable customer interaction; helper coworker steps in
2. worker_01 alone in staff nook, opens messenger
3. SEND + WRONG-CHAT REALIZATION merged into one reaction-led slide; KakaoTalk-inspired UI appears as vector inset with rapidly decrementing read-status
4. delete/too-late beat uses a physically valid over-shoulder/POV screen-information shot
5. private coworker DM uses a natural handset + separate DM inset; mortified frozen reaction
6. silent whole-body embarrassment landing; no text

## Current artifacts
- STORY_SOURCE_PACK.md
- EPISODE_PLAN.json — revised six-slide screen-safe plan
- RENDER_MANIFEST.json — rebound to exact revised plan blob
- LETTERING_PLAN.json — revised six-slide layout
- PRODUCTION_STATE.json

## Next action
User reviews the revised S03-S05 screen-safe sequence / six-slide plan.
On PASS:
1. advance state to render-contract-ready;
2. run render guard;
3. verify actual required reference media is present in the renderer;
4. regenerate only the affected phone-centric slides under the new contracts;
5. internal QC must include screen/device geometry before style/taste QC.
