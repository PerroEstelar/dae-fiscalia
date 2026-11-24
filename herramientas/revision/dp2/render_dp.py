# -*- coding: utf-8 -*-
"""Capturas de las escenas revisadas (1113×448, texto fijo) y de las láminas de los mapas para descargar.

python3 render_dp.py 1.1 [n …]          escenas -> out/escenas/L1.1_E01.png
python3 render_dp.py --mapas            láminas de los mapas -> leccion-0L/documentos/mapa-u…png
"""
import glob, json, os, sys
from playwright.sync_api import sync_playwright
OUT = '/home/claude/dp2/out/sitio/derecho-peticion/'
PNG = '/home/claude/dp2/out/escenas/'

PREP = r'''() => {
  document.querySelectorAll('.j-aviso, .confeti').forEach(e => e.remove());
}'''


def escenas(clave, solo=None):
    u, l = map(int, clave.split('.'))
    idx = OUT + 'unidad-%02d/leccion-%02d/index.html' % (u, l)
    h = open(idx, encoding='utf-8').read()
    import re
    d = json.loads(re.search(r'id="contenido">(.*?)</script>', h, re.S).group(1))
    os.makedirs(PNG, exist_ok=True)
    out = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        c = b.new_context(viewport={'width': 1113, 'height': 448}, device_scale_factor=2)
        c.add_init_script("try{localStorage.setItem('ova-escritura','inmediata')}catch(e){}")
        pg = c.new_page()
        for n in range(1, len(d['scenes']) + 1):
            if solo and n not in solo:
                continue
            pg.goto('file://' + idx + '?escena=%d' % n)
            pg.wait_for_timeout(900)
            bt = pg.query_selector('.escritura-btn')
            if bt and 'fijo' in (bt.inner_text() or '').lower():
                bt.click()
                pg.wait_for_timeout(300)
            pg.evaluate(PREP)
            f = PNG + 'L%s_E%02d.png' % (clave, n)
            pg.screenshot(path=f)
            sc = pg.evaluate("() => { const s = document.querySelector('.escenario'); return s ? [s.scrollHeight, s.clientHeight] : null }")
            out.append((n, d['scenes'][n - 1]['titulo_genially'][:50], sc))
        b.close()
    return out


def mapas():
    hechos = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        c = b.new_context(viewport={'width': 1113, 'height': 448}, device_scale_factor=2)
        pg = c.new_page()
        for idx in sorted(glob.glob(OUT + 'unidad-0*/leccion-0*/index.html')):
            import re
            d = json.loads(re.search(r'id="contenido">(.*?)</script>', open(idx, encoding='utf-8').read(), re.S).group(1))
            for n, e in enumerate(d['scenes'], 1):
                ds = e.get('descarga') or {}
                if ds.get('lamina') and ds.get('href', '').endswith('.png'):
                    pg.goto('file://' + idx + '?escena=%d&lamina=mapa' % n)
                    pg.wait_for_timeout(900)
                    f = os.path.join(os.path.dirname(idx), ds['href'])
                    os.makedirs(os.path.dirname(f), exist_ok=True)
                    el = pg.query_selector('.lamina-mapa') or pg.query_selector('body')
                    pg.screenshot(path=f, full_page=True)
                    hechos.append(f.replace(OUT, ''))
        b.close()
    return hechos


if __name__ == '__main__':
    if sys.argv[1] == '--mapas':
        for h in mapas():
            print(h)
    else:
        for r in escenas(sys.argv[1], [int(x) for x in sys.argv[2:]] or None):
            print(r)
