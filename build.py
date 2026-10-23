#!/usr/bin/env python3
"""Build the BoxyTrucks static prototype from data/ into site/.

data/<family>.json            family landing + the family's flagship example page
data/pages/<family>/<gen>.json  a full guide for any other generation
data/resources/<family>.json    YouTube / Instagram / forums / other references
"""
import json, re
from pathlib import Path
from markupsafe import Markup, escape
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).parent
DATA = ROOT / 'data'
SITE = ROOT / 'site'

SITE_URL = 'https://boxytrucks.com/'
SUBMIT_EMAIL = 'webhank@gmail.com'
# TODO: Google Analytics — paste the GA4 measurement ID (G-XXXXXXX) here to enable tracking on every page.
GA_MEASUREMENT_ID = 'G-XHC493ES9X'
SITE_NAME = 'BoxyTrucks'
DEFAULT_OG_IMAGE = 'img/home/lc80-georgia.jpg'
SITEMAP = []
# Families are shown everywhere in alphabetical order of the name people use for them.
SHORT_NAME = {'4runner': '4Runner', 'g-class': 'G-Class', 'grenadier': 'Grenadier', 'jeep': 'Jeep',
              'land-cruiser': 'Land Cruiser', 'land-rover': 'Land Rover', 'lexus': 'Lexus LX & GX', 'range-rover': 'Range Rover',
              'nissan-patrol': 'Nissan Patrol', 'scout': 'International Scout'}
FAMILY_ORDER = sorted(SHORT_NAME, key=lambda k: SHORT_NAME[k].lower())
NAV_FAMS = []
NAV = [
    {'key': 'models', 'label': 'MODELS', 'href': 'models/index.html'},
    {'key': 'repairs', 'label': 'REPAIRS', 'href': 'repairs/index.html'},
    {'key': 'mods', 'label': 'MODS & BUILDERS', 'href': 'mods/index.html'},
    {'key': 'resources', 'label': 'RESOURCES', 'href': 'resources/index.html'},
    {'key': 'sale', 'label': 'FOR SALE', 'href': 'for-sale/index.html'},
    {'key': 'submit', 'label': 'SHOW US YOUR RIG', 'href': 'submit/index.html', 'cta': True},
]
LATER = [
    {'name': 'Ford', 'models': ['Bronco 1966–77', 'Bronco (2021+)']},
    {'name': 'Chevrolet / GMC', 'models': ['K5 Blazer', 'Square-body Suburban']},
    {'name': 'Mitsubishi · Isuzu', 'models': ['Pajero Gen 1–2', 'Trooper']},
    {'name': 'Suzuki', 'models': ['Samurai', 'Jimny']},
    {'name': 'Cult & military', 'models': ['Lada Niva', 'UAZ-469', 'Pinzgauer', 'Unimog', 'Volvo C303', 'Hummer H1', 'FJ Cruiser']},
]
BUILDERS = [
    {'name': 'Jackwagon Overlanding', 'what': 'G-Class · overland builds', 'url': 'https://jackwagonoverlanding.com/'},
    {'name': 'Expedition Motor Company', 'what': 'G-Class · W460 / Wolf restorations', 'url': 'https://www.expeditionmotorcompany.com/'},
    {'name': 'ICON 4x4', 'what': 'Land Cruiser · restomods', 'url': 'https://www.icon4x4.com/'},
    {'name': 'The FJ Company', 'what': 'Land Cruiser · restorations', 'url': 'https://www.thefjcompany.com/'},
    {'name': 'Arkonik', 'what': 'Defender · restomods', 'url': 'https://www.arkonik.com/'},
]
STORIES = [
    {'img': 'lc-dune.jpg', 'alt': 'A silver Toyota Land Cruiser climbing a dune at sunset', 'tag': 'LAND CRUISER 200 · EXPEDITION PORTAL', 'title': 'Staples in Tents: the 200 Series built for Mexico, Baja and, next, the Arctic Ocean', 'href': 'https://expeditionportal.com/feature-vehicle-staples-in-tents-200-series-toyota-land-cruiser/'},
    {'img': 'defender-desert.jpg', 'alt': 'The open cockpit of a vintage Land Rover looking out over desert sand', 'tag': 'SERIES IIA · HUCKBERRY JOURNAL', 'title': 'Panama to Mexico in a 1968 Series IIA: Sinuhe Xavier’s rain-soaked scene report', 'href': 'https://huckberry.com/journal/posts/sinuhe-xavier-scene-report-costa-rica'},
    {'img': 'lc-desert.jpg', 'alt': 'Land Cruiser 70 Series troop carriers parked among desert boulders', 'tag': 'LAND CRUISER 70 · OVERLAND JOURNAL', 'title': 'Why the 70 Series is still the overlander’s truck, and how to build one without overdoing it', 'href': 'https://overlandjournal.com/pages/principles-of-overlanding-building-a-70-series-land-cruiser'},
]
HOME_CREDITS = ['Darina Rodionova', 'Hasse Lossius', 'Kristina', 'Caspian Dahlström', 'Charlota Blunarova']
ALIASES = {('land-cruiser', '60-series'): ('land-cruiser', 'fj60')}
LINK_RE = re.compile(r'\[\[([a-z0-9-]+)/([a-z0-9-]+)\|([^\]]+)\]\]')


