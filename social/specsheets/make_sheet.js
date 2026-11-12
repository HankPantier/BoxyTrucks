// Renders a 1080x1350 (4:5) "spec sheet" post from a JSON file. Usage: node social/specsheets/make_sheet.js social/specsheets/<truck>.json
// Hero photo + two photo tiles, spec table, buy/avoid years, five checks, owner note. Licensed or Hank's own photos only; every fact comes from site data.
const fs = require('fs'), path = require('path'); const { chromium } = require('playwright');
const ROOT = path.resolve(__dirname, '..', '..');
const r = JSON.parse(fs.readFileSync(path.resolve(process.argv[2]), 'utf8'));
const esc = s => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;');
const img = p => 'data:image/jpeg;base64,' + fs.readFileSync(path.join(ROOT, p)).toString('base64');
const mark = `<svg viewBox="0 0 64 64" width="38"><path d="M1 1 H63 V63 H53 A13 13 0 0 0 27 63 H1 Z" fill="none" stroke="#B0915A" stroke-width="2.6"/><rect x="1" y="33" width="62" height="2.4" fill="#B0915A"/><circle cx="40" cy="63" r="9.5" fill="#B0915A"/><circle cx="40" cy="63" r="3.5" fill="#0E0F0E"/></svg>`;
const css = `*{box-sizing:border-box;margin:0}body{width:1080px;height:1350px;background:#0E0F0E;color:#F7F4EE;overflow:hidden;font-family:'Inter Tight',sans-serif;position:relative}
.mono{font-family:'IBM Plex Mono',monospace}
.hero{position:absolute;left:0;top:0;width:1080px;height:560px;background-size:cover}
.hero:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(14,15,14,.92) 0%,rgba(14,15,14,.55) 38%,rgba(14,15,14,0) 62%),linear-gradient(transparent 70%,#0E0F0E)}
.head{position:absolute;left:56px;top:48px;z-index:2;width:640px}
.brand{display:flex;align-items:center;gap:12px;font-weight:600;letter-spacing:.2em;font-size:17px}
.no{font-size:17px;letter-spacing:.24em;color:#C9A86A;margin-top:34px}
h1{font-size:150px;line-height:.9;letter-spacing:-.045em;font-weight:600;margin-top:10px}
.sub{font-size:27px;margin-top:14px;color:#E9E4DA;font-weight:500}
.tag{display:inline-block;white-space:nowrap;max-width:968px;padding-right:18px !important;margin-top:20px;padding:8px 14px;border:1.5px solid #C9A86A;color:#C9A86A;font-size:16px;letter-spacing:.16em}
.tiles{position:absolute;left:56px;right:56px;top:520px;display:grid;grid-template-columns:1fr 1fr;gap:16px;z-index:2}
.tile{height:132px;background-size:cover;position:relative;border:1px solid rgba(201,168,106,.35)}
.tile:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(14,15,14,.9) 0%,rgba(14,15,14,.35) 70%)}
.tile>div{position:absolute;left:18px;top:18px;right:120px;z-index:1}.tile .l{font-size:14px;letter-spacing:.22em;color:#C9A86A}
.tile .t{font-size:21px;line-height:1.2;font-weight:600;margin-top:8px}
.grid{position:absolute;left:56px;right:56px;top:676px;display:grid;grid-template-columns:1.08fr 1fr;gap:36px}
.h{font-size:15px;letter-spacing:.24em;color:#C9A86A;padding-bottom:10px;border-bottom:1.5px solid #C9A86A;margin-bottom:6px}
.spec{display:grid;grid-template-columns:172px 1fr;gap:10px;padding:8px 0;border-bottom:1px solid rgba(247,244,238,.12);font-size:19px;line-height:1.25}
.spec .k{color:#A8A296;font-size:15px;letter-spacing:.06em;padding-top:2px}.spec .v{font-weight:600}
.yr{display:grid;grid-template-columns:auto 1fr;gap:14px;align-items:start;padding:11px 0;border-bottom:1px solid rgba(247,244,238,.12)}
.badge{font-size:15px;letter-spacing:.14em;padding:5px 10px;border:1.5px solid;min-width:74px;text-align:center}
.yr b{display:block;font-size:24px;font-weight:600}.yr span{display:block;font-size:16px;line-height:1.3;color:#D9D3C6;margin-top:3px}
.chk{margin-top:14px}.chk ol{list-style:none;padding:0;counter-reset:c}
.chk li{counter-increment:c;display:grid;grid-template-columns:30px 1fr;font-size:17px;line-height:1.3;padding:6px 0;border-bottom:1px solid rgba(247,244,238,.12)}
.chk li:before{content:counter(c);font-family:'IBM Plex Mono',monospace;color:#C9A86A;font-size:16px}
.owner{position:absolute;left:56px;right:56px;bottom:84px;padding:14px 20px;border-left:3px solid #C9A86A;background:rgba(201,168,106,.08);font-size:19px;line-height:1.35}
.owner .l{font-size:14px;letter-spacing:.22em;color:#C9A86A;margin-bottom:6px}
.ft{position:absolute;left:56px;right:56px;bottom:30px;display:flex;align-items:flex-end;gap:24px;font-size:13px;line-height:1.35;color:#A8A296}.ft .cr{flex:1;min-width:0}
.ft .url{margin-left:auto;color:#C9A86A;font-size:18px;white-space:nowrap}`;
const page = `<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet"><style>${css}</style></head><body>
<div class="hero" style="background-image:url(${img(r.hero)});background-position:${r.hero_pos || '50% 50%'}"></div>
<div class="head"><div class="brand">${mark}<span>BOXY TRUCKS</span></div>
<div class="no mono">SPEC SHEET · ${esc(r.number)}</div><h1>${esc(r.title)}</h1><div class="sub">${esc(r.subtitle)}</div><div class="tag mono">${esc(r.tagline)}</div></div>
<div class="tiles">${r.tiles.map(t => `<div class="tile" style="background-image:url(${img(t.photo)});background-position:${t.pos || '50% 50%'}"><div><div class="l mono">${esc(t.label)}</div><div class="t">${esc(t.text)}</div></div></div>`).join('')}</div>
<div class="grid"><div><div class="h mono">SPECIFICATIONS</div>${r.specs.map(([k, v]) => `<div class="spec"><span class="k mono">${esc(k)}</span><span class="v">${esc(v)}</span></div>`).join('')}</div>
<div><div class="h mono">WHICH YEAR</div>
<div class="yr"><span class="badge mono" style="color:#6FAE80;border-color:#6FAE80">BUY</span><div><b>${esc(r.buy[0])}</b><span>${esc(r.buy[1])}</span></div></div>
${r.avoid ? `<div class="yr"><span class="badge mono" style="color:#D5684C;border-color:#D5684C">AVOID</span><div><b>${esc(r.avoid[0])}</b><span>${esc(r.avoid[1])}</span></div></div>` : ''}
<div class="chk"><div class="h mono">CHECK BEFORE YOU BUY</div><ol>${r.checks.map(c => `<li>${esc(c)}</li>`).join('')}</ol></div></div></div>
${r.owner ? `<div class="owner"><div class="l mono">${esc(r.owner_label || 'OWNER NOTE')}</div>${esc(r.owner)}</div>` : ''}
<div class="ft mono"><span class="cr">${esc(r.credit)}</span><span class="url">${esc(r.url_label)}</span></div></body></html>`;
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await pg.setContent(page); await pg.waitForTimeout(1200);
  // fit: shrink the tiles, then the table text, until the grid clears the owner note (or the footer)
  const over = await pg.evaluate(() => {
    const ov = () => { const g = document.querySelector('.grid').getBoundingClientRect().bottom, o = document.querySelector('.owner'); return o ? g - o.getBoundingClientRect().top + 14 : g - 1290; };
    const grid = document.querySelector('.grid'), tiles = document.querySelectorAll('.tile');
    // title: shrink until the header block clears the tiles; tagline: shrink until it fits one line
    const h = document.querySelector('h1'), head = document.querySelector('.head'), tag = document.querySelector('.tag');
    let hs = 150; while (head.getBoundingClientRect().bottom > 500 && hs > 84) { hs -= 6; h.style.fontSize = hs + 'px'; }
    let ts = 16; while (tag.scrollWidth > tag.clientWidth + 1 && ts > 11) { ts -= 1; tag.style.fontSize = ts + 'px'; tag.style.letterSpacing = '.1em'; }
    const ub = document.querySelector('.ft .url'); let us = 18; while (ub.getBoundingClientRect().width > 520 && us > 13) { us -= 1; ub.style.fontSize = us + 'px'; }
    let top = 676, th = 132, f = 1;
    while (ov() > 0 && th > 96) { th -= 6; top -= 6; tiles.forEach(t => t.style.height = th + 'px'); grid.style.top = top + 'px'; }
    while (ov() > 0 && f > 0.8) { f -= 0.03; document.querySelectorAll('.spec,.chk li,.yr span').forEach(e => { e.style.fontSize = ''; const fs = parseFloat(getComputedStyle(e).fontSize); e.style.fontSize = (fs * f / (f + 0.03)) + 'px'; e.style.paddingTop = e.style.paddingBottom = Math.round(7 * f) + 'px'; }); }
    return ov();
  });
  fs.mkdirSync(path.dirname(path.join(ROOT, r.image)), { recursive: true });
  await pg.screenshot({ path: path.join(ROOT, r.image), type: 'jpeg', quality: 90 }); console.log(r.image, over > 0 ? 'STILL OVERLAPS ' + Math.round(over) + 'px: shorten the text' : 'fits');
  await b.close();
})();
