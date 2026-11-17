# Hook-style test Shorts (Nov 17, 2026): one surprising fact per Short, voiceover on every scene, real clips or slowly
# panning photos. Built after the YouTube Studio "Outliers in my niche" research (title patterns: price contrast,
# engineering quirk, question). Facts only from the site's data or Hank's own statements.
# Usage: VOICE=<en_US-joe-medium.onnx> python3 social/hooks/build_hook.py social/hooks/<name>.json <out.mp4>
import json, os, subprocess, sys, wave
from PIL import Image, ImageDraw, ImageFont, ImageFilter
SPEC = json.load(open(sys.argv[1])); OUT = sys.argv[2]
WORK = os.environ.get('WORK', '/tmp/hook-' + os.path.basename(sys.argv[1]).replace('.json', '')); os.makedirs(WORK, exist_ok=True)
VOICE = os.environ['VOICE']; W, H, FPS = 1080, 1920, 30
F = '/usr/share/fonts/opentype/inter/'
f_hook = ImageFont.truetype(F + 'InterDisplay-Bold.otf', 92); f_cap = ImageFont.truetype(F + 'InterDisplay-Bold.otf', 70)
f_eye = ImageFont.truetype(F + 'Inter-SemiBold.otf', 30); f_brand = ImageFont.truetype(F + 'Inter-Bold.otf', 30)
f_big = ImageFont.truetype(F + 'InterDisplay-Bold.otf', 100); f_body = ImageFont.truetype(F + 'Inter-Medium.otf', 44)
f_credit = ImageFont.truetype(F + 'Inter-Medium.otf', 24)
BRASS, INK, CREAM = (201, 168, 106), (14, 15, 14), (247, 244, 238)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run(c):
    r = subprocess.run(c, capture_output=True)
    if r.returncode: sys.exit(r.stderr.decode()[-1500:])


def tts(text, path):
    subprocess.run(['python3', '-m', 'piper', '-m', VOICE, '--length-scale', '1.0', '--noise-scale', '0.8', '--noise-w-scale', '1.0', '-f', path],
                   input=text.encode(), check=True, capture_output=True)
    with wave.open(path) as w: return w.getnframes() / w.getframerate()


def wrap(d, text, font, maxw):
    lines, cur = [], ''
    for w_ in text.split():
        t = (cur + ' ' + w_).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w_
    return lines + [cur]


def mark(d, x, y):
    d.rectangle([x, y, x + 34, y + 34], outline=BRASS, width=3); d.rectangle([x, y + 17, x + 34, y + 19], fill=BRASS)
    d.text((x + 48, y + 1), 'BOXY TRUCKS', font=f_brand, fill=CREAM)


def overlay(sc, first, path):
    """Top brand mark, a dark gradient behind the caption, the caption (big hook on scene 1), eyebrow and photo credit."""
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g = Image.new('L', (1, H)); [g.putpixel((0, y), int(max(0, (y - 1000) / 920) ** 1.1 * 235)) for y in range(H)]
    im.paste(Image.new('RGBA', (W, H), INK + (255,)), (0, 0), g.resize((W, H)))
    top = Image.new('L', (1, H)); [top.putpixel((0, y), int(max(0, (300 - y) / 300) * 160)) for y in range(H)]
    im.paste(Image.new('RGBA', (W, H), INK + (255,)), (0, 0), top.resize((W, H)))
    d = ImageDraw.Draw(im); mark(d, 64, 120)
    font, lh = (f_hook, 100) if first else (f_cap, 80)
    lines = wrap(d, sc['caption'], font, W - 150)
    y = 1440 - lh * (len(lines) - 1)
    if sc.get('eyebrow'): d.text((64, y - 58), sc['eyebrow'], font=f_eye, fill=BRASS)
    for l in lines: d.text((64, y), l, font=font, fill=CREAM); y += lh
    if sc.get('credit'): d.text((64, 1640), 'Photo: ' + sc['credit'], font=f_credit, fill=(170, 165, 155))
    im.save(path)


def endcard(path, bgsrc):
    bg = Image.open(os.path.join(ROOT, bgsrc)).convert('RGB'); s = max(W / bg.width, H / bg.height)
    bg = bg.resize((int(bg.width * s) + 1, int(bg.height * s) + 1)); l = (bg.width - W) // 2; bg = bg.crop((l, 0, l + W, H)).filter(ImageFilter.GaussianBlur(14))
    bg = Image.blend(bg, Image.new('RGB', (W, H), INK), 0.72); d = ImageDraw.Draw(bg); mark(d, 64, 120)
    y = 600
    for t in SPEC['end']['lines']: d.text((64, y), t, font=f_big, fill=CREAM); y += 112
    d.text((64, y + 50), SPEC['end']['sub'], font=f_body, fill=(217, 211, 198))
    d.text((64, y + 112), SPEC['end']['url'], font=f_body, fill=BRASS)
    d.text((64, y + 220), 'Follow for one boxy-truck fact a day.', font=f_body, fill=(217, 211, 198))
    d.text((64, 1640), 'Voiceover is AI-generated.', font=f_credit, fill=(170, 165, 155))
    bg.save(path)


