#!/usr/bin/env python3
"""Playbook lint: the cheap checks that stop it rotting. No dependencies. Exit 1 on any error.

Checks the universal layer (CORE.md, README.md, SKILL.md, craft/, tools/, process/, and every file in kit/: code,
templates and records too, since the kit ships them):
  - no private names, paths, emails or prices (the house layer, profiles and archive are exempt). The names are read
    from the repo: profile file names, house folder names and each house's private-names.txt; a multiword name is
    caught across a line break, since Markdown wraps it;
  - no status words in rules ("latest", "currently", "not yet", "TODO", ...): status belongs in a production book;
  - no em dashes (house writing style);
  - every rule has an id, ids are unique, and every rule has Rule, Why and Basis lines;
  - relative links point at files that exist;
  - word budgets (CORE 500, a craft chapter 3,500) so growth forces a merge.
Holding files starting with "_" (drafts waiting to be sorted) are skipped.
Usage: python3 scripts/lint.py
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UNIVERSAL = ['CORE.md', 'README.md', 'SKILL.md', 'craft', 'tools', 'process', 'kit']
DETAILS = re.compile(r'/Users/|@[\w.-]+\.(com|in|io)\b|₹|\bRs ?\d|\bUSD ?\d', re.I)


def private_names():
    """Names that must stay out of the universal layer: every profile's file name (hyphens read as spaces), every
    house's folder name, and the lines of each house's private-names.txt (characters, projects, people without a
    profile). Read from the repo, so adding a profile or a house protects its names without editing this script."""
    names = []
    pdir = os.path.join(ROOT, 'profiles')
    for f in sorted(os.listdir(pdir)) if os.path.isdir(pdir) else []:
        if f.endswith('.md') and not f.startswith('_'):
            names.append(f[:-3].replace('-', ' '))
    hdir = os.path.join(ROOT, 'houses')
    for h in sorted(os.listdir(hdir)) if os.path.isdir(hdir) else []:
        if os.path.isdir(os.path.join(hdir, h)):
            names.append(h.replace('-', ' '))
            p = os.path.join(hdir, h, 'private-names.txt')
            if os.path.exists(p):
                names += [l.strip() for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')]
    return names


def phrase_re(phrase):
    """A name matched word by word, with any whitespace (a space, a wrapped line) between the words."""
    return r'\s+'.join(re.escape(w) for w in phrase.split())


NAMES = private_names()
NAME_RE = re.compile(r'\b(' + '|'.join(phrase_re(n) for n in NAMES) + r')\b', re.I) if NAMES else None
STATUS = re.compile(r'\b(latest (v\d|version is|render|cut)|currently|right now|not yet|still (being|to be|open)|TODO|TBD|for now)\b', re.I)
BUDGET = {'CORE.md': 500}
CHAPTER_BUDGET = 3500


def files():
    for top in UNIVERSAL:
        p = os.path.join(ROOT, top)
        if os.path.isfile(p):
            yield p
        elif os.path.isdir(p):
            for dp, dns, fs in os.walk(p):
                dns[:] = sorted(d for d in dns if d != '__pycache__' and not d.startswith('.'))
                for f in sorted(fs):
                    # kit/ ships code, templates and records, so every file there is checked, not only Markdown
                    if (f.endswith('.md') or top == 'kit') and not f.startswith(('_', '.')):
                        yield os.path.join(dp, f)


def main():
    errors, ids = [], {}
    for path in files():
        rel = os.path.relpath(path, ROOT)
        is_md = path.endswith('.md')
        try:
            text = open(path, encoding='utf-8').read()
        except UnicodeDecodeError:
            errors.append(f'{rel}: not a UTF-8 text file (the kit is plain text)')
            continue
        in_code = False
        for n, line in enumerate(text.splitlines(), 1):
            if line.startswith('```'):
                in_code = not in_code
            if '—' in line:
                errors.append(f'{rel}:{n}: em dash')
            if rel != 'README.md' and not in_code:
                m = DETAILS.search(line)
                if m:
                    errors.append(f'{rel}:{n}: private detail in the universal layer: "{m.group(0)}"')
                m = STATUS.search(line)
                if m and rel.startswith(('craft', 'CORE')):
                    errors.append(f'{rel}:{n}: status word in a rule: "{m.group(0)}" (status belongs in a production book)')
            for target in re.findall(r'\]\(([^)#\s]+)(?:#[^)]*)?\)', line) if is_md else []:
                if not target.startswith(('http', 'mailto:')) and not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(path), target))):
                    errors.append(f'{rel}:{n}: broken link to {target}')
        # private names: over the whole text, so a name wrapped across two lines is still one name
        if rel != 'README.md' and NAME_RE:
            for m in NAME_RE.finditer(text):
                n = text.count('\n', 0, m.start()) + 1
                errors.append(f'{rel}:{n}: private name in the universal layer: "{" ".join(m.group(0).split())}"')
        # rule cards
        for block in re.split(r'\n(?=### )', text)[1:] if is_md else []:
            title = block.splitlines()[0][4:]
            m = re.search(r'`id: ([\w.-]+)`', block)
            if not m:
                if rel.startswith('craft'):
                    errors.append(f'{rel}: rule "{title}" has no id')
                continue
            rid = m.group(1)
            if rid in ids:
                errors.append(f'{rel}: duplicate id {rid} (also in {ids[rid]})')
            ids[rid] = rel
            if rel.startswith('craft'):
                for field in ('Rule', 'Why', 'Basis'):
                    if f'**{field}.**' not in block:
                        errors.append(f'{rel}: rule {rid} is missing its {field} line')
        words = len(re.findall(r'\w+', text))
        limit = BUDGET.get(rel, CHAPTER_BUDGET if rel.startswith('craft') else None)
        if limit and words > limit:
            errors.append(f'{rel}: {words} words, over the {limit} budget: merge before adding')
    for e in errors:
        print(e)
    print(f'{len(errors)} problem(s); {len(ids)} rule ids checked')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
