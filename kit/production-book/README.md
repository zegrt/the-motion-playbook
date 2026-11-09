# Production book kit

One production's book: where every unit stands, what the director approved and in what words, what's still open, and
their decisions. It lives in the project, never in the playbook. The method behind it is
[process/production-book.md](../../process/production-book.md); this is the tool.

## In five minutes

The tool stays in your clone of the playbook; the book goes in your project. Run every command from your project
folder, with the path to the tool (here `<playbook>` stands for where you cloned the playbook):

```
cd path/to/your-project
python3 <playbook>/kit/production-book/book.py new book --title "My film" --units "S01 Opening" "S02 Product"
```

That makes `book/` in your project. Then:

1. Write two or three sentences under "Now" in `book/BOOK.md`, and the look in `book/LOOK.md`.
2. Log work as it happens, still from the project folder. A version's output has to exist (`check` reports a current
   version whose file is missing), so render it first; here an empty file stands in for the render:

   ```
   mkdir -p out && touch out/s01_anim_v001_half.mp4
   python3 <playbook>/kit/production-book/book.py log version unit=S01 step=anim pass=rough \
       output=out/s01_anim_v001_half.mp4 summary="First pass" checked="watched at speed, half resolution"
   python3 <playbook>/kit/production-book/book.py log note unit=S01 version=s01_anim_v001 frames=f40-60 \
       priority=must text="The phone lands too late"
   python3 <playbook>/kit/production-book/book.py log approval version=s01_anim_v001 medium=call by=director \
       quote="Yes, that's it."
   ```

3. Run `check` at the end of each work block. Every `log` rebuilds the pages; after editing a record by hand, run
   `build`.

`example/` is a whole book for a fictional 15 second ad (three shots, two variants). Read `example/book/BOOK.md` to see
where it leads.

## What's in a book

| File | Written by | What |
|---|---|---|
| `book.txt` | you, once | title, kind (`linear`, `interactive`, `still`, `campaign`), steps |
| `records/*.txt` | `log`, or you by hand | the truth: one small `key: value` file per unit, version, approval, note or decision |
| `BOOK.md` | you above the marker, `build` below | the front page: "Now", then every unit by step |
| `LOOK.md`, `units/*.md` | you | the shared look; one page per unit, with "Now" kept to 15 lines |
| `CUT.tsv` | you | the cut, by hand: unit, version, source frames, film frames |
| `OPEN.md`, `DECISIONS.md` | `build` | the one open list, and the director's decisions |

For a contractor, copy the kit's `templates/PACKAGE.md` into the package folder and fill it in.

A record is plain text, so you can write one without the script:

```
kind: note
id: N-014
unit: S02
version: s02_anim_v003
frames: f120-140
priority: should
text: The card arrives in lockstep with the label; offset it a few frames.
date: 2026-03-02T16:40
by: director
```

A line starting with a space continues the value above it. `check` holds every record to the same rules `log` does, so
a record written by hand is never looser.

## How the state is worked out

Nothing depends on the order of the records, their dates or their file names:

- **The current version** of a unit and step is the one with the highest number. Versions are named
  `{unit}_{step}_v###` (`s05_anim_v003`), never reused, and `log` numbers them for you.
- **A version is approved** when an approval record names it, with the director's words, the director as `by`, how
  the words were given (the medium) and the date. `log` never fills in `by` for an approval or a decision: whoever runs
  the command records it; only the director gives it. A newer version is simply not approved yet; the front page shows
  the last approved one beside it.
- **A note is open** until a record with its id closes it (`state: closed`, `parked` or `wontfix`):
  `book.py log note id=N-001 state=closed` is enough. Closed stays closed: `log` refuses to reopen a note, and a new
  note gets a new id (`log` numbers notes too, `N-015`). A note that names a version names one of its own unit's.

## The commands

| Command | Does |
|---|---|
| `new PATH --title T --units "ID Title" ...` | makes a book from the templates; never overwrites one |
| `log KIND key=value ...` | writes one record and rebuilds; refuses one that breaks a rule (an approval or decision without the director's words, a reused id, a reopened note) |
| `build` | regenerates the generated pages |
| `status` | the front page in the terminal |
| `check` | errors (exit 1): every record against the rules, a current version whose output is missing. Warnings: versions that don't say what was checked, notes open too long, pages out of date |
| `close --inbox DIR` | writes the book's lessons (notes of type `lesson`) as one proposal for the playbook's inbox, once; the director's decisions stay in the book, with the project |

Every command takes `--book DIR` (default `book`) and `--by NAME` (default `$BOOK_BY`, then your login name);
`log --help` lists every kind and its fields.

## What it isn't

No server, no database, no viewer: plain files and one script with no dependencies. Without Python, the records and
pages are still readable and writable; you lose only the generated tables and the checks. The kit holds no client data:
the book, with the client's names, prices and links, stays in the client's project.

Left out until a production asks for them: claims for several writers at once (the method's team-mode rules still
apply, kept by hand), a generated delivery manifest, cut and timing checks, and a delivery record for interactive or
still pieces.
