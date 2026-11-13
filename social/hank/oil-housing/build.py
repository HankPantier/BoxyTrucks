# Builds the G500 oil filter housing gasket Short from Hank's clips (Nov 13, 2026).
# Usage: python3 social/hank/oil-housing/build.py <clips dir> <out.mp4>
# Voice: Piper TTS (en_US-ryan-high) at $VOICE; facts only from data/g-class.json (repairs[1], baseline_service, owner_notes).
import json, os, subprocess, sys, wave
from PIL import Image, ImageDraw, ImageFont, ImageFilter

CLIPS, OUT = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.environ.get('WORK', '/tmp/oilwork'); os.makedirs(WORK, exist_ok=True)
VOICE = os.environ['VOICE']
W, H = 1080, 1920
F = '/usr/share/fonts/opentype/inter/'
f_title = ImageFont.truetype(F + 'InterDisplay-Bold.otf', 84)
f_eye = ImageFont.truetype(F + 'Inter-SemiBold.otf', 30)
f_brand = ImageFont.truetype(F + 'Inter-Bold.otf', 30)
f_big = ImageFont.truetype(F + 'InterDisplay-Bold.otf', 104)
f_body = ImageFont.truetype(F + 'Inter-Medium.otf', 44)
BRASS = (201, 168, 106)

# (clip, start, max_len, eyebrow, on-screen title, voice line)
SEG = [
 ('IMG_0625', 0.0, 7.6, "HANK'S 2007 G 500 · M113 V8", 'Its biggest leak: the oil filter housing',
  "The biggest issue on Hank's 2007 G 500: the oil filter housing gasket. Here's the fix."),
 ('IMG_0625', 7.6, 7.7, 'THE SYMPTOM', 'Oil pooling at the front of the V',
  "If oil is pooling at the front of the V and running down onto the belt, start here."),
 ('IMG_0626', 0.0, 6.0, 'STEP 1', 'Housing off. Clean both faces.',
  "Pull the intake ducting, unbolt the housing, and clean both mating faces completely."),
 ('IMG_0628', 0.0, 8.0, 'STEP 2', 'New seals: filter housing and oil cooler',
  "New seals in the housing and the oil cooler ports. Use genuine Mercedes or Elring."),
 ('IMG_0633', 0.0, 6.8, 'STEP 3', 'Torque it down, fresh filter',
  "Torque it to the factory figures and fit a fresh filter. The cap takes a 74 millimeter, 14 flute wrench."),
 ('IMG_0634', 0.0, 1.5, 'STEP 4', 'New drain plug and washer, fresh oil',
  "New drain plug and washer, then fresh MB 229.5 oil. About eight and a half quarts with the filter."),
]
END_VOICE = "A simple, inexpensive fix. It just takes some time. Parts list and the full how to are on boxy trucks dot com."

def run(c): subprocess.run(c, check=True, capture_output=True)

def tts(text, path):
    subprocess.run(['python3', '-m', 'piper', '-m', VOICE, '--length-scale', '0.92', '-f', path], input=text.encode(), check=True, capture_output=True)
    with wave.open(path) as w: return w.getnframes() / w.getframerate()

def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ''
    for w_ in words:
        t = (cur + ' ' + w_).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w_
    return lines + [cur]

def mark(d, x, y):
    d.rectangle([x, y, x + 34, y + 34], outline=BRASS, width=3); d.rectangle([x, y + 17, x + 34, y + 19], fill=BRASS)
    d.text((x + 48, y + 1), 'BOXY TRUCKS', font=f_brand, fill=(247, 244, 238))

def overlay(eye, title, path):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    g = Image.new('L', (1, H)); [g.putpixel((0, y), int(max(0, (y - 1150) / 770) ** 1.2 * 235)) for y in range(H)]
    im.paste(Image.new('RGBA', (W, H), (14, 15, 14, 255)), (0, 0), g.resize((W, H)))
    top = Image.new('L', (1, H)); [top.putpixel((0, y), int(max(0, (260 - y) / 260) * 150)) for y in range(H)]
    im.paste(Image.new('RGBA', (W, H), (14, 15, 14, 255)), (0, 0), top.resize((W, H)))
    d = ImageDraw.Draw(im); mark(d, 64, 120)
    lines = wrap(d, title, f_title, W - 128); y = 1420 - 92 * (len(lines) - 1)
    d.text((64, y - 58), eye, font=f_eye, fill=BRASS)
    for l in lines: d.text((64, y), l, font=f_title, fill=(247, 244, 238)); y += 92
    im.save(path)

