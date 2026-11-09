# Sound and VO

Voice-over, music and sound effects for motion pieces: VO to picture, generated voices, checking takes, handing off to an
audio engineer, licences, delivery, and what measuring audio can't prove. Tool-free. How to do it in a given tool lives in `tools/`.

Principles behind this chapter: [1 Know what each moment is for](../CORE.md), [2 Judge what the viewer sees](../CORE.md),
[6 One source of truth](../CORE.md).

## Writing and timing VO

### Write it to be said
`id: sound.write-spoken` · principle 1

- **Rule.** Write VO as someone would say it: short lines, plain words, one idea each. Read every line aloud at the
intended pace, against the picture, before anyone records or generates it.
- **Why.** Lines that read well on a page often sound like an ad when spoken. Reading aloud also gives each line its first
honest length.
- **Basis.** principle; director notes on a film script ("sound more human"). **Scope.** any VO.

### Each line has a moment
`id: sound.line-moment` · principles 1, 2

- **Rule.** Give every line the picture moment it belongs to and the word that should land on it. Write the script as a
table: line, rough in-point, what it lands on. Leave some hits with no voice on them (a logo thud, a big impact), and let
demonstrated actions play without talk. When a beat is retimed, its word moves with it, landed on the word's measured start
([motion.word-sync](motion-and-timing.md#land-on-the-word-not-the-time)).
- **Why.** VO placed "somewhere in this scene" drifts off its meaning when the picture is retimed. A hit with a word on top
loses both.
- **Basis.** principle; director notes. **Scope.** any piece with VO.
- **Check.** Watch with VO only. Gaps you hear should be choices you can name, not leftovers.

### Split a line at a visual change
`id: sound.split-line` · principles 1, 3

- **Rule.** When one sentence spans two picture beats, cut it into two takes at the natural pause, so each half can sit on
its own beat. Keep together the words that describe one thing ("see patterns across games"), and separate the part that
belongs to the next picture ("and where to focus next").
- **Why.** One continuous take forces the picture to wait for the voice, or the voice to talk over the change.
- **Basis.** director notes; one production. **Scope.** any VO over cut or staged picture.

### Check a line can make both its hits
`id: sound.two-hits` · principle 2

- **Rule.** When a line has to land two words on two picture hits, measure the gap between the words in the take and the
gap between the hits. If they differ, say so early and choose: tighten the gap in the edit, move a hit, or split the
difference.
- **Why.** A title line's two words were 0.67 s apart; its two titles were 0.4 s apart. No placement lands both, and it is
cheaper to know before picture lock.
- **Basis.** measured. **Scope.** any double sync.

### Make it work with the sound off
`id: sound.sound-off` · principle 2

- **Rule.** For social pieces, put every key line on screen as well as in the voice, so the piece still reads muted.
- **Why.** Feeds often start videos muted.
- **Basis.** technical fact (feed autoplay, 2026); a common client requirement. **Scope.** social video.

## AI voice

### Generate all the lines in one take, then cut
`id: sound.ai-one-take` · principle 6

- **Rule.** Generate the whole script in one generation, with a clear pause between lines, then cut it at the silences into
numbered takes in script order. Export lossless (WAV or PCM) when the plan allows, and keep the original file beside the
takes.
- **Why.** Separate generations drift in tone, energy and pace; one take keeps one voice through the piece. Converting a
128 kbps MP3 to 24-bit WAV gives the right container, not better quality, so say when the source was compressed.
- **Basis.** technical fact (generative voices vary per generation; seen with ElevenLabs v4, November 2026). **Scope.** any
generated VO.
- **Unless.** One line needs a different delivery: regenerate it alone and compare it with its neighbours.

### Direct pace with words, not a slider
`id: sound.ai-pace` · principle 7

- **Rule.** If a generated voice is too slow, direct it in the text: pace tags, punctuation, explicit pauses only where you
want them. Then tighten the gaps between phrases in the edit. Stretch the audio last, and only a little.
- **Why.** Some voice models have no reliable speed control, and time-stretching a voice changes its character before it
saves much time.
- **Basis.** technical fact (ElevenLabs v4, November 2026: speed control unreliable, audio tags work; check current
docs). **Scope.** generated VO.
- **In tools.** Tag and pronunciation syntax: `tools/` (ElevenLabs).

### Spell out the names that matter
`id: sound.ai-pronunciation` · principle 4

- **Rule.** Give brand and product names an explicit pronunciation (phonetic spelling or IPA) before generating, and check
them in the takes. A transcription that hears the name as a different word is a warning to listen, not a verdict.
- **Why.** A brand name said wrong is the first thing the client hears. One take transcribed the brand as an ordinary name,
and it stayed unresolved through several versions.
- **Basis.** measured (transcription); technical fact. **Scope.** any VO with names.

## Checking takes

### Transcribe every take, and doubt the transcriber too
`id: sound.transcribe` · principles 2, 4

- **Rule.** After cutting, transcribe each take and compare it with the script: right words, right order, right count.
Name files by number and first words, so a mislabel shows. When a transcript differs from the script, a missing word or
an extra one, check the audio at that spot before re-editing: transcribe the take both with and without silence padded
around it, and compare with the uncut source.
- **Why.** Cutting by silence fails quietly: a take split in two, two lines merged, labels one place out (it happened). And
transcribers get very short edge words wrong both ways: one invented a 30 ms "And" before a take that had none, which
went away once silence was padded in front, and another pass lost the first "a" of "across". The audio was fine both
times.
- **Basis.** measured. **Scope.** any cut VO and automatic transcription.

### Measure each take against its slot
`id: sound.take-fits-slot` · principle 2

- **Rule.** Measure each take's length and its word start times, and compare them with the picture window it has to fit:
from its in-point to the next hit that must stay clear. List the lines that don't fit and say what would fix each one.
- **Why.** Otherwise the overrun is found in the mix, after picture lock.
- **Basis.** measured. **Scope.** any VO to picture.

## Handing off to an audio engineer

### Write for a person
`id: sound.handoff-human` · principles 2, 6

- **Rule.** The brief is a short document a person reads (a PDF), not a data file. Timecodes are `HH:MM:SS:FF`, never frame
numbers or seconds to three decimals. A short README in the folder points to the brief.
- **Why.** An engineer works in timecode with the picture running. A CSV of frame numbers is made for a script.
- **Basis.** director notes ("this is to send to a human, not an AI"). **Scope.** any external audio hand-off.

### Picture they can work against
`id: sound.handoff-picture` · principle 6

- **Rule.** Send two picture files: an edit-friendly proxy (such as ProRes Proxy) with burned-in timecode for the session,
and a clean H.264 for watching. State the exact frame rate in words ("30.000 fps non-drop, not 29.97"), the frame count,
the duration, and the timecode on the first frame.
- **Why.** 29.97 and 30 look alike in a menu. Over a minute they drift about 0.06 s apart, nearly two frames: every late hit
gets later.
- **Basis.** technical fact. **Scope.** any picture sent for sound.
- **Check.** Probe both files: same frame count, same rate, timecode on frame one.

### What the brief covers
`id: sound.brief-contents` · principle 1

- **Rule.** In order: what we need; the piece in one line; how it should feel (one line overall, then a short table, one
row per scene); the moments that must land, with timecodes; the VO script with rough in-points and what each line lands
on; any character sounds; music sources; rules from the client brief; deliverables; the process. Then an appendix that
lists every action in the picture by timecode, for reference.
- **Why.** Intent first, detail last. The appendix saves hunting for hits without saying what to do with them.
- **Basis.** one production, reviewed by its director. **Scope.** any external audio hand-off.

### Agree the feel before you write it
`id: sound.agree-feel` · principle 1

- **Rule.** Ask the director the feel questions (overall mood, references, one track or several, the biggest moments, what
happens at the silences) and write their answers. Don't draft the feel section from your own reading of the picture.
- **Why.** The feel section is the director speaking to the engineer. A guessed one points them the wrong way, confidently.
- **Basis.** director notes ("ask me stuff before making the how it should feel thing"). **Scope.** any brief.

### Name the moments, not the sounds
`id: sound.no-sound-suggestions` · principles 1, 7

- **Rule.** List what happens and what matters ("the catch is a hit", "sound drops to near-silence here"). Don't suggest a
sound for each action.
- **Why.** Choosing sounds is the engineer's craft. A suggestions column reads as the design already done.
- **Basis.** director notes (a suggestions column was removed from a brief). **Scope.** any brief to a sound designer.

### Rough in-points, dry takes
`id: sound.vo-handoff` · principles 6, 7

- **Rule.** Send VO as dry, unlevelled takes in the delivery format, numbered in script order, with the measured loudness
of each noted and the original source file included. Mark VO in-points as rough and ask the engineer to place each take
on its moment and say when a line needs to move.
- **Why.** Levelling belongs to the mix, in context; anything baked in can't be undone. The engineer will hear timing
problems that measurement missed.
- **Basis.** principle; one production. **Scope.** any VO hand-off.

### A short rights page, signed before work starts
`id: sound.rights-page` · principle 6

- **Rule.** One plain page, signed by the engineer before they start: the work; the fee and how it is paid; ownership
passes to the client on payment, worldwide, for the full term, in all media, whether or not it is used; the client may
edit and make versions (cutdowns, other formats, language versions); the work is original or properly licensed;
confidential until release, portfolio use with credit after.
- **Why.** Rights not written down get argued about when the piece is reused. Some jurisdictions
(India, for one) require a copyright assignment in writing, signed by the author, stating the rights, territory,
duration and fee, and let assigned rights lapse if unused for a period unless the agreement says otherwise.
- **Basis.** practice; not legal advice, check local law. **Scope.** any commissioned audio.
- **Unless.** The engineer has their own contract: check it covers the same points.

## Music and licences

### Plan the music for every version
`id: sound.music-versions` · principle 6

- **Rule.** Tell the composer every version the piece will have (other aspect ratios, cutdowns) and ask for clean edit
points, listed by timecode.
- **Why.** One long arc may not cut to 15 seconds without a jump. Planned edit points are free; found later, they cost a
remix.
- **Basis.** principle. **Scope.** any piece with cutdowns.

### License under the client's account
`id: sound.licences` · principle 6

- **Rule.** Library music and effects are licensed under the account of whoever publishes the piece. Ask the engineer for
the track names and links, and the source of every effect, and keep that list with the project.
- **Why.** A licence usually covers the account holder's projects; the engineer's personal subscription may not cover the
client's channels.
- **Basis.** technical fact (typical subscription library terms, 2026; check each library's terms). **Scope.** any library
audio.

## Sound effects

### Every layer has a job
`id: sound.layer-roles` · principles 1, 5

- **Rule.** Build an effect from layers with distinct jobs (identity, contact, weight, motion, tail, space) and only the
jobs the action has. Mute layers one at a time in context; drop any that change nothing. Choose the source by the
object's size and distance first, then process.
- **Why.** Stacked layers doing the same job blur the event. A loud generic whoosh annoys long before it helps. Ninety
layers is an inventory, not a soundtrack.
- **Basis.** practitioner sources; director notes (both "too loud and annoying" and "this event needs more than one
sound"). **Scope.** any sound design.

### Decide what leads each moment
`id: sound.foreground` · principles 1, 5

- **Rule.** For each moment, pick one foreground: voice, music or effect. VO first, music under it, effects supporting.
Settle the plain balance before reaching for EQ or ducking tricks.
- **Why.** When everything is equally loud nothing reads. Music too loud to hear the effects under it was the first note on
an early mix.
- **Basis.** principle; director notes. **Scope.** any mix.

### Sound ends where the action ends
`id: sound.ends-with-action` · principles 3, 4

- **Rule.** Stop a sound's texture when the pictured action stops; let only the contact's natural decay carry past.
- **Why.** A rolling-number tick that continued 0.26 s past the number settling made the picture look unfinished.
- **Basis.** measured. **Scope.** any sync effect.

### Silence as a hit
`id: sound.silence-hit` · principle 1

- **Rule.** A sudden drop to near-silence can be a moment of its own. Keep the faintest tail so it reads as intended.
- **Why.** Total digital silence sounds like a dropout or a broken file.
- **Basis.** taste (a director's choice, agreed for a lights-out beat). **Scope.** any piece.

## Delivery specs

### Deliverables
`id: sound.deliverables` · principle 6

- **Rule.** Ask for: WAV, 48 kHz / 24-bit, exactly the picture length, starting on frame one; a full mix plus stems (VO,
music, effects) and an M&E (music and effects without VO) for language versions; a preview of the picture with the mix;
and the list of every music and effect source with its licence.
- **Why.** Stems and an M&E make later versions without going back to the engineer; exact length drops straight into the
edit.
- **Basis.** technical fact (standard post deliverables). **Scope.** any finished soundtrack.

### Loudness for where it plays
`id: sound.loudness` · principle 2

- **Rule.** For social, aim for about −14 LUFS integrated and no more than −1 dBTP true peak, and check the mix on a phone
speaker in mono. Ask the engineer to report what they measured.
- **Why.** Platforms normalise loudness, so a louder master is turned down and only loses dynamics. Most viewers hear a
phone.
- **Basis.** technical fact (common social and streaming targets, 2026; platforms vary). **Scope.** social and web video.
- **Unless.** Broadcast or cinema delivery, which has its own specs.

### Fade every edit
`id: sound.fade-edits` · principle 4

- **Rule.** Every cut in audio gets its own short fade, including cuts inside a repeated sequence. A fade around the whole
group does not fix the cuts inside it.
- **Why.** A cut that lands away from zero makes a click.
- **Basis.** technical fact. **Scope.** any audio edit.

## What measurement can't tell you

### Meters prove the export, not the sound
`id: sound.meters-limit` · principles 2, 7

- **Rule.** Measure what measurement can prove: format, length, sync, peaks, loudness, clipping, the words in the takes.
Judge by ear whether a sound convinces, a balance works or a music edit lands: a person, at a fixed comfortable level, on
headphones and a small speaker, comparing level-matched versions. Every audio report says which checks were measured and
which were heard. An AI agent can cut, place, transcribe and measure; it can't audition.
- **Why.** Equal integrated loudness isn't equal loudness at every moment, and correct placement isn't a good sound.
Confident "mix complete" notes over unheard audio cost one production several rounds.
- **Basis.** principle; measured (that production's own audit). **Scope.** any audio check, especially by agents.
