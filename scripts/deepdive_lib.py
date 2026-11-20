"""Helpers for the Nov 2026 deep dive: load/save a generation's page data wherever it lives."""
import json, os, re

def _path(g):
    fam, gen = g.split('/')
    p = f'data/pages/{fam}/{gen}.json'
    return (p, None) if os.path.exists(p) else (f'data/{fam}.json', 'page')

def load_page(g):
    p, key = _path(g)
    raw = open(p).read(); d = json.loads(raw)
    return (d[key] if key else d), (p, key, raw, d)

def save_page(handle):
    p, key, raw, d = handle
    ind = 1 if raw.startswith('{\n "') else (2 if raw.startswith('{\n  "') else None)
    open(p, 'w').write(json.dumps(d, indent=ind, ensure_ascii=False) + ('\n' if raw.endswith('\n') else ''))

def load_extra(g):
    p = f'data/extra/{g}.json'; raw = open(p).read()
    return json.loads(raw), (p, raw)

def save_extra(X, h):
    p, raw = h
    ind = 1 if raw.startswith('{\n "') else (2 if raw.startswith('{\n  "') else None)
    open(p, 'w').write(json.dumps(X, indent=ind, ensure_ascii=False) + ('\n' if raw.endswith('\n') else ''))

def repair_slug(title, used):
    t = re.sub(r'\(.*?\)', '', str(title)).lower().replace('&', 'and')
    t = re.sub(r'[^a-z0-9]+', '-', t).strip('-')
    t = '-'.join(t.split('-')[:9]) or 'repair'
    base, n = t, 2
    while t in used:
        t = f'{base}-{n}'; n += 1
    used.add(t); return t

def report(g):
    pg, _ = load_page(g)
    noidx = set(json.load(open('data/repair_noindex.json'))['paths'])
    used = set(); out = [f"TITLE {pg['title']} | {pg.get('eyebrow')}"]
    for r in pg.get('repairs', []):
        s = repair_slug(r['title'], used)
        out.append(('THIN ' if f'{g}/{s}' in noidx else 'ok   ') + f"{s} | fix {len(r.get('fix',''))} | refs {len(r.get('refs',[]) or [])} | {r['title'][:70]}")
    out.append('SERVICE ' + json.dumps([(i['item'], i.get('interval')) for i in (pg.get('baseline_service') or {}).get('items', [])], ensure_ascii=False))
    out.append('GENTAB ' + json.dumps([(r.get('years'), r.get('engine')) for r in pg.get('generations_table', [])], ensure_ascii=False))
    out.append('CHECKS ' + json.dumps([c.get('head') for c in pg.get('buying_checks', []) if isinstance(c, dict)], ensure_ascii=False))
    return '\n'.join(out)

if __name__ == '__main__':
    import sys; print(report(sys.argv[1]))
