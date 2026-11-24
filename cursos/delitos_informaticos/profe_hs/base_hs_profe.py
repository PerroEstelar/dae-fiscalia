# -*- coding: utf-8 -*-
r"""Base de los videos de profe de «Delitos informáticos» grabados por **Humberto Suárez Gómez** (Prioridad 3, 24 nov
2026). **Entrega provisional**: intro, cartón de título, rótulo, cartón de cierre y outro; el cuerpo va sin gráficos.

**Pedido.** Sebastián (24 nov): «we just got delitos informáticos, estilo de gráfica provisional, profe hablando a
cámara (…) procesa todo este batch, lo mismo que ya sabemos hacer; me recomendaron que mejorara los niveles y
ecualización de estos videos». Carpeta de Drive del pedido: `1r5rcMiIs8Pw6RbO438B2BYAqXchAXFst`.

**Por qué hay otra vez U3 y U4.** La ficha del curso («Vaciado_Corrección…», una por unidad) pide, por unidad, un
video de introducción (3.x.1, «Video unidad N») y uno de cierre («Video de cierre de la unidad»), más la presentación
(2.1) y el cierre del curso: son justo estas diez grabaciones. Lo del 22 nov eran cinco videos que **Yefrin
Garavito** editó por su cuenta (bienvenida, intermedio y cierre de U3 y U4; los «intermedios» no están en la ficha).
Sebastián (24 nov): **dejar ambos**; estos van en carpeta aparte y con otro nombre.

**Las fuentes.** Diez exports ProRes 422 HQ (1280×720, 10000/333 ≈ 30,03 cuadros/s, 10 bits, BT.709) con audio PCM
float mono de 48 kHz, en `E:\DAE MASTER\CURSO DELITOS INFORMATICOS\GRABACIONES 24 NOV\` (copiadas de la carpeta del
pedido por copia de servidor a «Mi unidad» y G:). El profe al centro, sobre el fondo del campus con el panel
DAE/Fiscalía arriba a la izquierda (es parte del fondo: queda). Ya vienen editadas; dos tienen algo que sale (ver los
planes de U2 inicio y U4 cierre).

**Rótulo.** El profe no dice su nombre en ninguna. Sebastián lo confirmó (24 nov): «Humberto Suárez Gómez»; es
coautor en la ficha («1.5 Autor: … Suárez Gómez Humberto …»). Cargo: «Coautor del curso». Abajo a la izquierda (en el
cierre del curso hace gestos con la mano derecha, del lado derecho del cuadro).

**Audio (lo nuevo).** Vienen muy bajas (−38 a −42 LUFS), con el piso de ruido a unos 20 dB de la voz y un espectro
cargado de graves y medios graves (125–630 Hz, +5 a +9 dB sobre la voz de referencia) y apagado arriba de 2,5 kHz
(−5 a −16 dB). Cada plan lleva su `AUDIO_CADENA`, medida en 2 min de su grabación con
`herramientas/audio/voz_analisis.py` (`voz_hs.json`): ecualización por curva hacia la referencia, reducción de
ruido suave, expansor, compresor de picos, de-esser y limitador; después, como siempre, loudnorm en dos pasadas.

**Dónde.** `E:\DAE MASTER\PRIORIDAD 03\CURSO DELITOS INFORMATICOS - VIDEOS PROFE HS\<CURSO|UNIDAD n>\<INICIO|CIERRE>`.
"""
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', '..', '..', 'herramientas', 'cartones'))
import balanceo as B  # noqa: E402

CLIP0 = 409
FPS = 24000 / 1001
FPS_FUENTE = 10000 / 333
FQ = FPS_FUENTE
FPS_COMPUESTO = '10000/333'
MATRIZ_FUENTE = 'bt709'
ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16

