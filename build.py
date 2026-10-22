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
FAMILY_ORDER = ['g-class', 'land-cruiser', 'lexus', '4runner', 'land-rover', 'range-rover', 'grenadier']
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
    {'name': 'International / Scout', 'models': ['Scout 80 / 800', 'Scout II', 'Scout Motors']},
    {'name': 'Jeep', 'models': ['Grand Wagoneer SJ', 'Cherokee XJ']},
    {'name': 'Chevrolet / GMC', 'models': ['K5 Blazer', 'Square-body Suburban']},
    {'name': 'Nissan · Mitsubishi · Isuzu', 'models': ['Patrol Y60', 'Patrol Y61', 'Pajero Gen 1–2', 'Trooper']},
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
    {'img': 'lc-dune.jpg', 'alt': 'A silver Toyota Land Cruiser climbing a dune at sunset', 'tag': 'LAND CRUISER 200 · DUNES', 'title': '[STORY] Chasing the last light up a dune'},
    {'img': 'defender-desert.jpg', 'alt': 'The open cockpit of a vintage Land Rover looking out over desert sand', 'tag': 'SERIES IIA · HUCKBERRY JOURNAL', 'title': 'Panama to Mexico in a 1968 Series IIA: Sinuhe Xavier’s rain-soaked scene report', 'href': 'https://huckberry.com/journal/posts/sinuhe-xavier-scene-report-costa-rica'},
    {'img': 'lc-desert.jpg', 'alt': 'Land Cruiser 70 Series troop carriers parked among desert boulders', 'tag': 'LAND CRUISER 70 · SAHARA', 'title': '[STORY] The Sahara, by troop carrier'},
]
HOME_CREDITS = ['Darina Rodionova', 'Hasse Lossius', 'Kristina', 'Caspian Dahlström', 'Charlota Blunarova']
ALIASES = {('land-cruiser', '60-series'): ('land-cruiser', 'fj60')}
LINK_RE = re.compile(r'\[\[([a-z0-9-]+)/([a-z0-9-]+)\|([^\]]+)\]\]')


from urllib.parse import urlparse, quote
AFFILIATES = []


def load_affiliates():
    try:
        return json.loads((DATA / 'affiliates.json').read_text()).get('programs', [])
    except Exception:
        return []


