"""Pinterest pins at scale (Hank, Nov 9, 2026: "yes proceed with 5 per day").

Pinterest is the one big channel where every post is a clickable link, so we pin 5 fresh 2:3 pins a day, each pointing at
the exact page it summarises. Three pin types, all built from the site's own data (never invent a number):
  years    : "<truck> years to avoid", the avoid years and the sweet spot, with the reason sentence  -> /years/
  tires    : "Biggest tire on a stock <truck>", stock size and each lift step                          -> /tires/
  problems : "<truck>: N things to check before you buy", the buying-check headings                    -> /problems/

  python3 social/pins/make_pins.py queue        # (re)build social/pins/queue.json, keeping posted rows
  python3 social/pins/make_pins.py render N     # render the next N unposted pins that have no image yet
"""
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from make_tire_shorts import ORDER, first_sentence, label  # noqa: E402
from make_years_shorts import reason  # noqa: E402

Q = ROOT / 'social' / 'pins' / 'queue.json'
# Same holds as the years Shorts (Nov 8): the avoid/buy flags read as contradictory there; fix the timeline first.
HOLD = {'land-cruiser/prado-120', 'jeep/cherokee-xj'}
OUT = ROOT / 'social' / 'pins' / 'img'


def gens():
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
            if not page:
                continue
            xx = ROOT / 'data' / 'extra' / fam['slug'] / f'{g["slug"]}.json'
            x = json.loads(xx.read_text()) if xx.exists() else {}
            photos = [p for p in page.get('photos', []) if (ROOT / 'site' / 'img' / fam['slug'] / p['file']).exists()]
            hero = next((p for p in photos if p['file'] == page.get('hero_photo')), None) or (photos[0] if photos else None)
            if not hero:
                continue
            yield fam, g, page, x, hero, photos


def credit(p):
    c = p.get('credit') or ''
    return c + (f' / {p["source"]}' if p.get('source') and p['source'].lower() not in c.lower() and p['source'] != 'Wikimedia Commons' else '')


def rows_for(fam, g, page, x, hero, photos):
    lab = label(fam, page, g)
    base = f'models/{fam["slug"]}/{g["slug"]}/'
    out = []
    alt = photos[1] if len(photos) > 1 else hero
    tl = x.get('timeline') or []
    avoid = [t for t in tl if t.get('flag') == 'avoid' and reason(t.get('change'))]
    buy = [t for t in tl if t.get('flag') == 'buy' and reason(t.get('change'))]
    if f'{fam["slug"]}/{g["slug"]}' not in HOLD and avoid and buy and (ROOT / 'site' / base / 'years' / 'index.html').exists() and not g['slug'].endswith('-unlimited'):
        out.append({'kind': 'years', 'eyebrow': 'Before you buy', 'title': f'{lab}: years to avoid',
                    'rows': [['avoid', t['year'], reason(t.get('change'), 150)] for t in avoid[:2]] + [['buy', buy[0]['year'], reason(buy[0].get('change'), 150)]],
                    'photo': hero, 'link': base + 'years/',
                    'pin_title': f'{lab} years to avoid, and the best year to buy'[:100],
                    'pin_description': (f'{lab} buying guide: avoid {", ".join(t["year"] for t in avoid[:2])}. {reason(avoid[0].get("change"), 200)} '
                                        f'The sweet spot is {buy[0]["year"]}. Every model year with the reasons and sources.')[:480]})
    mt = (x.get('fitment') or {}).get('max_tire') or []
    if len(mt) >= 2 and (ROOT / 'site' / base / 'tires' / 'index.html').exists():
        out.append({'kind': 'tires', 'eyebrow': 'Tire fitment', 'title': f'Biggest tire on a stock {lab}',
                    'rows': [['tire', m['lift'], m['size']] for m in mt[:4]], 'photo': alt, 'link': base + 'tires/',
                    'pin_title': f'Biggest tire on a stock {lab} (and with a lift)'[:100],
                    'pin_description': (f'The biggest tire that fits a stock {lab}: {mt[0]["size"]}. ' + '; '.join(f'{m["lift"]}: {m["size"]}' for m in mt[1:4]) +
                                        '. Fitment notes, wheel specs, speedometer error and where to buy.')[:480]})
    checks = page.get('buying_checks') or []
    if len(checks) >= 4 and (ROOT / 'site' / base / 'problems' / 'index.html').exists():
        n = min(len(checks), 6)
        out.append({'kind': 'problems', 'eyebrow': 'Inspection checklist', 'title': f'{lab}: {n} things to check before you buy',
                    'rows': [['check', f'{i + 1:02d}', c['head']] for i, c in enumerate(checks[:n])], 'photo': photos[2] if len(photos) > 2 else hero,
                    'link': base + 'problems/',
                    'pin_title': f'{lab} problems: {n} things to check before you buy'[:100],
                    'pin_description': (f'Buying a used {lab}? Check these first: ' + '; '.join(c['head'] for c in checks[:n]) +
                                        '. What each one means, the repairs and the costs.')[:480]})
    for r in out:
        r['id'] = f'pin-{r["kind"]}-{fam["slug"]}-{g["slug"]}'
        r['fam'] = fam['slug']
        r['credit'] = 'Photo: ' + credit(r['photo'])
        r['photo'] = f'site/img/{fam["slug"]}/{r["photo"]["file"]}'
        r['url_label'] = 'boxytrucks.com/' + r['link'].rstrip('/')
        r['image'] = f'social/pins/img/{r["id"]}.jpg'
        r['pin_link'] = f'https://boxytrucks.com/{r["link"]}?utm_source=pinterest&utm_medium=social&utm_campaign=pin-{r["kind"]}'
    return out


def queue():
    old = {r['id']: r for r in json.loads(Q.read_text())} if Q.exists() else {}
    byfam = {}
    for args in gens():
        for r in rows_for(*args):
            byfam.setdefault(r['fam'], []).append(r)
    # interleave families and kinds so a day's 5 pins are 5 different trucks
    order = [f for f in ORDER if f in byfam] + sorted(f for f in byfam if f not in ORDER)
    for f in byfam:
        byfam[f].sort(key=lambda r: {'years': 0, 'tires': 1, 'problems': 2}[r['kind']])
    rows, i = [], 0
    while any(byfam.values()):
        f = order[i % len(order)]; i += 1
        if byfam.get(f):
            r = byfam[f].pop(0)
            prev = old.get(r['id']) or {}
            r.update({k: prev[k] for k in ('status', 'posted', 'url') if k in prev})
            r.setdefault('status', 'queued')
            rows.append(r)
    rows.sort(key=lambda r: r['status'] != 'posted')
    Q.write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    print(f'{len(rows)} pins queued ({sum(r["status"] == "posted" for r in rows)} posted)')


def render(n):
    OUT.mkdir(parents=True, exist_ok=True)
    todo = [r for r in json.loads(Q.read_text()) if r['status'] != 'posted' and not (ROOT / r['image']).exists()][:n]
    if todo:
        subprocess.run(['node', str(ROOT / 'social' / 'pins' / 'make_pin.js')] + [r['id'] for r in todo], check=True)


if __name__ == '__main__':
    {'queue': queue, 'render': lambda: render(int(sys.argv[2]) if len(sys.argv) > 2 else 5)}[sys.argv[1]]()
