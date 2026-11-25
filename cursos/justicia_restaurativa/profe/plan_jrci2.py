# -*- coding: utf-8 -*-
r"""Bienvenida al curso «Justicia restaurativa en la práctica del fiscal», **profe a cámara** (25 nov 2026). **Entrega
provisional; es la versión 2 del inicio del curso** (la v1 es la conversación de los dos coautores, `plan_jrci`).

Lleva intro, cartón de título, un lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_jr_camara`).

**Fuente.** `jr_inicio_curso2_fuente.mp4` (enlace duro de «VIDEO JUSTICIA RESTAURATIVA TOMA 2.mp4», que llegó en la carpeta
del cierre del curso: por el nombre parece otra toma del cierre, pero es la bienvenida): 22.332 cuadros (12:24,4), 30
cuadros casi parejos (29,9999), pico de −0,1 dBFS. STT (Scribe): 1.163 palabras.

**Qué es.** Víctor Hugo Ospina Vargas abre con una pregunta («¿Cómo superar una cultura punitivista…?»), da la bienvenida,
se presenta, enuncia la competencia general y recorre las cuatro unidades.

**Un corte** (segundos de la fuente; cambia de plano): en la unidad 2 se pierde («…instituciones procesales que
permiten— una pausa, por favor, que aquí me, me equivoqué») y retoma desde «Partiremos del sustento constitucional…».
Sale 313,20–371,25 (58,05 s): queda «…¿cuándo y cómo es viable aplicar este enfoque en el proceso penal colombiano? |
Partiremos del sustento constitucional como el artículo doscientos cincuenta…», una sola vez.
Entra en 3,40 (la primera palabra empieza en 4,04) y termina en 742,50 (0,8 s después de «…recorrido formativo.»). Quedan
11:21,0.

Se dejan los tropiezos menores («la lesividad y cof— y conflit— la lesividad y conflictividad», «concentra— esta se
concentra», «Las— los invito»). Scribe oye «Espina» y «Martín Posada Martín»: en los subtítulos van Ospina y Martínez.

**Lower third.** Cuando se presenta: «Mi nombre es Víctor Hugo Ospina Vargas…» (82,2 s de la fuente).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_jr_camara import *  # noqa: E402,F401,F403
from base_jr_camara import armar_camara, CERRADO, VICTOR_CAM  # noqa: E402

VERSION = 2
globals().update(armar_camara('jr_inicio_curso2_fuente.mp4', 'INICIO DEL CURSO', 'Inicio del curso',
                              'JR - CURSO - INICIO - V2', 'justiciarestaurativa - CURSO - INICIO', 'JRCI2',
                              [(102, 9396), (11138, 22275, CERRADO)]))

ITEMS = [
    ('lt01', 'lt', 82.4, 90.4, VICTOR_CAM),
]
