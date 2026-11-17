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

**Unidades (17 nov 2026): inicio y cierre de las unidades 1 a 4, entrega provisional.** Sebastián:
«vamos a dejarlos por favor con versión provisional, queriendo decir: solo hagamos intro y outro,
placas de entrada y salida y títulos del profe por ahora, para que salgan más rápido». Ocho planes
(`plan_tau1i` … `plan_tau4c`, con `armar_unidad`) que llevan en `ITEMS` solo el lower third.
- **Fuentes.** Drive del curso → VIDEOS › «VIDEOS UNIDADES» (`1Cg7mvB8pLSoFVS43ao_kNxgTjL8tf7kE`,
  JP, 17 nov). Son otra grabación que las del inicio y el cierre del curso: **1920×1080**, H.264
  Constrained Baseline, 30 fps parejos, AAC estéreo a 48 kHz (−17,5 a −18,0 LUFS, picos de −0,2
  a −0,5 dBTP), sin etiquetas de color. De 6:06 a 7:57 cada una; 99.296 cuadros en total.
- **Color: BT.709.** Se midió el rojo, el azul y el amarillo del panel DAE/Fiscalía leyendo la
  fuente como 601 y como 709, contra el compuesto del inicio del curso: como 709 dan (214, 49, 64),
  (11, 88, 160) y (241, 200, 19), contra (216, 45, 62), (5, 82, 161) y (236, 200, 27); como 601 el
  rojo cae a (197, 28, 62). Van con `MATRIZ_FUENTE = 'bt709'`.
- **Una sola toma, leída de corrido.** La imagen repite cuadros (la diferencia entre cuadros
  alterna ceros y saltos de 5 a 9), así que el pico aislado no sirve para buscar cortes; no hay
  ninguno por encima de 9,3, ni pausas de más de 2,6 s. Entran de medio segundo antes de la
  primera palabra a 0,8 s después de la última. Hay tropiezos sueltos («funcio-, fu--»), que se
  dejan.
- **Ventana: el cuadro entero** (`XY_UNIDADES`, `VENTANA_UNIDADES`). El profe está más cerca de la
  cámara que en los videos del curso: el borde izquierdo de la cabeza va de x 376–420 (p5) a
  476–524 (p50) de 1920, y el tope de la cabeza de y 40–68 (p5) a 64–92 (p50). No hay de dónde
  recortar. **La columna de cartones (x 86–640) le cae en la cara**: para la versión con gráficos
  hay que decidir antes cómo van (columna más angosta, texto abajo o gráficos a pantalla), y no
  alcanza con agregar ítems.
- El lower third va a la izquierda, sobre el hombro y la plaza, con las medidas del curso.

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
# inicio y cierre de las unidades: fuente de 1920×1080, el cuadro entero
XY_UNIDADES, VENTANA_UNIDADES = (0, 0), (1920, 1080)
MAXW = 470
ANCHO = MAXW
# el nombre a 40 px y el cargo a 440 de ancho: termina en x≈610, sobre la plaza y lejos de la cara
LT = (40, 440)
AUDIO_META = 'I=-16:TP=-3:LRA=7'
PROFE = ('Juan David Peña Gómez',
         'Coautor del curso. Investigador académico de la Universidad Nacional de Colombia')
# Los nombres de las unidades, del formato de diseño del curso (FGN-AP01-F-204, «07_09_2026 Definitivo
# DISEÑO CURSO_TERMINACIONES ANTICIPADAS», `1g8GxE5ZjdCM1xAXowHrxgBPJkC-tIs66`): «Ruta de aprendizaje».
UNIDADES = {1: 'Archivo de la indagación', 2: 'La preclusión en el proceso penal',
            3: 'Aplicación del principio de oportunidad', 4: 'Preacuerdos y negociaciones en el sistema penal'}


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
        R=r, BIN=BIN_CURSO + [carpeta.replace('/', ' - ') + ' - PROFE'],
        ORIGINAL=r + '/01 VIDEO/' + fuente, COMPUESTO=r + '/01 VIDEO/%s_compuesto_v1.mp4' % prefijo,
        TITULO=r + '/02 CARTONES/carton titulo %s.mp4' % prefijo.lower(), SUB=sub, NOMBRE_LINEA=linea,
        EXPORT=export + '-v%d', PREFIJO=prefijo, TMP='D:/DAE/_tmp/sr_ta/' + prefijo.lower(),
        TRAMOS=[(t0, t1, None)], T0=t0, T1=t1, cuadro=cuadro, MASTER_DIR=MASTERS + '/' + carpeta)


def armar_unidad(u, pieza, k0, k1):
    """Inicio o cierre de una unidad (`pieza` = 'INICIO' | 'CIERRE'): carpeta «UNIDAD n/INICIO», línea
    «TA - Un - INICIO», entrega «terminacionesanticipadas - Un - INICIO» y el nombre de la unidad en el
    cartón de título, como en SRPA."""
    return armar('ta_u%d_%s_fuente.mp4' % (u, pieza.lower()), 'UNIDAD %d/%s' % (u, pieza),
                 'Unidad %d. %s' % (u, UNIDADES[u]), 'TA - U%d - %s' % (u, pieza),
                 'terminacionesanticipadas - U%d - %s' % (u, pieza), 'TAU%d%s' % (u, pieza[0]), k0, k1)


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
