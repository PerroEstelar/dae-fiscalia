#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Quema los seis cartones verbatim del caso Miriam y Mariana.

LA FORMA ES LA QUE SEBASTIAN APROBO EN EL P3C5
    «los cartones debens er verbatum ... no los hagas con la little tiel
    sino el one big block of word, blu tinted bk ann the yellow line».

    O sea: sin antetitulo, un solo bloque, tinte azul translucido, UN filete
    amarillo de una pieza que crece con el bloque, y cada renglon entra
    cuando se dice. Se reusa `verbatim` tal cual: no se reescribe una forma
    que el ya aprobo.

EL TEXTO NO LO ELIJO YO
    Sale de `cartones_df`, que cruza la rejilla de voz con las ranuras y
    devuelve la oracion COMPLETA que se esta oyendo encima del plano. Aqui
    solo se quema.

EL CUERPO SE AJUSTA AL LARGO DE LA FRASE, NO AL REVES
    Las seis frases van de 99 a 220 caracteres. Con un cuerpo fijo la de
    220 se sale del cuadro. Entonces el cuerpo baja por tramos hasta que el
    bloque cabe en la caja, y la frase nunca se corta: cortar una oracion
    para que quepa seria reescribirla, que es justo lo que la regla
    prohibe.
"""
import json
import os
import sys

from PIL import Image, ImageDraw

REPO = r'D:\DAE\_repo\herramientas'
sys.path.insert(0, os.path.join(REPO, 'cartones'))
sys.path.insert(0, os.path.join(REPO, 'prompts'))
import cartones_ta as C                            # noqa: E402
import plan_camara_df as PC                        # noqa: E402

AZUL_FGN = (0, 72, 144)
C.TINTE = AZUL_FGN

import apertura_verbatim_p3c5 as V                 # noqa: E402

# El alto util de la caja de texto: desde y0 hasta dejar el margen inferior
# de la serie. Si el bloque pasa de aqui, baja el cuerpo.
ALTO_UTIL = 470


def medida(frase, cuerpo, salto):
    f = C.fuente(C.F_BOLD, cuerpo)
    d = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
    return len(V.partir(frase, f, d)) * salto


def ajusta(frase):
    """Baja el cuerpo por tramos hasta que el bloque cabe entero."""
    for cuerpo in (52, 48, 44, 40, 36, 33):
        salto = int(round(cuerpo * 1.36))
        if medida(frase, cuerpo, salto) <= ALTO_UTIL:
            return cuerpo, salto
    return 33, 45


if __name__ == '__main__':
    todo = json.load(open(r'D:\DAE\_tmp\df\cartones_df.json', encoding='utf-8'))
    for d in todo:
        sal = os.path.join(PC.RAIZ, PC.CAPS[d['cap']], '02 CARTONES')
        os.makedirs(sal, exist_ok=True)
        cuerpo, salto = ajusta(d['frase'])
        n_ren = medida(d['frase'], cuerpo, salto) // salto
        y0 = int(540 - (n_ren * salto) / 2.0) + 20
        ruta = os.path.join(sal, 'DF_C%d_r%02d_%s_carton.mov'
                            % (d['cap'], d['ranura'], d['nombre']))
        V.verbatim([(d['frase'], d['entrada'])], d['cuadros'], ruta,
                   y0=y0, cuerpo=cuerpo, salto=salto)
        print('   cuerpo %d  salto %d  y0 %d  entra en %d'
              % (cuerpo, salto, y0, d['entrada']), flush=True)
    print('LISTO', flush=True)
