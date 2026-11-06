"""Second daily Short (Hank, Nov 5, 2026): "Biggest tire on a stock <truck>" series, generated from site data.

  python3 scripts/make_tire_shorts.py queue        # (re)build social/shorts.json + reel specs, keeping posted items
  python3 scripts/make_tire_shorts.py render N     # render the next N queued videos that don't exist yet

Each Short: hook -> stock-height size -> one or two lifted sizes -> CTA to the truck's /tires/ page
(which carries the Tire Rack, Mavis and Amazon size links). Facts come only from data/extra/*/<gen>.json
fitment.max_tire; photos only from that generation's licensed page photos.
"""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUEUE = ROOT / 'social' / 'shorts.json'
ORDER = ['land-cruiser', '4runner', 'jeep', 'bronco', 'g-class', 'land-rover', 'lexus', 'range-rover', 'grenadier',
         'nissan-patrol', 'scout', 'chevrolet', 'suzuki', 'hummer', 'ramcharger', 'pajero', 'delica', 'trooper',
         'pinzgauer', 'unimog', 'niva']
TAGS = {'land-cruiser': '#landcruiser', '4runner': '#4runner', 'jeep': '#jeep', 'bronco': '#bronco', 'g-class': '#gwagon',
        'land-rover': '#landrover', 'lexus': '#lexus', 'range-rover': '#rangerover', 'grenadier': '#ineosgrenadier',
        'nissan-patrol': '#nissanpatrol', 'scout': '#internationalscout', 'chevrolet': '#k5blazer', 'suzuki': '#suzuki',
        'hummer': '#hummer', 'ramcharger': '#ramcharger', 'pajero': '#pajero', 'delica': '#delica', 'trooper': '#isuzutrooper'}


def first_sentence(s, n=120):
    s = re.sub(r'\[\[[^|\]]+\|([^\]]+)\]\]', r'\1', str(s or '')).strip()
    s = re.split(r'(?<=[.!?])\s', s)[0]
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + '…'


MAKE = {'land-cruiser': 'Land Cruiser', '4runner': 'Toyota', 'jeep': 'Jeep', 'bronco': 'Ford', 'g-class': 'Mercedes',
        'land-rover': 'Land Rover', 'lexus': 'Lexus', 'range-rover': 'Range Rover', 'grenadier': 'Ineos', 'nissan-patrol': 'Nissan',
        'scout': 'International', 'chevrolet': 'Chevy', 'suzuki': 'Suzuki', 'hummer': 'Hummer', 'ramcharger': 'Dodge',
        'pajero': 'Mitsubishi', 'delica': 'Mitsubishi', 'trooper': 'Isuzu', 'pinzgauer': 'Steyr-Puch', 'unimog': 'Mercedes', 'niva': 'Lada'}


def label(fam, page, g):
    t = page.get('title') or g['name']
    mk = MAKE.get(fam['slug'], '')
    known = [mk, 'Toyota', 'Ford', 'Chevrolet', 'Mercedes', 'Land Rover', 'Range Rover', 'Lexus', 'Jeep', 'Nissan', 'International', 'Ineos', 'Land Cruiser']
    return t if any(k and k.lower() in t.lower() for k in known) else f'{mk} {t}'.strip()


def items():
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
            mt = (json.loads(xx.read_text()).get('fitment') or {}).get('max_tire') or []
            if not (len(mt) >= 2 and str(mt[0].get('lift', '')).lower().startswith('stock')):
                continue
            photos = [p for p in page.get('photos', []) if (ROOT / 'site' / 'img' / fam['slug'] / p['file']).exists()]
            hero = next((p for p in photos if p['file'] == page.get('hero_photo')), None)
            photos = ([hero] if hero else []) + [p for p in photos if p is not hero]
            if len(photos) < 2:
                continue
            out.setdefault(fam['slug'], []).append((fam, g, page, mt, photos))
    return out


