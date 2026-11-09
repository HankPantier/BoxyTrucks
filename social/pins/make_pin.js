// Renders 1000x1500 (2:3) Pinterest pins from social/pins/queue.json rows. Usage: node social/pins/make_pin.js <id> [<id> ...]
// Photo top, dark panel with the facts, footer with the page URL. Licensed site photos only; text comes from the queue row.
const fs = require('fs'), path = require('path'); const { chromium } = require('playwright');
const ROOT = path.resolve(__dirname, '..', '..');
const rows = JSON.parse(fs.readFileSync(path.join(ROOT, 'social/pins/queue.json'), 'utf8'));
const esc = s => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;');
const img = p => 'data:image/jpeg;base64,' + fs.readFileSync(path.join(ROOT, p)).toString('base64');
const mark = `<svg viewBox="0 0 64 64" width="44"><path d="M1 1 H63 V63 H53 A13 13 0 0 0 27 63 H1 Z" fill="none" stroke="#B0915A" stroke-width="2.6"/><rect x="1" y="33" width="62" height="2.4" fill="#B0915A"/><circle cx="40" cy="63" r="9.5" fill="#B0915A"/><circle cx="40" cy="63" r="3.5" fill="#0E0F0E"/></svg>`;
const tag = { avoid: ['AVOID', '#C0533A'], buy: ['BUY', '#4E8B5F'], tire: ['', '#C9A86A'], check: ['', '#C9A86A'] };
const css = `*{box-sizing:border-box;margin:0}body{width:1000px;height:1500px;background:#0E0F0E;color:#F7F4EE;overflow:hidden;font-family:'Inter Tight',sans-serif;position:relative}
.ph{height:760px;background-size:cover;position:relative}.ph:after{content:"";position:absolute;inset:auto 0 0 0;height:160px;background:linear-gradient(transparent,#0E0F0E)}
.cr{position:absolute;right:16px;top:12px;font-family:'IBM Plex Mono',monospace;font-size:14px;color:rgba(247,244,238,.92);text-shadow:0 1px 3px #000;z-index:2}
.bd{padding:0 64px;margin-top:-40px;position:relative;z-index:2}.ey{font-family:'IBM Plex Mono',monospace;font-size:22px;letter-spacing:.26em;color:#C9A86A;text-transform:uppercase}
h1{font-size:80px;line-height:1.02;letter-spacing:-.03em;font-weight:600;margin-top:16px;text-wrap:balance}
.rows{margin-top:34px;display:grid;gap:18px}.r{display:grid;grid-template-columns:auto 1fr;gap:18px;align-items:start;border-top:1px solid rgba(201,168,106,.3);padding-top:16px}
.k{font-family:'IBM Plex Mono',monospace;font-size:24px;padding:6px 12px;border:1.5px solid;white-space:nowrap;min-width:120px;text-align:center}
.v b{display:block;font-size:40px;letter-spacing:-.01em;font-weight:600}.v span{display:block;font-size:27px;line-height:1.28;color:#D9D3C6;margin-top:4px}
.v.one b{font-size:40px}.ft{position:absolute;left:64px;right:64px;bottom:44px;display:flex;align-items:center;gap:14px;font-weight:600;letter-spacing:.2em;font-size:22px}
.url{margin-left:auto;font-family:'IBM Plex Mono',monospace;letter-spacing:.02em;font-weight:400;color:#C9A86A;font-size:22px;text-align:right}`;
const body = r => r.rows.map(([k, a, b]) => {
  const [lbl, col] = tag[k];
  if (k === 'avoid' || k === 'buy') return `<div class="r"><span class="k" style="color:${col};border-color:${col}">${lbl}</span><div class="v"><b>${esc(a)}</b><span>${esc(b)}</span></div></div>`;
  if (k === 'tire') return `<div class="r"><span class="k" style="color:${col};border-color:${col}">${esc(a)}</span><div class="v one"><b>${esc(b)}</b></div></div>`;
  return `<div class="r"><span class="k" style="color:${col};border-color:${col};min-width:70px">${esc(a)}</span><div class="v one"><b>${esc(b)}</b></div></div>`;
}).join('');
const page = r => `<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet"><style>${css}</style></head><body>
<div class="ph" style="background-image:url(${img(r.photo)});background-position:50% 55%"><div class="cr">${esc(r.credit)}</div></div>
<div class="bd"><div class="ey">${esc(r.eyebrow)}</div><h1>${esc(r.title)}</h1><div class="rows">${body(r)}</div></div>
<div class="ft">${mark}<span>BOXY TRUCKS</span><span class="url">${esc(r.url_label)}</span></div></body></html>`;
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1000, height: 1500 } });
  for (const id of process.argv.slice(2)) {
    const r = rows.find(x => x.id === id); if (!r) { console.log('missing', id); continue; }
    await pg.setContent(page(r)); await pg.waitForTimeout(900);
    // shrink the title until the panel fits above the footer
    await pg.evaluate(() => { const h = document.querySelector('h1'), ph = document.querySelector('.ph'); let s = 80, p = 760; const ok = () => document.querySelector('.rows').getBoundingClientRect().bottom < 1380; while (!ok() && s > 60) { s -= 4; h.style.fontSize = s + 'px'; } while (!ok() && p > 480) { p -= 40; ph.style.height = p + 'px'; } });
    await pg.screenshot({ path: path.join(ROOT, r.image), type: 'jpeg', quality: 88 }); console.log(r.image);
  }
  await b.close();
})();
