# -*- coding: utf-8 -*-
r"""Cierre del curso «Justicia restaurativa en la práctica del fiscal», **profe a cámara** (25 nov 2026). **Entrega
provisional; es la versión 2 del cierre** (la v1 es la conversación de los dos coautores, `plan_jrcc`).

Lleva intro, cartón de título, un lower third, cartón de cierre y outro; el cuerpo va sin gráficos (ver
`base_jr_camara`).

**Fuente.** `jr_cierre_curso2_toma1_fuente.mp4` (enlace duro de «VIDEO 2 CIERRE DE TODO EL CURSO JUSTICIA RESTAURATIVA
TOMA 1.mp4», carpeta de la pieza): 24.921 cuadros (13:50,7), pico de −0,0 dBFS. STT (Scribe): 1.241 palabras.

**Qué es.** Víctor Hugo Ospina Vargas felicita por terminar el curso, recuerda la competencia general y repasa las cuatro
unidades. Lee un guion; se equivoca tres veces y retoma él mismo.

**Cortes** (segundos de la fuente; cada uno cambia de plano):
1. Arranque en falso: «Felicitaciones… han analizado, comprendido y gestionado los conflictos. No, me equivoqué en esta…
   Ay, Dios.» Entra en 40,70 (el segundo «Felicitaciones» empieza en 41,14).
2. Unidad 2, primera vez (238,66 a 393): se enreda en «se hizo énfasis en él dada, dadas sus…», dice «no, me enredé. Voy
   a retomar. Listo.» y repite la unidad 2 entera. Sale 237,90–396,85 (158,95 s): queda «…de la reparación y de la
   reintegración. | En la unidad dos fortalecieron su criterio jurídico…», una sola vez.
3. Unidad 3, primera vez: «adquirieron herramientas sobre los lineamientos y herramientas— ahí quedó redundante.
   Retomo.» Sale 539,10–551,75 (12,65 s).
4. Tropiezo: «…monitoreo y seguimiento para cons— para cons— para constr— para contrastar…». Sale 681,95–686,10
   (4,15 s): queda «…monitoreo y seguimiento | para contrastar los compromisos asumidos…».
Termina en 826,00 (0,8 s después de «Hasta pronto.», que acaba en 825,23). Quedan 10:09,6.

Se dejan los tropiezos de quien lee sin cortar la idea («utiliz-utilizando», «extri-estrictamente», «lis— de lesividad»).

**Lower third.** Al empezar a hablar (42,0 s de la fuente).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_jr_camara import *  # noqa: E402,F401,F403
from base_jr_camara import armar_camara, CERRADO, VICTOR_CAM  # noqa: E402

VERSION = 2
globals().update(armar_camara('jr_cierre_curso2_toma1_fuente.mp4', 'CIERRE DEL CURSO', 'Cierre del curso',
                              'JR - CURSO - CIERRE - V2', 'justiciarestaurativa - CURSO - CIERRE', 'JRCC2',
                              [(1221, 7137), (11906, 16173, CERRADO), (16553, 20459), (20583, 24780, CERRADO)]))

ITEMS = [
    ('lt01', 'lt', 42.0, 50.0, VICTOR_CAM),
]
