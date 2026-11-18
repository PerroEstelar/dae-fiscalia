# -*- coding: utf-8 -*-
r"""Base de los videos de profe de «Justicia restaurativa en la práctica del fiscal» (Prioridad 1, 18 nov
2026). **Entrega provisional**: intro, cartón de título, lower thirds, cartón de cierre y outro; el cuerpo va
sin gráficos (`ITEMS` lleva solo los lower thirds).

**Pedido.** Sebastián (18 nov): «por favor continúa con justicia restaurativa [carpeta VIDEOS del curso,
`1s-ZDIhTCPriybRjIIzSYx1GIqkcmgZvy`]; creo que por ahora el único es el cierre del curso».

**Nombre del curso.** De la ficha («Prioridad 1 - Presentacion Vaciado_ Justicia Restaurativa en la Práctica del
Fiscal.docx», `1bQcllAcXC6Ka9i76T3Ep4ZLYv1o1YY2y`, 1.1): «Justicia restaurativa en la práctica del fiscal».

**Los profes.** Son dos y salen los dos todo el tiempo, en dos mosaicos de videollamada. La ficha (1.5 y 2.1)
dice: autores «Víctor Hugo Ospina Vargas / Martín Posada Martínez»; «Víctor Hugo Ospina Vargas, profesor de
pregrado y posgrado de la Universidad Nacional, y Martín Posada Martínez, investigador académico», y los llama
coautores. En el video se presentan ellos mismos («lo construimos Martín Posada Martínez… y quien habla, Víctor
Hugo Ospina Vargas»; Scribe oye «Espina»).

**La fuente** es del mismo editor que las de Bienes: 1920×1080, 30 fps parejos, H.264 Constrained Baseline,
`smpte170m` (BT.601: no lleva `MATRIZ_FUENTE`), y **trae una intro y un outro pegados**, que se sacan.

**El cuadro.** Un lienzo blanco con dos mosaicos de 936×528: el de la izquierda en x 7–942 y el de la derecha en
x 982–1916, los dos en y 290–817. Arriba y abajo queda blanco. Va el cuadro entero: no hay recorte que deje a
los dos.

**Lower thirds: debajo de cada mosaico, sobre el blanco, en tinta azul.** El blanco con sombra de la serie no se
lee sobre el lienzo, y dentro del mosaico taparía a la persona. Cada rótulo va bajo su mosaico (`x`), con la tinta
del subtítulo del cartón de título (`titulo_srpa.COLOR_SUB`), sin sombra (opciones del rótulo en
`cartones_srpa.lower_third`).

Los tiempos de cada plan están en segundos de la fuente.
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

RAIZ = 'E:/DAE MASTER/PRIORIDAD 1/CURSO - JUSTICIA RESTAURATIVA'
BIN_CURSO = ['PRIORIDAD 1', 'CURSO - JUSTICIA RESTAURATIVA']
MASTERS = 'D:/DAE/_masters_archivo/PRIORIDAD 1/CURSO - JUSTICIA RESTAURATIVA'
AE_DIR = RAIZ + '/00 MOTION GRAPHICS'
AEP = AE_DIR + '/JR_profe_mg.aep'          # no existe todavía: la entrega provisional no lleva motion graphics
ICONOS = AE_DIR + '/iconos'
CURSO_LINEAS = ['Justicia restaurativa', 'en la práctica del fiscal']
NOMBRE_CURSO = 'Justicia restaurativa en la práctica del fiscal'
TITULO_BASE = None
XY, VENTANA = (0, 0), (1920, 1080)
ANCHO = 615
AUDIO_META = 'I=-16:TP=-3:LRA=7'
PRESET_ENTREGA = 'medium'
TINTA_LT = (22, 58, 79)                    # la del subtítulo del cartón de título
_LT = dict(top=852, ancho=760, tinta=TINTA_LT)
VICTOR = ('Víctor Hugo Ospina Vargas',
          'Coautor del curso. Profesor de pregrado y posgrado de la Universidad Nacional de Colombia',
          dict(_LT, x=40))
MARTIN = ('Martín Posada Martínez', 'Coautor del curso. Investigador académico', dict(_LT, x=1015))


def armar(fuente, carpeta, sub, linea, export, prefijo, k0, k1):
    """Constantes de un plan: `fuente` es el archivo de `01 VIDEO`, `carpeta` la de la pieza bajo RAIZ, y k0–k1
    los cuadros de la fuente que entran (k1 exclusivo)."""
    r = RAIZ + '/' + carpeta
    t0, t1 = k0 / FQ, k1 / FQ

    def cuadro(t):
        if not t0 - 1e-6 <= t <= t1 + 1e-6:
            raise ValueError('%.2f cae fuera del tramo' % t)
        return CLIP0 + int(round((t - t0) * FPS))

    return dict(
        R=r, BIN=BIN_CURSO + [carpeta.replace('/', ' - ') + ' - PROFE'],
        ORIGINAL=r + '/01 VIDEO/' + fuente, COMPUESTO=r + '/01 VIDEO/%s_compuesto_v1.mp4' % prefijo,
        TITULO=r + '/02 CARTONES/carton titulo %s.mp4' % prefijo.lower(), SUB=sub, NOMBRE_LINEA=linea,
        EXPORT=export + '-v%d', PREFIJO=prefijo, TMP='D:/DAE/_tmp/jr_p/' + prefijo.lower(),
        TRAMOS=[(t0, t1, None)], T0=t0, T1=t1, cuadro=cuadro, MASTER_DIR=MASTERS + '/' + carpeta)


def _p(texto, peso, px, gap):
    return B.piezas(texto, peso, px, gap, ANCHO)


def cita(t):
    return _p(t, 'bold', TIT, 0) if len(t) <= 78 else _p(t, 'med', CUE, 0)


def c_tit(titulo, cuerpo):
    return _p(titulo, 'bold', TIT, 0) + _p(cuerpo, 'med', CUE, GAP_TIT)


def lista(titulo, *filas):
    return {'titulo': titulo, 'filas': list(filas)}
