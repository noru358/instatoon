# WORKFLOW_PROTOCOL.md

# CROSS-ENVIRONMENT / “갱신” PROTOCOL v1.3
Updated: 2026-09-05

Purpose:
Preserve current decisions, prompts, assets, execution evidence, failure lessons, exact next actions, and stage-level accountability across ChatGPT, Claude, local work, and future automation.

## 0. Meaning of “갱신”

When the user says “갱신”, do NOT merely append a handoff.

Run repository reconciliation:

1. fetch current remote state;
2. read every current root Markdown authority and relevant active-episode Markdown;
3. build an internal conflict/duplication map;
4. merge still-valid old rules into current authorities;
5. remove or explicitly retire contradictions/duplication;
6. prefer editing existing canonical files over creating new session files;
7. update active episode evidence;
8. update CURRENT_STATE last;
9. commit/push;
10. refetch/verify remote state before saying completion;
11. update AutoPipeline child pointer when applicable.

Git history is the archive.
Root Markdown should describe the present.

## 1. No chat-memory dependency

If a clean environment would need a decision to continue correctly, GitHub must contain it.

Preserve:
- project purpose;
- current stage;
- current style;
- exact canonical prompt;
- content/story/dialogue workflow;
- cast-routing rule;
- character/reference identities;
- known failure modes;
- active episode state;
- last-known-good logic;
- exact next action.

## 2. File-proliferation rule

Do not create:
- NEW_SESSION_HANDOFF;
- LATEST;
- FINAL_FINAL;
- per-session duplicate prompt documents

when an existing authority can be coherently updated.

A new file is justified for:
- an independently auditable episode;
- a genuinely new authority/spec;
- binary/reference asset;
- schema with its own lifecycle.

When an old root document is fully superseded:
1. merge still-useful content;
2. remove the current duplicate;
3. rely on Git history for historical recovery.

## 3. Mandatory restore pack

Before production in a clean session, read:

1. README.md
2. CURRENT_STATE.md
3. SOURCE_STORY_PIPELINE.md
4. MASTER_PROMPTS.md
5. VISUAL_GRAMMAR.md
6. GENERATION_PROTOCOL.md
7. REFERENCE_SET.md
8. active episode README/package

Do not produce a new story frame after reading only MASTER_PROMPTS or only CURRENT_STATE.

For automation implementation, also read AUTOMATION_TRANSITION.md.

## 4. During-work recording

Record durable changes in the proper authority:

- style/prompt change → MASTER_PROMPTS + STYLE_LOCK
- reference promotion/retirement → REFERENCE_SET
- story/dialogue/cast workflow → SOURCE_STORY_PIPELINE
- text/composition/layout → VISUAL_GRAMMAR
- generation/repair/QC → GENERATION_PROTOCOL
- active episode result → episode package
- current stage/next action → CURRENT_STATE
- cross-session procedure → WORKFLOW_PROTOCOL
- future code contract → AUTOMATION_TRANSITION

Do not leave a cross-session rule only in chat.

## 5. Cast / episode-character portability rule

Story/context decides whether an episode uses:
- Gaeun;
- Harin;
- Taemin;
- one-off cast;
- a mixture.

There is no default main-character insertion merely by gender.
There is no global Taemin ban.

If a new non-main character appears in 2+ cuts:
1. derive the person internally from story/context;
2. record one compact episode-only identity digest;
3. render the whole episode batch with that same digest.

Do not insert a separate user-facing character-sheet or approval stage by default.

This rule survives session changes.

## 6. Last-known-good portability rule

A repair must start from the best accepted prior state, not automatically from the latest generated state.

Record when useful:
- which frame/reference is LAST_KNOWN_GOOD;
- what is accepted;
- what exact defect remains.

If a retry regresses:
- reject it;
- do not chain from it;
- return to the prior accepted base.

## 7. “갱신” reconciliation order

A. Fetch remote.
B. Sweep current root Markdown + active episode Markdown.
C. Reconcile decisions and contradictions.
D. Update durable authorities.
E. Update episode evidence.
F. Update CURRENT_STATE last.
G. Commit/push.
H. Refetch changed files/tree.
I. Verify exact remote HEAD.
J. Update parent AutoPipeline pointer if present.

Never say “갱신 완료” before H/I.

## 8. Asset integrity

Text is not a lossless substitute for important image/audio authority.

If a binary reference controls visual identity:
- preserve the actual asset in GitHub when the environment/tool permits;
- record exact path/hash after upload;
- never claim it is preserved when it is not.

If the current connector cannot upload the binary:
- document the gap explicitly;
- never fall back to an obsolete asset silently.

## 9. Minimal-change preservation

When the user approves most of a frame and requests one fix:

LOCAL ISSUE:
- edit the target only;
- preserve all unmentioned composition/style/identity/geometry.

SYSTEMIC ISSUE:
- repair the shared prompt/reference/layout system;
- rerun only affected dependencies.

Do not regenerate the entire visual package to fix a local defect unless targeted editing is impossible.

## 10. Environment portability

Canonical docs use repository-relative paths.
Do not depend on:
- a desktop path;
- hidden chat context;
- one model's memory;
- an unrecorded UI choice.

Never commit secrets.

## 11. AutoPipeline relationship

Target parent:
noru358/AutoPipeline

Child repository remains creative/project authority.
Parent records the exact child commit combination.

Update child first.
Then advance parent pointer to the verified child commit.

## 12. Automation-transition preservation

If manual production discovers a durable rule that future code must enforce, update both:
- the current production authority;
- AUTOMATION_TRANSITION.md when it changes orchestration/state/schema behavior.

Examples:
- new episode-only identity-continuity stage;
- last-known-good state;
- USER VOICE GATE;
- sequence-order validation;
- new deterministic text-layout rule;
- mandatory stage execution reporting.

## 13. Mandatory stage execution report

During active production, do not silently jump across stages.

After each meaningful pipeline stage completes, report it to the user even when they did not explicitly ask for a status report.

For every reported stage include:
- STAGE: canonical stage/layer name;
- WORKER ROLE: researcher, story editor, dialogue writer, storyboard/cast director, character designer, visual director, renderer, letterer, QC, performance analyst, etc.;
- EXECUTION ACTOR: the actual actor that performed it (for current manual/chat mode this may be the same ChatGPT orchestrator operating in a bounded role; do not pretend separate agents ran when they did not);
- INPUT: exact upstream artifact/state used;
- SOURCE / PROVENANCE: URLs, posts, user-provided material, repository file, or explicitly “original/internal premise — no external source”;
- OUTPUT: concrete artifact/result produced;
- STATUS: pass / fail / blocked / awaiting user gate;
- QC: key checks performed and defects found;
- NEXT: exact next stage.

Source collection must never imply external provenance when none exists.
Visual generation must state which exact style and character reference assets were actually supplied to the renderer.
If required canonical binaries were not supplied, report that as a production defect rather than implying reference compliance.

For long runs, stage reports may be grouped into a compact progress table, but every completed stage must remain auditable.

## 14. Definition of lossless

A competent person/model in a clean environment can determine:
- what this project makes;
- what is locked;
- what was tried;
- what failed and why;
- what assets/prompts are current;
- what the active episode is;
- what to do next;
- which worker role executed each production stage and from what source/input;

without the previous chat transcript.

Lossless means decision/state fidelity, not copying conversational noise.
