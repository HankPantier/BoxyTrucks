#!/usr/bin/env python3
"""Build the BoxyTrucks static prototype from data/ into site/.

data/<family>.json            family landing + the family's flagship example page
data/pages/<family>/<gen>.json  a full guide for any other generation
data/resources/<family>.json    YouTube / Instagram / forums / other references
"""
import json
from collections import defaultdict
import re
from pathlib import Path
from markupsafe import Markup, escape
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).parent
DATA = ROOT / 'data'
SITE = ROOT / 'site'

SITE_URL = 'https://boxytrucks.com/'
SUBMIT_EMAIL = 'boxytrucks@gmail.com'
# TODO: Google Analytics — paste the GA4 measurement ID (G-XXXXXXX) here to enable tracking on every page.
# Newsletter: paste the provider's form action once an account exists, e.g. Buttondown
# 'https://buttondown.com/api/emails/embed-subscribe/<username>' (field 'email'). Empty = sign-up hidden.
NEWSLETTER = {'provider': 'kit', 'action': 'https://app.kit.com/forms/10110095/subscriptions', 'field': 'email_address'}
GA_MEASUREMENT_ID = 'G-XHC493ES9X'
SITE_NAME = 'BoxyTrucks'
INSTAGRAM_URL = 'https://www.instagram.com/boxytrucks/'
DEFAULT_OG_IMAGE = 'img/home/lc80-georgia.jpg'
SITEMAP = []
INDEXNOW_KEY = 'df5e9f5700c975efa4ebdb9e75a3fa77'  # public by design: IndexNow verifies ownership by fetching /<key>.txt
# Families are shown everywhere in alphabetical order of the name people use for them.
SHORT_NAME = {'4runner': '4Runner', 'g-class': 'G-Class', 'grenadier': 'Grenadier', 'jeep': 'Jeep',
              'land-cruiser': 'Land Cruiser', 'land-rover': 'Land Rover', 'lexus': 'Lexus LX & GX', 'range-rover': 'Range Rover',
              'nissan-patrol': 'Nissan Patrol', 'scout': 'International Scout', 'bronco': 'Ford Bronco',
              'chevrolet': 'Chevrolet / GMC', 'suzuki': 'Suzuki', 'pajero': 'Mitsubishi Pajero', 'trooper': 'Isuzu Trooper', 'hummer': 'Hummer H1'}
FAMILY_ORDER = sorted(SHORT_NAME, key=lambda k: SHORT_NAME[k].lower())
NAV_FAMS = []
NAV = [
    {'key': 'models', 'label': 'MODELS', 'href': 'models/index.html'},
    {'key': 'garage', 'label': 'GARAGE', 'href': 'garage/index.html', 'children': [
        {'key': 'repairs', 'label': 'Repair guides', 'href': 'repairs/index.html'},
        {'key': 'tires', 'label': 'Tire fitment', 'href': 'tires/index.html'},
        {'key': 'compare', 'label': 'Compare', 'href': 'compare/index.html'},
        {'key': 'bestyears', 'label': 'Best years to buy', 'href': 'garage/index.html#best-years'},
        {'key': 'resources', 'label': 'Resources', 'href': 'resources/index.html'},
    ]},
    {'key': 'mods', 'label': 'MODS & BUILDERS', 'href': 'mods/index.html'},
    {'key': 'sale', 'label': 'FOR SALE', 'href': 'for-sale/index.html'},
    {'key': 'submit', 'label': 'SHOW US YOUR RIG', 'href': 'submit/index.html', 'cta': True},
]
GARAGE_KEYS = {'garage', 'repairs', 'tires', 'compare', 'resources', 'recalls'}
LATER = [
    {'name': 'Cult & military', 'models': ['Lada Niva', 'UAZ-469', 'Pinzgauer', 'Unimog', 'Volvo C303']},
    {'name': 'More classics', 'models': ['Dodge Ramcharger', 'International Travelall', 'Toyota Hilux Surf']},
]
BUILDERS = [
    {'name': 'Jack Wagon Overlanding', 'what': 'G-Class · overland parts & builds', 'url': 'https://jackwagonoverlanding.com/'},
    {'name': 'Expedition Motor Company', 'what': 'G-Class · ex-military 250 GD / Wolf restorations', 'url': 'https://www.expeditionmotorcompany.com/'},
    {'name': 'ICON 4x4', 'what': 'Land Cruiser · restomods', 'url': 'https://www.icon4x4.com/'},
    {'name': 'The FJ Company', 'what': 'Land Cruiser · restorations', 'url': 'https://www.fj.co/'},
    {'name': 'Arkonik', 'what': 'Defender · restomods', 'url': 'https://www.arkonik.com/'},
]
STORIES = [
    {'img': 'lc-dune.jpg', 'alt': 'A white Toyota Land Cruiser 200 Series climbing a desert dune at sunset', 'tag': 'LAND CRUISER 200 · EXPEDITION PORTAL', 'title': 'Staples in Tents: the 200 Series built for Mexico, Baja and, next, the Arctic Ocean', 'href': 'https://expeditionportal.com/feature-vehicle-staples-in-tents-200-series-toyota-land-cruiser/'},
    {'img': 'defender-desert.jpg', 'alt': 'The open cockpit of a vintage Land Rover looking out over desert sand', 'tag': 'SERIES IIA · HUCKBERRY JOURNAL', 'title': 'Panama to Mexico in a 1968 Series IIA: Sinuhe Xavier’s rain-soaked scene report', 'href': 'https://huckberry.com/journal/posts/sinuhe-xavier-scene-report-costa-rica'},
    {'img': 'lc-desert.jpg', 'alt': 'Land Cruiser 70 Series troop carriers parked among desert boulders', 'tag': 'LAND CRUISER 70 · OVERLAND JOURNAL', 'title': 'Why the 70 Series is still the overlander’s truck, and how to build one without overdoing it', 'href': 'https://overlandjournal.com/pages/principles-of-overlanding-building-a-70-series-land-cruiser'},
]
HOME_CREDITS = ['Darina Rodionova', 'Hasse Lossius', 'Kristina', 'Caspian Dahlström', 'Charlota Blunarova']
ALIASES = {('land-cruiser', '60-series'): ('land-cruiser', 'fj60')}
LINK_RE = re.compile(r'\[\[([a-z0-9-]+)/([a-z0-9-]+)\|([^\]]+)\]\]')
LINK_PLAIN = lambda t: LINK_RE.sub(lambda m: m.group(3), str(t or ''))


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


