# -*- coding: utf-8 -*-
r"""Inicio de la unidad 1 de «Derecho de petición y acción de tutela» (20 nov 2026). **Entrega provisional** (ver `base_dp_profe`).

Fuente: `VIDEO2 - PRESENTACION UNIDAD 1 - TOMA 2.mp4`.

**Se compone de la toma 2**, que trae el guion entero en tres tramos separados por «Pausemos ahí, por favor». La
toma 1 es un primer intento (llega a la lección 2 y «cortemos ahí, Camilo»): no entra.
- Sale el principio (0:00–1:29,4): «se me desconectó la cámara», un intento que se corta («Lo tengo muy rápido
  ahora. Perdón») y otro («Esto no me está funcionando»). Empieza en «Una persona se acerca a la fiscalía y dice…».
- Sale de 231,80 a 239,95: «Pausemos ahí, por favor, Camila».
- Sale de 346,29 a 358,13: «Una idea será especialmente importante responder de— una idea—» y «Pausemos ahí»; sigue
  la toma buena de la misma frase.
- Termina en «…identificar qué nos corresponde hacer» (sale «Hasta ahí. Listo, Camilo»).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dp_profe import *  # noqa: E402,F401,F403
from base_dp_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(1, 'INICIO', 'VIDEO2 - PRESENTACION UNIDAD 1 - TOMA 2.mp4',
                             [(89.37, 231.80), (239.95, 346.29), (358.13, 500.97)]))

ITEMS = rotulo(T0 + 1.5)  # noqa: F821
