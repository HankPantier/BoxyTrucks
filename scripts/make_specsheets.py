"""Spec Sheet series (Hank approved Nov 11, 2026): a one-image "build sheet" post for a truck, twice a week as a change of pace.

  python3 scripts/make_specsheets.py queue      # (re)build social/specsheets/queue.json + one JSON spec per truck, keeping posted items
  python3 scripts/make_specsheets.py render N   # render the next N queued sheets that don't have an image yet

Every fact comes from site data: data/pages (or the family file's page), data/extra/<family>/<gen>.json.
Photos: that generation's licensed page photos (Hank's own first when there are any). Owner note only from page.owner_notes,
which holds only things Hank has told us. Hand-made specs (like g500.json) are kept as they are.
"""
import json, re, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_tire_shorts import ORDER, TAGS, MAKE, label  # same family order, hashtags and naming as the tire Shorts

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / 'social' / 'specsheets'
QUEUE = DIR / 'queue.json'
MANUAL = {'specsheet-g500': 'g500.json'}  # hand-written specs, never regenerated


def clean(s):
    return re.sub(r'\[\[[^|\]]+\|([^\]]+)\]\]', r'\1', str(s or '')).strip()


def cut(s, n):
    s = clean(s)
    s = re.split(r'(?<=[.!?])\s', s)[0].rstrip('.')
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0].rstrip(',;:') + '…'


def short_engine(e):
    e = clean(e).split(' (')[0]
    return e


def load():
    out = {}
    for fj in sorted((ROOT / 'data').glob('*.json')):
        d = json.loads(fj.read_text())
        if not isinstance(d, dict) or 'family' not in d:
            continue
        fam = d['family']
        for g in fam.get('generations', []):
            if not g.get('has_page'):
                continue
            px = ROOT / 'data' / 'pages' / fam['slug'] / f'{g["slug"]}.json'
            page = json.loads(px.read_text()) if px.exists() else (d.get('page') if (d.get('page') or {}).get('slug') == g['slug'] else None)
            xx = ROOT / 'data' / 'extra' / fam['slug'] / f'{g["slug"]}.json'
            if not page or not xx.exists():
                continue
            out.setdefault(fam['slug'], []).append((fam, g, page, json.loads(xx.read_text())))
    return out


def tagline_for(page):
    parts = []
    for c in page.get('codes') or []:
        for bit in clean(c).upper().split(' · '):
            if len(' · '.join(parts + [bit])) > 46:
                return ' · '.join(parts)
            parts.append(bit)
    return ' · '.join(parts)


def title_for(g, page):
    t = g['name'] if len(g['name']) <= 16 else (page.get('title') or g['name'])
    t = re.sub(r'\s*\(Third [Gg]eneration\)', ' Gen 3', t)
    t = re.sub(r'\s*\(sixth generation\)', ' (6th gen)', t, flags=re.I)
    t = re.sub(r'\s*\((?=[^)]*(\d{4}|[Gg]eneration))[^)]*\)', '', t).strip()
    return t


def subtitle_for(fam, g):
    mk, fn = MAKE.get(fam['slug'], ''), fam.get('name', '')
    if fam['slug'] == 'land-cruiser':
        mk = 'Toyota'
    if fam['slug'] == 'land-rover':
        mk, fn = '', 'Land Rover'
    yrs = re.sub(r'\s*\([^)]*\)', '', str(g.get('years', ''))).split(' · ')[0].strip()
    head = fn if (not mk or fn.lower().startswith(mk.lower()) or mk.lower() in fn.lower()) else f'{mk} {fn}'
    return f'{head} · {yrs}'


