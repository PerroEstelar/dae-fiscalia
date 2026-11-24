# -*- coding: utf-8 -*-
"""Prueba un HTML de lección en Chromium: capturas de varias páginas y errores de consola."""
import sys, os, json
from playwright.sync_api import sync_playwright
f = os.path.abspath(sys.argv[1]); paginas = [int(x) for x in sys.argv[2:]] or [1, 2, 3]
out = '/tmp/claude-0/hl/'
with sync_playwright() as p:
    b = p.chromium.launch()
    c = b.new_context(viewport={'width': 1280, 'height': 720})
    pg = c.new_page()
    errs = []
    pg.on('console', lambda m: errs.append(('console', m.type, m.text[:200])) if m.type in ('error', 'warning') else None)
    pg.on('pageerror', lambda e: errs.append(('pageerror', str(e)[:300])))
    for n in paginas:
        pg.goto('file://' + f + '#p%d' % n)
        pg.reload()
        pg.wait_for_timeout(2500)
        pg.screenshot(path=out + os.path.basename(f)[:-5] + '_p%02d.png' % n)
    print(json.dumps(errs[:30], ensure_ascii=False, indent=0))
    b.close()
