# -*- coding: utf-8 -*-
"""Prueba de funciones: índice, instrucciones, descarga (Blob), caso con audio, video."""
import sys, os, json
from playwright.sync_api import sync_playwright
f = os.path.abspath(sys.argv[1]); p_desc = int(sys.argv[2]); p_caso = int(sys.argv[3]) if len(sys.argv) > 3 else 0
out = '/tmp/claude-0/hl/'
res = {}
with sync_playwright() as p:
    b = p.chromium.launch()
    c = b.new_context(viewport={'width': 1280, 'height': 720}, accept_downloads=True)
    pg = c.new_page()
    errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)[:300]))
    pg.goto('file://' + f + '#p2'); pg.wait_for_timeout(1500)
    # índice: tercera fila con interactividad -> debe cambiar de página
    filas = pg.locator('#lienzo [data-a]')
    res['interactivos_indice'] = filas.count()
    destino = pg.evaluate("()=>[...document.querySelectorAll('#lienzo [data-a]')].map(x=>x.dataset.a+':'+(x.getAttribute('aria-label')||'').slice(0,30))")
    res['indice'] = destino[:16]
    # instrucciones: botón dentro del iframe -> ventana del lector
    fr = pg.frame_locator('#lienzo iframe').first
    fr.locator('.abrir').click(); pg.wait_for_timeout(1200)
    res['ventana_abierta'] = pg.evaluate("()=>document.getElementById('ventana').classList.contains('abierta')")
    pg.screenshot(path=out + 'ventana.png')
    pg.keyboard.press('Escape'); pg.wait_for_timeout(300)
    res['ventana_cerrada'] = not pg.evaluate("()=>document.getElementById('ventana').classList.contains('abierta')")
    # descarga
    pg.goto('file://' + f + '#p%d' % p_desc); pg.reload(); pg.wait_for_timeout(2500)
    fr = pg.frame_locator('#lienzo iframe').first
    a = fr.locator('a.boton-descarga, a.descarga-btn').first
    res['descarga_href'] = (a.get_attribute('href') or '')[:20]
    res['descarga_nombre'] = a.get_attribute('download')
    with pg.expect_download() as dl:
        a.click()
    d = dl.value
    pth = d.path(); res['descarga_bytes'] = os.path.getsize(pth); res['descarga_sugerido'] = d.suggested_filename
    pg.screenshot(path=out + 'descarga.png')
    if p_caso:
        pg.goto('file://' + f + '#p%d' % p_caso); pg.reload(); pg.wait_for_timeout(2500)
        fr = pg.frame_locator('#lienzo iframe').first
        fr.locator('.caso-audio-btn').first.click(); pg.wait_for_timeout(2000)
        caso = fr.frame_locator('.ventana-caso iframe')
        res['caso_titulo'] = caso.locator('#titulo').inner_text()
        res['caso_parrafos'] = caso.locator('.texto p').count()
        dur = caso.locator('#a').evaluate("a=>new Promise(r=>{if(a.duration)r(a.duration);a.addEventListener('loadedmetadata',()=>r(a.duration));setTimeout(()=>r(a.duration||-1),4000)})")
        res['caso_audio_s'] = dur
        res['caso_src'] = caso.locator('#a').evaluate("a=>a.src.slice(0,10)")
        pg.screenshot(path=out + 'caso.png')
    res['errores'] = errs
    print(json.dumps(res, ensure_ascii=False, indent=1))
    b.close()
