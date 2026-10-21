#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Amarra cada placa a la creacion de Magnific que la produjo, MIDIENDO.

POR QUE NO SIRVE NINGUN ATAJO
    Ni el nombre del archivo ni la memoria de la sesion ni el orden del
    historial. Los nombres mienten -`cama_sello_sin_fecha` no es un sello, son
    once capturas de pantalla impresas-, y el historial se reordena cuando una
    placa se repite.

    Tampoco sirve la MINIATURA. El `thumbnailUrl` de Magnific es un recorte
    CUADRADO de 400x400 de un cuadro 16:9: la correlacion se mide entonces
    sobre otra imagen, y eso ya produjo tres parejas falsas en este proyecto.
    Se usa el `previewUrl` a 1024.

    Y se compara contra el `_crudo_*.png`, NUNCA contra la placa ya graduada:
    el grade mueve el histograma lo bastante como para acercar una placa a la
    vecina.

Y UNA MAS, QUE NO ES DE EMPAREJAR SINO DE CONFIAR
    El borrador local del prompt no es necesariamente lo que se envio.
    Comprobado en el Caso 3: de seis prompts guardados en local antes de
    mandarlos, dos coincidian al caracter con el historial y cuatro traian una
    frase de mas. Manda lo que devuelve Magnific.

USO
    python casar_con_magnific.py previews.json dir_con_crudos [mas_dirs...]

    previews.json: [{"id": ..., "preview": <previewUrl>}, ...], tal como sale
    de creations_search. Escribe `casados.json` al lado del primer directorio.
"""
import json
import os
import sys
import urllib.request

from PIL import Image

LADO = (64, 36)


def firma(im):
    """Miniatura en gris, normalizada a media 0 y desviacion 1.

    Normalizar es lo que hace que la medida no dependa del brillo ni del
    contraste: lo que compara es la ESTRUCTURA.
    """
    im = im.convert('L').resize(LADO, Image.LANCZOS)
    px = list(im.getdata())
    m = sum(px) / len(px)
    s = (sum((p - m) ** 2 for p in px) / len(px)) ** 0.5 or 1.0
    return [(p - m) / s for p in px]


def dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) / len(a)


def casar(previews, dirs, tmp):
    os.makedirs(tmp, exist_ok=True)
    crudos = {}
    for d in dirs:
        for f in sorted(os.listdir(d)):
            if '_crudo' in f and f.lower().endswith('.png'):
                crudos[f[:-4]] = firma(Image.open(os.path.join(d, f)))

    firmas = {}
    for c in previews:
        dst = os.path.join(tmp, c['id'] + '.png')
        if not os.path.exists(dst):
            try:
                urllib.request.urlretrieve(c['preview'], dst)
            except Exception as e:
                print('ERR baja', c['id'], e)
                continue
        try:
            firmas[c['id']] = firma(Image.open(dst))
        except Exception as e:
            print('ERR abre', c['id'], e)
    print('%d crudos, %d vistas previas' % (len(crudos), len(firmas)))

    res = {}
    for nom, f in sorted(crudos.items()):
        pares = sorted((dist(f, g), i) for i, g in firmas.items())
        res[nom] = {'id': pares[0][1], 'd': round(pares[0][0], 4),
                    'segundo': pares[1][1], 'd2': round(pares[1][0], 4)}
        print('%-42s %s  d=%.4f   (2o %s d=%.4f)'
              % (nom, pares[0][1], pares[0][0], pares[1][1], pares[1][0]))
    return res


if __name__ == '__main__':
    prev = json.load(open(sys.argv[1], encoding='utf-8'))
    dirs = sys.argv[2:]
    tmp = os.path.join(dirs[0], '_prev')
    res = casar(prev, dirs, tmp)
    salida = os.path.join(dirs[0], 'casados.json')
    json.dump(res, open(salida, 'w', encoding='utf-8'), indent=1)
    print('\n->', salida)
    # un ganador flojo o un segundo demasiado cerca es motivo para MIRAR la
    # pareja, no para aceptarla
    duda = [n for n, v in res.items() if v['d'] > 0.01 or v['d2'] < 0.05]
    print('PAREJAS QUE HAY QUE MIRAR A OJO:', duda or 'ninguna')
