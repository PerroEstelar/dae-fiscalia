# -*- coding: utf-8 -*-
"""Derecho de petición · Unidad 4."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dp_u1 import PORTADA, PIES, BIEN, PARADAS, camino, audio
from dp_u2 import LISTA, sin_num

REJILLA = ('Rejilla de 8 cajas con scroll donde va una secuencia: ruta paso a paso, con la intro arriba.',
           [('c', (80, 330, 920, 300), 'Ruta paso a paso, sin scroll')])
S = {}

S['U4 L1'] = {
    1: PORTADA,
    2: BIEN, 3: BIEN, 4: BIEN, 5: BIEN,
    6: ('Sacar en un recuadro aparte los plazos del trámite (preferente y sumario, fallo en diez días).',
        [('+', (80, 520, 900, 80), 'Recuadro con los plazos')]),
    7: BIEN, 8: BIEN,
    9: REJILLA,
    10: BIEN,
    11: audio(),
    12: LISTA,
    13: BIEN,
    14: PIES,
}

S['U4 L2'] = {
    1: PORTADA,
    2: BIEN, 3: BIEN, 4: BIEN, 5: BIEN,
    6: camino(),
    7: REJILLA,
    8: BIEN,
    9: ('Camino de medidas provisionales: pasarlo a mapa conceptual con su descarga.',
        [('c', PARADAS, 'Mapa conceptual, no camino')]),
    10: ('La matriz de seguimiento pide scroll: dejarla como tabla descargable en PDF.',
         [('c', (80, 400, 920, 230), 'Tabla descargable en PDF')]),
    11: audio(),
    12: LISTA,
    13: BIEN,
    14: PIES,
}

S['U4 L3'] = {
    1: PORTADA,
    2: BIEN, 3: BIEN, 4: BIEN, 5: BIEN,
    6: REJILLA,
    7: BIEN,
    8: ('Bien; después de esta falta el caso práctico de impugnar y cumplir en paralelo (§5 del DI), con audio.',
        [('+', (1000, 560, 230, 60), 'Falta el caso práctico + audio')]),
    9: BIEN,
    10: ('530 palabras en scroll: dos pestañas (cumplimiento / desacato); falta el cuadro comparativo y la advertencia.',
         [('c', (80, 290, 900, 330), 'Dos pestañas, sin scroll'), ('+', (1000, 560, 230, 60), 'Falta el cuadro comparativo')]),
    11: camino(),
    12: audio(),
    13: LISTA,
    14: BIEN,
    15: PIES,
}

NUMERAR = ('Las actuaciones van con viñetas: numerarlas, es una lista ordenada.',
           [('c', (90, 300, 700, 330), 'Lista numerada 1, 2, 3…')])
S['U4 L4'] = {
    1: PORTADA,
    2: sin_num(4),
    3: BIEN, 4: BIEN, 5: BIEN,
    6: REJILLA,
    7: audio(), 8: NUMERAR,
    9: audio(), 10: NUMERAR,
    11: audio(), 12: NUMERAR,
    13: audio(), 14: NUMERAR,
    15: ('Falta el audio del caso; aquí se llama «Caso 5» y en el DI «8. Caso de análisis»: unificar.',
         [('+', (860, 190, 360, 60), 'Falta el audio del caso'), ('c', 'zona:titulo', 'Mismo nombre que el DI')]),
    16: NUMERAR,
    17: ('Bien la tabla, pero pide scroll: botón para descargar la matriz en PDF.',
         [('+', (880, 590, 260, 50), 'Botón: matriz en PDF')]),
    18: LISTA,
    19: BIEN,
    20: PIES,
}
