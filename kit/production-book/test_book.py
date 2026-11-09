#!/usr/bin/env python3
"""Tests for book.py, on throwaway copies of example/. Usage: python3 kit/production-book/test_book.py"""
import os, random, shutil, stat, subprocess, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK_PY = os.path.join(HERE, 'book.py')
TODAY = '2026-01-13'


def slurp(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def put(path, text):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def rmtree(p):
    def onerr(f, path, _):
        os.chmod(path, stat.S_IWRITE)
        f(path)
    shutil.rmtree(p, onerror=onerr)


class BookTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.project = os.path.join(self.tmp, 'project')
        shutil.copytree(os.path.join(HERE, 'example'), self.project)
        self.book = os.path.join(self.project, 'book')

    def tearDown(self):
        rmtree(self.tmp)

    def run_book(self, *args, by='tester', ok=True):
        r = subprocess.run([sys.executable, BOOK_PY] + list(args) + ['--by', by], capture_output=True, text=True,
                           cwd=self.project)
        if ok:
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return r.returncode, r.stdout + r.stderr

    def log(self, *args, date='2026-01-13T09:00', ok=True):
        return self.run_book('log', *args, '--book', self.book, '--date', date, ok=ok)

    def check(self):
        return self.run_book('check', '--book', self.book, '--today', TODAY, ok=False)

    def read(self, name):
        return slurp(os.path.join(self.book, name))

    def write_record(self, name, text):
        put(os.path.join(self.book, 'records', name), text)

    def touch(self, rel):
        put(os.path.join(self.project, rel), 'placeholder\n')

    def version(self, unit, step, n, **kw):
        self.touch(f'out/{unit.lower()}_{step}_v{n:03d}.mp4')
        return self.log('version', f'unit={unit}', f'step={step}', 'pass=rough',
                        f'output=out/{unit.lower()}_{step}_v{n:03d}.mp4', 'summary=x', 'checked=x', **kw)

    # --- the example and the pages

    def test_example_passes_check_and_build_is_stable(self):
        rc, out = self.check()
        self.assertEqual(rc, 0, out)
        self.assertIn('0 error(s), 0 warning(s)', out)
        before = {n: self.read(n) for n in ('BOOK.md', 'OPEN.md', 'DECISIONS.md')}
        self.run_book('build', '--book', self.book)
        self.assertEqual(before, {n: self.read(n) for n in before})

    def test_one_write_updates_every_view(self):
        self.version('S03', 'finish', 2)
        self.assertIn('| S03 | finish | s03_finish_v002 | not approved yet | last approved: s03_finish_v001 |',
                      self.read('BOOK.md'))
        self.log('note', 'id=N-003', 'unit=S03', 'state=closed', 'text=Glow matched.')
        self.assertNotIn('N-003', self.read('OPEN.md'))
        self.assertIn('Open items: 0', self.read('BOOK.md'))
        rc, out = self.check()
        self.assertEqual(rc, 0, out)

    def test_a_record_written_by_hand_is_picked_up(self):
        self.write_record('by-hand.txt', 'kind: note\nid: N-050\nunit: S02\npriority: must\n'
                          'text: The lamp flickers on\n  frame 200.\ndate: 2026-01-13T09:00\nby: director\n')
        self.run_book('build', '--book', self.book)
        self.assertIn('N-050', self.read('OPEN.md'))
        self.assertIn('The lamp flickers on frame 200.', self.read('OPEN.md'))
        self.assertIn('Open items: 2', self.read('BOOK.md'))

    # --- the design: no state depends on record order

    def test_state_is_the_same_whatever_the_dates_or_file_names(self):
        self.version('S02', 'anim', 2, date='2026-01-13T09:00')
        self.version('S02', 'anim', 3, date='2026-01-10T09:00')  # an earlier date than v002
        self.log('approval', 'version=s02_anim_v002', 'medium=call', 'quote=That one.', 'by=director',
                 date='2026-01-14T09:00')
        self.log('note', 'id=N-002', 'unit=S01', 'state=closed', 'text=Done.', date='2026-01-01T09:00')
        pages = {n: self.read(n) for n in ('BOOK.md', 'OPEN.md')}
        self.assertIn('| S02 | anim | s02_anim_v003 | not approved yet | last approved: s02_anim_v002 |',
                      pages['BOOK.md'])
        rdir = os.path.join(self.book, 'records')
        names = sorted(os.listdir(rdir))
        shuffled = names[:]
        random.Random(7).shuffle(shuffled)
        for old in names:
            os.rename(os.path.join(rdir, old), os.path.join(rdir, 'tmp-' + old))
        for old, new in zip(names, shuffled):
            os.rename(os.path.join(rdir, 'tmp-' + old), os.path.join(rdir, 'z-' + new))
        self.run_book('build', '--book', self.book)
        self.assertEqual(pages, {n: self.read(n) for n in pages})

    # --- versions and approvals

    def test_the_current_version_is_the_highest_number(self):
        for n in (3, 4, 5):  # review 8, finding 1: three versions logged in one minute
            self.version('S01', 'anim', n)
        self.assertIn('| S01 | anim | s01_anim_v005 | not approved yet |', self.read('BOOK.md'))

    def test_a_hand_written_version_and_a_logged_one_in_one_minute(self):  # review 9, finding 2
        self.touch('out/s02_anim_v002.mp4')
        self.write_record('hand.txt', 'kind: version\nid: s02_anim_v002\nunit: S02\nstep: anim\npass: rough\n'
                          'output: out/s02_anim_v002.mp4\nsummary: by hand\nchecked: x\ndate: 2026-01-13T09:00\n')
        self.version('S02', 'anim', 3)
        self.assertIn('| S02 | anim | s02_anim_v003 |', self.read('BOOK.md'))
        rc, out = self.check()
        self.assertEqual(rc, 0, out)

    def test_an_approval_approves_exactly_the_version_it_names(self):  # review 8, finding 4
        self.version('S02', 'anim', 2)
        self.assertIn('| S02 | anim | s02_anim_v002 | not approved yet | last approved: s02_anim_v001 |',
                      self.read('BOOK.md'))
        self.log('approval', 'version=s02_anim_v002', 'medium=call', 'quote=Fine.', 'by=director')
        self.assertIn('| S02 | anim | s02_anim_v002 | approved (rough) | director, 2026-01-13: "Fine." |',
                      self.read('BOOK.md'))

    def test_approval_and_decision_need_the_directors_words(self):
        rc, out = self.log('approval', 'version=s01_anim_v002', 'medium=call', ok=False)
        self.assertEqual(rc, 1)
        self.assertIn("director's words", out)
        rc, out = self.log('decision', 'scope=film', ok=False)
        self.assertEqual(rc, 1)
        self.assertIn('recommendation is a note', out)

    def test_the_director_is_named_never_whoever_logs_it(self):  # blind review, finding 1
        records = os.path.join(self.book, 'records')
        before = sorted(os.listdir(records))
        for kind, fields in (('approval', ('version=s01_anim_v002', 'quote=ok', 'medium=chat')),
                             ('decision', ('scope=film', 'words=Use the blue'))):
            with self.subTest(kind):
                rc, out = self.log(kind, *fields, ok=False)  # run as "tester", with no by=
                self.assertEqual(rc, 1, out)
                self.assertIn('needs by', out)
                self.assertEqual(sorted(os.listdir(records)), before)
        self.log('approval', 'version=s01_anim_v002', 'quote=ok', 'medium=chat', 'by=director')
        self.assertIn('director, 2026-01-13: "ok"', self.read('BOOK.md'))
        self.assertNotIn('tester', self.read('BOOK.md'))

    def test_an_approval_needs_its_medium_and_date(self):  # review 9, finding 5
        self.write_record('bare.txt', 'kind: approval\nversion: s01_anim_v002\nby: director\nquote: Approved\n')
        rc, out = self.check()
        self.assertEqual(rc, 1)
        self.assertIn('an approval needs medium, date', out)
        rc, out = self.log('approval', 'version=s01_anim_v002', 'quote=Yes', 'by=director', ok=False)
        self.assertIn('needs medium', out)

    def test_a_version_needs_an_id(self):  # review 8, finding 8
        self.touch('out/s02_anim_v009.mp4')
        self.write_record('noid.txt', 'kind: version\nunit: S02\nstep: anim\npass: rough\n'
                          'output: out/s02_anim_v009.mp4\nsummary: by hand\nchecked: x\ndate: 2026-01-13T09:00\n')
        rc, out = self.check()
        self.assertEqual(rc, 1)
        self.assertIn('a version needs id', out)

    def test_a_unit_id_is_used_once(self):  # review 10: two records for one unit made the record order decide
        rc, out = self.log('unit', 'id=S01', 'title=Replacement', 'steps=finish', ok=False)
        self.assertEqual(rc, 1)
        self.assertIn('unit id S01 is used twice', out)
        self.assertNotIn('Replacement', ''.join(slurp(os.path.join(self.book, 'records', f))
                                                for f in os.listdir(os.path.join(self.book, 'records'))))
        self.write_record('dup.txt', 'kind: unit\nid: S01\ntitle: Replacement\nsteps: finish\ndate: 2026-01-13T09:00\n')
        rc, out = self.check()
        self.assertEqual(rc, 1, out)
        self.assertIn('records/dup.txt: unit id S01 is used twice (also in records/unit-S01.txt)', out)
        self.assertIn('records/unit-S01.txt: unit id S01 is used twice (also in records/dup.txt)', out)
        target = os.path.join(self.tmp, 'fresh', 'book')
        rc, out = self.run_book('new', target, '--title', 'T', '--units', 'S01 One', 'S01 Two', ok=False)
        self.assertEqual(rc, 1)
        self.assertIn('unit id S01 is given twice', out)
        self.assertFalse(os.path.exists(target))

    def test_check_errors(self):
        cases = [
            ('reuse.txt', 'kind: version\nid: s01_anim_v002\nunit: S01\nstep: anim\npass: rough\n'
                          'output: out/s01_anim_v002_half.mp4\nsummary: again\nchecked: x\ndate: 2026-01-13T09:00\n',
             'used twice'),
            ('ghost.txt', 'kind: approval\nversion: s09_anim_v001\nby: director\nquote: yes\nmedium: call\n'
                          'date: 2026-01-13T09:00\n', 'no version record'),
            ('missing.txt', 'kind: version\nid: s02_anim_v002\nunit: S02\nstep: anim\npass: rough\n'
                            'output: out/nowhere.mp4\nsummary: lost\nchecked: x\ndate: 2026-01-13T09:00\n',
             'has no output'),
            ('kind.txt', 'kind: memo\ntext: hi\n', 'is not one of'),
        ]
        for name, text, expect in cases:
            with self.subTest(name):
                self.write_record(name, text)
                rc, out = self.check()
                self.assertEqual(rc, 1, out)
                self.assertIn(expect, out)
                os.remove(os.path.join(self.book, 'records', name))

    def test_warnings(self):
        self.touch('out/s01_finish_v002.mov')
        self.log('version', 'unit=S01', 'step=finish', 'pass=final', 'output=out/s01_finish_v002.mov',
                 'summary=Regrade')
        self.log('note', 'unit=S01', 'text=An old worry', date='2025-12-01T09:00')
        rc, out = self.check()
        self.assertEqual(rc, 0, out)
        self.assertIn('says nothing in "checked"', out)
        self.assertIn('has been open 43 days', out)

    # --- notes

    def test_notes_logged_in_one_minute_all_reach_the_open_list(self):  # the PM's check, finding 1
        texts = [('S01', 'must', 'The hook needs a beat more'), ('S02', 'should', 'note A'),
                 ('S02', 'should', 'note B')]
        for unit, prio, text in texts:
            self.log('note', f'unit={unit}', f'priority={prio}', f'text={text}')
        open_page = self.read('OPEN.md')
        for (_, _, text), nid in zip(texts, ('N-004', 'N-005', 'N-006')):
            self.assertIn(text, open_page)
            self.assertIn(nid, open_page)
        self.assertIn('Open items: 4', self.read('BOOK.md'))

    def test_a_note_opened_and_closed_in_one_minute_is_closed(self):  # review 8, finding 1
        self.log('note', 'unit=S02', 'text=quick one')
        self.log('note', 'id=N-004', 'unit=S02', 'state=closed', 'text=done')
        self.assertNotIn('N-004', self.read('OPEN.md'))

    def test_closed_stays_closed(self):
        rc, out = self.log('note', 'id=N-001', 'unit=S01', 'text=again', ok=False)
        self.assertEqual(rc, 1)
        self.assertIn('closed stays closed', out)
        self.write_record('reopen.txt', 'kind: note\nid: N-001\nunit: S01\ntext: again\n'
                          'date: 2026-01-13T09:00\nby: x\n')
        rc, out = self.check()
        self.assertEqual(rc, 1)
        self.assertIn('note id N-001 is already closed, and closed stays closed', out)

    def test_note_id_problems_are_reported(self):
        for name, text in (('a.txt', 'note A'), ('b.txt', 'note B')):
            self.write_record(name, f'kind: note\nid: N-050\nunit: S02\ntext: {text}\ndate: 2026-01-13T09:00\nby: x\n')
        rc, out = self.check()
        self.assertEqual(rc, 1, out)
        self.assertIn('note id N-050 is already used', out)
        for name in ('a.txt', 'b.txt'):
            os.remove(os.path.join(self.book, 'records', name))
        self.write_record('ghost.txt', 'kind: note\nid: N-099\nunit: S01\nstate: closed\ntext: done\n'
                          'date: 2026-01-13T09:00\nby: x\n')
        rc, out = self.check()
        self.assertIn('closed here but never opened', out)

    def test_a_note_closes_with_only_its_id_and_state(self):  # blind review, finding 4
        self.log('note', 'unit=S02', 'text=quick one')
        rc, out = self.log('note', 'id=N-004', 'state=closed')
        self.assertIn('Logged note N-004', out)
        self.assertNotIn('N-004', self.read('OPEN.md'))
        rc, out = self.check()
        self.assertEqual(rc, 0, out)

    def test_a_note_names_a_version_of_its_own_unit(self):  # blind review, finding 4
        rc, out = self.log('note', 'unit=S01', 'version=s01_anim_v077', 'text=x', ok=False)
        self.assertEqual(rc, 1)
        self.assertIn('note names version s01_anim_v077, which no version record has', out)
        rc, out = self.log('note', 'unit=S02', 'version=s01_anim_v001', 'text=x', ok=False)
        self.assertEqual(rc, 1)
        self.assertIn("version s01_anim_v001 is S01's, not S02's", out)
        self.write_record('stray.txt', 'kind: note\nid: N-050\nunit: S02\nversion: s01_anim_v001\ntext: x\n'
                          'date: 2026-01-13T09:00\nby: x\n')
        rc, out = self.check()
        self.assertEqual(rc, 1, out)
        self.assertIn("records/stray.txt: version s01_anim_v001 is S01's", out)

    def test_a_unit_with_no_versions_is_on_the_front_page(self):  # blind review, finding 3
        self.log('unit', 'id=S04', 'title=Outro')
        self.assertIn('| S04 |  |  | no versions yet |  |', self.read('BOOK.md'))

    def test_a_parked_note_is_listed_as_parked(self):
        self.log('note', 'id=N-003', 'unit=S03', 'state=parked', 'text=v1.1 if asked')
        self.assertIn('Parked:\n- N-003', self.read('OPEN.md'))
        self.assertIn('Open items: 0', self.read('BOOK.md'))

    def test_cross_unit_note_lands_with_the_owner(self):
        self.log('note', 'unit=S01', 'type=cross-unit', 'text=S01 ends brighter than S02 starts')
        self.assertIn('## S01 Hook', self.read('OPEN.md'))
        self.assertIn('[cross-unit]', self.read('OPEN.md'))

    # --- messages and help (the PM's check, findings 2 and 3)

    def test_the_log_message_says_what_was_logged(self):
        rc, out = self.log('approval', 'version=s01_anim_v002', 'quote=Still good.', 'medium=call', 'by=director')
        self.assertIn('Logged approval s01_anim_v002 in records/', out)

    def test_log_help_names_the_kinds(self):
        rc, out = self.run_book('log', '--help')
        for kind in ('unit', 'version', 'approval', 'note', 'decision'):
            self.assertIn(kind, out)
        self.assertIn('README.md', out)

    # --- new and close

    def test_new_makes_a_book_and_never_overwrites(self):
        target = os.path.join(self.tmp, 'fresh', 'book')
        self.run_book('new', target, '--title', 'Test', '--units', 'S01 One', 'S02 Two', '--date', '2026-01-01T09:00')
        self.assertTrue(os.path.exists(os.path.join(target, 'units', 'S02.md')))
        rc, out = self.run_book('check', '--book', target, '--today', TODAY, ok=False)
        self.assertEqual(rc, 0, out)
        rc, out = self.run_book('new', target, '--title', 'Again', ok=False)
        self.assertEqual(rc, 1)
        self.assertIn('never overwrites', out)

    def test_close_writes_one_inbox_proposal(self):
        inbox = os.path.join(self.tmp, 'inbox')
        self.run_book('close', '--book', self.book, '--inbox', inbox, '--today', TODAY)
        files = os.listdir(inbox)
        self.assertEqual(len(files), 1)
        text = slurp(os.path.join(inbox, files[0]))
        self.assertIn('**From:** tester', text)
        self.assertNotIn('Vertical, fifteen seconds', text)  # blind review, finding 3: decisions stay in the project
        self.assertIn('check a hook muted', text)
        rc, out = self.run_book('close', '--book', self.book, '--inbox', inbox, '--today', TODAY, ok=False)
        self.assertEqual(rc, 1)


if __name__ == '__main__':
    unittest.main(verbosity=1)
