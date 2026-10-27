"""Download channel/profile icons for every YouTube (and, where possible, Instagram) link in data/,
shrink them to small thumbnails and host them on the site, so pages never load third-party images.

  python scripts/fetch_avatars.py            # fetch any missing icons
  python scripts/fetch_avatars.py --refresh  # re-fetch all

Writes site/img/avatars/<key>.jpg and data/avatars.json ({normalised url: "avatars/<key>.jpg"}).
Run by hand now and then (not in CI), then commit the results.
"""
import io, json, re, sys, time, hashlib, urllib.request, urllib.parse
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'site' / 'img' / 'avatars'
MAP = ROOT / 'data' / 'avatars.json'
UA = {'User-Agent': 'Mozilla/5.0 (compatible; BoxyTrucksBot/1.0; +https://boxytrucks.com)'}
URL_RE = re.compile(r'https://(?:www\.)?(youtube|instagram)\.com/[^"\s?#]+')


def norm(u):
    u = u.split('?')[0].split('#')[0].rstrip('/')
    u = re.sub(r'/(videos|featured|streams|shorts|about)$', '', u)
    u = re.sub(r'^https://(www\.)?', 'https://www.', u)
    if 'instagram.com' in u or '/@' in u:
        u = u.lower()  # handles are case-insensitive; channel IDs are not
    return u


def key(u):
    tail = u.rstrip('/').split('/')[-1].lstrip('@')
    tail = re.sub(r'[^a-z0-9_.-]', '', tail.lower())[:40] or 'x'
    site = 'yt' if 'youtube' in u else 'ig'
    return f'{site}-{tail}-{hashlib.sha1(u.encode()).hexdigest()[:6]}'


def get(url, binary=False):
    with urllib.request.urlopen(urllib.request.Request(urllib.parse.quote(url, safe=':/?=&@%-._~'), headers=UA), timeout=20) as r:
        b = r.read()
    return b if binary else b.decode('utf-8', 'replace')


def og_image(html):
    m = re.search(r'<meta property="og:image" content="([^"]+)"', html)
    return m.group(1).replace('&amp;', '&') if m else None


def save(img_bytes, path):
    im = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    w, h = im.size; s = min(w, h)
    im = im.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2)).resize((96, 96), Image.LANCZOS)
    im.save(path, 'JPEG', quality=85, optimize=True)


def main():
    refresh = '--refresh' in sys.argv
    OUT.mkdir(parents=True, exist_ok=True)
    amap = json.loads(MAP.read_text()) if MAP.exists() else {}
    urls = set()
    for f in (ROOT / 'data').rglob('*.json'):
        if f.name == 'avatars.json':
            continue
        urls |= {norm(m.group(0)) for m in URL_RE.finditer(f.read_text())}
    urls = sorted(u for u in urls if re.search(r'youtube\.com/(@|channel/|c/|user/)', u) or re.search(r'instagram\.com/[a-z0-9_.]+$', u))
    got = miss = 0
    for u in urls:
        if u in amap and not refresh and (ROOT / 'site' / 'img' / amap[u]).exists():
            continue
        if 'instagram' in u:
            miss += 1
            continue  # Instagram requires a login; filled separately
        try:
            src = og_image(get(u))
            if not src:
                raise ValueError('no og:image')
            src = re.sub(r'=s\d+-', '=s176-', src)
            k = key(u)
            save(get(src, binary=True), OUT / f'{k}.jpg')
            amap[u] = f'avatars/{k}.jpg'
            got += 1
        except Exception as e:
            print('  skip', u, e)
            miss += 1
        time.sleep(0.8)
    MAP.write_text(json.dumps(dict(sorted(amap.items())), indent=1))
    print(f'{got} fetched, {miss} missing, {len(amap)} total in map')


if __name__ == '__main__':
    main()
