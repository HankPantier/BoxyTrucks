# Builds the Riverhouse Defender 110 reader-rig Short (Nov 20, 2026) from the two clips Riverhouse sent of this truck
# (IMG_9336 exterior, IMG_9340 interior; 1080x1920 proxies) plus three of their listing photos.
# Usage: python3 social/rigs/riverhouse-110/build.py <clips dir> <voice wav dir> <out.mp4>
# Voice: Piper en_US-joe-medium (voice B, see social/voice/README.md), settings 1.0 / 0.8 / 1.0. Lines are in VOICE below;
# facts only from Riverhouse's submission and listing (data/rigs/riverhouse-110.json) and our Defender guide.
import os, subprocess, sys, wave
from PIL import Image, ImageDraw, ImageFont, ImageFilter

CLIPS, VDIR, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
IMG = f'{ROOT}/site/img/rigs/riverhouse-110/riverhouse-110-'
WORK = os.environ.get('WORK', '/tmp/rhwork'); os.makedirs(WORK, exist_ok=True)
W, H = 1080, 1920
F = '/usr/share/fonts/opentype/inter/'
f_title = ImageFont.truetype(F + 'InterDisplay-Bold.otf', 84)
f_eye = ImageFont.truetype(F + 'Inter-SemiBold.otf', 30)
f_brand = ImageFont.truetype(F + 'Inter-Bold.otf', 30)
f_big = ImageFont.truetype(F + 'InterDisplay-Bold.otf', 100)
f_body = ImageFont.truetype(F + 'Inter-Medium.otf', 44)
BRASS, BONE = (201, 168, 106), (247, 244, 238)

VOICE = [
 "So this is a nineteen ninety-seven Defender one-ten, in Arles Blue. Riverhouse Land Rover in the Netherlands sent it in.",
 "It's a matching-numbers truck out of southern Spain, and it still has the three hundred T D I. That's the simple, mechanical diesel most people want.",
 "Underneath, the axle ends were rebuilt with new hubs, bearings, brakes, shocks and springs.",
 "Inside? Nine seats, heated fronts, new air conditioning, and Apple CarPlay. In a Defender. Honestly? We'll allow it.",
 "It's old enough to import to the U S, and yes, it's for sale. The full story is up on boxy trucks dot com.",
]
# (kind, sources, eyebrow, on-screen title); a clip source is (name, start seconds)
SEG = [
 ('clip', ('IMG_9336', 0.0), 'SHOW US YOUR RIG · RIVERHOUSE LAND ROVER', '1997 Defender 110 in Arles Blue'),
 ('photo', ['side-profile', '300tdi-engine'], 'THE ENGINE', 'Matching-numbers 300Tdi, new timing belt'),
 ('photo', ['rear-axle-brakes'], 'UNDERNEATH', 'Axle ends rebuilt. New brakes, shocks and springs.'),
 ('clip', ('IMG_9340', 1.5), 'INSIDE', 'Nine seats, heated fronts, AC and CarPlay'),
]

def run(c): subprocess.run(c, check=True, capture_output=True)
def wavlen(p):
    with wave.open(p) as w: return w.getnframes() / w.getframerate()
def wrap(d, text, font, maxw):
    lines, cur = [], ''
    for w_ in text.split():
        t = (cur + ' ' + w_).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w_
    return lines + [cur]
def mark(d, x, y):
    d.rectangle([x, y, x + 34, y + 34], outline=BRASS, width=3); d.rectangle([x, y + 17, x + 34, y + 19], fill=BRASS)
    d.text((x + 48, y + 1), 'BOXY TRUCKS', font=f_brand, fill=BONE)

def overlay(eye, title, path, credit=True):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g = Image.new('L', (1, H)); [g.putpixel((0, y), int(max(0, (y - 980) / 760) ** 1.05 * 245)) for y in range(H)]
    im.paste(Image.new('RGBA', (W, H), (14, 15, 14, 255)), (0, 0), g.resize((W, H)))
    top = Image.new('L', (1, H)); [top.putpixel((0, y), int(max(0, (260 - y) / 260) * 150)) for y in range(H)]
    im.paste(Image.new('RGBA', (W, H), (14, 15, 14, 255)), (0, 0), top.resize((W, H)))
    d = ImageDraw.Draw(im); mark(d, 64, 120)
    lines = wrap(d, title, f_title, W - 128 - 110); y = 1400 - 92 * (len(lines) - 1)   # keep clear of the Shorts buttons on the right
    d.text((64, y - 58), eye, font=f_eye, fill=BRASS)
    for l in lines: d.text((64, y), l, font=f_title, fill=BONE); y += 92
    if credit: d.text((64, y + 26), 'Footage and photos: Riverhouse Land Rover', font=f_eye, fill=(190, 184, 172))
    im.save(path)

