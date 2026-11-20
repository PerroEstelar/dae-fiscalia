# -*- coding: utf-8 -*-
r"""Inicio de la unidad 3 de «Investigación judicial y forense de desaparición forzada» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third (cuando esté confirmado el nombre), cartón de cierre y outro; el cuerpo
va sin gráficos (ver `base_df_profe`).

**Qué es.** El «Video de presentación de la unidad 3». Empieza en la bienvenida a la unidad y termina en la
despedida; lo que dice antes y después para marcar los videos («Finaliza ese video y comienza…») no entra.

**Tramos de la fuente** (6:34.8 en total; los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última):
- Tramo 1: 0:47:04.6 a 0:53:39.4 (394.8 s). Empieza «Reciban una cordial bienvenida a la unidad…» (2825.03 s; 3.90
  s de silencio antes) y termina «…tres. Les deseamos muchos éxitos en adelante.» (3218.83 s; 1.14 s después).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_df_profe import *  # noqa: E402,F401,F403
from base_df_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(3, 'INICIO', [(2824.58, 3219.40)]))

ITEMS = rotulo(T0)  # noqa: F821
