# -*- coding: utf-8 -*-
r"""Base de los videos de profe de SRPA que llegaron después de la tanda del 11 nov (17 nov 2026).

**Pedido.** Del inventario de SRPA, Ley 1826 y Terminaciones anticipadas salieron cinco videos
de profe grabados y sin producir. Sebastián: «empieza con lo que falta del material que
tenemos pero no se lo hemos producido, cada uno excelentemente hecho siguiendo todos los
protocolos, de pe a pa, los dejas subidos y actualizas el inventario».

De SRPA eran tres piezas (Drive del curso → VIDEOS/UNIDADES):
- **cierre de la unidad 1** (`Unidad 1 - cierre.mp4`, `18Gdlyg_7e0q_6stYaBnG48pSAENnca9A`):
  Estanislao Escalante Barreto. Es el plan `plan_sr1c`.
- **presentación de la unidad 2** y **cierre de la unidad 2** (partes A y B): otro profe, que no
  dice su nombre, grabado con cámara contra una pared blanca, sin el fondo virtual. **En pausa**
  por indicación de Sebastián (17 nov): «lo más probable es que alguien más me va a enviar los
  videos con el fondo adecuado». Lo que quedó medido y preparado está en el README del curso.

Estos planes van por `ic_pieza` (como los de Derechos humanos, Enfoque diferencial y Bienes), no
por `sr_pieza`/`plan_srpa.py`, que es el molde viejo de los siete primeros.

**Dónde.** E: no tiene espacio (6 GB libres), así que el árbol va en
`D:\DAE MASTER\PRIORIDAD 1\CURSO - SRPA Y JUSTICIA RESTAURATIVA\`, con un `LEER` en las carpetas
de E:. Los bins de Resolve son los del curso. El proyecto de AE es el de siempre
(`E:\…\00 MOTION GRAPHICS\SRPA_mg.aep`). Los másters de 32 Mb/s van a
`D:\DAE\_masters_archivo\PRIORIDAD 1\CURSO - SRPA Y JUSTICIA RESTAURATIVA\`.

**Unidad 4 (17 nov 2026).** Ese mismo día llegó `SRPA_unidad_4_inicio_v2.mp4`: la bienvenida y
la clase de la unidad 4 en un solo archivo, de Carlos Humberto Ramírez Romero. Son dos piezas,
como en la unidad 3: `plan_sr4b` (inicio) y `plan_sr4d` (desarrollo). Él no está tan cerca de
la cámara: la columna es de 560 (`columna(560)`).

Los tiempos de cada plan están en segundos de la fuente.
"""
import os
import sys

_AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_AQUI, '..', '..', '..', 'herramientas', 'cartones'))
sys.path.insert(0, os.path.join(_AQUI, '..'))
import balanceo as B  # noqa: E402
import srpa as S  # noqa: E402

CLIP0 = 409
FPS = 24000 / 1001
FQ = 30.0
ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16

RAIZ = 'D:/DAE MASTER/PRIORIDAD 1/CURSO - SRPA Y JUSTICIA RESTAURATIVA'
BIN_CURSO = [S.BIN_RAIZ]
MASTERS = 'D:/DAE/_masters_archivo/PRIORIDAD 1/CURSO - SRPA Y JUSTICIA RESTAURATIVA'
AE_DIR = S.RAIZ + '/00 MOTION GRAPHICS'
AEP = AE_DIR + '/SRPA_mg.aep'
ICONOS = AE_DIR + '/iconos'
CURSO_LINEAS = list(S.CURSO_LINEAS)
TITULO_BASE = None
MAXW = 470
ANCHO = MAXW
LT = (40, 440)
AUDIO_META = 'I=-16:TP=-3:LRA=7'
ESTANISLAO = S.ESTANISLAO
CARLOS = S.CARLOS


def columna(ancho):
    """Ancho de la columna de cartones y listas de un plan que no usa el de la base (470). El plan
    lo guarda en su `MAXW` (lo lee `ic_pieza.ajustes`) y acá queda para repartir los renglones:
    `MAXW = columna(560)`. Un plan por proceso: el ancho queda puesto para lo que se importe después."""
    global ANCHO
    ANCHO = ancho
    return ancho


def cuadro_de(tramos):
    """Segundos de la fuente → cuadro de la línea, descontando los cortes de `tramos`."""
    def cuadro(t):
        acum = 0.0
        for a, b, _w in tramos:
            if a - 1e-6 <= t <= b + 1e-6:
                return CLIP0 + int(round((acum + t - a) * FPS))
            acum += b - a
        raise ValueError('%.2f cae en un corte' % t)
    return cuadro


def armar(fuente, carpeta, unidad, linea, export, prefijo, tramos):
    """Constantes de un plan: `fuente` es el archivo de `01 VIDEO`, `carpeta` la de la pieza
    bajo RAIZ («UNIDAD 1/CIERRE») y `tramos` los de la fuente, en segundos, con su ventana."""
    r = RAIZ + '/' + carpeta
    return dict(
        R=r, BIN=BIN_CURSO + carpeta.split('/'),
        ORIGINAL=r + '/01 VIDEO/' + fuente, COMPUESTO=r + '/01 VIDEO/%s_compuesto_v1.mp4' % prefijo,
        TITULO=r + '/02 CARTONES/carton titulo %s.mp4' % prefijo.lower(),
        SUB='Unidad %d. %s' % (unidad, S.UNIDADES[unidad]), NOMBRE_LINEA=linea,
        EXPORT=export + '-v%d', PREFIJO=prefijo, TMP='D:/DAE/_tmp/sr_ta/' + prefijo.lower(),
        TRAMOS=tramos, T0=tramos[0][0], T1=tramos[-1][1], cuadro=cuadro_de(tramos),
        MASTER_DIR=MASTERS + '/' + carpeta.replace('/', ' - '))


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


def c_suelta(t):
    return _p(t, 'bold', SUELTA, 0)


def lista(titulo, *filas):
    return {'titulo': titulo, 'filas': list(filas)}
