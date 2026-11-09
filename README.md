# The motion playbook

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
| `profiles/` | `_template.md`: copy it to write your own taste and way of working |
| `houses/` | not included: your company's brand, characters and standards go here |
| `inbox/` | proposed changes and lessons, waiting for approval; see its README |

When two layers disagree: the project's own decisions win, then the directing person's taste profile, then the house,
then the core. Within a project, the director's latest approved direction beats older records; history is context.

## Using it with an agent

The folder is itself an Agent Skill (`SKILL.md` at the root). Link it in once, wherever you cloned it. Mac or Linux:

    ln -s "$PWD" ~/.claude/skills/motion-playbook   # Claude Code
    ln -s "$PWD" ~/.codex/skills/motion-playbook    # Codex

Windows (PowerShell), with your clone's path:

    New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\motion-playbook" -Target "<your clone>"
    New-Item -ItemType Junction -Path "$env:USERPROFILE\.codex\skills\motion-playbook" -Target "<your clone>"

No project has to carry anything for the playbook to work.

## How rules are written

Each rule is a short card:

- **Rule**: what to do, in a line or two.
- **Why**: the reason it works.
- **Basis**: what it rests on. One of: *principle* (how motion and perception work), *measured* (we checked it on screen),
  *technical fact* (true of the medium or a tool, with the version), or *taste* (whose).
- **Scope**: where it applies (any, any camera-based scene, 2D, interactive...).
- Only when they add something: **Unless** (when it doesn't apply, or which rule wins), **Check** (how to verify it),
  **In tools** (where the tool-specific how-to lives).

When observations conflict, write the tradeoff (an Unless line) instead of letting the newest case overwrite the rule.

Every rule has an `id` so other files link to it instead of copying it. Examples in the universal folders stay generic;
real project cases live in the house layer and link to rule ids, never the other way round.

Tool notes use a different card, because a software quirk is searched by its symptom: **Symptom**, **Cause**, **Fix**,
**Seen** (tool version and date).

## Sending changes

Lessons and changes go through `inbox/`, one file each; [inbox/README.md](inbox/README.md) has the format. Pull requests
are welcome.

## Licence

The text is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0): see [LICENSE](LICENSE).
Attribute it as "the motion playbook, by Cyril", with a link to this repository.
