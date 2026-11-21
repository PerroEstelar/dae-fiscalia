# -*- coding: utf-8 -*-
r"""Base de los videos de profe de «Derecho de petición y acción de tutela: régimen constitucional, legal y
jurisprudencial para servidores públicos» (Prioridad 3, 20 nov 2026). **Entrega provisional**: intro, cartón de
título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (`ITEMS` lleva solo el lower third).

**Pedido.** Sebastián (20 nov): «continuar con todos los videos de profe hablando a cámara del curso derechos de
petición (…) en uno o dos videos se hicieron varias tomas que se supone deben componer» y «como nosotros le decimos
inicio, componerlos, revisar si necesitan edición (repetición, error, inicio, pausas o cierre), hacer el tratamiento
de gráfica provisional a todos, subir, actualizar, sacar srt, todo como los demás cursos».

**Las fuentes.** Siete grabaciones de videollamada en `E:\DAE MASTER\CURSO DERECHOS DE PETICION\` (1920×1080 a 30
fps, H.264 Constrained Baseline sin etiquetas de color, AAC estéreo 48 kHz), con el fondo virtual del campus y el
panel DAE/Fiscalía arriba a la izquierda. Cada plan lleva su `ORIGINAL`. Entre toma y toma el profe le habla al
técnico («Suspendamos ahí, por favor, Camilo»): eso, las tomas fallidas y la conversación del principio y del final
no entran. STT (Scribe, WAV 16 kHz) en `D:\DAE\_tmp\dp_p\stt\`.

- `VIDEO 1 PRESENTACION GENERAL DEL CURSO - TOMA1.mp4` (9:01,9) → inicio del curso.
- `VIDEO2 - PRESENTACION UNIDAD 1 - TOMA 1.mp4` (3:39,1) y `… TOMA 2.mp4` (8:28,8) → inicio de la U1. La toma 2 trae
  el guion entero en tres tramos; la toma 1 es un primer intento que se corta en la lección 2 («cortemos ahí»):
  no entra.
- `VIDEO2 - PRESENTACION UNIDAD 2- TOMA 1.mp4`, `VIDEO4 - … UNIDAD 3…`, `VIDEO5 - … UNIDAD 4…` → inicios de U2 a U4.
- `VIDEO6 - CIERRE UNIDAD 1- TOMA 1.mp4` (28:41) → cierre de la U1.

**Imagen.** Cuadro entero (no hay lienzo ni rayas: filas y columnas de las orillas como el resto del fondo). **Color**:
el rojo, el azul y el amarillo del panel leídos como BT.601 dan (220, 33, 74), (4, 90, 165) y (244, 211, 26), lo mismo
que la fuente de Desaparición forzada, que se midió contra un compuesto entregado: va como BT.601 (no lleva
`MATRIZ_FUENTE`).

**Nombres.** Del formato de diseño (FGN-AP01-F-204) y de «1.1 Nombre del curso» de los vaciados, que coinciden:
«Derecho de petición y acción de tutela: régimen constitucional, legal y jurisprudencial para servidores públicos».
La carpeta del curso en Drive dice además «y daño antijurídico»: no es fuente. Unidades: «3.1 Nombre de la unidad».

**Profe.** Óscar Jairo Fonseca Fonseca: lo dice él en el inicio del curso («Mi nombre es Óscar Jairo Fonseca
Fonseca») y es el «1.5 Autor» de los vaciados («Fonseca Fonseca Oscar Jairo»; el formato de diseño: «AUTOR EXPERTO:
Oscar Fonseca»). Cargo: «Autor del curso».

**Rótulo a la derecha.** El profe está al centro y sus manos entran a menudo en la esquina de abajo a la izquierda,
donde va el rótulo de la serie; la de abajo a la derecha queda libre (hoja de 48 cuadros de las seis fuentes con
las dos cajas dibujadas, `D:\DAE\_tmp\dp_p\prep\hoja_lt.jpg`). Va en x=1330, nombre en dos renglones.

**Dónde.** E: tiene 1,4 GB libres: el árbol va en `D:\DAE MASTER\PRIORIDAD 03\CURSO DERECHO DE PETICION - VIDEOS
PROFE\` y las fuentes se leen de E: (no se copian).
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

FUENTES = 'E:/DAE MASTER/CURSO DERECHOS DE PETICION/'
RAIZ = 'D:/DAE MASTER/PRIORIDAD 03/CURSO DERECHO DE PETICION - VIDEOS PROFE'
BIN_CURSO = ['PRIORIDAD 03', 'CURSO DERECHO DE PETICION - VIDEOS PROFE']
MASTERS = 'D:/DAE/_masters_archivo/PRIORIDAD 03/CURSO DERECHO DE PETICION - VIDEOS PROFE'
AE_DIR = RAIZ + '/00 MOTION GRAPHICS'
AEP = AE_DIR + '/DP_profe_mg.aep'          # no existe: la entrega provisional no lleva motion graphics
ICONOS = AE_DIR + '/iconos'
CURSO_LINEAS = ['Derecho de petición y acción de tutela:', 'régimen constitucional, legal y',
                'jurisprudencial para servidores públicos']
NOMBRE_CURSO = ('Derecho de petición y acción de tutela: régimen constitucional, legal y jurisprudencial para '
                'servidores públicos')
TITULO_BASE = None
XY, VENTANA = (0, 0), (1920, 1080)
ANCHO = 615
AUDIO_META = 'I=-16:TP=-3:LRA=7'
PRESET_ENTREGA = 'medium'
PRESET_COMPUESTO = 'veryfast'
UNIDADES = {
    1: 'Derecho de petición: fundamentos, modalidades y términos',
    2: 'Gestión y respuesta del derecho de petición',
    3: 'Acción de tutela: fundamentos y procedencia',
    4: 'Gestión, cumplimiento y seguimiento de la acción de tutela',
}
LT = (44, 440)
PROFE = ('Óscar Jairo\nFonseca Fonseca', 'Autor del curso', {'x': 1330})
# Seis cuadros de mezcla en los cortes de toma, como en Desaparición forzada
SUAVE = 6


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


def armar(carpeta, sub, linea, export, prefijo, fuente, tramos):
    """Constantes de un plan: `carpeta` la de la pieza bajo RAIZ («UNIDAD 1/INICIO»), `fuente` el nombre del archivo
    en FUENTES y `tramos` los de la fuente, en segundos: [(desde, hasta), …]."""
    r = RAIZ + '/' + carpeta
    tr = [(a, b, None) for a, b in tramos]
    k0 = max(0, int(tr[0][0] * FQ) - 30)
    return dict(CUADRO_0=k0,
        R=r, BIN=BIN_CURSO + [carpeta.replace('/', ' - ')],
        ORIGINAL=FUENTES + fuente, COMPUESTO=r + '/01 VIDEO/%s_compuesto_v1.mp4' % prefijo,
        TITULO=r + '/02 CARTONES/carton titulo %s.mp4' % prefijo.lower(), SUB=sub, NOMBRE_LINEA=linea,
        EXPORT=export + '-v%d', PREFIJO=prefijo, TMP='D:/DAE/_tmp/dp_p/' + prefijo.lower(),
        TRAMOS=tr, T0=tr[0][0], T1=tr[-1][1], cuadro=cuadro_de(tr), MASTER_DIR=MASTERS + '/' + carpeta)


def armar_unidad(u, pieza, fuente, tramos):
    """Inicio o cierre de una unidad: el cartón de título lleva el nombre de la unidad."""
    return armar('UNIDAD %d/%s' % (u, pieza), 'Unidad %d. %s' % (u, UNIDADES[u]), 'DP - U%d - %s' % (u, pieza),
                 'derechodepeticion - U%d - %s' % (u, pieza), 'DPU%d%s' % (u, pieza[0]), fuente, tramos)


def rotulo(t, dura=7.5):
    """El lower third del profe desde el segundo `t` de la fuente."""
    return [('lt01', 'lt', t, t + dura, PROFE)]


def _p(texto, peso, px, gap):
    return B.piezas(texto, peso, px, gap, ANCHO)
