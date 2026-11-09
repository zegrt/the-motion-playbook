# Audio and encoding tools

How-to behind `craft/sound-and-vo.md` and the delivery checks. Dated, with versions: check them before trusting a command
on a newer build.

## ElevenLabs (v4 model, November 2026)

- No reliable speed slider on v4. Set pace in the text: audio tags such as `[brisk]` or `[rushed]`, punctuation, and
  `[pause]` only where a pause is wanted; tighten remaining gaps in the edit. Tag sets change between models; check the
  current docs.
- Pronunciation: IPA between slashes (for example `/ˈmætɪks/` for a brand name) or a phonetic respelling. Confirm by
  transcription and by ear.
- Generate the whole script in one generation with clear pauses between lines, then cut it into takes
  ([sound.ai-one-take](../craft/sound-and-vo.md)).
- Choose WAV/PCM output when the plan allows; the default download can be MP3 (44.1 kHz, 128 kbps mono). The download name
  records the voice, model and settings: keep the original file as the record.

## ffmpeg (9.0.2, Homebrew, macOS, November 2026)

- Find the gaps between lines: `ffmpeg -i vo.mp3 -af silencedetect=noise=-45dB:d=0.3 -f null -` (prints `silence_start`
  and `silence_end`). These are starting values: check the number of segments against the script, and cut a little inside
  each silence so breaths and tails survive.
- Cut and convert a take: `ffmpeg -i in.mp3 -ss A -to B -ar 48000 -ac 1 -c:a pcm_s24le 01_first-words.wav`. This changes
  the container only; MP3 quality stays MP3 quality.
- Loudness and true peak: `ffmpeg -nostats -i take.wav -af ebur128=peak=true -f null -` (summary shows `I:` in LUFS and
  `Peak:` in dBTP). For JSON: `-af loudnorm=print_format=json` (measures only, unless you apply it).
- Picture for a sound engineer: ProRes Proxy is `-c:v prores_ks -profile:v 0`; add `-timecode 00:00:00:00` so the timecode
  track starts at zero (ffprobe then shows `tag:timecode=00:00:00:00`).
- Check picture files match: `ffprobe -v error -show_entries
  stream=codec_name,profile,r_frame_rate,nb_frames:stream_tags=timecode -of compact=p=0 file`.
- Bit-exact comparison of two renders, frame by frame: `ffmpeg -i a.mov -map 0:v -f framemd5 -` on each, then diff.

### `No such filter: 'drawtext'`
`id: ffmpeg.drawtext`
- **Symptom.** Burning in timecode fails with `No such filter: 'drawtext'`.
- **Cause.** The Homebrew build has no libfreetype.
- **Fix.** Render a per-frame timecode strip as PNGs (Python with Pillow) and `overlay` it, or install a build with
  freetype.
- **Seen.** ffmpeg 9.0.2, November 2026.

### `-vsync` is gone
`id: ffmpeg.vsync`
- **Symptom.** `Unrecognized option 'vsync'`.
- **Fix.** Use `-fps_mode passthrough`. To grab frame ranges reliably, seek with `-ss` before the input and take `-frames:v`.
- **Seen.** ffmpeg 9.0.2, November 2026.

### A VO won't pad to a fixed length
`id: ffmpeg.pad-bed`
- **Symptom.** `apad` with `whole_dur` or `pad_dur` didn't pad the VO to length.
- **Cause.** Unknown; it may have been the pipeline around it rather than `apad`.
- **Fix.** What worked: mix the VO over a fixed-length `anullsrc` bed with `amix duration=first`.
- **Seen.** November 2026, version not recorded.

### `-shortest` drops video frames
`id: ffmpeg.shortest`
- **Symptom.** The muxed file is a few frames short.
- **Fix.** With AAC audio, `-shortest` dropped 3 video frames; mux without it.
- **Seen.** November 2026, version not recorded.

## whisper.cpp (`whisper-cli`, Homebrew, November 2026)

- Word timings: `whisper-cli -m ggml-model.bin -f take16k.wav -ml 1 -sow` (one word per segment). Feed it 16 kHz mono
  16-bit WAV: `ffmpeg -i take.wav -ar 16000 -ac 1 -c:a pcm_s16le take16k.wav`.
- Artefacts seen: a 30 ms "And" at the start of a tightly cut take vanished when silence was padded before it; a trial cut
  lost the first syllable of a word; a brand name came back misspelled. Re-run on a padded copy and on the source before
  re-editing.
- Word start times are approximate (tens of milliseconds). For a frame-exact sync, confirm the onset on the waveform.

## reportlab (4.5.1, Python, November 2026): PDF briefs and one-page documents

- The built-in fonts are Latin-1 only: signs outside it (the rupee sign, for one) render as boxes. Register a TTF
  (`pdfmetrics.registerFont(TTFont(...))`) and map bold and italic with `addMapping` so `<b>` works in Paragraphs.
- Use static font instances. From a variable font, cut them with fontTools (`instantiateVariableFont`) and give each a
  unique internal name, or the PDF shows one weight for all of them.
- `SimpleDocTemplate` frames pad 6 pt: shrink the margins by that so body text lines up with a canvas-drawn letterhead.
- Long tables: `repeatRows=1` repeats the header on each page; wrap each section in `KeepTogether`.
- Generate timecodes from frame numbers in the script rather than typing them, so a re-cut regenerates every timecode.
- To check pages without poppler on macOS, render thumbnails with PDFKit from JXA (`osascript -l JavaScript`).
