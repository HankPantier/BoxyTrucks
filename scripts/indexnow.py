"""Tell IndexNow-enabled search engines (Bing, Yandex, Seznam, Naver...) which pages changed.

  python scripts/indexnow.py prepare   # before deploy: diff site/page-hashes.json against the live site
  python scripts/indexnow.py send      # after deploy: submit the changed URLs

Does nothing unless https://boxytrucks.com is serving the key file over HTTPS, so it is safe
to run before the domain's certificate is ready. Google does not use IndexNow; it reads the sitemap.
"""
import json, re, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOST = 'boxytrucks.com'
UA = {'User-Agent': 'BoxyTrucksBot/1.0 (+https://boxytrucks.com)'}
LIST = ROOT / 'indexnow-urls.txt'


def key():
    return re.search(r"INDEXNOW_KEY = '([0-9a-f]+)'", (ROOT / 'build.py').read_text()).group(1)


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
        return r.read().decode()


def prepare():
    new = json.loads((ROOT / 'site' / 'page-hashes.json').read_text())
    try:
        old = json.loads(get(f'https://{HOST}/page-hashes.json'))
    except Exception as e:
        print(f'no live hashes ({e}); treating every page as new')
        old = {}
    changed = [u for u, h in new.items() if old.get(u) != h]
    LIST.write_text('\n'.join(changed))
    print(f'{len(changed)} changed of {len(new)} pages')


def send():
    urls = [u for u in LIST.read_text().split('\n') if u] if LIST.exists() else []
    if not urls:
        print('nothing to submit'); return
    k = key()
    try:
        live = get(f'https://{HOST}/{k}.txt').strip()
    except Exception as e:
        print(f'key file not reachable over HTTPS yet ({e}); skipping'); return
    if live != k:
        print('live key file does not match; skipping'); return
    body = json.dumps({'host': HOST, 'key': k, 'keyLocation': f'https://{HOST}/{k}.txt', 'urlList': urls[:10000]}).encode()
    req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body, method='POST',
                                 headers={**UA, 'Content-Type': 'application/json; charset=utf-8'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f'IndexNow: HTTP {r.status} for {len(urls)} URLs')
    except Exception as e:
        print(f'IndexNow submit failed: {e}')  # never fail the deploy over this


if __name__ == '__main__':
    {'prepare': prepare, 'send': send}[sys.argv[1]]()