def still(name, path):
    # landscape listing photo shown whole: blurred, darkened copy behind, sharp photo across the middle
    ph = Image.open(IMG + name + '.jpg').convert('RGB')
    bg = ph.resize((int(ph.width * H / ph.height), H)).crop((0, 0, W, H)) if False else ph.resize((2560, 1920))
    bg = bg.crop(((2560 - W) // 2, 0, (2560 - W) // 2 + W, H)).filter(ImageFilter.GaussianBlur(24))
    bg = Image.blend(bg, Image.new('RGB', (W, H), (14, 15, 14)), 0.55)
    fg = ph.resize((W, int(ph.height * W / ph.width)), Image.LANCZOS); bg.paste(fg, (0, 330)); bg.save(path, quality=95)

def endcard(path):
    ph = Image.open(IMG + 'rear-three-quarter.jpg').convert('RGB').resize((2560, 1920))
    bg = ph.crop((700, 0, 700 + W, H)).filter(ImageFilter.GaussianBlur(14))
    bg = Image.blend(bg, Image.new('RGB', (W, H), (14, 15, 14)), 0.7); d = ImageDraw.Draw(bg); mark(d, 64, 120)
    y = 560
    for l in ['Old enough', 'to import.', 'And yes,', "it's for sale."]: d.text((64, y), l, font=f_big, fill=BONE); y += 112
    d.text((64, y + 40), '1997 Defender 110 300Tdi · Riverhouse Land Rover', font=f_eye, fill=BRASS)
    d.text((64, y + 130), 'Full story and photos:', font=f_body, fill=(217, 211, 198))
    d.text((64, y + 190), 'boxytrucks.com/field-notes', font=f_body, fill=BRASS)
    d.text((64, y + 290), 'Got a boxy truck? Show us your rig.', font=f_body, fill=(217, 211, 198))
    d.text((64, y + 350), 'boxytrucks.com/submit', font=f_body, fill=BRASS)
    bg.save(path)

enc = ['-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-c:a', 'aac', '-b:a', '160k', '-ar', '48000', '-ac', '2']
parts, voices, t = [], [], 0.0
for i, (kind, src, eye, title) in enumerate(SEG):
    dur = wavlen(f'{VDIR}/v{i}.wav') + 0.5
    overlay(eye, title, f'{WORK}/o{i}.png')
    if kind == 'clip':
        name, ss = src
        probe = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'{CLIPS}/{name}.mp4'], capture_output=True, text=True).stdout)
        mx = min(dur, probe - ss - 0.05); speed = max(0.5, min(1.0, mx / dur))   # slow the clip if the line outlasts the footage
        vf = (f"[0:v]trim=start={ss}:duration={mx},setpts=(PTS-STARTPTS)/{speed},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps=30,"
              f"tpad=stop_mode=clone:stop_duration=10,trim=duration={dur:.3f}[b];[b][1:v]overlay=0:0,format=yuv420p[v]")
        af = f"[0:a]atrim=start={ss}:duration={mx},asetpts=PTS-STARTPTS,atempo={speed},volume=0.2,apad,atrim=duration={dur:.3f}[a]"
        run(['ffmpeg', '-y', '-v', 'error', '-i', f'{CLIPS}/{name}.mp4', '-loop', '1', '-i', f'{WORK}/o{i}.png', '-filter_complex', vf + ';' + af,
             '-map', '[v]', '-map', '[a]', '-t', f'{dur:.3f}', *enc, f'{WORK}/p{i}.mp4'])
        parts.append(f'{WORK}/p{i}.mp4')
    else:
        each = dur / len(src)
        for k, name in enumerate(src):
            still(name, f'{WORK}/s{i}_{k}.jpg'); n = int(each * 30) + 1
            vf = (f"[0:v]scale={W*2}:{H*2},zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih*0.36-(ih/zoom*0.36)':d={n}:s={W}x{H}:fps=30[b];"
                  f"[b][1:v]overlay=0:0,format=yuv420p[v]")
            run(['ffmpeg', '-y', '-v', 'error', '-i', f'{WORK}/s{i}_{k}.jpg', '-loop', '1', '-i', f'{WORK}/o{i}.png', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo',
                 '-filter_complex', vf, '-map', '[v]', '-map', '2:a', '-t', f'{each:.3f}', *enc, f'{WORK}/p{i}_{k}.mp4'])
            parts.append(f'{WORK}/p{i}_{k}.mp4')
    voices.append((t + 0.25, f'{VDIR}/v{i}.wav')); t += dur

endcard(f'{WORK}/end.png'); ed = wavlen(f'{VDIR}/v4.wav') + 0.9
run(['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-i', f'{WORK}/end.png', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-t', f'{ed:.3f}',
     '-vf', 'fps=30,format=yuv420p', *enc, f'{WORK}/pend.mp4'])
parts.append(f'{WORK}/pend.mp4'); voices.append((t + 0.25, f'{VDIR}/v4.wav')); t += ed

open(f'{WORK}/list.txt', 'w').write(''.join(f"file '{p}'\n" for p in parts))
run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', f'{WORK}/list.txt', '-c:v', 'libx264', '-preset', 'medium', '-crf', '21', '-c:a', 'aac', '-b:a', '160k', f'{WORK}/body.mp4'])
ins = ['-i', f'{WORK}/body.mp4']; fl = []
for k, (st, p) in enumerate(voices):
    ins += ['-i', p]; fl.append(f'[{k+1}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={int(st*1000)}|{int(st*1000)},volume=1.6[v{k}]')
fl.append('[0:a]' + ''.join(f'[v{k}]' for k in range(len(voices))) + f'amix=inputs={len(voices)+1}:duration=first:normalize=0,alimiter=limit=0.95[a]')
run(['ffmpeg', '-y', '-v', 'error', *ins, '-filter_complex', ';'.join(fl), '-map', '0:v', '-map', '[a]', '-c:v', 'libx264', '-preset', 'slow', '-b:v', '1550k', '-maxrate', '2400k', '-bufsize', '4800k', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', OUT])
print(OUT, f'{t:.1f}s')
