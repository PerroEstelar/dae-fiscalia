# -*- coding: utf-8 -*-
"""Espeja en disco las escenas HTML de los Genially de un curso (GitHub Pages de estebanioi), para abrirlas
sin red en otro lado. Lee los JSON de Genially de <base>/genially/, saca los iframes y baja cada lección
(index, instrucciones, fin), sus css/js, fuentes, íconos e ilustraciones. Deja todo en <base>/sitio/ y un zip.

    python crawl_dp.py <base>
"""
import glob
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import zipfile

B = sys.argv[1].rstrip('/') + '/'
OUT = B + 'sitio/'
LOG = B + 'crawl.log'
HOST = 'https://estebanioi.github.io/'


def log(*a):
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(time.strftime('%H:%M:%S ') + ' '.join(str(x) for x in a) + '\n')


def bajar(u):
    p = OUT + urllib.parse.unquote(u[len(HOST):].split('?')[0].split('#')[0])
    if p.endswith('/'):
        p += 'index.html'
    if os.path.exists(p):
        return p, open(p, 'rb').read()
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=30)
        d = r.read()
    except Exception as e:  # noqa
        return None, str(e)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'wb').write(d)
    return p, d


def main():
    srcs = set()
    for f in sorted(glob.glob(B + 'genially/*.json')):
        s = open(f, encoding='utf-8').read().replace('\\/', '/').replace('&amp;', '&')
        for u in re.findall(r'https://estebanioi\.github\.io/[^"\'\\\s<>]+', s):
            srcs.add(u.split('?')[0].split('#')[0])
    lecciones = sorted(set(u.rsplit('/', 1)[0] + '/' for u in srcs if u.endswith('.html')))
    log('iframes', len(srcs), 'lecciones', len(lecciones))
    cola = list(srcs)
    for d in lecciones:
        cola += [d + 'index.html', d + 'instrucciones.html', d + 'fin.html']
    hechos, malos = set(), []
    while cola:
        u = cola.pop(0)
        u = u.split('#')[0]
        clave = u.split('?')[0]
        if clave in hechos or not clave.startswith(HOST):
            continue
        hechos.add(clave)
        p, d = bajar(u)
        if p is None:
            malos.append((clave, d))
            continue
        base = clave
        nuevos = []
        if clave.endswith('.html'):
            t = d.decode('utf-8', 'replace')
            nuevos += re.findall(r'(?:src|href)="([^"#]+)"', t)
            for img in set(re.findall(r'([\w-]+\.(?:webp|png|jpg|jpeg|svg|gif))', t)):
                nuevos += ['../comun/assets/contexto/' + img, 'assets/contexto/' + img, '../comun/assets/' + img]
        elif clave.endswith('.css'):
            t = d.decode('utf-8', 'replace')
            nuevos += [x.strip('\'" ') for x in re.findall(r'url\(([^)]+)\)', t) if not x.strip('\'" ').startswith('data:')]
        elif clave.endswith('.js'):
            t = d.decode('utf-8', 'replace')
            lits = set(re.findall(r'["\'`]([\w./-]+\.(?:webp|png|jpg|svg|css|js|json|woff2?|html))["\'`]', t))
            pag = [x for x in hechos if x.endswith('index.html')]
            for x in lits:
                nuevos.append(x)  # relativo al script
                for pg in pag[:1]:
                    cola.append(urllib.parse.urljoin(pg, x))
        for x in nuevos:
            if x.startswith('data:') or x.startswith('mailto:') or x.startswith('javascript:'):
                continue
            cola.append(urllib.parse.urljoin(base, x))
        if len(hechos) % 25 == 0:
            log('van', len(hechos), 'cola', len(cola), 'malos', len(malos))
    json.dump({'lecciones': lecciones, 'iframes': sorted(srcs), 'malos': malos}, open(B + 'sitio_indice.json', 'w',
              encoding='utf-8'), ensure_ascii=False, indent=1)
    z = zipfile.ZipFile(B + 'sitio_dp.zip', 'w', zipfile.ZIP_DEFLATED)
    for r, _ds, fs in os.walk(OUT):
        for f in fs:
            z.write(os.path.join(r, f), os.path.relpath(os.path.join(r, f), B))
    for f in glob.glob(B + 'genially/*.json'):
        z.write(f, os.path.relpath(f, B))
    z.write(B + 'sitio_indice.json', 'sitio_indice.json')
    z.close()
    log('LISTO', len(hechos), 'archivos;', len(malos), 'malos (404 esperables en candidatos)')


if __name__ == '__main__':
    main()
