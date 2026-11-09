# Rive

How Rive behaves for character work. Seen in the Rive editor and runtimes as used in October 2026 (exact version not
recorded). Character craft lives in `craft/character.md`.

## Rig and artboards

- Keep the whole character's scale and position on the parent's nested artboard instance, not inside the pose artboard.
- `clip=false` on a nested pose component lets full-size arms sweep out, but the parent mask, the outer canvas and a
  child's screenshot viewport can still crop. `clip=false` is omitted on readback because it's the schema default.
- Relocating a pivot: move the control, counter-translate its children, then reverse rotation keys if the direction flips.

## Curves

- A key's outgoing interpolation shapes the segment that follows it.
- Ballistic Y with a CubicValueInterpolator: X handles at 1/3 and 2/3, Y handles at `y0 + v/3` and `yEnd − (v + 2a)/3`
  (see [motion.ballistic](../craft/motion-and-timing.md)). A value interpolator shapes values; a time-easing interpolator
  shapes progress between them.

## Effects

- Give burst pop-scale and burst rotation separate controls when they need separate ownership. A constant full turn can
  be two linear keys; variable-speed or directional rotation needs another curve and a checked seam.
- If an entrance owns a particle event, its last hidden reset can set when it releases, even after the character has
  settled.

## State machines and ownership

- When parts need to run, stop or repeat on their own (`interactive.simplest-structure`), give the entrance, the hold and
  gesture, the eyes (open hold, blink, open hold) and the effects separate layers; choose each layer's start rule
  (immediate, cued by the entrance, or gated on readiness).
- A static Hold or Waiting state deliberately owns neutral values; an empty gate releases them; a skip initialiser applies
  its baseline once, then releases. Independent layers must not animate the same channels.
- Blinks and idles are one-shot timelines repeated by transitions; holds are loop timelines exited after one full cycle.
  Effective time includes the state's speed (a 23-frame blink at 0.25× lasts four times as long).
- When a contract picks one of several discrete poses through a View Model, prefer an enum to a number; keep whatever
  type an existing contract declares. Don't copy model names, enum indices or trigger names between files; verify the
  bound instance and the selected child's data context.
- Changing `autoPlay` after the entry state has evaluated doesn't restart anything; a native `play()` only resumes
  advancing. Fire the contract's play trigger.
- If reset and play reach a nested instance together, one trigger can be lost; a short static initialisation state helps.
- A hidden instance's timeline can keep advancing; pausing doesn't reset or hide it. With several pose instances, choose
  which ones advance and check that selection keys don't override the intended defaults; add a pause policy only if the
  project needs one.
- Observed time also changes with enabled work areas, transitions and delayed child starts.
- An event can start a loop (a sheen) at a chosen moment instead of a separate timed timeline.

## Saving and verification

- A save once kept timeline names and durations but lost the keyed tracks. Restore the subtree with fresh IDs and verify by
  readback: hierarchy, keys per timeline, and renders.
- Compare float32 values and omitted schema defaults by meaning, not by text.
- Compare RGB and alpha separately: an RGBA difference can hide changed RGB when alpha is unchanged.
- Before editing a live file, read it fresh and keep the user's edits made since.
- When reducing keys, remove only proven redundancies. A constant channel can go only if it never changes anywhere
  relevant, equals the base artwork value and has no ownership, reset or binding role; equal endpoints don't prove a
  static curve. Keep neutral and reset ownership, holds, easing boundaries, invisible reset keys and meaningful loop
  seam endpoints, and compare the evaluated motion and renders before and after. Interior collinear keys and duplicate
  endpoints may be redundant, but inspect delay, interpolation and timeline duration before removing them.
- Sharing identical curves or removing internal labels may help an export, provided public names and useful source
  organization are preserved.
