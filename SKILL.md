---
name: motion-playbook
description: Motion craft, judgment and technique for any motion work - animation, motion graphics, character animation, product motion, film and ad production, in After Effects, Rive, Premiere, Resolve, Blender, Figma or code. Use before planning, building, reviewing, finishing or delivering a shot or a piece, before giving or answering motion notes, and when a motion tool misbehaves. Holds the core principles, craft rules with ids, dated tool notes, house layers and director profiles.
---

# Motion playbook

Craft, judgment and technique for motion work. This folder is the source: read the files, don't work from memory of them.
Paths below are relative to this folder.

## Every session

At the start of a project, if this folder is a git clone, run `git pull --ff-only` in it first, so you work from the
latest playbook. If the pull fails for any reason, say so with its error, and carry on with what's here.

Use existing project context to resolve routine choices; investigate missing details when they would change the
outcome.

1. Read [CORE.md](CORE.md). One page.
2. Read the profiles in `profiles/`: the taste of whoever directs, and the working style of whoever runs the session. At
   the start of a project, ask who directs it, unless the project already says; don't assume it's the person at the
   keyboard. Someone without a profile gets the house and the core. Where the working-style half is silent, or there's
   no profile, follow the [working agreement](process/working-agreement.md).
3. If the project has a production book, read its front page (`book/BOOK.md`): its decisions and approvals are the
   project's own, and they win (When layers disagree).
   If it has none, start one at the first director decision or the first version of anything (`book.py new`,
   [production book](process/production-book.md)), and say so.
4. If the work is for a company with a folder in `houses/`, read its README, then the house files the stage needs. Only
   when the brief or the project says so: a house never applies by default. If you can't ask, say what you assumed.
5. Route by stage below. Don't load every chapter: the core and all chapters come to about 18,000 tokens. A named section
   means that `## ` heading and its rules; a named rule means that one `### ` card. Neither means the whole file.

A resumed or summarised session is a new session: before the next action, re-read CORE, the profiles and the book's
front page. A summary of the playbook is not the playbook.

## Route by stage

| Stage | Read |
|---|---|
| Plan: brief, concept, beats, boards, styleframes | [story-and-edit](craft/story-and-edit.md) (The whole and its beats, Time on screen; Versions and variants when versions are coming); [look-and-finish](craft/look-and-finish.md) (Building a look; the rule Judge the look at viewing size); [character](craft/character.md) (Before animating) if there's a character; [sound-and-vo](craft/sound-and-vo.md) (Writing and timing VO) if there's VO; [sound-and-vo](craft/sound-and-vo.md) (the rule Plan the music for every version) when versions are coming; [interactive](craft/interactive.md) (the rule Settle the behaviour before building) if an app plays it; [working agreement](process/working-agreement.md) (the rule Plan each shot in one block); [production book](process/production-book.md) when a production starts (a single piece needs only its front page) |
| Build: layout, rigging, animation | [motion-and-timing](craft/motion-and-timing.md); [scenes-and-camera](craft/scenes-and-camera.md) if there's a camera or depth; [character](craft/character.md) if there's a character; [sound-and-vo](craft/sound-and-vo.md) (AI voice, Checking takes) if there's VO; [interactive](craft/interactive.md) if an app plays it; the tool's file in [tools/](tools/); log versions, notes and approvals in the project's book, if it has one ([production book](process/production-book.md)) |
| Review: your own output before showing it, or the director's notes | [verification](process/verification.md); the **Check** lines of the rules behind what was built; `interactive.qc` for interactive pieces; [scenes-and-camera](craft/scenes-and-camera.md) (Check what the camera really sees, Check that motion keeps the meaning); [story-and-edit](craft/story-and-edit.md) (The whole at speed); core principles 2 and 4; the book's open list and current versions, if the project has one |
| Finish: look, grade, glow, grain, sound | [look-and-finish](craft/look-and-finish.md) (Light and value, Colour and reading size, Finishing); [sound-and-vo](craft/sound-and-vo.md) (Handing off to an audio engineer, Sound effects, What measurement can't tell you) |
| Deliver: masters, versions, encodes, audio specs | [look-and-finish](craft/look-and-finish.md) (Output and QC); [story-and-edit](craft/story-and-edit.md) (Versions and variants); [sound-and-vo](craft/sound-and-vo.md) (Music and licences, Delivery specs); [audio-and-encoding](tools/audio-and-encoding.md); [verification](process/verification.md) (Say how far a claim is proven); the project's cut list, if it has a book (`CUT.tsv`; [production book](process/production-book.md), the rule The cut is one record); [interactive](craft/interactive.md) (Identify what is handed over) for interactive assets |

A tool misbehaving: search its file in `tools/` by the symptom before debugging from scratch.

Where no rule covers the work, say so: name what's missing, cite a nearby rule only for the part it supports, and
mark the rest as general judgment, not as the playbook's. The known gaps are listed in the README's
[Coverage](README.md#coverage).

When a rule drives a choice or a review note, cite its id (`motion.overlap`), so the director can check it. Copy the id
from the `id:` line under the rule's heading; never build one from the title.

## When layers disagree

The project's own decisions win (the director's latest approved direction; older records are context), then the
director's taste profile, then the house layer, then the core. Remarks a director made mid-project are evidence, not
rulings: when one matters, present it as an open decision.

## Capturing a lesson

From project work, never edit the playbook's files. When something is learned (a correction the director had to repeat,
a tool quirk, a rule that misfired or was missing), write it as a new file in [inbox/](inbox/README.md), named and
formatted as that README says. If you can't write there, put the proposal at the end of your reply so the director can
carry it. When a repeated correction is one person's taste or way of working rather than craft, propose it as a line for
their profile (`profiles/<name>.md`, or a new one from the template); that person approves their own. Nothing reaches
the playbook until it's approved, as [that README](inbox/README.md#how-a-proposal-becomes-part-of-the-playbook)
describes. At the end of a project, run the wrap in [process/wrap.md](process/wrap.md); if the project has a production
book, `book.py close` gathers its lessons into one inbox file for it. If the person you work with isn't
the playbook's maintainer, their wrap ends with sending their proposals as that README says.
