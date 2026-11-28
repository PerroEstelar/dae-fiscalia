# -*- coding: utf-8 -*-
r"""Inicio de la unidad 1, «Contexto estratégico y política criminal», de «Gerencia judicial» (27 nov 2026). **Entrega provisional**
(ver `base_gj_profe`). **Compuesto entre dos tomas.**

**Fuente.** `01 VIDEO/gj_u1i_fuente.mp4` = VIDEO 2 (cuadros 1299 a 6144: la toma completa, después del arranque en falso «voy a volver a
comenzar…») seguida de VIDEO 3 (cuadros 4242 a 4649: la frase de la evaluación de la otra toma), en cuadros del _fuente desde 4845.

**El cambio.** En VIDEO 2 dice «Tendrá chequeos formativos sin nota y una evaluación calificada al cierre de cada unidad de los
tres temas»; en VIDEO 3, «Tendrá chequeos formativos sin nota, una evaluación calificada al cierre de cada uno de los tres temas»,
que es lo que dice la ficha (evaluación al cierre de cada tema en las unidades 1 y 2). Sale la de VIDEO 2 (11.07 s, con la pausa
de 3,9 s de antes) y entra la de VIDEO 3 en plano cerrado; después vuelve VIDEO 2 en plano entero en «Mi recomendación».
Bordes: 46 y 39 dB bajo la voz en VIDEO 2; 44 y 49 en VIDEO 3.

La toma de VIDEO 3 entera no se usa: lee los rótulos («Los temas, uno a uno», «La evaluación calificada al cierre de cada tema.
Chequeos formativos sin nota.») y tiene más tropiezos.

El lower third entra 1,2 s después de la primera palabra y dura 8 s.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_gj_profe import *  # noqa: E402,F401,F403
from base_gj_profe import armar_unidad, PROFE, CERRADO  # noqa: E402

globals().update(armar_unidad(1, 'INICIO', [(46, 3933), (5057, 5250, CERRADO), (4265, 4793)]))

SUAVE = 3

ITEMS = [
    ('lt01', 'lt', 3.22, 11.22, PROFE),
]
