# Wrap

How lessons from a production reach the playbook. The maintainer runs it at the end of every production. At a break in
a long one, run steps 1 to 6 only: lessons, with the project's own record left alone. Someone who isn't the maintainer
runs steps 2 and 3 only, from their own notes and session history, and sends their proposals as
[inbox/README.md](../inbox/README.md) says: the harvest and the archive are the maintainer's.

Principles behind this file: [6 One source of truth](../CORE.md), [7 Change the least that fixes it](../CORE.md).

## The sequence

1. **Harvest** (the maintainer's tool). On each of the maintainer's machines the work ran on, the maintainer harvests
   the director's own messages from the AI session logs, reading only the folders registered for it: list each
   production's folders when it starts or at its wrap, and add anything else only deliberately (the playbook's own
   sessions, for one: they also hold agents' reports relayed between sessions, stored exactly like the director's
   messages, so remove those by hand before committing the harvest). Only the maintainer's own messages are harvested:
   other people's never go into the archive, and their evidence is the quotes in their proposals. Session logs live per
   machine and expire, so what isn't harvested at the wrap is lost. In the maintainer's copy the tool is
   `scripts/harvest_messages.py`, its folder list `archive/harvest-sources.txt`, and `--source` a deliberate addition;
   a shared or public copy doesn't ship them.
2. **Collect.** The project's proposals in `inbox/`, the corrections the director had to repeat (search the harvest),
   tool quirks hit, and rules that misfired. Check each against the playbook first: a lesson it already carries is
   dropped, and one that sharpens a rule is an edit to that rule, not a new one.
3. **Write proposals.** One file each, in the inbox format, written from the full source, not from a summary of it.
   Keep the source's conditions ("when", "may", "only if"): sharpen the wording, but don't harden an option into a
   requirement.
4. **Check each proposal,** as its writer: step 1 of
   [how a proposal becomes part of the playbook](../inbox/README.md#how-a-proposal-becomes-part-of-the-playbook).
5. **Review and approve:** steps 2 and 3 there. Nothing merges without the approval.
6. **Merge:** step 4 there. Then check that the stage routing in `SKILL.md` reaches each new rule at the stage it
   acts on: a rule that settles something before building is routed at Plan, whatever chapter holds it.
7. **Retire old copies** that the playbook now carries (notes files, agent memory): move them to `archive/` and leave a
   pointer where they were, rather than deleting them.
8. **Review the merge:** the independent review of step 2 there, on what was merged.
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