def affiliate_rewrite(html, programs):
    active = [p for p in programs if p.get('template')]
    if not active:
        return html, False
    hit = False
    def rep(m):
        nonlocal hit
        url = m.group(2)
        host = urlparse(url).netloc.lower().replace('www.', '')
        for p in active:
            if any(host == d or host.endswith('.' + d) for d in p['domains']):
                hit = True
                new = p['template'].replace('{url}', quote(url, safe='')).replace('{raw}', url)
                tail = m.group(3)
                if 'rel="' in tail:
                    tail = tail.replace('rel="', 'rel="sponsored nofollow ', 1)
                else:
                    tail = ' rel="sponsored nofollow noopener"' + tail
                return f'{m.group(1)}{new}"{tail}'
        return m.group(0)
    out = re.sub(r'(<a\b[^>]*?href=")(https?://[^"]+)"([^>]*>)', rep, html)
    return out, hit


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
        fam = d['family']; fam['slug'] = slug
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
        apply_social_manual(pages)
        for g in fam['generations']:
            g['has_page'] = g['slug'] in pages[slug]
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
    art = {'@context': 'https://schema.org', '@type': 'Article', 'headline': f'{fam["maker"]} {page["title"]}: history, buying guide, repairs and FAQs',
           'description': strip(page.get('verdict', g['summary'])), 'abstract': lead[:500], 'image': img,
           'datePublished': '2026-10-22', 'dateModified': date.today().isoformat(),
           'author': {'@type': 'Organization', 'name': SITE_NAME, 'url': SITE_URL},
           'publisher': {'@type': 'Organization', 'name': SITE_NAME, 'url': SITE_URL},
           'mainEntityOfPage': SITE_URL + f'models/{fam["slug"]}/{g["slug"]}.html',
           'about': {'@type': 'Car', 'name': f'{fam["maker"]} {page["title"]}', 'brand': {'@type': 'Brand', 'name': fam['maker'] if fam['maker'] != 'Lexus' else 'Lexus'}, 'model': page['title'], 'vehicleModelDate': g.get('years', '')}}
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
        env.globals['affiliates_on'] = any(p.get('template') for p in AFFILIATES)
        env.globals.update(img=lambda fs, f: f'{root}img/{fs}/{f}',
                           gen_href=lambda fs, gs: (lambda a: f'{root}models/{a[0]}/{a[1]}.html' if gen_exists(*a) else None)(ALIASES.get((fs, gs), (fs, gs))),
                           mark=mark, mark2=lambda: mark('#141513', 18, '#F7F4EE'), nav=NAV)
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
        render('family.html', f'models/{slug}/index.html', '../../', fam=fam, page=main_page, res=res, og_image=(f'img/{slug}/{fam["hero_photo"]}' if fam.get('hero_photo') else None), crumbs=[('Models', 'models/'), (f'{fam["maker"]} {fam["name"]}', f'models/{slug}/')], jsonld=[{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': f'{fam["maker"]} {fam["name"]}', 'description': fam['verdict'], 'url': SITE_URL + f'models/{slug}/', 'mainEntity': {'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': f'{fam["maker"]} {fam["name"]} {g["name"]}', 'url': SITE_URL + f'models/{slug}/{g["slug"]}.html'} for i, g in enumerate(fam['generations'])]}}], reading=[dict(r, gen=k.split('/')[1]) for k, v in reading.items() if k.startswith(slug + '/') for r in v], active='models',
               title=f'{fam["maker"]} {fam["name"]} — BoxyTrucks', description=fam['verdict'], credits=credits_of(fp.values()))
        for g in fam['generations']:
            page = fp.get(g['slug'])
            if page:
                yt = [s for s in page.get('social', []) if s.get('kind') == 'YT']
                ig = [s for s in page.get('social', []) if s.get('kind') != 'YT']
                toc = [(i, l) for i, l, k in [
                    ('story', 'The story', 'story'), ('engineering', 'How it’s built', 'engineering'),
                    ('variants', 'Variants & years', 'generations_table'), ('buying', 'Buying one: what to check', 'buying_checks'),
                    ('service', 'After you buy it', 'baseline_service'), ('repairs', 'Common repairs', 'repairs'), ('faq', 'Questions, answered', 'faq'),
                    ('mods', 'Modifications & who does them', 'mods'), ('sale', 'For sale now', 'searches'),
                    ('resources', 'Resources', None), ('related', 'Related models', 'related')] if (k is None or page.get(k))]
                hero_alt = next((ph['alt'] for ph in page.get('photos', []) if ph['file'] == page.get('hero_photo')), f'{page.get("title", g["name"])} off road')
                page.setdefault('title', g['name'])
                render('gen_page.html', f'models/{slug}/{g["slug"]}.html', '../../', fam=fam, page=page, toc=toc, hero_alt=hero_alt,
                       og_image=(f'img/{slug}/{page["hero_photo"]}' if page.get('hero_photo') else None), og_type='article', crumbs=[('Models', 'models/'), (f'{fam["maker"]} {fam["name"]}', f'models/{slug}/'), (page['title'], f'models/{slug}/{g["slug"]}.html')], jsonld=gen_ld(fam, g, page),
                       part_search=suppliers_cfg.get(slug, []),
                       yt=yt, ig=ig, res=res, reading=reading.get(f'{slug}/{g["slug"]}', []), active='models', title=f'{fam["maker"]} {page["title"]} — BoxyTrucks',
                       description=page.get('verdict', g['summary']), credits=credits_of([page]))
            else:
                render('gen_stub.html', f'models/{slug}/{g["slug"]}.html', '../../', fam=fam, g=g, crumbs=[('Models', 'models/'), (f'{fam["maker"]} {fam["name"]}', f'models/{slug}/'), (g['name'], f'models/{slug}/{g["slug"]}.html')], reading=reading.get(f'{slug}/{g["slug"]}', []), active='models',
                       title=f'{fam["maker"]} {fam["name"]} {g["name"]} — BoxyTrucks', description=g['summary'], credits='')

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
            tire = next((f for f in p.get('faq', []) if 'tire' in f['q'].lower() and 'lift' in f['q'].lower()), None)
            if tire:
                faqs.append({'q': tire['q'], 'a': tire['a'], 'model': label, 'href': href('', slug, p['slug']) + '#faq'})

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

    render('home.html', 'index.html', '', active='home', jsonld=[{'@context': 'https://schema.org', '@type': 'WebSite', 'name': SITE_NAME, 'url': SITE_URL, 'description': 'An enthusiast guide to boxy 4x4s.'}, {'@context': 'https://schema.org', '@type': 'Organization', 'name': SITE_NAME, 'url': SITE_URL, 'logo': SITE_URL + 'img/home/lc80-georgia.jpg'}], title='BoxyTrucks — For the love of right angles',
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
                rep_groups.append({'maker': f'{fam["maker"]} {fam["name"]}', 'model': p['title'], 'href': h, 'repairs': p['repairs']})
            if p.get('mods'):
                mod_groups.append({'maker': f'{fam["maker"]} {fam["name"]}', 'model': p['title'], 'href': h, 'mods': p['mods'], 'fam': slug, 'gen': gs, 'order': len(mod_groups)})
        res_groups.append({'maker': fam['maker'], 'name': fam['name'], 'href': f'../models/{slug}/index.html', 'res': resources[slug]})

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
        add('Family', f'{fam["maker"]} {fam["name"]}', f'models/{slug}/index.html', f'{fam["maker"]} {fam["name"]}', ' '.join(fam.get('intro', [])) + ' ' + fam['verdict'])
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
                add('Resource', it['name'], it['url'], f'{fam["maker"]} {fam["name"]}', (it.get('focus') or it.get('note') or '') + ' ' + {'youtube': 'YouTube channel', 'instagram': 'Instagram account', 'forums': 'Forum', 'other': 'Reference'}[kind])
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


if __name__ == '__main__':
    main()
