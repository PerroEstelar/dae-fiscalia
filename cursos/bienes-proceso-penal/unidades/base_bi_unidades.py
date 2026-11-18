# -*- coding: utf-8 -*-
r"""Base del inicio y el cierre de las unidades 1 a 4 de «Bienes en el proceso penal» (Curso 5,
17 nov 2026). **Entrega provisional.**

**Pedido.** Sebastián: «continúa con Bienes en el proceso penal, cada video que está en esta carpeta
debemos dejarlo procesado con el estilo provisional de gráfica; hay creo que 4 unidades, inicio y
cierre por cada unidad, más inicio y cierre del curso en general». El estilo provisional es intro,
cartón de título, lower third, cartón de cierre y outro, con el cuerpo sin gráficos (`ITEMS` lleva
solo el lower third). El inicio y el cierre del curso ya estaban entregados con gráficos desde el
14 nov (`introduccion_curso/plan_bi.py` y `cierre_curso/plan_bc.py`): no se rehacen.

**Fuentes.** Drive del curso → VIDEOS UNIDADES (`1s9P1jkAOz0CBJs_gfUdVWGdplWxfc2H_`, 17 nov), ocho
archivos «Bienes -  Unidad  n - Inicio|cierre.mp4». Son otra grabación que las del curso:
**1920×1080**, H.264 Constrained Baseline, 30 fps parejos, AAC estéreo a 44,1 kHz (−15,7 a −20,7
LUFS, picos hasta +0,3 dBTP), etiquetadas `smpte170m`.
- **Vienen con una intro y un outro ya pegados.** Los cuadros 0–277 (9,27 s) son una intro de la FGN
  sin sonido y los últimos 278 (9,27 s) un outro, los dos a corte. El profe empieza en el cuadro 278.
  El cierre de la unidad 4 no trae outro. Eso se saca: cada plan toma solo el tramo del profe y la
  línea le pone la intro, los cartones y el outro de siempre.
- **Color: BT.601.** El panel DAE/Fiscalía leído como 601 da rojo (207, 48, 60), azul (10, 85, 158) y
  amarillo (238, 201, 18), que es la firma correcta; no llevan `MATRIZ_FUENTE`.
- **Profe.** Sergio Andrés López Zamora, el mismo del inicio y el cierre del curso (se comparó un
  cuadro con el compuesto del inicio). Lee de corrido; no hay pausas de más de 2 s.
- **Recorte.** De medio segundo antes de la primera palabra (nunca antes del cuadro 280) a 0,8 s
  después de la última (nunca más allá del primer cuadro del outro). En varios el editor cortó muy
  cerca de la última palabra (en el cierre de la unidad 3 quedan 0,07 s).

**Ventana: el cuadro entero.** El profe está sentado lejos de la cámara, chico y abajo al centro, y
el panel DAE/Fiscalía arriba a la izquierda: no hay recorte que acerque al profe y deje el panel
entero. Para la versión con gráficos hay que decidir antes dónde va la columna de cartones.

**Lower third: columna angosta a la izquierda.** El profe ocupa el centro de abajo (de x≈500 a
x≈1400, con la cara hasta y≈1000 en el cierre de la unidad 1): con las medidas del cierre del curso
(44 px y 560 de ancho) el nombre le cruzaba la cara en el cierre de la unidad 1 y el hombro o las
manos en los demás. Se simuló sobre dos cuadros de cada una de las ocho fuentes
(`D:\DAE\_tmp\bi_u\sim_todos_*.jpg`). Va con el nombre en dos renglones, el cargo a 345 de ancho y
la cima en y=740 (`LT`, `LT_TOP`, y el salto de renglón en `PROFE`): termina en x≈480.

**Dónde.** E: no tiene espacio: el árbol va en `D:\DAE MASTER\CURSO 5 - Bienes en el proceso penal\
UNIDAD n\INICIO|CIERRE`, y los másters de 32 Mb/s en `D:\DAE\_masters_archivo\CURSO 5 - Bienes en el
proceso penal\UNIDAD n\…`. El proyecto de AE del curso sigue en E:.

**Nombres de las unidades.** Del formato de diseño del curso («07_09_2026 (pte) DISEÑO
CURSO_BIENES EN EL PROCESO PENAL», `1tBoTP13X60naUlM4prS9Bu8Ngk4on19Q`, «Ruta de aprendizaje»). La
unidad 4 figura ahí como «…extinción del derecho **del** dominio»; el profe dice, las dos veces,
«del derecho **de** dominio», que es además el término de la ley. Va «de dominio».

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

RAIZ = 'D:/DAE MASTER/CURSO 5 - Bienes en el proceso penal'
BIN_CURSO = ['C5 BIENES EN EL PROCESO PENAL']
MASTERS = 'D:/DAE/_masters_archivo/CURSO 5 - Bienes en el proceso penal'
AE_DIR = 'E:/DAE MASTER/CURSO 5 - Bienes en el proceso penal/00 MOTION GRAPHICS'
AEP = AE_DIR + '/BIENES_intros_mg.aep'
ICONOS = AE_DIR + '/iconos'
CURSO_LINEAS = ['Bienes en el proceso penal']
NOMBRE_CURSO = 'Bienes en el proceso penal'
TITULO_BASE = None
XY, VENTANA = (0, 0), (1920, 1080)
ANCHO = 615
LT = (44, 345)             # px del nombre y ancho del cargo
LT_TOP = 740               # cima del lower third (estándar 870): lleva siete renglones
AUDIO_META = 'I=-16:TP=-3:LRA=7'
# Entrega provisional. Los cuatro inicios salieron con x264 CRF 18 preset medium. Los cuatro cierres (20 a 26
# min cada uno) con 'nvenc': Sebastián los necesitaba antes de las 22:00 y con x264 no llegaban (ver
# mp4_entrega). La v2 con gráficos vuelve a la receta (quitar esta línea: slow).
PRESET_ENTREGA = 'nvenc'
PROFE = ('Sergio Andrés\nLópez Zamora',
         'Abogado, doctor en Derecho Público, magíster en Derecho Penal y Procesal Penal y en '
         'Derechos Humanos')
UNIDADES = {1: 'Función del bien', 2: 'Medidas cautelares con fines de reparación',
            3: 'Medidas cautelares con fines de comiso y administración de bienes',
            4: 'Medidas cautelares con fines de extinción del derecho de dominio'}


def armar_unidad(u, pieza, k0, k1):
    """Constantes del plan del inicio o el cierre de una unidad (`pieza` = 'INICIO' | 'CIERRE'); k0–k1
    son los cuadros de la fuente que entran (k1 exclusivo): el tramo del profe, sin la intro ni el
    outro que trae pegados."""
    carpeta = 'UNIDAD %d/%s' % (u, pieza)
    prefijo = 'BIU%d%s' % (u, pieza[0])
    r = RAIZ + '/' + carpeta
    t0, t1 = k0 / FQ, k1 / FQ

    def cuadro(t):
        if not t0 - 1e-6 <= t <= t1 + 1e-6:
            raise ValueError('%.2f cae fuera del tramo' % t)
        return CLIP0 + int(round((t - t0) * FPS))

    return dict(
        R=r, BIN=BIN_CURSO + [carpeta.replace('/', ' - ') + ' - PROFE'],
        ORIGINAL=r + '/01 VIDEO/bi_u%d_%s_fuente.mp4' % (u, pieza.lower()),
        COMPUESTO=r + '/01 VIDEO/%s_compuesto_v1.mp4' % prefijo,
        TITULO=r + '/02 CARTONES/carton titulo %s.mp4' % prefijo.lower(),
        SUB='Unidad %d. %s' % (u, UNIDADES[u]), NOMBRE_LINEA='BIENES - U%d - %s' % (u, pieza),
        EXPORT='bienes - U%d - %s' % (u, pieza) + '-v%d', PREFIJO=prefijo,
        TMP='D:/DAE/_tmp/bi_u/' + prefijo.lower(),
        TRAMOS=[(t0, t1, None)], T0=t0, T1=t1, cuadro=cuadro, MASTER_DIR=MASTERS + '/' + carpeta)


def _p(texto, peso, px, gap):
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