CONFIRM_RE = re.compile(r'\s*\[(CONFIRM[^\]]*)\]')

def _confirm_txt(m):
    t = m.group(1).strip()
    t = re.sub(r'\s+', ' ', t).replace('CONFIRM', 'confirm', 1)
    t = t if t != 'confirm' else 'confirm in your manual'
    return t[0].lower() + t[1:].lower() if t.isupper() or t.startswith('confirm ') else t

def confirm_plain(text):
    return CONFIRM_RE.sub(lambda m: f' ({_confirm_txt(m)})', str(text))

def confirm_html(html):
    parts = re.split(r'(<script\b.*?</script>|<[^>]+>)', html, flags=re.S)
    out = []
    for seg in parts:
        if seg.startswith('<script'):
            out.append(confirm_plain(seg))
        elif seg.startswith('<'):
            out.append(confirm_plain(seg) if 'CONFIRM' in seg else seg)
        else:
            out.append(CONFIRM_RE.sub(lambda m: f' <span class="chk" title="Not checked against a factory source: confirm before you rely on it">{_confirm_txt(m)}</span>', seg))
    return ''.join(out)


def repair_slug(title, used):
    t = re.sub(r'\(.*?\)', '', str(title)).lower().replace('&', 'and')
    t = re.sub(r'[^a-z0-9]+', '-', t).strip('-')
    t = '-'.join(t.split('-')[:9]) or 'repair'
    base, n = t, 2
    while t in used:
        t = f'{base}-{n}'; n += 1
    used.add(t)
    return t


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



# ---- pretty URLs: every page is built as <name>/index.html and linked as <name>/ ----
from urllib.parse import urljoin as _urljoin
AVATARS = {}
def avatar_key(u):
    u = u.split('?')[0].split('#')[0].rstrip('/')
    u = re.sub(r'/(videos|featured|streams|shorts|about)$', '', u)
    u = re.sub(r'^https://(www\.)?', 'https://www.', u)
    if 'instagram.com' in u or '/@' in u:
        u = u.lower()
    return u

def pretty_path(path):
    """'/models/jeep/tj.html#faq' -> '/models/jeep/tj/#faq'; '/x/index.html' -> '/x/'."""
    frag = ''
    for sep in ('#', '?'):
        if sep in path:
            i = path.index(sep); path, frag = path[:i], path[i:] + frag
    if path.endswith('404.html'):
        pass
    elif path.endswith('/index.html'):
        path = path[:-10]
    elif path == 'index.html':
        path = ''
    elif path.endswith('.html'):
        path = path[:-5] + '/'
    return path + frag

def pretty_out(out):
    if out.endswith('index.html') or out == '404.html':
        return out
    return out[:-5] + '/index.html'

_ATTR_RE = re.compile(r'\b(href|src|action)="([^"]*)"')
_SKIP = ('http:', 'https:', '//', 'mailto:', 'tel:', 'data:', 'javascript:', '#', 'sms:')
def prettify_html(html, old_out):
    base = '/' + old_out
    def fix(m):
        attr, url = m.group(1), m.group(2)
        if not url or url.startswith(_SKIP) or '{{' in url or "'" in url:
            return m.group(0)
        u = _urljoin(base, url.replace('&amp;', '&')).replace('&', '&amp;')
        return f'{attr}="{pretty_path(u)}"'
    html = _ATTR_RE.sub(fix, html)
    # absolute site URLs (canonical, og:url, JSON-LD, form redirects)
    html = re.sub(re.escape(SITE_URL) + r'([^"\s<>]*?\.html)', lambda m: SITE_URL + pretty_path(m.group(1)).lstrip('/'), html)
    return html


# ---------- responsive images ----------
RESP_WIDTHS = (480, 800, 1280)
RESP_DIR = 'img/_r'
RESP = {}  # '/img/x/y.jpg' -> [(url, width), ...] plus the original

def ensure_variants():
    """Make WebP copies of every site image at a few widths (cached; only missing ones are built)."""
    try:
        from PIL import Image
    except ImportError:
        print('  Pillow not installed: responsive images skipped')
        return
    made = 0
    for f in sorted((SITE / 'img').rglob('*')):
        if f.suffix.lower() not in ('.jpg', '.jpeg', '.png') or '/_r/' in f.as_posix() or '/avatars/' in f.as_posix():
            continue
        rel = f.relative_to(SITE / 'img').as_posix()
        try:
            with Image.open(f) as im:
                ow, oh = im.size
                cands = []
                for w in RESP_WIDTHS:
                    if w >= ow * 0.9:
                        continue
                    out = SITE / RESP_DIR / f'{rel.rsplit(".", 1)[0]}-{w}.webp'
                    if not out.exists() or out.stat().st_mtime < f.stat().st_mtime:
                        out.parent.mkdir(parents=True, exist_ok=True)
                        rim = im.convert('RGB').resize((w, round(oh * w / ow)), Image.LANCZOS)
                        rim.save(out, 'WEBP', quality=72, method=4)
                        made += 1
                    cands.append((f'/{RESP_DIR}/{rel.rsplit(".", 1)[0]}-{w}.webp', w))
                cands.append(('/img/' + rel, ow))  # the original is the largest option
                RESP['/img/' + rel] = cands
        except Exception as e:
            print('  variant failed', rel, e)
    print(f'  responsive images: {len(RESP)} images, {made} variants built')

_IMG_RE = re.compile(r'<img\b[^>]*>')
def responsive_imgs(html):
    def fix(m):
        tag = m.group(0)
        if 'srcset=' in tag:
            return tag
        sm = re.search(r'\ssrc="(/img/[^"]+)"', tag)
        if not sm or sm.group(1) not in RESP:
            return tag
        srcset = ', '.join(f'{u} {w}w' for u, w in RESP[sm.group(1)])
        if 'fetchpriority="high"' in tag or 'class="hero' in tag:
            sizes = '100vw'
        else:
            sizes = '(max-width: 760px) 100vw, (max-width: 1200px) 60vw, 720px'
        return tag[:-1].rstrip('/').rstrip() + f' srcset="{srcset}" sizes="{sizes}" decoding="async">'
    return _IMG_RE.sub(fix, html)

