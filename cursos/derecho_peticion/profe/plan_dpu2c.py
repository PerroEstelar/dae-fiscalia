# -*- coding: utf-8 -*-
r"""Cierre de la unidad 2 de «Derecho de petición y acción de tutela» (21 nov 2026). **Entrega provisional** (ver `base_dp_profe`).

Fuentes: `Derecho de petición - Unidad 2 Cierre Toma 1.mp4` (29:42) y `Derecho de petición Unidad 2 Cierre - Toma 2.mp4`
(2:29), las dos en `E:\DAE MASTER\CURSO DERECHOS DE PETICION\`. Se compone con las dos: la toma 1 termina en «Pauso porque
tengo un ruido acá… Voy a pausar» y la toma 2 empieza «Retomo este video desde la anterior pausa» y lee el resto del guion.

**La fuente del plan es una sola** (`ic_pieza` trabaja con una): `01 VIDEO/dpu2c_fuente_unida.mov`, las dos tomas enteras
pegadas sin recodificar el video (demuxer `concat` con `duration 1782.166667`, que son los 53.465 cuadros de la toma 1 a 30;
las dos tomas son H.264 Constrained Baseline 4.0 a 30) y el audio en PCM, con el de la toma 1 recortado a esa misma
duración (ver CLAUDE.md, «Unir dos grabaciones sin recodificar el video»). Un tiempo t de la toma 2 es 1782,1667 + t en la
unida. (NVENC desde ffmpeg no sirve en esta máquina: el controlador es más viejo que el que pide ffmpeg 9.) Los bordes se midieron sobre las tomas, en RMS de 10 ms
(`D:\DAE\_tmp\dp_p\bordes_c23.json`).

Qué sale (en tiempos de la toma 1, salvo el último):
- 144,63–212,66: «Los canales electrónico institucional, el presencial—», «Ay, perdón, paremos ahí un segundo, profesor
  Juan» y la charla con el técnico (que le dice que siga y que ellos editan).
- 334,38–356,54: el primer intento de «Los lineamientos exigen atender por orden de llegada…», que se traba en «mediante
  lengua de suen—» y «Que retomo la línea desde los lineamientos».
- 682,17–702,75: el primer intento de «Esta organización es una ayuda pedagógica…» y «Retomamos en la frase esta
  organización que acabo de señalar».
- 976,84–1020,50: el primer intento de «En ambos casos importan finalidad…» hasta «Requieren protección reforzada. No deben
  circular», y «Voy a retomar, suspendo aquí… y retomo desde la línea anterior».
- 1405,86–1420,42: «Ocultar en el sentido pedagógico utilizando…» y «Retomo ahí desde ocultar en el sentido pedagógico».
- Desde 1728,00: el primer intento de «Quien recibe puede advertir una barrera…», «Retomo desde la línea anterior», el
  segundo intento (la toma 1 lo lee entero, pero el profe paró por un ruido) y la pausa. Sigue la toma 2 desde «Quien recibe
  puede advertir una barrera» (7,57 de la toma 2) hasta «…en la siguiente unidad» (136,70; sale «Listo, ahí finalizaría ese
  video»).

Quedan en el video, como en las demás piezas, los tropiezos sueltos sin disculpa («de un dis— de un discurso», «sos— sobre»,
«indiscra— indiscriminadamente», «que otra persona preparó, que otro servidor preparó», «peticiones de este tipo de, de
alcance»); salen del subtítulo.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dp_profe import *  # noqa: E402,F401,F403
from base_dp_profe import armar, armar_unidad, rotulo, RAIZ  # noqa: E402,F401

T2 = 1782.166667     # un tiempo t de la toma 2 es T2 + t en la fuente unida (53.465 cuadros / 30)
globals().update(armar_unidad(2, 'CIERRE', 'dpu2c_fuente_unida.mov',
                             [(4.34, 144.63), (212.66, 334.38), (356.54, 682.17), (702.75, 976.84), (1020.50, 1405.86),
                              (1420.42, 1728.00), (T2 + 7.57, T2 + 136.70)]))
ORIGINAL = RAIZ + '/UNIDAD 2/CIERRE/01 VIDEO/dpu2c_fuente_unida.mov'

ITEMS = rotulo(T0 + 1.5)  # noqa: F821
