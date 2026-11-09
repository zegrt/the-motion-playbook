# Scenes and camera

Building a world the camera can believe: depth, space, the ground, the lens, camera moves, continuity between shots, and
what fills the frame. Tool-free. How to do it in a given tool lives in `tools/`.

Principles behind this chapter: [2 Judge what the viewer sees](../CORE.md), [6 One source of truth](../CORE.md),
[1 Know what each moment is for](../CORE.md), [5 A living frame](../CORE.md).

## Depth and space

### Real distance, true size
`id: scene.true-size` · principles 2, 6

- **Rule.** Place things at their real distance and give each kind of object one true size, so only distance changes how
big it looks.
- **Why.** Sizing far things by eye fights the camera, and it's easy to miss: the scene looks fine until an audit finds the
far pieces are just scaled down near the lens.
- **Basis.** principle; measured. **Scope.** any camera-based scene.
- **Check.** List each family's true size and every piece's distance. Nothing should be scaled to fake depth.

### Repeat things at several depths
`id: scene.repeat-depths` · principle 2

- **Rule.** Show the same kind of object at several distances.
- **Why.** The eye reads depth by comparing sizes of things it knows are the same.
- **Basis.** principle. **Scope.** any camera-based scene.

### One depth rule
`id: scene.depth-rule` · principle 6

- **Rule.** Tie blur, fade and colour to distance with one rule for the whole scene, not piece by piece. For example: no
blur up to a near distance, then blur growing with distance on a gentle power curve, capped at a share of the piece's
on-screen width; opacity falling by up to half with distance.
- **Why.** Per-piece settings drift and contradict each other as the camera moves.
- **Basis.** measured. **Scope.** any camera-based scene.

### Blur and fade must reach the screen
`id: scene.blur-on-screen` · principle 2

- **Rule.** Check depth blur and fade in pixels on the final frame.
- **Why.** A blur that looks right in settings can land at under a pixel, especially on precomposed or scaled layers.
- **Basis.** measured. **Scope.** any depth effect.

### Silhouettes for a horizon, faces for a swarm
`id: scene.far-silhouettes` · principles 2, 4

- **Rule.** Far objects can flatten to silhouettes against a bright horizon. Things that must be recognised, like a swarm
of cards, keep their faces at any distance; let size and blur carry the depth.
- **Why.** Silhouettes read better than fading away on a horizon. In a tall swarm most pieces are far, so tinting them
turns most of the swarm into plain blocks.
- **Basis.** measured. **Scope.** any deep scene.

### Ground things
`id: scene.ground-it` · principle 2

- **Rule.** Where you can, put things on the ground: bars rising from the floor, markers laid along it. A piece lying on a
floor needs a tight contact shadow to sit down; a lifted piece's shadow grows wider and softer as it rises.
- **Why.** Grounded things give more depth than the same things floating. A bright side edge alone reads as raised.
- **Basis.** principle; director notes. **Scope.** any scene with a floor.

### Solid things stay solid
`id: scene.solid` · principle 2

- **Rule.** Nothing passes through anything by accident: moving paths stay clear of other objects, growing things don't
visibly break through the floor or sit below it, and nested art doesn't double up (a card inside a card).
- **Why.** A piece passing through another breaks the world at once. It's cheap to check by numbers and expensive to find
in a render.
- **Unless.** A deliberate reveal, such as a shape sliding up through the floor (`scene.meaning-checks`); its hidden
part is not a fault.
- **Basis.** principle; director notes, repeated. **Scope.** any camera-based scene.
- **Check.** Check numerically in 3D across every frame: path clearances, and the lowest point of each piece against the
floor. Not from a 2D frame (`verify.review`). Facing, edges and camera smoothness are checked by `scene.face-the-lens`,
`scene.reaudit-angles` and `scene.one-move`.

### The ground reaches the camera
`id: scene.ground-edge` · principles 2, 6

- **Rule.** Run the floor under and past the lens; let only its far end dissolve, by opacity, not by fading to a colour.
Any world edge should dissolve rather than show.
- **Why.** A floor that stops in front of the character shows its edge, and a floor that fades to black shows its edge
against any sky that isn't black. Fading opacity lets the sky through and survives a change of sky.
- **Basis.** measured. **Scope.** any scene with a floor.

