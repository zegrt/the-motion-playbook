# Motion and timing

How things move: phrasing, continuity, curves, contacts, groups, hand-offs, and effects that repeat. Tool-free. How to do
it in a given tool lives in `tools/`.

Principles behind this chapter: [3 Caused and continuous](../CORE.md), [2 Judge what the viewer sees](../CORE.md),
[5 A living frame](../CORE.md).

## Phrasing

### Phrase the action
`id: motion.phrase` · principle 3

- **Rule.** Build an action as a phrase: preparation, focal action, follow-through, recovery, then a readable hold. Shorten or
drop parts when the action calls for it; a micro-interaction doesn't need an obvious anticipation or overshoot.
- **Why.** The phrase is what makes an action read as intended rather than as a value changing. The main idea gets
priority over making every part move.
- **Basis.** principle (classic animation). **Scope.** any.

### Arrive, stay, depart
`id: motion.hold-phases` · principle 3

- **Rule.** Treat arriving at a pose, staying with it and leaving it as three phases, tuned separately. A hold can contain
small motion.
- **Why.** Tuned as one curve, a presented pose turns into one long return movement and never reads as held.
- **Basis.** principle. **Scope.** any.

### Overlap, don't take turns
`id: motion.overlap` · principle 3

- **Rule.** Parts that belong together share a phrase but start and finish at different moments. Never run action 1 to
completion, then action 2, then action 3. Many separate events pull the eye around; try making them one chain, where one
action passes through the scene and each element answers as it arrives.
- **Why.** Sequential motion reads as a checklist. Overlap reads as one cause moving through a system.
- **Basis.** principle; strongly confirmed by director notes. **Scope.** any.
- **Check.** Scrub for frames where only one thing moves, or where everything stops at once.

### No stop-start
`id: motion.no-stop-start` · principle 3

- **Rule.** Don't chain tight moves with stops between them. Overlap them into one move instead of returning to a pose and
pausing.
- **Why.** Each stop resets the eye; a string of them reads as jerky even when every move is smooth on its own.
- **Basis.** principle; measured. **Scope.** any.
- **Check.** Plot on-screen speed per frame. A dip to near zero between two moves that should feel like one is the fault.

### Nothing in lockstep
`id: motion.no-lockstep` · principle 3

- **Rule.** Vary speed, direction, amount and delay between pieces, even when one cause moves them all.
- **Why.** Two cards spinning the same way at the same time read as one block; uniform linear motion reads as machinery.
- **Basis.** principle; director notes. **Scope.** any group of moving things.

### Let something lead a big change
`id: motion.leader` · principle 3

- **Rule.** Give every big change a visible cause in the scene that moves first: lights sweep before the whiteout, a hand
moves before the card lifts.
- **Why.** A change with a leader feels caused; without one it feels like an edit.
- **Basis.** principle; one strong example. **Scope.** any.

### Already moving at the cut
`id: motion.already-moving` · principle 3

- **Rule.** At a cut, the shot is already in motion: camera, world and anything on a path have speed on frame one. Cut on
motion. When something dissipates, it keeps its momentum.
- **Why.** Motion that starts after the cut and ends before the next one is the classic beginner tell. A shot that starts
still reads as a slideshow.
- **Unless.** The shot specifically needs a still start, for a deliberate beat.
- **Basis.** principle; director notes, stated as a law. **Scope.** any cut sequence.
- **Check.** Compare the first two frames of each shot: something meaningful should differ.

### Arrive, don't appear
`id: motion.arrive` · principles 2, 3

- **Rule.** Things joining a moving system enter across a frame edge, already moving with it. Their start point comes from
what the camera sees at that depth.
- **Why.** Fading up in mid-air, far from the action, reads as "appearing from nowhere".
- **Basis.** principle; measured. **Scope.** any camera-based scene.
- **Check.** Count pieces first seen well inside the frame. Aim for zero.

### Show the stagger in arrivals
`id: motion.stagger-arrivals` · principle 3

- **Rule.** Stagger when things arrive, not only when they start.
- **Why.** Staggered starts on curves of different length can land together and undo the stagger.
- **Basis.** principle. **Scope.** any group.

## Speed and curves

### Fly in fast, arrive slow
`id: motion.fast-in-slow-arrive` · principles 2, 3

