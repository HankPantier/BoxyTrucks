// Usage: node social/carousels/make_carousel.js social/carousels/<spec>.json -> social/posts/<prefix>-N.jpg (1080x1350)
// Single image: give one slide, no end, and footer_url (shown instead of the page count).
// Spec: {prefix, footer_url?, cover?: existing image path used as slide 1, slides:[{photo,pos,credit,eyebrow,title,body,tag}], end:{title,body,url}}
const fs = require('fs'), path = require('path'); const { chromium } = require('playwright');
const ROOT = path.resolve(__dirname, '..', '..'); const spec = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const esc = s => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;');
const img = p => 'data:image/jpeg;base64,' + fs.readFileSync(path.join(ROOT, p)).toString('base64');
const mark = `<svg viewBox="0 0 64 64" width="44"><path d="M1 1 H63 V63 H53 A13 13 0 0 0 27 63 H1 Z" fill="none" stroke="#B0915A" stroke-width="2.6"/><rect x="1" y="33" width="62" height="2.4" fill="#B0915A"/><circle cx="40" cy="63" r="9.5" fill="#B0915A"/><circle cx="40" cy="63" r="3.5" fill="#0E0F0E"/></svg>`;
const css = `*{box-sizing:border-box;margin:0}body{width:1080px;height:1350px;background:#0E0F0E;color:#F7F4EE;overflow:hidden;position:relative;font-family:'Inter Tight','Inter',sans-serif}
.ph{position:absolute;left:0;right:0;top:0;height:860px;background-size:cover}.ph:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,15,14,0) 45%,rgba(14,15,14,.75) 80%,#0E0F0E 100%)}
.cr{position:absolute;top:16px;right:20px;font-family:'IBM Plex Mono',monospace;font-size:14px;color:rgba(247,244,238,.85);text-shadow:0 1px 3px rgba(0,0,0,.7)}
.tx{position:absolute;left:64px;right:64px;top:730px}.ey{font-family:'IBM Plex Mono',monospace;font-size:22px;letter-spacing:.26em;color:#C9A86A;text-transform:uppercase}
h1{font-size:84px;line-height:1;letter-spacing:-.03em;font-weight:600;margin-top:20px;text-wrap:balance}.bd{font-family:'Newsreader',Georgia,serif;font-size:34px;line-height:1.42;color:#E4DFD3;margin-top:24px}
.tag{display:inline-block;margin-top:22px;font-family:'IBM Plex Mono',monospace;font-size:20px;letter-spacing:.18em;padding:8px 14px;border:1px solid #4E6B58;background:#22302A;text-transform:uppercase}
.ft{position:absolute;left:64px;right:64px;bottom:44px;display:flex;align-items:center;gap:16px;font-weight:600;letter-spacing:.2em;font-size:22px}.pg{margin-left:auto;font-family:'IBM Plex Mono',monospace;letter-spacing:.1em;font-weight:400;color:#B9B3A6}
.end{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 80px;gap:28px;border:2px solid rgba(201,168,106,.35);margin:40px}.end h1{font-size:96px}.url{font-family:'IBM Plex Mono',monospace;font-size:30px;color:#C9A86A}`;
const head = `<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600&family=Newsreader:opsz,wght@6..72,400&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet"><style>${css}</style></head><body>`;
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  const out = []; let n = 1; const total = (spec.cover ? 1 : 0) + spec.slides.length + (spec.end ? 1 : 0);
  if (spec.cover) { const dst = `social/posts/${spec.prefix}-1.jpg`; fs.copyFileSync(path.join(ROOT, spec.cover), path.join(ROOT, dst)); out.push(dst); n++; }
  const shot = async (body) => { await pg.setContent(head + body + '</body></html>'); await pg.waitForTimeout(1500); const dst = `social/posts/${spec.prefix}-${n}.jpg`; await pg.screenshot({ path: path.join(ROOT, dst), type: 'jpeg', quality: 90 }); out.push(dst); n++; };
  for (const s of spec.slides) await shot(`<div class="ph" style="background-image:url(${img(s.photo)});background-position:${s.pos || '50% 50%'}"></div><div class="cr">${esc(s.credit)}</div>
    <div class="tx"><div class="ey">${esc(s.eyebrow)}</div><h1>${esc(s.title)}</h1>${s.body ? `<p class="bd">${esc(s.body)}</p>` : ''}${s.tag ? `<span class="tag">${esc(s.tag)}</span>` : ''}</div>
    <div class="ft">${mark}<span>BOXY TRUCKS</span><span class="pg">${spec.footer_url ? esc(spec.footer_url) : `${n} / ${total}`}</span></div>`);
  if (spec.end) await shot(`<div class="end"><div class="ey">${esc(spec.end.eyebrow || 'Save this')}</div><h1>${esc(spec.end.title)}</h1><p class="bd">${esc(spec.end.body)}</p><div class="url">${esc(spec.end.url)}</div></div>
    <div class="ft">${mark}<span>BOXY TRUCKS</span><span class="pg">${spec.footer_url ? esc(spec.footer_url) : `${n} / ${total}`}</span></div>`);
  await b.close(); console.log(JSON.stringify(out));
})();