### Flat layers don't belong to a 3D world
`id: scene.no-flat-in-3d` · principle 6

- **Rule.** If something should stay in the space (a spotlight, a beam, a sign), build it in the space.
- **Why.** Flat screen-space layers drift across the frame when the camera moves.
- **Basis.** measured. **Scope.** any moving camera.

### Flat things face the lens
`id: scene.face-the-lens` · principles 2, 4

- **Rule.** Flat pieces in 3D (cards, tiles, screens) turn toward the camera within a limited tumble, so they never show an
edge-on sliver or a mirrored back. When a flat piece lifts or tilts near a low camera, tilt its far edge up so the face
turns toward the lens.
- **Why.** Edge-on, a card built from stacked layers shows through; a mirrored back breaks the read. Backs that never
show never need building (one scene dropped 55 layers).
- **Basis.** measured. **Scope.** any 3D scene with flat pieces.
- **Check.** Measure the worst angle any piece reaches against the camera across the shot.

### Fake 3D through one camera
`id: scene.one-projection` · principle 6

- **Rule.** When building perspective by hand (vector or 2D), project every point through one calculated camera: screen
corners, thickness, floor footprints, shadows, the character's plane. Map flat UI onto a face with one projective
transform, not by dragging corners.
- **Why.** Parts adjusted separately each look plausible alone, but together they describe no single space.
- **Basis.** measured. **Scope.** any hand-built perspective.

## The lens and the camera

### Let the camera decide direction
`id: scene.camera-direction` · principle 2

- **Rule.** Work out direction from the camera. With a camera tilted up, the horizon sits low, so going away goes down in
frame, not up.
- **Why.** Directions chosen by habit fight the perspective the camera actually has.
- **Basis.** principle. **Scope.** any camera-based scene.

### Lens length changes what reads as height
`id: scene.lens` · principle 2

- **Rule.** A wide lens shows the sides of pieces at the frame edges, so lying pieces look stood up. A longer lens flattens
them; shadows then carry the height of anything that lifts.
- **Why.** The same layout reads differently through different lenses.
- **Basis.** principle; measured. **Scope.** any camera-based scene.

### Check what the camera really sees
`id: scene.camera-sees` · principles 1, 2

- **Rule.** Before designing a surface, measure what fills the frame. Compare the same object's on-screen scale across
neighbouring shots, and draw a quick top-down map when geography is in doubt.
- **Why.** A slab filling the frame turned out to be an object's side, seen about four times closer than in the shots
around it; no surface detail could make it read. Moving the camera back fixed what weeks of surface work could not.
- **Basis.** measured. **Scope.** any camera-based scene.

### A camera move is one move
`id: scene.one-move` · principle 3

- **Rule.** Design each shot's camera as one continuous move, with continuous position, speed and acceleration (a
quintic blend gives all three), and look at its speed graph before rendering.
- **Why.** A slow drift followed by a catch-up reads as "too slow, then a jerk", even when speed never jumps.
- **Basis.** measured. **Scope.** any camera move.

### Make parallax visible
`id: scene.parallax` · principle 2

- **Rule.** To show depth, truck while panning to hold the subject still, so the camera pivots around it. Foreground and
background then slide in opposite directions.
- **Why.** A plain pan moves everything the same way and hides most of the parallax a truck could give.
- **Basis.** measured. **Scope.** any camera move.
- **Check.** Compare pixel offsets of near and far pieces against the subject, including how much of the move happens
before anything covers the scene.

### Keep the camera steady where the eye reads
`id: scene.steady-read` · principles 1, 4

- **Rule.** On an information shot, use one small steady push; don't aim the camera at each action as it happens.
- **Why.** A camera that follows the action up and down reads as jerky and pulls the eye off what it should read.
- **Basis.** director notes. **Scope.** any information beat.

### A camera move changes what the set must survive
`id: scene.reaudit-angles` · principle 2

