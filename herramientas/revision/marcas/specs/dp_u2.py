# -*- coding: utf-8 -*-
"""Derecho de petición · Unidad 2."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dp_u1 import PORTADA, PIES, BIEN, PARADAS, camino, audio

LISTA = ('Lista de verificación con scroll: en dos columnas y con botón para descargarla en PDF.',
         [('c', (80, 330, 920, 300), 'Dos columnas + PDF, sin scroll')])
SIN_NUM = ('El rótulo dice «Lección» sin número: «Lección {}».', [('c', (35, 135, 205, 55), 'Falta el {}')])


def sin_num(n):
    return (SIN_NUM[0].format(n), [(SIN_NUM[1][0][0], SIN_NUM[1][0][1], SIN_NUM[1][0][2].format(n))])


S = {}

S['U2 L1'] = {
    1: PORTADA,
    2: BIEN, 3: BIEN,
    4: ('Arranque largo (290 palabras con scroll): resaltar arriba el objetivo y dejar el resto debajo.',
        [('c', (80, 290, 870, 70), 'El objetivo arriba, resaltado')]),
    5: BIEN,
    6: ('Camino de paradas: mapa conceptual de nodo con ramas (virtual, telefónico, escrito, presencial).',
        [('c', PARADAS, 'Mapa conceptual, no camino')]),
    7: ('La rejilla en dos columnas pide scroll: pasarla a 4 × 2 para ver los 7 valores de una.',
        [('c', (80, 300, 900, 270), 'Rejilla 4 × 2, sin scroll')]),
    8: BIEN, 9: BIEN,
    10: camino(),
    11: audio(),
    12: ('Idea clave y conclusión quedan escondidas tras un clic: mostrarlas en pestañas, a la vista.',
         [('c', (505, 210, 690, 360), 'A la vista, en pestañas')]),
    13: PIES,
}

S['U2 L2'] = {
    1: PORTADA,
    2: BIEN, 3: BIEN, 4: BIEN, 5: BIEN,
    6: camino(),
    7: BIEN, 8: BIEN,
    9: audio(),
    10: ('Es un modelo de oficio: mostrarlo como documento, con botón para descargar la plantilla en PDF.',
         [('c', (80, 300, 880, 360), 'Como documento + plantilla PDF')]),
    11: LISTA,
    12: BIEN,
    13: PIES,
}

S['U2 L3'] = {
    1: PORTADA,
    2: BIEN, 3: BIEN, 4: BIEN, 5: BIEN,
    6: ('Cinco paradas y la 5 se sale de su tarjeta: mapa conceptual con su descarga.',
        [('c', PARADAS, 'Mapa conceptual, no camino')]),
    7: ('Once categorías en dos diapositivas (7 y 8) con la misma ilustración: agruparlas por tipo.',
        [('c', (90, 320, 1150, 330), 'Agrupar: pública, personal, restringida')]),
    8: ('Sigue la lista de la 7 con las mismas ilustraciones: unir y agrupar.',
        [('f', 'zona:titulo', 'zona:ant', 'Unir con la 7 y agrupar')]),
    9: ('Antes de esta falta la 4.4 (eliminación, anonimización y ocultamiento), con sus casos y audio.',
        [('+', (60, 200, 300, 120), 'Falta la 4.4 antes de esta')]),
    10: BIEN,
    11: audio(),
    12: LISTA,
    13: BIEN,
    14: PIES,
}

S['U2 L4'] = {
    1: PORTADA,
    2: sin_num(4),
    3: BIEN, 4: BIEN,
    5: ('Cada paso trae unas 235 palabras en un panel chico: dejar lo clave y el texto completo en PDF.',
        [('c', (90, 245, 940, 150), 'Solo lo clave + PDF')]),
    6: ('Camino con unas 200 palabras por parada: mapa conceptual con el detalle en ventanas.',
        [('c', PARADAS, 'Mapa conceptual, no camino')]),
    7: audio(),
    8: LISTA,
    9: BIEN,
    10: PIES,
}
