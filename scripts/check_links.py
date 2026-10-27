"""Check every outbound link in data/ and report the ones that look broken.

  python scripts/check_links.py                 # writes reports/link-check.md
  python scripts/check_links.py --limit 200     # quick sample

Flags:
  BROKEN    404/410, DNS failure, or connection refused
  PARKED    page looks like a parked/for-sale/spam domain
  MOVED     redirects to a different site, or to the homepage of the same site
  BLOCKED   403/429/5xx/timeouts (site blocks bots or was down; usually fine, listed for reference)
Runs monthly in GitHub Actions (.github/workflows/link-check.yml), which opens an issue with the report.
"""
import json, re, sys, socket, ssl, urllib.request, urllib.error
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data'
UA = 'Mozilla/5.0 (compatible; BoxyTrucksBot/1.0; +https://boxytrucks.com)'
SKIP_HOSTS = ('api.nhtsa.gov', 'static.nhtsa.gov', 'boxytrucks.com', 'instagram.com', 'facebook.com', 'amazon.com')
PARKED_RE = re.compile(r'domain (is|may be) for sale|buy this domain|this domain is parked|parkingcrew|sedoparking|bodis\.com|'
                       r'hugedomains|dan\.com/buy|afternic|casino|slot gacor|judi online|togel', re.I)
URL_RE = re.compile(r'https?://[^\s"<>\\\]]+')


def _strings(o):
    if isinstance(o, dict):
        for v in o.values():
            yield from _strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from _strings(v)
    elif isinstance(o, str):
        yield o


def _urls_in(text):
    for m in URL_RE.finditer(text):
        u = m.group(0).rstrip('.,;:')
        while u.endswith(')') and u.count('(') < u.count(')'):
            u = u[:-1]
        yield u


def collect():
    where = defaultdict(set)
    for f in DATA.rglob('*.json'):
        if f.name in ('avatars.json', 'affiliates.json'):
            continue
        rel = f.relative_to(DATA).as_posix()
        try:
            strings = _strings(json.loads(f.read_text()))
        except Exception:
            continue
        for st in strings:
            for u in _urls_in(st):
                if '{' in u or any(h in urlparse(u).netloc for h in SKIP_HOSTS):
                    continue
                where[u].add(rel)
    return where


def check(url):
    ctx = ssl.create_default_context()
    for method in ('HEAD', 'GET'):
        req = urllib.request.Request(url, method=method, headers={'User-Agent': UA, 'Accept': 'text/html,*/*'})
        try:
            with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
                final = r.geturl()
                body = r.read(60000).decode('utf-8', 'replace') if method == 'GET' else ''
                if method == 'HEAD':
                    # need the body to spot parked pages
                    continue
                return classify(url, r.status, final, body)
        except urllib.error.HTTPError as e:
            if method == 'HEAD' and e.code in (403, 404, 405, 429, 500, 501, 503):
                continue  # many servers mishandle HEAD; retry with GET
            return classify(url, e.code, url, '')
        except (urllib.error.URLError, socket.timeout, TimeoutError, ConnectionError, ssl.SSLError) as e:
            reason = str(getattr(e, 'reason', e))
            if 'Name or service not known' in reason or 'nodename nor servname' in reason or 'getaddrinfo' in reason:
                return ('BROKEN', 'domain does not resolve', url)
            if 'refused' in reason:
                return ('BROKEN', 'connection refused', url)
            return ('BLOCKED', reason[:80], url)
        except Exception as e:  # noqa
            return ('BLOCKED', str(e)[:80], url)
    return ('BLOCKED', 'no response', url)


def classify(url, code, final, body):
    if code in (404, 410):
        return ('BROKEN', f'HTTP {code}', final)
    if code in (403, 429) or code >= 500:
        return ('BLOCKED', f'HTTP {code}', final)
    if body and PARKED_RE.search(body[:60000]) and not re.search(r'casino|slot', urlparse(url).netloc + urlparse(url).path, re.I):
        return ('PARKED', 'looks parked or spam', final)
    a, b = urlparse(url), urlparse(final)
    ha, hb = a.netloc.lower().removeprefix('www.'), b.netloc.lower().removeprefix('www.')
    if ha != hb and not hb.endswith('.' + ha) and not ha.endswith('.' + hb):
        return ('MOVED', f'now redirects to {hb}', final)
    if a.path.strip('/') and not b.path.strip('/'):
        return ('MOVED', 'redirects to the homepage', final)
    return ('OK', f'HTTP {code}', final)


def main():
    limit = int(sys.argv[sys.argv.index('--limit') + 1]) if '--limit' in sys.argv else None
    where = collect()
    urls = sorted(where)[:limit] if limit else sorted(where)
    if '--only' in sys.argv:
        keep = set(Path(sys.argv[sys.argv.index('--only') + 1]).read_text().split())
        urls = [u for u in urls if any(u.startswith(k) for k in keep)]
    with ThreadPoolExecutor(max_workers=16) as ex:
        results = dict(zip(urls, ex.map(check, urls)))
    groups = defaultdict(list)
    for u, (kind, why, final) in results.items():
        groups[kind].append((u, why, final))
    out = ['# Outbound link check', '', f'Checked {len(urls)} unique links found in `data/`.', '',
           '| Result | Count |', '|---|---|'] + [f'| {k} | {len(groups[k])} |' for k in ('BROKEN', 'PARKED', 'MOVED', 'BLOCKED', 'OK')] + ['']
    for kind, title in (('BROKEN', 'Broken: fix or replace'), ('PARKED', 'Parked or spam domains: replace now'),
                        ('MOVED', 'Redirected: check they still go to the right page'),
                        ('BLOCKED', 'Blocked or slow: usually fine (the site blocks bots), listed for reference')):
        if not groups[kind]:
            continue
        out += [f'## {title}', '']
        for u, why, final in sorted(groups[kind]):
            files = ', '.join(sorted(where[u]))[:200]
            extra = f' → {final}' if final != u and kind == 'MOVED' else ''
            out.append(f'- {u} — {why}{extra}  \n  in: {files}')
        out.append('')
    (ROOT / 'reports').mkdir(exist_ok=True)
    (ROOT / 'reports' / 'link-check.md').write_text('\n'.join(out))
    print('\n'.join(out[:12]))
    bad = len(groups['BROKEN']) + len(groups['PARKED'])
    Path(ROOT / 'link-check-summary.txt').write_text(f'{bad} broken or parked, {len(groups["MOVED"])} redirected')


if __name__ == '__main__':
    main()