from urllib.parse import urlparse, quote, parse_qsl, urlencode, urlunparse
import html as _html
AFFILIATES = []


def load_affiliates():
    try:
        return json.loads((DATA / 'affiliates.json').read_text()).get('programs', [])
    except Exception:
        return []


def affiliate_rewrite(html, programs):
    active = [p for p in programs if p.get('template') or p.get('params')]
    if not active:
        return html, False
    hit = False
    def rep(m):
        nonlocal hit
        url = _html.unescape(m.group(2))
        host = urlparse(url).netloc.lower().replace('www.', '')
        for p in active:
            if any(host == d or host.endswith('.' + d) for d in p['domains']):
                hit = True
                if p.get('params'):
                    pu = urlparse(url)
                    q = [(k, v) for k, v in parse_qsl(pu.query, keep_blank_values=True) if k not in p['params']]
                    new = urlunparse(pu._replace(query=urlencode(q + list(p['params'].items()))))
                else:
                    new = p['template'].replace('{url}', quote(url, safe='')).replace('{raw}', url)
                new = new.replace('&', '&amp;')
                tail = m.group(3)
                if 'rel="' in tail:
                    tail = tail.replace('rel="', 'rel="sponsored nofollow ', 1)
                else:
                    tail = ' rel="sponsored nofollow noopener"' + tail
                return f'{m.group(1)}{new}"{tail}'
        return m.group(0)
    out = re.sub(r'(<a\b[^>]*?href=")(https?://[^"]+)"([^>]*>)', rep, html)
    return out, hit


AMZ_SKIP_SUP = ('amazon', 'service centre', 'service center', 'dealer')
AMZ_SKIP_NAME = ('catalog', 'diagram', 'parts list', 'service centre')


def amz_q(pt, vehicle=''):
    """Amazon search query for a listed part, or '' when it isn't a retail product."""
    name = str(pt.get('name') or '')
    sup = str(pt.get('supplier') or '').lower()
    low = name.lower()
    if any(k in sup for k in AMZ_SKIP_SUP) or any(k in low for k in AMZ_SKIP_NAME) or re.search(r'\bsearch\b', low + ' ' + sup):
        return ''
    q = re.split(r';| — listed| - listed|, listed| — confirm|, confirm', name)[0]
    if q.count('(') > q.count(')'):
        q = q[:q.rfind('(')]
    q = re.sub(r'\b(genuine|oem|kit for)\b', '', q, flags=re.I)
    q = q.replace('&', 'and').replace('—', ' ').replace('–', '-')
    q = re.sub(r'\s+', ' ', q).strip(' ,·-')
    has_pn = re.search(r'[A-Za-z]*\d[\w./-]{3,}', q)
    if not has_pn and vehicle and vehicle.lower() not in q.lower():
        q = f'{q} {vehicle}'
    return q


def mlabel(maker, title):
    return title if str(title).lower().startswith(maker.lower()) else f'{maker} {title}'


def jload(p):
    try:
        return json.loads(Path(p).read_text())
    except Exception as e:
        print('  ! could not read', p, e)
        return None