def spec_for(fam, g, page, mt, photos):
    lab = label(fam, page, g)
    url = f'boxytrucks.com/models/{fam["slug"]}/{g["slug"]}/tires'
    ph = lambda i: f'site/img/{fam["slug"]}/{photos[i % len(photos)]["file"]}'
    focus = page.get('hero_focus') or '50% 55%'
    sc = [{'photo': ph(0), 'pos': focus, 'dur': 2.4, 'eyebrow': 'Biggest tire, no lift', 'title': f'{lab}?', 'zoom': [1.05, 1.14]},
          {'photo': ph(0), 'pos': focus, 'dur': 3.2, 'eyebrow': 'Stock height', 'title': mt[0]['size'], 'body': first_sentence(mt[0].get('note')), 'zoom': [1.14, 1.22]}]
    for i, t in enumerate(mt[1:3], start=1):
        sc.append({'photo': ph(i), 'pos': '50% 55%', 'dur': 3.0, 'eyebrow': f'With a {t["lift"]} lift' if 'lift' not in str(t['lift']).lower() else str(t['lift']), 'title': t['size'], 'body': first_sentence(t.get('note')), 'zoom': [1.05, 1.15]})
    sc.append({'photo': ph(len(sc)), 'pos': '50% 50%', 'dur': 2.6, 'title': 'Every size, every lift.', 'body': url, 'cta': True, 'zoom': [1.04, 1.1]})
    # Hank, Nov 6, 2026: end every Short with a follow ask (works on YouTube, TikTok, IG, X and Pinterest alike).
    sc.append({'photo': ph(0), 'pos': focus, 'dur': 2.0, 'eyebrow': 'Boxy Trucks', 'title': 'Follow for a new truck every day.', 'body': 'Tomorrow: another boxy 4x4.', 'cta': True, 'zoom': [1.1, 1.14]})
    used = []
    for s in sc:
        f = s['photo'].rsplit('/', 1)[1]
        p_ = next((p for p in photos if p['file'] == f), None)
        c = None
        if p_ and p_.get('credit'):
            c = p_['credit'] + (f' / {p_["source"]}' if p_.get('source') and p_['source'].lower() not in p_['credit'].lower() and p_['source'] not in ('Wikimedia Commons',) else '')
        if c and c not in used:
            used.append(c)
    gid = f'tires-{fam["slug"]}-{g["slug"]}'
    spec = {'out': f'social/posts/shorts/{gid}.mp4', 'url': url, 'credit': 'Photos: ' + ' · '.join(used), 'scenes': sc}
    link = f'https://boxytrucks.com/models/{fam["slug"]}/{g["slug"]}/tires/'
    sizes = '; '.join(f'{t["lift"]}: {t["size"]}' for t in mt[:3])
    yt_title = f'Biggest tire on a stock {lab}: {mt[0]["size"]}'[:100]
    yt_desc = (f'The biggest tire that fits a stock {lab}, and what fits with a lift. {sizes}.\n\n'
               f'Every size with fitment notes, wheel specs and where to buy: {link}?utm_source=youtube&utm_medium=social\n\n'
               f'Subscribe for a new boxy truck every day.\n\n{spec["credit"]}')
    tt_desc = f'Biggest tire on a stock {lab}? {mt[0]["size"]}. With a lift: {mt[1]["size"]}. Every size at boxytrucks.com. Follow for a new truck every day '
    return gid, spec, {'id': gid, 'fam': fam['slug'], 'gen': g['slug'], 'label': lab, 'spec': f'social/reels/shorts/{gid}.json',
                       'video': spec['out'], 'link': link, 'yt_title': yt_title, 'yt_description': yt_desc,
                       'tt_description': tt_desc, 'tt_hashtags': [TAGS.get(fam['slug'], '#4x4'), '#offroad', '#tires'],
                       # Hank, Nov 6, 2026: the second daily post goes to every platform, not just YouTube and TikTok.
                       'ig_caption': (f'Biggest tire on a stock {lab}: {mt[0]["size"]}.\n\n' + '\n'.join(f'{t["lift"]}: {t["size"]}' for t in mt[1:3]) +
                                      f'\n\nEvery size with fitment notes and wheel specs: link in bio.\n\nWhat are you running on yours?\n\nFollow for a new truck every day.\n\n{spec["credit"]}\n\n'
                                      + ' '.join([TAGS.get(fam['slug'], '#4x4'), '#offroad', '#tires', '#overland'])),
                       'x_text': (f'Biggest tire on a stock {lab}? {mt[0]["size"]}. With a lift: {mt[1]["size"]}.\n\nEvery size: {link}?utm_source=x&utm_medium=social')[:270],
                       'pin_title': f'Biggest tire on a stock {lab}'[:100],
                       'pin_description': (f'The biggest tire that fits a stock {lab}, and what fits with a lift. {sizes}. Fitment notes, wheel specs and where to buy.')[:480],
                       'pin_link': f'{link}?utm_source=pinterest&utm_medium=social',
                       'status': 'queued'}


def queue():
    old = {q['id']: q for q in json.loads(QUEUE.read_text())} if QUEUE.exists() else {}
    byfam = items()
    (ROOT / 'social' / 'reels' / 'shorts').mkdir(parents=True, exist_ok=True)
    order = [f for f in ORDER if f in byfam] + sorted(f for f in byfam if f not in ORDER)
    rows, i = [], 0
    while any(byfam[f] for f in order):  # round-robin across families so the feed varies day to day
        f = order[i % len(order)]; i += 1
        if not byfam[f]:
            continue
        gid, spec, row = spec_for(*byfam[f].pop(0))
        (ROOT / row['spec']).write_text(json.dumps(spec, indent=1, ensure_ascii=False))
        prev = old.get(gid)
        rows.append({**row, **{k: v for k, v in (prev or {}).items() if k.startswith(('yt_', 'tt_status', 'tt_url', 'ig_status', 'ig_url', 'x_status', 'x_url', 'pin_status', 'pin_url', 'posted', 'status')) and k not in ('yt_title', 'yt_description') and v}})
    QUEUE.write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    print(f'{len(rows)} shorts queued ({sum(r["status"] == "posted" for r in rows)} posted)')


def render(n):
    rows = json.loads(QUEUE.read_text())
    todo = [r for r in rows if r['status'] != 'posted' and not (ROOT / r['video']).exists()][:n]
    (ROOT / 'social' / 'posts' / 'shorts').mkdir(parents=True, exist_ok=True)
    for r in todo:
        subprocess.run(['node', str(ROOT / 'social' / 'reels' / 'make_reel.js'), str(ROOT / r['spec'])], check=True)
        mb = (ROOT / r['video']).stat().st_size / 1e6
        print(f'{r["id"]}: {mb:.1f} MB' + ('  (OVER 10 MB: TikTok web upload will refuse)' if mb > 10 else ''))


if __name__ == '__main__':
    {'queue': lambda: queue(), 'render': lambda: render(int(sys.argv[2]) if len(sys.argv) > 2 else 7)}[sys.argv[1]]()
