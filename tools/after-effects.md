# After Effects

Gotchas and techniques, searched by symptom. Each entry: Symptom, Cause, Fix, Seen (AE version and date). Unless noted,
seen in AE 26.5 (2026) on macOS, October to November 2026. Craft rules live in `craft/`; this file is only how AE behaves.

## Scripting (ExtendScript)

### Every later script hangs after one error
`id: ae.script-error-dialog`
- **Symptom.** AE stops responding to scripts.
- **Cause.** A script error opens a modal dialog; it blocks every script after it until someone clicks OK.
- **Fix.** Wrap every script in try/catch and write errors to a report file. Run one script at a time; never send a
script while another may still be running (including one moved to the background). Common throwers: text + array
(`ae.text-plus-array`) and reading `xRotation` on a 2D layer.

### "invalid numeric result (divide by zero?)" when building a string
`id: ae.text-plus-array`
- **Symptom.** A harmless line like `"pos " + p` throws a divide-by-zero error.
- **Cause.** Arrays have built-in maths operators in AE 26.5 scripts, so text + array is evaluated as maths.
- **Fix.** Use `p.join(",")` when building strings or expressions. It also bites inspection scripts.

### Expressions that read other layers fail with "Internal error" after a rebuild
`id: ae.rebuild-once`
- **Symptom.** After deleting and recreating a comp a second time in one session, expressions reading layers by name fail.
- **Cause.** AE's expression engine keeps stale references; only a restart clears it. Re-applying expressions doesn't.
- **Fix.** Rebuild a comp once per AE session; for small changes, patch keys and expressions in place. Before a full
rebuild, restart AE: save any work worth keeping as a new version first, then close without saving the broken
state, `app.quit()`, reopen, and wait until AE has really loaded (a
person or a screenshot confirms it); then build once, run heal, check expressions, render. Baking the broken expressions
to keys doesn't cure it. Keep a small "heal" script that re-applies expressions AE disabled mid-build, run it before
renders, and copy it (with the render helper) into every new scene or project.

### A rebuild that was fast becomes slow
`id: ae.purge`
- **Symptom.** After hours of rebuilds a build goes from 40 seconds to over 2 minutes.
- **Fix.** Restart AE; start build scripts with `app.purge(PurgeTarget.ALL_CACHES)`.

### `in` can't be an object key
`id: ae.reserved-in`
- **Symptom.** A syntax error on an object literal.
- **Cause.** `in` is reserved in ExtendScript.

### Moving keys in time
`id: ae.move-keys`
- **Symptom.** There's no API to shift a key in time.
- **Fix.** Read every key's value, interpolation, temporal eases, spatial tangents and flags, remove the keys, re-add
them at the new times and restore everything. 2D layers still take three-value spatial tangents. Colour keys have four
values; most ease helpers can't take them, so keep colour keys linear or handle them separately.

### Reading rest values from keyed properties drifts
`id: ae.no-readback`
- **Fix.** Keep rest values as constants in the build script; never read them back from keys, or reruns drift.

### Parenting moves or mirrors a layer
`id: ae.parent-jump`
- **Symptom.** Content parented under a rotated or auto-oriented null comes out mirrored or skewed.
- **Cause.** `layer.parent = X` keeps the old world transform by adding compensation.
- **Fix.** Use `layer.setParentWithJump(X)`, then set local values. Duplicated layers also get renumbered names.

### Stacking order changes between runs
`id: ae.copy-order`
- **Fix.** `copyToComp` order isn't stable; set order explicitly afterwards (`moveToEnd`, `moveBefore`).

### References into an effect list go stale
`id: ae.effect-refs`
- **Symptom.** Setting a value on an effect property errors after adding another effect.
- **Cause.** Adding a property to the effects list invalidates earlier references.
- **Fix.** Look each property up again by name before keying.

### `replaceSource` renames layers
`id: ae.replace-source`
- **Symptom.** A layer is no longer found by its name after swapping its source.
- **Cause.** A layer whose name was never set explicitly takes its new source's name.
- **Fix.** Set names explicitly, or look layers up by both names.

### 2D values come back with three numbers
`id: ae.2d-three-values`
- **Symptom.** Key maths on a 2D layer's position or scale produces NaN eases.
- **Fix.** Slice `position.value` and `scale.value` to two numbers on 2D layers before doing maths.