def load():
    fams, flagship, pages, resources = {}, {}, {}, {}
    for slug in FAMILY_ORDER:
        d = jload(DATA / f'{slug}.json')
        if not d:
            continue
        fam = d['family']; fam['slug'] = slug; fam['short'] = SHORT_NAME.get(slug, fam['name'])
        fams[slug] = fam
        pages[slug] = {}
        if d.get('page'):
            flagship[slug] = d['page']['slug']
            pages[slug][d['page']['slug']] = d['page']
        pdir = DATA / 'pages' / slug
        if pdir.exists():
            for f in sorted(pdir.glob('*.json')):
                p = jload(f)
                if p and isinstance(p, dict):
                    p['slug'] = f.stem
                    pages[slug][f.stem] = p
        imgdir = SITE / 'img' / slug
        for p in pages[slug].values():
            if p.get('hero_photo') and not (imgdir / p['hero_photo']).exists():
                p['hero_photo'] = None
            p['photos'] = [ph for ph in p.get('photos', []) if (imgdir / ph.get('file', '')).exists()]
            if not p.get('hero_photo') and p['photos']:
                p['hero_photo'] = p['photos'][0]['file']
            xf = DATA / 'extra' / slug / f"{p['slug']}.json"
            p['x'] = (jload(xf) or {}) if xf.exists() else {}
        apply_social_manual(pages)
        for g in fam['generations']:
            g['has_page'] = g['slug'] in pages[slug]
        missing = [g['slug'] for g in fam['generations'] if not g['has_page']]
        if missing:
            print(f'  · holding back {slug}: no page yet for {", ".join(missing)}')
            del fams[slug], pages[slug]
            flagship.pop(slug, None)
            continue
        if fam.get('hero_photo') and not (imgdir / fam['hero_photo']).exists():
            fam['hero_photo'] = None
        if not fam.get('hero_photo'):
            fam['hero_photo'] = next((p['hero_photo'] for p in pages[slug].values() if p.get('hero_photo')), None)
        r = jload(DATA / 'resources' / f'{slug}.json') if (DATA / 'resources' / f'{slug}.json').exists() else None
        manual = (jload(DATA / 'resources_manual.json') or {}).get(slug, {})
        r = r or {}
        for k, v in manual.items():
            r[k] = list(v) + list(r.get(k, []))
        resources[slug] = merge_resources(slug, fam, pages[slug], r)
    return fams, flagship, pages, resources


def apply_social_manual(pages):
    sm = jload(DATA / 'social_manual.json') or {}
    for key, items in sm.items():
        fs, gs = key.split('/')
        p = pages.get(fs, {}).get(gs)
        if p is None:
            continue
        have = {s.get('url', '').rstrip('/') for s in p.get('social', [])}
        p['social'] = [s for s in items if s['url'].rstrip('/') not in have] + p.get('social', [])


def merge_resources(slug, fam, fpages, r):
    out = {'youtube': [], 'instagram': [], 'forums': [], 'other': []}
    seen = set()

    def add(kind, item):
        key = (item.get('url') or item.get('name', '')).lower().rstrip('/')
        if not key or key in seen:
            return
        seen.add(key); out[kind].append(item)
    for k in out:
        for it in r.get(k, []) or []:
            add(k, it)
    for p in fpages.values():
        for s in p.get('social', []) or []:
            kind = 'youtube' if s.get('kind') == 'YT' else 'instagram'
            add(kind, {'name': s.get('name'), 'url': s.get('url'), 'focus': s.get('focus', '').capitalize()})
    for b in fam.get('forums', []) or []:
        add('forums', b)
    for p in fpages.values():
        for b in p.get('forums', []) or []:
            add('forums', b)
    return out


def gen_ld(fam, g, page):
    from datetime import date
    img = [SITE_URL + f'img/{fam["slug"]}/{ph["file"]}' for ph in page.get('photos', [])][:4]
    strip = lambda t: LINK_RE.sub(lambda m: m.group(3), str(t or ''))
    lead = strip((page.get('story') or [{}])[0].get('paragraphs', [''])[0])
    art = {'@context': 'https://schema.org', '@type': 'Article', 'headline': f'{mlabel(fam["maker"], page["title"])}: history, buying guide, repairs and FAQs',
           'description': strip(page.get('verdict', g['summary'])), 'abstract': lead[:500], 'image': img,
           'datePublished': '2026-10-22', 'dateModified': date.today().isoformat(),
           'author': {'@type': 'Organization', 'name': SITE_NAME, 'url': SITE_URL},
           'publisher': {'@type': 'Organization', 'name': SITE_NAME, 'url': SITE_URL},
           'mainEntityOfPage': SITE_URL + f'models/{fam["slug"]}/{g["slug"]}.html',
           'about': {'@type': 'Car', 'name': mlabel(fam["maker"], page["title"]), 'brand': {'@type': 'Brand', 'name': fam['maker'] if fam['maker'] != 'Lexus' else 'Lexus'}, 'model': page['title'], 'vehicleModelDate': g.get('years', '')}}
    out = [art]
    if page.get('faq'):
        out.append({'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
            {'@type': 'Question', 'name': f['q'], 'acceptedAnswer': {'@type': 'Answer', 'text': strip(f['a'])}} for f in page['faq']]})
    return out


