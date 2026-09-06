# MASTER_PROMPTS.md

# INSTATOON ASSET AUTHORING PROMPT AUTHORITY v3.0
Updated: 2026-09-07

This file no longer defines a prompt for generating every complete final slide.
It defines the reusable prompt grammar for **ASSET_GAP authoring** and explicit full-frame exceptions.

Final frames are normally built by deterministic composition under ASSET_COMPOSITION_PROTOCOL.md.

## 1. Drawing-language core

Use the approved Instatoon references as the visual authority.

Target:
- simple hand-drawn 2D Instagram webcomic;
- black outlines with slight natural irregularity;
- flat local colors;
- minimal modeled shading;
- simple nose/mouth;
- reference-consistent eye grammar;
- hair as broad readable masses;
- contemporary clothing simplified into clear shapes;
- character/background rendered with the same drawing language.

Reject:
- generic polished AI/webtoon/anime beautification;
- glossy hair or detailed irises;
- cinematic lighting, depth of field, vignette or global beige wash;
- realistic material rendering;
- hyper-detailed environments;
- decorative polish not evidenced by the approved references.

STYLE_LOCK.md owns pass/fail interpretation.

## 2. Reference roles

REF_V2_D:
- person style + selected recurring identity.

REF_V2_E:
- scene/background drawing-language evidence + multi-person coherence.

REF_V2_SUB_01:
- optional secondary style evidence.

Never infer current pose, camera, action or location from a reference merely because it is attached.

## 3. Asset-authoring contract

Each generation request should author the **smallest missing production asset** that can close the current ASSET_GAP.

Examples:
- one character pose/view/expression asset;
- one episode-local supporting-person pose;
- one prop;
- one background/local plate;
- one FX asset;
- one interaction/contact asset when simple composition cannot express it.

Do not generate a whole final comic frame merely because one component is missing.

Preferred output for composable foreground elements:
- isolated subject;
- clean transparent or easily removable background when the renderer can provide it;
- complete anatomy for every visible limb needed by the intended crop;
- no lettering, caption, speech bubble, logo or UI text.

For a background plate:
- no character unless the asset definition explicitly includes one;
- no meaning-bearing text;
- enough margin for crop/reframing;
- same simplified drawing language as the person assets.

## 4. Character identity block

When authoring a recurring main character:
- bind the actual selected identity reference;
- preserve face proportions, eye grammar, hair silhouette/color and clothing identity declared by the asset request;
- do not import the appearance of unselected cast members.

When authoring an episode-only person:
- use the style reference for drawing language only;
- derive age/presentation/body/hair/clothing from the story contract;
- make the person visibly distinct from recurring leads.

## 5. Pose / expression block

The asset request owns:
- body view/orientation;
- pose;
- gesture;
- expression amplitude;
- prop interaction.

Do not default every asset to the same safe three-quarter portrait.
Expression may be strong when the beat requires it, but must remain inside the approved identity/style.

High-risk anatomy/contact must remain physically plausible.

## 6. Background / prop block

Story semantics own location and prop choice.

Backgrounds:
- large simple shapes;
- low detail density;
- flat local color;
- only location-identifying information;
- enough compositional flexibility to crop or place characters differently.

Screen-bearing props:
- produce physically valid device geometry;
- keep meaning-bearing UI/text blank for deterministic composition unless the asset is only a non-semantic shell.

## 7. Output block

Default asset output:
- one asset;
- one image file;
- no multi-panel/grid/contact sheet;
- no baked dialogue/caption;
- no unrelated character/scene;
- no extra variants unless explicitly requested.

The asset registry, not the prompt, decides whether an output is approved for production.

## 8. Repair block

Repair from the last known good asset when practical.

Preserve every accepted property not implicated in the defect.
Do not redesign identity, palette, pose, background or style while fixing one local issue.

## 9. Full-frame exception

A complete final-frame generation prompt is allowed only when ASSET_COMPOSITION_PROTOCOL declares an exception.

It must explicitly state:
- why normal composition is insufficient;
- exact scene semantics;
- bound references;
- no text;
- episode-local scope by default.

An exception output never becomes project-wide style/identity authority automatically.
