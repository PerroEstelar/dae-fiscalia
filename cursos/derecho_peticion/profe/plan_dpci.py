# -*- coding: utf-8 -*-
r"""Inicio del curso de «Derecho de petición y acción de tutela» (20 nov 2026). **Entrega provisional** (ver `base_dp_profe`).

Fuente: `VIDEO 1 PRESENTACION GENERAL DEL CURSO - TOMA1.mp4`.

**Cortes** (los bordes van a la mitad del silencio, hasta 0,45 s antes de la primera palabra y 0,7 s después de la
última; seis cuadros de mezcla en cada corte):
- Sale el principio (0:00–0:23,9): un primer intento que empieza a mitad de frase («Dependencia. Una persona pide…») y
  «Listo, ya puedes empezar. Apenas yo me quito». Empieza en «Llega un mensaje a su dependencia».
- Sale de 191,42 a 213,91: el primer intento de «En la primera, derecho de petición…», que se traba («la solicitud
  de, de decir y decidir») y «Ahí deberíamos cortar. Camilo, por favor».
- Sale de 412,89 a 428,95: el primer intento de «Tampoco se trata de memorizar artículos…» («El recurso…
  Suspendamos ahí, por favor, Camilo»).
- Termina en «…la Escuela de Altos Estudios de la Fiscalía».

**v2 (20 nov 2026):** el rótulo entra al empezar, a 1,5 s del primer tramo, como en los demás videos. En la v1
entraba cuando dice su nombre («Mi nombre es Óscar Jairo Fonseca Fonseca», 97,9 s de la fuente, 1:31 del video) y
Sebastián no lo vio: «por lo menos en uno de los videos no veo el rótulo del profesor».
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dp_profe import *  # noqa: E402,F401,F403
from base_dp_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar('CURSO/INICIO', 'Inicio del curso', 'DP - CURSO - INICIO', 'derechodepeticion - CURSO - INICIO', 'DPCI',
                       'VIDEO 1 PRESENTACION GENERAL DEL CURSO - TOMA1.mp4', [(23.85, 191.42), (213.91, 412.89), (428.95, 539.64)]))

VERSION = 2
ITEMS = rotulo(T0 + 1.5)  # noqa: F821
