# -*- coding: utf-8 -*-
"""Delitos ambientales · Unidad 3."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from da_u1 import PORTADA, UNIDAD_REP, BIEN

OBJ_CAMINO = ('El objetivo va en un camino con doctrina: apertura aparte, con texto fijo.',
              [('c', 'Objetivo', 'Objetivo aparte, texto fijo')])
S = {}

S['U3 L1'] = {
    1: PORTADA,
    2: ('Falta el video de inicio de la unidad 3 (ya existe) antes de entrar a la lección.',
        [('+', (640, 140, 560, 380), 'Falta el video de inicio de la unidad 3')]),
    3: BIEN, 4: BIEN, 5: BIEN, 6: BIEN, 7: BIEN, 8: BIEN, 9: BIEN,
}

S['U3 L2'] = {
    1: PORTADA,
    2: UNIDAD_REP,
    3: BIEN, 4: BIEN,
    5: OBJ_CAMINO,
    6: ('Faltan los pasos 3 y 5 de la fase 1 del DI (están en la ficha de la 8); fases 1 y 2 en una con pestañas.',
        [('+', (90, 560, 240, 60), 'Faltan los pasos 3 y 5'), ('f', 'zona:titulo', 'zona:sig', 'Unir con la 7')]),
    7: ('Falta el examen 5, «¿Qué falta y cómo conseguirlo?»; va como pestaña B de la 6.',
        [('+', (1030, 470, 200, 70), 'Falta el examen 5'), ('c', 'zona:titulo', 'Pestaña B de la 6')]),
    8: BIEN, 9: BIEN,
}

S['U3 L3'] = {
    1: PORTADA,
    2: UNIDAD_REP,
    3: BIEN,
    4: ('Quitar «(1 de 2)» y «(2 de 2)»: una sola entrada para las técnicas especiales.',
        [('c', '2004 (1 de 2)', 'Una sola entrada'), ('c', '2004 (2 de 2)', None)]),
    5: BIEN,
    6: ('Las pestañas dicen «Fila 1…5»: cada una con el nombre de la técnica, y el cuadro completo en PDF.',
        [('c', (90, 208, 440, 32), 'Nombre de la técnica'), ('+', (960, 560, 260, 60), 'Botón: cuadro en PDF')]),
    7: ('La misma tabla sigue de la 6: una sola diapositiva con dos pestañas.',
        [('f', 'zona:titulo', 'zona:ant', 'Unir con la 6')]),
    8: BIEN, 9: BIEN, 10: BIEN, 11: BIEN,
}

S['U3 L4'] = {
    1: PORTADA,
    2: UNIDAD_REP,
    3: BIEN, 4: BIEN,
    5: OBJ_CAMINO,
    6: ('407 palabras en cuatro fichas con sublistas: mapa mental en ventana y lectura en PDF.',
        [('+', (960, 560, 260, 60), 'Mapa mental + PDF')]),
    7: BIEN, 8: BIEN,
}

S['U3 L5'] = {
    1: PORTADA,
    2: UNIDAD_REP,
    3: BIEN,
    4: ('Cuatro entradas con el título de la lección y «(1 de 4)»…: una entrada por tema.',
        [('c', 'ambientales (1 de 4)', 'Una entrada por tema'), ('c', 'ambientales (2 de 4)', None),
         ('c', 'ambientales (3 de 4)', None), ('c', 'ambientales (4 de 4)', None)]),
    5: ('Un juego de arrastrar para el objetivo no tiene sentido: apertura con el objetivo en texto fijo.',
        [('x', (90, 250, 600, 280), 'Objetivo en texto fijo, sin juego')]),
    6: BIEN,
    7: ('Se titula como la lección «(2 de 4)»; 7, 8 y 9 van en una sola diapositiva con tres pestañas.',
        [('c', 'zona:titulo', 'Unir 7, 8 y 9 en pestañas')]),
    8: ('Va como pestaña B (386 palabras): sumar la lectura completa en PDF.',
        [('c', 'zona:titulo', 'Pestaña B de la 7'), ('+', (960, 560, 260, 60), 'Botón: lectura en PDF')]),
    9: ('Va como pestaña C; «Se encuentran atributos que pueden formar» y «No se tiene en cuenta» cortan la frase.',
        [('c', 'Se encuentran atributos', 'Rótulos propios'), ('c', 'No se tiene en cuenta', None)]),
    10: BIEN,
    11: ('Falta el cierre de la unidad 3: el video de repaso va antes del fin.',
         [('+', (620, 560, 600, 90), 'Falta el video de cierre de la unidad 3')]),
}
