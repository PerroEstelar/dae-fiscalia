# -*- coding: utf-8 -*-
r"""Base de los videos de profe de «Delitos informáticos» (Prioridad 3, 22 nov 2026). **Entrega provisional**: intro,
cartón de título, cartón de cierre y outro. Sin rótulo nuestro: el video ya trae los del profe.

**Pedido.** Sebastián (22 nov): «tenemos que procesar videos para el curso delitos informáticos, creo que solo están las
unidades 3 y 4; este profe metió su propia gracia: lo que debemos quitarle es inicio y cierre, donde intentó hacer un
cartón del caso inicial que no puede ir, reemplazarlos por el nuestro; sus lower thirds y gracia dentro del video
pueden ir; lo que no puede ir es ese logo que él le puso en la esquina superior derecha (…) intro, cartón de entrada,
cartón de salida y outro».

**Las fuentes.** `E:\DAE MASTER\CURSO DELITOS INFORMATICOS\`: cinco videos ya editados por el profe en DaVinci
(1280×720 a 25, H.264, BT.709 etiquetado, AAC estéreo), con su cartón de entrada (2 a 5 s, sobre fondo azul noche),
sus rótulos («Docente · Ing. Yefrin Garavito Navarro», los de sección), sus láminas a cuadro completo y, junto con los
rótulos de sección, una placa «DAE | FISCALÍA» arriba a la derecha. Dos terminan además con otro cartón suyo
(«¡Bienvenido a la Unidad 4!», «Cierre de la Unidad 4»). La grabación de la videollamada deja abajo a la izquierda el
nombre del participante («Yefrin Alexis Garavito Navarro», blanco sobre negro, y 704–720).

- `1. bienvenida unidad 3.mov` (5:57,6) → U3 inicio · `2. Intermedia unidad 3.mov` (5:24,1) → U3 intermedio.
- `4. Bienvenida Unidad 4.mov` (5:55,7; `… (1).mov` es el mismo archivo, md5 igual) → U4 inicio.
- `5. intermedio unidad 4.mov` (6:40,3) → U4 intermedio · `6. cierre unidad 4.mov` (5:51,5) → U4 cierre.
- No hay «3.»: falta el cierre de la U3. Tampoco hay U1, U2, inicio ni cierre del curso.

**Qué se hace.**
1. La placa de arriba a la derecha se tapa con el fondo virtual que hay detrás, sacado de la misma grabación
   (`limpia_logo_di.py`): la fuente del plan es `01 VIDEO/<PREFIJO>_fuente_limpia.mp4`.
2. Ventana 1248×702 desde (16, 0): deja fuera la franja del nombre de la videollamada (abajo) y pierde 16 px a cada
   lado; las láminas del profe tienen margen de sobra. Sube a 1080 (×1,54).
3. Entra desde el corte de su cartón (o medio segundo antes de la primera palabra, si habla más tarde) hasta 0,7 s
   después de la última palabra (o hasta su cartón final). Adentro no se corta nada.

**Nombres.** Del formato «Prioridad 3 - Presentacion Vaciado_Corrección_Curso Delitos Informáticos»: el curso es
«Delitos Informáticos» (1.1; en el cartón, «Delitos informáticos», en minúscula como el resto de nombres de curso de la
serie); «Unidad 3. Investigación y judicialización», «Unidad 4. Evidencia digital». Profe: Yefrin Garavito («1.5
Autor»; su rótulo dice «Ing. Yefrin Garavito Navarro»).

**Dónde.** `E:\DAE MASTER\PRIORIDAD 03\CURSO DELITOS INFORMATICOS - VIDEOS PROFE\UNIDAD n\<INICIO|INTERMEDIO|CIERRE>`.
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
FPS_COMPUESTO = '25'
MATRIZ_FUENTE = 'bt709'
ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16

FUENTES = 'E:/DAE MASTER/CURSO DELITOS INFORMATICOS/'
RAIZ = 'E:/DAE MASTER/PRIORIDAD 03/CURSO DELITOS INFORMATICOS - VIDEOS PROFE'
BIN_CURSO = ['PRIORIDAD 03', 'CURSO DELITOS INFORMATICOS - VIDEOS PROFE']
MASTERS = 'D:/DAE/_masters_archivo/PRIORIDAD 03/CURSO DELITOS INFORMATICOS - VIDEOS PROFE'
AE_DIR = RAIZ + '/00 MOTION GRAPHICS'
AEP = AE_DIR + '/DI_profe_mg.aep'          # no existe: la entrega provisional no lleva motion graphics
ICONOS = AE_DIR + '/iconos'
CURSO_LINEAS = ['Delitos informáticos']
NOMBRE_CURSO = 'Delitos informáticos'
TITULO_BASE = None
XY, VENTANA = (16, 0), (1248, 702)
ANCHO = 615
AUDIO_META = 'I=-16:TP=-3:LRA=7'
PRESET_ENTREGA = 'medium'
PRESET_COMPUESTO = 'veryfast'
UNIDADES = {
    3: 'Investigación y judicialización',
    4: 'Evidencia digital',
}
PROFE = None          # el video trae los rótulos del profe
SUAVE = 0


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
    """Constantes de un plan: `carpeta` la de la pieza bajo RAIZ («UNIDAD 3/INICIO»), `fuente` el nombre del archivo
    del profe en FUENTES (la ORIGINAL es su copia sin la placa) y `tramos` los de la fuente, en segundos."""
    r = RAIZ + '/' + carpeta
    tr = [(a, b, None) for a, b in tramos]
    k0 = max(0, int(tr[0][0] * FQ) - 30)
    return dict(CUADRO_0=k0,
        R=r, BIN=BIN_CURSO + [carpeta.replace('/', ' - ')],
        FUENTE_PROFE=FUENTES + fuente, ORIGINAL=r + '/01 VIDEO/%s_fuente_limpia.mp4' % prefijo,
        COMPUESTO=r + '/01 VIDEO/%s_compuesto_v1.mp4' % prefijo,
        TITULO=r + '/02 CARTONES/carton titulo %s.mp4' % prefijo.lower(), SUB=sub, NOMBRE_LINEA=linea,
        EXPORT=export + '-v%d', PREFIJO=prefijo, TMP='D:/DAE/_tmp/di_p/' + prefijo.lower(),
        TRAMOS=tr, T0=tr[0][0], T1=tr[-1][1], cuadro=cuadro_de(tr), MASTER_DIR=MASTERS + '/' + carpeta)


def armar_unidad(u, pieza, fuente, tramos):
    """Inicio, intermedio o cierre de una unidad: el cartón de título lleva el nombre de la unidad."""
    return armar('UNIDAD %d/%s' % (u, pieza), 'Unidad %d. %s' % (u, UNIDADES[u]), 'DI - U%d - %s' % (u, pieza),
                 'delitosinformaticos - U%d - %s' % (u, pieza), 'DIU%d%s' % (u, pieza[0] if pieza != 'INTERMEDIO'
                                                                              else 'M'), fuente, tramos)


def _p(texto, peso, px, gap):
    return B.piezas(texto, peso, px, gap, ANCHO)
