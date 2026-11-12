"""Third daily Short (optimization plan, Nov 7, 2026, approved by Hank): "Years to avoid: <truck>" series, generated from site data.

  python3 scripts/make_years_shorts.py queue        # (re)build social/shorts-years.json + reel specs, keeping posted items
  python3 scripts/make_years_shorts.py render N     # render the next N queued videos that don't exist yet

Each Short: hook -> the year(s) to avoid and why -> the sweet-spot year(s) and why -> CTA to the truck's /years/ page -> follow card.
Facts come only from data/extra/<family>/<gen>.json timeline entries flagged 'avoid' and 'buy' (the same data as the
site's years pages, each sourced there); photos only from that generation's licensed page photos.
"""
import json, re, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_tire_shorts import ROOT, ORDER, TAGS, first_sentence, label  # noqa: E402

QUEUE = ROOT / 'social' / 'shorts-years.json'
WHY = re.compile(r'fail|crack|problem|gremlin|issue|recall|complain|avoid|stay away|steer clear|skip|reliab|sweet spot|the pick|recommend|rates|to have|desirable|sorted|fixed|resolved|dependable|leak|burns|known for|fewer|most', re.I)


def reason(change, n=110):
    """The sentence of a timeline entry that says WHY (not the spec note that usually comes first). None if there isn't one."""
    txt = re.sub(r'\[\[[^|\]]+\|([^\]]+)\]\]', r'\1', str(change or ''))
    for sent in re.split(r'(?<=[.!?])\s+|;\s+', txt):
        sent = sent.strip().rstrip('.')
        if len(sent) >= 30 and WHY.search(sent):
            return first_sentence(sent + '.', n)
    return None


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
            tl = json.loads(xx.read_text()).get('timeline') or []
            avoid = [t for t in tl if t.get('flag') == 'avoid' and reason(t.get('change'))]
            buy = [t for t in tl if t.get('flag') == 'buy' and reason(t.get('change'))]
            if g['slug'].endswith('-unlimited'):  # same years and reasons as the two-door page; one Short is enough
                continue
            if not (avoid and buy):
                continue
            if not (ROOT / 'site' / 'models' / fam['slug'] / g['slug'] / 'years' / 'index.html').exists():
                continue
            photos = [p for p in page.get('photos', []) if (ROOT / 'site' / 'img' / fam['slug'] / p['file']).exists()]
            hero = next((p for p in photos if p['file'] == page.get('hero_photo')), None)
            photos = ([hero] if hero else []) + [p for p in photos if p is not hero]
            if len(photos) < 2:
                continue
            out.setdefault(fam['slug'], []).append((fam, g, page, avoid, buy, photos))
    return out


