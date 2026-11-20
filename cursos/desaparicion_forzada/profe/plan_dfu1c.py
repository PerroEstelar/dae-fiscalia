# -*- coding: utf-8 -*-
r"""Cierre de la unidad 1 de «Investigación judicial y forense de desaparición forzada» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver `base_df_profe`).

**Qué es.** El «Video de cierre de la unidad 1» (lo que el profe llama «finalización y síntesis»). Va antes que las
retroalimentaciones en la grabación; en el aula va al final de la unidad. **Va la segunda toma.** En la primera
(10:33–14:54) el profe dice «artículo ciento sesenta y seis» por el 165, se enreda en el «Tercero», lo repite y pide
volver a empezar («vamos a suspender porque creo que repetí este punto… voy a repetir desde finalización y síntesis
de la unidad uno»); la segunda, de 15:26,8 a 18:42,4, va entera y dice «ciento sesenta y cinco».

**Tramos de la fuente** (3:16.7 en total; los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última):
- Tramo 1: 0:15:26.4 a 0:18:43.0 (196.7 s). Empieza «Felicitaciones por haber completado la unidad uno…» (926.84
  s; 4.62 s de silencio antes) y termina «…para poner en marcha la búsqueda efectiva.» (1122.35 s; 1.66 s después).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_df_profe import *  # noqa: E402,F401,F403
from base_df_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(1, 'CIERRE', [(926.39, 1123.05)]))

ITEMS = rotulo(T0)  # noqa: F821
