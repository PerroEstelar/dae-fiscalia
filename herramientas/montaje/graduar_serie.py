#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El mismo grade de la serie, pero en coma flotante y con tramado al bajar.

EL PROBLEMA, DIAGNOSTICADO DESPUES DE ROMPER EL SET DOS VECES
    Las placas del Caso 4 salieron del modelo MUCHO mas claras y planas que
    las del Caso 3. Medido sobre los percentiles p2/p50/p98:

        Caso 3 aprobado, final      23,6 /  85,0 / 201,6
        Caso 4 crudo                68,0 / 133,9 / 183,6
        objetivo de la serie        23   /  84   / 205

    O sea: al Caso 3 el grade tenia que estirarlo poco y al Caso 4 tiene que
    estirarlo casi el doble. Y ahi esta el dano: la mesa oscura de estas
    placas ocupa una franja estrechisima de niveles -43 a 112 en r01- y
    estirarla cuatro veces convierte el escalonado de 8 bits en MOTEADO
    visible, con manchas de color. Medido a 1:1 en r01: gradiente medio de
    0,45 a 1,80 y percentil 99 de 6 a 32.

    No se arregla bajando la mezcla: a mezcla 0,25 el moteado seguia ahi,
    porque el problema no es cuanto se estira sino que se estira SOBRE OCHO
    BITS. Entre dos niveles contiguos de un gris plano no hay nada que
    repartir, y la curva los separa en dos mesetas visibles.

LA SOLUCION: NO CUANTIZAR HASTA EL FINAL
    La curva se aplica en float32 sobre el array, no como LUT de 256 entradas
    sobre la imagen de 8 bits, y al volver a 8 bits se anade un tramado
    triangular de +-0,5 niveles. El tramado rompe las mesetas en ruido de
    amplitud sub-nivel, que es invisible y ademas desaparece al comprimir el
    video.

    Es la misma idea que `aplanar.py` por el otro lado: alli se quitaba grano
    que sobraba, aqui se anade un ruido minimo para que no aparezca el que de
    verdad se ve.

EL TRAMADO NO BASTO, Y POR QUE
    Corrido sobre las 36, el tramado dejo 6 placas por encima de la
    referencia y una en 7,62. El tramado arregla el REDONDEO FINAL; aqui el
    problema es la AMPLIFICACION: la mitad oscura de estos crudos vive en una
    franja de dos a seis niveles y la curva la abre a sesenta. No hay nada que
    tramar porque no hay nada en medio.

    Por eso antes de la curva entra `suave.alisar`, que alisa en coma flotante
    SOLO lo que ya esta medido como plano y oscuro. Las dos cosas juntas
    -alisar antes, tramar despues- bajan la peor zona oscura de 7,62 a
    por debajo de la referencia del Caso 3. El alisado tiene que ir en el
    MISMO float que la curva: pasando por un PNG de 8 bits en medio, r01
    bajaba solo de 5,38 a 1,80 en vez de a 1,16.

NO CAMBIA NADA MAS
    Misma curva PCHIP, mismos percentiles, mismo objetivo, misma neutralizacion
    y mismo tope de dureza. Solo cambia la aritmetica.