def spec_for(fam, g, page, avoid, buy, photos):
    lab = label(fam, page, g)
    url = f'boxytrucks.com/models/{fam["slug"]}/{g["slug"]}/years'
    ph = lambda i: f'site/img/{fam["slug"]}/{photos[i % len(photos)]["file"]}'
    focus = page.get('hero_focus') or '50% 55%'
    sc = [{'photo': ph(0), 'pos': focus, 'dur': 2.0, 'align': 'top', 'hook': True, 'eyebrow': 'Before you buy one', 'title': f'Don\'t buy these {lab} years', 'zoom': [1.0, 1.18]}]
    for i, t in enumerate(avoid[:2], start=1):
        sc.append({'photo': ph(i), 'pos': '50% 55%', 'dur': 3.4, 'eyebrow': 'Avoid', 'title': t['year'], 'body': reason(t.get('change'), 150), 'zoom': [1.05, 1.15]})
    for t in buy[:1]:
        sc.append({'photo': ph(len(sc)), 'pos': '50% 55%', 'dur': 3.4, 'eyebrow': 'The sweet spot', 'title': t['year'], 'body': reason(t.get('change'), 150), 'zoom': [1.05, 1.15]})
    sc.append({'photo': ph(len(sc)), 'pos': '50% 50%', 'dur': 3.0, 'eyebrow': url, 'title': 'Every year, with the reasons.', 'body': 'Follow for a new truck every day.', 'cta': True, 'zoom': [1.04, 1.12]})
    used = []
    for s in sc:
        f = s['photo'].rsplit('/', 1)[1]
        p_ = next((p for p in photos if p['file'] == f), None)
        c = None
        if p_ and p_.get('credit'):
            c = p_['credit'] + (f' / {p_["source"]}' if p_.get('source') and p_['source'].lower() not in p_['credit'].lower() and p_['source'] not in ('Wikimedia Commons',) else '')
        if c and c not in used:
            used.append(c)
    gid = f'years-{fam["slug"]}-{g["slug"]}'
    spec = {'out': f'social/posts/shorts/{gid}.mp4', 'url': url, 'credit': 'Photos: ' + ' · '.join(used), 'scenes': sc}
    link = f'https://boxytrucks.com/models/{fam["slug"]}/{g["slug"]}/years/'
    av = ', '.join(t['year'] for t in avoid[:2])
    by = buy[0]['year']
    tag = TAGS.get(fam['slug'], '#4x4')
    why_av = reason(avoid[0].get('change'), 400)
    why_by = reason(buy[0].get('change'), 400)
    return gid, spec, {
        'id': gid, 'fam': fam['slug'], 'gen': g['slug'], 'label': lab, 'spec': f'social/reels/shorts/{gid}.json', 'video': spec['out'], 'link': link,
        'yt_title': f'{lab} years to avoid ({av}) and the one to buy'[:100],
        'yt_description': (f'Every {lab} year, with the reasons: {link}?utm_source=youtube&utm_medium=social\n\n{lab}: the years to avoid and the sweet spot. Avoid {av}: {why_av} Buy {by}: {why_by}\n\n'
                           f'Every year with the reasons and sources: {link}?utm_source=youtube&utm_medium=social\n\nSubscribe for a new boxy truck every day.\n\n{spec["credit"]}'),
        'tt_description': f'{lab} years to avoid: {av}. The sweet spot: {by}. Every year with the reasons at boxytrucks.com. Follow for a new truck every day ',
        'tt_hashtags': [tag, '#offroad', '#carbuying'],
        'ig_caption': (f'{lab}: the years to avoid, and the one to buy.\n\nAvoid {av}: {why_av}\n\nBuy {by}: {why_by}\n\n'
                       f'Every year with the reasons and a free inspection checklist: link in bio.\n\nWhich year is yours?\n\nFollow for a new truck every day.\n\n{spec["credit"]}\n\n'
                       + ' '.join([tag, '#offroad', '#carbuying', '#overland'])),
        'x_text': (f'{lab} years to avoid: {av}. The sweet spot: {by}.\n\nEvery year, with the reasons: {link}?utm_source=x&utm_medium=social')[:270],
        'pin_title': f'{lab} years to avoid, and the best year to buy'[:100],
        'pin_description': (f'{lab} buying guide: avoid {av} ({why_av}) The sweet spot is {by}. Every model year with the reasons and sources.')[:480],
        'pin_link': f'{link}?utm_source=pinterest&utm_medium=social',
        'status': 'queued'}


def queue():
    old = {q['id']: q for q in json.loads(QUEUE.read_text())} if QUEUE.exists() else {}
    byfam = items()
    (ROOT / 'social' / 'reels' / 'shorts').mkdir(parents=True, exist_ok=True)
    order = [f for f in ORDER if f in byfam] + sorted(f for f in byfam if f not in ORDER)
    rows, i = [], 0
    while any(byfam[f] for f in order):
        f = order[i % len(order)]; i += 1
        if not byfam[f]:
            continue
        gid, spec, row = spec_for(*byfam[f].pop(0))
        (ROOT / row['spec']).write_text(json.dumps(spec, indent=1, ensure_ascii=False))
        prev = old.get(gid)
        rows.append({**row, **{k: v for k, v in (prev or {}).items() if k.startswith(('yt_', 'tt_status', 'tt_url', 'ig_status', 'ig_url', 'x_status', 'x_url', 'pin_status', 'pin_url', 'posted', 'status')) and k not in ('yt_title', 'yt_description') and v}})
    rows.sort(key=lambda r: r.get('status') == 'hold')  # held items go to the back and are never posted
    QUEUE.write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    print(f'{len(rows)} years Shorts queued ({sum(r["status"] == "posted" for r in rows)} posted)')


def render(n):
    rows = json.loads(QUEUE.read_text())
    todo = [r for r in rows if r['status'] not in ('posted', 'hold') and not (ROOT / r['video']).exists()][:n]
    for r in todo:
        subprocess.run(['node', str(ROOT / 'social' / 'reels' / 'make_reel.js'), str(ROOT / r['spec'])], check=True)
        mb = (ROOT / r['video']).stat().st_size / 1e6
        print(f'{r["id"]}: {mb:.1f} MB' + ('  (OVER 10 MB: TikTok web upload will refuse)' if mb > 10 else ''))


if __name__ == '__main__':
    {'queue': lambda: queue(), 'render': lambda: render(int(sys.argv[2]) if len(sys.argv) > 2 else 2)}[sys.argv[1]]()
