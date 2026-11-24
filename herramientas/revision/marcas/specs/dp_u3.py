# -*- coding: utf-8 -*-
"""Derecho de petición · Unidad 3."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dp_u1 import PORTADA, PIES, BIEN, PARADAS, camino, audio
from dp_u2 import LISTA, sin_num

S = {}

S['U3 L1'] = {
    1: PORTADA,
    2: BIEN, 3: BIEN,
    4: ('Introducción y objetivo en dos láminas seguidas con el mismo escudo: unirlas; el aviso «¡Tramo superado!» tapa el texto.',
        [('f', 'zona:titulo', 'zona:sig', 'Unir con la 5'), ('x', (490, 350, 300, 45), 'El aviso tapa el texto: a una esquina')]),
    5: ('Va unida a la 4 (introducción y objetivo en una sola lámina).',
        [('f', 'zona:titulo', 'zona:ant', 'Unir con la 4')]),
    6: ('Camino de 4 paradas que tapa la escena: mapa conceptual con la tutela arriba y sus ramas.',
        [('c', PARADAS, 'Mapa conceptual, no camino')]),
    7: BIEN, 8: BIEN, 9: BIEN,
    10: audio(),
    11: LISTA,
    12: BIEN,
    13: PIES,
}

S['U3 L2'] = {
    1: PORTADA,
    2: BIEN, 3: BIEN, 4: BIEN, 5: BIEN,
    6: ('Son dos cajas y van tres; el texto es de una versión anterior del DI (agente oficioso, sin abogado).',
        [('+', (1000, 560, 230, 60), 'Falta la tercera caja'), ('c', (80, 260, 1150, 380), 'Texto del DI vigente')]),
    7: ('Texto de una versión anterior del DI; falta el ejemplo de quien no obtuvo respuesta a su petición.',
        [('c', (80, 260, 1150, 380), 'Texto del DI vigente + ejemplo')]),
    8: ('Actualizar al texto vigente del DI (por qué importa el tiempo) y destacar el ejemplo.',
        [('c', (500, 205, 700, 370), 'Texto vigente + ejemplo destacado')]),
    9: ('Camino de 3 paradas: hacerlo como el mapa conceptual de la 10 y actualizar el texto.',
        [('f', PARADAS, 'zona:sig', 'Como el mapa de la 10')]),
    10: ('Muy bien: este es el modelo de mapa conceptual para el resto del curso.', []),
    11: BIEN,
    12: LISTA,
    13: PIES,
}

S['U3 L3'] = {
    1: PORTADA,
    2: BIEN, 3: BIEN, 4: BIEN, 5: BIEN,
    6: ('Camino de 5 paradas: mapa conceptual con su descarga.', [('c', PARADAS, 'Mapa conceptual, no camino')]),
    7: ('Requisitos generales y defectos específicos escondidos en un camino sin descarga: mapa conceptual con los 7 a la vista.',
        [('c', PARADAS, 'Los 7 requisitos a la vista + descarga')]),
    8: ('Cosa juzgada no está en el DI vigente de esta lección (va en la 3.4): confirmar si se quita.',
        [('c', 'zona:titulo', 'Confirmar: es de la 3.4')]),
    9: ('Temeridad no está en el DI vigente de esta lección (va en la 3.4): confirmar si se quita.',
        [('c', 'zona:titulo', 'Confirmar: es de la 3.4')]),
    10: BIEN,
    11: ('Esta diapositiva (implicaciones) no está en el DI vigente de la 3.3: confirmar con el autor.',
         [('c', 'zona:titulo', 'No está en el DI vigente')]),
    12: ('El caso es el de temeridad de la 3.4: va el de la grabación judicial, con sus 4 preguntas y audio.',
         [('c', 'Situación', 'Cambiar por el caso del DI'), ('+', (860, 190, 360, 60), 'Falta el audio del caso')]),
    13: LISTA,
    14: ('Falta el «Cierre de la lección» del DI (§8) antes del fin.',
         [('+', (80, 560, 900, 60), 'Falta el cierre de la lección (§8)')]),
    15: PIES,
}

S['U3 L4'] = {
    1: PORTADA,
    2: ('El rótulo dice «Lección» sin el 4 y el título parte la palabra «Reconocimient-o».',
        [('c', (35, 135, 205, 55), 'Falta el 4'), ('c', (40, 175, 600, 80), 'La palabra se parte')]),
    3: BIEN, 4: BIEN,
    5: ('Camino de 3 paradas: mapa conceptual de nodo con ramas, con el problema según el DI vigente.',
        [('c', PARADAS, 'Mapa conceptual + texto vigente')]),
    6: ('1.170 palabras en un solo scroll: intro corta, una ventana por causal del art. 6 y el texto en PDF.',
        [('c', (80, 290, 1000, 320), 'Ventana por causal + PDF')]),
    7: ('Pide scroll con 170 palabras porque la ilustración ocupa medio lienzo: texto más ancho, la idea clave arriba.',
        [('f', (80, 300, 330, 320), (440, 300, 120, 60), 'Texto más ancho')]),
    8: ('Igual: pide scroll por la ilustración; texto más ancho y resaltar que se mira si el plazo fue razonable.',
        [('f', (80, 300, 330, 320), (440, 300, 120, 60), 'Texto más ancho')]),
    9: BIEN,
    10: ('Pide scroll: resaltar arriba que la tutela no es una instancia adicional.',
         [('c', (500, 300, 600, 60), 'Esta idea, resaltada arriba')]),
    11: ('Muy bien: mapa conceptual con descarga.', []),
    12: BIEN,
    13: audio(),
    14: ('Los 17 ítems no son la lista del DI (reconocimiento y canalización de comunicaciones): cambiarlos.',
         [('c', (80, 330, 920, 300), 'Cambiar por la lista del DI')]),
    15: ('Actualizar al DI vigente: síntesis de legitimación, inmediatez, subsidiariedad e improcedencia.',
         [('c', (80, 290, 1000, 320), 'Texto del DI vigente')]),
    16: PIES,
}
