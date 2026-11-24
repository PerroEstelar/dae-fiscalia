# Abre cada escena visible de las 16 lecciones (servidor local) y junta las URLs que dan 404.
import json, re, sys
from playwright.sync_api import sync_playwright
g = json.load(open('/tmp/claude-0/rev/genially_escenas.json', encoding='utf-8'))
urls = []
for f, v in g.items():
    for s in v['slides']:
        for u in s['iframes']:
            urls.append(u.replace('https://estebanioi.github.io/', 'http://localhost:8765/'))
urls = list(dict.fromkeys(urls))
fallos = set()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1113, 'height': 448})
    pg.on('response', lambda r: fallos.add(r.url) if r.status >= 400 else None)
    for i, u in enumerate(urls):
        try:
            pg.goto(u, wait_until='load', timeout=20000); pg.wait_for_timeout(700)
        except Exception as e:
            print('ERR', u, e)
        if i % 20 == 0: print(i, len(urls), len(fallos), flush=True)
    b.close()
json.dump(sorted(fallos), open('/tmp/claude-0/rev/faltan.json', 'w'), indent=0)
print('LISTO', len(urls), 'escenas', len(fallos), 'faltan')
