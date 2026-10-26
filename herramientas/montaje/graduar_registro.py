#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Gradua un set que viene en TRES REGISTROS DE LUZ, no en uno.

POR QUE HACE FALTA
    `graduar_serie` lleva toda placa a 23/84/205, que es el promedio del set
    del C5U1. Eso estaba bien mientras todas las placas se pedian con «flat
    even light» y la unica variacion era ruido del modelo.

    Desde la BIBLIA_puesta_en_escena_P3 las placas se piden en tres
    registros, y la mediana baja ES LA DECISION, no un defecto:

        r05 el muelle al atardecer   p50 53   57,7 % del cuadro bajo 60
        r28 la sala con una lampara  p50 46   72,8 %
        r37 la sala vacia de noche   p50 39   71,4 %

    Llevar esas tres a p50 84 las sube treinta niveles y devuelve la pieza
    exactamente al gris plano del que la estamos sacando. Medido: el plano
    hero de la serie SRPA -el que Sebastian senalo como el mejor- esta en
    p50 45. La curva de la serie, aplicada a el, lo destruiria tambien.

LO QUE SE CONSERVA Y LO QUE SE MUEVE
    Los EXTREMOS siguen siendo casi los de la serie: el negro y el blanco
    tienen que ser los mismos en toda la pieza o los cortes saltan. Lo que
    cambia por registro es el MEDIO TONO, que es justamente lo que un
    registro de luz es.

        dia        23 /  84 / 205    la curva historica de la serie
        contraluz  20 /  60 / 200    mas de la mitad del cuadro en sombra
        hero       16 /  45 / 190    bajo, y sin blanco reventado

    Todo lo demas -el alisado, el croma, la neutralizacion del entorno, el
    tramado y `anclas()`- queda igual. Esto solo cambia a donde apunta.

COMO SE USA
    python graduar_registro.py <entrada> <salida> <mapa.json>

    El mapa es {nombre_de_archivo: 'dia'|'contraluz'|'hero'}.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\montaje')

import numpy as np
from PIL import Image

import grade_placas as G
import graduar_serie as GS

REGISTRO = {
    'dia':       (23, 84, 205),
    'contraluz': (20, 60, 200),
    'hero':      (16, 45, 190),
}

# Cuanto puede estar el crudo por debajo de su registro antes de que el
# techo lo respete en vez de subirlo. Seis niveles es ruido del modelo;
# veinte es una decision de luz.
TOLERANCIA = 6

# Y el techo SOLO aplica si la placa viene oscura de arriba a abajo: si su
# p98 llega al blanco del registro, la mediana baja es una silueta y no una
# decision de exposicion. Ver patch_techo2.
BLANCO_MINIMO = 0.75


# LAS TRES PUERTAS POR LAS QUE ENTRA EL OBJETIVO, Y DOS SON TRAMPAS
#     `G.OBJETIVO` es un modulo-global que `pendiente_de` LEE en cada
#     llamada, asi que moverlo basta para esa.
#
#     Pero `anclas(p2, p50, p98, objetivo=G.OBJETIVO)` y
#     `G.curva(p2, p50, p98, objetivo=OBJETIVO)` lo llevan como VALOR POR
#     DEFECTO, y Python ata un default UNA SOLA VEZ, en el `def`. Reasignar
#     el global despues no los toca.
#
#     La primera version de esto solo movia G.OBJETIVO y GS.anclas, y las
#     veintidos placas de contraluz y hero salieron todas en p50 83-84 -el
#     objetivo de dia- sin un solo error. Lo unico que lo delato fue medir
#     el resultado contra el objetivo declarado. Es la misma leccion de
#     siempre: la herramienta no avisa, la medida si.
def graduar(origen, destino, registro='dia', techo=False):
    """Gradua una placa contra el objetivo de SU registro.

    Con `techo=True` el medio tono del registro es un TECHO y no un
    destino: si la placa YA viene mas oscura que su registro se queda
    donde esta y solo se le fijan los extremos. Ver el encabezado.
    """
    obj = REGISTRO[registro]
    if techo:
        m = medir(origen)
        oscura = m[1] < obj[1] - TOLERANCIA and m[2] < obj[2] * BLANCO_MINIMO
        if oscura:
            obj = (obj[0], int(round(m[1])), obj[2])
    viejo_g = G.OBJETIVO
    viejo_a = GS.anclas.__defaults__
    viejo_c = G.curva.__defaults__
    viejo_p = GS.POR_PENDIENTE
    try:
        G.OBJETIVO = obj
        GS.anclas.__defaults__ = (obj,)
        G.curva.__defaults__ = (obj,)
        GS.POR_PENDIENTE = bool(techo)
        return GS.graduar16(origen, destino)
    finally:
        G.OBJETIVO = viejo_g
        GS.anclas.__defaults__ = viejo_a
        G.curva.__defaults__ = viejo_c
        GS.POR_PENDIENTE = viejo_p


def medir(p):
    a = np.asarray(Image.open(p).convert('RGB')).astype(np.float32)
    l = 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]
    mx, mn = a.max(2), a.min(2)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1), 0)
    return (float(np.percentile(l, 2)), float(np.percentile(l, 50)),
            float(np.percentile(l, 98)), float((l < 60).mean() * 100),
            float(sat.mean()))


if __name__ == '__main__':
    ENT, SAL, MAPA = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(SAL, exist_ok=True)
    m = json.load(open(MAPA, encoding='utf-8'))
    print('%-30s %-10s %17s %17s %7s'
          % ('placa', 'registro', 'crudo p2/p50/p98', 'final p2/p50/p98', 'sat'))
    fuera = []
    for f in sorted(os.listdir(ENT), key=lambda x: x):
        if not f.endswith('.png'):
            continue
        reg = m.get(f, 'dia')
        o, d = os.path.join(ENT, f), os.path.join(SAL, f)
        c = medir(o)
        graduar(o, d, reg)
        v = medir(d)
        obj = REGISTRO[reg]
        if abs(v[1] - obj[1]) > 18:
            fuera.append((f[:-4], reg, round(v[1]), obj[1]))
        print('%-30s %-10s %17s %17s %7.3f'
              % (f[:-4][:30], reg,
                 '%.0f/%.0f/%.0f' % c[:3], '%.0f/%.0f/%.0f' % v[:3], v[4]))
    print('')
    print('placas a mas de 18 niveles de su objetivo:', fuera or 'ninguna')
