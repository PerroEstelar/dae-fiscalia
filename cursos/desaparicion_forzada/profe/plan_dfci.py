# -*- coding: utf-8 -*-
r"""Inicio del curso de «Investigación judicial y forense de desaparición forzada» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver `base_df_profe`).

**Qué es.** El «Video de inicio del curso». No lee palabra por palabra el texto de la ficha (2.1): es su
bienvenida. Termina en
«Bienvenidos y éxitos en este proceso de formación». Lo que sigue («Ahí termina el primer video. Vamos a comenzar el
segundo video») no entra.

**Tramos de la fuente** (3:22.8 en total; los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última):
- Tramo 1: 0:00:03.6 a 0:03:26.4 (202.8 s). Empieza «Reciban un cordial saludo en nombre de…» (4.04 s; 9.00 s de
  silencio antes) y termina «…y éxitos en este proceso de formación.» (205.68 s; 5.08 s después).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_df_profe import *  # noqa: E402,F401,F403
from base_df_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar('CURSO/INICIO', 'Inicio del curso', 'DF - CURSO - INICIO', 'desaparicionforzada - CURSO - INICIO', 'DFCI',
                       [(3.59, 206.38)]))

ITEMS = rotulo(T0)  # noqa: F821
