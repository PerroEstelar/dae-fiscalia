# -*- coding: utf-8 -*-
r"""Inicio de la unidad 1 de «Investigación judicial y forense de desaparición forzada» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third (cuando esté confirmado el nombre), cartón de cierre y outro; el cuerpo
va sin gráficos (ver `base_df_profe`).

**Qué es.** El «Video de presentación de la unidad 1». Empieza en la bienvenida a la unidad y termina en la
despedida; lo que dice antes y después para marcar los videos («Finaliza ese video y comienza…») no entra. Antes
dice «Unidad uno», como rótulo, y hace una pausa de 3,6 s: no entra.

**Tramos de la fuente** (6:36.9 en total; los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la última):
- Tramo 1: 0:03:40.5 a 0:10:17.4 (396.9 s). Empieza «Iniciamos hoy la unidad uno titulada: comprensión…» (220.94
  s; 3.64 s de silencio antes) y termina «…Bienvenidos y bienvenidas a la unidad uno.» (616.72 s; 2.72 s después).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_df_profe import *  # noqa: E402,F401,F403
from base_df_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(1, 'INICIO', [(220.49, 617.42)]))

ITEMS = rotulo(T0)  # noqa: F821
