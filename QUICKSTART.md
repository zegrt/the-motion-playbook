# Quick start

For a motion designer new to the playbook, working on ads, film or product motion. Ten minutes to install, twenty to
write your profile.

## 1. Install it

Get access from the maintainer and clone the repo. Commit as yourself: check `git config user.name` and
`git config user.email` in your clone. The folder is itself an agent skill: link it once into each agent's skills
folder.

Mac or Linux, from inside your clone:

    mkdir -p ~/.claude/skills ~/.codex/skills
    ln -s "$PWD" ~/.claude/skills/motion-playbook   # Claude Code
    ln -s "$PWD" ~/.codex/skills/motion-playbook    # Codex

Windows (PowerShell), with your clone's path:

    $clone = "<your clone's path>"
    foreach ($d in "$env:USERPROFILE\.claude\skills", "$env:USERPROFILE\.codex\skills") {
      New-Item -ItemType Directory -Force $d | Out-Null
      New-Item -ItemType Junction -Path "$d\motion-playbook" -Target $clone
    }

Check it: `~/.claude/skills/motion-playbook/SKILL.md` should open through the link. A new agent session then loads
the playbook by itself when the work is motion; no project needs to mention it. `git pull` now and then to get what
others have added.

## 2. Write your profile

Copy [profiles/_template.md](profiles/_template.md) to `profiles/<your-name>.md` (your full name, hyphenated) and
start small: a few lines you're sure of. It has two halves: **taste**, used when you direct, and **working style**,
used when you run the session (how much the agent does on its own, when to show you work, your shorthand). It grows
from the corrections you repeat: the agent proposes a line, and you approve it. Until it's in, agents use the house
layer and the core. Send it the way you send a lesson (step 5): your profile is yours to approve.

## 3. Read these first

1. [CORE.md](CORE.md): seven principles, one page.
2. [README.md](README.md): the layers, which one wins when they disagree, and how a rule is written.
3. [SKILL.md](SKILL.md): which chapters go with which stage (plan, build, review, finish, deliver).

Then read by stage, as the work needs it, not all at once. If you work for a company with a folder in `houses/`, read
its README too; a house applies only when the brief says so.

## 4. Working with it

The agent reads the chapters for the stage and cites a rule's id (`motion.overlap`) when it drives a choice, so you can
check it. You direct and approve. Where the playbook has no rule (the README's Coverage section lists the known gaps),
the agent should say so rather than pass general knowledge off as the playbook.

## 5. Send what you learn

Never edit the playbook's own files from project work. When something is learned (a correction you had to repeat, a
tool quirk, a rule that misfired or was missing), the agent writes it as one file in `inbox/`. At the end of a project,
send your inbox files as a pull request on a branch named `inbox/<your-name>-<date>`, or send the files to the
maintainer. [inbox/README.md](inbox/README.md) has the format (it starts with who it's from) and who approves what.
Quote the words you rely on: your session logs stay yours, so the quotes in your proposals are the only record the
playbook keeps. Nothing reaches the playbook until it's approved.