FUENTES = 'E:/DAE MASTER/CURSO DELITOS INFORMATICOS/GRABACIONES 24 NOV/'
RAIZ = 'E:/DAE MASTER/PRIORIDAD 03/CURSO DELITOS INFORMATICOS - VIDEOS PROFE HS'
BIN_CURSO = ['PRIORIDAD 03', 'CURSO DELITOS INFORMATICOS - VIDEOS PROFE HS']
MASTERS = 'D:/DAE/_masters_archivo/PRIORIDAD 03/CURSO DELITOS INFORMATICOS - VIDEOS PROFE HS'
AE_DIR = RAIZ + '/00 MOTION GRAPHICS'
AEP = AE_DIR + '/DI_HS_profe_mg.aep'      # no existe: la entrega provisional no lleva motion graphics
ICONOS = AE_DIR + '/iconos'
CURSO_LINEAS = ['Delitos informáticos']
NOMBRE_CURSO = 'Delitos informáticos'
TITULO_BASE = None
XY, VENTANA = (0, 0), (1280, 720)
ANCHO = 615
AUDIO_META = 'I=-16:TP=-3:LRA=7'
PRESET_ENTREGA = 'medium'
PRESET_COMPUESTO = 'veryfast'
UNIDADES = {
    1: 'Fundamentos conceptuales y contexto de la cibercriminalidad',
    2: 'Marco jurídico',
    3: 'Investigación y judicialización',
    4: 'Evidencia digital',
}
LT = (44, 440)
PROFE = ('Humberto\nSuárez Gómez', 'Coautor del curso', {})
SUAVE = 6
VOZ = json.load(open(os.path.join(AQUI, 'voz_hs.json'), encoding='utf-8'))


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


def armar(clave, carpeta, sub, linea, export, prefijo, fuente, tramos):
    """Constantes de un plan: `clave` la de `voz_hs.json`, `carpeta` la de la pieza bajo RAIZ («UNIDAD 1/INICIO»),
    `fuente` el nombre del archivo en FUENTES y `tramos` los de la fuente, en segundos: [(desde, hasta), …]."""
    r = RAIZ + '/' + carpeta
    tr = [(a, b, None) for a, b in tramos]
    k0 = max(0, int(tr[0][0] * FQ) - 30)
    assert VOZ[clave]['fuente'] == fuente, (clave, fuente)
    return dict(CUADRO_0=k0,
        R=r, BIN=BIN_CURSO + [carpeta.replace('/', ' - ')],
        ORIGINAL=FUENTES + fuente, COMPUESTO=r + '/01 VIDEO/%s_compuesto_v1.mp4' % prefijo,
        TITULO=r + '/02 CARTONES/carton titulo %s.mp4' % prefijo.lower(), SUB=sub, NOMBRE_LINEA=linea,
        EXPORT=export + '-v%d', PREFIJO=prefijo, TMP='D:/DAE/_tmp/di2/' + prefijo.lower(),
        TRAMOS=tr, T0=tr[0][0], T1=tr[-1][1], cuadro=cuadro_de(tr), MASTER_DIR=MASTERS + '/' + carpeta,
        AUDIO_CADENA=VOZ[clave]['cadena'])


def armar_unidad(clave, u, pieza, fuente, tramos):
    """Inicio o cierre de una unidad: el cartón de título lleva el nombre de la unidad."""
    return armar(clave, 'UNIDAD %d/%s' % (u, pieza), 'Unidad %d. %s' % (u, UNIDADES[u]),
                 'DI HS - U%d - %s' % (u, pieza), 'delitosinformaticos - U%d - %s - SUAREZ' % (u, pieza),
                 'DXU%d%s' % (u, pieza[0]), fuente, tramos)


def armar_curso(clave, pieza, sub, fuente, tramos):
    return armar(clave, 'CURSO/%s' % pieza, sub, 'DI HS - CURSO - %s' % pieza,
                 'delitosinformaticos - CURSO - %s - SUAREZ' % pieza, 'DXC%s' % pieza[0], fuente, tramos)


def rotulo(t, dura=7.5):
    """El lower third del profe desde el segundo `t` de la fuente."""
    return [('lt01', 'lt', t, t + dura, PROFE)]


def _p(texto, peso, px, gap):
    return B.piezas(texto, peso, px, gap, ANCHO)