parts, voices, t = [], [], 0.0
for i, sc in enumerate(SPEC['scenes']):
    vd = tts(sc['voice'], f'{WORK}/v{i}.wav') if sc.get('voice') else 0
    dur = round(max(vd + 0.45, sc.get('min', 2.0)), 3)
    overlay(sc, i == 0, f'{WORK}/o{i}.png')
    src = os.path.join(ROOT, sc['src']); tmp = f'{WORK}/p{i}.tmp.mp4'
    if sc['kind'] == 'clip':
        ss = sc.get('start', 0)
        if sc.get('fit'):  # whole frame over a blurred fill, so a passing truck stays in shot
            base = (f"[0:v]trim=start={ss}:duration={sc.get('max', dur)},setpts=PTS-STARTPTS,split[a0][b0];[a0]scale={W}:{H}:force_original_aspect_ratio=increase,"
                    f"crop={W}:{H},boxblur=30:2[bg0];[b0]scale={W}:-2[fg0];[bg0][fg0]overlay=0:(H-h)/2-260")
        else:
            base = f"[0:v]trim=start={ss}:duration={sc.get('max', dur)},setpts=PTS-STARTPTS,scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}"
        vf = base + f",fps={FPS},tpad=stop_mode=clone:stop_duration=20,trim=duration={dur}[b];[b][1:v]overlay=0:0,format=yuv420p[v]"
        af = f"[0:a]atrim=start={ss}:duration={sc.get('max', dur)},asetpts=PTS-STARTPTS,volume=0.3,apad,atrim=duration={dur},aresample=48000,aformat=channel_layouts=stereo[a]"
        run(['ffmpeg', '-y', '-v', 'error', '-i', src, '-loop', '1', '-i', f'{WORK}/o{i}.png', '-filter_complex', vf + ';' + af,
             '-map', '[v]', '-map', '[a]', '-t', f'{dur}', '-r', str(FPS), '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-c:a', 'aac', '-b:a', '160k', tmp])
    else:  # photo: fill the frame and pan slowly across it (fx = focus 0..1 across the width, pan = px over the scene)
        if sc.get('fit'):  # landscape frame shown whole over a blurred fill (pre-composed slightly oversize so it can still drift)
            src0 = Image.open(src).convert('RGB'); CW, CH = int(W * 1.08) // 2 * 2, int(H * 1.08) // 2 * 2
            k = max(CW / src0.width, CH / src0.height); bgf = src0.resize((int(src0.width * k) + 1, int(src0.height * k) + 1))
            l = (bgf.width - CW) // 2; bgf = bgf.crop((l, 0, l + CW, CH)).filter(ImageFilter.GaussianBlur(28))
            fg = src0.resize((CW, int(src0.height * CW / src0.width))); bgf.paste(fg, (0, (CH - fg.height) // 2 - 280))
            src = f'{WORK}/fit{i}.jpg'; bgf.save(src, quality=92)
        im = Image.open(src); scale = H * 1.12 / im.height; sw = int(im.width * scale) // 2 * 2; sh = int(H * 1.12) // 2 * 2
        fx = sc.get('fx', 0.5); pan = sc.get('pan', 120); x0 = max(0, min(sw - W, int(fx * sw - W / 2 - pan / 2)))
        x1 = max(0, min(sw - W, x0 + pan)); y0 = (sh - H) // 2
        vf = (f"[0:v]scale={sw}:{sh},fps={FPS},crop={W}:{H}:'{x0}+({x1}-{x0})*t/{dur}':'{y0}+{-40 if sc.get('rise') else 0}*t/{dur}'"
              f"[b];[b][1:v]overlay=0:0,format=yuv420p[v]")
        run(['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-framerate', str(FPS), '-i', src, '-loop', '1', '-i', f'{WORK}/o{i}.png',
             '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-filter_complex', vf, '-map', '[v]', '-map', '2:a', '-t', f'{dur}',
             '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-c:a', 'aac', '-b:a', '160k', tmp])
    os.replace(tmp, f'{WORK}/p{i}.mp4'); parts.append(f'{WORK}/p{i}.mp4')
    if sc.get('voice'): voices.append((t + 0.2, f'{WORK}/v{i}.wav'))
    t += dur

endcard(f'{WORK}/end.png', SPEC['end']['bg']); ed = round(tts(SPEC['end']['voice'], f'{WORK}/vend.wav') + 1.2, 3)
run(['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-framerate', str(FPS), '-i', f'{WORK}/end.png', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo',
     '-t', f'{ed}', '-vf', 'format=yuv420p', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-c:a', 'aac', '-b:a', '160k', f'{WORK}/pend.tmp.mp4'])
os.replace(f'{WORK}/pend.tmp.mp4', f'{WORK}/pend.mp4'); parts.append(f'{WORK}/pend.mp4'); voices.append((t + 0.2, f'{WORK}/vend.wav')); t += ed
open(f'{WORK}/list.txt', 'w').write(''.join(f"file '{p}'\n" for p in parts))
run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', f'{WORK}/list.txt', '-c', 'copy', f'{WORK}/body.mp4'])
ins = ['-i', f'{WORK}/body.mp4']; fl = []
for k, (st, p) in enumerate(voices):
    ins += ['-i', p]; fl.append(f'[{k+1}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={int(st*1000)}|{int(st*1000)},volume=1.6[v{k}]')
fl.append('[0:a]' + ''.join(f'[v{k}]' for k in range(len(voices))) + f'amix=inputs={len(voices)+1}:duration=first:normalize=0,alimiter=limit=0.95[a]')
run(['ffmpeg', '-y', '-v', 'error', *ins, '-filter_complex', ';'.join(fl), '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k',
     '-movflags', '+faststart', OUT + '.tmp.mp4'])
os.replace(OUT + '.tmp.mp4', OUT)
print(OUT, f'{t:.1f}s')
