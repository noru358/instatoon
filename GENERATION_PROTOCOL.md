# GENERATION_PROTOCOL.md

# Generation & QC protocol — INSTATOON_STYLE_v2.0
Updated: 2026-09-04

## 1. Plan before rendering

Required before a production episode:
- approved source/angle;
- story beats;
- humanized dialogue;
- USER VOICE GATE status during prototype phase;
- slide/scene count;
- character roster (recurring vs episode-only);
- location per scene;
- key props/actions/reactions;
- output track(s).

Do not render first and invent the story afterward.

## 2. Output tracks

Primary:
- Instagram carousel/feed toon: 4:5, target 1080×1350.
- Reels/Shorts: 9:16, target 1080×1920.

16:9 is not a project default.
Use it only for explicit landscape/long-form derivative content.

Build one semantic scene specification, then adapt composition for each target ratio.
Do not stretch finished art.

## 3. Environment policy

There is no mandatory permanent background-anchor library.
Story determines location.
Generate environments using the background style lock in MASTER_PROMPTS.md.

Create an episode-local or recurring-location anchor only when:
- the same place repeats across multiple beats/episodes;
- spatial continuity matters;
- re-generation drift becomes a real problem.

## 4. Character policy

Recurring main characters use their identity anchors/notes.
Episode-only characters may be generated on demand and kept only as temporary continuity references for that episode.

Current main cast:
Gaeun / Harin / Taemin.
Harin uses black socks when visible.
Taemin uses the current approved 2026-09-04 black-haired identity.

## 5. Raster prompt assembly

Order:
1. scene facts;
2. story beat / clarity;
3. output ratio/composition;
4. recurring or episode-local identity continuity;
5. approved visual reference when available;
6. MASTER VISUAL STYLE LOCK;
7. ENVIRONMENT / BACKGROUND STYLE LOCK;
8. ANTI-GPT / ANTI-POLISH LOCK.

Do not rewrite the style ad hoc for every scene.

## 6. Text layer

For final production, keep important captions/dialogue editable outside the generated raster whenever possible.
This improves typo correction, voice iteration, layout control, and multi-format adaptation.

Quick prototypes may contain generated text, but they are not automatically final masters.

## 7. First-pass QC order

1. Does the beat read immediately?
2. Does dialogue still sound human?
3. Does the image match STYLE_LOCK v2.0?
4. Is recurring identity preserved?
5. Are one-off characters internally consistent where needed?
6. Are hands/objects/feet/seating/spatial relations plausible?
7. Is the environment simple enough?
8. Is there sufficient text safe space?
9. Is the target ratio correct?

## 8. Hard stop / repair

Systemic style drift across multiple frames:
STOP and repair reference/prompt assembly.

Single local defect:
target-edit that frame; preserve accepted areas.

Weak story/dialogue:
return to story/dialogue layers rather than trying to save it with prettier art.

## 9. Minimal-change edit

When a frame is accepted except for a named defect:
change only the named defect.
Preserve unmentioned identity, composition, style, palette, geometry, and narrative function.

## 10. Automation boundary

Automation may:
collect/normalize sources, route formats, draft story beats, draft dialogue, humanize dialogue, assemble prompts, generate storyboards, run deterministic QC, and prepare exports.

During the current learning phase, USER VOICE GATE remains explicit before dialogue lock.
Style or voice rules do not silently mutate from performance feedback.
