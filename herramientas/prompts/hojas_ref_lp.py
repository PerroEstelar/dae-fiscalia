# -*- coding: utf-8 -*-
r"""Hojas de personaje del curso Ley 1826 con la piel de la serie (es `hojas_ref_dh`).

Las hojas de Seedream salieron con la piel durazno-rosada en siete de nueve
personajes (ver `piel_ref`). Como entran como PRIMERA referencia de cada
placa, la piel se copiaba a todo el curso. Cada hoja pasa por la misma
limpieza de bandas que una placa (`lp_pieza.limpia`: frio y ambar fuera,
topes de piel; con acento solo Carmen) y despues por `piel_ref`.

La hoja original no se toca: la corregida va a
    00 PERSONAJES\_piel_ref\DH_HOJA_<personaje>.png
y es la que se sube a Magnific (`subir_lp.py` con "archivo").

    python hojas_ref_lp.py
"""
import os
import sys

sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\montaje')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rutas_lp as R                    # noqa: E402
from lp_pieza import limpia             # noqa: E402
from piel_ref import piel_ref, medir    # noqa: E402
from PIL import Image                   # noqa: E402

CON_ACENTO = {'maria', 'mariaelena', 'ciudadana'}
QUIENES = (sys.argv[1:] or ['maria', 'supervisor', 'mariaelena', 'fiscal_mujer',
                           'mediador', 'ciudadana', 'estudiante', 'defensor'])

dst_d = os.path.join(R.PERSONAJES, '_piel_ref')
os.makedirs(dst_d, exist_ok=True)
for q in QUIENES:
    src = os.path.join(R.PERSONAJES, 'LP_HOJA_%s.png' % q)
    dst = os.path.join(dst_d, 'LP_HOJA_%s.png' % q)
    antes = medir(Image.open(src).convert('RGB'))
    limpia(src, dst, q in CON_ACENTO, True)
    im = piel_ref(Image.open(dst).convert('RGB'))
    im.save(dst)
    print('%-14s piel p50 %.3f -> %.3f  p90 %.3f -> %.3f  rosado %.2f%% -> %.2f%%'
          % (q, antes['p50'], medir(im)['p50'], antes['p90'], medir(im)['p90'],
             antes['rosado'], medir(im)['rosado']), flush=True)
print('LISTO')
