# -*- coding: utf-8 -*-
"""Delitos ambientales · Unidad 1. Por lección y número de diapositiva (como en los pantallazos):
(comentario breve para el Excel, [marcas sobre el pantallazo]). Ver marcas.py para las marcas."""
# Sebastián (24 nov): «en estos casos la primer diapositiva sí puede ser el título de esa unidad o lección».
PORTADA = ('Puede abrir la lección, pero con el título de la unidad o de la lección, no el del curso.',
           [('c', ['Curso', 'Investigación y judicialización', 'medio ambiente y los recursos'],
             'Aquí el título de la unidad o de la lección, no el del curso')])
UNIDAD_REP = ('Bien así.', [])
BIEN = ('Bien así.', [])

S = {}

S['U1 L1'] = {
    1: PORTADA,
    2: ('Falta el video de inicio de la unidad 1 antes de entrar a la lección.',
        [('+', (640, 140, 560, 380), 'Falta el video de inicio de la unidad 1')]),
    3: BIEN,
    4: ('Índice con «(1 de 2)» y «(1 de 3)»: una entrada por apartado del DI.',
        [('c', 'grupos armados) (1 de 2)', 'Una entrada por apartado'), ('c', 'grupos armados) (2 de 2)', None),
         ('c', 'Sociedad de riesgo (1 de 3)', None), ('c', 'Sociedad de riesgo (2 de 3)', None),
         ('c', 'Sociedad de riesgo (3 de 3)', None)]),
    5: ('El video va después del objetivo (diapositiva 6), no antes.',
        [('f', 'zona:video', 'zona:sig', 'Pasar después del objetivo')]),
    6: ('«Desarrollo» es una sola frase: unirla al objetivo y mostrarlo sin clic.',
        [('f', 'Desarrollo', 'Objetivo', 'Unir al objetivo, visible sin clic')]),
    7: BIEN,
    8: BIEN,
    9: ('«Sociedad de riesgo» está en tres diapositivas (9 a 11): una sola con tres pestañas.',
        [('c', 'zona:titulo', 'Unir 9, 10 y 11 en una con pestañas')]),
    10: ('Va como pestaña B de «Sociedad de riesgo»; sumar la lectura completa en PDF.',
         [('c', 'zona:titulo', 'Pestaña B de la diapositiva 9'), ('+', (920, 560, 300, 64), 'Botón: lectura en PDF')]),
    11: ('Va como pestaña C de «Sociedad de riesgo».',
         [('c', 'zona:titulo', 'Pestaña C de la diapositiva 9')]),
    12: ('Sumar la lista a) a j) de técnicas preventivas como PDF descargable.',
         [('+', (960, 520, 260, 70), 'Botón: técnicas a) a j) en PDF')]),
    13: BIEN,
    14: ('Cuatro paradas de 50 a 120 palabras: mejor mapa mental con descarga en PDF.',
         [('c', (190, 330, 1000, 290), 'Pasar a mapa mental + PDF')]),
    15: ('Unir con «Delitos de peligro» (diapositiva 16) en una sola con dos pestañas.',
         [('f', 'zona:titulo', 'zona:sig', 'Unir con la 16 en pestañas')]),
    16: ('Las fichas 3 y 4 tienen pedazos de frase como rótulo: ponerles título propio.',
         [('c', 'Pueden configurarse', 'Rótulos propios'), ('c', 'Debido a que normalmente', None)]),
    17: BIEN,
}

S['U1 L2'] = {
    1: PORTADA,
    2: UNIDAD_REP,
    3: BIEN, 4: BIEN, 5: BIEN, 6: BIEN,
    7: ('Las paradas 1 y 4 tienen pedazos de frase como rótulo: ponerles título propio.',
        [('c', 'Corte Constitucional manifiesta', 'Rótulos propios'), ('c', 'Tras la conquista de la', None)]),
    8: ('La parada 2 tiene un pedazo de frase como rótulo; sumar la lectura completa en PDF.',
        [('c', 'Este artículo señala', 'Rótulo propio'), ('+', (960, 560, 260, 60), 'Botón: lectura en PDF')]),
    9: ('«Amaya (2003a)» no dice la idea de la parada: rótulo propio.',
        [('c', 'Amaya (2003a)', 'Rótulo con la idea, no el autor')]),
    10: BIEN,
}