### `saveFrameToPng` returns before the file exists
`id: ae.save-frame-async`
- **Fix.** It's asynchronous: wait for the files, and don't change the comp until they exist. It renders at the comp's
resolution factor: set half before calling it for rough stills.

### Borrowing a comp from another project brings it in empty
`id: ae.import-empty`
- **Fix.** Rebuild small things natively instead of importing a project to borrow one comp.

### Apply a cubic-bezier curve as keyframe ease
`id: ae.bezier-ease`
- **Symptom.** A named curve such as (0.35, 0, 0.1, 1) has to become AE keyframe ease, and AE has no bezier input.
- **Fix.** For a key pair whose value changes by `change` over `duration` seconds: `outInfluence = x1 * 100`,
`outSpeed = (y1 / x1) * change / duration`, `inInfluence = (1 - x2) * 100`,
`inSpeed = ((1 - y2) / (1 - x2)) * change / duration`. Spatial properties take one `KeyframeEase` and `change` is the
path length; other properties take one per dimension. AE needs influence between 0.1 and 100, so a curve with x1 = 0 or
x2 = 1 needs clamping. Use custom ease, not auto-bezier. This is how the curves in `motion.curve-tokens` get into AE.

### Retime a scripted build without rewriting it
`id: ae.time-map`
- **Fix.** Pass every key time through a piecewise time map (old beat times to new) inside the key helpers. One build
script keeps working through retimes; a shot that jumps gets a separate shift.

## Expressions

### An expression silently returns its default
`id: ae.detached-effect`
- **Symptom.** An opacity driven by sliders renders at 100% whatever the sliders say.
- **Cause.** Storing `thisComp.layer("X").effect` in a variable and calling it later fails; the property falls back.
- **Fix.** Call `L.effect("Name")(1)` on the layer directly. Check `property.expressionError` after setting any
expression. Seen November 2026.

### Controls on a hidden layer read as defaults
`id: ae.controls-on`
- **Cause.** Effects on a disabled (eye off) layer are skipped at render.
- **Fix.** A controls null must stay switched on.

### Fill effect opacity runs 0 to 1
`id: ae.fill-opacity`
- **Fix.** In expressions, the Fill effect's Opacity is 0 to 1, not 0 to 100.

### Facing idioms
`id: ae.lookat`
- **Fix.** `lookAt(cameraPos, position)` faces the camera; `lookAt([0, y, 0], position)` faces an axis. To keep a 3D
logo parallel to the image plane when the camera looks elsewhere, use `lookAt(position - cameraForward, position)` and
bake it.

### Never scale to exactly zero
`id: ae.no-zero-scale`
- **Symptom.** Layers depending on a layer's `toWorld` error out.
- **Fix.** Scale to 0.5% instead of 0.

## 3D

### Classic 3D sorts overlapping flat layers by their centres
`id: ae.classic-sorting`
- **Symptom.** An arm draws over a face, a number under its own tile, a card in front of what it should be behind.
- **Cause.** Two flat 3D layers that overlap on screen without intersecting are ordered by camera distance to each
layer's centre, not by their surfaces.
- **Fix.** Use one of four reliable arrangements: the layers truly intersect (sorted per pixel); they share one plane and
one centre (stack order decides); they are one precomp; or they never overlap on screen (check every frame).

### A 2D layer splits 3D render groups
`id: ae.2d-splits-3d`
- **Fix.** A 2D layer (even an empty shape layer) between 3D layers splits Classic 3D groups. Use it deliberately to draw
one 3D group over another.

### Renderers differ
`id: ae.renderers`
- **Fix.** Check `comp.renderer` before copying 3D layers between comps: `ADBE Calder` is Advanced 3D, and
`ADBE Advanced 3d` is Classic 3D, despite the name. Advanced 3D can extrude; Classic 3D can't, so an extruded layer
copied into Classic becomes a flat sheet.
- **Observed once.** Advanced 3D drew an extruded body over flat 3D layers at any depth; a later test didn't reproduce
it, so the condition is unknown. It also ignored the Fill effect on its shape layers; not retested. If either shows up,
render body and details as separate comps with the same camera.
- **Also.** Advanced 3D depth of field is per pixel and grainy at default quality, and the camera's Blur Level is hidden.

### No layer motion blur in Advanced 3D
`id: ae.a3d-motion-blur`
- **Symptom.** Setting `layer.motionBlur` throws "not supported by the current composition renderer".
- **Fix.** Use CC Force Motion Blur on a wrapper comp (16 or more samples), with its own background solid.