def redirect_stub(target_url):
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved — BoxyTrucks</title>'
            f'<link rel="canonical" href="{SITE_URL}{target_url.lstrip("/")}"><meta name="robots" content="noindex">'
            f'<meta http-equiv="refresh" content="0; url={target_url}">'
            f'<script>location.replace("{target_url}"+location.hash)</script></head>'
            f'<body><a href="{target_url}">This page has moved.</a></body></html>')

def main():
    global AVATARS
    try:
        AVATARS = json.loads((DATA / 'avatars.json').read_text())
    except Exception:
        AVATARS = {}
    ensure_variants()
    fams, flagship, pages, resources = load()
    for _fs, _gp in pages.items():
        for _gs, _p in _gp.items():
            _used = set()
            for _r in (_p or {}).get('repairs', []) or []:
                _r['slug'] = repair_slug(_r.get('title', ''), _used)
    _cmp_early = defaultdict(list)
    for _f in sorted((DATA / 'compare').glob('*.json')) if (DATA / 'compare').exists() else []:
        _c = json.loads(_f.read_text())
        for _m in _c['models']:
            _cmp_early[_m].append({'slug': _c['slug'], 'title': _c['title']})
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
        env.globals['avatar'] = lambda u: (lambda a: f'/img/{a}' if a else None)(AVATARS.get(avatar_key(u or '')))
        env.globals['mlabel'] = mlabel
        env.globals['newsletter'] = NEWSLETTER
        env.globals['amz_q'] = amz_q
        env.globals['amazon_on'] = any(p['name'] == 'Amazon Associates' and p.get('params') for p in AFFILIATES)
        env.globals.update(img=lambda fs, f: f'{root}img/{fs}/{f}',
                           gen_href=lambda fs, gs: (lambda a: f'{root}models/{a[0]}/{a[1]}.html' if gen_exists(*a) else None)(ALIASES.get((fs, gs), (fs, gs))),
                           mark=mark, mark2=lambda: mark('#141513', 18, '#F7F4EE'), nav=NAV, nav_fams=NAV_FAMS, garage_keys=GARAGE_KEYS, instagram_url=INSTAGRAM_URL)
        path = pretty_path(out)
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
        html = prettify_html(html, out)
        html = responsive_imgs(html)
        if 'CONFIRM' in html:
            html = confirm_html(html)
        new_out = pretty_out(out)
        if new_out != out:  # keep the old .html address working
            (SITE / out).parent.mkdir(parents=True, exist_ok=True)
            (SITE / out).write_text(redirect_stub('/' + pretty_path(out)))
        dest = SITE / new_out
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html)

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
                       part_search=suppliers_cfg.get(slug, []), cmp_links=_cmp_early.get(f'{slug}/{g["slug"]}', []),
                       yt=yt, ig=ig, res=res, reading=reading.get(f'{slug}/{g["slug"]}', []), active='models', title=f'{mlabel(fam["maker"], page["title"])} — BoxyTrucks',
                       description=page.get('verdict', g['summary']), credits=credits_of([page]))
                if page.get('plate') or (page.get('baseline_service') or {}).get('items'):
                    _m = mlabel(fam['maker'], page['title'])
                    render('specs.html', f'models/{slug}/{g["slug"]}/specs.html', '../../../', fam=fam, g=g, p=page, x=x, model=_m,
                           gen_href=f'../../../models/{slug}/{g["slug"]}.html', active='models', og_type='article',
                           crumbs=[('Models', 'models/'), (f'{mlabel(fam["maker"], fam["name"])}', f'models/{slug}/'), (page['title'], f'models/{slug}/{g["slug"]}/'), ('Specs & fluids', f'models/{slug}/{g["slug"]}/specs/')],
                           jsonld=[{'@context': 'https://schema.org', '@type': 'Article', 'headline': f'{_m} specs, fluids and service intervals', 'url': SITE_URL + f'models/{slug}/{g["slug"]}/specs/', 'publisher': {'@type': 'Organization', 'name': SITE_NAME, 'url': SITE_URL}}],
                           title=f'{_m} specs, fluid capacities & service intervals | BoxyTrucks',
                           description=f'{_m} ({g.get("years", "")}) spec sheet, fluid capacities, oil grades, service intervals, wheel and tire sizes and parts numbers, on one printable page.'[:158], credits='')
            else:
                render('gen_stub.html', f'models/{slug}/{g["slug"]}.html', '../../', fam=fam, g=g, crumbs=[('Models', 'models/'), (f'{mlabel(fam["maker"], fam["name"])}', f'models/{slug}/'), (g['name'], f'models/{slug}/{g["slug"]}.html')], reading=reading.get(f'{slug}/{g["slug"]}', []), active='models',
                       title=f'{mlabel(fam["maker"], fam["name"])} {g["name"]} — BoxyTrucks', description=g['summary'], credits='')


    # ---------- best-years pages (one per family) and comparison pages ----------
    compares = []
    for f in sorted((DATA / 'compare').glob('*.json')) if (DATA / 'compare').exists() else []:
        c = json.loads(f.read_text())
        if all(gen_exists(*m.split('/')) for m in c['models']):
            compares.append(c)
    def model_info(key, root):
        fs, gs = key.split('/')
        fam, p = fams[fs], pages[fs].get(gs) or {}
        name = mlabel(fam['maker'], p.get('title') or next(g['name'] for g in fam['generations'] if g['slug'] == gs))
        return {'key': key, 'name': name, 'href': f'{root}models/{fs}/{gs}.html', 'img': (f'{root}img/{fs}/{p["hero_photo"]}' if p.get('hero_photo') else None)}
    BEST_Q = re.compile(r'best (model )?years?|which years?|years? (to|should I) (buy|avoid)', re.I)
    COMPARE_BY_GEN = defaultdict(list)
    for c in compares:
        for m in c['models']:
            COMPARE_BY_GEN[m].append(c)
    by_fam = []
    for slug in FAMILY_ORDER:
        if slug not in fams: continue
        fam = fams[slug]
        gens = []
        for g in fam['generations']:
            p = pages[slug].get(g['slug'])
            if not p: continue
            tl = (p.get('x') or {}).get('timeline') or []
            ans = next((f['a'] for f in p.get('faq', []) if BEST_Q.search(f['q'])), None)
            gens.append({'slug': g['slug'], 'title': p.get('title', g['name']), 'years': g['years'], 'answer': ans,
                         'flags': [t for t in tl if t.get('flag') in ('buy', 'avoid', 'recall')]})
        label = mlabel(fam['maker'], fam['name'])
        n_buy = sum(1 for g in gens if any(t['flag'] == 'buy' for t in g['flags']))
        NUMW = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve'}
        lead = ((f'{len(gens)} generations of the {label}, and for each one the model years owners and specialists ' if len(gens) > 1 else f'For the {label}: the model years owners and specialists ') +
                f'recommend, the ones with documented problems, and the recalls to check. '
                + (f'{NUMW.get(n_buy, n_buy)} of them {"has" if n_buy == 1 else "have"} a clear sweet spot; the rest are best bought on condition.' if n_buy and n_buy < len(gens) else
                   ('Every generation has a clear sweet spot.' if len(gens) > 1 else 'There is a clear sweet spot.') if n_buy else 'None has a single standout year, so buy on condition and history.'))
        fam_compares = [c for c in compares if any(m.startswith(slug + '/') for m in c['models'])]
        faq_ld = [{'@type': 'Question', 'name': f'What are the best {g["title"]} years to buy?', 'acceptedAnswer': {'@type': 'Answer', 'text': LINK_RE.sub(lambda m: m.group(3), g['answer'])}} for g in gens if g['answer']]
        render('best_years.html', f'models/{slug}/best-years.html', '../../', fam=fam, gens=gens, lead=lead, compares=fam_compares, active='models',
               crumbs=[('Models', 'models/'), (label, f'models/{slug}/'), ('Best years', f'models/{slug}/best-years.html')],
               jsonld=([{'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': faq_ld}] if faq_ld else []),
               title=f'Best {label} years to buy (and which to avoid) — BoxyTrucks',
               description=f'The best {label} years to buy and the ones to avoid, generation by generation, with the recalls to check. Sourced from owners and specialists.'[:158],
               credits='')
        by_fam.append({'slug': slug, 'label': label})
    for c in compares:
        ms = [model_info(m, '../') for m in c['models']]
        names = {m['key']: m['name'] for m in ms}
        render('compare.html', f'compare/{c["slug"]}.html', '../', c=c, ms=ms, names=names, active='compare', og_type='article',
               og_image=(ms[0]['img'][3:] if ms[0]['img'] else None),
               crumbs=[('Compare', 'compare/'), (c['title'], f'compare/{c["slug"]}.html')],
               jsonld=[{'@context': 'https://schema.org', '@type': 'Article', 'headline': c['title'], 'description': c['description'], 'url': SITE_URL + f'compare/{c["slug"]}/',
                        'publisher': {'@type': 'Organization', 'name': SITE_NAME}},
                       {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': f['q'], 'acceptedAnswer': {'@type': 'Answer', 'text': LINK_RE.sub(lambda m: m.group(3), f['a'])}} for f in c.get('faqs', [])]}],
               title=f'{c["title"]}: which to buy — BoxyTrucks', description=c['description'][:158], credits='')
    for c in compares:
        c['fam_label'] = ' vs '.join(dict.fromkeys(mlabel(fams[m.split('/')[0]]['maker'], fams[m.split('/')[0]]['name']) for m in c['models']))
    render('compare_hub.html', 'compare/index.html', '../', compares=compares, by_fam=by_fam, active='compare', crumbs=[('Compare', 'compare/')],
           jsonld=[{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Compare', 'url': SITE_URL + 'compare/'}],
           title='Compare boxy 4x4s head to head — BoxyTrucks', description='80 vs 100 Series, JK vs JL, Wrangler vs Bronco, Defender vs Grenadier vs G-Class: sourced head-to-heads and the best years to buy.', credits='')


    # ---------- tire fitment tool ----------
    _clean = lambda t: LINK_RE.sub(lambda m: m.group(3), re.sub(r'\s*\[CONFIRM[^\]]*\]', '', str(t or ''))).strip()
    tf_rows = []
    for slug in FAMILY_ORDER:
        if slug not in fams: continue
        fam = fams[slug]
        for g in fam['generations']:
            p = pages[slug].get(g['slug'])
            ft = ((p or {}).get('x') or {}).get('fitment') or {}
            if not p or not ft.get('max_tire'): continue
            tf_rows.append({'fs': slug, 'gs': g['slug'], 'fam': mlabel(fam['maker'], fam['name']), 'name': p.get('title', g['name']), 'years': g['years'],
                            'stock': [_clean(x) for x in ft.get('stock', [])][:2], 'bolt': _clean((ft.get('wheel') or {}).get('bolt_pattern')),
                            'tires': [{'lift': _clean(t['lift']), 'size': _clean(t['size']), 'note': _clean(t.get('note'))} for t in ft['max_tire']]})
    if tf_rows:
        tf_fams = [{'slug': s, 'label': next(r['fam'] for r in tf_rows if r['fs'] == s)} for s in dict.fromkeys(r['fs'] for r in tf_rows)]
        tf_first = next((r for r in tf_rows if r['fs'] == 'land-cruiser' and r['gs'] == '80-series'), tf_rows[0])
        render('tires.html', 'tires/index.html', '../', rows=tf_rows, fams=tf_fams, first=tf_first, active='tires',
               data_json=Markup(json.dumps(tf_rows, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')),
               crumbs=[('Tire fitment', 'tires/')],
               jsonld=[{'@context': 'https://schema.org', '@type': 'WebApplication', 'name': 'BoxyTrucks tire fitment tool', 'url': SITE_URL + 'tires/', 'applicationCategory': 'UtilitiesApplication', 'operatingSystem': 'Any', 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'}}],
               title='Biggest tire without a lift (and with one): fitment for every boxy 4x4 — BoxyTrucks',
               description='Pick your truck and lift height to see the biggest tire owners and specialists run on every Land Cruiser, G-Class, Jeep, Bronco, 4Runner and more.', credits='')

    render('garage.html', 'garage/index.html', '../', active='garage', by_fam=by_fam, n_compare=len(compares), n_tires=len(tf_rows) if tf_rows else 0,
           crumbs=[('Garage', 'garage/')],
           jsonld=[{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Garage', 'url': SITE_URL + 'garage/'}],
           title='Garage: repairs, tire fitment, comparisons and best years — BoxyTrucks',
           description='The BoxyTrucks garage: DIY repair guides, the tire fitment tool, head-to-head comparisons, the best years to buy and the best owner resources.', credits='')

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
         'a': 'Nearly every repair, and every item in each guide\'s “After you buy it” service list, links to the parts you need at suppliers owners trust for that truck, usually with an Amazon search alongside. (Recall checks and a few dealer-only jobs have no parts links.) Use the part numbers, check fitment against your VIN, and when in doubt call the supplier.',
         'href': 'repairs/index.html', 'cta': 'BROWSE ALL REPAIRS'},
        {'model': 'BUYING', 'q': 'Can I buy a truck here?',
         'a': 'No, we don\'t sell anything. Each guide to a truck you can buy links straight to live AutoTempest searches and Bring a Trailer listings for that generation, and the buying checks tell you what to look at before you hand over money.',
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

    render('home.html', 'index.html', '', active='home', jsonld=[{'@context': 'https://schema.org', '@type': 'WebSite', 'name': SITE_NAME, 'url': SITE_URL, 'description': 'An enthusiast guide to boxy 4x4s: history, buying checks, repairs, parts and mods for every generation.', 'potentialAction': {'@type': 'SearchAction', 'target': {'@type': 'EntryPoint', 'urlTemplate': SITE_URL + 'search/?q={search_term_string}'}, 'query-input': 'required name=search_term_string'}}, {'@context': 'https://schema.org', '@type': 'Organization', 'name': SITE_NAME, 'url': SITE_URL, 'logo': SITE_URL + 'img/home/lc80-georgia.jpg', 'sameAs': [INSTAGRAM_URL]}, {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': f['q'], 'acceptedAnswer': {'@type': 'Answer', 'text': f['a']}} for f in faqs]}], title='BoxyTrucks — For the love of right angles',
           description='An enthusiast guide to boxy 4x4s: ' + ', '.join(SHORT_NAME.get(f['slug'], f['name']) for f in fam_list) + '. History, buying checks, repairs, parts, mods and where to find one.',
           garage=garage[:8], faqs=faqs, stories=STORIES, suppliers=suppliers, socials=home_res,
           credits=', '.join(HOME_CREDITS) + ' and others via Unsplash and Pexels')
    render('models.html', 'models/index.html', '../', active='models', crumbs=[('Models', 'models/')], jsonld=[{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Models', 'url': SITE_URL + 'models/'}], title='Models — BoxyTrucks', description='Every boxy 4x4 we cover, family by family and generation by generation: Land Cruiser, G-Class, Defender, Jeep, Bronco, Patrol, Scout and more.', later=LATER, credits='')

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
                rep_groups.append({'maker': f'{mlabel(fam["maker"], fam["name"])}', 'fam_short': fam['short'], 'model': p['title'], 'href': h, 'repairs': p['repairs'], 'id': f'{slug}-{gs}', 'fam': slug, 'gen': gs})
            if p.get('mods'):
                mod_groups.append({'maker': f'{mlabel(fam["maker"], fam["name"])}', 'model': p['title'], 'href': h, 'mods': p['mods'], 'fam': slug, 'gen': gs, 'order': len(mod_groups)})
        res_groups.append({'maker': fam['maker'], 'name': fam['name'], 'short': fam['short'], 'href': f'../models/{slug}/index.html', 'res': resources[slug]})

    n_repair_pages = 0
    for slug in FAMILY_ORDER:
        if slug not in fams:
            continue
        fam = fams[slug]
        for gs in gen_order(slug):
            p = pages[slug].get(gs)
            if not p or not p.get('repairs'):
                continue
            model = mlabel(fam['maker'], p['title'])
            reps = p['repairs']
            for r in reps:
                rt = LINK_PLAIN(r.get('title', ''))
                steps = [x.strip() for x in re.split(r'(?<=[.!?])\s+(?=[A-Z])', LINK_PLAIN(r.get('fix', ''))) if len(x.strip()) > 3]
                tools = [x.strip() for x in str(r.get('tools', '')).split('·') if x.strip()]
                url = SITE_URL + f'repairs/{slug}/{gs}/{r["slug"]}/'
                howto = {'@context': 'https://schema.org', '@type': 'HowTo', 'name': f'{rt}: {model}', 'url': url,
                         'description': LINK_PLAIN(r.get('symptoms', ''))[:300],
                         'tool': [{'@type': 'HowToTool', 'name': t[:120]} for t in tools[:12]],
                         'supply': [{'@type': 'HowToSupply', 'name': pt.get('name', '')} for pt in (r.get('parts') or [])][:12],
                         'step': [{'@type': 'HowToStep', 'position': i + 1, 'text': st} for i, st in enumerate(steps)],
                         'publisher': {'@type': 'Organization', 'name': SITE_NAME, 'url': SITE_URL}}
                others = [o for o in reps if o is not r]
                render('repair.html', f'repairs/{slug}/{gs}/{r["slug"]}.html', '../../../', fam=fam, p=p, r=r, model=model, steps=steps, others=others,
                       gen_href=f'../../../models/{slug}/{gs}.html', fam_slug=slug, gen_slug=gs, active='repairs', og_type='article', part_search=suppliers_cfg.get(slug, []),
                       crumbs=[('Repair guides', 'repairs/'), (model, f'models/{slug}/{gs}/'), (rt, f'repairs/{slug}/{gs}/{r["slug"]}/')],
                       jsonld=[howto], title=f'{rt} — {model} DIY repair guide | BoxyTrucks'[:110],
                       description=(f'{model}: ' + LINK_PLAIN(r.get('symptoms', '')))[:158], credits='')
                n_repair_pages += 1
    print(f'  repair pages: {n_repair_pages}')
    rc_groups, rc_recent, n_items, n_tsbs = [], [], 0, 0
    for slug in FAMILY_ORDER:
        if slug not in fams:
            continue
        fam = fams[slug]
        for gs in gen_order(slug):
            p = pages[slug].get(gs)
            if not p:
                continue
            rc = (p.get('x') or {}).get('recalls') or {}
            items, tsbs = rc.get('items') or [], rc.get('tsbs') or []
            if not items and not tsbs:
                continue
            model = mlabel(fam['maker'], p['title'])
            h = f'../models/{slug}/{gs}.html'
            rc_groups.append({'fam': slug, 'gen': gs, 'model': model, 'href': h, 'items': items, 'tsbs': tsbs})
            n_items += len(items); n_tsbs += len(tsbs)
            for r in items:
                m = re.search(r'(\d\d)V(\d{3})', r.get('ref', '') or '')
                if m:
                    _yy = int(m.group(1)); rc_recent.append(((2000 + _yy) if _yy < 60 else (1900 + _yy), int(m.group(2)), dict(r, model=model, href=h)))
    rc_recent = [r for *_, r in sorted(rc_recent, key=lambda t: (t[0], t[1]), reverse=True)[:12]]
    render('recalls.html', 'recalls/index.html', '../', active='recalls', groups=rc_groups, recent=rc_recent, n_items=n_items, n_tsbs=n_tsbs,
           fam_opts=[{'slug': f, 'label': mlabel(fams[f]['maker'], fams[f]['name'])} for f in FAMILY_ORDER if f in fams and any(g['fam'] == f for g in rc_groups)],
           crumbs=[('Garage', 'garage/'), ('Recall tracker', 'recalls/')],
           jsonld=[{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Recall tracker', 'url': SITE_URL + 'recalls/'}],
           title='Recall tracker: every recall for boxy 4x4s, by model — BoxyTrucks', description=f'{n_items} recalls and {n_tsbs} service bulletins for Land Cruisers, G-Wagens, Defenders, Jeeps, Broncos and more, by generation, with links to NHTSA.', credits='')
    render('hub.html', 'repairs/index.html', '../', crumbs=[('Repair guides', 'repairs/')], jsonld=[{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Repair guides', 'url': SITE_URL + 'repairs/'}], active='repairs', title='Repair guides — BoxyTrucks', description='DIY repair guides for boxy 4x4s by model: symptoms, tools, steps and the parts you need, from Land Cruisers to Defenders and Jeeps.', credits='',
           hub={'kind': 'repairs', 'eyebrow': 'From the garage', 'title': 'Repair guides', 'lead': 'The jobs owners actually do, rated for a competent home mechanic — symptoms, the fix, tools and parts. Pick a truck.', 'groups': rep_groups})
    render('hub.html', 'mods/index.html', '../', crumbs=[('Mods & builders', 'mods/')], jsonld=[{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Mods & builders', 'url': SITE_URL + 'mods/'}], active='mods', title='Mods & builders — BoxyTrucks', description='Who makes the parts and who builds the trucks: suspension, armor, lockers and full builds for every boxy 4x4 we cover, sorted by model.', credits='',
           hub={'kind': 'mods', 'eyebrow': 'Mods & builders', 'title': 'Who builds them right', 'lead': 'Suspension, armor, racks, restorations and full builds — the suppliers and shops each platform’s owners actually trust.', 'groups': mod_groups, 'suppliers': suppliers, 'builders': BUILDERS})
    render('hub.html', 'resources/index.html', '../', crumbs=[('Resources', 'resources/')], jsonld=[{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Resources', 'url': SITE_URL + 'resources/'}], active='resources', title='Resources — BoxyTrucks', description='The best YouTube channels, Instagram accounts, owner forums and reference sites for every boxy 4x4 we cover, sorted by model.', credits='',
           hub={'kind': 'resources', 'eyebrow': 'Resources', 'title': 'Channels, accounts, forums & references', 'lead': 'The YouTube channels, Instagram accounts, message boards and reference sources worth your time, filed by truck. Suggestions welcome.', 'groups': res_groups})
    render('hub.html', 'for-sale/index.html', '../', crumbs=[('For sale', 'for-sale/')], jsonld=[{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'For sale', 'url': SITE_URL + 'for-sale/'}], active='sale', title='For sale — BoxyTrucks', description='Find a boxy 4x4 for sale: ready-made AutoTempest and Bring a Trailer searches for every generation, from FJ40s to Grenadiers.', credits='',
           hub={'kind': 'sale', 'eyebrow': 'The one you’ll own someday', 'title': 'For sale now', 'lead': 'Live AutoTempest searches across the major marketplaces, plus Bring a Trailer auctions and results, for every generation we cover.'})
    # keep old /watch/ URL working
    (SITE / 'watch').mkdir(exist_ok=True)
    (SITE / 'watch' / 'index.html').write_text('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=/resources/"><title>Resources — BoxyTrucks</title><a href="/resources/">Resources</a>')

    gens_json = json.dumps({s: [{'slug': g['slug'], 'name': g['name'], 'years': g['years']} for g in fams[s]['generations']] for s in fams})
    render('submit.html', 'submit/index.html', '../', active='submit', crumbs=[('Show Us Your Rig', 'submit/')], title='Show Us Your Rig — BoxyTrucks', description='Show Us Your Rig: send photos and the story of your boxy 4x4 build for a feature on BoxyTrucks. Off-road shots preferred.', credits='Hasse Lossius via Unsplash', gens_json=gens_json, submit_email=SUBMIT_EMAIL, site_url=SITE_URL)
    render('privacy.html', 'about/privacy.html', '../', active='', title='Privacy — BoxyTrucks', description='What BoxyTrucks collects, why, and who processes it: Google Analytics, the submission form, affiliate cookies and GitHub hosting.', credits='', crumbs=[('Privacy', 'about/privacy.html')])
    _ngens = sum(1 for _fs in pages for _gs, _pg in pages[_fs].items() if _pg)
    _nreps = sum(len((_pg or {}).get('repairs') or []) for _fs in pages for _pg in pages[_fs].values())
    render('about.html', 'about/index.html', '../', active='', title='About BoxyTrucks: how we research and make money', description='Who makes BoxyTrucks, how every guide is sourced, how best years are chosen, how we make money and how to send corrections.', credits='',
           crumbs=[('About', 'about/')], n_gens=_ngens, n_fams=len(fams), n_repairs=_nreps,
           jsonld=[{'@context': 'https://schema.org', '@type': 'AboutPage', 'name': 'About BoxyTrucks', 'url': SITE_URL + 'about/', 'mainEntity': {'@type': 'Organization', 'name': SITE_NAME, 'url': SITE_URL, 'email': 'boxytrucks@gmail.com', 'sameAs': [INSTAGRAM_URL]}}])
    render('disclaimer.html', 'about/disclaimer.html', '../', active='', title='Disclaimer — BoxyTrucks', description='BoxyTrucks specs, fluids and repair guides are for general information: verify against your manual or a qualified mechanic.', credits='', crumbs=[('Disclaimer', 'about/disclaimer.html')])
    render('cookies.html', 'about/cookies.html', '../', active='', title='Cookies — BoxyTrucks', description='The cookies BoxyTrucks sets (Google Analytics only), how long they last, and how to accept, refuse or change your choice.', credits='', crumbs=[('Cookies', 'about/cookies.html')])
    render('disclosure.html', 'about/affiliate-disclosure.html', '../', active='', title='Affiliate disclosure — BoxyTrucks', description='How BoxyTrucks uses affiliate links, including Amazon Associates, what we earn from them and why it never changes what we recommend.', credits='', crumbs=[('Affiliate disclosure', 'about/affiliate-disclosure.html')])
    render('newsletter_thanks.html', 'newsletter/thanks.html', '../', noindex=True, hide_newsletter=True, title='Check your inbox — BoxyTrucks', description='One more step: confirm your subscription to The Boxy Dispatch.', credits='')
    render('newsletter_welcome.html', 'newsletter/welcome.html', '../', noindex=True, track_event='newsletter_confirmed', hide_newsletter=True, title="You're in — BoxyTrucks", description='Welcome to The Boxy Dispatch, the monthly BoxyTrucks email.', credits='')
    render('submit_thanks.html', 'submit/thanks.html', '../', active='submit', noindex=True, track_event='rig_submission', hide_newsletter=True, title='Thanks — BoxyTrucks', description='Thanks for sending your rig to BoxyTrucks. We read every submission and will be in touch if we feature it.', credits='')

    render('404.html', '404.html', '', noindex=True, hide_newsletter=True, title='Not found — BoxyTrucks', description='That page took a wrong turn. Search the guides or pick a model family.', credits='')

    # site search index
    strip = lambda t: LINK_RE.sub(lambda m: m.group(3), str(t or ''))
    idx = []
    def add(kind, title, url, model, text):
        if not url.startswith('http'): url = pretty_path(url)
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
                add('Repair', r['title'], f'/repairs/{slug}/{gs}/{r["slug"]}/', model, r.get('symptoms', '') + ' ' + r.get('tools', ''))
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
    (SITE / 'search-index.json').write_text(confirm_plain(json.dumps(idx, ensure_ascii=False, separators=(',', ':'))))
    render('search.html', 'search/index.html', '../', active='search', title='Search — BoxyTrucks', description='Search model guides, repairs, owner questions, suppliers and resources.', credits='', noindex=True)

    from datetime import date
    today = date.today().isoformat()
    urls = sorted(set(SITEMAP))
    (SITE / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n' for u in urls) + '</urlset>\n')
    (SITE / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nDisallow: /submit/thanks/\n\nSitemap: {SITE_URL}sitemap.xml\n')

    # ---- llms.txt / llms-full.txt (regenerated from the data on every build, so CI keeps them current) ----
    def _t(x):
        return re.sub(r'\s+', ' ', LINK_RE.sub(lambda m: m.group(3), str(x or ''))).strip()
    def _txt(x):
        if isinstance(x, (list, tuple)):
            return ' '.join(_txt(i) for i in x)
        if isinstance(x, dict):
            return ' '.join(_txt(v) for v in x.values())
        return _t(x)
    gurl = lambda slug, g: SITE_URL + f'models/{slug}/{g}/'
    L = [f'# {SITE_NAME}', '',
         '> An enthusiast guide to boxy, body-on-frame 4x4s for hands-on owners: history, buying checks, '
         'DIY repairs with parts, service baselines, wheel and tire fitment, recalls, values and mods, '
         'one guide per generation. Facts are sourced on each page.', '',
         'Fluid specs, capacities and torque figures are general guidance: always verify against the factory '
         f'manual for the exact vehicle (see {SITE_URL}about/disclaimer/). Parts links may be affiliate links.', '',
         f'Full text of every model guide: {SITE_URL}llms-full.txt', '']
    for slug in FAMILY_ORDER:
        if slug not in fams: continue
        fam = fams[slug]
        L += [f'## {mlabel(fam["maker"], fam["name"])}', '',
              f'- [{mlabel(fam["maker"], fam["name"])} overview]({SITE_URL}models/{slug}/): {_t(fam["verdict"])}']
        for g in fam['generations']:
            p = pages[slug].get(g['slug'])
            if not p: continue
            L.append(f'- [{mlabel(fam["maker"], p["title"])} ({g.get("years", "")})]({gurl(slug, g["slug"])}): {_t(g["summary"])}')
        L.append('')
    L += ['## Site', '',
          f'- [Repair guides]({SITE_URL}repairs/): every DIY repair, by model',
          f'- [Instagram @boxytrucks]({INSTAGRAM_URL}): our posts and reader builds',
          f'- [Mods & builders]({SITE_URL}mods/): suppliers and builders, by model',
          f'- [Resources]({SITE_URL}resources/): YouTube, Instagram, forums and references, by model',
          f'- [For sale]({SITE_URL}for-sale/): AutoTempest and Bring a Trailer searches for every generation',
          f'- [Disclaimer]({SITE_URL}about/disclaimer/)', f'- [Privacy]({SITE_URL}about/privacy/)',
          f'- [Affiliate disclosure]({SITE_URL}about/affiliate-disclosure/)', '']
    (SITE / 'llms.txt').write_text('\n'.join(L))

    F = [f'# {SITE_NAME}: full model guides', '', f'Source: {SITE_URL} · generated {today}', '',
         'Verify every fluid, capacity and torque figure against the factory manual for the exact vehicle. '
         f'Disclaimer: {SITE_URL}about/disclaimer/', '']
    for slug in FAMILY_ORDER:
        if slug not in fams: continue
        fam = fams[slug]
        F += ['', f'# {mlabel(fam["maker"], fam["name"])} ({fam.get("years", "")})', f'URL: {SITE_URL}models/{slug}/', '',
              _txt(fam.get('intro', [])), '', f'Verdict: {_t(fam["verdict"])}']
        for g in fam['generations']:
            p = pages[slug].get(g['slug'])
            if not p: continue
            x = p.get('x') or {}
            F += ['', f'## {mlabel(fam["maker"], p["title"])} ({g.get("years", "")})', f'URL: {gurl(slug, g["slug"])}',
                  f'Codes: {", ".join(g.get("codes", []))}', '', f'Verdict: {_t(p.get("verdict"))}', '']
            for st in p.get('story', []):
                if st.get('heading'): F.append(f'### {_t(st["heading"])}')
                F += [_t(par) for par in st.get('paragraphs', [])] + ['']
            if p.get('plate'):
                F += ['### Data plate'] + [f'- {_t(i["k"]).title()}: {_t(i["v"])}' for i in p['plate']] + ['']
            if p.get('engineering'):
                F += ['### Engineering', _t(p.get('engineering_intro'))] + [f'- {_t(i["k"]).title()}: {_t(i["v"])}' + (f' ({_t(i["note"])})' if i.get('note') else '') for i in p['engineering']] + ['']
            if p.get('generations_table'):
                F += ['### Versions'] + ['- ' + ' · '.join(_t(v) for v in r.values() if v) for r in p['generations_table']] + ['']
            if x.get('timeline'):
                F += ['### Year-by-year'] + [f'- {_t(r["year"])}: {_t(r["change"])}' + (f' [{r["flag"]}]' if r.get('flag') in ('buy', 'avoid') else '') for r in x['timeline']] + ['']
            if x.get('capability'):
                F += ['### Capability'] + [f'- {_t(r["k"])}: {_t(r["v"])}' + (f' ({_t(r["note"])})' if r.get('note') else '') for r in x['capability']] + ['']
            fit = x.get('fitment') or {}
            if fit:
                F.append('### Wheels and tires')
                if fit.get('stock'): F.append(f'- Stock tires: {", ".join(fit["stock"])}')
                for k, v in (fit.get('wheel') or {}).items(): F.append(f'- {k.replace("_", " ").title()}: {_t(v)}')
                for r in fit.get('max_tire', []): F.append(f'- Biggest tire, {_t(r.get("lift"))} lift: {_t(r.get("size"))}' + (f' ({_t(r["note"])})' if r.get('note') else ''))
                F.append('')
            if p.get('buying_checks'):
                F += ['### Buying checks'] + [f'- {_t(c["head"])}: {_t(c["body"])}' for c in p['buying_checks']] + ['']
            if p.get('repairs'):
                F.append('### Common repairs')
                for r in p['repairs']:
                    F += [f'#### {_t(r["title"])}', f'Difficulty {_t(r.get("diff"))} · time {_t(r.get("time"))} · cost {_t(r.get("cost"))}',
                          f'Symptoms: {_t(r.get("symptoms"))}', f'Fix: {_txt(r.get("fix"))}', f'Tools: {_t(r.get("tools"))}', '']
            bs = p.get('baseline_service') or {}
            if bs.get('items'):
                F += ['### Baseline service', _t(bs.get('intro'))] + [f'- {_t(i["item"])}: {_t(i.get("spec"))}' + (f' · {_t(i["interval"])}' if i.get('interval') else '') + (f' ({_t(i["note"])})' if i.get('note') else '') for i in bs['items']] + ['']
            if p.get('faq'):
                F.append('### FAQ')
                for q in p['faq']: F += [f'Q: {_t(q["q"])}', f'A: {_t(q["a"])}', '']
            srcs = list(p.get('sources', [])) + list(x.get('sources', []))
            if srcs:
                F += ['### Sources'] + [f'- {_t(s_["name"])}: {s_["url"]}' for s_ in srcs if s_.get('url')] + ['']
    (SITE / 'llms-full.txt').write_text(confirm_plain(re.sub(r'\n{3,}', '\n\n', '\n'.join(F))))

    # IndexNow key file + per-page content hashes (CI compares them with the live site to ping only changed pages)
    import hashlib
    (SITE / f'{INDEXNOW_KEY}.txt').write_text(INDEXNOW_KEY)
    hashes = {}
    for u in sorted(set(SITEMAP)):
        f = SITE / (u[len(SITE_URL):] + 'index.html')
        if f.exists():
            body = re.sub(r'"dateModified": "[^"]*"', '', f.read_text())
            hashes[u] = hashlib.sha1(body.encode()).hexdigest()[:16]
    (SITE / 'page-hashes.json').write_text(json.dumps(hashes, indent=0))

    n = sum(1 for _ in SITE.rglob('*.html'))
    full = sum(len(v) for v in pages.values())
    stubs = sum(1 for f in fams.values() for g in f['generations'] if not g['has_page'])
    print(f'built {n} pages · full guides: {full} · overview-only: {stubs}')
    for f in sorted(DATA.rglob('*.json')):
        if re.search(r'archive\.org/(details|download)/', f.read_text()):
            print(f'  ! archive.org manual link in {f.relative_to(DATA)} (cite by name, no url)')
    ph = re.compile(r'\[(TO RESEARCH|TBD|TODO|PHOTO|OWNER|STORY|ONE-PARAGRAPH)[^\]]*\]')
    for f in sorted(SITE.rglob('*.html')):
        for m in ph.finditer(f.read_text()):
            print(f'  ! placeholder left in {f.relative_to(SITE)}: {m.group(0)[:60]}')
            break


if __name__ == '__main__':
    main()
