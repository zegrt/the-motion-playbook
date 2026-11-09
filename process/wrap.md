# Wrap

How lessons from a production reach the playbook. The maintainer runs it at the end of every production. At a break in
a long one, run steps 1 to 6 only: lessons, with the project's own record left alone. Someone who isn't the maintainer
runs steps 2 and 3 only, from their own notes and session history, and sends their proposals as
[inbox/README.md](../inbox/README.md) says: the harvest and the archive are the maintainer's.

Principles behind this file: [6 One source of truth](../CORE.md), [7 Change the least that fixes it](../CORE.md).

## The sequence

1. **Harvest.** Run `python3 scripts/harvest_messages.py` on each of the maintainer's machines the work ran on. It
   reads only the folders listed in `archive/harvest-sources.txt`, so list each production's folders there when it
   starts or at its wrap; anything else only deliberately, with `--source` (the playbook's own sessions, for one: they
   also hold agents' reports relayed between sessions, stored exactly like the director's messages, so remove those by
   hand before committing the harvest). Only the maintainer's own messages are harvested: other people's never go into
   the archive, and their evidence is the quotes in their proposals. Session logs live per machine and expire, so what
   isn't harvested at the wrap is lost.
2. **Collect.** The project's proposals in `inbox/`, the corrections the director had to repeat (search the harvest),
   tool quirks hit, and rules that misfired. Check each against the playbook first: a lesson it already carries is
   dropped, and one that sharpens a rule is an edit to that rule, not a new one.
3. **Write proposals.** One file each, in the inbox format, written from the full source, not from a summary of it.
   Keep the source's conditions ("when", "may", "only if"): sharpen the wording, but don't harden an option into a
   requirement.
4. **Check each proposal** ([verification](verification.md)): against its source; against the playbook's own contract
   (lint, the right layer, the card fields, routing); then step back, and ask whether it makes the playbook sharper or
   only longer.
5. **Approve.** The owner of each layer approves, changes or drops each proposal ([who approves
   what](../inbox/README.md)). Nothing merges without it.
6. **Merge.** Merge each approved proposal where it belongs, run `python3 scripts/lint.py`, and delete the proposal.
   Check that the stage routing in `SKILL.md` reaches each new rule at the stage it acts on: a rule that settles
   something before building is routed at Plan, whatever chapter holds it.
7. **Retire old copies** that the playbook now carries (notes files, agent memory): move them to `archive/` and leave a
   pointer where they were, rather than deleting them.
8. **Review.** An independent reviewer, another agent or a person, checks the merge in the same three passes. Verify
   each finding before acting on it, then fix it and name the commit, or answer it with evidence.
9. **Close the project's record.** For each parked item and open note, propose done, next version or drop, with a
   one-line reason. The director decides; an agent closes nothing.

## Where a wrap goes wrong

### Retire a copy only when all of it is carried
`id: wrap.carried-before-retired` · principle 6

- **Rule.** Before archiving an old copy, check every instruction in it against the rule meant to carry it, not just
the topic. Quote the line that carries each one.
- **Why.** An archived note's main instruction (what a shot's secondary elements must come from) had no home: the rule
on the same topic carried a different instruction.
- **Basis.** measured (one case). **Scope.** any retirement.

### Recheck citations after moving cited text
`id: wrap.citations-move` · principle 6

- **Rule.** After trimming, moving or prepending to a file that others cite by line, check every citation into it,
or point the citations at an unchanged copy.
- **Why.** A block added at the top of a cited file, then a trim, moved the lines under eight line-number citations,
which then pointed at the wrong text.
- **Basis.** measured (one case). **Scope.** any wrap that edits a cited file.
