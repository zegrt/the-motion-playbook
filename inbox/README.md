# Inbox

How anyone who uses the playbook proposes a change, an addition or a lesson, and how a proposal becomes part of the
playbook. This is the one description of that flow: the skill, the wrap, the quick start and the reviewer's brief
point here. Nothing in this folder is part of the playbook yet: the skill doesn't route agents here for reading, and
lint doesn't check it.

## Writing a proposal

One file per proposal, so parallel agents never write to the same file: `YYYY-MM-DD-<project>-<short-slug>.md`. Inside:

- **From:** who sent it (your name, as your profile's file name has it if you have one) and the date;
- what it changes: a new rule, an edit to an existing one (give its id), a tool note, or a rule that misfired;
- the rule card or tool note in the [README](../README.md#how-rules-are-written) format;
- **Evidence:** the date, the project, the director's own words, and the file or render it came from. Quote the words
  you rely on in full: unless you're the maintainer, the quotes in your proposals are the only record of your messages
  the playbook keeps, because nobody else's session logs are harvested.

## Sending it

If you're the maintainer, it's already where it needs to be. Anyone else sends their proposals at the end of a project:
a pull request that adds their inbox files (branch `inbox/<your-name>-<date>`), or the files themselves if you don't have
access to the repo.

## How a proposal becomes part of the playbook

1. **Checked by whoever wrote it:** against its sources; against the playbook's own rules (the right layer, the card
   fields, the routing, lint); then stepped back, asking whether it makes the playbook sharper or only longer
   ([verification](../process/verification.md)).
2. **Reviewed,** where there's an independent reviewer (another agent or a person): before approval, in the same
   three passes. The writer answers each finding where it was raised: fixed, naming the commit, or not, with
   evidence. The same reviewer can check the merge afterwards.
3. **Approved** by the owner of the layer it touches (below), who approves, changes or drops it. Nothing merges
   without that approval.
4. **Merged** by the maintainer where it belongs, with lint run, and the proposal deleted from here.

At the end of a production, a project's proposals go through these steps together, as the [wrap](../process/wrap.md).

### Who approves what

| Proposal touches | Approved by |
|---|---|
| `CORE.md`, `craft/`, `tools/`, `process/`, `kit/`, `SKILL.md`, `README.md`, `QUICKSTART.md`, `scripts/` | the maintainer |
| `houses/<company>/` | that house's owner |
| `profiles/<name>.md` | that person |
