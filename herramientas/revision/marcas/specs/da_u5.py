# -*- coding: utf-8 -*-
"""Delitos ambientales · Unidad 5."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from da_u1 import PORTADA, UNIDAD_REP, BIEN
from da_u3 import OBJ_CAMINO

S = {}

S['U5 L3'] = {
    1: PORTADA,
    2: UNIDAD_REP,
    3: BIEN,
    4: ('Quitar «(1 de 2)» y «(2 de 2)»: una sola entrada para el concepto jurisprudencial.',
        [('c', 'jurisprudencial (1 de 2)', 'Una sola entrada'), ('c', 'jurisprudencial (2 de 2)', None)]),
    5: ('Diapositiva solo para el objetivo: apertura con texto fijo y audio.', []),
    6: BIEN,
    7: ('Concepto jurisprudencial en dos (7 y 8): una sola con dos pestañas; «Sentencia T-1026 de 2006» rotula un párrafo que no es de esa sentencia.',
        [('f', 'zona:titulo', 'zona:sig', 'Unir con la 8'), ('c', 'Sentencia T-1026 de 2006', 'Rótulo equivocado')]),
    8: ('Va como pestaña B de la 7.', [('c', 'zona:titulo', 'Pestaña B de la 7')]),
    9: ('Bien las tarjetas; «Cuando la aceptación recaiga…» y «La terminación anticipada no hace…» van con su idea.',
        [('c', 'Cuando la aceptación recaiga', 'Rótulos propios'), ('c', 'La terminación anticipada no hace', None)]),
    10: ('Muy bien la ruta en cinco momentos con su alerta final, como pide el DI.', []),
    11: BIEN,
}

S['U5 L4'] = {
    1: PORTADA,
    2: UNIDAD_REP,
    3: BIEN, 4: BIEN, 5: BIEN,
    6: ('La primera ficha mezcla la introducción con a) Restitución: el rótulo debe decirlo.',
        [('c', 'Reparación integral', 'Separar intro y a) Restitución')]),
    7: ('Aparece «Causal 13» sin una causal anterior: confirmar con el autor la numeración.',
        [('c', 'Causal 13', 'Confirmar numeración')]),
    8: BIEN,
    9: ('Las conclusiones no son para arrastrar y soltar: mejor tarjetas que giran o una síntesis en audio.',
        [('x', (90, 290, 1050, 300), 'Sin arrastrar: tarjetas o audio')]),
    10: ('Falta el cierre de la unidad 5 (video de repaso); el cierre del curso es un recurso aparte, no va aquí.',
         [('+', (620, 560, 600, 90), 'Falta el video de cierre de la unidad 5')]),
}

S['U5 L1'] = {
    1: PORTADA,
    2: ('Falta el video de inicio de la unidad 5 antes de entrar a la lección (no está en el sitio).',
        [('+', (640, 140, 560, 380), 'Falta el video de inicio de la unidad 5')]),
    3: BIEN,
    4: ('Veinte entradas con «(1 de 3)», «(1 de 2)»…: el índice va por los nueve apartados del DI.',
        [('c', (40, 300, 1200, 330), 'Nueve entradas, una por apartado')]),
    5: ('Diapositiva solo para el objetivo: apertura con texto fijo y audio.', []),
    6: ('Nociones preliminares en tres diapositivas (6 a 8): una sola con tres pestañas y lectura en PDF.',
        [('c', 'zona:titulo', 'Unir 6, 7 y 8 en pestañas')]),
    7: ('Va como pestaña B de la 6 (382 palabras).', [('c', 'zona:titulo', 'Pestaña B de la 6')]),
    8: ('Va como pestaña C de la 6.', [('c', 'zona:titulo', 'Pestaña C de la 6')]),
    9: ('Bien el esquema radial que pide el DI.', []),
    10: ('La lista a) a h) sigue en la 11 con otra actividad: una sola con dos pestañas.',
         [('f', 'zona:titulo', 'zona:sig', 'Unir con la 11')]),
    11: ('Arrastrar artículos sirve, pero va como pestaña B de la misma lista (10).',
         [('c', 'zona:titulo', 'Pestaña B de la 10')]),
    12: ('Bien el mapa normativo; lo pide el DI tal cual.', []),
    13: ('Criterios a) a d) partidos en dos (13 y 14): una sola con dos pestañas.',
         [('f', 'zona:titulo', 'zona:sig', 'Unir con la 14')]),
    14: ('Va como pestaña B de la 13.', [('c', 'zona:titulo', 'Pestaña B de la 13')]),
    15: ('460 palabras en cinco paradas con rótulos como «Cada caso y cada delito»: rótulos propios, mapa mental y PDF.',
         [('c', 'Cada caso y cada', 'Rótulo propio'), ('+', (960, 560, 260, 60), 'Mapa mental + PDF')]),
    16: ('Causales en dos diapositivas (16 y 17, 434 y 291 palabras): una con dos pestañas y lectura en PDF.',
         [('f', 'zona:titulo', 'zona:sig', 'Unir con la 17')]),
    17: ('Va como pestaña B de la 16; los cuatro requisitos se leen mejor como lista.',
         [('c', 'zona:titulo', 'Pestaña B de la 16')]),
    18: ('El ejemplo de inmunidad queda partido: «Inmunidad total» aquí e «Inmunidad parcial» en la 19.',
         [('c', 'Inmunidad total', 'Sigue en la 19: juntarlo')]),
    19: ('Empieza con «Inmunidad parcial», el final del ejemplo: el ejemplo va completo en su pestaña, narrado en audio.',
         [('c', 'Inmunidad parcial', 'Viene de la 18: juntarlo')]),
    20: ('Una diapositiva para 89 palabras: va con «Características» (21) en dos pestañas.',
         [('f', 'zona:titulo', 'zona:sig', 'Unir con la 21')]),
    21: ('Va como pestaña B de la 20.', [('c', 'zona:titulo', 'Pestaña B de la 20')]),
    22: ('Bien el caso Lizama en línea de tiempo; los rótulos deben decir cada momento.',
         [('c', 'Pozo Lizama', 'Rótulos con cada momento')]),
    23: BIEN,
}

S['U5 L2'] = {
    1: PORTADA,
    2: UNIDAD_REP,
    3: BIEN,
    4: ('Quitar «(1 de 2)» y «(2 de 2)» del índice: cada entrada con su tema.',
        [('c', 'ambiental (1 de 2)', 'Cada entrada con su tema'), ('c', 'ambiental (2 de 2)', None)]),
    5: ('Objetivo y tres párrafos en un camino titulado «(1 de 2)»: apertura aparte, con texto fijo.',
        [('c', 'Objetivo', 'Objetivo aparte, texto fijo'), ('c', 'zona:titulo', None)]),
    6: ('Se titula como la lección «(2 de 2)»; «La Corte ha reconocido» no orienta: rótulos propios.',
        [('c', 'zona:titulo', 'Título con su tema')]),
    7: ('Bien las tarjetas de la infografía que pide el DI.', []),
    8: BIEN,
    9: BIEN,
}
