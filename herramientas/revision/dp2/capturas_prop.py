# -*- coding: utf-8 -*-
"""Miniaturas reales de la propuesta: cada escena revisada tal como queda en el Genially (marco + mediación), capturada
del HTML de la lección (html_leccion/out/dp) a 1200 × 675, con el texto fijo y sin avisos del juego."""
import glob, os, re, sys
from playwright.sync_api import sync_playwright
HTML = '/home/claude/html_leccion/out/dp/'
OUT = '/home/claude/dp2/out/prop/'
LIMPIA = "()=>{const f=document.querySelector('#lienzo iframe'); if(!f)return; const d=f.contentDocument; d.querySelectorAll('.j-aviso,.confeti').forEach(e=>e.remove());}"
with sync_playwright() as p:
    b = p.chromium.launch()
    c = b.new_context(viewport={'width': 1200, 'height': 675})
    c.add_init_script("try{localStorage.setItem('ova-escritura','inmediata')}catch(e){}")
    for f in sorted(glob.glob(HTML + 'DP_U*_L*.html')):
        u, l = map(int, re.search(r'U(\d)_L(\d)', f).groups())
        pg = c.new_page()
        pg.goto('file://' + f); pg.wait_for_timeout(1000)
        n = pg.evaluate("()=>Number(document.getElementById('estado').textContent.match(/de (\\d+)/)[1])")
        for k in range(1, n):
            pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(1300)
            if 2 <= k <= n - 2:      # escenas: diapositiva 3 .. n-1
                pg.evaluate(LIMPIA); pg.wait_for_timeout(150)
                pg.screenshot(path=OUT + 'L%d.%d_E%02d.png' % (u, l, k - 1))
        pg.close()
        print(u, l, n - 3, flush=True)
    b.close()