S['U1 L3'] = {
    1: PORTADA,
    2: UNIDAD_REP,
    3: BIEN,
    4: ('Dos entradas casi iguales («Estructura del SINA»): al unir 7, 9 y 10 queda una sola.',
        [('c', 'Estructura del Sistema Nacional Ambiental (SINA)', 'Una sola entrada'), ('c', 'Estructura del SINA', None)]),
    5: BIEN,
    6: ('Las pestañas dicen «Fila 1», «Filas 2 y 3»…: una pestaña por norma, con su nombre.',
        [('c', (120, 268, 470, 38), 'Una pestaña por norma, con su nombre')]),
    7: ('Dos paradas cortas: unir con «Sector central» y «Órganos autónomos» (9 y 10) en pestañas.',
        [('f', 'zona:titulo', 'zona:sig', 'Unir con 9 y 10 en pestañas')]),
    8: ('Bien la lupa sobre la figura del SINA; va después de las pestañas que la explican.', []),
    9: ('Bien; va como pestaña B del apartado 2.', [('c', 'zona:titulo', 'Pestaña B (con la 7)')]),
    10: ('Bien; va como pestaña C del apartado 2.', [('c', 'zona:titulo', 'Pestaña C (con la 7)')]),
    11: ('Apartados 3 y 4 en dos diapositivas cortas (11 y 12): una sola con dos pestañas.',
         [('f', 'zona:titulo', 'zona:sig', 'Unir con la 12 en pestañas')]),
    12: ('«Corte aclara» no dice la idea de la tarjeta: rótulo propio.',
         [('c', 'Corte aclara', 'Rótulo propio')]),
    13: BIEN,
}

S['U1 L4'] = {
    1: PORTADA,
    2: UNIDAD_REP,
    3: BIEN,
    4: ('Al unir 6 y 7, el índice queda con una sola entrada para el apartado.',
        [('c', 'derechos (1 de 2)', 'Una sola entrada'), ('c', 'derechos (2 de 2)', None)]),
    5: BIEN,
    6: ('Bien la línea de tiempo; «Sala de Casación Civil» debe decir qué fallo es.',
        [('c', 'Sala de Casación Civil', 'Nombrar el fallo')]),
    7: ('Mismo apartado en dos diapositivas (6 y 7): una sola con dos pestañas.',
        [('f', 'zona:titulo', 'zona:ant', 'Unir con la 6 en pestañas')]),
    8: BIEN,
}

S['U1 L5'] = {
    1: PORTADA,
    2: UNIDAD_REP,
    3: BIEN, 4: BIEN, 5: BIEN, 6: BIEN, 7: BIEN,
    8: ('El caso va narrado en audio y en la misma diapositiva que su cuadro (9).',
        [('+', (980, 300, 230, 60), 'Botón de audio del caso'), ('f', 'Momento 1 de 4', 'zona:sig', 'Unir con el cuadro (9)')]),
    9: ('Las pestañas «Filas 1 a 3» y «Filas 4 y 5» deben nombrar los tipos de daño.',
        [('c', (120, 206, 220, 34), 'Nombrar los tipos de daño')]),
    10: ('Una diapositiva para una nota de 36 palabras: pasarla al pie del cuadro del caso (9).',
         [('f', (95, 268, 430, 90), 'zona:ant', 'Al pie del cuadro (9)')]),
    11: BIEN,
    12: ('Falta el cierre de la unidad 1: el video de repaso va antes del fin.',
         [('+', (620, 560, 600, 90), 'Falta el video de cierre de la unidad 1')]),
}
