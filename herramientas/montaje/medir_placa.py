# -*- coding: utf-8 -*-
"""Las metricas de aceptacion de una placa del P3C4.

NO JUZGA LA COMPOSICION, JUZGA LO QUE SE PUEDE MEDIR
    zonas tonales   ninguna area grande cerca del blanco ni del negro
    planitud        el gradiente local sobre las superficies grandes
    piel            tono y saturacion de las manos, contra la banda aprobada
    acento          saturacion del unico color saturado, contra el piso 0,45
"""
import os, sys
import numpy as np
from PIL import Image

BANDA_TONO = (12, 37)
BANDA_SAT = (0.16, 0.28)
PISO_ACENTO = 0.45


def met(f):
    im = Image.open(f).convert('RGB')
    a = np.asarray(im).astype(np.float32) / 255.0
    mx = a.max(2); mn = a.min(2); v = mx
    s = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    h = np.zeros_like(mx); d = mx - mn + 1e-6
    m = (mx == r); h[m] = ((g - b)[m] / d[m]) % 6
    m = (mx == g); h[m] = ((b - r)[m] / d[m]) + 2
    m = (mx == b); h[m] = ((r - g)[m] / d[m]) + 4
    h = h * 60
    gris = a.mean(2)
    # ruido: gradiente local horizontal medio sobre el 60 % mas plano
    gx = np.abs(np.diff(gris, axis=1)) * 255.0
    ruido = float(np.mean(np.sort(gx.ravel())[:int(gx.size * 0.6)]))
    piel = (h > 5) & (h < 45) & (s > 0.10) & (s < 0.45) & (v > 0.25)
    acen = s > PISO_ACENTO
    # EL TINTE GLOBAL. Lo anadi despues de que r18 saliera entera en azul y
    # mi banda de aceptacion la diera por buena: no tenia ninguna medida para
    # la regla que mas le importa a esta serie, "el entorno es todo gris".
    azul = (b > r + 0.02) & (s > 0.08)
    calido = (r > b + 0.02) & (s > 0.08)
    o = {'tinte_frio': 100 * azul.mean(),
         'tinte_calido': 100 * calido.mean(),
         'sat_media': float(s.mean()),
         'blanco': 100 * ((v > 0.93) & (s < 0.08)).mean(),
         'negro': 100 * (v < 0.07).mean(),
         'ruido': ruido,
         'acento': 100 * acen.mean(),
         'sat_acento': float(np.median(s[acen])) if acen.sum() > 200 else 0.0}
    if piel.sum() > 2000:
        o.update(tono=float(np.median(h[piel])), sat=float(np.median(s[piel])),
                 val=float(np.median(v[piel])), n_piel=int(piel.sum()))
    return o


def juicio(o):
    mal = []
    # el entorno es gris: ni el 8 % del cuadro puede ir teniido de un lado,
    # salvo lo que sea piel o acento, que son poblaciones pequenias
    if o['tinte_frio'] > 8.0: mal.append('TINTE AZUL %.0f%%' % o['tinte_frio'])
    if o['sat_media'] > 0.06: mal.append('saturacion media %.3f' % o['sat_media'])
    if o['blanco'] > 2.0: mal.append('blanco %.1f%%' % o['blanco'])
    if o['negro'] > 2.0: mal.append('negro %.1f%%' % o['negro'])
    if o['ruido'] > 2.5: mal.append('ruido %.2f' % o['ruido'])
    if 'tono' in o:
        if not (BANDA_TONO[0] <= o['tono'] <= BANDA_TONO[1]):
            mal.append('tono %.1f' % o['tono'])
        if not (BANDA_SAT[0] <= o['sat'] <= BANDA_SAT[1]):
            mal.append('satPiel %.3f' % o['sat'])
    if o['acento'] > 0.02 and o['sat_acento'] < PISO_ACENTO:
        mal.append('acento %.2f' % o['sat_acento'])
    return mal


if __name__ == '__main__':
    d = sys.argv[1]
    print('%-30s %6s %6s %7s %7s %7s %7s %7s  %s'
          % ('placa', 'tono', 'satP', '%blanc', '%negro', 'ruido', '%azul', 'satMed', 'fuera de banda'))
    for f in sorted(os.listdir(d)):
        if not f.endswith('_crudo.png') or 'hoja' in f: continue
        o = met(os.path.join(d, f))
        mal = juicio(o)
        print('%-30s %6s %6s %7.2f %7.2f %7.2f %7.1f %7.3f  %s'
              % (f.replace('P3C4_', '').replace('_crudo.png', '')[:30],
                 ('%.1f' % o['tono']) if 'tono' in o else '-',
                 ('%.3f' % o['sat']) if 'sat' in o else '-',
                 o['blanco'], o['negro'], o['ruido'],
                 o['tinte_frio'], o['sat_media'],
                 ', '.join(mal) if mal else 'ok'))
