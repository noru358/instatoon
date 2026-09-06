# CURRENT_STATE.md

Updated: 2026-09-07
Repository: noru358/instatoon

## SESSION HANDOFF — RESET BOUNDARY / DO NOT CONTINUE LEGACY E001

Canonical user decision:
- all concrete episode content created before the redesigned production system is retired;
- production numbering restarts from a fresh E001 under the new AutoPipeline structure;
- project-wide workflow/style/reference/QC lessons remain active.

Conflict detected in this session:
- this file and `pipeline/render_guard.py` still assume one parseable active episode;
- the current `episodes/E001` package is therefore still present as a legacy machine fixture/state;
- continuing, rendering, repairing, or creatively extending that E001 would mix retired episode content with the new system.

Execution authorization: **BLOCKED_RESET_PENDING**.

The parseable line below is retained temporarily only because the current render guard and CI require it. It does **not** authorize creative continuation of this episode.

Active episode: episodes/E001/README.md

### Completed before handoff
- 2026-09-07 approved creative baseline was merged into `VISUAL_GRAMMAR.md`.
- AutoPipeline durable artifact bridge and PROJECT/EPISODE work-scope separation are merged.
- Parent AutoPipeline was pinned to the approved instatoon/jipbap creative-baseline revisions before this reset conflict was detected.
- No new redesigned E001 story package was created in this session.

### Unapproved source candidate for the fresh E001
- Human-source candidate: https://theqoo.net/job/4123344083
- Seed fact: while cleaning advertisement chat rooms, the poster accidentally left a four-year work team group chat containing work history and photos and had no backup.
- Status: **CANDIDATE ONLY / NOT USER-APPROVED / DO NOT STORYBOARD YET**.

### Exact next single action
In a new session:
1. re-read AutoPipeline and instatoon authority;
2. change the state/render-guard contract so `Active episode: NONE` is a valid fail-closed non-rendering state;
3. move the current legacy `episodes/E001` package out of the active production namespace without losing useful failure evidence;
4. set no active episode and run CI;
5. only then start the fresh E001 at L1-L7 and present the L8 package for explicit user approval.

Reason for new-session handoff: repository authority conflicts with the current canonical reset decision, which is a configured context-contamination signal.

## Canonical operating mode — MANUAL_VALIDATION

Standard topology:
`pre-raster content/plan → S01 USER anchor → S02..final OPERATOR INTERNAL QC → complete text-free raster-set USER gate → lettering/final USER gate`.

One slide = one image file.
One slide != one user approval gate.

## Episode reset boundary
All concrete pre-reset episode content remains retired.
Project-wide workflow/style/reference/QC lessons remain active.

## E001 reconciled state
- L1-L7: PASS
- L8 USER VOICE GATE: PASS
- pre-raster plan gate: PASS
- first S01 attempt without required reference media: INVALID / DISCARDED
- corrected S01 after user supplied reference: USER PASS visual/taste anchor only; not machine-bound
- later phone-centric prototypes: NOT APPROVED / NON-AUTHORITATIVE after systemic screen/UI geometry defects
- current plan: revised from 7 to 6 slides
- revised six-slide screen-safe plan: USER PASS (`ㅇㅋ`)
- current stage: RENDER_CONTRACT_READY
- current checkpoint: REFERENCE_MEDIA_PREFLIGHT_BLOCKED

## Global structural fix now canonical

### Adjacent visual-delta / merge
Story beats are not automatically separate slides.
Adjacent low-delta beats must be reviewed for merge before slide locking.
UI-state-only or tiny-reaction continuations are merge candidates.

### Visual information ownership
Every slide declares one primary information owner:
CHARACTER_REACTION / SCREEN_INFORMATION / PHYSICAL_ACTION / ENVIRONMENT / RELATIONSHIP / MIXED_WITH_DECLARED_PRIORITY.

### Screen-bearing prop contract
Every screen-bearing slide declares:
- subject-screen relation
- camera-screen relation
- geometry contract
- UI profile
- UI delivery mode

Hard failures:
- UI on device back/case
- impossible character/camera screen orientation
- private phone unnaturally presented to the audience solely to expose information
- screen/reaction/UI all forced into one incompatible composition

### Interface routing
UI profile is context-routed, not episode-hard-coded.
Contemporary Korean ordinary personal/group messaging with no named service defaults to:
`KR_EVERYDAY_MESSENGER_KAKAOTALK_INSPIRED`.

Meaning-bearing chat text, room names, read/unread numerals and decrement/disappearing read-status effects are normally vector/layout content.

### Reference fail-closed
If required style/reference media is not actually available to the active renderer/tool, STOP and tell the user.
Do not make a prompt-only production image.

## E001 revised six-slide sequence
1. customer conflict + coworker intervention
2. private staff nook / opens messenger
3. send + wrong-chat realization MERGED; reaction-led + KakaoTalk-inspired UI inset
4. delete/too-late; over-shoulder/POV screen-information shot
5. coworker private DM; reaction-led + DM inset
6. silent embarrassment landing

## Reference binding
Canonical v2 production references remain:
- `assets/style_refs/v2_current/REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg`
- `assets/style_refs/v2_current/REF_V2_E_3PERSON_INDOOR_SCENE.jpeg`

Both remain BINARY_REQUIRED where the episode contract lists them.

## Exact next action
Do not render yet.
REF_V2_D has an equivalent attached copy in the active conversation, but REF_V2_E does not.
Obtain/attach the approved REF_V2_E 3-person indoor/background application reference, then revalidate actual media delivery and regenerate only the affected phone-centric slides under the new screen contracts.
