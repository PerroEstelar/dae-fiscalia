#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Gradua DOS placas que son una rima con UNA SOLA curva.

POR QUE HACE FALTA
    Una rima visual -dos planos con la misma camara y la misma mesa, donde lo
    unico que cambia es lo que hay encima- se rompe en el grade si cada placa
    se gradua por su cuenta. Medido en el P3C5, r33 contra r35:

        crudo       r33 mesa 118      r35 mesa  81
        por separado  r33 65/186/193 -> 23/197/205   mesa en gris medio
                      r35  80/81/181 -> 22/ 23/204   mesa en casi negro

    Las dos mesas acabaron a 174 niveles de distancia y el espectador ve dos
    habitaciones distintas, no la misma mesa dos veces. Y la rima ES el
    argumento de la pieza: cuatro cosas de un lado, dos y mesa vacia del otro.

    No lo arregla pegar las dos y graduar: los crudos ya traian la mesa en
    118 y en 81, y una curva comun sobre entradas distintas da salidas
    distintas.

LO QUE SI FUNCIONA, EN DOS PASOS
    1. IGUALAR LA ENTRADA. Se mide el valor de la mesa en cada crudo como la
       moda del BORDE del cuadro -en una cenital de papel sobre mesa el borde
       es mesa en las dos- y se desplaza la segunda placa hasta la primera.
       Un desplazamiento plano sobre una superficie plana es invisible.
    2. UNA SOLA CURVA. Se pegan las dos en una imagen, se gradua esa, y se
       parte. Asi la curva sale de un histograma que contiene las dos y cae
       igual sobre las dos por construccion.

    Resultado medido: mesa en 84 y 83. Un nivel de diferencia.

Y DE PASO ARREGLA OTRA COSA
    Con las dos pegadas el histograma queda repartido, asi que `anclas()` no
    se dispara y entra la curva de tres puntos completa: 23/84/204, que es el
    objetivo de la serie. Graduada sola, r35 caia en 22/23/204.
"""
import os
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import graduar_serie as GS


def mesa(ruta_o_array):
    """El valor del plano de fondo: la moda del borde del cuadro."""
    a = (np.asarray(Image.open(ruta_o_array).convert('L'))
         if isinstance(ruta_o_array, str) else ruta_o_array)
    h, w = a.shape[:2]
    m = max(8, h // 20)
    borde = np.concatenate([a[:m].ravel(), a[-m:].ravel(),
                            a[:, :m].ravel(), a[:, -m:].ravel()])
    return int(np.bincount(borde.astype(np.uint8), minlength=256).argmax())


def graduar_par(crudo_a, crudo_b, salida_a, salida_b, temp=None):
    temp = temp or os.path.dirname(salida_a)
    os.makedirs(temp, exist_ok=True)
    ia = Image.open(crudo_a).convert('RGB')
    ma, mb = mesa(crudo_a), mesa(crudo_b)
    ib = np.asarray(Image.open(crudo_b).convert('RGB')).astype(np.float32)
    ib = Image.fromarray(np.clip(ib + (ma - mb), 0, 255).astype(np.uint8))

    par = Image.new('RGB', (ia.width + ib.width, ia.height))
    par.paste(ia, (0, 0))
    par.paste(ib, (ia.width, 0))
    pc = os.path.join(temp, '_par_crudo.png')
    pg = os.path.join(temp, '_par_grade.png')
    par.save(pc)
    pct, masc = GS.graduar16(pc, pg)

    g = Image.open(pg).convert('RGB')
    g.crop((0, 0, ia.width, ia.height)).save(salida_a)
    g.crop((ia.width, 0, g.width, ia.height)).save(salida_b)
    os.remove(pc)
    os.remove(pg)
    return {'mesa_crudo': (ma, mb), 'desplazamiento': ma - mb,
            'percentiles': pct, 'mascara': masc,
            'mesa_final': (mesa(salida_a), mesa(salida_b))}


if __name__ == '__main__':
    r = graduar_par(*sys.argv[1:5])
    print('mesa en el crudo: %d y %d  ->  desplazamiento %+d'
          % (r['mesa_crudo'][0], r['mesa_crudo'][1], r['desplazamiento']))
    print('curva comun: %.0f/%.0f/%.0f  ·  mascara %.0f %%'
          % (tuple(r['percentiles']) + (r['mascara'] * 100,)))
    print('mesa graduada: %d y %d  ->  diferencia %d'
          % (r['mesa_final'][0], r['mesa_final'][1],
             abs(r['mesa_final'][0] - r['mesa_final'][1])))
