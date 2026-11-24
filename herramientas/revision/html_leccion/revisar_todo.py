# -*- coding: utf-8 -*-
"""Recorre todas las páginas de cada HTML con la flecha del teclado y verifica: sin errores de JS, el iframe de cada
escena con la mediación pintada, imágenes cargadas. Guarda una miniatura por página para la hoja de contacto."""
import sys, os, json, glob
from playwright.sync_api import sync_playwright
archivos = sys.argv[1:]
out = '/tmp/claude-0/hl/todo/'; os.makedirs(out, exist_ok=True)
rep = {}
with sync_playwright() as p:
    b = p.chromium.launch()
    c = b.new_context(viewport={'width': 1200, 'height': 675})
    for f in archivos:
        pg = c.new_page()
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)[:200]))
        pg.goto('file://' + os.path.abspath(f)); pg.wait_for_timeout(1200)
        n = pg.evaluate("()=>document.title") and pg.evaluate("()=>{var m=document.getElementById('estado').textContent.match(/de (\\d+)/);return m?Number(m[1]):0}")
        malos = []
        for k in range(n):
            if k:
                pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(900)
            info = pg.evaluate("""()=>{var f=document.querySelector('#lienzo iframe');var r={pag:document.getElementById('estado').textContent,
              imgs:[...document.querySelectorAll('#lienzo img')].filter(i=>!i.complete||!i.naturalWidth).length};
              if(f){try{var d=f.contentDocument;var o=d.getElementById('ova');r.ifr=o?o.children.length:(d.body?d.body.children.length:-1);
              r.ifr_imgs=[...d.querySelectorAll('img')].filter(i=>i.complete&&!i.naturalWidth).length;}catch(e){r.ifr='err'}}return r}""")
            pg.screenshot(path=out + '%s_p%02d.png' % (os.path.basename(f)[:-5], k + 1), scale='css')
            if info.get('imgs') or info.get('ifr') in (0, -1, 'err') or info.get('ifr_imgs'):
                malos.append((k + 1, info))
        rep[os.path.basename(f)] = {'paginas': n, 'errores': errs[:5], 'malos': malos}
        print(os.path.basename(f), n, 'errores', len(errs), 'malos', malos[:4], flush=True)
        pg.close()
    b.close()
json.dump(rep, open(out + '_rep.json', 'w'), ensure_ascii=False, indent=1)
