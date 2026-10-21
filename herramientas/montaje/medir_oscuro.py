# -*- coding: utf-8 -*-
"""Planitud medida DONDE PUEDE ROMPERSE: en las zonas oscuras y grandes.

POR QUE NO SIRVE "EL 60 % MAS PLANO DEL CUADRO"
    Fue mi error en el Caso 4. Esa medida promedia todo el cuadro, y en una
    placa con papel claro el 60 % mas plano ES EL PAPEL, que aguanta
    cualquier estiron. La mesa oscura -que es la que se rompe, porque ocupa
    una franja estrecha de niveles y el grade la estira cuatro veces- no
    entraba en la cuenta.

    Medido en r01: la medida del cuadro entero daba 0,06 y la daba por buena;
    el recorte 1:1 de la mesa oscura paso de 0,45 a 1,80 de gradiente medio y
    de 6 a 32 en el percentil 99, con moteado visible a simple vista.

LO QUE MIDE
    El gradiente local sobre los pixeles del TERCIO MAS OSCURO, que es donde
    el moteado aparece, y el percentil 99 ademas de la media: el moteado es
    de baja amplitud y gran extension, y una media lo esconde.
"""
import os
import sys

import numpy as np
from PIL import Image


def oscuro(ruta):
    a = np.asarray(Image.open(ruta).convert('L')).astype(np.float32)
    umbral = np.percentile(a, 33)
    m = a <= umbral
    gx = np.abs(np.diff(a, axis=1))
    mg = m[:, :-1] & m[:, 1:]
    if mg.sum() < 1000:
        return 0.0, 0.0
    v = gx[mg]
    return float(v.mean()), float(np.percentile(v, 99))


# ANADIDO EL 21 OCT 2026, POR EL SEGUNDO ERROR DE LA MISMA FAMILIA
#     `oscuro` mide el canal L. El moteado de r01, despues de corregir la
#     poblacion, SEGUIA viendose a 1:1 y la medida ya lo daba por bueno: la
#     mancha era CROMATICA -el rojo, el verde y el azul se separaban entre si-
#     y en luma se compensaba. Una medida de gris no puede ver una mancha de
#     color.
#
#     `croma_oscura` mide lo mismo sobre las dos diferencias de color, que es
#     donde vive. Una placa no se da por buena hasta que pasan LAS DOS.
def croma_oscura(ruta):
    a = np.asarray(Image.open(ruta).convert('RGB')).astype(np.float32)
    L = a.mean(axis=2)
    m = L <= np.percentile(L, 33)
    mg = m[:, :-1] & m[:, 1:]
    if mg.sum() < 1000:
        return 0.0, 0.0
    v = np.zeros(int(mg.sum()), dtype=np.float32)
    for i, j in ((0, 1), (2, 1)):
        d = a[..., i] - a[..., j]
        v += np.abs(np.diff(d, axis=1))[mg]
    return float(v.mean()), float(np.percentile(v, 99))


# Y la contrapartida: que el alisado NO se haya comido dibujo.
#     Se mide el gradiente sobre el DECIL MAS DETALLADO del cuadro -donde si
#     hay dibujo- y se compara con el del crudo. Si baja, el alisado entro
#     donde no debia.
def detalle(ruta):
    a = np.asarray(Image.open(ruta).convert('L')).astype(np.float32)
    gx = np.abs(np.diff(a, axis=1))
    return float(np.percentile(gx, 90)), float(gx.mean())


if __name__ == '__main__':
    import glob
    ref = sys.argv[1]
    print('%-30s %9s %8s %9s %8s %9s'
          % ('placa', 'gx medio', 'gx p99', 'croma', 'croma99', 'detalle'))
    peor = (0, 0, '')
    pc = (0, '')
    for f in sorted(glob.glob(os.path.join(ref, '*.png'))):
        m, p = oscuro(f)
        cm, cp = croma_oscura(f)
        dt = detalle(f)[0]
        if m > peor[0]:
            peor = (m, p, os.path.basename(f))
        if cm > pc[0]:
            pc = (cm, os.path.basename(f))
        print('%-30s %9.2f %8.2f %9.2f %8.2f %9.2f'
              % (os.path.basename(f)[:-4][:30], m, p, cm, cp, dt))
    print('\npeor luma:  %s  medio %.2f  p99 %.2f' % (peor[2], peor[0], peor[1]))
    print('peor croma: %s  medio %.2f' % (pc[1], pc[0]))