### Effects on a 3D shape layer land in screen space
`id: ae.shape-3d-effects`
- **Symptom.** A Grid effect on a 3D shape floor lies flat to the screen; Gradient Ramp points miss.
- **Fix.** Use a solid with a mask, or a precomp, for surfaces that carry effects; convert ramp points with `toComp`.

### Large 3D shapes break near the frame edge
`id: ae.big-3d-shapes`
- **Symptom.** Strokes drop out on big 3D shape layers near the edge.
- **Fix.** Draw large surfaces in a flat comp and place that comp in 3D.

### A transparent shadow precomp renders solid black
`id: ae.shadow-precomp`
- **Symptom.** In Classic 3D, one shared transparent shadow precomp on the floor rendered black and hid the floor.
- **Fix.** One layer per shadow, each at its own small height, following its object by expression; coplanar layers cut
each other. A shadow's scale must include its object's scale.

### Measure where a point lands
`id: ae.to-comp`
- **Fix.** Use `toComp` on a temporary null to see where a 3D point lands on screen before designing a surface.

### Animation clips at a precomp's edge
`id: ae.precomp-headroom`
- **Symptom.** A bounce or overshoot inside a precomp gets cut off.
- **Cause.** A precomp only renders inside its own frame.
- **Fix.** Size the precomp for the whole motion, including the overshoot (about 300 px for one bounce).

### Fake a card's thickness in Classic 3D
`id: ae.card-thickness`
- **Fix.** Classic 3D can't extrude (`ae.renderers`): stack a few rounded-rect slices behind the face, all under one
null, so the card moves as one piece.

## Text

### Font size tops out at 1296
`id: ae.font-cap`
- **Fix.** Size bigger type by uniform layer scale.

### Variable font instances by name
`id: ae.variable-font`
- **Fix.** Set an instance by its full name (family plus axis values), in the form
`RobotoFlex_144.000opsz_440.000wght_42.000wdth_760.000YTUC`: each axis value with three decimals, then the axis tag. AE
drops axes at their default from the name and refuses names over 63 characters. `tracking` must be an integer.

### Measured text bounds don't match the ink
`id: ae.source-rect`
- **Fix.** `sourceRectAtTime` doesn't match the glyphs; place the text, render a still and measure the rendered pixels.

### A font lacks a glyph
`id: ae.missing-glyph`
- **Fix.** Check the font has the glyph before designing with it (a display font had no arrow; draw a shape instead).

### Rolling digits
`id: ae.odometer`
- **Fix.** A text animator on Position plus a mask on the text layer; roll the digits together.

## Effects and look

### Gaussian blur stops at a shape layer's bounds
`id: ae.blur-bounds`
- **Fix.** Add an invisible full-frame rectangle to the shape layer so the blur has room.

### Blur on a precomp is in layer pixels
`id: ae.blur-precomp`
- **Fix.** To get `b` pixels on screen, use `b × distance / (zoom × scale / 100)`.

### Blurriness is not sigma
`id: ae.blur-sigma`
- **Fix.** Gaussian Blur's Blurriness is about 3.5 × sigma (measured with a test comp). Convert when matching a mock-up
made elsewhere.

### Glow brightens the whole layer
`id: ae.glow`
- **Symptom.** A glow washed a pale plate to grey-white and dark cards to bright blue.
- **Fix.** For a rim glow, blur a copy of the outline only. For a film-wide bloom, see `craft/look-and-finish.md`.

### Hairline seams inside letters from a design-tool SVG
`id: ae.fill-rule`
- **Cause.** SVG paths fill non-zero by default; an even-odd fill in AE leaves seams at full resolution.
- **Fix.** Keep non-zero. Rebuild an "outside stroke" band as a stroke on the letters, not a separate filled band.

### Shape contents draw top first
`id: ae.shape-order`
- **Fix.** In a shape layer, the first item in the contents draws on top.

### Banding in soft gradients
`id: ae.banding`
- **Fix.** Work in 16 bpc with a little grain over soft gradients.

## Performance

### Switch things off, don't hide them at opacity 0
`id: ae.eye-off`
- **Cause.** At opacity 0, expressions still run; with the eye off, the layer and its expressions are skipped.
- **Fix.** Keep a toggle script for heavy systems (a storm of hundreds of pieces) and work with them off.