def main():
    fams, flagship, pages, resources = load()
    reading = jload(DATA / 'reading.json') or {}
    global AFFILIATES
    AFFILIATES = load_affiliates()
    suppliers_cfg = jload(DATA / 'suppliers.json') or {}
    fam_list = [fams[s] for s in FAMILY_ORDER if s in fams]
    NAV_FAMS[:] = [{'slug': f['slug'], 'label': SHORT_NAME.get(f['slug'], f['name'])} for f in fam_list]
    env = Environment(loader=FileSystemLoader(str(ROOT / 'templates')), autoescape=True)

    def gen_exists(fs, gs):
        return fs in fams and any(g['slug'] == gs for g in fams[fs]['generations'])

    def render(tpl, out, root, **ctx):
        def lk(text):
            if text is None:
                return ''
            s = str(escape(text))
            def rep(m):
                fs, gs, t = m.group(1), m.group(2), m.group(3)
                fs, gs = ALIASES.get((fs, gs), (fs, gs))
                return f'<a class="inline-link" href="{root}models/{fs}/{gs}.html">{t}</a>' if gen_exists(fs, gs) else t
            return Markup(LINK_RE.sub(rep, s))
        env.filters['lk'] = lk
        env.filters['striplk'] = lambda t: LINK_RE.sub(lambda m: m.group(3), str(t or ''))
        def mark(color, w=34, bg='#0E0F0E'):
            return Markup(f'<svg viewBox="0 0 64 64" width="{w}" aria-hidden="true"><path d="M1 1 H63 V63 H53 A13 13 0 0 0 27 63 H1 Z" fill="none" stroke="{color}" stroke-width="2.6"/><rect x="1" y="33" width="62" height="2.4" fill="{color}"/><circle cx="40" cy="63" r="9.5" fill="{color}"/><circle cx="40" cy="63" r="3.5" fill="{bg}"/></svg>')
        env.globals['affiliates_on'] = any(p.get('template') or p.get('params') for p in AFFILIATES)
        env.globals['mlabel'] = mlabel
        env.globals['amz_q'] = amz_q
        env.globals['amazon_on'] = any(p['name'] == 'Amazon Associates' and p.get('params') for p in AFFILIATES)
        env.globals.update(img=lambda fs, f: f'{root}img/{fs}/{f}',
                           gen_href=lambda fs, gs: (lambda a: f'{root}models/{a[0]}/{a[1]}.html' if gen_exists(*a) else None)(ALIASES.get((fs, gs), (fs, gs))),
                           mark=mark, mark2=lambda: mark('#141513', 18, '#F7F4EE'), nav=NAV, nav_fams=NAV_FAMS)
        path = out.replace('index.html', '') if out.endswith('index.html') else out
        canonical = SITE_URL + path
        og_img = ctx.pop('og_image', None) or DEFAULT_OG_IMAGE
        ld = ctx.pop('jsonld', [])
        crumbs = ctx.pop('crumbs', None)
        if crumbs:
            ld.append({'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
                {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE_URL + u} for i, (n, u) in enumerate(crumbs)]})
        seo = {'canonical': canonical, 'og_image': SITE_URL + og_img, 'og_type': ctx.pop('og_type', 'website'),
               'jsonld': [Markup(json.dumps(x, ensure_ascii=False).replace('</', '<\\/')) for x in ld], 'ga': GA_MEASUREMENT_ID, 'site_name': SITE_NAME}
        if not ctx.get('noindex'):
            SITEMAP.append(canonical)
        html = env.get_template(tpl).render(root=root, families=fams, fam_list=fam_list, flagship=flagship, seo=seo, **ctx)
        html, _ = affiliate_rewrite(html, AFFILIATES)
        out = SITE / out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html)

    def credits_of(plist):
        names = []
        for p in plist:
            for ph in (p or {}).get('photos', []):
                c = ph.get('credit')
                if c and c not in names and 'TO RESEARCH' not in c:
                    names.append(c)
        return ', '.join(names) + (' via Unsplash, Pexels and Wikimedia Commons' if names else '')

    for slug, fam in fams.items():
        fp = pages[slug]
        res = resources[slug]
        main_page = fp.get(flagship.get(slug)) if flagship.get(slug) else None
        render('family.html', f'models/{slug}/index.html', '../../', fam=fam, page=main_page, res=res, og_image=(f'img/{slug}/{fam["hero_photo"]}' if fam.get('hero_photo') else None), crumbs=[('Models', 'models/'), (f'{mlabel(fam["maker"], fam["name"])}', f'models/{slug}/')], jsonld=[{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': f'{mlabel(fam["maker"], fam["name"])}', 'description': fam['verdict'], 'url': SITE_URL + f'models/{slug}/', 'mainEntity': {'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': f'{mlabel(fam["maker"], fam["name"])} {g["name"]}', 'url': SITE_URL + f'models/{slug}/{g["slug"]}.html'} for i, g in enumerate(fam['generations'])]}}], reading=[dict(r, gen=k.split('/')[1]) for k, v in reading.items() if k.startswith(slug + '/') for r in v], active='models',
               title=f'{mlabel(fam["maker"], fam["name"])} — BoxyTrucks', description=fam['verdict'], credits=credits_of(fp.values()))
        for g in fam['generations']:
            page = fp.get(g['slug'])
            if page:
                yt = [s for s in page.get('social', []) if s.get('kind') == 'YT']
                ig = [s for s in page.get('social', []) if s.get('kind') != 'YT']
                x = page.get('x') or {}
                has = lambda *ks: any(page.get(k) for k in ks)
                hx = lambda k: bool(x.get(k)) and (k != 'recalls' or bool(x['recalls'].get('items') or x['recalls'].get('tsbs') or x['recalls'].get('lookup') in ('US', 'UK')))
                toc = [(grp, [(i, l) for i, l, ok in items if ok]) for grp, items in [
                    ('Overview', [('story', 'The story', has('story')), ('timeline', 'Year by year', hx('timeline'))]),
                    ('Specs & capability', [('engineering', 'How it’s built', has('engineering')), ('variants', 'Variants & engines', has('generations_table')),
                                            ('capability', 'Capability numbers', hx('capability')), ('fitment', 'Wheels & tires', hx('fitment')),
                                            ('production', 'Production & editions', hx('production'))]),
                    ('Buying one', [('values', 'What they cost', hx('values')), ('buying', 'What to check', has('buying_checks')),
                                    ('identify', 'Spotting the real thing', hx('identify')), ('recalls', 'Recalls & bulletins', hx('recalls')),
                                    ('import', 'Importing & legality', hx('import')), ('sale', 'For sale now', has('searches'))]),
                    ('Owning one', [('service', 'After you buy it', bool((page.get('baseline_service') or {}).get('items'))), ('repairs', 'Common repairs', has('repairs')),
                                    ('docs', 'Manuals & documentation', hx('docs')), ('faq', 'Questions, answered', has('faq'))]),
                    ('Building one', [('mods', 'Modifications', has('mods')), ('community', 'Clubs & events', hx('community')), ('resources', 'Channels & forums', True)]),
                ]]
                toc = [(grp, items) for grp, items in toc if items]
                hero_alt = next((ph['alt'] for ph in page.get('photos', []) if ph['file'] == page.get('hero_photo')), f'{page.get("title", g["name"])} off road')
                page.setdefault('title', g['name'])
                render('gen_page.html', f'models/{slug}/{g["slug"]}.html', '../../', fam=fam, page=page, toc=toc, hero_alt=hero_alt,
                       og_image=(f'img/{slug}/{page["hero_photo"]}' if page.get('hero_photo') else None), og_type='article', crumbs=[('Models', 'models/'), (f'{mlabel(fam["maker"], fam["name"])}', f'models/{slug}/'), (page['title'], f'models/{slug}/{g["slug"]}.html')], jsonld=gen_ld(fam, g, page),
                       part_search=suppliers_cfg.get(slug, []),
                       yt=yt, ig=ig, res=res, reading=reading.get(f'{slug}/{g["slug"]}', []), active='models', title=f'{mlabel(fam["maker"], page["title"])} — BoxyTrucks',
                       description=page.get('verdict', g['summary']), credits=credits_of([page]))
            else:
                render('gen_stub.html', f'models/{slug}/{g["slug"]}.html', '../../', fam=fam, g=g, crumbs=[('Models', 'models/'), (f'{mlabel(fam["maker"], fam["name"])}', f'models/{slug}/'), (g['name'], f'models/{slug}/{g["slug"]}.html')], reading=reading.get(f'{slug}/{g["slug"]}', []), active='models',
                       title=f'{mlabel(fam["maker"], fam["name"])} {g["name"]} — BoxyTrucks', description=g['summary'], credits='')

    def href(root, slug, gen):
        return f'{root}models/{slug}/{gen}.html'

    garage, faqs = [], []
    for slug in FAMILY_ORDER:
        if slug in flagship:
            p = pages[slug][flagship[slug]]
            label = mlabel(fams[slug]['maker'], p['title']).upper()
            if p.get('repairs'):
                r = dict(p['repairs'][0]); r['model'] = label; r['href'] = href('', slug, p['slug']) + '#repairs'
                garage.append(r)

    covered = ', '.join(SHORT_NAME.get(f['slug'], f['name']) for f in fam_list)
    faqs = [
        {'model': 'ABOUT', 'q': 'What is BoxyTrucks?',
         'a': 'An independent guide to the square-shouldered 4x4s people actually take off-road: where each generation came from, how it\'s built, what to check before you buy, the repairs owners end up doing, and the suppliers, builders, forums and channels worth knowing. Think Wikipedia meets an overland magazine, written by enthusiasts for hands-on owners.',
         'href': 'models/index.html', 'cta': 'BROWSE THE MODELS'},
        {'model': 'COVERAGE', 'q': 'Which trucks do you cover?',
         'a': f'Right now: {covered}, with a full guide for every generation. More are on the list at the bottom of the models page; if yours isn\'t there yet, tell us.',
         'href': 'models/index.html', 'cta': 'SEE EVERY GENERATION'},
        {'model': 'SOURCES', 'q': 'Where does the information come from?',
         'a': 'Owner\'s and factory service manuals, specialist shops, parts suppliers, long-running owner forums and reputable press. Every guide lists its sources at the bottom. Specs vary by year, market and engine, so always confirm fluids, torque figures and part numbers for your VIN before you start.',
         'href': 'about/disclaimer.html', 'cta': 'READ THE DISCLAIMER'},
        {'model': 'PARTS', 'q': 'How do I find the right parts for my truck?',
         'a': 'Every repair and every item in each guide\'s “After you buy it” service list links to the parts you need at suppliers owners trust for that truck, plus an Amazon search. Use the part numbers, check fitment against your VIN, and when in doubt call the supplier.',
         'href': 'repairs/index.html', 'cta': 'BROWSE ALL REPAIRS'},
        {'model': 'BUYING', 'q': 'Can I buy a truck here?',
         'a': 'No, we don\'t sell anything. Each guide links straight to live AutoTempest searches and Bring a Trailer listings for that generation, and the buying checks tell you what to look at before you hand over money.',
         'href': 'for-sale/index.html', 'cta': 'SEE WHAT\'S FOR SALE'},
        {'model': 'YOUR RIG', 'q': 'Can my truck be featured?',
         'a': 'Yes. Send your truck, the build list and your best off-pavement photos through Show Us Your Rig. The good ones become Featured Builds on the home page and their model page, always credited to you.',
         'href': 'submit/index.html', 'cta': 'SHOW US YOUR RIG'},
        {'model': 'MONEY', 'q': 'How does BoxyTrucks pay for itself?',
         'a': 'Some parts and gear links are affiliate links, including Amazon: if you buy through them we may earn a small commission at no cost to you. It never decides which parts or suppliers we recommend, and we\'re not affiliated with any manufacturer.',
         'href': 'about/affiliate-disclosure.html', 'cta': 'AFFILIATE DISCLOSURE'},
        {'model': 'CORRECTIONS', 'q': 'I spotted a mistake. How do I tell you?',
         'a': 'Use the Show Us Your Rig form and put the correction in the story box, with a source if you have one. Owners know these trucks better than anyone, and we fix errors fast.',
         'href': 'submit/index.html', 'cta': 'SEND A CORRECTION'},
    ]

    suppliers, seen = list(BUILDERS), {b['name'].lower() for b in BUILDERS}
    for slug in FAMILY_ORDER:
        for p in pages.get(slug, {}).values():
            for m in p.get('mods', []):
                for w in m.get('who', []):
                    if w['name'].lower() in seen or w['name'].startswith('['):
                        continue
                    seen.add(w['name'].lower())
                    suppliers.append({'name': w['name'], 'url': w.get('url'), 'what': f'{fams[slug]["name"]} · {m["cat"].lower()}'})

    home_res = []
    for slug in FAMILY_ORDER:
        if slug in resources:
            r = resources[slug]
            for kind, lab in (('youtube', 'YT'), ('instagram', 'IG')):
                if r[kind]:
                    it = r[kind][0]
                    home_res.append({'kind': lab, 'name': it['name'], 'url': it['url'], 'focus': fams[slug]['name'].upper()})

    render('home.html', 'index.html', '', active='home', jsonld=[{'@context': 'https://schema.org', '@type': 'WebSite', 'name': SITE_NAME, 'url': SITE_URL, 'description': 'An enthusiast guide to boxy 4x4s.'}, {'@context': 'https://schema.org', '@type': 'Organization', 'name': SITE_NAME, 'url': SITE_URL, 'logo': SITE_URL + 'img/home/lc80-georgia.jpg'}, {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': f['q'], 'acceptedAnswer': {'@type': 'Answer', 'text': f['a']}} for f in faqs]}], title='BoxyTrucks — For the love of right angles',
           description='An enthusiast guide to boxy 4x4s: G-Class, Land Cruiser, Defender, Range Rover, 4Runner, Lexus GX/LX and Grenadier.',
           garage=garage[:8], faqs=faqs, stories=STORIES, suppliers=suppliers, socials=home_res,
           credits=', '.join(HOME_CREDITS) + ' and others via Unsplash and Pexels')
    render('models.html', 'models/index.html', '../', active='models', crumbs=[('Models', 'models/')], jsonld=[{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Models', 'url': SITE_URL + 'models/'}], title='Models — BoxyTrucks', description='Every boxy truck, every generation.', later=LATER, credits='')

    def gen_order(slug):
        return [g['slug'] for g in fams[slug]['generations']]
    rep_groups, mod_groups, res_groups = [], [], []
    for slug in FAMILY_ORDER:
        if slug not in fams:
            continue
        fam = fams[slug]
        for gs in gen_order(slug):
            p = pages[slug].get(gs)
            if not p:
                continue
            h = href('../', slug, gs)
            if p.get('repairs'):
                rep_groups.append({'maker': f'{mlabel(fam["maker"], fam["name"])}', 'model': p['title'], 'href': h, 'repairs': p['repairs']})
            if p.get('mods'):
                mod_groups.append({'maker': f'{mlabel(fam["maker"], fam["name"])}', 'model': p['title'], 'href': h, 'mods': p['mods'], 'fam': slug, 'gen': gs, 'order': len(mod_groups)})
        res_groups.append({'maker': fam['maker'], 'name': fam['name'], 'short': fam['short'], 'href': f'../models/{slug}/index.html', 'res': resources[slug]})

    render('hub.html', 'repairs/index.html', '../', crumbs=[('Repair guides', 'repairs/')], jsonld=[{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Repair guides', 'url': SITE_URL + 'repairs/'}], active='repairs', title='Repair guides — BoxyTrucks', description='DIY repair guides for boxy 4x4s.', credits='',
           hub={'kind': 'repairs', 'eyebrow': 'From the garage', 'title': 'Repair guides', 'lead': 'The jobs owners actually do, rated for a competent home mechanic — symptoms, the fix, tools and parts. Pick a truck.', 'groups': rep_groups})
    render('hub.html', 'mods/index.html', '../', crumbs=[('Mods & builders', 'mods/')], jsonld=[{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Mods & builders', 'url': SITE_URL + 'mods/'}], active='mods', title='Mods & builders — BoxyTrucks', description='Suppliers and builders by model.', credits='',
           hub={'kind': 'mods', 'eyebrow': 'Mods & builders', 'title': 'Who builds them right', 'lead': 'Suspension, armor, racks, restorations and full builds — the suppliers and shops each platform’s owners actually trust.', 'groups': mod_groups, 'suppliers': suppliers, 'builders': BUILDERS})
    render('hub.html', 'resources/index.html', '../', crumbs=[('Resources', 'resources/')], jsonld=[{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Resources', 'url': SITE_URL + 'resources/'}], active='resources', title='Resources — BoxyTrucks', description='YouTube channels, Instagram accounts, forums and references by model.', credits='',
           hub={'kind': 'resources', 'eyebrow': 'Resources', 'title': 'Channels, accounts, forums & references', 'lead': 'The YouTube channels, Instagram accounts, message boards and reference sources worth your time, filed by truck. Suggestions welcome.', 'groups': res_groups})
    render('hub.html', 'for-sale/index.html', '../', crumbs=[('For sale', 'for-sale/')], jsonld=[{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'For sale', 'url': SITE_URL + 'for-sale/'}], active='sale', title='For sale — BoxyTrucks', description='AutoTempest and Bring a Trailer searches for every generation.', credits='',
           hub={'kind': 'sale', 'eyebrow': 'The one you’ll own someday', 'title': 'For sale now', 'lead': 'Live AutoTempest searches across the major marketplaces, plus Bring a Trailer auctions and results, for every generation we cover.'})
    # keep old /watch/ URL working
    (SITE / 'watch').mkdir(exist_ok=True)
    (SITE / 'watch' / 'index.html').write_text('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=../resources/index.html"><title>Resources — BoxyTrucks</title><a href="../resources/index.html">Resources</a>')

    gens_json = json.dumps({s: [{'slug': g['slug'], 'name': g['name'], 'years': g['years']} for g in fams[s]['generations']] for s in fams})
    render('submit.html', 'submit/index.html', '../', active='submit', crumbs=[('Show Us Your Rig', 'submit/')], title='Show Us Your Rig — BoxyTrucks', description='Submit your boxy truck build for a feature.', credits='Hasse Lossius via Unsplash', gens_json=gens_json, submit_email=SUBMIT_EMAIL, site_url=SITE_URL)
    render('disclaimer.html', 'about/disclaimer.html', '../', active='', title='Disclaimer — BoxyTrucks', description='BoxyTrucks specs, fluids and repair guides are for general information: verify against your manual or a qualified mechanic.', credits='', crumbs=[('Disclaimer', 'about/disclaimer.html')])
    render('disclosure.html', 'about/affiliate-disclosure.html', '../', active='', title='Affiliate disclosure — BoxyTrucks', description='How BoxyTrucks uses affiliate links.', credits='', crumbs=[('Affiliate disclosure', 'about/affiliate-disclosure.html')])
    render('submit_thanks.html', 'submit/thanks.html', '../', active='submit', noindex=True, title='Thanks — BoxyTrucks', description='Submission received.', credits='')

    # site search index
    strip = lambda t: LINK_RE.sub(lambda m: m.group(3), str(t or ''))
    idx = []
    def add(kind, title, url, model, text):
        idx.append({'k': kind, 't': title, 'u': url, 'm': model, 'x': strip(text)[:400]})
    for slug in FAMILY_ORDER:
        if slug not in fams: continue
        fam = fams[slug]
        add('Family', f'{mlabel(fam["maker"], fam["name"])}', f'models/{slug}/index.html', f'{mlabel(fam["maker"], fam["name"])}', ' '.join(fam.get('intro', [])) + ' ' + fam['verdict'])
        for g in fam['generations']:
            p = pages[slug].get(g['slug'])
            model = mlabel(fam['maker'], p['title'] if p else g['name'])
            u = f'models/{slug}/{g["slug"]}.html'
            add('Model guide', model, u, model, ' '.join(g.get('codes', [])) + ' ' + g['summary'] + ' ' + (p.get('verdict', '') if p else ''))
            if not p: continue
            for r in p.get('repairs', []):
                add('Repair', r['title'], u + '#repairs', model, r.get('symptoms', '') + ' ' + r.get('tools', ''))
            for f in p.get('faq', []):
                add('Question', f['q'], u + '#faq', model, f['a'])
            for m in p.get('mods', []):
                add('Mods', m['cat'].title() + ' — ' + ', '.join(w['name'] for w in m.get('who', [])), u + '#mods', model, m['why'])
            for s in (p.get('baseline_service') or {}).get('items', []):
                add('Service', s['item'], u + '#service', model, s.get('spec', '') + ' ' + s.get('note', ''))
        for kind, items in resources[slug].items():
            for it in items:
                add('Resource', it['name'], it['url'], f'{mlabel(fam["maker"], fam["name"])}', (it.get('focus') or it.get('note') or '') + ' ' + {'youtube': 'YouTube channel', 'instagram': 'Instagram account', 'forums': 'Forum', 'other': 'Reference'}[kind])
    for s in suppliers:
        if s.get('url'):
            add('Supplier', s['name'], s['url'], s.get('what', ''), s.get('what', ''))
    (SITE / 'search-index.json').write_text(json.dumps(idx, ensure_ascii=False, separators=(',', ':')))
    render('search.html', 'search/index.html', '../', active='search', title='Search — BoxyTrucks', description='Search model guides, repairs, owner questions, suppliers and resources.', credits='', noindex=True)

    from datetime import date
    today = date.today().isoformat()
    urls = sorted(set(SITEMAP))
    (SITE / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n' for u in urls) + '</urlset>\n')
    (SITE / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nDisallow: /submit/thanks.html\n\nSitemap: {SITE_URL}sitemap.xml\n')

    n = sum(1 for _ in SITE.rglob('*.html'))
    full = sum(len(v) for v in pages.values())
    stubs = sum(1 for f in fams.values() for g in f['generations'] if not g['has_page'])
    print(f'built {n} pages · full guides: {full} · overview-only: {stubs}')
    ph = re.compile(r'\[(TO RESEARCH|TBD|TODO|PHOTO|OWNER|STORY|ONE-PARAGRAPH)[^\]]*\]')
    for f in sorted(SITE.rglob('*.html')):
        for m in ph.finditer(f.read_text()):
            print(f'  ! placeholder left in {f.relative_to(SITE)}: {m.group(0)[:60]}')
            break


if __name__ == '__main__':
    main()