def endcard(path):
    bg = Image.open(f'{WORK}/end_bg.png').convert('RGB').resize((W, H)).filter(ImageFilter.GaussianBlur(18))
    bg = Image.blend(bg, Image.new('RGB', (W, H), (14, 15, 14)), 0.72); d = ImageDraw.Draw(bg); mark(d, 64, 120)
    y = 640
    for l in ['A simple,', 'inexpensive fix.', 'It just takes', 'some time.']: d.text((64, y), l, font=f_big, fill=(247, 244, 238)); y += 116
    d.text((64, y + 40), "Hank's 2007 G 500 · Nov 2026", font=f_eye, fill=BRASS)
    d.text((64, y + 130), 'Parts list + full how-to:', font=f_body, fill=(217, 211, 198))
    d.text((64, y + 190), 'boxytrucks.com/repairs', font=f_body, fill=BRASS)
    d.text((64, y + 245), 'G 500 › Oil filter housing gasket', font=f_eye, fill=(168, 162, 150))
    d.text((64, y + 340), 'Follow for more from the garage.', font=f_body, fill=(217, 211, 198))
    bg.save(path)

parts, voices, t = [], [], 0.0
for i, (clip, ss, mx, eye, title, line) in enumerate(SEG):
    vd = tts(line, f'{WORK}/v{i}.wav'); dur = max(vd + 0.5, 2.0)
    src = f'{CLIPS}/{clip}.mov'; overlay(eye, title, f'{WORK}/o{i}.png')
    speed = max(0.5, min(1.0, mx / dur))  # slow the clip if the line is longer than the footage
    vf = f"[0:v]trim=start={ss}:duration={mx},setpts=(PTS-STARTPTS)/{speed},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps=30,tpad=stop_mode=clone:stop_duration=10,trim=duration={dur:.3f}[b];[b][1:v]overlay=0:0,format=yuv420p[v]"
    af = f"[0:a]atrim=start={ss}:duration={mx},asetpts=PTS-STARTPTS,atempo={max(0.5, speed)},volume=0.35,apad,atrim=duration={dur:.3f},aresample=48000,aformat=channel_layouts=stereo[a]"
    run(['ffmpeg', '-y', '-v', 'error', '-i', src, '-loop', '1', '-i', f'{WORK}/o{i}.png', '-filter_complex', vf + ';' + af,
         '-map', '[v]', '-map', '[a]', '-t', f'{dur:.3f}', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-c:a', 'aac', '-b:a', '160k', f'{WORK}/p{i}.mp4'])
    parts.append(f'{WORK}/p{i}.mp4'); voices.append((t + 0.25, f'{WORK}/v{i}.wav')); t += dur

run(['ffmpeg', '-y', '-v', 'error', '-ss', '0', '-i', f'{CLIPS}/IMG_0628.mov', '-frames:v', '1', f'{WORK}/end_bg.png']); endcard(f'{WORK}/end.png')
ed = tts(END_VOICE, f'{WORK}/vend.wav') + 0.8
run(['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-i', f'{WORK}/end.png', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-t', f'{ed:.3f}',
     '-vf', 'fps=30,format=yuv420p', '-c:v', 'libx264', '-crf', '20', '-c:a', 'aac', f'{WORK}/pend.mp4'])
parts.append(f'{WORK}/pend.mp4'); voices.append((t + 0.25, f'{WORK}/vend.wav')); t += ed

open(f'{WORK}/list.txt', 'w').write(''.join(f"file '{p}'\n" for p in parts))
run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', f'{WORK}/list.txt', '-c', 'copy', f'{WORK}/body.mp4'])
ins = ['-i', f'{WORK}/body.mp4']; fl = []
for k, (st, p) in enumerate(voices):
    ins += ['-i', p]; fl.append(f'[{k+1}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={int(st*1000)}|{int(st*1000)},volume=1.6[v{k}]')
fl.append('[0:a]' + ''.join(f'[v{k}]' for k in range(len(voices))) + f'amix=inputs={len(voices)+1}:duration=first:normalize=0,alimiter=limit=0.95[a]')
run(['ffmpeg', '-y', '-v', 'error', *ins, '-filter_complex', ';'.join(fl), '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', OUT])
print(OUT, f'{t:.1f}s')
