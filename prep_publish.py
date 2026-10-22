#!/usr/bin/env python3
"""Prepare the artifact entry page and print the files map for publishing."""
import json, re
from pathlib import Path
SITE = Path(__file__).parent / 'site'
idx = (SITE / 'index.html').read_text()
head = re.search(r'<head>(.*?)</head>', idx, re.S).group(1)
body = re.search(r'<body>(.*)</body>', idx, re.S).group(1)
head = re.sub(r'<meta charset="utf-8">\s*', '', head)
head = re.sub(r'<meta name="viewport"[^>]*>\s*', '', head)
(SITE.parent / 'entry.html').write_text(head.strip() + '\n' + body.strip() + '\n')
files = {}
for p in sorted(SITE.rglob('*')):
    if p.is_file() and p.name != '.DS_Store':
        rel = p.relative_to(SITE).as_posix()
        if rel == 'index.html':
            continue
        files[rel] = 'site/' + rel
print(len(files), 'files')
(SITE.parent / 'files.json').write_text(json.dumps(files))
