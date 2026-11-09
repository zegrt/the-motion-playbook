# Interactive

Pieces a product plays: in-app characters, UI motion, rewards, anything an app starts, stops or interrupts. The motion
craft in the other chapters still applies; this chapter covers what changes when the piece runs live. Tool-free. How to
do it in a given runtime lives in `tools/`.

Principles behind this chapter: [1 Know what each moment is for](../CORE.md), [2 Judge what the viewer sees](../CORE.md),
[3 Caused and continuous](../CORE.md), [6 One source of truth](../CORE.md).

### Settle the behaviour before building
`id: interactive.behaviour-first` · principle 1

- **Rule.** Before building, settle: what it communicates and where it appears, at what size and crop
(`look.viewing-size`); what starts it and what remains at the end; whether it repeats, reverses or can be
interrupted; which host, runtime and renderer play it; and what happens on first load, on replay or reset, and under
reduced motion. Write the choices down next to the project so someone else can reproduce them. Nothing carries over by
default from another project: frame rate, duration, number of poses, startup and autoplay are decided each time.
- **Why.** These answers decide the structure. Found late, they force a rebuild.
- **Basis.** principle; one interactive project. **Scope.** any interactive or embedded piece.

### The simplest structure that does the job
`id: interactive.simplest-structure` · principle 6

- **Rule.** A one-shot can be a single timeline. Split responsibilities (entrance, hold and gesture, blink, effects)
only when parts need to run, stop or repeat on their own, as a recurring or interruptible character may. A parent can
own shared placement and reveal while a child owns its own performance. Every animated property has one owner at a
time.
- **Why.** Extra structure is extra state to keep consistent, and two owners of one property fight.
- **Basis.** principle; one interactive project. **Scope.** any interactive piece.

### A small, named contract for the app
`id: interactive.contract` · principle 6

- **Rule.** What the app can set or read is small and semantic: each control has a name, type, default, direction and
valid values, written down for the project. Keep the contract intact through unrelated edits, and don't copy another
file's internal names into it.
- **Why.** Engineers build against the contract; a silent change breaks the product, not the animation file.
- **Basis.** principle. **Scope.** any piece an app controls.

### Observe the start, don't assume it
`id: interactive.observe-start` · principle 2

- **Rule.** Resuming playback is not the same as asking for the entrance. Set the initial data and start observing
first, then send the action the contract names.
- **Why.** A connection in the graph doesn't mean the piece is ready: a start that arrives together with a reset can be
lost.
- **Basis.** measured (one interactive project). **Scope.** any interactive piece. **In tools.** `tools/rive.md`, State
machines and ownership.
- **Check.** Watch the actual first visible frame and the actual completion, not the graph.

### Decide what shows while waiting
`id: interactive.startup` · principle 1

- **Rule.** Choose per project between transparent waiting, a visible idle, autoplay, an explicit start and a static
first frame. Loading and failure show through the host's own status, not through missing pixels.
- **Why.** "Nothing on screen" reads the same whether the piece is waiting, loading or broken.
- **Basis.** principle; one interactive project. **Scope.** any piece that loads in a product.
- **Check.** With transparent waiting, inspect the backdrop, glow and host alpha as well as the character.

### Reduced motion is a decision
`id: interactive.reduced-motion` · principle 1

- **Rule.** Decide explicitly what reduced motion does: drop large spatial entrances, reduce amplitudes, simplify
effects, or show a static presentation. A setting with that name means nothing until it's decided, and one project's
choice is not the next project's policy.
- **Why.** Assumed in either direction (freeze everything, or keep every loop), it fails someone.
- **Basis.** principle. **Scope.** any piece in a product with a reduced-motion setting.

### Interruption, replay and completion
`id: interactive.interruption` · principle 3

- **Rule.** Define reset, replay, interruption and mode changes around what the user is doing: whether an interrupted
action settles, reverses or restarts, whether a later mode change replays anything, and what happens to cancelled
requests and simultaneous inputs. Report completion once, at the end of the one-shot, not on every loop.
- **Why.** The app acts on these events; a completion fired every loop or a lost interruption shows up as a product bug.
- **Basis.** principle; one interactive project. **Scope.** any interactive piece.
- **Check.** Run each path the contract defines: start, hold, replay and reset, interruption, mode changes, repeated
input, selection; count completion events.

### Check it in its host, on its device
`id: interactive.qc` · principle 2

- **Rule.** An interactive piece is proven in its real host and on its target device, not in the editor. The behaviour
paths are checked by the rules that own them.
- **Why.** Each item is a path the app can take; an untested path is where it breaks.
- **Basis.** principle; one interactive project. **Scope.** any interactive piece.
- **Check.** Check the piece alone and in its real parent layout, at display size and speed, on first load and with
initial and missing data; test renderer-dependent features and final alignment in the intended host, and on the target
device. Say which level each claim reached (`verify.evidence-levels`).

### Identify what is handed over
`id: interactive.handoff` · principle 6

- **Rule.** A delivery identifies the actual asset and version, its entry point, and the source and runtime
deliverables separately. Include or link the current controls and defaults (`interactive.contract`), the initial and
ending presentation, looping and reset behaviour, and required runtime features. List unresolved checks; name their
evidence levels and practical limits (`verify.evidence-levels`).
- **Why.** A usable asset includes the information needed to start and control the right version. A file alone leaves
the next person to infer behaviour that the author already settled.
- **Basis.** principle; working practice from one interactive asset set. **Scope.** interactive asset deliveries.
- **Check.** The identified files and linked contract match the delivered version; behaviour or device claims that
were not verified are labelled that way.
