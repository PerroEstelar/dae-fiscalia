# -*- coding: utf-8 -*-
"""Curso «Sistema de responsabilidad penal para adolescentes y justicia
restaurativa»: los siete videos de profes a cámara (11 nov 2026).

Pedido de Sebastián: «necesitamos realizarlos en ese formato, intro, outro,
lower thirds, frases más relevantes en pantalla, gráfica con aftr… cartón de
entrada y de salida con el nombre del curso y como subtítulo justo abajo el
nombre de la unidad». El formato es el de las introducciones de Delitos
ambientales: intro FGN, cartón de título, el profe a cámara con cartones de caja
y motion graphics a la izquierda, lower third, cartón de cierre y outro.

Fuente: Drive, curso → VIDEOS/UNIDADES (siete mp4 de Teams, 1280×720, 30 fps,
fondo virtual DAE/Fiscalía). Se miraron y se transcribieron todos (Scribe,
`03 VOCES/stt`) para ubicarlos:

    clave  archivo original                   qué es                         profe
    curso  Inicio Curso.mp4                   presentación del curso 15:21   Estanislao Escalante Barreto
    u1b    Unidad1-presentacion.mp4           bienvenida de la U1     8:39   Estanislao Escalante Barreto
    u3b    Unidad 3 - presentacion - a.mp4    bienvenida de la U3     3:43   Carlos Humberto Ramírez Romero
    u3d    Unidad 3 - presentacion - b.mp4    desarrollo de la U3    39:31   Carlos Humberto Ramírez Romero
    u3c    Unidad 3 - cierrre.mp4             cierre de la U3        11:21   Carlos Humberto Ramírez Romero
    u4c    Unidad 4 - cierrre.mp4             cierre de la U4         9:01   Carlos Humberto Ramírez Romero
    u5c    Unidad 5 - cierrre.mp4             cierre de la U5        17:43   Carlos Humberto Ramírez Romero

Los nombres van en minúscula salvo la primera palabra, como el de Delitos
ambientales: el «sistema de responsabilidad penal para adolescentes» es el
nombre genérico del sistema (así lo escribe el artículo 139 de la Ley 1098),
no un título.
"""

CURSO_NOMBRE = 'Sistema de responsabilidad penal para adolescentes y justicia restaurativa'
CURSO_LINEAS = ['Sistema de responsabilidad penal para', 'adolescentes y justicia restaurativa']

UNIDADES = {
    1: 'Principios y sentido de un sistema de responsabilidad penal para adolescentes',
    2: 'Autoridades y políticas públicas de prevención en el sistema de responsabilidad '
       'penal para adolescentes',
    3: 'Principio de oportunidad en el marco de la justicia restaurativa y terapéutica',
    4: 'Justicia restaurativa y terapéutica: implementación en el sistema de responsabilidad '
       'penal para adolescentes',
    5: 'Medidas restrictivas de derechos y la sanción con sentido educativo y restaurativo',
}

RAIZ = 'E:/DAE MASTER/PRIORIDAD 1/CURSO - SRPA Y JUSTICIA RESTAURATIVA'
BIN_RAIZ = 'CURSO - SRPA Y JUSTICIA RESTAURATIVA'
SUBCARPETAS = ['01 VIDEO', '02 CARTONES', '03 VOCES', '05 EXPORTS', '09 MOTION GRAPHICS',
               '10 TIMELINE SEBASTIAN']

ESTANISLAO = ('Estanislao Escalante Barreto',
              'Docente e investigador de la Facultad de Derecho, Ciencias Políticas y Sociales '
              'de la Universidad Nacional de Colombia')
CARLOS = ('Carlos Humberto Ramírez Romero',
          'Juez séptimo penal de conocimiento para adolescentes de Bogotá')

# Ventana de la fuente (x0, y0) que se lleva a 1920×1080. Ancho 1143 y alto 643
# (×1,68): el profe queda corrido a la derecha, la cara desde x≈770, y a la
# izquierda queda la caja de los cartones (x 62–790, y 250–720), como en las
# introducciones de Delitos ambientales. Se va además el filete blanco de 10 px
# que trae el fondo virtual del edificio. En el fondo aéreo (u3b, u3d) el profe
# está más abajo y el logo más arriba: y0=30.
VENTANA = (1143, 643)

