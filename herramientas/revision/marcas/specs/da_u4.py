# -*- coding: utf-8 -*-
"""Delitos ambientales · Unidad 4."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from da_u1 import PORTADA, UNIDAD_REP, BIEN
from da_u3 import OBJ_CAMINO

S = {}

S['U4 L1'] = {
    1: PORTADA,
    2: ('Falta el video de inicio de la unidad 4 (ya existe) antes de entrar a la lección.',
        [('+', (640, 140, 560, 380), 'Falta el video de inicio de la unidad 4')]),
    3: BIEN,
    4: ('Dieciséis entradas con «(1 de 2)» y los datos del caso sueltos: una entrada por apartado.',
        [('c', (60, 300, 1160, 330), 'Una entrada por apartado')]),
    5: ('Diapositiva solo para el objetivo, titulada «(1 de 2)»: apertura con texto fijo y audio.',
        [('c', 'zona:titulo', 'Quitar «(1 de 2)»')]),
    6: BIEN,
    7: ('Se titula «(2 de 2)»: ponerle su tema.', [('c', 'zona:titulo', 'Título con su tema')]),
    8: ('«Concepto de la justicia restaurativa» partido en dos (8 y 9): una sola con dos pestañas.',
        [('f', 'zona:titulo', 'zona:sig', 'Unir con la 9')]),
    9: ('Va como pestaña B de la 8.', [('c', 'zona:titulo', 'Pestaña B de la 8')]),
    10: BIEN,
    11: ('El apartado 3 sigue en la 12: una sola con dos pestañas y mapa mental.',
         [('f', 'zona:titulo', 'zona:sig', 'Unir con la 12')]),
    12: ('Va como pestaña B de la 11.', [('c', 'zona:titulo', 'Pestaña B de la 11')]),
    13: ('Muestra «Título del Caso» y «Temática Central»: son datos de la ficha para virtualizar, no para el estudiante.',
         [('x', (100, 290, 500, 110), 'Datos de la ficha: quitar')]),
    14: BIEN,
    15: ('El caso está en cuatro diapositivas sueltas (13, 15, 16, 17): una sola con pestañas y el video al lado.',
         [('c', 'zona:titulo', 'Unir 13, 15, 16 y 17 en pestañas')]),
    16: ('Va como pestaña del caso (ver la 15).', [('c', 'zona:titulo', 'Pestaña del caso')]),
    17: ('Va como pestaña del caso (ver la 15).', [('c', 'zona:titulo', 'Pestaña del caso')]),
    18: ('La secuencia de preguntas del caso es una ruta: mostrarla como diagrama en ventana.',
         [('+', (960, 560, 260, 60), 'Ruta en diagrama')]),
    19: BIEN,
}

S['U4 L2'] = {
    1: PORTADA,
    2: UNIDAD_REP,
    3: BIEN, 4: BIEN,
    5: ('El objetivo (92 palabras) comparte camino con la cita de la Corte: apertura aparte, con texto fijo.',
        [('c', 'Objetivo', 'Objetivo aparte, texto fijo')]),
    6: BIEN, 7: BIEN,
    8: ('Las cuatro preguntas son la estructura del caso: van como ruta en ventana antes del video.',
        [('c', 'Cuatro preguntas', 'Ruta en ventana, antes del video')]),
    9: BIEN,
    10: ('Arrastrar dos fichas es poco: las tres preguntas del caso (10 a 12) en una sola con pestañas.',
         [('c', 'zona:titulo', 'Unir 10, 11 y 12 en pestañas')]),
    11: ('Va como pestaña B del caso (ver la 10).', [('c', 'zona:titulo', 'Pestaña B de la 10')]),
    12: ('Va como pestaña C del caso; «Estado respeta el estándar de consulta» es el resultado: rótulo propio.',
         [('c', 'zona:titulo', 'Pestaña C de la 10'), ('c', 'Estado respeta el', 'Rótulo propio')]),
    13: ('El apartado 4 sigue en la 14 (402 y 223 palabras): una con dos pestañas y lectura en PDF.',
         [('f', 'zona:titulo', 'zona:sig', 'Unir con la 14')]),
    14: ('Va como pestaña B de la 13.', [('c', 'zona:titulo', 'Pestaña B de la 13')]),
    15: BIEN,
}

S['U4 L3'] = {
    1: PORTADA,
    2: UNIDAD_REP,
    3: BIEN,
    4: ('Quitar «(1 de 3)», «(1 de 2)»…: una entrada por apartado.',
        [('c', 'reparación (1 de 3)', 'Una entrada por apartado'), ('c', 'reparación (2 de 3)', None),
         ('c', 'reparación (3 de 3)', None), ('c', 'colombiano (1 de 2)', None), ('c', 'colombiano (2 de 2)', None)]),
    5: ('El DI no trae objetivo para esta lección: confirmar con el autor.',
        [('c', 'zona:titulo', 'Confirmar el objetivo con el autor')]),
    6: ('Medidas cautelares en tres diapositivas (6 a 8): una sola con tres pestañas y lectura en PDF.',
        [('c', 'zona:titulo', 'Unir 6, 7 y 8 en pestañas')]),
    7: ('La lista salta de b) a d): falta la característica c) o el DI la numera mal; confirmar con el autor.',
        [('c', 'zona:titulo', 'Pestaña B de la 6'), ('+', (960, 560, 260, 60), 'Falta la c): confirmar')]),
    8: ('Va como pestaña C de la 6; 489 palabras: lectura completa en PDF.',
        [('c', 'zona:titulo', 'Pestaña C de la 6'), ('+', (960, 560, 260, 60), 'Botón: lectura en PDF')]),
    9: ('Ejemplos en dos diapositivas (9 y 10); «Las dos normas que plasman» no orienta: rótulo propio.',
        [('f', 'zona:titulo', 'zona:sig', 'Unir con la 10')]),
    10: ('Los rótulos con «(continuación)» parten cada delito: cada fila con su medida.',
         [('c', (60, 290, 640, 40), 'Sin «(continuación)»: una fila por delito')]),
    11: ('Bien; el DI deja una nota suelta («caso tortugas, caso ingrid») que no se usa: confirmar con el autor.', []),
}

S['U4 L4'] = {
    1: PORTADA,
    2: UNIDAD_REP,
    3: BIEN,
    4: ('Tres entradas con el título de la lección y «(1 de 3)»: el índice va por temas.',
        [('c', (60, 380, 1160, 150), 'Una entrada por tema')]),
    5: ('El objetivo y el criterio a) en el mismo camino: apertura solo con el objetivo, en texto fijo.',
        [('c', 'Objetivo', 'Objetivo aparte, texto fijo')]),
    6: ('Criterios a) a f) partidos en tres diapositivas con el mismo título: una con pestañas y mapa mental.',
        [('c', 'zona:titulo', 'Unir 5, 6 y 7 en pestañas')]),
    7: ('Va como pestaña B; la síntesis merece destacarse.', [('c', 'zona:titulo', 'Pestaña B de la 6')]),
    8: BIEN,
}

S['U4 L5'] = {
    1: PORTADA,
    2: UNIDAD_REP,
    3: BIEN,
    4: ('Con dos diapositivas, el índice puede ir directo al video.', []),
    5: ('Diapositiva solo para el objetivo: apertura con texto fijo y audio.', []),
    6: ('Bien el video del caso Francisco; la lección es solo eso: confirmar con el autor si falta el análisis.',
        [('+', (960, 560, 260, 60), '¿Falta el análisis del caso?')]),
    7: ('Falta el cierre de la unidad 4: el video de repaso va antes del fin.',
        [('+', (620, 560, 600, 90), 'Falta el video de cierre de la unidad 4')]),
}
