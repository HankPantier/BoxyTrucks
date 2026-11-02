// Usage: node social/reels/make_reel.js social/reels/<spec>.json  ->  social/posts/<out>.mp4
// Spec: {out, fps, credit, scenes:[{photo, pos:"50% 50%", zoom:[1.05,1.18], dur, eyebrow, title, body, cta:true}]}
const fs = require('fs'), path = require('path'), { execFileSync } = require('child_process');
const { chromium } = require('playwright');
const ROOT = path.resolve(__dirname, '..', '..');
const spec = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const fps = spec.fps || 30, W = 1080, H = 1920, FADE = 0.45;
const esc = s => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;');
const img = p => 'data:image/jpeg;base64,' + fs.readFileSync(path.join(ROOT, p)).toString('base64');
const mark = `<svg viewBox="0 0 64 64" width="64"><path d="M1 1 H63 V63 H53 A13 13 0 0 0 27 63 H1 Z" fill="none" stroke="#B0915A" stroke-width="2.6"/><rect x="1" y="33" width="62" height="2.4" fill="#B0915A"/><circle cx="40" cy="63" r="9.5" fill="#B0915A"/><circle cx="40" cy="63" r="3.5" fill="#0E0F0E"/></svg>`;
let t0 = 0;
const scenes = spec.scenes.map(s => { const o = { ...s, start: t0 }; t0 += s.dur; return o; });
const total = t0;
const html = `<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600&family=Newsreader:opsz,wght@6..72,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>*{box-sizing:border-box;margin:0}body{width:${W}px;height:${H}px;background:#0E0F0E;color:#F7F4EE;overflow:hidden;position:relative;font-family:'Inter Tight','Inter',sans-serif}
.sc{position:absolute;inset:0;opacity:0}.ph{position:absolute;inset:0;background-size:cover;will-change:transform}
.sh{position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,15,14,.35) 0%,rgba(14,15,14,0) 22%,rgba(14,15,14,0) 42%,rgba(14,15,14,.82) 68%,#0E0F0E 100%)}
.tx{position:absolute;left:80px;right:80px;bottom:300px}
.ey{font-family:'IBM Plex Mono',monospace;font-size:30px;letter-spacing:.24em;color:#C9A86A;text-transform:uppercase}
h1{font-size:104px;line-height:.98;letter-spacing:-.035em;font-weight:600;margin-top:24px;text-wrap:balance}
.bd{font-family:'Newsreader',Georgia,serif;font-size:44px;line-height:1.38;color:#E4DFD3;margin-top:28px}
.cta h1{font-size:92px}.brand{position:absolute;left:80px;right:80px;bottom:150px;display:flex;align-items:center;gap:20px;font-weight:600;letter-spacing:.2em;font-size:30px}
.url{margin-left:auto;font-family:'IBM Plex Mono',monospace;letter-spacing:0;font-weight:400;font-size:30px;color:#E4DFD3}
.cr{position:absolute;left:80px;right:80px;bottom:78px;font-family:'IBM Plex Mono',monospace;font-size:20px;color:rgba(228,223,211,.7)}
.top .tx{top:230px;bottom:auto}.top .sh{background:linear-gradient(0deg,rgba(14,15,14,.85) 0%,rgba(14,15,14,0) 22%,rgba(14,15,14,0) 50%,rgba(14,15,14,.85) 75%,#0E0F0E 100%)}
.bar{position:absolute;left:0;top:0;height:6px;background:#C9A86A}</style></head><body>
${scenes.map((s, i) => `<div class="sc${s.cta ? ' cta' : ''}${s.align === 'top' ? ' top' : ''}" id="s${i}"><div class="ph" style="background-image:url(${img(s.photo)});background-position:${s.pos || '50% 50%'};transform-origin:${s.origin || '50% 50%'}"></div><div class="sh"></div>
<div class="tx">${s.eyebrow ? `<div class="ey">${esc(s.eyebrow)}</div>` : ''}${s.title ? `<h1>${esc(s.title)}</h1>` : ''}${s.body ? `<p class="bd">${esc(s.body)}</p>` : ''}</div></div>`).join('')}
<div class="brand">${mark}<span>BOXY TRUCKS</span><span class="url">${esc(spec.url || 'boxytrucks.com')}</span></div>
<div class="cr">${esc(spec.credit || '')}</div><div class="bar" id="bar"></div>
<script>const S=${JSON.stringify(scenes.map(s => ({ start: s.start, dur: s.dur, zoom: s.zoom || [1.04, 1.16] })))},T=${total},F=${FADE};
const ease=x=>x<0?0:x>1?1:1-Math.pow(1-x,3);
window.render=t=>{S.forEach((s,i)=>{const el=document.getElementById('s'+i),l=t-s.start;
let o=0;if(l>=-F&&l<s.dur){o=l<0?1+l/F:1;} if(i===0&&l<0)o=0; if(i===0&&l>=0&&l<F*0.6)o=1;
el.style.opacity=Math.max(0,Math.min(1,o));const p=Math.max(0,Math.min(1,(l+F)/(s.dur+F)));
el.querySelector('.ph').style.transform='scale('+(s.zoom[0]+(s.zoom[1]-s.zoom[0])*p)+')';
[...el.querySelectorAll('.ey,h1,.bd')].forEach((n,k)=>{const a=i===0?1:ease((l-0.15-k*0.22)/0.5);n.style.opacity=a;n.style.transform='translateY('+(30*(1-a))+'px)';});});
document.getElementById('bar').style.width=(100*t/T)+'%';};</script></body></html>`;
(async () => {
  const tmp = fs.mkdtempSync('/tmp/reel-');
  fs.writeFileSync(path.join(tmp, 'r.html'), html);
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: W, height: H } });
  await pg.goto('file://' + path.join(tmp, 'r.html')); await pg.waitForTimeout(2500);
  const n = Math.round(total * fps);
  for (let f = 0; f < n; f++) { await pg.evaluate(t => window.render(t), f / fps); await pg.screenshot({ path: path.join(tmp, 'f' + String(f).padStart(5, '0') + '.jpg'), type: 'jpeg', quality: 88 }); }
  await b.close();
  const out = path.join(ROOT, spec.out);
  // Capped bitrate keeps a ~26s Reel under 10 MB, the browser-upload limit for Instagram, X, TikTok, YouTube and Pinterest.
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(fps), '-i', path.join(tmp, 'f%05d.jpg'), '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-shortest', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-crf', '22', '-maxrate', '3200k', '-bufsize', '6400k', '-c:a', 'aac', '-b:a', '96k', '-movflags', '+faststart', out]);
  const cover = out.replace(/\.mp4$/, '-cover.jpg'); fs.copyFileSync(path.join(tmp, 'f' + String(Math.round(1.6 * fps)).padStart(5, '0') + '.jpg'), cover);
  fs.rmSync(tmp, { recursive: true, force: true });
  console.log('wrote', out, total + 's', n + ' frames');
})();
