# -*- coding: utf-8 -*-
r"""Base de los videos de profe de «Ley 1826 de 2017: procedimiento penal especial abreviado y acusador
privado» (Prioridad 1, 19 nov 2026). **Entrega provisional**: intro, cartón de título, lower third, cartón de
cierre y outro; el cuerpo va sin gráficos (`ITEMS` lleva solo el lower third).

**Pedido.** Sebastián (19 nov): «necesitaríamos en esos videos editar si hay repeticiones o errores, cortes,
silencios, entradas, salidas, cambiar el fondo virtual por el de la Fiscalía y además hacer todo nuestro
procedimiento habitual de pe a pa con gráfica provisional… revisa todo el material, organízalo y recuerda que
suelen haber inicio y cierre general del curso y lo mismo pero por unidades». Carpeta de Drive «VIDEOS CURSO PPA»
(`1glwsHbdJS1ltwziPilxhj4od6Ky4o-Cf`): diez grabaciones, el juego completo (inicio y cierre del curso, inicio y
cierre de las unidades 1 a 4) y un archivo repetido («entrada unidad 1», `1g3bOsK7IMwHPa6-ut_vQdZdOIsuJpWli`,
los mismos 159.482.226 bytes que `1V6EKTtRNWik_5O9wD7FA7w_cBUw77-Ok`).

**La fuente.** Un solo profe, de frente, leyendo, con un fondo virtual de biblioteca: 1920×1080, H.264 High a 30
fps parejos (video y audio arrancan en 0), sin etiquetas de color (se lee BT.709), AAC **mono** a 48 kHz, −21 a
−23 LUFS con picos en 0 dBFS y silencio digital entre frases (−80 a −92 dB). Sin intro ni outro pegados. El
profe se mueve: se acerca y se aleja de la cámara dentro de un mismo video.

**El profe se recorta y va sobre el fondo de la Fiscalía**, como los avatares de Trata:
`herramientas/video/recorta_cuadro.py` (Robust Video Matting, resnet50, por la placa) toma el cuadro entero de
la fuente, lo achica al 90 % y lo apoya en el borde de abajo con el centro en x=1250, sobre `00 FONDOS/FONDO 4
V2.png` (los logos DAE y Fiscalía arriba a la izquierda, sin «Aprende con la DAE»). Sebastián vio dos cuadros de
muestra (tamaño original y 10 % más chico) y eligió «B: 10 % más chico». Sale `…_recortado.mp4` (la `ORIGINAL`
del plan) y `…_recortado_mate.mp4` (el alfa, para cambiar de fondo sin volver a recortar); la cruda queda al
lado (`FUENTE_CRUDA`). Lo corre `lote/recorta_lote.py`, dos a la vez (4,4 c/s cada uno en la GTX 970).

**La pluma de los bordes.** Con el cuadro al 90 %, el borde izquierdo de la fuente cae en x=386 y el de arriba en
y=108, dentro del cuadro: una mano que entra por la izquierda o la cabeza cuando el profe se acerca quedaban
cortadas por una línea recta. `recorta_cuadro.py` multiplica el alfa por una rampa de 96 px a la izquierda y 48
arriba (`--pluma-x`, `--pluma-y`). Los cuatro primeros recortes salieron antes de que existiera y se emplumaron
después con `lote/emplumar.py`, sin volver a pasar el modelo; el inicio de la U1 ya estaba entregado y salió en v2.

**Qué se editó.** Se leyeron las diez transcripciones enteras (Scribe, 7.559 palabras): no hay tomas repetidas
ni pedidos de corte. Lo que hay son cuatro palabras en falso, que se cortan, y titubeos chicos que se dejan:
- se cortan «las vara— las variaciones» y «y ava— avanzar» (inicio de la U2), «imp— inimputabilidad» (cierre de
  la U3) y «y consid— y… considerar» (inicio de la U4). Los puntos de corte se eligieron en los valles de la
  energía (ventanas de 25 ms cada 10 ms, por bandas) y caen en cuadro entero de la fuente;
- los tres primeros mueven poco la imagen (diferencia entre el último cuadro de antes y el primero de después:
  1,7 a 3,1, contra 0,5 a 0,9 entre cuadros seguidos): van con `SUAVE = 3` (`ic_pieza.tramos_vf`): tres cuadros
  de mezcla con el último cuadro de antes. El cuarto mueve mucho (9 a 12: el profe cambia de postura en el
  segundo y medio que se saca): va seco y con plano cerrado (`CERRADO`) hasta el final de la frase;
- se dejan «contribuirán a, a una justicia» (inicio del curso), «recíproco de la, de la defensa» (cierre del
  curso) y un «eh» (inicio de la U4): la palabra repetida va pegada a la anterior o a la siguiente, sin un
  valle donde cortar, y el corte se notaría más que el titubeo;
- las pausas de más de 2 s son cuatro, de 2,1 a 2,8 s, todas entre un bloque y el siguiente: se dejan;
- **entradas y salidas:** cada video entra medio segundo antes de la primera palabra (antes hay de 3,6 a 11,8 s
  de espera) y sale 0,8 s después de la última, medidas en el audio (primeros 30 ms seguidos sobre −38 dB y
  último tramo sobre −38 dB). Se miraron los cuadros de cada borde: el profe ya está de frente y quieto al
  entrar, y sigue mirando a cámara al salir.

**Nombre del curso y de las unidades.** De la ficha (`1ZPHQzXCHRswPlOSYeb8yY1sYOt2GFrQH`): «Ley 1826 de 2017:
procedimiento penal especial abreviado y acusador privado»; el profe los dice igual en los videos.

**Lower third.** «Jorge Eduardo Castillo Pantoja · Autor experto del curso. Magíster en Ciencias Penales y
Forenses y docente universitario». La ficha dice «Castillo Pantoja Jorge Eduardo (autor experto)»; el resto lo
dice él en el inicio del curso («Mi nombre es Jorge Eduardo Castillo Pantoja, autor experto de este programa,
abogado magíster en Ciencias Penales y Forenses por la Universidad Autónoma de Colombia, diploma de estudios
avanzados de Derecho Penal por la Universidad Complutense de Madrid, España, y docente universitario»). El
nombre va en dos renglones y el cargo en una columna de 520 px, con la cima en y=800: el profe ocupa el centro
y la derecha, y un nombre de 30 letras en un renglón le llegaba al hombro.

**Dónde.** `E:\DAE MASTER\PRIORIDAD 1\CURSO - LEY 1826 PROCEDIMIENTO PENAL ABREVIADO\VIDEOS PROFE\<CURSO|UNIDAD
n>\<INICIO|CIERRE>`. **Sin máster de 32 Mb/s**: la entrega sale directo de Resolve por la placa NVIDIA
(`lote/entrega_gpu.py`), unos 5 Mb/s, como las de Trata y Justicia restaurativa.

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

CURSO_DISCO = 'E:/DAE MASTER/PRIORIDAD 1/CURSO - LEY 1826 PROCEDIMIENTO PENAL ABREVIADO'
RAIZ = CURSO_DISCO + '/VIDEOS PROFE'
BIN_CURSO = ['PRIORIDAD 1', 'CURSO - LEY 1826 PROCEDIMIENTO PENAL ABREVIADO', 'VIDEOS PROFE']
MASTERS = 'D:/DAE/_masters_archivo/PRIORIDAD 1/CURSO - LEY 1826 PROCEDIMIENTO PENAL ABREVIADO/VIDEOS PROFE'
AE_DIR = RAIZ + '/00 MOTION GRAPHICS'
AEP = AE_DIR + '/LP_profe_mg.aep'          # no existe todavía: la entrega provisional no lleva motion graphics
ICONOS = AE_DIR + '/iconos'
NOMBRE_CURSO = 'Ley 1826 de 2017: procedimiento penal especial abreviado y acusador privado'
CURSO_LINEAS = ['Ley 1826 de 2017: procedimiento penal', 'especial abreviado y acusador privado']
TITULO_BASE = None
XY, VENTANA = (0, 0), (1920, 1080)
CERRADO = (0, 0, 1728, 972)                # plano cerrado: deja entero el panel de logos (x 58–785, y 42–172)
ANCHO = 470
LT = (44, 520)                             # px del nombre y ancho del cargo (estándar 48 y 900)
LT_TOP = 800                               # cima del lower third (estándar 870): lleva cinco renglones
AUDIO_META = 'I=-16:TP=-3:LRA=7'
MATRIZ_FUENTE = 'bt709'
PRESET_ENTREGA = 'medium'
PROFE = ('Jorge Eduardo\nCastillo Pantoja',
         'Autor experto del curso. Magíster en Ciencias Penales y Forenses y docente universitario')
UNIDADES = {
    1: 'Finalidad, ámbito de aplicación y procedencia',
    2: 'Procedimiento: investigación, traslado, audiencia concentrada y juicio',
    3: 'Acusador privado, conversión y reversión',
    4: 'Terminación anticipada y mecanismos restaurativos'}
FONDO = RAIZ + '/00 FONDOS/FONDO 4 V2.png'
ESCALA = 0.9             # el cuadro de la fuente, al 90 %
CENTRO_X = 1250          # centro del cuadro achicado en el cuadro de 1920 (apoyado abajo)


def armar(nombre, carpeta, sub, linea, export, prefijo, tramos):
    """Constantes de un plan. `nombre` es el archivo de `01 VIDEO` sin `_fuente.mp4`; `carpeta`, la de la pieza
    bajo RAIZ; `tramos`, lo que entra, en cuadros de la fuente: [(k0, k1)] o [(k0, k1, ventana)], k1 exclusivo.
    Entre dos tramos que no se tocan hay un corte."""
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
        ORIGINAL=r + '/01 VIDEO/' + nombre + '_recortado.mp4', FUENTE_CRUDA=r + '/01 VIDEO/' + nombre + '_fuente.mp4',
        COMPUESTO=r + '/01 VIDEO/%s_compuesto_v1.mp4' % prefijo,
        TITULO=r + '/02 CARTONES/carton titulo %s.mp4' % prefijo.lower(), SUB=sub, NOMBRE_LINEA=linea,
        EXPORT=export + '-v%d', PREFIJO=prefijo, TMP='D:/DAE/_tmp/lp_p/' + prefijo.lower(),
        TRAMOS=tr, T0=tr[0][0], T1=tr[-1][1], cuadro=cuadro, MASTER_DIR=MASTERS + '/' + carpeta)


def armar_curso(pieza, tramos):
    """Inicio ('INICIO') o cierre ('CIERRE') del curso."""
    sub = 'Introducción al curso' if pieza == 'INICIO' else 'Cierre del curso'
    return armar('lp_curso_' + pieza.lower(), 'CURSO/' + pieza, sub, 'LEY1826 - CURSO - ' + pieza,
                 'ley1826 - CURSO - ' + pieza, 'LPC' + pieza[0], tramos)


def armar_unidad(u, pieza, tramos):
    """Inicio o cierre de una unidad: línea «LEY1826 - Un - INICIO», entrega «ley1826 - Un - INICIO» y el nombre
    de la unidad en el cartón de título."""
    return armar('lp_u%d_%s' % (u, pieza.lower()), 'UNIDAD %d/%s' % (u, pieza),
                 'Unidad %d. %s' % (u, UNIDADES[u]), 'LEY1826 - U%d - %s' % (u, pieza),
                 'ley1826 - U%d - %s' % (u, pieza), 'LPU%d%s' % (u, pieza[0]), tramos)


def _p(texto, peso, px, gap):
    return B.piezas(texto, peso, px, gap, ANCHO)


def cita(t):
    return _p(t, 'bold', TIT, 0) if len(t) <= 78 else _p(t, 'med', CUE, 0)


def c_tit(titulo, cuerpo):
    return _p(titulo, 'bold', TIT, 0) + _p(cuerpo, 'med', CUE, GAP_TIT)


def lista(titulo, *filas):
    return {'titulo': titulo, 'filas': list(filas)}
