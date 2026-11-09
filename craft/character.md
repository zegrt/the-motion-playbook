# Character

How a character moves and acts: motion language, poses and holds, rigs and pivots, props and contact, feet, eyes, gaze,
expression and deformation, and a character placed in a scene. For any character: a mascot, a UI character, 2D or 3D.
Tool-free. How to do it in a given tool lives in `tools/`.

Principles behind this chapter: [1 Know what each moment is for](../CORE.md), [3 Caused and continuous](../CORE.md),
[6 One source of truth](../CORE.md). Phrasing, overlap, curves and hand-offs in general are in
[Motion and timing](motion-and-timing.md); this chapter links to them rather than repeating them.

## Before animating

### Develop the look before placing it
`id: character.look-dev-first` · principles 1, 6

- **Rule.** For a new character or hero prop, finish the story and plan first. Then develop its look on its own (views,
parts, states, material and light, one isolated motion test), and only then place it in scenes.
- **Why.** Designed inside scene stills, it becomes a new version in every scene; one concept's side view was simply
wrong, with no sheet to check against.
- **Basis.** taste (one director). **Scope.** any new character or hero prop.
- **Check.** Front, side and back views exist before any shot shows the character turn.

### Act to the beats
`id: character.act-to-beats` · principle 1

- **Rule.** Before building, write each shot's job and what the character does in it; neighbouring shots give it
different things to do. Key the face to those beats, never to leftover test keys. Start each shot from where the last
one really left the character: its exit, its facing, its way of moving (if it hopped out, it hops back in).
- **Why.** Three neighbouring mid shots "didn't do anything", and leftover rig-test keys made a curious character look
angry.
- **Basis.** practice (one director's notes). **Scope.** any character in a cut sequence.
- **Check.** One line per shot: what the character notices, feels or does. Two identical lines in a row is the fault.

### Build toward the destination
`id: character.authoring-order` · principles 6, 7

- **Rule.** Start from the current brief and artwork, including the expression, grip points and existing motion already
approved for this work. Then list everything that can move: body, limbs, face, props, accessories, feet, ground,
effects. For a new reusable pose, then set up controls, the hold and its recurring gesture, and build the entrance
toward that hold. Review broad motion first, then expression and secondary response, then small effects.
- **Why.** An entrance built toward a known hold hands off cleanly. A part found late (an eye squeeze, a cheek puff) gets
laid on top of finished motion instead of inside its phrase.
- **Unless.** A one-shot, or an edit to existing motion: use the order that best protects the approved behaviour.
- **Basis.** practice (one set of reusable poses). **Scope.** any character, most of all reusable poses.
- **Check.** The entrance ends on the hold's values, and every new property has a neutral value in each hold and reset.

## Motion language

### Pose and timing carry it
`id: character.pose-first` · principles 1, 5

- **Rule.** The character communicates through pose and timing first. Bursts, sparkles and glows come after, support the
same action and keep the face readable. They're optional: choose their density for the scene rather than copying a count
from another piece.
- **Why.** An effect can't rescue an unclear pose, and it competes with the face for the eye.
- **Basis.** principle. **Scope.** any.

### One peak, settling from the centre out
`id: character.one-peak` · principle 3

- **Rule.** Body, arms, held prop and the strongest expression peak on the same beat. Only follow-through comes later,
from the centre out: body, then held prop, then face and wrists, a few frames apart. Settle with corrections that
shrink, not a wobble on every move.
- **Why.** An expression peaking after the body reads as a second action. Settling from the centre out reads as weight
passing through; wobble everywhere reads as jelly.
- **Basis.** principle; repeated in approved work. **Scope.** any character action.

### The entrance is loud, the loop is quiet
`id: character.entrance-vs-loop` · principle 5

- **Rule.** An entrance can be bigger than anything that repeats, and starts from a believable rest (arms down by the
body, not already in the air) so its arc has travel. A recurring gesture is a quieter echo with holds between: a big arm
raise on entrance, a slight wave in the loop; cheeks puffing about 6% on entrance, under 2% in the loop.
- **Why.** A gesture that starts halfway has no energy to show. A big gesture on repeat tires the viewer and fights
whatever the character sits beside.
- **Basis.** taste (one director, approved across several poses). **Scope.** entrances and recurring or idle motion.
- **Check.** The hold-plus-gesture period differs from the blink's ([motion.cycles](motion-and-timing.md#connected-parts-share-a-phrase-independent-parts-dont)).

### Weight starts soft
`id: character.weight-onset` · principle 3

- **Rule.** A gentle or weighty move (a hug, a lean) leaves its anticipation on a curve that also starts at zero speed.
- **Why.** A fast-release curve out of a soft stop jumps from rest to full speed in one frame: a twitch, even over a small
distance.
- **Unless.** A snappy action can want that jump.
- **Basis.** measured. **Scope.** gentle or weighty gestures.
- **Check.** Plot speed per frame at each exit from an anticipation.

### Each character moves like what it is
`id: character.motion-language` · principle 1

- **Rule.** Give each character a motion language that fits its nature, and keep it: a soft mascot on overlapping curves,
a robot on robotic moves (single axes, hard stops, held poses). When two share a shot, the contrast tells them apart.
- **Why.** If both move the same way, the viewer loses who is who.
- **Unless.** [motion.no-stop-start](motion-and-timing.md#no-stop-start) still holds for the soft character; the robot's
stops are its language.
- **Basis.** taste (one director). **Scope.** more than one character.

### Decide how far limbs stretch
`id: character.stretch` · principles 1, 6

- **Rule.** Decide per character whether limbs stretch and by how much, and hold to it across the piece. Never stretch
to reach something by accident; move the body or the object.
- **Why.** In one design, arms twice their length lifting a trophy read as a celebratory reach; in another, a hand
stretched toward a card looked weird. The style already set decides.
- **Basis.** taste (one director, both cases). **Scope.** any character with limbs.

## Poses and holds

### Hold the presented pose
`id: character.presented-hold` · principle 3

- **Rule.** When a character presents something, hold the raised pose long enough to read, with small motion inside it (a
slight drift, gaze staying on the prop), then leave at a matched speed. See [motion.hold-phases](motion-and-timing.md#arrive-stay-depart).
- **Why.** Without a hold, lift and descent become one movement. About 0.3 s of drifting hold fixed a lift that
"returned too immediately".
- **Basis.** taste (one director's notes); measured. **Scope.** any presented pose.

### Confusion longer than the payoff
`id: character.realisation` · principles 1, 3

- **Rule.** In an overwhelmed-then-realisation beat, give the confusion more time than the payoff. One tuned example: eye
darts about 0.11 s apart on a curve between a snap and a soft ease, then about 0.4 s of hold with a small body perk.
- **Why.** Seven snaps read too fast, four soft moves too much, and a longer smile reads as "smiles and does nothing".
- **Basis.** taste (one director's notes, one film). **Scope.** any reaction beat.
- **Check.** Retiming the beat moves its spoken word too ([motion.word-sync](motion-and-timing.md#land-on-the-word-not-the-time)).

## Rig, controls and pivots

### Placement above performance
`id: character.rig-layers` · principle 6

- **Rule.** Keep placement and overall scale in a parent, the performance in controls beneath, named by what they move.
One feature's fill, outline, shine and clipping move together. Split a limb into broad and delayed controls (shoulder,
wrist) when it wants drag. Accessories hang under their owner; the ground shadow sits beside the body.
- **Why.** Scale set once in the parent keeps one size across poses and scenes. A feature split across controls tears
apart; a limb with no delayed part can't follow through.
- **Basis.** principle; director notes. An example structure, not a required rig. **Scope.** any rigged character.
- **In tools.** `tools/rive.md`, `tools/after-effects.md`.

### Pivots where the joint is
`id: character.pivots` · principles 3, 6

- **Rule.** Arms pivot at the shoulder, held props at the contact point, flexible accessories at their base. Moving a
pivot keeps the artwork where it was.
- **Why.** An arm pivoted at its hand swings the shoulder off the body. A correct end pose doesn't prove the sweep
between stays attached.
- **Basis.** principle; one real case. **Scope.** any rig.
- **Check.** Neutral, extreme and in-between poses, and the widest arc at full speed.

### Keep the stacking order believable
`id: character.layer-order` · principles 4, 6

- **Rule.** A gripping arm sits in front of the prop along its whole length, not only the hand, and no limb slides over
the face by accident. In 3D, keep the character's parts in one unit or on one plane so the renderer can't re-sort them.
- **Why.** Some renderers order flat layers by distance to each layer's centre, which once put an arm over a face.
- **Basis.** technical fact; director notes. **Scope.** layered characters, especially in 3D.
- **In tools.** `tools/after-effects.md` (Classic 3D sort order).

### Clipping comes in layers
`id: character.clipping` · principle 2

- **Rule.** Check the widest arm arc and prop travel against every boundary: the character's own component, a reveal mask,
the parent layout, the output frame. Don't shrink or slide a limb to fit; move the boundary.
- **Why.** Turning off one clip leaves the others. Arms shrunk to stay inside a box read wrong.
- **Basis.** technical fact; director notes. **Scope.** any character inside UI or a container.

## Props, contact and hands

### Two hands, one prop
`id: character.two-hand-grip` · principle 3

- **Rule.** Build a held prop and its grips as one assembly; each arm reaches its grip from its shoulder.
- **Why.** Reach and angle interpolated separately can detach a hand mid-move even when every key is right.
- **Basis.** measured. **Scope.** any prop held by two limbs.
- **Check.** Sample hand-to-grip distance at subframes through the move; add a correction key only where the error shows
(a fifth of a pixel at display size was fine).

### Stage the catch where it reads
`id: character.prop-staging` · principles 1, 2

- **Rule.** A character meets a prop in front of the body, around chest to face height, not on top of the head or down
by the feet. The prop may cross the face briefly in travel; the held pose shows the face.
- **Why.** A catch above or below reads as the prop landing on the character.
- **Basis.** taste (one director's notes). **Scope.** any prop interaction.

### A hand alone is still the character
`id: character.hands` · principles 1, 6

- **Rule.** A hand shown alone keeps the character's design and the same on-screen scale as in other shots. It enters
from the frame edge, makes its contact ([motion.contact](motion-and-timing.md#contacts-speed-up-into-them)) and moves
afterwards only with a reason. Two characters' hands get different colours.
- **Why.** A hand that changes size or wanders breaks the sense of one character behind it.
- **Basis.** taste (one director's notes). **Scope.** hand-only or partial-character shots.

## Feet, ground and shadow

### Planted feet, answering shadow
`id: character.feet` · principles 3, 6

- **Rule.** Planted feet counter the body's motion (position and rotation), or the rig pins them. The ground shadow
answers the body on the same phrase, changing size as it lifts. Don't scale locally to hide a contact error.
- **Why.** Sliding feet break weight at once; a shadow that ignores the lift makes the character float.
- **Basis.** principle; measured. **Scope.** any standing character.
- **Check.** A tracked foot point doesn't move on screen. The shadow follows its owner's scale and visibility
([motion.handoff](motion-and-timing.md#match-what-you-hand-off-to)).

## Eyes, blinks and gaze

### Blink on its own, by moving
`id: character.blink` · principles 4, 5

- **Rule.** Open eyes blink automatically, an open hold then a blink, on its own period, so it doesn't fall into step
with other loops by accident (a deliberate sync is fine when it supports the action); a manual trigger is optional, and
a deliberately closed-eye pose needs none. Default construction: move the whole open-eye assembly (white, pupil,
highlight, mask) down while a lower cover rises, swap to aligned closed drawings, reverse to reopen. Scale the eye only
by deliberate choice (a slight unsquash as eyes open on an entrance).
- **Why.** Unblinking open eyes read as dead. Scaling squashes pupil and highlight into a different eye.
- **Basis.** principle; director taste. **Scope.** drawn 2D eyes; another design may justify another construction.

### Fit the lids, hide the swap
`id: character.blink-swap` · principles 2, 4

- **Rule.** Fit each closed lid to its own eye's visible baseline, keeping purposeful left/right differences. At the
swap, the first visible frame shows a narrow opening; reopening travel starts when the open drawing appears, not before.
Swap on one frame rather than crossfading.
- **Why.** Rotation baked into a path differs from the transform's, so a lid copied across once sat 25° off. Travel hidden
behind the closed drawing makes the eye pop open (once, 80% of it was hidden). A crossfade shows doubled lids.
- **Basis.** measured. **Scope.** any drawing-swap blink or expression change.
- **Check.** The swap at full speed, final display size and subframes.

### Look at what it acts on
`id: character.gaze` · principles 1, 3

- **Rule.** The character looks at what it acts on: the card it reads, the opponent, the trophy it lifts (eyes follow it
up and stay). Both eyes move together. A flat character can face the camera and address its side with the eyes alone.
In a quiet build-up, gaze leads the viewer to the next event ([motion.build-vs-stack](motion-and-timing.md#a-quiet-build-up-or-a-stacked-transition)).
- **Why.** Gaze is the strongest pointer on screen; a character looking the wrong way reads as not involved.
- **Basis.** principle; director notes, several times. **Scope.** any.
- **Check.** In every shot, from the camera: which way does the body face, and where do the pupils point?

## Expression and deformation

### Expressions from the beat, read at size
`id: character.expression-read` · principles 1, 2

- **Rule.** Choose each expression for its beat and check it at final display size. Use distinct drawings for distinct
states (smile, "oh", gasp, grin) rather than pushing one mouth through all of them. Know what each rig value does before
keying it.
- **Why.** Small faces read differently from the rig preview: default brow values read as angry, a guessed mouth value
came out as a gasp.
- **Basis.** practice (one director's notes). **Scope.** any face.

### Deform only the feature
`id: character.deformation` · principles 4, 7

- **Rule.** Deformation is a choice, not a requirement. When used, isolate it: squeeze a closed lid's own shape while
keeping brow and stroke thickness, curve continuity and stroke caps (move vertex handles as well as positions); puff a
cheek from its own centre without moving the mouth. Release without a big reverse squash.
- **Why.** Squashing the whole eye-and-brow group reads as another expression; a big release reads as deflation.
- **Basis.** principle; director notes. **Scope.** any character deformation.
- **Check.** At display size the squeeze reads as tighter, not as an eye opening or a stroke thinning out.

## A character in a scene

### Judge it inside its container
`id: character.in-container` · principle 2

- **Rule.** Inside a moving parent (a reveal, a camera move, a card), judge the character's timing in screen space. A
local peak is not the visual peak while the parent still moves. An accessory's hop takes off with the main lift, stays
up briefly and lands once.
- **Why.** A hat kept rising on screen while its own hop descended, because the parent was still lifting.
- **Basis.** measured. **Scope.** any nested character.
- **Check.** Review alone and in the parent, at display size and speed, from preparation through recovery.

### Keep the character's rendering
`id: character.keep-rendering` · principles 6, 7

- **Rule.** In new staging, keep the character's approved shape, shading and edges. Turn the whole character rather than
skewing it. Don't push its face through a proxy plane; use rear artwork for a back view, with no eyes on the back. A
flat character can stay flat beside 3D objects.
- **Why.** Following composition geometry too literally flattened a shaded character and skewed it; its source
rendering fixed both.
- **Basis.** taste (one director's notes, several rounds). **Scope.** any existing character in new staging.
