# -*- coding: utf-8 -*-
r"""Base de los videos de profe a cámara de «Derechos humanos aplicados a la función judicial»
(16 nov 2026).

**Pedido.** Sebastián: «tenemos otro inicio de curso profe hablando a cámara, necesito que lo
proceses de pe a pa con todos los protocolos y requerimientos establecidos». El formato es el de
los profes de Enfoque diferencial y Bienes:
- intro FGN y cartón de título con el nombre del curso y el de la pieza;
- el profe a cámara, con cartones de caja y listas de AE a la izquierda y lower third;
- cartón de cierre y outro.

**Fuentes.** Drive del curso → VIDEOS (`16xDO2LgXTBunKGEeu8BQzzMZ6pY-kX6w`), de JP:
- `01. Video Presentación.mp4`: la toma cruda, 1620×1080, 30 fps parejos (7370 cuadros en
  245,667 s), H.264 Main a 16 Mb/s, BT.709, audio AAC estéreo;
- `DDHH_funcion_inio_curso/` es un paquete de Camtasia con la misma toma recortada y bajada a
  1280×720 Baseline. Se usa la cruda: tiene más calidad, y lo que JP quitó se corta con TRAMOS.
- Hay además los inicios y cierres de las unidades (U1 a U4), sin procesar todavía.

**Fondo.** Virtual: el edificio con el panel DAE/Fiscalía (x 37–739, y 76–233 de la fuente).
El profe está centrado y cerca: la cabeza va de x≈633 a 1021 y de y≈177 a la barba en y≈810.

**Ventana 1620×912 desde (0, 40), ×1,185.** Es todo el ancho de la fuente, la más abierta
posible: la cabeza queda desde x≈750 de salida, así que la columna de texto se angosta a 520
(`MAXW`). El panel entra entero y la barba queda en y≈912 de salida. Se probó con la caja dibujada
sobre 16 cuadros (`D:\DAE\_tmp\dh_profe\caja_A.jpg`): las manos, cuando gesticula, quedan bajo
la caja.

**Plano cerrado 1472×828 desde (0, 40), ×1,30**, para disimular los cortes de toma. Más cerrado
no se puede: el panel tiene que entrar entero y la barba no puede salirse por abajo.

**Dónde.** `E:\DAE MASTER\PRIORIDAD 2\CURSO - DERECHOS HUMANOS APLICADOS A LA FUNCION JUDICIAL\`,
una carpeta por pieza con las de la serie; los bins, iguales en `DAE MASTER - CURSOS`.
El proyecto de AE es `00 MOTION GRAPHICS\DH_profe_mg.aep` (copia de `ED_profe_mg.aep`).
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

CURSO = 'E:/DAE MASTER/PRIORIDAD 2/CURSO - DERECHOS HUMANOS APLICADOS A LA FUNCION JUDICIAL'
BIN_CURSO = ['PRIORIDAD 2', 'CURSO - DERECHOS HUMANOS APLICADOS A LA FUNCION JUDICIAL']
AE_DIR = CURSO + '/00 MOTION GRAPHICS'
AEP = AE_DIR + '/DH_profe_mg.aep'
ICONOS = AE_DIR + '/iconos'
CURSO_LINEAS = ['Derechos humanos aplicados', 'a la función judicial']
TITULO_BASE = None
XY, VENTANA = (0, 40), (1620, 912)
CERRADO = (0, 40, 1472, 828)
MATRIZ_FUENTE = 'bt709'
MAXW = 520
ANCHO = MAXW
# el cargo a 410 de ancho: «Coautor del curso Derechos / humanos aplicados a la / función judicial»
# (a 440 quedaba «judicial» solo en el tercer renglón). Simulado sobre cuatro cuadros del compuesto:
# termina en x≈620, sobre la plaza y el hombro del saco, lejos de la cara.
LT = (40, 410)
AUDIO_META = 'I=-16:TP=-3:LRA=7'


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
