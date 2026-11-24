# -*- coding: utf-8 -*-
"""Derecho de petición · Unidad 1. Por lección y número de diapositiva (como en los pantallazos):
(comentario breve para el Excel, [marcas sobre el pantallazo])."""
# Sebastián (24 nov): «en estos casos la primer diapositiva sí puede ser el título de esa unidad o lección».
PORTADA = ('Puede abrir la lección, pero con el título de la unidad o de la lección, no el del curso.',
           [('c', ['Curso', 'Derecho de petición y acción', 'Régimen constitucional'],
             'Aquí el título de la unidad o de la lección, no el del curso')])
PIES = ('Los pies de la ilustración se asoman debajo del pie de página.',
        [('c', (600, 668, 560, 46), 'Se asoman los pies: subir o recortar la ilustración')])
BIEN = ('Bien así.', [])
CAMINO_MAPA = 'Camino de paradas: pasarlo a mapa conceptual (nodo con ramas) y dejar la descarga.'
PARADAS = (60, 300, 1160, 270)


def camino(nota='Mapa conceptual, no camino'):
    return (CAMINO_MAPA, [('c', PARADAS, nota)])


def audio(caja=(860, 190, 360, 60)):
    return ('Falta el audio de la situación: botón de audio arriba del caso.',
            [('+', caja, 'Falta el audio del caso')])


S = {}

S['U1 L1'] = {
    1: PORTADA,
    2: BIEN, 3: BIEN,
    4: ('El objetivo debe salir completo de una, sin animación.',
        [('c', (215, 285, 440, 70), 'Completo de una, sin animación')]),
    5: ('Tres rasgos del mismo derecho, no pasos: mapa conceptual; quitar el «Clic aquí» que tapa la tarjeta 1.',
        [('x', 'Clic aquí', 'Quitar: tapa la tarjeta 1'), ('c', PARADAS, 'Mapa conceptual, no camino')]),
    6: ('Un ícono propio por caja; la caja 1 como línea de tiempo 2011-2015 y el art. 13 en viñetas.',
        [('c', 'El CPACA en su texto vigente', 'Línea de tiempo 2011-2015'),
         ('c', 'Actuaciones que pueden', 'Viñetas')]),
    7: ('Pasar a viñetas lo que revelan las peticiones (tercera tarjeta).',
        [('c', 'Una fuente de información', 'Viñetas')]),
    8: ('Quitar la columna de íconos y armar el texto en dos bloques sin scroll.',
        [('x', (1140, 270, 80, 290), 'Quitar íconos'), ('c', (90, 290, 960, 420 - 120), 'Dos bloques, sin scroll')]),
    9: ('Escenario con botones a, b y c en ventana; en c) los plazos de 15, 10 y 30 días como barras.',
        [('c', ['a) Facultad de presentar', 'c) Oportunidad de la decisión'], 'Botones a, b, c en ventana')]),
    10: ('Partir el texto de 380 palabras en tres pestañas; el traslado como flujo de 5 días.',
         [('c', (80, 300, 830, 300), 'Tres pestañas, sin scroll')]),
    11: ('El escudo de la tarjeta 3 tapa «Cerrar»; quiénes llegan a la Fiscalía, en chips.',
         [('c', (870, 330, 230, 170), 'El escudo tapa «Cerrar»')]),
    12: ('Quitar «baje con la barra» (no hay scroll) y poner arriba la frase fuerza.',
         [('x', 'baje con la barra', 'No hay scroll')]),
    13: ('«Caso de aplicación» como dice el DI; la idea clave visible sin clic.',
         [('c', 'Idea clave', 'Visible sin clic')]),
    14: ('Anuncia la Política de Atención para la 1.2, pero es de la 2.1: confirmar con el autor.',
         [('c', 'La siguiente lección', 'Es de la 2.1: confirmar')]),
    15: PIES,
}

S['U1 L2'] = {
    1: PORTADA,
    2: BIEN, 3: BIEN, 4: BIEN, 5: BIEN,
    6: ('Falta el caso práctico de la petición particular (§2.2 del DI), con audio, en la caja 2.',
        [('+', (515, 300, 300, 120), 'Falta el caso práctico + audio')]),
    7: ('Subir las tres cajas (dejan un hueco arriba) y quitar la columna de íconos.',
        [('f', (90, 395, 990, 160), (90, 195, 990, 40), 'Subir las cajas'), ('x', (1140, 270, 80, 270), 'Quitar íconos')]),
    8: camino(),
    9: ('Las tarjetas del camino se montan; los términos (15, 10, 30 días y prórroga) mejor en tabla.',
        [('c', (540, 280, 440, 200), 'Se montan: mejor tabla')]),
    10: ('Tercer camino seguido: el traslado es un proceso, mejor ruta paso a paso.',
         [('c', PARADAS, 'Ruta paso a paso')]),
    11: ('Rejilla de 8 cajas: pasarla a ruta paso a paso, como la 2.1 (E06).',
         [('c', (80, 330, 1000, 280), 'Ruta paso a paso')]),
    12: audio(),
    13: PIES,
}

S['U1 L3'] = {
    1: PORTADA,
    2: BIEN, 3: BIEN, 4: BIEN,
    5: ('Camino de 2 paradas con medio lienzo vacío: mapa conceptual con las cuatro exigencias.',
        [('c', PARADAS, 'Mapa conceptual con las 4 exigencias')]),
    6: BIEN,
    7: ('Bien; dos pestañas en vez de dos cajas funciona igual.', []),
    8: BIEN, 9: BIEN,
    10: ('El caso no es el del DI vigente (carta de la ciudadana) y falta el audio.',
         [('c', 'Situación', 'Caso del DI vigente'), ('+', (860, 190, 360, 60), 'Falta el audio del caso')]),
    11: BIEN,
    12: PIES,
}

S['U1 L4'] = {
    1: PORTADA,
    2: ('El rótulo dice «Lección» sin número: «Lección 4».', [('c', (35, 135, 205, 55), 'Falta el 4')]),
    3: BIEN, 4: BIEN,
    5: ('Cinco paradas que se montan y la última se sale: mapa conceptual con su descarga.',
        [('c', PARADAS, 'Se montan: mapa conceptual')]),
    6: PIES,
}
