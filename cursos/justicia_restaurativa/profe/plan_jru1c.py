# -*- coding: utf-8 -*-
r"""Cierre de la unidad 1 de «Justicia restaurativa en la práctica del fiscal» (18 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower thirds, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_jr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** `jr_u1_cierre_fuente.mp4` (Drive del curso → VIDEOS, «Justica restuaraativa-  Unidad 1 cierre.mp4»,
`1n-OFMmvE1RjNZL4HWB1yWu41y6wLcjc0`, 179 MB): 1920×1080, 30 fps parejos, 18.835 cuadros (10:27,9), BT.601, pico de
−0,9 dBFS. Trae la intro pegada (cuadros 0–277) y **no trae outro**: la conversación llega al último cuadro (brillo
medido en los 18.835 cuadros: parejo en 153 desde el 278). Entra del cuadro 280 al 18835; la última palabra termina
en 627,34 s, 0,5 s antes del final del archivo.

**Qué es.** Los mismos tres mosaicos del inicio de la unidad (ver `plan_jru1i`): Martín Posada Martínez arriba a la
izquierda, Jhonatan Sandoval arriba a la derecha y Víctor Hugo Ospina Vargas abajo al centro. Víctor abre y pregunta
(0:11,5 a 1:33,7); responde Jhonatan (1:33,8 a 4:17,5), después Martín (5:04,5 a 8:18,5) y cierra Víctor (8:21,2 a
10:27,3). STT (Scribe): 1.261 palabras en la fuente.

**Un corte de 46,1 s** (cuadros 7742 a 9126 de la fuente; 258,07 a 304,20 s). Martín arranca, se traba y lo dice
(«De acuerdo, pues al cerrar espero que— se esperaría más bien que… Mmm, ahí me tosté, espérense. Ya.»), pregunta
fuera de la grabación cómo referirse a quienes cursan («¿estudiantes o…?»), Víctor le contesta («Se puede decir
estudiantes o fiscales…») y Martín vuelve a empezar: «Vale. Pues al final, al finalizar esta unidad, yo creo…».
Sale todo eso, «Vale.» incluido. Queda «…la conflictividad que se acerca por medio de modelo penal. | Pues al final,
al finalizar esta unidad…»: «penal.» termina en 257,54 s y «Pues» empieza en 304,54. Es un corte directo: con tres
mosaicos no hay plano cerrado que lo disimule. No hay más reinicios (las otras pausas de más de 2 s son cambios de
quien habla).

**Lower thirds.** Los del inicio de la unidad (dos renglones, en el blanco libre de abajo), cada uno cuando esa
persona empieza a hablar. Los tiempos están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_jr_profe import *  # noqa: E402,F401,F403
from base_jr_profe import armar, CLIP0, FPS, FQ  # noqa: E402
from plan_jru1i import VICTOR_U, MARTIN_U, TERCERO, _LTU  # noqa: E402  (los rótulos de tres mosaicos)

globals().update(armar('jr_u1_cierre_fuente.mp4', 'UNIDAD 1/CIERRE',
                       'Unidad 1. Bases conceptuales y marco jurídico de la justicia restaurativa',
                       'JR - U1 - CIERRE', 'justiciarestaurativa - U1 - CIERRE', 'JRU1C', 280, 18835))

TRAMOS = [(T0, 7742 / FQ, None), (9126 / FQ, T1, None)]  # noqa: F821


def cuadro(t):
    """Segundos de la fuente → cuadro de la línea, descontando el corte."""
    acum = 0.0
    for a, b, _w in TRAMOS:
        if a - 1e-6 <= t <= b + 1e-6:
            return CLIP0 + int(round((acum + t - a) * FPS))
        acum += b - a
    raise ValueError('%.2f cae en el corte' % t)


ITEMS = [
    ('lt01', 'lt', 13.0, 20.5, VICTOR_U),
    ('lt02', 'lt', 94.6, 102.1, (TERCERO[0], TERCERO[1], dict(_LTU, x=1440, top=575))),
    ('lt03', 'lt', 305.5, 313.0, MARTIN_U),
]