def build(fam, g, page, x):
    photos = [p for p in page.get('photos', []) if (ROOT / 'site' / 'img' / fam['slug'] / p['file']).exists()]
    hank = [p for p in photos if 'hank' in (p.get('credit') or '').lower()]
    hero = next((p for p in photos if p['file'] == page.get('hero_photo')), None)
    order = hank + ([hero] if hero and hero not in hank else []) + [p for p in photos if p not in hank and p is not hero]
    if len(order) < 3:
        return None
    eng = page.get('engineering') or []
    if len(eng) < 2:
        return None
    fit = x.get('fitment') or {}
    mt = fit.get('max_tire') or []
    cap = {c['k']: c['v'] for c in x.get('capability') or []}
    tl = x.get('timeline') or []
    buy = next((t for t in tl if t.get('flag') == 'buy' and '–' in str(t.get('year'))), None) or next((t for t in tl if t.get('flag') == 'buy'), None)
    avoid = next((t for t in tl if t.get('flag') == 'avoid'), None)
    checks = [cut(c['head'], 48) for c in (page.get('buying_checks') or [])][:5]
    if not buy or len(checks) < 4:
        return None
    specs = []
    engines = []
    for row in page.get('generations_table') or []:
        e = short_engine(row.get('engine'))
        if e and e not in engines:
            engines.append(e)
    if engines:
        specs.append(['Engine', ' / '.join(engines[:2]) if len(' / '.join(engines[:2])) <= 42 else engines[0]])
    for e in eng[2:]:
        if len(specs) >= 3 or e['k'].lower() in ('engine', 'engines') or any(e['k'].lower() == sp[0].lower() for sp in specs):
            continue
        specs.append([re.sub(r'(?i)\b4wd\b', '4WD', e['k'][:1].upper() + e['k'][1:].lower()), cut(e['v'], 46)])
    if fit.get('stock'):
        st = clean(fit['stock'][0]).split(' on ')[0].split(' (')[0]
        bp = (fit.get('wheel') or {}).get('bolt_pattern', '').split(' (')[0]
        specs.append(['Stock tire', f'{st} · {bp}' if bp and len(st) < 22 else st])
    if mt and str(mt[0].get('lift', '')).lower().startswith('stock'):
        specs.append(['Biggest, no lift', cut(mt[0]['size'], 34)])
    for k, lab in (('Towing', 'Towing'), ('Fuel economy', 'Fuel')):
        if cap.get(k):
            specs.append([lab, cut(cap[k].split(' (')[0], 34)])
    vals = x.get('values') or {}
    drv = next((r for r in vals.get('ranges') or [] if r['cond'].lower().startswith('driver')), None)
    if drv:
        specs.append(['Price today', f'{drv["range"]} for a driver'])
    specs = specs[:8]
    owner, owner_label = None, 'OWNER NOTE'
    notes = page.get('owner_notes') or []
    if notes:
        owner = f'Hank, who owned one: “{cut(notes[0]["text"], 150)}.”'
    elif page.get('verdict'):
        owner, owner_label = cut(page['verdict'], 190) + '.', 'THE SHORT VERSION'
    used = order[:3]
    credits = []
    for p in used:
        c = clean(p.get('credit'))
        if c and c not in credits:
            credits.append(c)
    lab = label(fam, page, g)
    year_word = lambda t: clean(t['year'])
    sid = f'specsheet-{fam["slug"]}-{g["slug"]}'
    link = f'https://boxytrucks.com/models/{fam["slug"]}/{g["slug"]}/'
    spec = {
        'id': sid, 'image': f'social/specsheets/img/{sid}.jpg',
        'title': title_for(g, page),
        'subtitle': subtitle_for(fam, g),
        'tagline': tagline_for(page),
        'hero': f'site/img/{fam["slug"]}/{used[0]["file"]}', 'hero_pos': page.get('hero_focus') or '50% 55%',
        'tiles': [{'photo': f'site/img/{fam["slug"]}/{p["file"]}', 'pos': '50% 55%', 'label': e['k'].upper(), 'text': cut(e['v'], 52)}
                  for p, e in zip(used[1:3], eng[:2])],
        'specs': specs,
        'buy': [year_word(buy), cut(buy['change'], 105)],
        'avoid': [year_word(avoid), cut(avoid['change'], 105)] if avoid else None,
        'checks': checks,
        'owner': owner, 'owner_label': owner_label,
        'credit': 'Photos: ' + ' · '.join(credits),
        'url_label': link.replace('https://', '').rstrip('/'),
    }
    hashtag = TAGS.get(fam['slug'], '#4x4')
    av = f' Skip {spec["avoid"][0]}.' if spec['avoid'] else ''
    social = {
        'ig_caption': f'Spec sheet: {lab}.\n\nThe years to buy ({spec["buy"][0]}),{" the years to skip (" + spec["avoid"][0] + ")," if spec["avoid"] else ""} what to check and what it costs today, on one page. Save it for when you go look at one.\n\n'
                      f'Which would you buy, and why?\n\nFull guide: link in bio.\n\n{spec["credit"]}\n\n{hashtag} #offroad #4x4 #overland',
        'x_text': f'Spec sheet: {lab}. Buy {spec["buy"][0]}.{av} Five things to check before you hand over the money. Save it.',
        'x_reply': f'The full guide, with sources: {link}?utm_source=x&utm_medium=social',
        'pin_title': f'{lab} spec sheet: best years, specs, what to check',
        'pin_description': f'One-page {lab} spec sheet: engine, tires, towing, today\'s prices, the years to buy ({spec["buy"][0]})'
                           + (f' and avoid ({spec["avoid"][0]})' if spec['avoid'] else '') + ', and five things to check before buying.',
        'pin_link': f'{link}?utm_source=pinterest&utm_medium=social',
        'link': link,
    }
    return spec, social