VIDEOS = {
    'curso': {'carpeta': 'PRESENTACION DEL CURSO', 'unidad': 0, 'tipo': 'PRESENTACION',
              'original': 'Inicio Curso.mp4', 'profe': ESTANISLAO, 'xy': (12, 40), 'ganancia': -0.4},
    'u1b': {'carpeta': 'UNIDAD 1/BIENVENIDA', 'unidad': 1, 'tipo': 'BIENVENIDA',
            'original': 'Unidad1-presentacion.mp4', 'profe': ESTANISLAO, 'xy': (12, 40), 'ganancia': -0.1},
    'u3b': {'carpeta': 'UNIDAD 3/BIENVENIDA', 'unidad': 3, 'tipo': 'BIENVENIDA',
            'original': 'Unidad 3 - presentacion - a.mp4', 'profe': CARLOS, 'xy': (12, 30), 'ganancia': -6.0},
    'u3d': {'carpeta': 'UNIDAD 3/DESARROLLO', 'unidad': 3, 'tipo': 'DESARROLLO',
            'original': 'Unidad 3 - presentacion - b.mp4', 'profe': CARLOS, 'xy': (12, 30), 'ganancia': -4.8},
    'u3c': {'carpeta': 'UNIDAD 3/CIERRE', 'unidad': 3, 'tipo': 'CIERRE',
            'original': 'Unidad 3 - cierre.mp4', 'profe': CARLOS, 'xy': (12, 40), 'ganancia': -3.1},
    'u4c': {'carpeta': 'UNIDAD 4/CIERRE', 'unidad': 4, 'tipo': 'CIERRE',
            'original': 'Unidad 4 - cierre.mp4', 'profe': CARLOS, 'xy': (12, 40), 'ganancia': -4.9},
    'u5c': {'carpeta': 'UNIDAD 5/CIERRE', 'unidad': 5, 'tipo': 'CIERRE',
            'original': 'Unidad 5 - cierre.mp4', 'profe': CARLOS, 'xy': (12, 40), 'ganancia': -3.1},
}

# Tramos de la fuente que se quedan, en segundos. Un tramo puede llevar su propia
# ventana (x0, y0, ancho, alto): es el acercamiento que tapa un salto.
#   u1b: a los 4:17 el profe dice «Corta ahí ese último minutico y volvemos a
#        empezar» y retoma con «quienes conocen la convención…». Se quita de la
#        pausa después de «infancia-adolescencia,» (256,55) a la pausa antes de
#        «quienes» (277,10). Lo que sigue va acercado hasta la pausa de 303,8,
#        para que el salto se lea como cambio de plano.
#   u3d: al final el profe le habla al técnico («Profe, ¿me escucha?»). Se corta
#        después de «Muchas gracias.».
TRAMOS = {
    'u1b': [(0.0, 256.55, None), (277.10, 303.80, (150, 110, 920, 518)), (303.80, None, None)],
    'u3d': [(0.0, 2363.0, None)],
}


def tramos(clave):
    return TRAMOS.get(clave, [(0.0, None, None)])


def a_salida(clave, t):
    """Segundo de la fuente → segundo del clip compuesto (después de los cortes)."""
    out = 0.0
    for a, b, _v in tramos(clave):
        if t < a:
            return out
        if b is None or t <= b:
            return out + t - a
        out += b - a
    return out


def carpeta(clave):
    return '%s/%s' % (RAIZ, VIDEOS[clave]['carpeta'])


def compuesto(clave):
    return '%s/01 VIDEO/SRPA_%s_compuesto_v1.mp4' % (carpeta(clave), clave)


def subtitulo(clave):
    u = VIDEOS[clave]['unidad']
    if u == 0:
        return 'Presentación del curso'
    return 'Unidad %d. %s' % (u, UNIDADES[u])


def titulo_carton(clave):
    """El cartón de título es uno por unidad (y uno del curso)."""
    u = VIDEOS[clave]['unidad']
    if u == 0:
        return '%s/02 CARTONES/carton titulo srpa curso.mp4' % carpeta(clave)
    return '%s/UNIDAD %d/02 CARTONES/carton titulo srpa u%d.mp4' % (RAIZ, u, u)


def nombre_linea(clave):
    v = VIDEOS[clave]
    u = 'CURSO' if v['unidad'] == 0 else 'U%d' % v['unidad']
    return 'SRPA - %s - %s' % (u, v['tipo'])


def nombre_export(clave, n=1):
    v = VIDEOS[clave]
    u = 'CURSO' if v['unidad'] == 0 else 'U%d' % v['unidad']
    return 'srpa - %s - %s-v%d' % (u, v['tipo'], n)
