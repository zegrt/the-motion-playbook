# The motion playbook

```
  ·          ·        ·       ·     ·    ·   ·  · · ●

  t h e   m o t i o n   p l a y b o o k
  craft, judgment and technique for motion work
```

Craft, judgment and technique for motion work, written so it plugs into any project and any tool (After Effects, Rive,
Premiere, Resolve, Blender...), for people and for AI agents alike. It's meant to get sharper with every production,
not longer.

This is the public edition: the universal layers. A studio or team adds its own house layer (`houses/<company>/`), and
each person their own profile (`profiles/<name>.md`); none ship here.

## Where things live

| Path | What |
|---|---|
| `SKILL.md` | the entry point for agents: what to read at each stage, precedence, how to propose a lesson |
| `CORE.md` | seven principles, one page; read before any work |
| `craft/` | tool-free rules by domain |
| `tools/` | how to do it in a given tool; dated, with versions |
| `process/` | how work is checked and run, in any domain |
| `QUICKSTART.md` | for someone new: install, profile, what to read, how to send a lesson |
| `scripts/lint.py` | the cheap checks: rule ids and fields, links, private details, word budgets |
| `kit/` | the production book kit |
| `profiles/` | `_template.md`: copy it to write your own taste and way of working |
| `houses/` | not included: your company's brand, characters and standards go here |
| `inbox/` | proposed changes and lessons, waiting for approval; see its README |

When two layers disagree: the project's own decisions win, then the directing person's taste profile, then the house,
then the core. Within a project, the director's latest approved direction beats older records; history is context.

```
  ┌───────────────────────────────┐
  │ the project's own decisions   │  wins
  ├───────────────────────────────┤
  │ the director's taste profile  │
  ├───────────────────────────────┤
  │ the house layer (your studio) │
  ├───────────────────────────────┤
  │ core · craft · tools · process│  the base
  └───────────────────────────────┘
```

## Using it with an agent

The folder is itself an Agent Skill (`SKILL.md` at the root). Link it in once, wherever you cloned it. Mac or Linux:

    mkdir -p ~/.claude/skills ~/.codex/skills
    ln -s "$PWD" ~/.claude/skills/motion-playbook   # Claude Code
    ln -s "$PWD" ~/.codex/skills/motion-playbook    # Codex

Windows (PowerShell), with your clone's path:

    New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills", "$env:USERPROFILE\.codex\skills"
    New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\motion-playbook" -Target "<your clone>"
    New-Item -ItemType Junction -Path "$env:USERPROFILE\.codex\skills\motion-playbook" -Target "<your clone>"

No project has to carry anything for the playbook to work.

## How rules are written

Each rule is a short card:

- **Rule**: what to do, in a line or two.
- **Why**: the reason it works.
- **Basis**: what it rests on. It starts with one or more of: *principle* (how motion and perception work), *measured*
  (we checked it on screen), *technical fact* (true of the medium or a tool, with the version), *practice* (a way of
  working that held up in production, or what practitioners do), or *taste* (whose). Then, where it helps, how much
  stands behind it: one case, one production, a director's notes. In the shared layers a director is named by role
  ("one director's notes"), never by name; their own taste lives in their profile.
- **Scope**: where it applies (any, any camera-based scene, 2D, interactive...).
- Only when they add something: **Unless** (when it doesn't apply, or which rule wins), **Check** (how to verify it),
  **In tools** (where the tool-specific how-to lives).

When observations conflict, write the tradeoff (an Unless line) instead of letting the newest case overwrite the rule.

Every rule has an `id` so other files link to it instead of copying it. Examples in the universal folders stay generic;
real project cases live in the house layer and link to rule ids, never the other way round.

Tool notes use a different card, because a software quirk is searched by its symptom: **Symptom**, **Cause**, **Fix**,
**Seen** (tool version and date). A technique rather than a quirk has no Symptom: its heading names what it solves, and
its card can be a Fix alone. Each tool file says at the top which version its notes were seen in, or that the version
wasn't recorded.

## Coverage

What the playbook holds, and the gaps known so far, for the work it serves: films, product motion (pieces an app
plays) and ads. In a gap there's no rule to cite, so say so when a brief lands there, and capture what you learn as a
proposal.

| Area | Holds | Known gaps |
|---|---|---|
| Story and edit | beats, time on screen, cutting, transitions, reviewing the whole at speed, versions and variants | the hook (the first seconds of a feed ad); compressing a story into a 6 or 15 second cutdown (`story.edit-points` plans the edit points, not the cut) |
| Motion and timing | phrasing, speed and curves, overlap, groups, timing to sound, ambient life, effects and loops | timing for interface motion (durations and feedback for UI transitions) |
| Scenes and camera | depth and space, lens and camera, continuity between shots, composition | the craft of reframing one shot for other aspect ratios (planning the versions is held: `story.edit-points`, `sound.music-versions`); platform safe zones (captions, buttons and overlays in feeds) |
| Character | from look development to a character in a scene: motion language, poses, rigs, props, feet, eyes, expression | none known |
| Look and finish | building a look, light and value, colour and reading size, finishing, output and QC | none known |
| Type on screen | reading size (`look.viewing-size`); key lines on screen for muted viewing (`sound.sound-off`); a held read for information and labelled numbers (`story.read-time`); rolling numbers that keep their meaning (`scene.meaning-checks`, and `ae.odometer` in After Effects) | type as the main motion (kinetic type, legibility while moving beyond numbers); caption design; logo and end-card reveals |
| Sound and VO | writing and timing VO, AI voice, handing off to an engineer, music and licences, effects, delivery and loudness | none known |
| Interactive | settling behaviour, structure, the app's contract, start, waiting, reduced motion, interruption, checking on the device | a motion spec page for engineers, putting the contract (`interactive.contract`) and the curves as values (`motion.curve-tokens`) in one handoff with durations, springs and the exported files |
| Process | verification; the working agreement and the wrap; the production book, its method and kit | a first real production run through the kit |
| Tools | After Effects, Rive; audio and encoding (ElevenLabs, ffmpeg, whisper.cpp, reportlab) | Premiere, Resolve, Figma, Blender, Lottie, code (CSS, SwiftUI, Compose); video specs per platform (bitrate, size and length limits) |

By kind of work, the gaps that matter most:
- **Ads:** the hook, cutdowns, reframing and safe zones, type and captions, logo and end card, platform video specs.
- **Product motion:** the motion spec page for engineers, interface timing, Lottie and code.
- **Film:** notes for Premiere, Resolve and Blender, and the production book kit proved on a real production.

## Sending changes

Every production feeds what it learned back in, which is how the playbook gets sharper:

```
   plan ─► build ─► review ─► finish ─► deliver
                                           │
   playbook ◄─ wrap ◄─ inbox ◄─ lessons ◄──┘
```

Lessons and changes go through `inbox/`, one file each; [inbox/README.md](inbox/README.md) has the format. Pull requests
are welcome. This repository is published from a main edition: an accepted pull request is brought into it and released
here with the next update, so the pull request itself is closed, not merged.

## Licence

The text is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0): see [LICENSE](LICENSE).
Attribute it as "the motion playbook, by Cyril", with a link to this repository.
