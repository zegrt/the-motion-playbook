# Production book

How one production keeps one record of where it stands: every unit, what the director approved and in what words,
what's open, the cut and what was delivered. The tool that runs it is the [production book
kit](../kit/production-book/README.md); a book lives in its own project, never in the playbook.

Principles behind this file: [2 Judge what the viewer sees](../CORE.md), [6 One source of truth](../CORE.md),
[7 Change the least that fixes it](../CORE.md).

### One book, its current state on top
`id: book.one-book` · principle 6

- **Rule.** A production keeps one book in its own folder: a front page whose "Now" is overwritten, never appended; one
page per unit, its "Now" 15 lines or fewer; the shared look; the one open list; the director's decisions. History goes
in the records, not on the pages. A single piece needs only the front page.
- **Why.** Pages that only grow stop being read: on one production they grew to hundreds of lines, fell behind the work,
and the team's handoff had to say the book was out of date.
- **Basis.** measured (one production's book, ten days). **Scope.** any production with more than one unit.

### One fact in one place
`id: book.one-fact` · principle 6

- **Rule.** Write each fact once, as a small record (a version, an approval, a note, a decision), and generate every
table that shows it. Never retype a status onto a second page.
- **Why.** Status kept in three places (a page header, a data file, an index row) drifted in all three, while the
book's checks still passed.
- **Basis.** measured (one case). **Scope.** any book.

### Versions are named once; the latest is worked out
`id: book.versions` · principles 6, 7

- **Rule.** Name every published output by unit, step and a three-digit number (`s05_anim_v003`), never reuse a number,
and let "current" and "last approved" be computed from the records, not typed. A delivery has its own ladder (v1, v1.1)
and lists the versions it contains. The kit numbers a delivery like any other version (`d1_deliver_v001`): write its
ladder and its contents by hand, in that version's summary.
- **Why.** Four naming schemes on one production meant nobody could say which file was the latest, or which version a
note or an approval was about.
- **Basis.** measured (one case); the same convention as production trackers. **Scope.** any book. Keeping earlier
versions reachable is `story.keep-versions`; building on the right one is `verify.right-version`.

### An approval names its version and quotes the director
`id: book.approval` · principle 2

- **Rule.** An approval says which version, which step and which pass (rough or final) it covers, and quotes the
director's words, with the date and how they were given. An agent records an approval; only the director gives one. A
recommendation is a note, not a decision.
- **Why.** Approvals pointing at a still or a plan couldn't answer "which version was approved, and for what?", and the
render that went out wasn't always the one approved.
- **Basis.** measured (one case). **Scope.** any book. How far a claim is proven is `verify.evidence-levels`.

### A note names a version, and closes with a later one
`id: book.notes` · principles 2, 7

- **Rule.** A note names the version and the frames it's about, and closes when a later version is checked against it.
Keep one open list, by unit (must, should, parked); announcements aren't notes.
- **Why.** A queue where nothing closes stops being read: most of one production's notes were still open after
delivery, and a separate parked list grew up beside it.
- **Basis.** measured (one case). **Scope.** any book.

### The cut is one record
`id: book.cut` · principle 6

- **Rule.** One cut list says which version of each unit plays where, in frames, and how each unit joins the next.
Lengths, contractor packages and the list of what each delivery contains are read from it, by hand: the kit keeps the
cut (`CUT.tsv`) as a file you write, and doesn't read it. A delivery says, in its summary, whether the timing changed
since the one before, because a timing change makes every contractor's package out of date.
- **Why.** A cut written in six places disagreed with itself, and trimming one shot silently broke the join into the
next.
- **Basis.** measured (one case). **Scope.** any linear piece. Versions with clean edit points are `story.edit-points`;
picture a contractor can work against is `sound.handoff-picture`; what to ask back is `sound.deliverables`; one master
is `finish.master`.

### A checkpoint records what the next person needs
`id: book.checkpoint` · principle 6

- **Rule.** Each new version records what changed and why (selected, proposed, still open); its exact paths (source,
versioned project, preview); how it's built (construction, camera, shared assets used); what was checked, and at which
level; its limits; and the units it affects. Work interrupted before a version leaves a handoff note.
- **Why.** The next person is a colleague, an agent after its context is lost, or you tomorrow; a checkpoint that says
only "done" sends them back to the files to rebuild what you knew.
- **Basis.** measured (one case). **Scope.** any book. Look at it before recording it (`verify.own-output`), and say
how far each check is proven (`verify.evidence-levels`).

## Team mode: two or more writers

A book is solo until a second person or agent writes to it. The idea under both cards: each piece of work has one
writer at a time, and anything outside your own scope changes only by proposal. The kit doesn't run team mode: keep
these rules by hand (a claim can be a line in a shared file, or a message to the others).

### One writer per scope
`id: book.one-writer` · principle 6

- **Rule.** Claim before you write: name the unit or task and the exact files, layers, frames or areas it covers. A
unit can have several writers at once on disjoint scopes, and a different claim name doesn't make overlapping edits
safe. One open project in one app has one writer: claim the app before driving it. Claim the shared look page while
editing it, and release it right after. A claim nobody has refreshed in hours is stale, but nothing takes it over: read
its last checkpoint, and ask its holder or the director first.
- **Why.** Several writers worked one production in parallel without overwriting each other's files; the one collision
on record came from a shared area nobody had claimed.
- **Basis.** measured (one case). **Scope.** team mode. Protecting unsaved work before taking a tool is `work.protect`.

### Outside your scope, propose
`id: book.propose` · principles 6, 7

- **Rule.** Anything that isn't yours changes only by proposal, never in place. To try something on claimed or shared
work, make an isolated, labelled variant (its own versioned file and area) and raise a note; it stays a labelled
alternative until the director picks it. Never overwrite a shared source asset, rename linked media or move someone
else's files to tidy your own area: version the shared thing, and say so in a record. A mismatch with another unit (a
join, a shared look value, a scale) becomes a cross-unit note to its owner; keep to the existing decision until the
owner answers, or the director, for a shared creative choice.
- **Why.** An edit in someone else's scope is invisible to them until it breaks their work; a proposal reaches the
person who can judge it.
- **Basis.** principle; measured (one case). **Scope.** team mode. A recommendation isn't an approval
(`work.yes-scope`).

## The book and the playbook

### The book stays in the project, and feeds the wrap
`id: book.stays` · principle 6

- **Rule.** A book is project data: the client's names, prices and links stay in it, in the project. A house's facts (a
character's rules, a palette, brand sources) live in the house layer, and the book links them. At the close, the book's
lessons go to the playbook's inbox as one proposal: that's the [wrap](wrap.md)'s step 2 for the project, and closing the
record is its step 9. The director's decisions stay in the book, since they hold the client's words; a decision that
teaches craft goes in as a lesson, in your own words.
- **Why.** Dependencies point one way: a project may depend on the playbook, never the reverse. Project facts mixed
into shared rules is the drift the playbook exists to stop.
- **Basis.** principle. **Scope.** any book.
