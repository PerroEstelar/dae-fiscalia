# -*- coding: utf-8 -*-
r"""Base de los videos de profe del curso «Investigación y judicialización de los delitos de tráfico de
migrantes y trata de personas» (Prioridad 03, 17–18 nov 2026). **Entrega provisional.**

**Pedido.** Sebastián (17 nov, noche): «continuemos con este grupo de videos, gráfica provisional pero
completos, continúa hasta terminar y dejas todo actualizado». Carpeta de Drive: curso → VIDEOS
(`1Xslh4RCzyn52FeFF_I1OynZ3oqowWgmv`). Son once videos: bienvenida y cierre general del curso, y la
introducción, la retroalimentación de la evaluación y el cierre de las unidades 1, 2 y 3. El estilo
provisional es intro, cartón de título, lower third, cartón de cierre y outro, con el cuerpo sin
gráficos (`ITEMS` lleva solo el lower third).

**Tres clases de fuente.**
- **Avatar vertical** (bienvenida, cierre general, introducciones y retroalimentaciones): 1080×1920,
  H.264 a 25 fps parejos, BT.709, AAC estéreo a 48 kHz (−21 LUFS, picos de −4 a −5 dBTP). Es un avatar
  de José María Peláez Mejía («Soy José María Peláez Mejía, autor experto de este curso»), de traje en
  la bienvenida y el cierre general y de suéter en las unidades. Sin intro ni outro pegados.
- **La introducción de la unidad 1** es ese mismo formato vertical metido en un cuadro de 1920×1080
  con barras negras: la imagen ocupa las columnas 656–1263 (608 px). Se trata igual, con su recorte.
- **Los cierres de unidad** (.webm): grabación horizontal de 1280×720 con el fondo virtual de la DAE,
  H.264 en WebM con **cadencia variable** (pasos de 2 a 147 ms) y Opus mono (−20,8 LUFS, picos de +0,2
  dBTP). Los presenta una mujer que no dice su nombre.

**El avatar se recorta y va sobre el fondo de la DAE.** Sebastián (17 nov, 22:35): «el fondo debería
ser alguno de los fondos que hemos usado para los otros videos, con el logo de la DAE y Fiscalía… recortar
el personaje y usar el fondo… específicamente las que están los logos hacia la izquierda y que no tenga el
logo Aprende con la DAE… la idea es que sean iguales al resto de videos de profe hablando a cámara».
- **Fondo:** `00 FONDOS/FONDO 4 V2.png` (2048×1152), de su carpeta de Drive «FONDOS SIN APRENDE CON LA DAE»
  (`1VFuiOQiV12FpQ1oRKp90oz0Boef8QtwJ`). De los cuatro de esa carpeta es el único con los logos arriba a
  la izquierda (vista aérea del edificio); FONDO 1 y 2 son la fachada con los logos abajo a la derecha, y
  las dos fachadas con logos a la izquierda que hay en Drive traen «Aprende con la DAE».
- **Recorte:** `herramientas/video/recorta_persona.py` (Robust Video Matting, resnet50, por la placa con
  DirectML). De la fuente se toma un cuadrado (`RECORTE`: y, x, lado) que llega del pelo al pecho, a
  tamaño real, y la persona queda apoyada en el borde inferior, con el centro en x=1250: a la derecha del
  panel de logos, como los profes de las grabaciones de Teams. Sale `…_recortado.mp4` (1920×1080, 25 fps,
  BT.709), que es la `ORIGINAL` del plan, y `…_recortado_mate.mp4` (el alfa), para cambiar de fondo sin
  volver a recortar. La fuente cruda queda al lado (`FUENTE_CRUDA`).
- `y` se elige por video (la cima del pelo menos unos 90 px): cada avatar tiene su encuadre.
- Lo primero que se probó, y se descartó sin entregar nada, fue el recorte cuadrado sobre el mismo cuadro
  desenfocado.
- Cadencia: el compuesto va a 25 (`FPS_COMPUESTO`), sin duplicar cuadros; Resolve lo conforma a 23,976.

**Los cierres** van con la ventana estándar (1143×643 desde (0, 40)), cortados por tiempo (`POR_TIEMPO`)
porque la cadencia es variable, y el mono se arma en dual-mono (lo hace `ic_pieza.base_audio`).

**Cartón de título.** El nombre del curso, del formato de diseño («07_09_2026 DISEÑO CURSO INVESTIGACIÓN
Y JUDICIALIZACIÓN…», `12tdLKOxyRlRN-fB41cLc0dZq_p7NCeuu`), en tres renglones; debajo, la pieza:
«Introducción al curso», «Cierre del curso», «Unidad n. Introducción», «Unidad n. Retroalimentación de la
evaluación», «Unidad n. Cierre». Los nombres de las unidades tienen de 97 a 157 caracteres y no entran
con el nombre del curso en el mismo cartón; quedan en `UNIDADES`.

**Lower third.** «José María Peláez Mejía · Autor experto del curso. Magistrado de la Sala Penal del
Tribunal Superior del Distrito Judicial de Cúcuta» (el documento de diseño dice «Magistrado Titular del
Despacho 03 de la Sala Penal del Tribunal Superior del Distrito Judicial de Cúcuta»). El de los cierres
espera la confirmación de Sebastián (`PROFE_CIERRES`): un nombre de lower third no se infiere.

**Dónde.** `D:\DAE MASTER\PRIORIDAD 03\VIDEOS PROFE\<CURSO|UNIDAD n>\<pieza>` (E: no tiene espacio).
**Sin máster de 32 Mb/s**: en D: quedaban 22 GB. La entrega sale directo de Resolve por la placa NVIDIA
(`lote/entrega_gpu.py`), como los cierres de Bienes. El recorte de los avatares lo corre `lote/recorta_lote.py`.

Los tiempos de cada plan están en segundos de la fuente.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'herramientas',
                                'cartones'))
import balanceo as B  # noqa: E402

CLIP0 = 409
FPS = 24000 / 1001
ANTE, TIT, CUE, SUELTA = 29, 46, 37, 54
GAP_TIT, GAP_CUE, GAP_ANTE = 28, 12, 16

RAIZ = 'D:/DAE MASTER/PRIORIDAD 03/VIDEOS PROFE'
BIN_CURSO = ['PRIORIDAD 03', 'VIDEOS PROFE']
MASTERS = 'D:/DAE/_masters_archivo/PRIORIDAD 03/VIDEOS PROFE'
AE_DIR = RAIZ + '/00 MOTION GRAPHICS'
AEP = AE_DIR + '/TRATA_profe_mg.aep'
ICONOS = AE_DIR + '/iconos'
NOMBRE_CURSO = 'Investigación y judicialización de los delitos de tráfico de migrantes y trata de personas'
CURSO_LINEAS = ['Investigación y judicialización de', 'los delitos de tráfico de migrantes', 'y trata de personas']
TITULO_BASE = None
XY, VENTANA = (0, 0), (1920, 1080)
ANCHO = 470
LT = (44, 560)
AUDIO_META = 'I=-16:TP=-3:LRA=7'
MATRIZ_FUENTE = 'bt709'
PRESET_ENTREGA = 'medium'
PROFE = ('José María Peláez Mejía',
         'Autor experto del curso. Magistrado de la Sala Penal del Tribunal Superior del Distrito Judicial '
         'de Cúcuta')
PROFE_CIERRES = None       # la presentadora de los cierres de unidad: pendiente de que Sebastián la confirme
UNIDADES = {
    1: 'Delimitación dogmática y jurisprudencial de los delitos de trata de personas, tráfico de migrantes y '
       'explotación sexual',
    2: 'Enfoque diferencial, interseccional y de derechos en la investigación y judicialización de los delitos '
       'de trata de personas y tráfico de migrantes',
    3: 'Investigación y programa metodológico en la trata de personas y el tráfico de migrantes'}
PIEZAS = {'INICIO': 'Introducción', 'RETROALIMENTACION': 'Retroalimentación de la evaluación', 'CIERRE': 'Cierre'}
FONDO = RAIZ + '/00 FONDOS/FONDO 4 V2.png'
CENTRO_X = 1250          # centro de la persona recortada en el cuadro de 1920


def armar(fuente, carpeta, sub, linea, export, prefijo, t0, t1, recortado=False):
    """Constantes de un plan: `fuente` es el archivo de `01 VIDEO` (sin `_fuente` ni extensión), `carpeta`
    la de la pieza bajo RAIZ y t0–t1 los segundos de la fuente que entran. Con `recortado`, la `ORIGINAL`
    es el avatar ya recortado sobre el fondo (`…_recortado.mp4`) y la cruda queda en `FUENTE_CRUDA`."""
    r = RAIZ + '/' + carpeta
    nom, ext = os.path.splitext(fuente)
    cruda = r + '/01 VIDEO/' + nom + '_fuente' + ext
    original = r + '/01 VIDEO/' + nom + '_recortado.mp4' if recortado else cruda

    def cuadro(t):
        if not t0 - 1e-6 <= t <= t1 + 1e-6:
            raise ValueError('%.2f cae fuera del tramo' % t)
        return CLIP0 + int(round((t - t0) * FPS))

    return dict(
        R=r, BIN=BIN_CURSO + [carpeta.replace('/', ' - ')],
        ORIGINAL=original, FUENTE_CRUDA=cruda, COMPUESTO=r + '/01 VIDEO/%s_compuesto_v1.mp4' % prefijo,
        TITULO=r + '/02 CARTONES/carton titulo %s.mp4' % prefijo.lower(), SUB=sub, NOMBRE_LINEA=linea,
        EXPORT=export + '-v%d', PREFIJO=prefijo, TMP='D:/DAE/_tmp/tr_p/' + prefijo.lower(),
        TRAMOS=[(t0, t1, None)], T0=t0, T1=t1, cuadro=cuadro, MASTER_DIR=MASTERS + '/' + carpeta)


def armar_curso(pieza, ext, t0, t1, recortado=False):
    """Bienvenida ('INICIO') o cierre general ('CIERRE') del curso."""
    sub = 'Introducción al curso' if pieza == 'INICIO' else 'Cierre del curso'
    return armar('tr_curso_%s%s' % (pieza.lower(), ext), 'CURSO/' + pieza, sub, 'TRATA - CURSO - ' + pieza,
                 'traficoytrata - CURSO - ' + pieza, 'TRC' + pieza[0], t0, t1, recortado)


def armar_unidad(u, pieza, ext, t0, t1, recortado=False):
    """Introducción ('INICIO'), retroalimentación de la evaluación ('RETROALIMENTACION') o cierre ('CIERRE')
    de una unidad."""
    corto = {'INICIO': 'inicio', 'RETROALIMENTACION': 'retro', 'CIERRE': 'cierre'}[pieza]
    return armar('tr_u%d_%s%s' % (u, corto, ext), 'UNIDAD %d/%s' % (u, pieza),
                 'Unidad %d. %s' % (u, PIEZAS[pieza]), 'TRATA - U%d - %s' % (u, pieza),
                 'traficoytrata - U%d - %s' % (u, pieza), 'TRU%d%s' % (u, pieza[0]), t0, t1, recortado)


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
