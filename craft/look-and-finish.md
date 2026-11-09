# Look and finish

How a piece looks: building the look on stills, light and value, form, colour, reading at real size, then the finish (grade,
glow, grain) and the final render. Tool-free. How to do it in a given tool lives in `tools/`.

Principles behind this chapter: [7 Change the least that fixes it](../CORE.md), [2 Judge what the viewer sees](../CORE.md),
[1 Know what each moment is for](../CORE.md), [6 One source of truth](../CORE.md).

## Building a look

### Settle the look on stills
`id: look.stills-first` · principles 1, 7

- **Rule.** Develop the look on a few full-size still frames of real shots before carrying it into animated work. Change one
thing per study, keep the rest frozen, and show each checkpoint before the next.
- **Why.** A still is cheap to revise and compare. A look changed across animated shots costs a rebuild of each, and drifts.
- **Unless.** Motion roughs can run in parallel on placeholder art; the look lands on them once the stills are agreed.
- **Basis.** principle; production practice. **Scope.** any styled piece.

### Reference is for the look, not the build
`id: look.reference-not-geometry` · principles 6, 7

- **Rule.** A reference image or generated render is evidence for value, light and mood. Name what it does (where the darks
sit, how bright the edges are), then rebuild that through your own camera and assets. Don't trace its geometry.
- **Why.** Generated geometry doesn't hold one camera, and work that copies a reference too literally loses the forms you
already had: a character traced from a comp came back flat.
- **Basis.** principle; director notes. **Scope.** any work built from references.

### Fix the structure, not the surface
`id: look.fix-structure` · principle 7

- **Rule.** When a look fails, check composition, camera, light and form before reaching for gradients, glow, grain or extra
decoration. A card whose side can't be seen at its angle will not read as solid however it is shaded: turn it until the side
shows, with front, bevel and side all from one camera rather than skewed separately. A slab that fills the frame because the
camera is too close will not read as the object: move the camera.
- **Why.** Surface work over a structural fault adds cost and still fails. Saturation and a thin glowing outline can't stand in
for a visible front, bevel and side; decorative forms don't repair weak lighting; grain doesn't replace light or depth.
- **Basis.** principle; measured (a shallow card at a slight turn showed about 2 px of side at 1080 wide; a deeper card turned
further showed about 10 px, and the side read). **Scope.** any.
- **Check.** Ask what changed in camera, light or form. "Only the surface" usually means the note comes back.

### Diagnose before restyling
`id: look.diagnose` · principle 7

- **Rule.** When a look is called "off" without a cause, test one candidate cause at a time on frozen staging (more light, a
neutral hero, a different hue spread, one accent), and let the director pick, before restyling anything.
- **Why.** The first guess is often wrong. In one case removing decoration changed nothing; the issue was value and colour
distribution.
- **Basis.** measured (one case). **Scope.** any revision of an established look.

## Light and value

### Bright edge beside a dark pocket
`id: look.edge-and-pocket` · principles 1, 2

- **Rule.** Make lit and shadowed surfaces clearly different. Put a dark gap next to each lit edge, put luminous marks on a
darker face, and keep foreground crops and distant shapes quieter than the hero.
- **Why.** Light reads by contrast with what sits beside it. A bright edge on a bright field disappears.
- **Basis.** principle. **Scope.** any lit or shaded scene.

### Contrast is a value structure
`id: look.value-structure` · principles 1, 7

