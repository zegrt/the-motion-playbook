# Verification

How to know something is true before saying it: in a review, before showing work, before a delivery note. Domain checks
live in each rule's Check line; this file is about checking itself.

Principles behind this file: [2 Judge what the viewer sees](../CORE.md), [6 One source of truth](../CORE.md),
[7 Change the least that fixes it](../CORE.md).

### A review reports real, proven faults
`id: verify.review` · principle 2

- **Rule.** List only genuine faults: render artifacts, broken continuity, wrong meaning, timing bugs, things that
contradict the plan. Check each item against the director's notes for that shot first, and never flag what they asked for.
Prove a fault before reporting it: measure sizes and timings from the frames, not from a small contact sheet, and confirm
an intersection from the 3D positions or across frames, because overlap in a 2D frame isn't proof. If unsure, leave it
out. If nothing is wrong, say it passes. Optional ideas get one line at most, outside the list.
- **Why.** Nitpicks hide the real faults and cost the director's time; unproven faults cost more.
- **Basis.** practice (one director's notes, repeated); measured (false collision reports from flat frames; a size
guessed at 1.9× that measured 1.27×). **Scope.** any review.

### Look at it before showing it
`id: verify.own-output` · principle 2

- **Rule.** Before showing anything, look at it: every motion sheet, and the key frames at full size, against the brief and
the source. A clean decode or passing expression checks is not a review. Report what was checked as facts (numbers, the
frames looked at), and claim nothing that wasn't checked. A claim that something is absent ("not covered", "not
found", "no rule says", "nothing was lost") shows the search behind it: the terms, where they were searched, and what
came back, hits included, so the reader can rerun it.
- **Why.** Technical checks pass on work that is visibly wrong: an unopened sheet once hid an illegible title, misplaced
elements and a false alignment claim. Absence claims are cheap to write and costly to check, and three were wrong in one
week. One showed its search but reported no hits for terms that did match, so the hits have to be shown, not only the
terms. Two showed no search at all: a retired note whose main instruction no rule carried, and a list of what was left
that was four too long.
- **Basis.** measured (one case; three absence claims in one week); director notes, repeated. **Scope.** any.

### Check the saved result, not the operation
`id: verify.readback` · principle 2

- **Rule.** After a meaningful edit, verify what was actually saved and rendered. A tool reporting success doesn't prove the
result survived.
- **Why.** A save once kept the timeline names and durations but lost the keyed tracks (see
[tools/rive.md](../tools/rive.md), Saving and verification). Nothing about that failure is specific to one tool.
- **Basis.** measured (one case). **Scope.** any tool.

### Say how far a claim is proven
`id: verify.evidence-levels` · principle 2

- **Rule.** Name the level a claim rests on: inspected (read the source), built cleanly, watched playing, read back from
the saved file, or checked on the target device. A delivery note marks each item as inspected, verified in the runtime it
ran in, or unverified, and says whether the whole was watched at speed (`story.whole-at-speed`). It also lists each
requirement in the brief as met, waived by the director (and when), or still open. A desktop benchmark doesn't establish
performance on a phone.
- **Why.** Each level proves something different (a clean build doesn't establish correct behaviour), and "it works" hides
which one was reached.
- **Basis.** principle; measured (one production reached delivery with two brief requirements unmet, one deferred and one
not yet final, recorded only in a parked list until the director decided them at the wrap). **Scope.** any; essential
for interactive pieces.

### Test the riskiest part small, first
`id: verify.test-small` · principle 2

- **Rule.** Before the full build, run a quick pass through the riskiest parts of the plan, and say what that pass can't
tell you (`story.whole-at-speed`: frame checks find errors, not feel).
- **Why.** A quick pass finds problems while the plan still looks good on paper: things that vanish, effects nobody can
see, symbols that change identity mid-motion.
- **Basis.** measured (one case). **Scope.** any. `character.look-dev-first` is the character case.
- **Check.** Before a full-length render, look at the keys, the expressions and a few stills, so a mistake doesn't
cost a whole render.

### Find the version that holds the work
`id: verify.right-version` · principles 6, 7

- **Rule.** Before revising a shot, confirm which shot the note is about, then find the version that actually holds its
latest approved work. An accepted blocking version may not hold the later animation. List what exists and say what a test
keeps.
- **Why.** Building on the accepted version instead of the one holding the latest animation silently throws work away.
This is how CORE 7's "latest approved version" is applied, not an exception to it.
- **Basis.** measured (one case). **Scope.** any revision.
