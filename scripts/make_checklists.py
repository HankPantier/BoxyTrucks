"""Make printable pre-purchase inspection checklists (PDF), one per generation.

Run locally after content changes:  python scripts/make_checklists.py
Writes site/checklists/<family>-<gen>.pdf (committed; CI doesn't need Playwright).
"""
import re, sys, html
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

OUT = ROOT / 'site' / 'checklists'
OUT.mkdir(parents=True, exist_ok=True)
plain = lambda t: html.escape(build.confirm_plain(build.LINK_PLAIN(t or '')))

CSS = """
@page { size: Letter; margin: 0.55in 0.6in; }
* { box-sizing: border-box; }
body { font-family: 'Helvetica Neue', Arial, sans-serif; color: #141513; font-size: 10.5pt; line-height: 1.42; margin: 0; }
.hd { display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 2px solid #141513; padding-bottom: 8px; margin-bottom: 14px; }
.brand { font-weight: 700; letter-spacing: .18em; font-size: 9pt; }
.brand span { color: #8A6A1F; }
.eyebrow { font-family: 'Courier New', monospace; font-size: 8pt; letter-spacing: .14em; color: #8A6A1F; text-transform: uppercase; }
h1 { font-size: 21pt; line-height: 1.1; margin: 4px 0 2px; letter-spacing: -.01em; }
h2 { font-size: 11pt; text-transform: uppercase; letter-spacing: .1em; margin: 16px 0 6px; border-bottom: 1px solid #c9c2b2; padding-bottom: 3px; }
.sub { color: #555; font-size: 9.5pt; margin: 0; }
ul.chk { list-style: none; margin: 0; padding: 0; }
ul.chk li { display: grid; grid-template-columns: 16px 1fr; gap: 8px; padding: 5px 0; border-bottom: 1px dotted #c9c2b2; break-inside: avoid; }
ul.chk li::before { content: ''; width: 11px; height: 11px; border: 1.3px solid #141513; margin-top: 2px; }
ul.chk b { display: block; }
.tl { width: 100%; border-collapse: collapse; font-size: 9.5pt; }
.tl td { padding: 4px 6px; border-bottom: 1px dotted #c9c2b2; vertical-align: top; }
.tl td.y { width: 80px; font-weight: 700; white-space: nowrap; }
.tl td.f { width: 70px; font-family: 'Courier New', monospace; font-size: 8pt; text-transform: uppercase; }
.f-buy { color: #2F5D3A; } .f-avoid { color: #9A2B1E; } .f-recall { color: #8A6A1F; }
.two { display: grid; grid-template-columns: 1fr 1fr; gap: 0 22px; }
.notes { height: 90px; border: 1px solid #c9c2b2; margin-top: 6px; }
.ft { margin-top: 16px; font-size: 8pt; color: #666; border-top: 1px solid #c9c2b2; padding-top: 6px; }
"""

def page_html(fam, g, p):
    x = p.get('x') or {}
    model = build.mlabel(fam['maker'], p['title'])
    out = [f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>',
           f'<div class="hd"><div><div class="eyebrow">Pre-purchase inspection checklist</div><h1>{html.escape(model)}</h1><p class="sub">{html.escape(g.get("years", ""))}{" · " + html.escape(" · ".join(g.get("codes", [])[:4])) if g.get("codes") else ""}</p></div>',
           '<div class="brand">BOXY<span>TRUCKS</span></div></div>']
    checks = p.get('buying_checks') or []
    if checks:
        out.append('<h2>Check before you buy</h2><ul class="chk">' + ''.join(f'<li><span><b>{plain(c.get("head"))}</b>{plain(c.get("body"))}</span></li>' for c in checks) + '</ul>')
    flagged = [t for t in (x.get('timeline') or []) if t.get('flag') in ('buy', 'avoid', 'recall')]
    if flagged:
        lab = {'buy': 'Sweet spot', 'avoid': 'Beware', 'recall': 'Recall'}
        out.append('<h2>Years to know</h2><table class="tl">' + ''.join(f'<tr><td class="y">{plain(t.get("year"))}</td><td class="f f-{t["flag"]}">{lab[t["flag"]]}</td><td>{plain(t.get("change"))}</td></tr>' for t in flagged) + '</table>')
    rc = (x.get('recalls') or {}).get('items') or []
    ident = (x.get('identify') or {}).get('items') or []
    if rc or ident:
        out.append('<div class="two">')
        if rc:
            out.append('<div><h2>Recalls to ask about</h2><ul class="chk">' + ''.join(f'<li><span><b>{plain(r.get("title"))}</b>{plain(r.get("years"))}{" · " + plain(r.get("ref")) if r.get("ref") else ""}</span></li>' for r in rc[:10]) + '</ul></div>')
        if ident:
            out.append('<div><h2>Is it the real thing?</h2><ul class="chk">' + ''.join(f'<li><span><b>{plain(i.get("head"))}</b>{plain(i.get("body"))}</span></li>' for i in ident[:6]) + '</ul></div>')
        out.append('</div>')
    out.append('<h2>Notes</h2><div class="notes"></div>')
    url = f'{build.SITE_URL}models/{fam["slug"]}/{g["slug"]}/'
    out.append(f'<div class="ft">From the full guide at {url}, with sources. Recalls follow the VIN: check at nhtsa.gov/recalls. General information only, not a professional inspection; see boxytrucks.com/about/disclaimer/. © BoxyTrucks</div></body></html>')
    return ''.join(out)

def main():
    fams, flagship, pages, resources = build.load()
    jobs = []
    for slug, fam in fams.items():
        for g in fam['generations']:
            p = pages.get(slug, {}).get(g['slug'])
            if p and p.get('buying_checks'):
                jobs.append((fam, g, p))
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page()
        for fam, g, p in jobs:
            pg.set_content(page_html(fam, g, p), wait_until='load')
            pg.pdf(path=str(OUT / f'{fam["slug"]}-{g["slug"]}.pdf'), format='Letter', print_background=True, margin={'top': '0.55in', 'bottom': '0.55in', 'left': '0.6in', 'right': '0.6in'})
        b.close()
    print(f'{len(jobs)} checklists written to {OUT}')

if __name__ == '__main__':
    main()