### Cull pieces outside the camera
`id: ae.cull`
- **Fix.** Drive each piece's opacity to 0 when it's behind the camera or off-screen by more than its half-diagonal plus a
margin for motion blur (250 px worked). Project the piece through `thisComp.activeCamera` in its opacity expression.

### Expression chains slow the scene
`id: ae.expr-chains`
- **Symptom.** A scene gets slower to preview and render as expressions pile up.
- **Cause.** Expressions that read other expression-driven layers re-evaluate the whole chain every frame.
- **Fix.** Bake driven transforms to keys. For ambient layers, compute static values in the build script instead of
per-frame expressions.

### Motion blur samples are per comp
`id: ae.mb-samples`
- **Fix.** Set `motionBlurSamplesPerFrame` and `motionBlurAdaptiveSampleLimit` per comp. 32/256 cured stepping on fast
pieces but cost about 4× at a 360° shutter.

## Time and editing

### Time remap without keys hides the property
`id: ae.time-remap`
- **Fix.** Keep its keys; set both to the same value to hold a frame. A source shorter than the shot (or an offset layer
reading past its end) renders black: extend sources before offsetting. A layer remapped to hold a frame stays frozen when
its source is replaced: only remap sources shorter than the shot, and turn remapping off after swapping in a full-length
source.

### Cut on an exact frame
`id: ae.exact-frame-cut`
- **Symptom.** Motion blur ghosts both shots into the last frame.
- **Fix.** Place cuts on exact frame times.

## Render and colour

### A master renders darker than its parts
`id: ae.working-space`
- **Cause.** A colour-managed working space (sRGB) reinterpreted lossless QuickTime Animation parts.
- **Fix.** For a finish comp built from AE-rendered parts, set the working space to None; then diff the master against a
part (expect a difference of at most 1 level). AE may show a missing-profile dialog: the result can still be correct.

### Rendering outside the app
`id: ae.aerender`
- **Fix.** `aerender -project P -comp C -s FIRST -e LAST -RStemplate "Best Settings" -OMtemplate "Lossless"` renders
without the app; add `-renderSettings "Resolution: Half"` for roughs. Kill leftover render processes after a rejected or
timed-out call.

### Effect and Lumetri property indices
`id: ae.indices`
- **Fix.** Pro Levels (ADBE Pro Levels2, values 0 to 1): 4 input black, 5 input white, 6 gamma, 7 output black, 20 green
gamma, 27 blue gamma. Lumetri: 21 Contrast, 22 Highlights, 23 Shadows, 25 Blacks.

## Recipes

### A film finish built over the assembled master
`id: ae.finish-recipe`
- **Fix.** One finish project, 16 bpc, working space None (see `ae.working-space`), the full-resolution parts placed end
to end in a master comp. Over it:
  - **Scene match:** one adjustment layer per scene with Pro Levels on individual controls, values fitted offline from
    per-scene medians; crossfade layers across joins meant to be seamless.
  - **Film curve:** Lumetri Contrast, Highlights and Shadows for a soft S-curve (calibrated against the picked mock-up).
  - **Bloom:** a mask comp (graded picture → luminance → Levels with a soft knee, e.g. input black 0.62, gamma 0.6), then
    several copies of it, each with Gaussian Blur at a different size and a Tint toward the glow colour, blended Screen; each
    copy's opacity is weight × Gain × Amount from sliders on a controls null.
  - **Grain:** a 50% grey solid with Noise (colour noise off, clip on), blended Overlay; it changes every frame by default.
  - **Vignette:** a black solid with a feathered elliptical mask; key its opacity to 0 across anything meant to be pure white.
- **Seen.** AE 26.5, November 2026.

### Calibrating effects against a mock-up
`id: ae.calibrate`
- **Fix.** Build a separate calibration project: a black-to-white ramp through the candidate grade, a 2 px white line through
Gaussian Blur at a few sizes, grain over 50% and 15% grey patches. Render with aerender, measure in a script, and fit the
settings to the mock-up. Rerun the blur test in a new AE version before trusting the Blurriness-to-sigma ratio.
- **Seen.** AE 26.5, November 2026.

### Fade strokes along their length; fade a floor
`id: ae.fade-recipes`
- **Fix.** Strokes: `Stencil Luma` gradient solids above the strokes in a precomp fade them along their length; two stack
to fade in two directions. A floor: fade it by opacity with a heavily feathered mask on the floor layer, drawn in the
layer's own source space (the how-to behind `scene.ground-edge`).
