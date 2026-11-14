# Builds "Hank's G 500 on a fall back road" Reel from Hank's Nov 14 clips (IMG_0644 drive-by, IMG_0643 pass-by, IMG_0645 driver's-seat view, IMG_0642 road photo for the end card).
# Usage: VOICE=<en_US-joe-medium.onnx> python3 social/hank/fall-drive/build.py <clips dir> <out.mp4>
# Voice B (Hank's pick), conversational; facts only from data/g-class.json and Hank's own statements.
import os, subprocess, sys, wave
from PIL import Image, ImageDraw, ImageFont, ImageFilter
CLIPS, OUT = sys.argv[1], sys.argv[2]
WORK = os.environ.get('WORK', '/tmp/falldrive'); os.makedirs(WORK, exist_ok=True)
VOICE = os.environ['VOICE']; W, H = 1080, 1920
F = '/usr/share/fonts/opentype/inter/'
f_title = ImageFont.truetype(F + 'InterDisplay-Bold.otf', 84); f_eye = ImageFont.truetype(F + 'Inter-SemiBold.otf', 30)
f_brand = ImageFont.truetype(F + 'Inter-Bold.otf', 30); f_big = ImageFont.truetype(F + 'InterDisplay-Bold.otf', 104); f_body = ImageFont.truetype(F + 'Inter-Medium.otf', 44)
BRASS = (201, 168, 106)
SEG = [  # clip, start, len, mode, eyebrow, title, voice ('' = no voice line)
 ('IMG_0644', 0.0, 4.3, 'fit', "HANK'S 2007 G 500", 'Out on a fall back road',
  "So this is Hank's 2007 G 500, out on a back road with the leaves turning."),
 ('IMG_0643', 6.6, 1.2, 'crop', "HANK'S 2007 G 500", 'Out on a fall back road', ''),  # cut at 7.8 s, before the rear plate shows
 ('IMG_0645', 0.0, 10.0, 'crop', 'M113 V8 · THREE LOCKERS', 'Nearly twenty years old',
  "Five liter V8, three locking diffs, and a ladder frame. It's nearly twenty years old, and honestly? It still drives like this."),
]
END_VOICE = "Thinking about a G 500? Every year, what to check, and what it costs, is on boxy trucks dot com."
def run(c): subprocess.run(c, check=True, capture_output=True)
def tts(text, path):
    subprocess.run(['python3', '-m', 'piper', '-m', VOICE, '--length-scale', '1.0', '--noise-scale', '0.8', '--noise-w-scale', '1.0', '-f', path], input=text.encode(), check=True, capture_output=True)
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
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
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
    bg = Image.open(f'{CLIPS}/IMG_0642.jpeg').convert('RGB'); s = max(W / bg.width, H / bg.height)
    bg = bg.resize((int(bg.width * s), int(bg.height * s))); l = (bg.width - W) // 2; bg = bg.crop((l, 0, l + W, H)).filter(ImageFilter.GaussianBlur(14))
    bg = Image.blend(bg, Image.new('RGB', (W, H), (14, 15, 14)), 0.7); d = ImageDraw.Draw(bg); mark(d, 64, 120)
    y = 640
    for t in ['Thinking about', 'a G 500?']: d.text((64, y), t, font=f_big, fill=(247, 244, 238)); y += 116
    d.text((64, y + 40), "Hank's 2007 G 500 · Nov 2026", font=f_eye, fill=BRASS)
    d.text((64, y + 130), 'Every year, what to check, what it costs:', font=f_body, fill=(217, 211, 198))
    d.text((64, y + 190), 'boxytrucks.com/models/g-class/g500', font=f_body, fill=BRASS)
    d.text((64, y + 300), 'Follow for more from the garage.', font=f_body, fill=(217, 211, 198))
    bg.save(path)
parts, voices, t = [], [], 0.0
for i, (clip, ss, ln, mode, eye, title, line) in enumerate(SEG):
    vd = tts(line, f'{WORK}/v{i}.wav') if line else 0
    dur = max(vd + 0.6, ln) if (line and i == len(SEG) - 1) else ln  # the opening line runs across the drive-by and pass-by; only the last clip holds for its line
    overlay(eye, title, f'{WORK}/o{i}.png'); src = f'{CLIPS}/{clip}.mov'
    if mode == 'fit':  # whole frame over a blurred fill, so the truck stays in shot as it approaches
        base = f"[0:v]trim=start={ss}:duration={ln},setpts=PTS-STARTPTS,split[a][b];[a]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=30:2[bg];[b]scale={W}:-2[fg];[bg][fg]overlay=0:(H-h)/2-180"
    else:
        base = f"[0:v]trim=start={ss}:duration={ln},setpts=PTS-STARTPTS,scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}"
    vf = base + f",fps=30,tpad=stop_mode=clone:stop_duration=10,trim=duration={dur:.3f}[b2];[b2][1:v]overlay=0:0,format=yuv420p[v]"
    af = f"[0:a]atrim=start={ss}:duration={ln},asetpts=PTS-STARTPTS,volume=0.4,apad,atrim=duration={dur:.3f},aresample=48000,aformat=channel_layouts=stereo[a]"
    run(['ffmpeg', '-y', '-v', 'error', '-i', src, '-loop', '1', '-i', f'{WORK}/o{i}.png', '-filter_complex', vf + ';' + af,
         '-map', '[v]', '-map', '[a]', '-t', f'{dur:.3f}', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-c:a', 'aac', '-b:a', '160k', f'{WORK}/p{i}.mp4'])
    parts.append(f'{WORK}/p{i}.mp4')
    if line: voices.append((t + 0.3, f'{WORK}/v{i}.wav'))
    t += dur
endcard(f'{WORK}/end.png'); ed = tts(END_VOICE, f'{WORK}/vend.wav') + 0.9
run(['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-i', f'{WORK}/end.png', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-t', f'{ed:.3f}',
     '-vf', 'fps=30,format=yuv420p', '-c:v', 'libx264', '-crf', '20', '-c:a', 'aac', f'{WORK}/pend.mp4'])
parts.append(f'{WORK}/pend.mp4'); voices.append((t + 0.25, f'{WORK}/vend.wav')); t += ed
open(f'{WORK}/list.txt', 'w').write(''.join(f"file '{p}'\n" for p in parts))
run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', f'{WORK}/list.txt', '-c', 'copy', f'{WORK}/body.mp4'])
ins = ['-i', f'{WORK}/body.mp4']; fl = []
for k, (st, p) in enumerate(voices):
    ins += ['-i', p]; fl.append(f'[{k+1}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={int(st*1000)}|{int(st*1000)},volume=1.6[v{k}]')
fl.append('[0:a]' + ''.join(f'[v{k}]' for k in range(len(voices))) + f'amix=inputs={len(voices)+1}:duration=first:normalize=0,alimiter=limit=0.95[a]')
run(['ffmpeg', '-y', '-v', 'error', *ins, '-filter_complex', ';'.join(fl), '-map', '0:v', '-map', '[a]', '-c:v', 'libx264', '-preset', 'medium', '-b:v', '3500k', '-maxrate', '4000k', '-bufsize', '8000k', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', OUT])
print(OUT, f'{t:.1f}s')