- **Rule.** When something "lacks contrast", look at where the values sit, not at saturation. The usual fault is a broad
midtone wash (grey or pastel haze spread over the frame); the fix is deeper dark gaps and concentrated bright areas. The
opposite fault is real too: everything dark and one colour.
- **Why.** More saturation makes a frame more colourful without giving it a lighter and a darker place.
- **Basis.** principle; director notes ("more colourful but not solved the contrast"; "too dark overall and all the same
colour"). **Scope.** any.
- **Check.** Greyscale at thumbnail size: there should be a clear lightest area, a clear darkest area, and a hero that sits on
one against the other.

### Background light is its own layer
`id: look.background-light` · principles 5, 6

- **Rule.** Keep the background light field (broad bands, falloff, haze) separate from the lighting on objects. Keep its
falloff smooth and its dark areas deliberate, and give background elements lower contrast so they blend in. A texture that
describes the space (a floor grid) stays still in that space and lies in its plane; light and noise drift over it.
- **Why.** A field built from blocks reads as "patches of colour instead of gradients of sky"; background pieces at full
contrast compete with the hero; a sliding or screen-flat grid reads as a filter, not as ground.
- **Basis.** principle; director notes. **Scope.** any scene with an atmosphere.

### Choose dimensionality per element
`id: look.dimensionality` · principles 1, 7

- **Rule.** Decide for each element how much depth it gets, and keep that construction. Flat character art stays flat when
props around it are extruded; its form comes from its own shading and acting. A flatter card doesn't need a flat background.
- **Why.** Inflating flat artwork to match 3D props loses the drawing; flattening everything loses the space.
- **Basis.** principle; director notes. **Scope.** any mixed 2D and 3D piece.

### Stylised shading, not physical materials
`id: look.stylised-materials` · principle 1

- **Rule.** Shade in a few clear value bands (flat or toon shading). Avoid physically based textures and render-style surface
detail.
- **Why.** In a graphic piece the shading should read at a glance; physical materials pull it toward a generic 3D or
generated look.
- **Basis.** taste (director: "keep shading flat and avoid PBR", "toon type NPR shading"; "looks too 3D" as a fault). Not
universal: a photoreal brief overrides it. **Scope.** stylised motion graphics.

## Colour and reading size

### A palette with roles
`id: look.palette-roles` · principles 1, 5

- **Rule.** Keep a small palette: one base family running from near-black to white, plus a few accents, each with a job
(category, active measure, selection, status, action). Don't colour every object; the rest stays tone on tone. Real product
colours stay as the product has them: don't recolour a source accent into the house hue.
- **Why.** An accent on everything is no accent. Roles keep colour meaning the same thing across shots.
- **Basis.** principle; director notes. **Scope.** any.

### Judge the look at viewing size
`id: look.viewing-size` · principle 2

- **Rule.** Settle where it appears (alone, inside UI, over content, in a clip), its final display size and its crop
before building. Check every look checkpoint at the size it will be watched (a phone-sized export for a vertical film)
and in greyscale, as well as at full size. Hero information must survive; small labels get enlarged or simplified;
foreground crops may blur.
- **Why.** Detail that carries the look at full size can vanish on a phone; contrast that reads in colour can collapse in value.
- **Basis.** principle; measured. **Scope.** any.
- **Check.** Three exports per checkpoint: full colour, greyscale, and the target's viewing size (phone size for a
vertical film). Say which ones you actually looked at.

## Finishing: grade, glow, grain

### One finishing pass over the master
`id: finish.one-pass` · principle 6

- **Rule.** Grade and finish in one place, over the assembled full-resolution master, never inside the scene files. Shot
matching comes first, then one film-wide look on top.
- **Why.** One place keeps the look consistent and changes it without touching or re-rendering scenes.
- **Basis.** principle. **Scope.** any multi-shot piece.

### Mock up, pick, then calibrate
`id: finish.calibrate` · principles 2, 6

- **Rule.** Develop the finish as mockups on real frames, with a few options side by side for the director to pick. Then match
the tool's settings to the picked mockup with rendered test patterns (a black-to-white ramp, a thin line, flat grey patches),
measured numerically. Verify test stills against the mockup before rendering the film.
- **Why.** A blur "amount" in one tool is not a blur radius in another. Measuring carries the approved look over exactly.
- **Basis.** measured (stills matched the mockup within about 0.01 to 0.02 per scene). **Scope.** any finish.
- **In tools.** Blur calibration and the grade build: `tools/after-effects.md`.

### Match shots before the look
`id: finish.match` · principles 2, 6

- **Rule.** Match scenes to each other: one shared black floor (lift crushed blacks, lower milky ones), a tint partway toward
the film's median (about 70% worked), a small lift for dim scenes. Measure per scene as the median over its frames. Keep
deliberate extremes (a dark scene, a whiteout, a lit floor). Crossfade corrections across joins designed to be seamless. Then
one gentle S-curve with a soft roll-off into white for the whole film.
- **Why.** Unmatched scenes make every cut a jump in exposure; matching to a median moves no scene far.
- **Basis.** measured. **Scope.** any multi-scene piece.
- **Check.** Measure the joins after grading: they should be as smooth as before.

### Protect the pure values
`id: finish.protect-extremes` · principle 2

