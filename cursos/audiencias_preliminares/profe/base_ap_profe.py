# -*- coding: utf-8 -*-
r"""Base de los videos de profe de «Audiencias preliminares y medidas de aseguramiento» (Prioridad 1, 20 nov 2026).
**Entrega provisional**: intro, cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos
(`ITEMS` lleva solo el lower third).

**Pedido.** Sebastián (20 nov): «ahora vamos a hacer lo mismo con estos», la carpeta de Drive «Videos Curso Virtual
FGN-UNAL» del curso (`1qXcS3F8bXq-yXtIz88b5U291yEfGwI37`): ocho grabaciones, la introducción y la recapitulación de
cada una de las cuatro unidades.

**Las fuentes.** 1280×720, 25 fps, H.264 High a ~880 kb/s, etiquetadas BT.601 (bt470bg), AAC estéreo a 48 kHz. Son
grabaciones de Teams con fondo virtual (el edificio de la DAE y el panel DAE/Fiscalía arriba a la izquierda) y el
rótulo de Teams con el nombre del profe abajo a la izquierda (x 0–180, y 684–717). Ya vienen editadas: arrancan con
2 a 3,8 s de silencio digital (−88 dB) y tres terminan pegadas a la última palabra (U2 introducción, U2 recapitulación,
U4 introducción). Las leyó el profe de corrido: no hay tomas repetidas ni pausas de más de 2 s.

**La ventana.** El rótulo de Teams se deja fuera de la ventana, no se tapa (CLAUDE.md, DA U3 L5): 1200×675 desde
(40, 0), que es 16:9 y termina en y=674, diez filas antes del rótulo. Escala ×1,6.

**Cuadros.** La fuente va a 25 fps y la línea a 23,976: el compuesto se escribe a 23,976 (`FPS_COMPUESTO`) para que
Resolve no tenga que conformar, y los tramos se cuentan a 25 (`FPS_FUENTE`).

**Documento del curso** (ficha «Vaciado_Curso Audiencias preliminares y medidas de aseguramiento», Word
`1TdXDfJV_j9MM45JcnWqbp4vvJjO2Ddz9`, y una por unidad): pide «Video de presentación» del curso (2.1), y por unidad el
video de la introducción (3.2) y el de la «Actividad de acompañamiento dirigido» (3.8: «una síntesis de los principales
temas abordados en la unidad»), que es la recapitulación. El cierre del curso (4.1) es un mensaje, sin video. El video
de presentación del curso no está en la carpeta.

**Nombres.** Curso: 1.1 de la ficha. Unidades: 3.1 de cada una; la de la unidad 4 repite la de la 3 en las dos fichas,
y va el nombre que le da la lista de contenidos del curso (2.x): «Intervención argumentada en audiencias preliminares y
ejercicio integrador». Profe: la ficha pone «Zuluaga John» como autor (1.5) y el rótulo de Teams dice «John Zuluaga
Taborda»: va ese nombre, con «Autor del curso».
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'herramientas',
                                'cartones'))
import balanceo as B  # noqa: E402

CLIP0 = 409
FPS = 24000 / 1001
FQ = 25.0
FPS_FUENTE = 25
FPS_COMPUESTO = '24000/1001'
ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16

RAIZ = 'D:/DAE MASTER/PRIORIDAD 1/CURSO - AUDIENCIAS PRELIMINARES Y MEDIDAS DE ASEGURAMIENTO/VIDEOS PROFE'
FUENTES = RAIZ + '/00 FUENTES/'
BIN_CURSO = ['PRIORIDAD 1', 'CURSO - AUDIENCIAS PRELIMINARES Y MEDIDAS DE ASEGURAMIENTO', 'VIDEOS PROFE']
MASTERS = 'D:/DAE/_masters_archivo/PRIORIDAD 1/CURSO - AUDIENCIAS PRELIMINARES Y MEDIDAS DE ASEGURAMIENTO/VIDEOS PROFE'
AE_DIR = RAIZ + '/00 MOTION GRAPHICS'
AEP = AE_DIR + '/AP_profe_mg.aep'          # no existe: la entrega provisional no lleva motion graphics
ICONOS = AE_DIR + '/iconos'
CURSO_LINEAS = ['Audiencias preliminares y', 'medidas de aseguramiento']
NOMBRE_CURSO = 'Audiencias preliminares y medidas de aseguramiento'
TITULO_BASE = None
XY, VENTANA = (40, 0), (1200, 675)
ANCHO = 615
AUDIO_META = 'I=-16:TP=-3:LRA=7'
PRESET_ENTREGA = 'medium'
PRESET_COMPUESTO = 'veryfast'
UNIDADES = {
    1: 'Naturaleza, fundamentos, finalidad y clasificación de las audiencias preliminares nominadas',
    2: 'Audiencias relacionadas con la libertad personal y la vinculación al proceso',
    3: 'Audiencias para la autorización y control de técnicas de investigación',
    4: 'Intervención argumentada en audiencias preliminares y ejercicio integrador',
}
FUENTE = {('INICIO', u): FUENTES + 'Unidad %d - Introducción.mp4' % u for u in range(1, 5)}
FUENTE.update({('CIERRE', u): FUENTES + 'Unidad %d - Recapitulación.mp4' % u for u in range(1, 5)})
# 23 nov 2026: llegaron a la carpeta del profe el inicio y el cierre del curso, que faltaban.
FUENTE.update({('INICIO', 'CURSO'): FUENTES + 'Apertura de curso.mp4', ('CIERRE', 'CURSO'): FUENTES + 'Cierre de curso.mp4'})
# El rótulo va a la izquierda, sobre la plaza del fondo: el profe ocupa el centro y la derecha.
LT = (40, 440)
PROFE = ('John Zuluaga\nTaborda', 'Autor del curso')


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


def armar_unidad(u, pieza, tramos):
    """Inicio (la introducción) o cierre (la recapitulación) de una unidad. `tramos` en segundos de la fuente:
    [(desde, hasta)]; el final del archivo va con su duración."""
    carpeta = 'UNIDAD %d/%s' % (u, pieza)
    prefijo = 'APU%d%s' % (u, pieza[0])
    r = RAIZ + '/' + carpeta
    tr = [(a, b, None) for a, b in tramos]
    return dict(
        R=r, BIN=BIN_CURSO + [carpeta.replace('/', ' - ')],
        ORIGINAL=FUENTE[(pieza, u)], COMPUESTO=r + '/01 VIDEO/%s_compuesto_v1.mp4' % prefijo,
        TITULO=r + '/02 CARTONES/carton titulo %s.mp4' % prefijo.lower(), SUB='Unidad %d. %s' % (u, UNIDADES[u]),
        NOMBRE_LINEA='AP - U%d - %s' % (u, pieza), EXPORT='audienciaspreliminares - U%d - %s' % (u, pieza) + '-v%d',
        PREFIJO=prefijo, TMP='D:/DAE/_tmp/ap_p/' + prefijo.lower(), TRAMOS=tr, T0=tr[0][0], T1=tr[-1][1],
        cuadro=cuadro_de(tr), MASTER_DIR=MASTERS + '/' + carpeta)


def armar_curso(pieza, sub, tramos):
    """Inicio o cierre del curso (23 nov 2026). Mismas reglas que las unidades; el cartón de título lleva
    «Inicio del curso» o «Cierre del curso», como en los demás cursos."""
    carpeta = 'CURSO/%s' % pieza
    prefijo = 'APC%s' % pieza[0]
    r = RAIZ + '/' + carpeta
    tr = [(a, b, None) for a, b in tramos]
    return dict(
        R=r, BIN=BIN_CURSO + [carpeta.replace('/', ' - ')],
        ORIGINAL=FUENTE[(pieza, 'CURSO')], COMPUESTO=r + '/01 VIDEO/%s_compuesto_v1.mp4' % prefijo,
        TITULO=r + '/02 CARTONES/carton titulo %s.mp4' % prefijo.lower(), SUB=sub,
        NOMBRE_LINEA='AP - CURSO - %s' % pieza, EXPORT='audienciaspreliminares - CURSO - %s' % pieza + '-v%d',
        PREFIJO=prefijo, TMP='D:/DAE/_tmp/ap_p/' + prefijo.lower(), TRAMOS=tr, T0=tr[0][0], T1=tr[-1][1],
        cuadro=cuadro_de(tr), MASTER_DIR=MASTERS + '/' + carpeta)


def rotulo(t):
    """El lower third del profe a 1,5 s de empezar, 7,5 s."""
    return [('lt01', 'lt', t + 1.5, t + 9.0, PROFE)]


def _p(texto, peso, px, gap):
    return B.piezas(texto, peso, px, gap, ANCHO)


def cita(t):
    return _p(t, 'bold', TIT, 0) if len(t) <= 78 else _p(t, 'med', CUE, 0)


def c_tit(titulo, cuerpo):
    return _p(titulo, 'bold', TIT, 0) + _p(cuerpo, 'med', CUE, GAP_TIT)


def lista(titulo, *filas):
    return {'titulo': titulo, 'filas': list(filas)}
