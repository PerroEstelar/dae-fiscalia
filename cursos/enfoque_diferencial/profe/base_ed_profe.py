# -*- coding: utf-8 -*-
r"""Base común de los 12 videos de profe de Enfoque diferencial (15 nov 2026).

**Pedido.** Sebastián: «ahora necesitamos hacer lo mismo para todos los videos en esta
carpeta, profe hablando a cámara de pe a pa». La carpeta es «Videos enfoques
diferenciales», de caborrerog@unal.edu.co, en Drive (`1dTALmfoD-P3cyiIoO39tg-0-3rTOy7mJ`).
- presentación general;
- presentaciones de las unidades 1 a 5;
- contenidos de las unidades 1 a 5;
- conclusiones.

**Profe.** Camilo Borrero García: «Soy profesor titular de la Universidad Nacional de
Colombia en su programa de Derecho. Llevo cuarenta años en la institución». Es la
primera vez que sale en la serie.

**Fuente.** Grabaciones de teléfono:
- HEVC, 30 fps, Rec.709;
- codificadas a 1080×1920 con rotación, así que se ven en 1920×1080;
- fondo virtual del edificio con el panel DAE/Fiscalía (x 190–890, y 78–235);
- audio AAC mono a 48 kHz.

El profe está al centro y cerca de la cámara, y casi no se mueve.

**Ventana 1440×810 desde (0, 40), ×1,33.**
- El panel entra entero.
- La cabeza queda desde x≈810 de salida (p2 de `perfil3`), así que la columna de texto
  es de 560.
- El nombre del lower third va a 40 px y el cargo a 440 de ancho: el pelo largo baja
  por la izquierda hasta los hombros.
- Se probó sobre 8 cuadros de cada uno de los 12 videos (`caja_ed.py`).

**Dónde.** E: no tiene espacio (8 GB libres para 2 h 12 min de video), así que el árbol
va en `D:\DAE MASTER\PRIORIDAD 2\CURSO - ENFOQUE DIFERENCIAL\VIDEOS PROFE\`, con un
`LEER` en el mismo sitio de E:.
- Las fuentes se leen de la copia en `G:\My Drive\_MA subidas\_ED profes`.
- El máster de cada entrega es de paso (decisión de Sebastián, 15 nov): se usa para la
  entrega MP4, se verifica y va a la papelera de Windows.

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

RAIZ = 'D:/DAE MASTER/PRIORIDAD 2/CURSO - ENFOQUE DIFERENCIAL/VIDEOS PROFE'
FUENTES = 'G:/My Drive/_MA subidas/_ED profes/'
AE_DIR = 'E:/DAE MASTER/PRIORIDAD 2/CURSO - ENFOQUE DIFERENCIAL/00 MOTION GRAPHICS'
AEP = AE_DIR + '/ED_profe_mg.aep'
ICONOS = AE_DIR + '/iconos'
CURSO_LINEAS = ['Enfoque diferencial en', 'la práctica del fiscal']
TITULO_BASE = None
XY, VENTANA = (0, 40), (1440, 810)
MATRIZ_FUENTE = 'bt709'
# 30 fps declarados con algún cuadro de 35 ms (29,98 de media): se corta por tiempo, no por número
# de cuadro (`ic_pieza._trim`). El audio es mono y `componer` lo arma en dual-mono.
POR_TIEMPO = True
MAXW = 560
ANCHO = MAXW
LT = (40, 440)
AUDIO_META = 'I=-16:TP=-3:LRA=7'
PROFE = ('Camilo Borrero García', 'Profesor titular de Derecho de la Universidad Nacional de Colombia')


def armar(clave, carpeta, sub, linea, export, prefijo, k0, k1):
    """Constantes de un plan: `clave` es el nombre de la fuente (ed_u1_contenido), `carpeta`
    la ruta bajo RAIZ, y k0–k1 los cuadros de la fuente que entran (k1 exclusivo)."""
    r = RAIZ + '/' + carpeta
    t0, t1 = k0 / FQ, k1 / FQ

    def cuadro(t):
        if not t0 - 1e-6 <= t <= t1 + 1e-6:
            raise ValueError('%.2f cae fuera del tramo' % t)
        return CLIP0 + int(round((t - t0) * FPS))

    return dict(
        R=r, BIN=['PRIORIDAD 2', 'CURSO - ENFOQUE DIFERENCIAL', 'VIDEOS PROFE'] + carpeta.split('/'),
        ORIGINAL=FUENTES + clave + '.mov', COMPUESTO=r + '/01 VIDEO/%s_compuesto_v1.mp4' % prefijo,
        TITULO=r + '/02 CARTONES/carton titulo %s.mp4' % clave, SUB=sub, NOMBRE_LINEA=linea,
        EXPORT=export + '-v%d', PREFIJO=prefijo, TMP='D:/DAE/_tmp/ed_profes/' + clave,
        TRAMOS=[(t0, t1, None)], T0=t0, T1=t1, cuadro=cuadro,
        MASTER_DIR='D:/DAE/_tmp/ed_profes/master')


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


def act(icono, ante, titulo, cuerpo=None):
    return {'icono': icono, 'ante': ante, 'titulo': titulo, 'cuerpo': cuerpo}