- **Rule.** Something flying in starts fast and slows all the way to its landing, on one tight curve.
- **Why.** A move that builds to a peak speed and then brakes feels wrong before anyone can name why.
- **Unless.** Contacts ([motion.contact](#contacts-speed-up-into-them)).
- **Basis.** principle; measured. **Scope.** any.
- **Check.** Track the object's speed on screen. On a 3D path most of the speed is depth, so measure in screen space, not
along the path.

### Contacts: speed up into them
`id: motion.contact` · principle 3

- **Rule.** A tap or press accelerates into the contact, holds it for 2 to 3 frames with a squash (the surface dips on the
same frame), then releases.
- **Why.** A hand that hovers and then whips away never reads as a press.
- **Basis.** principle; measured. **Scope.** any contact.

### Values make the shape, easing makes the travel
`id: motion.curve-shape` · principle 3

- **Rule.** Keyed values establish an overshoot; the easing only controls travel between them. Check arrival speed,
reversal and departure together. A hop is steady travel with the height on its own curve, not one curve on the whole
position.
- **Why.** Zero velocity at a peak doesn't by itself make the acceleration around it feel smooth.
- **Basis.** principle. **Scope.** any keyframed motion.
- **In tools.** Which key's handle shapes which segment differs by tool; see `tools/`.

### Name your curves
`id: motion.curve-tokens` · principle 6

- **Rule.** Keep a small set of named curves and reuse them, the way design systems name easing tokens. Choose by distance,
duration and intent, not habit.
- **Why.** Named curves keep a film's motion consistent and make notes like "tighter" mean something exact.
- **Basis.** principle (design-system practice). **Scope.** any.

Reference curves from past work (cubic bezier). They are starting points, not presets.

| Name | Curve | Used for |
|---|---|---|
| soft | (0.42, 0, 0.58, 1) | soft movement, recovery |
| accelerate | (0.55, 0, 0.85, 0.3) | building into an impact |
| fast release | (0.12, 0.8, 0.2, 1) | snapping out of a hold |
| eased arrival | (0.35, 0, 0.65, 1) | a deliberate settle |
| tight S | (0.78, 0, 0.12, 1) | a decisive move between poses |
| tight arrival | (0.35, 0, 0.1, 1) | settling off an overshoot |

The last two are a director's house taste for a premium, tight feel (see the house layer); the first four are general.

### Recheck tangents after editing time
`id: motion.tangents-after-edit` · principle 3

- **Rule.** After extending or shortening a hold, recheck the departure tangent. When cropping motion at a shot's start,
keep the evaluated pose and the rest of the curve at the crop point instead of clamping keys onto frame zero.
- **Why.** Continuous positions can still hide a velocity hitch.
- **Basis.** measured. **Scope.** any keyframed motion.

### Know your real duration
`id: motion.effective-duration` · principle 2

- **Rule.** Effective duration is frames ÷ fps ÷ playback speed. Note local frames and parent time separately when shots are
nested, retimed or slowed.
- **Why.** Speeds, holds and nested time change what is actually on screen.
- **Basis.** technical fact. **Scope.** any nested or retimed timeline.

## Groups and systems

### Space a group with one push
`id: motion.group-push` · principles 3, 6

- **Rule.** Move a group with one shared offset, the leading item fastest, so the group opens out as it travels. A gust
reaches the nearest pieces first, so push the farther ones more and the gaps only open. Each piece still gets its own
direction, amount and delay.
- **Why.** Nudging items one at a time away from a limit piles them up at its edge; fast starts on the near pieces make them
overtake and pass through the ones ahead.
- **Basis.** measured. **Scope.** any group or scatter.

### Connected parts share a phrase, independent parts don't
`id: motion.cycles` · principle 3

- **Rule.** Parts linked by cause (body, reaching arms, held prop, face, shadow) move in one coordinated phrase. Independent
cycles (blinks, ambient loops, continuous rotation) get their own periods, different enough that they don't keep landing
together.
- **Why.** Shared periods make unrelated things pulse in sync; deliberate sync is fine when the action wants it.
- **Basis.** principle. **Scope.** any character or system.

## Hand-offs and timing to sound

### Match what you hand off to
`id: motion.handoff` · principles 3, 6

- **Rule.** For a settled hand-off, match the incoming hold's values. Joining a moving loop, match velocity as well as
position. When you retime a gesture, retime what belongs to it: its shadow, glow, visibility swap and effect reset.
- **Why.** An attached shadow or glow that doesn't follow its owner's scale and visibility is left behind: a shadow stays on
the floor after its object shrinks away.
- **Basis.** principle; measured. **Scope.** any.

### Land on the word, not the time
`id: motion.word-sync` · principle 2

- **Rule.** To land an action on a spoken word, measure where the word starts in the actual audio. Don't trust a time
carried over from an earlier version.
- **Why.** An inherited key once put a title 10 frames after its word began, as the word was ending.
- **Basis.** measured. **Scope.** anything synced to voice or music.

## A living frame

### Everything visible has some life
`id: motion.living-frame` · principle 5

- **Rule.** Give each visible element something subtle from its first visible frame, separate from its main action: a
chart keeps ticking up after it rises, a far crowd sways. Plan secondary, ambient and effects with the shot, not after.
- **Why.** Anything left still for long reads as dead, even in the background.
- **Unless.** An information beat: keep ambient motion out of the way while the viewer reads.
- **Basis.** principle; director notes. **Scope.** any scene.
- **Check.** For each shot, list the main action, the secondary motion, the ambient motion and the effects. An empty
line is a decision, not an omission. Rough passes carry secondary detail too. After a redesign, restate the secondary
motion and effects for the new design; the old list may no longer fit.

### Ambient motion stays cheap
`id: motion.ambient-cheap` · principles 5, 7

- **Rule.** Keep ambient motion simple: a few cheap techniques (one noise layer, looping bands, offset copies of one
animation; for a piece in a 3D world, one bob or drift plus a slow turn) rather than many hand-keyed parts.
- **Why.** Ambient motion is felt, not studied; expensive ambient motion slows every iteration of the shot.
- **Basis.** practice (one director's notes); measured on render times. **Scope.** any.

### A quiet build-up, or a stacked transition
`id: motion.build-vs-stack` · principles 1, 3

- **Rule.** A quiet build-up starts with almost nothing, ties its first big event to a word, and lets each new thing be
caused by the one before, one main thing at a time, with the character's gaze leading the eye. A transition is different:
it can stack events (the dark lifting, a grin, the cards coming back) on top of each other.
- **Why.** Build-ups need a readable chain; transitions need momentum.
- **Basis.** taste (one director: the stacked transition is confirmed; the quiet build-up was judged at full speed in a
finished film, one case). **Scope.** any.

## Effects and loops

### Pop motifs: in, turn, out
`id: motion.pop-motif` · principles 3, 5

- **Rule.** For popping decorations: pop in, rotate while visible, then anticipate and shrink out. Stagger between groups and
within them. Make the rotation visible during entry and exit; reset position and rotation while hidden.
- **Why.** Spinning mostly at zero scale contributes nothing; resets done while visible pop.
- **Basis.** principle. **Scope.** any repeating decoration.
- **Check.** At the seam of a phase-shifted loop, density shouldn't collapse.

### Seamless travelling patterns
`id: motion.travel-loop` · principle 6

- **Rule.** For a pattern travelling under a mask, build it at least one repeat wider than the mask, match shape and tangent
across the boundary, and move it by exactly one period. Two linear keys are enough for constant travel. To keep paint
still while the shape moves, move the path inside a stationary painted or clipped structure.
- **Why.** Any mismatch at the period shows as a jump at the loop.
- **Basis.** technical fact. **Scope.** any looping pattern.

### Simple ballistic particles
`id: motion.ballistic` · principle 3

- **Rule.** For sparse particles, move X linearly and Y on a parabola. With flight progress u from 0 to 1:
`Y(u) = y0 + v·u + a·u²`, where `a = yEnd − y0 − v` (v is change over the whole flight, not pixels per second). Vary
launch time, travel, rotation and fade; fade before resetting.
- **Why.** It gives believable arcs with two keys per channel.
- **Basis.** technical fact. **Scope.** any 2D particles.
- **Check.** The variation is visible on screen, not just numerically different.
- **In tools.** Rive cubic value interpolator handles: see `tools/rive.md`.
