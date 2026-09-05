# E006 — 알아서 하라며?

Status: L1-L7 REVIEW CANDIDATE — USER VOICE GATE NEXT
Updated: 2026-09-06

## 1. Topic reset

The previously approved dentist-language-misunderstanding package is superseded for E006 by the user's new topic selection.

Do not render the old E006 EPISODE_PLAN / RENDER_MANIFEST.
They remain repository history only until the new L8 package is approved and the structured plan is rebuilt.

New selected topic:
- workplace / office-life contradiction;
- employees are expected to act independently, but independent action can trigger "why didn't you tell me?";
- asking for direction can trigger the opposite complaint: "do I have to tell you everything?" / "figure it out yourself."

## 2. Provenance candidate

Primary human-source seed:
- Reddit r/living_in_korea_now
- thread: "is there a middle ground in korean work culture"
- URL: https://www.reddit.com/r/living_in_korea_now/comments/1w68bje/is_there_a_middle_ground_in_korean_work_culture/
- source pattern: the poster describes experiencing two opposite workplace extremes — a micromanaging boss who wants every action reported and, elsewhere/at other times, an expectation to invent work and decide independently without asking.

Provenance class: HUMAN_SEEDED_INSPIRATION.

Source-faithfulness rule:
- preserve the contradiction itself;
- do not falsely claim the source described one literal boss delivering both lines in one incident;
- a compressed/composite episode may dramatize the contradiction, but it must be framed as a recognizable repeated workplace pattern rather than a verbatim single-event reenactment.

## 3. L1-L7 review candidate

### L1 SOURCE DISCOVERY
Selected because the human post contains a clean, sceneable contradiction with strong office-worker recognition value.

### L2 HUMAN-INTEREST GATE
PASS candidate:
- immediate conflict without exposition;
- highly recognizable office frustration;
- dialogue-driven and cheap to stage visually;
- can work with one recurring lead plus episode-local boss/coworker, or entirely episode-local cast;
- no need to force all three main characters into the episode.

### L3 SOURCE NORMALIZATION
SOURCE FACTS / PATTERN:
- one extreme: manager wants constant updates and permission before independent action;
- independent action can be met with "why didn't you tell me?";
- opposite extreme: worker is expected to find or define work independently;
- asking what to do can be met with "do I have to tell you what to do?" / "don't come ask me what you should do."

SOURCE VOICE TO PRESERVE:
- frustration comes from contradictory expectations, not from incompetence;
- the comedy is the impossible decision rule;
- avoid turning it into a generic anti-company rant or moral lecture.

### L4 STORY SHAPE
CONTRADICTION_LOOP / OFFICE-RELATABLE.

### L5 STORY BEATS — draft
1. HOOK — protagonist gets a small task and decides it is simple enough to handle.
2. AUTONOMY PUNISHED — after completing it, boss reacts: "이걸 왜 보고도 없이 진행했어?"
3. ADAPTATION — next task arrives; protagonist now asks before acting.
4. ASKING PUNISHED — boss reacts: "이런 것까지 하나하나 물어봐야 돼? 좀 알아서 해."
5. LOOP REALIZATION — protagonist freezes, mentally comparing the two opposite rules.
6. LANDING — next task arrives; protagonist's hand hovers between 'ask' and 'just do it' while an internal caption lands the contradiction.

### L6-L7 DIALOGUE / HUMANIZATION — draft
- boss A / first beat: "이걸 왜 보고도 없이 진행했어?"
- protagonist, next time: "이건 이렇게 처리하면 될까요?"
- boss / opposite beat: "이런 것까지 하나하나 물어봐야 돼? 좀 알아서 해."
- final internal line candidate: "그래서... 물어봐? 말아?"

Dialogue should feel like ordinary office speech, not meme catchphrases.
The final line may be tightened after user review.

## 4. Episode cast decision — not yet locked

This episode follows the project-wide cast-routing policy in MASTER_PROMPTS.md §5 and GENERATION_PROTOCOL.md §0.5; that policy is not redefined here.

E006-specific unresolved choice:
- protagonist: one recurring lead OR one episode-local employee;
- boss: episode-local supporting character;
- optional coworker/reaction character only if a beat materially improves with them.

Only the resolved E006 cast belongs in this episode package.

## 5. Exact next gate

User reviews the L1-L7 package above.
If approved:
1. lock cast;
2. derive episode-local identity digests as needed;
3. build the six-slide storyboard/visual plan;
4. regenerate EPISODE_PLAN / RENDER_MANIFEST;
5. only then return to L13 first-frame rendering.
