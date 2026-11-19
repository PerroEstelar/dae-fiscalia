# -*- coding: utf-8 -*-
r"""Inicio del curso «Justicia restaurativa en la práctica del fiscal» (18 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, tres lower thirds, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_jr_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** `jr_inicio_curso_fuente.mp4` (Drive del curso → VIDEOS, «Justica restuaraativa-  inicio curso.mp4»,
`1GOxoYu5V3zS3XvNvsLddTvv8AElk73B4`, del 18 nov): 1920×1080, 30 fps parejos, 36.485 cuadros (20:16,2), BT.601, pico de
−2,6 dBFS. Como el cierre, trae pegados una intro (cuadros 0–277) y un outro (desde el 36208; el 36206 y el 36207
son blancos): no entran.

**Qué es.** La bienvenida de los dos coautores, en los mismos dos mosaicos del cierre. Habla Víctor Hugo Ospina
Vargas (izquierda) de 0:10,0 a 7:46,8; Martín Posada Martínez (derecha) de 7:48,6 a 12:49,0; y cierra Víctor de
12:52,0 a 20:06,0. STT (Scribe): 2.100 palabras.

**Un corte.** Víctor se enreda y lo pide él mismo: «Están en su despacho y tienen un caso contra el señor o la
señora tal por tales delitos y cómo puedo, en ese caso, con unas víctimas y con todos los, eh, con todos los… con
todo el — ahí, ahí, pequeño corte. Cuentan, est—, eh, perdón.» y retoma: «Se encuentran en su despacho de fiscales
y desean, en un caso concreto…». Sale del cuadro 4392 (146,40 s; «…al caso concreto.» termina en 146,24) al 5285
(176,17 s; «Se encuentran» empieza en 176,34): 29,8 s. Queda «…al caso penal, al caso concreto. | Se encuentran
en su despacho de fiscales…». Es un corte directo: con dos mosaicos no hay plano cerrado que lo disimule.
No hay más reinicios (se buscó «repito», «perdón», «corte», «de nuevo», frases repetidas y pausas; las tres pausas
de más de 2,8 s son cambios de idea o de quien habla).

Entra del cuadro 280 (el profe empieza en el 278; primera palabra en 9,98 s) al 36206 (0,9 s después de la última
palabra, que termina en 1205,9 s, y justo antes del blanco). Los tiempos están en segundos de la fuente.

**Lower thirds.** Uno por persona al principio, uno tras otro, y el de Martín otra vez cuando toma la palabra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_jr_profe import *  # noqa: E402,F401,F403
from base_jr_profe import armar, VICTOR, MARTIN, CLIP0, FPS, FQ  # noqa: E402

globals().update(armar('jr_inicio_curso_fuente.mp4', 'INICIO DEL CURSO', 'Inicio del curso', 'JR - CURSO - INICIO',
                       'justiciarestaurativa - CURSO - INICIO', 'JRCI', 280, 36206))

TRAMOS = [(T0, 4392 / FQ, None), (5285 / FQ, T1, None)]  # noqa: F821


def cuadro(t):
    """Segundos de la fuente → cuadro de la línea, descontando el corte."""
    acum = 0.0
    for a, b, _w in TRAMOS:
        if a - 1e-6 <= t <= b + 1e-6:
            return CLIP0 + int(round((acum + t - a) * FPS))
        acum += b - a
    raise ValueError('%.2f cae en el corte' % t)


ITEMS = [
    ('lt01', 'lt', 11.0, 18.5, VICTOR),
    ('lt02', 'lt', 19.2, 26.7, MARTIN),
    ('lt03', 'lt', 469.6, 477.6, MARTIN),
]
