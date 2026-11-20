# -*- coding: utf-8 -*-
r"""Base de los videos de profe de «Investigación judicial y forense de desaparición forzada» (Prioridad 3, 19 nov
2026). **Entrega provisional**: intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin
gráficos (`ITEMS` lleva solo el lower third).

**Pedido.** Sebastián (19 nov): «de un solo video tenemos que sacar inicio y cierre del curso general y contenido de
las unidades que sean necesarias según el documento del curso, con gráfica provisional y todo lo que implica (…)
haz la transcripción del video y coteja con el documento del curso, no te salgas del lineamiento del documento,
crea las unidades con base en él y piensa muy bien en cómo distribuir los segmentos».

**La fuente.** Una sola grabación: `E:\DAE MASTER\CURSO DESAPARICION FORZADA\Desaparición Forzada  Inicio -
Curso.mp4` (4,1 GB, 1:57:55,8, 212.273 cuadros a 30 fps, H.264 Constrained Baseline sin etiquetas de color, AAC
estéreo a 48 kHz). El profe lee de corrido los guiones de todos los videos del curso, uno tras otro, y entre uno y
otro dice en voz alta dónde termina y qué viene («Ahí termina el primer video. Vamos a comenzar el segundo video»).
Todas las piezas salen de este archivo; cada plan lleva sus `TRAMOS` en segundos de la fuente. STT (Scribe, WAV a
16 kHz): 13.047 palabras.

**Lo que pide el documento del curso** («Curso_Investigacion Judicial y forense de desaparicion forzada v nov 11 RV
DAE FGN MPNN nov 17 2026.pdf», `1bOqazSl33_tby-opyvhPgn5MMKMKNXxg`): «Video de inicio del curso», y por cada unidad
«Video de presentación de la unidad», «Video de retroalimentación de evaluaciones» y «Video de cierre de la unidad»,
y «Video de cierre del curso». Son 17 piezas. Lo que el profe grabó por unidad son cinco guiones: la bienvenida, la
finalización y síntesis, y tres retroalimentaciones (actividad 1, actividad 2 y cuestionario sumativo). Las tres
retroalimentaciones van juntas en el único video de retroalimentación que el documento pone en cada unidad: en la
ficha las dos actividades también son ejercicios evaluados con retroalimentación por opción, y el documento describe
ese video como el que analiza «las respuestas de los cuestionarios». La unidad 5 no trae el encabezado del video de
retroalimentación, pero su «acompañamiento dirigido» y su «Finalización» lo nombran, y el profe lo grabó: va igual.

**La imagen.** Un lienzo blanco con la imagen del profe adentro, como las fuentes de Justicia restaurativa: la
imagen va de x 16 a 1903 y de y 9 a 1070 (1888×1062, 16:9), con blanco alrededor y una raya oscura en las filas 0–1.
La ventana toma solo la imagen (`XY`, `VENTANA`): sin el marco blanco ni la raya, ×1,017.

**Color.** Sin etiquetas. El rojo, el azul y el amarillo del panel DAE/Fiscalía leídos como BT.601 dan (220, 33, 70),
(2, 91, 165) y (247, 211, 18); como BT.709, (235, 52, 69), (0, 87, 170) y (252, 203, 10); en un compuesto ya
entregado del mismo fondo, (216, 45, 62), (5, 82, 161) y (236, 200, 27). Va como BT.601, que es lo que supone
`ic_pieza` (no lleva `MATRIZ_FUENTE`).

**Nombre del curso.** De la ficha (1.1): «Investigación Judicial y Forense de Desaparición Forzada». Los nombres de
las unidades son los de «Nombre de la unidad» de cada una (3.1 a 3.5).

**Dónde.** E: tiene 4 GB libres: el árbol va en `D:\DAE MASTER\PRIORIDAD 03\CURSO DESAPARICION FORZADA - VIDEOS
PROFE\` y la fuente se lee de E: (no se copia). Los tiempos de cada plan están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'herramientas',
                                'cartones'))
import balanceo as B  # noqa: E402

CLIP0 = 409
FPS = 24000 / 1001
FQ = 30.0
ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16

FUENTE = 'E:/DAE MASTER/CURSO DESAPARICION FORZADA/Desaparición Forzada  Inicio - Curso.mp4'
RAIZ = 'D:/DAE MASTER/PRIORIDAD 03/CURSO DESAPARICION FORZADA - VIDEOS PROFE'
BIN_CURSO = ['PRIORIDAD 03', 'CURSO DESAPARICION FORZADA - VIDEOS PROFE']
MASTERS = 'D:/DAE/_masters_archivo/PRIORIDAD 03/CURSO DESAPARICION FORZADA - VIDEOS PROFE'
AE_DIR = RAIZ + '/00 MOTION GRAPHICS'
AEP = AE_DIR + '/DF_profe_mg.aep'          # no existe: la entrega provisional no lleva motion graphics
ICONOS = AE_DIR + '/iconos'
CURSO_LINEAS = ['Investigación judicial y forense', 'de desaparición forzada']
NOMBRE_CURSO = 'Investigación judicial y forense de desaparición forzada'
TITULO_BASE = None
XY, VENTANA = (16, 9), (1888, 1062)
ANCHO = 615
AUDIO_META = 'I=-16:TP=-3:LRA=7'
PRESET_ENTREGA = 'medium'
UNIDADES = {
    1: 'Comprensión y marco jurídico del delito de desaparición forzada',
    2: 'Mecanismos de búsqueda de personas desaparecidas',
    3: 'La actividad de la Fiscalía General de la Nación y los roles intervinientes para la atención, investigación '
       'y judicialización de la desaparición forzada',
    4: 'Atención a víctimas y familiares',
    5: 'Investigación de la desaparición forzada',
}
# El profe no dice su nombre en la grabación y la ficha nombra a tres autores (Estanislao Escalante Barreto, autor
# experto; Carlos Eduardo Valdés Moreno, coautor; Cristian Camilo Martínez Álvarez, auxiliar investigativo). Por la
# imagen no es Estanislao (comparado con su cierre del curso de SRPA). Sebastián lo confirmó (19 nov): Carlos Eduardo
# Valdés Moreno. El cargo es el de la ficha (1.5, «Coautor»).
# El rótulo va a la izquierda, sobre la plaza: el hombro del profe empieza hacia x≈540 de salida y el rótulo
# termina en x≈491 con el nombre en dos renglones (simulado sobre 20 cuadros de toda la grabación, uno por pieza).
LT = (40, 440)
PROFE = ('Carlos Eduardo\nValdés Moreno', 'Coautor del curso')


def cuadro_de(tramos):
    """Segundos de la fuente → cuadro de la línea, descontando los cortes."""
    def cuadro(t):
        acum = 0.0
        for a, b, _w in tramos:
            if a - 1e-6 <= t <= b + 1e-6:
                return CLIP0 + int(round((acum + t - a) * FPS))
            acum += b - a
        raise ValueError('%.2f cae en un corte' % t)
    return cuadro


def armar(carpeta, sub, linea, export, prefijo, tramos):
    """Constantes de un plan: `carpeta` la de la pieza bajo RAIZ («UNIDAD 1/INICIO») y `tramos` los de la fuente, en
    segundos: [(desde, hasta), …]."""
    r = RAIZ + '/' + carpeta
    tr = [(a, b, None) for a, b in tramos]
    return dict(
        R=r, BIN=BIN_CURSO + [carpeta.replace('/', ' - ')],
        ORIGINAL=FUENTE, COMPUESTO=r + '/01 VIDEO/%s_compuesto_v1.mp4' % prefijo,
        TITULO=r + '/02 CARTONES/carton titulo %s.mp4' % prefijo.lower(), SUB=sub, NOMBRE_LINEA=linea,
        EXPORT=export + '-v%d', PREFIJO=prefijo, TMP='D:/DAE/_tmp/df_p/' + prefijo.lower(),
        TRAMOS=tr, T0=tr[0][0], T1=tr[-1][1], cuadro=cuadro_de(tr), MASTER_DIR=MASTERS + '/' + carpeta)


PIEZA = {'INICIO': 'INICIO', 'CIERRE': 'CIERRE', 'RETROALIMENTACION': 'RETROALIMENTACION'}


def armar_unidad(u, pieza, tramos):
    """Inicio, cierre o retroalimentación de una unidad. El cartón de título lleva el nombre de la unidad en el inicio
    y el cierre, como en los demás cursos, y «Retroalimentación de evaluaciones» en la retroalimentación (el nombre
    del video en el documento)."""
    sub = 'Unidad %d. %s' % (u, UNIDADES[u] if pieza != 'RETROALIMENTACION' else 'Retroalimentación de evaluaciones')
    return armar('UNIDAD %d/%s' % (u, pieza), sub, 'DF - U%d - %s' % (u, pieza),
                 'desaparicionforzada - U%d - %s' % (u, pieza), 'DFU%d%s' % (u, pieza[0]), tramos)


def rotulo(t):
    """El lower third del profe a 1,5 s de empezar, 7,5 s; ninguno si todavía no está confirmado el nombre."""
    return [('lt01', 'lt', t + 1.5, t + 9.0, PROFE)] if PROFE else []


def _p(texto, peso, px, gap):
    return B.piezas(texto, peso, px, gap, ANCHO)


def cita(t):
    return _p(t, 'bold', TIT, 0) if len(t) <= 78 else _p(t, 'med', CUE, 0)


def c_tit(titulo, cuerpo):
    return _p(titulo, 'bold', TIT, 0) + _p(cuerpo, 'med', CUE, GAP_TIT)


def lista(titulo, *filas):
    return {'titulo': titulo, 'filas': list(filas)}