"""
import os
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, '.')
import grade_placas as G
import suave


def _lut_float(p2, p50, p98):
    """La misma curva de grade_placas, evaluada en 4096 puntos."""
    p50, _ = anclas(p2, p50, p98)
    lut8 = G.curva(p2, p50, p98)
    x = np.arange(256, dtype=np.float32)
    y = np.array(lut8, dtype=np.float32)
    xf = np.linspace(0, 255, 4096, dtype=np.float32)
    return xf, np.interp(xf, x, y).astype(np.float32)


def pendiente_de(a):
    """Cuanto va a abrir la curva el tramo mas estirado de esta placa."""
    L = a.mean(axis=2)
    p2, p50, p98 = (float(np.percentile(L, p)) for p in (2, 50, 98))
    p50, _ = anclas(p2, p50, p98)
    o = G.OBJETIVO
    return max((o[1] - o[0]) / max(p50 - p2, 0.5),
               (o[2] - o[1]) / max(p98 - p50, 0.5))


def graduar16(origen, destino, mezcla=1.0, semilla=7, alisar=True):
    a = np.asarray(Image.open(origen).convert('RGB')).astype(np.float32)
    mascara = 0.0
    if alisar:
        a, mascara = suave.alisar(a, pendiente_de(a))
        a, _ = suave.alisar_croma(a)
    out = np.empty_like(a)
    for c in range(3):
        ch = a[..., c]
        p2, p50, p98 = (float(np.percentile(ch, p)) for p in (2, 50, 98))
        xf, yf = _lut_float(p2, p50, p98)
        out[..., c] = np.interp(ch, xf, yf)
    if mezcla < 1.0:
        out = a + (out - a) * mezcla
    if alisar:
        out, _ = suave.neutralizar_entorno(out)
    # tramado triangular de +-0,5 niveles, justo antes de cuantizar
    rng = np.random.default_rng(semilla)
    d = rng.random(out.shape, dtype=np.float32) - rng.random(out.shape, dtype=np.float32)
    b = np.clip(out + d * 0.5, 0, 255).astype(np.uint8)
    Image.fromarray(b).save(destino)
    return ([float(np.percentile(b[..., 1], p)) for p in (2, 50, 98)], mascara)



# --------------------------------------------------------------- anclas
# EL HALLAZGO DE FONDO, 21 OCT 2026, VISTO A 1:1 Y NO EN LA MEDIDA
#     Ni el tramado ni el alisado salvaban r01 y r39, y ademas aparecio el
#     mismo dano por ARRIBA en r17, r26, r33, r31, r18 y r15: el papel
#     convertido en ruido de arcoiris. La medida de zona oscura los daba
#     todos por buenos. Mirados a 1:1, ocho de las 36 estaban rotas.
#
#     La causa no es el grade: es DONDE SE ANCLA.
#
#     La curva de la serie fija tres puntos -p2 al 23, p50 al 84, p98 al 205-
#     y eso supone un histograma repartido. En una toma cenital de papel sobre
#     mesa, el papel o la mesa ocupan mas de la mitad del cuadro con UN SOLO
#     valor, asi que la MEDIANA CAE DENTRO DE ESA MANCHA. Medido en el crudo:
#
#         r01  p2  61   p50  63   p98 113     la mesa es p2 y p50 a la vez
#         r33  p2  84   p50 209   p98 211     el papel es p50 y p98 a la vez
#
#     Entonces la curva tiene que llevar dos niveles a sesenta -pendiente x30-
#     y lo que estira es el escalonado. Y de paso arrastra el papel de r33 al
#     gris medio, que es ademas una lectura falsa de la placa.
#
#     Ninguna herramienta posterior lo arregla porque el dano se crea en la
#     curva. Lo que hay que quitar es el ancla del medio: cuando la mediana
#     esta pegada a un extremo, no describe un medio tono, describe la mancha.
#
#     Con el ancla corrida a la recta, la pendiente de las ocho cae de 24-60 a
#     1,3-4,4, que es la banda de las placas que si salieron bien.
FRANJA_MINIMA = 20.0        # distancia minima de la mediana a cada extremo


def anclas(p2, p50, p98, objetivo=G.OBJETIVO):
    """Si la mediana esta dentro de una mancha plana, se deja de usar.

    Devuelve el p50 que hay que pasarle a la curva: el medido, o el que cae
    sobre la recta que une los dos extremos, que convierte los tres puntos en
    un mapa de dos y deja la pendiente en (205-23)/(p98-p2).
    """
    if (p50 - p2) >= FRANJA_MINIMA and (p98 - p50) >= FRANJA_MINIMA:
        return p50, False
    f = (objetivo[1] - objetivo[0]) / float(objetivo[2] - objetivo[0])
    return p2 + f * (p98 - p2), True


if __name__ == '__main__':
    from medir_oscuro import oscuro, croma_oscura, detalle
    ENT, SAL = sys.argv[1], sys.argv[2]
    os.makedirs(SAL, exist_ok=True)
    print('%-26s %13s %13s %5s %6s %6s %6s %6s'
          % ('placa', 'crudo', 'final', 'masc', 'oscuro', 'croma', 'det cr', 'det fn'))
    peor = pcr = 0.0
    bajas = []
    for f in sorted(os.listdir(ENT)):
        if not f.endswith('.png'):
            continue
        o = os.path.join(ENT, f); d = os.path.join(SAL, f)
        a0 = np.asarray(Image.open(o).convert('L')).astype(np.float32)
        c0 = [float(np.percentile(a0, p)) for p in (2, 50, 98)]
        d0 = detalle(o)[0]
        p, masc = graduar16(o, d)
        oc1, cr1, d1 = oscuro(d)[0], croma_oscura(d)[0], detalle(d)[0]
        peor, pcr = max(peor, oc1), max(pcr, cr1)
        if d1 < d0:
            bajas.append(f)
        print('%-26s %13s %13s %4.0f%% %6.2f %6.2f %6.2f %6.2f'
              % (f[:-4][:26], '%.0f/%.0f/%.0f' % tuple(c0),
                 '%.0f/%.0f/%.0f' % tuple(p), masc, oc1, cr1, d0, d1))
    print('\npeor zona oscura: luma %.2f  croma %.2f'
          '   (Caso 3 aprobado: luma 1,48  croma 4,84)' % (peor, pcr))
    print('placas donde el detalle BAJO respecto al crudo: %s'
          % (', '.join(b[:-4] for b in bajas) if bajas else 'ninguna'))
