// Spec-stack graphic (Hank, Nov 6, 2026): one band per truck, licensed photo + key specs, tied to a /compare/ page.
// Usage: node social/stacks/make_stack.js social/stacks/<spec>.json  ->  social/posts/stack-<slug>.jpg (1080x1350)
// Spec: {slug, eyebrow, title, url, trucks:[{name, years, photo, pos, credit, specs:[[icon,label,value],...]}]}
// Facts must come from data/compare/<slug>.json; photos only from the site's licensed page photos. No brand logos.
const fs = require('fs'), path = require('path'); const { chromium } = require('playwright');
const ROOT = path.resolve(__dirname, '..', '..'); const spec = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const esc = s => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;');
const img = p => 'data:image/jpeg;base64,' + fs.readFileSync(path.join(ROOT, p)).toString('base64');
const I = { // simple line icons, drawn here
  engine: '<path d="M4 9h3l2-2h6v2h3v2h2v4h-2v2h-3l-2 2H9l-2-2H4z"/>',
  power: '<path d="M13 3 5 14h6l-1 7 8-11h-6z"/>',
  gears: '<circle cx="6" cy="6" r="2"/><circle cx="12" cy="6" r="2"/><circle cx="18" cy="6" r="2"/><circle cx="6" cy="18" r="2"/><circle cx="12" cy="18" r="2"/><path d="M6 8v8M12 8v8M18 8v4H6"/>',
  axle: '<circle cx="5" cy="12" r="3"/><circle cx="19" cy="12" r="3"/><path d="M8 12h8M12 9v6"/>',
  lock: '<rect x="5" y="11" width="14" height="9" rx="1"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
  tow: '<path d="M3 16h11l3-5h3v5h1M6 19a2 2 0 1 0 0-.1M17 19a2 2 0 1 0 0-.1M14 16v-6"/>',
  tire: '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/>',
  price: '<path d="M12 3v18M16 7H10a3 3 0 0 0 0 6h4a3 3 0 0 1 0 6H8"/>',
};
const svg = k => `<svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="#C9A86A" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">${I[k] || I.engine}</svg>`;
const mark = `<svg viewBox="0 0 64 64" width="40"><path d="M1 1 H63 V63 H53 A13 13 0 0 0 27 63 H1 Z" fill="none" stroke="#B0915A" stroke-width="2.6"/><rect x="1" y="33" width="62" height="2.4" fill="#B0915A"/><circle cx="40" cy="63" r="9.5" fill="#B0915A"/><circle cx="40" cy="63" r="3.5" fill="#0E0F0E"/></svg>`;
const n = spec.trucks.length, bandH = Math.floor((1350 - 190 - 96) / n);
const css = `*{box-sizing:border-box;margin:0}body{width:1080px;height:1350px;background:#0E0F0E;color:#F7F4EE;overflow:hidden;font-family:'Inter Tight',sans-serif}
.hd{height:190px;padding:44px 56px 0}.ey{font-family:'IBM Plex Mono',monospace;font-size:20px;letter-spacing:.26em;color:#C9A86A;text-transform:uppercase}
h1{font-size:62px;line-height:1.02;letter-spacing:-.03em;font-weight:600;margin-top:14px}
.band{height:${bandH}px;display:grid;grid-template-columns:470px 1fr;border-top:1px solid rgba(201,168,106,.35)}
.ph{position:relative;background-size:cover}.cr{position:absolute;left:12px;bottom:8px;font-family:'IBM Plex Mono',monospace;font-size:12px;color:rgba(247,244,238,.9);text-shadow:0 1px 3px #000}
.inf{padding:26px 40px 0 36px}.nm{display:flex;align-items:baseline;gap:14px}.yr{font-family:'IBM Plex Mono',monospace;font-size:20px;padding:4px 10px;border:1px solid #C9A86A;color:#C9A86A}
.nm b{font-size:38px;letter-spacing:-.02em;font-weight:600}
.sp{margin-top:16px;display:grid;gap:${n > 2 ? 7 : 11}px}.r{display:grid;grid-template-columns:34px 1fr;gap:12px;align-items:center;font-size:${n > 2 ? 21 : 24}px;line-height:1.2;color:#E4DFD3}
.ft{position:absolute;left:56px;right:56px;bottom:30px;display:flex;align-items:center;gap:14px;font-weight:600;letter-spacing:.2em;font-size:20px}.url{margin-left:auto;font-family:'IBM Plex Mono',monospace;letter-spacing:.04em;font-weight:400;color:#C9A86A;font-size:22px}`;
const html = `<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet"><style>${css}</style></head><body>
<div class="hd"><div class="ey">${esc(spec.eyebrow)}</div><h1>${esc(spec.title)}</h1></div>
${spec.trucks.map(t => `<div class="band"><div class="ph" style="background-image:url(${img(t.photo)});background-position:${t.pos || '50% 50%'}"><div class="cr">${esc(t.credit)}</div></div>
<div class="inf"><div class="nm"><span class="yr">${esc(t.years)}</span><b>${esc(t.name)}</b></div><div class="sp">${t.specs.map(([k, v]) => `<div class="r">${svg(k)}<span>${esc(v)}</span></div>`).join('')}</div></div></div>`).join('')}
<div class="ft">${mark}<span>BOXY TRUCKS</span><span class="url">${esc(spec.url)}</span></div></body></html>`;
(async () => { const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await pg.setContent(html); await pg.waitForTimeout(1500); const out = `social/posts/stack-${spec.slug}.jpg`;
  await pg.screenshot({ path: path.join(ROOT, out), type: 'jpeg', quality: 90 }); await b.close(); console.log(out); })();
