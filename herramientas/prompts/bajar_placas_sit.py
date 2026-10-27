# -*- coding: utf-8 -*-
r"""Baja las candidatas de placa de las situaciones y arma la hoja de contacto.

    python bajar_placas_sit.py urls.json [contacto.jpg]

urls.json = {"SIT_A_r01_el_lider": ["url_a", "url_b"], ...}
Cada url va a <situacion>/01 PLANOS/_candidatas/<nombre>_<a|b>.png. No pisa
lo que ya existe. La hoja de contacto pone las candidatas de cada ranura en
una fila, con el nombre (solo para revisar: no es material de la pieza).
"""
import json
import os
import sys
import time
import urllib.request

sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
import rutas_sit as R                                       # noqa: E402


def destino(nombre, letra_var):
    L = nombre.split('_')[1]
    d = os.path.join(R.sub(L, '01 PLANOS'), '_candidatas')
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, '%s_%s.png' % (nombre, letra_var))


def bajar(url, ruta):
    if os.path.exists(ruta) and os.path.getsize(ruta) > 10000:
        return 'ya'
    for i in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                data = r.read()
            with open(ruta + '.part', 'wb') as f:
                f.write(data)
            os.replace(ruta + '.part', ruta)
            return 'ok %d' % len(data)
        except Exception as e:                                # noqa: BLE001
            err = e
            time.sleep(3)
    return 'FALLA %s' % err


def contacto(urls, salida):
    from PIL import Image, ImageDraw
    filas = sorted(urls)
    W, H = 640, 360
    hoja = Image.new('RGB', (W * 2 + 30, (H + 34) * len(filas) + 10), (30, 30, 30))
    d = ImageDraw.Draw(hoja)
    for i, n in enumerate(filas):
        y = 10 + i * (H + 34)
        d.text((10, y), n, fill=(230, 230, 230))
        for j, v in enumerate('abcdefgh'[:len(urls[n])]):
            p = destino(n, v)
            if os.path.exists(p):
                im = Image.open(p).convert('RGB')
                im.thumbnail((W, H))
                hoja.paste(im, (10 + j * (W + 10), y + 20))
                d.text((14 + j * (W + 10), y + 22), v, fill=(255, 255, 0))
    hoja.save(salida, quality=82)


if __name__ == '__main__':
    urls = json.load(open(sys.argv[1], encoding='utf-8'))
    for n, lista in sorted(urls.items()):
        for v, u in zip('abcdefgh', lista):
            print(n, v, bajar(u, destino(n, v)), flush=True)
    if len(sys.argv) > 2:
        contacto(urls, sys.argv[2])
        print('contacto', sys.argv[2])
    print('LISTO')