def queue():
    old = {q['id']: q for q in json.loads(QUEUE.read_text())} if QUEUE.exists() else {}
    fams = load()
    rows, n = [], 1
    # G 500 first: Hank's own truck, hand-made sheet
    g5 = json.loads((DIR / 'g500.json').read_text())
    rows.append({'id': g5['id'], 'label': 'Mercedes G 500', 'spec': 'social/specsheets/g500.json', 'image': g5['image'], 'status': 'queued',
                 'ig_caption': "Spec sheet: Mercedes G 500 (2002–2008 US).\n\nThe years to buy (2005–08), the years to skip (2002–04), what to check and what it costs today, on one page. And a note from my own 2007.\n\nWhich would you buy, and why?\n\nFull guide: link in bio.\n\nPhotos: Hank · BoxyTrucks\n\n#gwagon #offroad #4x4 #overland",
                 'x_text': 'Spec sheet: Mercedes G 500. Buy 2005–08. Skip 2002–04. Five things to check before you hand over the money. Save it.',
                 'x_reply': 'The full guide, with sources: https://boxytrucks.com/models/g-class/g500/?utm_source=x&utm_medium=social',
                 'pin_title': 'Mercedes G 500 spec sheet: best years, specs, what to check',
                 'pin_description': 'One-page Mercedes G 500 (W463, 2002–2008 US) spec sheet: engine, tires, towing, today\'s prices, the years to buy (2005–08) and avoid (2002–04), and five things to check before buying.',
                 'pin_link': 'https://boxytrucks.com/models/g-class/g500/?utm_source=pinterest&utm_medium=social',
                 'link': 'https://boxytrucks.com/models/g-class/g500/'})
    lists = {f: list(fams.get(f, [])) for f in ORDER}
    while any(lists.values()):
        for f in ORDER:
            while lists.get(f):
                fam, g, page, x = lists[f].pop(0)
                if fam['slug'] == 'g-class' and g['slug'] == 'g500':
                    continue
                r = build(fam, g, page, x)
                if not r:
                    continue
                spec, social = r
                (DIR / 'specs').mkdir(parents=True, exist_ok=True)
                sp = DIR / 'specs' / f'{spec["id"]}.json'
                sp.write_text(json.dumps(spec, indent=1, ensure_ascii=False))
                rows.append({'id': spec['id'], 'label': label(fam, page, g), 'spec': str(sp.relative_to(ROOT)), 'image': spec['image'], 'status': 'queued', **social})
                break
    for r in rows:
        o = old.get(r['id'])
        if o and o.get('status') in ('posted', 'hold'):
            r.update({k: v for k, v in o.items() if k not in ('spec',)})
    for i, r in enumerate(rows, 1):
        spec_path = ROOT / r['spec']
        s = json.loads(spec_path.read_text())
        s['number'] = f'{i:02d}'
        spec_path.write_text(json.dumps(s, indent=1, ensure_ascii=False) + '\n')
    QUEUE.write_text(json.dumps(rows, indent=1, ensure_ascii=False) + '\n')
    print(f'{len(rows)} spec sheets queued')


def render(n):
    rows = json.loads(QUEUE.read_text())
    done = 0
    for r in rows:
        if r.get('status') in ('posted', 'hold') or (ROOT / r['image']).exists():
            continue
        out = subprocess.run(['node', 'social/specsheets/make_sheet.js', r['spec']], cwd=ROOT, capture_output=True, text=True)
        print(out.stdout.strip() or out.stderr.strip()[-400:])
        done += 1
        if done >= n:
            break


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'queue'
    if cmd == 'queue':
        queue()
    elif cmd == 'render':
        render(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
