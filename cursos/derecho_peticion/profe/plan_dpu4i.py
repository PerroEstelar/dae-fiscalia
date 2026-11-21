# -*- coding: utf-8 -*-
r"""Inicio de la unidad 4 de «Derecho de petición y acción de tutela» (20 nov 2026). **Entrega provisional** (ver `base_dp_profe`).

Fuente: `VIDEO5 - PRESENTACION UNIDAD 4- TOMA 1.mp4`.

- Empieza en «Una orden judicial llega a la Fiscalía».
- Sale de 117,92 a 139,07: el primer intento de «Antes de responder, necesitamos leer…» («¿Qué hacemos, eh, para—?
  Suspendamos ahí, por favor»).
- Sale de 351,86 a 367,25: «Aunque no se imponga una sanción, una orden de pendiente…», «Suspendamos ahí, por favor»,
  «Me colgué». La toma siguiente arranca en «Por eso, la respuesta institucional…».
- Sale de 442,08 a 478,38: la frase que él mismo pidió repetir («Utilice matrices y e-instrumentos…»), «Nos paremos
  ahí… Voy a repetir esta frase» y la segunda lectura de «Pregúntese qué información hace falta…», que ya quedó dicha.
  Sigue «Utilice las listas de verificación y la retroalimentación…».
- Termina en «…sus resultados pueden verificarse» (sale «Listo. Es que uno puede separar antes»).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dp_profe import *  # noqa: E402,F401,F403
from base_dp_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(4, 'INICIO', 'VIDEO5 - PRESENTACION UNIDAD 4- TOMA 1.mp4',
                             [(5.17, 117.92), (139.07, 351.86), (367.25, 442.08), (478.38, 529.78)]))

ITEMS = rotulo(T0 + 1.5)  # noqa: F821
