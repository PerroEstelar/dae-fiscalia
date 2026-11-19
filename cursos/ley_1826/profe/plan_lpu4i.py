# -*- coding: utf-8 -*-
r"""Inicio de la unidad 4, «Terminación anticipada y mecanismos restaurativos», de «Ley 1826 de 2017: procedimiento
penal especial abreviado y acusador privado» (19 nov 2026). **Entrega provisional.**

Lleva intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_lp_profe`). Cuando se pidan, se agregan a `ITEMS` y sale una v2 sobre el mismo compuesto.

**Fuente.** Drive «VIDEOS CURSO PPA» (`1glwsHbdJS1ltwziPilxhj4od6Ky4o-Cf`), «Copia de bienvenida unidad
4-18/11/2026, 20:45.mp4» (`1o2LWmklI58OFlxvyXP5tv7AyUokjeWxr`, 147.348.165 bytes): 1920×1080, 30 fps parejos, 8.769
cuadros (4:52,3), audio mono. El profe se recorta y va sobre el fondo de la Fiscalía (`recorta_cuadro.py`, ver la
base): la `ORIGINAL` del plan es el recortado. STT (Scribe): 663 palabras; la voz va de 3,60 a 290,68 s (medida en
el audio).

Entra del cuadro 93 (3,10 s: medio segundo antes de la primera palabra) al 8745 (291,50 s: 0,8 s después de la
última).

**Un corte, seco y con plano cerrado.** «Para valorar y consid— y… considerar nuestro aprendizaje» (3:58):
salen los cuadros 7166 a 7210 (238,87 a 240,37 s), del valle que sigue a la primera «y» al silencio que precede
a «considerar» (arranca en 240,39). En ese segundo y medio el profe cambia de postura (diferencia de imagen 11,9;
con cualquier otro cuadro del silencio, de 8,7 a 12,3): una mezcla dejaría un fantasma, así que el corte va seco
y lo que sigue, hasta el final de la frase («…desarrollaremos dos actividades.», cuadro 7343, a mitad de la
pausa de 0,54 s), va en plano cerrado (`CERRADO`: 1728×972 desde la esquina de arriba a la izquierda, con el
panel de logos entero). El salto se lee como cambio de plano.

**Qué se deja.** Un «Eh,» al empezar una frase (2:42,7). **Termina sin despedida**: «Los animo a estudiar
detenidamente el contenido de la unidad».

El lower third entra 1,2 s después de la primera palabra y dura 8 s. Los tiempos de `ITEMS` están en segundos de la
fuente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_lp_profe import *  # noqa: E402,F401,F403
from base_lp_profe import armar_unidad, PROFE, CERRADO  # noqa: E402

globals().update(armar_unidad(4, 'INICIO', [(93, 7166), (7211, 7343, CERRADO), (7343, 8745)]))

ITEMS = [
    ('lt01', 'lt', 4.8, 12.8, PROFE),
]
