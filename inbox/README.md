# Inbox

How anyone who uses the playbook proposes a change, an addition or a lesson. Nothing here is part of the playbook yet:
the skill doesn't route agents here for reading and lint doesn't check it.

## Writing a proposal

One file per proposal, so parallel agents never write to the same file: `YYYY-MM-DD-<project>-<short-slug>.md`. Inside:

- what it changes: a new rule, an edit to an existing one (give its id), a tool note, or a rule that misfired;
- the rule card or tool note in the [README](../README.md#how-rules-are-written) format;
- **Evidence:** the date, the project, the director's own words, and the file or render it came from.

## Sending it

If you're the maintainer, it's already where it needs to be. Anyone else sends their proposals at the end of a project:
a pull request that adds their inbox files (branch `inbox/<your-name>-<date>`), or the files themselves if you don't have
access to the repo.

## Who approves what

| Proposal touches | Approved by |
|---|---|
| `CORE.md`, `craft/`, `tools/` | the maintainer |
| `houses/<company>/` | that house's owner |
| `profiles/<name>.md` | that person |

At a wrap, each proposal is approved (merged where it belongs), changed, or dropped, and then deleted from here.
