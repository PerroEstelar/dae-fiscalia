# -*- coding: utf-8 -*-
r"""Base de los dos videos de profe a cámara de «Terminaciones anticipadas»: inicio y cierre
del curso (17 nov 2026).

**Pedido.** Del inventario de SRPA, Ley 1826 y Terminaciones anticipadas salieron cinco
videos de profe grabados y sin producir. Sebastián: «empieza con lo que falta del material que
tenemos pero no se lo hemos producido, cada uno excelentemente hecho siguiendo todos los
protocolos, de pe a pa, los dejas subidos y actualizas el inventario». El formato es el de
los profes de Derechos humanos, Enfoque diferencial y Bienes:
- intro FGN y cartón de título con el nombre del curso y el de la pieza;
- el profe a cámara, con cartones de caja y listas de AE a la izquierda y lower third;
- cartón de cierre y outro.

**Profe.** Juan David Peña Gómez. Lo dice en el inicio: «elaborado por Víctor Hugo Ospina
Vargas y quien les habla, Juan David Peña Gómez». El documento de introducción del curso lo
presenta como «investigador académico» de la Universidad Nacional de Colombia.

**Fuentes.** Drive del curso → VIDEOS:
- inicio del curso (`1YmOIgt9Qo49ayMXJm804QYeZWTUWjRDn`): 14.517 cuadros, 483,9 s;
- cierre del curso (`1AA096BLK_v7yd9aE3qISuidZvfX5M0nh`): 14.168 cuadros, 472,27 s.
Las dos son grabaciones de Teams: 1280×720, H.264 Constrained Baseline, 30 fps parejos,
BT.601, AAC estéreo a 44,1 kHz, con el fondo virtual del edificio y el panel DAE/Fiscalía.
Están leídas al guion, sin pausas de más de 2 s ni tomas repetidas: van enteras.

**Ventana 1067×600 desde (0, 20), ×1,8.** El profe está muy cerca de la cámara y corrido a
la derecha. Medido sobre una muestra cada 2 s (fondo = mediana): el borde izquierdo de la
cabeza va de x 389 (p5) a 472 (p50) en el inicio y de 333 (p5) a 504 (p50) en el cierre.
Con esa ventana queda desde x≈700 de salida (p5 del inicio) y la columna de texto se
angosta a 470 (`MAXW`): la caja termina en x=640. El panel DAE/Fiscalía entra entero. Se
probó con la caja dibujada sobre diez cuadros de cada video (`D:\DAE\_tmp\sr_ta\tiras`).

**Dónde.** E: no tiene espacio (6 GB libres), así que el árbol va en
`D:\DAE MASTER\CURSO 4 - Curso Terminaciones Anticipadas\`, con un `LEER` en la carpeta del
curso de E:. El proyecto de AE es `00 MOTION GRAPHICS\TA_profe_mg.aep` (copia de
`SRPA_mg.aep`), en esa misma carpeta de D:. Los másters de 32 Mb/s van a
`D:\DAE\_masters_archivo\CURSO 4 - Curso Terminaciones Anticipadas\`.

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

RAIZ = 'D:/DAE MASTER/CURSO 4 - Curso Terminaciones Anticipadas'
BIN_CURSO = ['CURSO 4 - TERMINACIONES ANTICIPADAS']
MASTERS = 'D:/DAE/_masters_archivo/CURSO 4 - Curso Terminaciones Anticipadas'
AE_DIR = RAIZ + '/00 MOTION GRAPHICS'
AEP = AE_DIR + '/TA_profe_mg.aep'
ICONOS = AE_DIR + '/iconos'
CURSO_LINEAS = ['Terminaciones anticipadas']
TITULO_BASE = None
XY, VENTANA = (0, 20), (1067, 600)
MAXW = 470
ANCHO = MAXW
# el nombre a 40 px y el cargo a 440 de ancho: termina en x≈610, sobre la plaza y lejos de la cara
LT = (40, 440)
AUDIO_META = 'I=-16:TP=-3:LRA=7'
PROFE = ('Juan David Peña Gómez',
         'Coautor del curso. Investigador académico de la Universidad Nacional de Colombia')


def armar(fuente, carpeta, sub, linea, export, prefijo, k0, k1):
    """Constantes de un plan: `fuente` es el archivo de `01 VIDEO`, `carpeta` la de la pieza
    bajo RAIZ, y k0–k1 los cuadros de la fuente que entran (k1 exclusivo)."""
    r = RAIZ + '/' + carpeta
    t0, t1 = k0 / FQ, k1 / FQ

    def cuadro(t):
        if not t0 - 1e-6 <= t <= t1 + 1e-6:
            raise ValueError('%.2f cae fuera del tramo' % t)
        return CLIP0 + int(round((t - t0) * FPS))

    return dict(
        R=r, BIN=BIN_CURSO + [carpeta + ' - PROFE'],
        ORIGINAL=r + '/01 VIDEO/' + fuente, COMPUESTO=r + '/01 VIDEO/%s_compuesto_v1.mp4' % prefijo,
        TITULO=r + '/02 CARTONES/carton titulo %s.mp4' % prefijo.lower(), SUB=sub, NOMBRE_LINEA=linea,
        EXPORT=export + '-v%d', PREFIJO=prefijo, TMP='D:/DAE/_tmp/sr_ta/' + prefijo.lower(),
        TRAMOS=[(t0, t1, None)], T0=t0, T1=t1, cuadro=cuadro, MASTER_DIR=MASTERS + '/' + carpeta)


def _p(texto, peso, px, gap):
    # renglones parejos (herramientas/cartones/balanceo.py): sin palabras solas abajo
    return B.piezas(texto, peso, px, gap, ANCHO)


def cita(t):
    return _p(t, 'bold', TIT, 0) if len(t) <= 78 else _p(t, 'med', CUE, 0)


def c_tit(titulo, cuerpo):
    return _p(titulo, 'bold', TIT, 0) + _p(cuerpo, 'med', CUE, GAP_TIT)


def c_ante(ante, titulo, cuerpo=None):
    ls = _p(ante, 'med', ANTE, 0) + _p(titulo, 'bold', TIT, GAP_ANTE)
    if cuerpo:
        ls += _p(cuerpo, 'med', CUE, GAP_CUE + 8)
    return ls


def c_nota(ante, cuerpo):
    # antetítulo y cuerpo, sin título
    return _p(ante, 'med', ANTE, 0) + _p(cuerpo, 'med', CUE, GAP_ANTE)


def c_suelta(t):
    return _p(t, 'bold', SUELTA, 0)


def lista(titulo, *filas):
    return {'titulo': titulo, 'filas': list(filas)}