- **Rule.** Keep tint corrections out of the highlights so whites keep their colour. Fade the vignette out across anything
meant to be pure (a whiteout). Check that intended whites are still at full white after the finish.
- **Why.** A tint shift turned a white title grey-white in one mockup; a vignette dirties a whiteout.
- **Basis.** measured. **Scope.** any grade.

### Bloom scales with bright area
`id: finish.bloom` · principles 2, 7

- **Rule.** Build glow from a bright mask with a soft knee, blurred at several sizes (each about two and a half times the last)
with gently falling weights. Take it only from the bright parts, never from the whole layer. Set its strength against
ordinary approved scenes, then check the largest bright area in the film.
- **Why.** Glow scales with how much is bright: a strength that suits small highlights floods a giant white title. A hard-knee
mask with two blurs reads as a rim around the letters, a step, then a flat haze. Several soft octaves fall off smoothly.
- **Basis.** measured; director notes ("way too much glow", "not smooth enough"). **Scope.** any glow, bloom or halation.
- **Check.** Look at 100% at the biggest white shape and at the darkest scene with a highlight.
- **In tools.** Why a tool's own Glow effect may wash a whole layer: `tools/after-effects.md`.

### Grain: fine, mono, moving
`id: finish.grain` · principles 2, 5

- **Rule.** Use fine monochrome luminance grain, new on every frame, blended so it lives in the midtones (an overlay-type blend
over mid grey). Judge it at 100% on full-resolution frames.
- **Why.** Colour grain reads as noise, static grain reads as a dirty screen. An overlay blend over mid grey leaves pure black
and pure white untouched. Half-resolution frames can't show it.
- **Basis.** technical fact (overlay arithmetic); taste for the amount. **Scope.** any finish.

### Stop banding at the source
`id: finish.banding` · principle 2

- **Rule.** Work soft gradients at 16 bits per channel and keep light grain over them; check dark gradients at 100% in the
final encode.
- **Why.** An 8-bit delivery quantises a slow dark gradient into steps; grain dithers across the steps.
- **Basis.** technical fact. **Scope.** any gradient-heavy piece.

## Output and QC

### Check the master before grading it
`id: finish.colour-management` · principles 2, 6

- **Rule.** After assembling rendered parts in a finishing project, compare the assembled master with the parts numerically
before grading. Use the same colour handling as the projects that made the parts.
- **Why.** Colour management can reinterpret footage through its embedded gamma tag. In one case the master rendered visibly
darker than its parts (mean luma 0.068 against 0.110), before any grade.
- **Basis.** technical fact (After Effects 26.5); measured. **Scope.** any pipeline that re-imports its own renders.
- **In tools.** `tools/after-effects.md`.

### One lossless master, versions from it
`id: finish.master` · principle 6

- **Rule.** Render one lossless graded master and encode every delivery from it. A variant (a version without prices, a
shorter cut) is a duplicate with only the changed part swapped and nothing retuned.
- **Why.** Re-encoding from encodes stacks loss; retuning a variant drifts it from the approved film.
- **Basis.** principle. **Scope.** any delivery.
- **Check.** Frames outside the swapped part are bit-identical to the main version.

### Motion blur on throughout, more samples for finals
`id: finish.motion-blur` · principles 2, 6

- **Rule.** Keep motion blur on while working so fast moves are judged as they'll be seen: 16 samples for review renders,
32 or more for finals, tested per shot on the fastest moves. Cut on an exact frame, or blur ghosts both shots into the last
frame.
- **Why.** Too few samples show a fan of separate edge copies; judging fast moves without blur misleads timing notes.
- **Basis.** measured (stepping on the fastest moves); the sample counts are a director decision (Nov 2026).
**Scope.** any piece with fast motion.

### Final QC
`id: finish.qc` · principle 2

- **Rule.** Before handoff: read the render logs; scan every frame for one-frame glitches and unintended blank or frozen
frames; compare the final with the approved rough, region by region; inspect 100% crops of text, fine lines, grids and dark
gradients; measure the joins; decode the whole file and check its metadata. Compare RGB and alpha separately. Watch it at speed,
and say so if you didn't.
- **Why.** A scan catches what playback hides, and playback catches what a scan can't. A combined RGBA difference can hide
changed RGB when alpha is unchanged.
- **Basis.** measured. **Scope.** any final render.
- **Check.** A difference you find is either explained (sharper edges at full resolution are expected) or reported. An
opaque preview background doesn't prove the asset is opaque; use an alpha-preserving capture for any transparency claim.