- **Rule.** When a camera angle changes, re-check every set piece from the new view.
- **Why.** Shortcuts that worked from low down (a beam near the lens, a leg hidden under a table, edge strips stopping
short of rounded corners) show once the camera rises.
- **Basis.** measured. **Scope.** any 3D set.

## Continuity between shots

### Continuity is not literal geography
`id: scene.continuity` · principle 1

- **Rule.** Shots need to feel like one place, not match a map. Screen direction, light direction, palette, floor
treatment and shared small elements carry that. Compose each shot for its own frame, cheat positions when it helps, and be
open about the cheat.
- **Why.** Exact geography can ruin individual frames; the audience reads the place, not the coordinates.
- **Basis.** principle. **Scope.** any sequence of shots.

### A cut-in from the same side
`id: scene.cut-in` · principle 2

- **Rule.** For a closer shot, put the camera on the previous camera's line to the subject.
- **Why.** From the same side, the cut reads as a push in rather than a jump.
- **Basis.** principle. **Scope.** any cut-in.

### Echo a move, don't copy it
`id: scene.echo-move` · principle 1

- **Rule.** When a later shot answers an earlier one (a reverse, a return), make it feel like the same move rather than a
one-to-one replica.
- **Why.** An exact replica reads as a repeat; an echo reads as intent.
- **Basis.** director notes. **Scope.** any sequence.

## What fills the frame

### One idea carries the composition
`id: scene.one-idea` · principles 1, 5

- **Rule.** Find the single gesture first (a current running from a screen to the horizon, say), then hang details off it.
Colour can carry the story along it, warm at the source, cooling with distance.
- **Why.** Details without a carrying idea scatter the eye.
- **Basis.** principle. **Scope.** any frame.
- **Check.** A small greyscale thumbnail should still read.

### Keep the ground quiet
`id: scene.quiet-ground` · principles 1, 5

- **Rule.** Fill a background with fewer pieces, mostly tone on tone, with one accent. On an information shot (a puzzle,
a card to read), keep background life out of the frame; floating elements belong to the shots that show the world.
- **Why.** Many bright, evenly spread objects make a floor busy and take the accent colours away from the message.
- **Basis.** director notes; measured. **Scope.** any scene.

### Nothing passes in front of the subject
`id: scene.subject-clear` · principles 1, 2

- **Rule.** Background elements never cross in front of the subject.
- **Why.** A crossing piece interrupts the read at the worst moment and breaks the depth order the eye expects.
- **Basis.** director notes. **Scope.** any scene with a subject.
- **Check.** Track crossings in front of the subject across every frame; aim for zero.

### A crowd made of the subject
`id: scene.crowd-from-subject` · principles 1, 4

- **Rule.** Build a crowd of objects only from what the scene is about (its real pieces, scores, symbols), never from
decorative shapes, speed lines or specks.
- **Why.** A storm meant to be "his games" read as a mess until only pieces taken from the subject remained; then it read as
a chaos of games.
- **Basis.** measured; director notes. **Scope.** any swarm or crowd.

### Reuse what already has life
`id: scene.reuse-life` · principles 5, 6

- **Rule.** Build crowds and background life from existing animated characters and rigs, driven by one control, rather
than drawing rows of static shapes.
- **Why.** One control on existing life gives a whole audience a performance for little effort.
- **Basis.** measured. **Scope.** any crowd.

### Check that motion keeps the meaning
`id: scene.meaning-checks` · principle 4

- **Rule.** Look at every moving piece for what it says mid-motion, and at the whole frame's shape:
  - a spinning plus becomes a times sign (rock it instead);
  - a flipping tile needs a designed back, or the flip makes it vanish;
  - growing a rounded shape by scale squashes its corners (slide it up through the floor instead);
  - a curved row of dots over a curved row of bumps reads as a grinning mouth;
  - a rolling number can pass through a wrong value (roll the digits together);
  - a small tag beside a number reads as part of a sum (make it a corner badge, and clear it once read).
- **Why.** Some faults only exist in motion, or only in the whole frame.
- **Basis.** measured. **Scope.** any.
