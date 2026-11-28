# -*- coding: utf-8 -*-
r"""Base de los videos de profe de «Gerencia judicial» (Prioridad 2, 27 nov 2026). **Entrega provisional**: intro,
cartón de título, lower third, cartón de cierre y outro; el cuerpo va sin gráficos (`ITEMS` lleva solo el lower
third).

**Pedido.** Sebastián (27 nov): «llegaron nuevos videos de profe hablando a cámara… procésalos con gráfica
provisional pero de pe a pa, también hay que quitarle los fondos y poner los que usualmente usamos para este tipo
de videos… si debes editar y componer entre clips, ok». Carpeta `E:\DAE MASTER\PRIORIDAD 2\CURSO - GERENCIA
JUDICIAL\VIDEOS PROFE`, tres grabaciones del profe Jairo Ignacio Acosta Aristizábal (autor del curso, ficha «Prioridad
2 - Presentacion - Vaciado_Correcion_Curso GerenciaJudicial.docx»):
- `VIDEO 1 GERENCIA JUDICIAL TOMA1.mp4` (24:56): la bienvenida al curso, de una sola toma;
- `VIDEO 2 GERENCIA JUDICIAL TOMA1.mp4` (3:27): el inicio de la unidad 1, un arranque en falso («voy a volver a
  comenzar…») y la toma completa;
- `VIDEO 3 … unidades guienes de apertura y cierre.mp4` (22:53): otra toma del inicio de la U1 y el inicio y el
  cierre de las unidades 1 a 4, en orden, con pausas largas entre piezas. **No hay cierre del curso**.

**La fuente.** Cámara web, 1920×1080, H.264 a 30 c/s (29,9997 de promedio), sin etiquetas de color (se lee BT.709),
AAC estéreo 48 kHz. El profe, sentado, en plano de cabeza y hombros, delante de una biblioteca real.

**El profe se recorta y va sobre el fondo de la Fiscalía** (`FONDO 4 V2.png`, logos arriba a la izquierda), como en
Ley 1826: `herramientas/video/recorta_cuadro.py` (Robust Video Matting, resnet50, por la placa). Es un plano de
cámara web: con el cuadro al 90 % la cabeza quedaba grande y el hombro derecho se salía; **al 85 %, centro en
x=1220**, la cabeza queda del tamaño de los videos de Justicia restaurativa y el hombro entra entero. Achicarlo más
lo hunde en el cuadro (la fuente apoya abajo). Lo corre `lote/recorta_lote.py`. Las piezas de VIDEO 3 (y la del
inicio de la U1) se sacan antes a su `_fuente.mp4` (`lote/extraer.py`: 2 s antes de la primera palabra y 2,5 s
después de la última, 30 c/s parejos, CRF 12).

**Qué se editó** (`lote/cortes.py` mide cada corte; los planes cuentan cada uno):
- **Se cortan los rótulos leídos.** El profe lee en voz alta, a veces, el texto de pantalla de su guion
  («Las cuatro competencias específicas, cada una asociada al ícono de su unidad», «Cuatro círculos concéntricos»,
  «Son tres ítems: …», «Tres indicadores para mi tablero») y en seguida dice lo mismo con sus palabras. Sale el
  rótulo y queda lo dicho. Los que funcionan como transición hablada («Retroalimentación de la evaluación», «Enfoque
  pedagógico. ¿Cómo vamos a aprender?») se dejan.
- **Se cortan los arranques en falso** solo donde hay silencio a los dos lados del corte (la energía en el borde de
  cuadro elegido, 25 dB o más por debajo de la voz). Donde la palabra cortada va pegada («dese— deje», «incorproan—
  incorporando», «discrecio— de discrecionalidad») se deja: el corte se notaría más.
- **Cada corte cambia de plano** (entero ↔ cerrado, `CERRADO`) hasta la pausa siguiente, porque el profe se mueve
  mucho (diferencia de imagen 6 a 18 entre el último cuadro de antes y el primero de después, contra 0,1 a 1,5 entre
  cuadros seguidos). Los de diferencia chica (hasta 4,5) van con `SUAVE = 3`.
- **Inicio de la U1, compuesto entre tomas:** la toma completa de VIDEO 2 (la más limpia) con la frase de la
  evaluación de VIDEO 3, porque en VIDEO 2 dice «una evaluación calificada al cierre de cada unidad de los tres
  temas» y en VIDEO 3 «…al cierre de cada uno de los tres temas», que es lo que dice la ficha.
- **Entradas y salidas:** medio segundo antes de la primera palabra y 0,8 s después de la última.

**Nombre del curso y de las unidades**, de la ficha: «Gerencia judicial»; U1 Contexto estratégico y política criminal,
U2 Liderazgo y gestión del talento humano, U3 Gestión de servicios, planeación y seguimiento, U4 Articulación
interinstitucional y territorial.

**Lower third.** «Jairo Ignacio Acosta Aristizábal · Autor experto del curso. Jurista; fue juez de la República y
procurador delegado en lo penal»: la ficha lo nombra autor; el resto lo dice él en la bienvenida («Fui juez de la
República durante más de dos décadas y procurador delegado en lo penal durante 17 años»).

**Dónde.** `E:\DAE MASTER\PRIORIDAD 2\CURSO - GERENCIA JUDICIAL\VIDEOS PROFE\<CURSO|UNIDAD n>\<INICIO|CIERRE>`.
Entrega directa de Resolve por la placa NVIDIA (`lote/entrega_gpu.py`), unos 5 Mb/s, como Ley 1826.

Los tramos de cada plan van en cuadros de la fuente (30 c/s); los tiempos de `ITEMS`, en segundos de la fuente.
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

CURSO_DISCO = 'E:/DAE MASTER/PRIORIDAD 2/CURSO - GERENCIA JUDICIAL'
RAIZ = CURSO_DISCO + '/VIDEOS PROFE'
BIN_CURSO = ['PRIORIDAD 2', 'CURSO - GERENCIA JUDICIAL', 'VIDEOS PROFE']
MASTERS = 'D:/DAE/_masters_archivo/PRIORIDAD 2/CURSO - GERENCIA JUDICIAL/VIDEOS PROFE'
AE_DIR = RAIZ + '/00 MOTION GRAPHICS'
AEP = AE_DIR + '/GJ_profe_mg.aep'          # no existe: la entrega provisional no lleva motion graphics
ICONOS = AE_DIR + '/iconos'
NOMBRE_CURSO = 'Gerencia judicial'
CURSO_LINEAS = ['Gerencia judicial']
TITULO_BASE = None
XY, VENTANA = (0, 0), (1920, 1080)
CERRADO = (0, 0, 1728, 972)                # plano cerrado: deja entero el panel de logos (x 58–785, y 42–172)
ANCHO = 470
LT = (44, 520)                             # px del nombre y ancho del cargo
LT_TOP = 800                               # cima del lower third
AUDIO_META = 'I=-16:TP=-3:LRA=7'
MATRIZ_FUENTE = 'bt709'
PRESET_ENTREGA = 'medium'
PROFE = ('Jairo Ignacio\nAcosta Aristizábal',
         'Autor experto del curso. Jurista; fue juez de la República y procurador delegado en lo penal')
UNIDADES = {
    1: 'Contexto estratégico y política criminal',
    2: 'Liderazgo y gestión del talento humano',
    3: 'Gestión de servicios, planeación y seguimiento',
    4: 'Articulación interinstitucional y territorial'}
FONDO = RAIZ + '/00 FONDOS/FONDO 4 V2.png'
ESCALA = 0.85            # el cuadro de la fuente, al 85 %
CENTRO_X = 1220          # centro del cuadro achicado en el cuadro de 1920 (apoyado abajo)


def armar(nombre, carpeta, sub, linea, export, prefijo, tramos, cruda=None):
    """Constantes de un plan. `nombre`: el recortado es `01 VIDEO/<nombre>_recortado.mp4`; `carpeta`, la de la
    pieza bajo RAIZ; `tramos`, lo que entra, en cuadros de la fuente: [(k0, k1)] o [(k0, k1, ventana)], k1
    exclusivo. Entre dos tramos que no se tocan hay un corte."""
    r = RAIZ + '/' + carpeta
    tr = [(t[0] / FQ, t[1] / FQ, t[2] if len(t) > 2 else None) for t in tramos]

    def cuadro(t):
        """Segundos de la fuente → cuadro de la línea, descontando los cortes."""
        acum = 0.0
        for a, b, _w in tr:
            if a - 1e-6 <= t <= b + 1e-6:
                return CLIP0 + int(round((acum + t - a) * FPS))
            acum += b - a
        raise ValueError('%.2f cae fuera de los tramos' % t)

    return dict(
        R=r, BIN=BIN_CURSO + [carpeta.replace('/', ' - ')],
        ORIGINAL=r + '/01 VIDEO/' + nombre + '_recortado.mp4',
        FUENTE_CRUDA=r + '/01 VIDEO/' + (cruda or nombre + '_fuente.mp4'),
        COMPUESTO=r + '/01 VIDEO/%s_compuesto_v1.mp4' % prefijo,
        TITULO=r + '/02 CARTONES/carton titulo %s.mp4' % prefijo.lower(), SUB=sub, NOMBRE_LINEA=linea,
        EXPORT=export + '-v%d', PREFIJO=prefijo, TMP='D:/DAE/_tmp/gj_p/' + prefijo.lower(),
        TRAMOS=tr, T0=tr[0][0], T1=tr[-1][1], cuadro=cuadro, MASTER_DIR=MASTERS + '/' + carpeta)


def armar_curso(pieza, tramos):
    """Inicio del curso (la bienvenida, VIDEO 1)."""
    sub = 'Introducción al curso' if pieza == 'INICIO' else 'Cierre del curso'
    return armar('gj_curso_' + pieza.lower(), 'CURSO/' + pieza, sub, 'GJ - CURSO - ' + pieza,
                 'gerenciajudicial - CURSO - ' + pieza, 'GJC' + pieza[0], tramos,
                 cruda='VIDEO 1 GERENCIA JUDICIAL TOMA1.mp4')


def armar_unidad(u, pieza, tramos):
    """Inicio o cierre de una unidad: línea «GJ - Un - INICIO», entrega «gerenciajudicial - Un - INICIO» y el nombre
    de la unidad en el cartón de título."""
    return armar('gj_u%d%s' % (u, pieza[0].lower()), 'UNIDAD %d/%s' % (u, pieza),
                 'Unidad %d. %s' % (u, UNIDADES[u]), 'GJ - U%d - %s' % (u, pieza),
                 'gerenciajudicial - U%d - %s' % (u, pieza), 'GJU%d%s' % (u, pieza[0]), tramos)


def _p(texto, peso, px, gap):
    return B.piezas(texto, peso, px, gap, ANCHO)


def cita(t):
    return _p(t, 'bold', TIT, 0) if len(t) <= 78 else _p(t, 'med', CUE, 0)


def c_tit(titulo, cuerpo):
    return _p(titulo, 'bold', TIT, 0) + _p(cuerpo, 'med', CUE, GAP_TIT)


def lista(titulo, *filas):
    return {'titulo': titulo, 'filas': list(filas)}
