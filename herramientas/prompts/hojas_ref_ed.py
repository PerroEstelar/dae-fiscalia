# -*- coding: utf-8 -*-
r"""Hojas de personaje del curso Enfoque diferencial con la piel de la serie (es `hojas_ref_dh`).

Las hojas de Seedream salieron con la piel durazno-rosada en siete de nueve
personajes (ver `piel_ref`). Como entran como PRIMERA referencia de cada
placa, la piel se copiaba a todo el curso. Cada hoja pasa por la misma
limpieza de bandas que una placa (`ed_pieza.limpia`: frio y ambar fuera,
topes de piel; con acento solo Carmen) y despues por `piel_ref`.

La hoja original no se toca: la corregida va a
    00 PERSONAJES\_piel_ref\DH_HOJA_<personaje>.png
y es la que se sube a Magnific (`subir_ed.py` con "archivo").

    python hojas_ref_ed.py
"""
import os
import sys

sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\montaje')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rutas_ed as R                    # noqa: E402
from ed_pieza import limpia             # noqa: E402
from piel_ref import piel_ref, medir    # noqa: E402
from PIL import Image                   # noqa: E402

CON_ACENTO = {'yolanda', 'madre', 'valentina'}
CHALECO = {'wilmer'}
QUIENES = (sys.argv[1:] or ['molano', 'yolanda', 'jairo', 'mauricio', 'wilmer',
                           'madre', 'fiscal_c4', 'valentina'])

dst_d = os.path.join(R.PERSONAJES, '_piel_ref')
os.makedirs(dst_d, exist_ok=True)
for q in QUIENES:
    src = os.path.join(R.PERSONAJES, 'ED_HOJA_%s.png' % q)
    dst = os.path.join(dst_d, 'ED_HOJA_%s.png' % q)
    antes = medir(Image.open(src).convert('RGB'))
    # 4 nov: Wilmer con el uniforme de la Policia Nacional (verde y chaleco)
    limpia(src, dst, q in CON_ACENTO, True, q in CHALECO)
    im = piel_ref(Image.open(dst).convert('RGB'))
    im.save(dst)
    print('%-14s piel p50 %.3f -> %.3f  p90 %.3f -> %.3f  rosado %.2f%% -> %.2f%%'
          % (q, antes['p50'], medir(im)['p50'], antes['p90'], medir(im)['p90'],
             antes['rosado'], medir(im)['rosado']), flush=True)
print('LISTO')
