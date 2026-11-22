# -*- coding: utf-8 -*-
r"""Cierre de la unidad 3 de «Derecho de petición y acción de tutela» (21 nov 2026). **Entrega provisional** (ver `base_dp_profe`).

Fuente: `Derecho de petición Unidad 3 cierre.mp4` (30:47). Una sola toma; el profe dice en voz alta desde dónde retoma
cada vez que se traba. Bordes en RMS de 10 ms (`D:\DAE\_tmp\dp_p\bordes_c23.json`).

Qué sale:
- 542,92–559,49: el primer intento de «Para quienes aportan antecedentes…» y «Voy a retomar desde la frase "para quienes
  aportan"».
- 787,78–795,18: una pausa de 7,9 s entre «…medidas que no puedan esperar» y «Preferir recibir el dinero…».
- 801,57–810,76: el primer «Tampoco una negativa.» y «Retomo desde "tampoco una negativa"».
- 918,48–929,70: el primer «También se exige una irregularidad procesal alegada.» y «Retomo desde esta última frase,
  "también se exige"».
- 1471,62–1497,77: el primer intento de «La temeridad se encuentra relacionada…» y «El artículo treinta y ocho regula la
  prestación injustificada», y «Pauso, retomo desde la temeridad».
- 1549,92–1571,79: el primer intento de «Si existe una tutela previa…» y «Retomo desde si existe una tutela previa».
- Termina en «…para contribuir responsablemente a su atención» (sale «Hasta ahí el video»).

Quedan en el video los tropiezos sueltos sin disculpa («los requisit— los requisitos», «el derecho cuta— cuya»,
«injusta— injustificados»); salen del subtítulo.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_dp_profe import *  # noqa: E402,F401,F403
from base_dp_profe import armar, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad(3, 'CIERRE', 'Derecho de petición Unidad 3 cierre.mp4',
                             [(2.32, 542.92), (559.49, 787.78), (795.18, 801.57), (810.76, 918.48), (929.70, 1471.62),
                              (1497.77, 1549.92), (1571.79, 1836.26)]))

ITEMS = rotulo(T0 + 1.5)  # noqa: F821
