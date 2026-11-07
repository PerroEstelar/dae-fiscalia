# -*- coding: utf-8 -*-
r"""Los videos del curso Delitos contra el medio ambiente (PRIORIDAD 3): es
`da_pieza` -la receta de Estándares interamericanos- apuntada al arbol de
`rutas_da`. Claves: V01 .. V06.

    python da_pieza.py V01 elegir construir blancos musica
    python da_pieza.py V01 montar            (dentro de Resolve: venv del MCP)
    python da_pieza.py V01 revisar           (render interno, NO es entrega)
    python da_pieza.py V01 exportar entregas verificar   (solo con el OK)

La geometria no cambia:

    intro 182 · entrada 119 · ranuras · respiro 48 · cierre 119 · outro 182

LO QUE CAMBIA RESPECTO DE EI (7 nov)
    1. EL COLOR DEL ENTORNO. EI apagaba el verde x0,08 y todo plano sin
       gente ni acento x0,15: aqui el bosque ES el tema. La direccion de arte
       del curso (base_da.C_PALETA) es un verde gris apagado, el agua minada
       ocre-gris y un solo saturado, la mostaza mate de la maquinaria y el
       oro. `limpia` ACOTA en vez de apagar:
           verde (tono PIL 58-112)      s <= VERDE_S
           frio de verdad (113-250)     x0,08, como siempre
           amarillo-ocre (28-57) sin acento   s <= OCRE_S
           calida (0-27): los topes de piel de siempre
       Y el grade no neutraliza: `graduar_da` aplica UNA curva de luma igual a
       los tres canales (grade_placas estira canal por canal y
       `suave.neutralizar_entorno` lleva el entorno a gris: las dos cosas se
       comian el verde que la limpieza dejo).
    2. LOS REGISTROS NUEVOS de la luz: 'aire' se gradua como 'dia' y
       'contra_ext' como 'contraluz'.
    3. V5 MOTION GRAPHICS: los graficos de datos (09 MOTION GRAPHICS,
       DA_<V>_mg.json, los rinde `mg_da.py`) van en V5, encima de los
       cartones. Sin rotulos (V8) ni detalles por ahora.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time

H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', 'prompts', 'cartones', 'musica', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import rutas_da as R                                    # noqa: E402
from guion_da import TEMAS, ANTE, ENTREGA, VIDEOS      # noqa: E402

FPS = '24000/1001'
FPS_N = 24000 / 1001.0
T0 = 86400
N_INTRO, N_BLANCO, N_RESPIRO, N_MARCA = 182, 119, 48, 168
CABEZA = N_INTRO + N_BLANCO
COMUNES = r'E:\DAE MASTER\00 COMUNES'
INTRO = os.path.join(COMUNES, 'INTRO', 'FGN_intro_version7.mp4')
MARCA = os.path.join(COMUNES, 'MARCA DE AGUA', 'MARCA_DE_AGUA_DAE_7s_fade.mov')
MARCA_PNG = os.path.join(COMUNES, 'MARCA DE AGUA', 'APRENDE_CON_LA_DAE_alfa.png')
PISTA_MUSICA_FUENTE = r'D:\DAE\_tmp\musica\TA03.mp3'
# 30 oct: los casos y la fabula con la cama de Gerencia judicial (TA03, ya
# aprobada); la conversacion con Juana, que son tres videos seguidos de la
# misma escena, con una sola cama propia (TA05) para que se oigan como uno.
# Derechos humanos: se escoge con el montaje (ver README del curso).
# 31 oct: como en Justicia restaurativa. U1 (llega la noticia) y U5 (la
# decision y el giro) con la cama de la serie (TA03, PISTA_MUSICA_FUENTE);
# U2-U4 (el analisis, la entrevista, la audiencia) con TA05, mas quieta.
# Ley 1826 (3 nov): los estudios reversos de la U2 con la cama de la serie
# (TA03); los casos de analisis de la U4, cortos y de analisis, con TA05.
# Enfoque diferencial (3 nov): la cama de la serie (TA03) en los dos casos
# que terminan en una correccion (C1 Molano, C3 Wilmer); TA05, mas quieta, en
# los tres que terminan sin respuesta (C2 impune, C4 punto muerto, C5 no
# volvio).
# Estándares interamericanos (5 nov): las cinco situaciones terminan en una
# pregunta abierta (qué hacer, qué fuente, qué actuaciones): TA05, la cama
# quieta de los casos que no se resuelven en pantalla, en las cinco.
# Delitos ambientales (7 nov): el V01 es la introduccion del curso y termina
# abriendo el recorrido («Ese es el recorrido que propone este curso»): la
# cama de la serie (TA03), como los casos que terminan en una salida.
CAMA_MUSICA = {k: PISTA_MUSICA_FUENTE for k in VIDEOS}
TMP = r'D:\DAE\_tmp\da'
RENDER = os.path.join(TMP, 'render')
ELEGIDAS = os.path.join(H, 'prompts', 'elegidas_da.json')

PISTAS_V = ((1, 'VIDEO'), (2, 'MOVIMIENTO'), (3, 'DETALLE'), (4, 'CARTONES'),
            (5, 'MOTION GRAPHICS'), (6, 'MARCA DE AGUA'), (7, 'EFECTOS'),
            (8, 'LOWER THIRD'))
PISTAS_A = ((1, 'NARRADOR'), (2, 'PREGUNTAS'), (3, 'DIALOGO'),
            (4, 'AMBIENTE'), (5, 'MUSICA'))
PISTA_MUSICA, PISTA_AMBIENTE = 5, 4


def w(*a):
    print(*a, flush=True)


def E(L):
    return __import__('escenas_da_%s' % L.lower())


def nombre(L, n):
    return 'DA_%s_r%02d_%s' % (L, n, E(L).NOMBRE[n])


def nombre_extra(L, k):
    """31 oct: una placa de EXTRA (no es una ranura entera): DH_C2_r04b_..."""
    return 'DA_%s_r%s_%s' % (L, k, E(L).EXTRA[k][0])


def con_acento_extra(L, k):
    e = E(L).EXTRA[k]
    return bool(e[3] is not None or 'mustard' in e[6].lower()), bool(e[2])


def pieza(L):
    return json.load(open(os.path.join(R.voces(L), 'DA_%s_ranuras.json' % L),
                          encoding='utf-8'))['pieza']


VERSION = 1


def nombre_linea(L):
    """La v1 se llama como siempre; desde la v2 la linea lleva la version en
    el nombre, para que en el bin se distingan sin abrirlas."""
    base = 'DA ' + ENTREGA[L].replace('PRIO 3 - DELITOS AMBIENTALES - ', '')
    return base if VERSION <= 1 else '%s v%d' % (base, VERSION)


def cuadros(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
                        '-count_frames', '-show_entries', 'stream=nb_read_frames',
                        '-of', 'default=nw=1:nk=1', p], capture_output=True,
                       text=True).stdout.split()
    return int(r[0]) if r else -1


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


def aparta(p, motivo):
    """Nada se borra: lo que se reemplaza va a _descartes con el motivo."""
    if not os.path.exists(p):
        return
    d = os.path.join(os.path.dirname(p), '_descartes')
    os.makedirs(d, exist_ok=True)
    b, e = os.path.splitext(os.path.basename(p))
    dest = os.path.join(d, '%s__%s%s' % (b, motivo, e))
    k = 2
    while os.path.exists(dest):
        dest = os.path.join(d, '%s__%s_%d%s' % (b, motivo, k, e))
        k += 1
    shutil.move(p, dest)


# ---------------------------------------------------------------- color
def _peso_banda(h, a, b, rampa=8.0):
    """1 dentro de [a, b], 0 fuera, con rampa lineal."""
    import numpy as np
    x = np.minimum(h - (a - rampa), (b + rampa) - h) / rampa
    return np.clip(x, 0.0, 1.0)


# 4 nov, Sebastian (revision del C3): «none of the characters from la Policia
# Nacional look like Colombian patrulleros». Los patrulleros de servicio llevan
# el uniforme de la Policia Nacional: verde oliva oscuro y el chaleco
# reflectivo verde-amarillo. En las ranuras de `escenas.CHALECO` la limpieza
# NO apaga ese verde ni ese verde-amarillo (con la regla de siempre los dos
# quedaban grises y el uniforme no se leia); los ACOTA: chaleco (tono PIL
# 34-62) a s <= 0,55 y verde del uniforme (62-95) a s <= 0,30. El frio de
# verdad (azul, cian, magenta: 96-255) sigue x0,08. El chaleco no es acento:
# no se gira a la mostaza de la serie.
CHALECO_S = (0.55, 0.30)


def chaleco(L, n):
    return n in getattr(E(L), 'CHALECO', set())


def topes_chaleco(hsv):
    import numpy as np
    h, s = hsv[..., 0], hsv[..., 1]
    wv = _peso_banda(h, 34, 62, rampa=4.0)
    s = s - wv * np.clip(s - CHALECO_S[0] * 255, 0, None)
    wg = _peso_banda(h, 63, 95, rampa=4.0)
    s = s - wg * np.clip(s - CHALECO_S[1] * 255, 0, None)
    hsv[..., 1] = s
    return hsv


# 7 nov: los topes del entorno de Delitos ambientales (ver el encabezado).
# Se fijan midiendo las placas elegidas del V01 (`medir_color` antes y despues).
VERDE = (58, 112)
VERDE_S = 0.20
OCRE_S = 0.26


def limpia_rgb(rgb, acento, gente=True):
    """La limpieza de bandas de DA sobre un array RGB uint8 (la usan `limpia`
    y, cuadro a cuadro, `mov_da`: Kling sube la saturacion)."""
    import numpy as np
    from PIL import Image, ImageFilter
    hsv = np.asarray(Image.fromarray(rgb).convert('HSV')).astype(np.float32)
    h, s = hsv[..., 0], hsv[..., 1]
    k = np.ones_like(s)
    frio = _peso_banda(h, VERDE[1] + 1, 262)
    k = np.minimum(k, 1 - frio * (1 - 0.08))
    # el peso se difumina antes de aplicarse: dos vecinos nunca distintos
    km = Image.fromarray(np.clip(k * 255, 0, 255).astype(np.uint8), 'L')
    km = km.filter(ImageFilter.GaussianBlur(6))
    k = np.asarray(km).astype(np.float32) / 255.0
    s = s * k
    # verde: tope, no apagado (el bosque gris verdoso de la direccion de arte)
    wv = _peso_banda(h, VERDE[0], VERDE[1], rampa=4.0)
    s = s - wv * np.clip(s - VERDE_S * 255, 0, None)
    # amarillo-ocre sin acento: el agua minada queda ocre-gris, nunca mostaza
    if not acento:
        wo = _peso_banda(h, 28, VERDE[0] - 1, rampa=4.0)
        s = s - wo * np.clip(s - OCRE_S * 255, 0, None)
    hsv[..., 1] = s
    hsv = topes_piel(hsv, acento)
    return np.asarray(Image.fromarray(np.clip(hsv, 0, 255).astype(np.uint8), 'HSV')
                      .convert('RGB'))


def limpia(src, dst, acento, gente, con_chaleco=False):
    import numpy as np
    from PIL import Image
    rgb = np.asarray(Image.open(src).convert('RGB'))
    Image.fromarray(limpia_rgb(rgb, acento, gente)).save(dst)
    return medir_color(dst)


def topes_piel(hsv, acento):
    """29 oct, Justicia restaurativa: las manos de T1 r03/r04 salieron ROSADAS
    despues del grade (la regla: piel gris calido, s <= 0,20, nunca rosada).
    Son los topes de `detalle_sit.topes`, que en las situaciones solo se
    pasaban a los insertos, aplicados aqui a toda placa:
      - rosado/rojo (tono PIL <= 12, rampa hasta 16): tope 0,20 SIEMPRE -la
        mostaza vive arriba de 20 grados y no se toca-;
      - sin acento: toda la banda calida (0-27) a tope 0,22."""
    import numpy as np
    h, s = hsv[..., 0], hsv[..., 1]
    wr = np.clip((16.0 - h) / 4.0, 0, 1)
    s = s - wr * np.clip(s - 0.20 * 255, 0, None)
    if not acento:
        wc = _peso_banda(h, 0, 27, rampa=4.0)
        s = s - wc * np.clip(s - 0.22 * 255, 0, None)
    hsv[..., 1] = s
    return hsv


def medir_color(p):
    import numpy as np
    from PIL import Image
    a = np.asarray(Image.open(p).convert('HSV')).reshape(-1, 3).astype(np.float32)
    h, s, v = a[:, 0], a[:, 1] / 255.0, a[:, 2]
    lit = v > 40
    def banda(lo, hi):
        # un gris puro tiene tono 0: sin el piso de saturacion cae en la calida
        m = lit & (s > 0.04) & (h >= lo) & (h <= hi)
        return float(np.percentile(s[m], 90)) if m.sum() > 500 else 0.0
    rosa = lit & (s > 0.20) & (h <= 12)
    return {'rosado_pct': round(float(rosa.mean()) * 100, 2),
            'calida_p90': round(banda(0, 27), 3),
            'amarilla_p90': round(banda(28, 55), 3),
            'verde_p90': round(banda(58, 112), 3),
            'fria_p90': round(max(banda(110, 255), 0), 3),
            'sat_media': round(float(s[lit].mean()) if lit.any() else 0, 3)}


# EL ACENTO DEL CURSO, IGUAL EN LOS TRES TEMAS (29 oct). Medido en las placas
# graduadas: el sueter del T3 tiene el tono de la serie (41-47 grados, como
# DF: 45), saturacion mediana ~0,5. El cardigan de la servidora y la manta de
# la joven del T4 salieron 10 grados mas NARANJA (31-34) y hasta 0,78 de
# saturacion: en el corte entre temas se lee como otra prenda y deja de ser
# «mostaza mate». Se gira el tono +7 unidades PIL (~10 grados) y se baja la
# saturacion del acento x0,9, solo en la banda del acento (tono PIL 14-45,
# s > 0,20 con rampa: la piel, s <= 0,20, no se toca). Va despues del grade
# en `construir`, cuadro a cuadro en `mov_da` y en los detalles.
ACENTO = {}
# 29 oct, noche: r06 y r07 del T4 se rehicieron (la servidora tiene que actuar
# como persona ciega: Sebastian). Sus placas nuevas no traen el naranja de la
# primera tirada, asi que el giro fijo las pasaria de largo. Para ellas el
# giro se MIDE: tono objetivo 42 grados (el sueter del T3) y saturacion
# mediana <= 0,55. `construir` lo calcula sobre la placa graduada y lo guarda;
# `mov_da` y `detalle_ei` leen el mismo valor para su ranura.
ACENTO_AUTO = set()
OBJETIVO_ACENTO = (42.0, 0.55)
ACENTO_J = os.path.join(TMP, 'acento_por_ranura.json')


def parametros_acento(L, n=None):
    if n is not None and (L, n) in ACENTO_AUTO and os.path.exists(ACENTO_J):
        v = json.load(open(ACENTO_J, encoding='utf-8')).get('%s_%02d' % (L, n))
        if v:
            return tuple(v)
    return ACENTO.get(L)


def mide_parametros_acento(L, n, p):
    m = medir_acento(p)
    if not m:
        return ACENTO.get(L)
    delta = max(-12.0, min(12.0, (OBJETIVO_ACENTO[0] - m[1]) * 255.0 / 360.0))
    k = min(1.0, OBJETIVO_ACENTO[1] / m[2])
    d = json.load(open(ACENTO_J, encoding='utf-8')) if os.path.exists(ACENTO_J) else {}
    d['%s_%02d' % (L, n)] = [round(delta, 2), round(k, 3)]
    json.dump(d, open(ACENTO_J, 'w', encoding='utf-8'), indent=1)
    return delta, k


def acento_serie(rgb, L, acento, girar=True, saturar=True, n=None, par=None):
    """rgb uint8 (H, W, 3) -> rgb con el acento del T4 llevado al de la serie."""
    import numpy as np
    from PIL import Image
    par = par or parametros_acento(L, n)
    if not par or not acento:
        return rgb
    delta, k = par
    hsv = np.asarray(Image.fromarray(rgb).convert('HSV')).astype(np.float32)
    h, s = hsv[..., 0], hsv[..., 1] / 255.0
    wgt = _peso_banda(h, 14, 45, rampa=4.0) * np.clip((s - 0.20) / 0.10, 0, 1)
    if girar:
        hsv[..., 0] = h + wgt * delta
    if saturar:
        hsv[..., 1] = hsv[..., 1] * (1 - wgt * (1 - k))
    return np.asarray(Image.fromarray(np.clip(hsv, 0, 255).astype(np.uint8), 'HSV')
                      .convert('RGB'))


# 31 oct (revision propia de la U5): el cielo del atardecer quedaba salmon
# -rosado claro en la ventana del despacho, s ~0,20 con la limpieza-; la regla
# es un entorno casi gris. Primer intento (v > 140, s <= 0,10): medido en la
# hoja, el cielo seguia leyendose rosado (s 0,10 con tono 7-20 grados en lo
# muy claro se ve rosa). Ahora: en lo CLARO (v > 150, rampa de 40) la banda
# calida y rosada (tono PIL <= 27 con rampa, y el lado magenta >= 245) baja
# a s <= 0,05 y su tono va a 20 PIL (28 grados, gris calido, no rosa). Es la
# misma regla de la piel (gris calido, nunca rosado): las luces de las caras
# quedan igual o mas grises. Va en la placa graduada (`construir`), cuadro a
# cuadro en Kling (`mov_da`) y en los detalles.
CIELO = {}


def cielo(rgb, L):
    """rgb (array uint8 HxWx3) -> array con el cielo calido apagado (solo
    las unidades de CIELO; las demas pasan igual)."""
    if L not in CIELO:
        return rgb
    import numpy as np
    from PIL import Image
    c = CIELO[L]
    hsv = np.asarray(Image.fromarray(rgb).convert('HSV')).astype(np.float32)
    h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    hh = np.where(h >= 245, h - 256.0, h)
    tibio = np.clip((31.0 - hh) / 4.0, 0, 1) * (hh >= -11)
    claro = np.clip((v - c['v']) / c['rampa'], 0, 1)
    w = tibio * claro
    hsv[..., 1] = s - w * np.clip(s - c['tope'] * 255, 0, None)
    hsv[..., 0] = np.mod(hh + w * (c['tono'] - hh), 256.0)
    return np.asarray(Image.fromarray(np.clip(hsv, 0, 255).astype(np.uint8), 'HSV')
                      .convert('RGB'))


def piso_negro(g, etiqueta, piso=16, codo=40):
    """31 oct, Sebastian (r28 del C2): «los negros son negro puro y eso casi
    nunca pasa en nuestros videos». La curva de la serie ancla p2 en 16-23,
    pero una placa con zonas de negro 0 (r05 nuevo del C2: 5 % del cuadro
    bajo 8) sale con p2 = 0. Si el p2 de la placa graduada queda bajo 10, se
    le sube el pie: v' = piso + v * (1 - piso/codo) para v < codo, identidad
    arriba. Monotona y continua; no toca los medios."""
    import numpy as np
    from PIL import Image
    im = Image.open(g).convert('RGB')
    a = np.asarray(im).astype(np.float32)
    lum = 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]
    p2 = float(np.percentile(lum, 2))
    if p2 >= 10:
        return None
    b = np.where(a < codo, piso + a * (1.0 - piso / float(codo)), a)
    Image.fromarray(np.clip(b, 0, 255).astype(np.uint8)).save(g)
    lum2 = 0.2126 * b[..., 0] + 0.7152 * b[..., 1] + 0.0722 * b[..., 2]
    w('%s pie del negro: p2 %.0f -> %.0f' % (etiqueta, p2, np.percentile(lum2, 2)))
    return p2


# 4 nov, Sebastian (revision del C3): «there are clips graded with too much hard
# black tones, everything's supposed to be more greyish». Medido sobre su
# linea: las placas de noche de la terminal (r02, r08-r11) tenian p50 18-31 y
# 53-70 % del cuadro bajo 30. Dos cosas, por tema (`escenas.GRIS`):
#   - las de noche van SIN_TECHO (el registro les sube el medio tono);
#   - a TODA placa del tema se le levanta la sombra con una curva suave:
#       v' = v + piso * (1 - v/codo)^2   para v < codo; identidad arriba.
#     Con (30, 130): 0 -> 30, 20 -> 42, 45 -> 58, 90 -> 93. Monotona (pendiente
#     minima 1 - 2*piso/codo = 0,54 en el negro), continua y derivable en el
#     codo: no hay quiebre. Los blancos y los medios altos no se tocan.
# La misma curva va en ffmpeg (`gris_vf`) para los clips de V2/V3 que no se
# rehacen, para que el corte entre placa y clip no salte.
def gris_lut(piso, codo):
    import numpy as np
    v = np.arange(256, dtype=np.float32)
    o = np.where(v < codo, v + piso * (1.0 - v / float(codo)) ** 2, v)
    return np.clip(np.round(o), 0, 255).astype(np.uint8)


def gris(g, L, etiqueta):
    par = getattr(E(L), 'GRIS', None)
    if not par:
        return None
    import numpy as np
    from PIL import Image
    a = np.asarray(Image.open(g).convert('RGB'))
    b = gris_lut(*par)[a]
    Image.fromarray(b).save(g)

    def lum(x):
        x = x.astype(np.float32)
        return 0.2126 * x[..., 0] + 0.7152 * x[..., 1] + 0.0722 * x[..., 2]
    la, lb = lum(a), lum(b)
    w('%s gris: p2 %.0f -> %.0f  p50 %.0f -> %.0f  bajo 30 %.1f%% -> %.1f%%'
      % (etiqueta, np.percentile(la, 2), np.percentile(lb, 2), np.percentile(la, 50),
         np.percentile(lb, 50), (la < 30).mean() * 100, (lb < 30).mean() * 100))
    return par


def gris_vf(L):
    """El filtro de ffmpeg con la misma curva (lutrgb), o None."""
    par = getattr(E(L), 'GRIS', None)
    if not par:
        return None
    piso, codo = par
    ex = 'if(lt(val\\,%d)\\,val+%g*pow(1-val/%d\\,2)\\,val)' % (codo, piso, codo)
    return 'lutrgb=r=%s:g=%s:b=%s' % (ex, ex, ex)


def reinyectar_acento(o, g, etiqueta, banda=(14, 45), piso_s=0.25, perdida=0.5):
    """31 oct (r12 del C2): el sueter de Camilo ocupa el 39 % del cuadro y la
    neutralizacion del entorno de `graduar_serie` lo tomo por dominante de
    color: la placa graduada quedo con el 2,5 % de pixeles saturados y el
    sueter salmon-gris. Donde la placa limpia (antes del grade) tiene el
    acento (tono en la banda mostaza, saturacion >= piso_s) y la graduada lo
    perdio (saturacion a menos de la mitad), se devuelven tono y saturacion
    de la limpia y se deja el valor de la graduada."""
    import numpy as np
    from PIL import Image
    a = np.asarray(Image.open(o).convert('RGB').resize(Image.open(g).size, Image.LANCZOS)
                   .convert('HSV')).astype(np.float32)
    b = np.asarray(Image.open(g).convert('HSV')).astype(np.float32)
    ha, sa = a[..., 0], a[..., 1] / 255.0
    sb = b[..., 1] / 255.0
    m = (sa >= piso_s) & (ha >= banda[0]) & (ha <= banda[1]) & (sb < perdida * sa)
    if m.mean() < 0.01:
        return None
    b[..., 0][m] = ha[m]
    b[..., 1][m] = np.minimum(255.0, sa[m] * 0.9 * 255.0)
    Image.fromarray(np.clip(b, 0, 255).astype(np.uint8), 'HSV').convert('RGB').save(g)
    w('%s acento devuelto al %.1f%% del cuadro que el grade desaturo' % (etiqueta, m.mean() * 100))
    return float(m.mean())


def nivelar_acento(L, g, etiqueta, tol=8.0):
    """31 oct: si el acento de una placa graduada se va del tono de la serie
    (42 grados) mas de `tol` grados, o se pasa de saturacion, se gira EN SITIO
    con el giro medido (r04 y 04b del C2 salieron a 54-57 grados: amarillo
    limon en vez de mostaza, al lado de las placas de dia a 37-41)."""
    import numpy as np
    from PIL import Image
    m = medir_acento(g)
    if not m:
        return None
    if abs(m[1] - OBJETIVO_ACENTO[0]) <= tol and m[2] <= OBJETIVO_ACENTO[1] + 0.07:
        return None
    delta = max(-12.0, min(12.0, (OBJETIVO_ACENTO[0] - m[1]) * 255.0 / 360.0))
    k = min(1.0, OBJETIVO_ACENTO[1] / m[2])
    rgb = acento_serie(np.asarray(Image.open(g).convert('RGB')), L, True, par=(delta, k))
    Image.fromarray(rgb).save(g)
    w('%s acento %s -> %s (giro %+.1f, k %.2f)' % (etiqueta, m, medir_acento(g), delta, k))
    return delta, k


def medir_acento(p):
    """(% del cuadro, tono en grados, saturacion mediana) del acento, o None."""
    import numpy as np
    from PIL import Image
    a = np.asarray(Image.open(p).convert('HSV')).reshape(-1, 3).astype(np.float32)
    h, s = a[:, 0], a[:, 1] / 255.0
    m = (h >= 12) & (h <= 45) & (s > 0.30)
    if m.mean() < 0.003:
        return None
    return (round(float(m.mean()) * 100, 2), round(float(np.median(h[m])) * 360 / 255, 1),
            round(float(np.median(s[m])), 2))


def con_acento(L, n):
    """DA: R[n][3] es la descripcion del acento (str) o None."""
    r = E(L).R[n]
    acento = r[3] is not None or 'mustard' in r[6].lower()
    return bool(acento), bool(r[2])


# ---------------------------------------------------------------- pasos
def elegir(L):
    el = json.load(open(ELEGIDAS, encoding='utf-8'))[L]
    pl = R.sub(L, '01 PLANOS')
    cand = os.path.join(pl, '_candidatas')
    hecho_p = os.path.join(pl, '_elegidas_aplicadas.json')
    hecho = json.load(open(hecho_p, encoding='utf-8')) if os.path.exists(hecho_p) else {}
    reusa = getattr(E(L), 'REUSA', {})
    for n in sorted(E(L).R):
        nm = nombre(L, n)
        # 30 oct, Justicia restaurativa: una ranura puede REUSAR la placa de
        # otra (escena, no placa: biblia §4). Se copia la candidata elegida
        # de la madre con el nombre de la hija y se hornea con otra camara.
        m = reusa[n][0] if n in reusa else n
        prest = getattr(E(L), 'PRESTADA', {}).get(n)
        if prest:
            # 7 nov: la placa es de otro video del curso (V02 r22 = V01 r03, la
            # draga que sigue trabajando): la candidata elegida de alla, limpia
            # con el acento y la gente de esta ranura
            L2, m2 = prest
            v = json.load(open(ELEGIDAS, encoding='utf-8'))[L2][str(m2)]
            src = os.path.join(R.sub(L2, '01 PLANOS'), '_candidatas',
                               '%s_%s.png' % (nombre(L2, m2), v))
            v = '%s_r%02d%s' % (L2, m2, v)
        elif str(m) not in el:
            # 31 oct, DH: se aplica lo que ya esta elegido aunque la pieza no
            # este completa (las placas graduadas sirven de referencia)
            w('r%02d sin elegir' % n)
            continue
        else:
            v = el[str(m)]
            src = os.path.join(cand, '%s_%s.png' % (nombre(L, m), v))
        dst = os.path.join(pl, nm + '.png')
        assert os.path.exists(src), src
        firma = '%s:%s' % (v, md5(src)[:10])
        if hecho.get(nm) == firma and os.path.exists(dst):
            w('r%02d %s ya aplicada' % (n, v))
            continue
        if os.path.exists(dst):
            aparta(dst, 'reemplazada_por_candidata_%s' % v)
        ac, ge = con_acento(L, n)
        antes = medir_color(src)
        despues = limpia(src, dst, ac, ge, chaleco(L, n))
        hecho[nm] = firma
        w('r%02d %s  acento %-5s gente %-5s  fria %.3f->%.3f  verde %.3f->%.3f  amarilla %.3f->%.3f'
          '  calida %.3f->%.3f  rosado %.2f%%->%.2f%%'
          % (n, v, ac, ge, antes['fria_p90'], despues['fria_p90'],
             antes['verde_p90'], despues['verde_p90'],
             antes['amarilla_p90'], despues['amarilla_p90'],
             antes['calida_p90'], despues['calida_p90'],
             antes['rosado_pct'], despues['rosado_pct']))
    # 31 oct: las placas EXTRA (ranuras compuestas) se eligen igual, con su
    # clave ('04b') en elegidas_da.json.
    for k in sorted(getattr(E(L), 'EXTRA', {})):
        nm = nombre_extra(L, k)
        v = el.get(k)
        if not v:
            w('%s sin tirada elegida' % nm)
            continue
        src = os.path.join(cand, '%s_%s.png' % (nm, v))
        dst = os.path.join(pl, nm + '.png')
        assert os.path.exists(src), src
        firma = '%s:%s' % (v, md5(src)[:10])
        if hecho.get(nm) == firma and os.path.exists(dst):
            w('%s %s ya aplicada' % (k, v))
            continue
        if os.path.exists(dst):
            aparta(dst, 'reemplazada_por_candidata_%s' % v)
        ac, ge = con_acento_extra(L, k)
        antes = medir_color(src)
        despues = limpia(src, dst, ac, ge)
        hecho[nm] = firma
        w('%s %s  acento %-5s gente %-5s  fria %.3f->%.3f  rosado %.2f%%->%.2f%%'
          % (k, v, ac, ge, antes['fria_p90'], despues['fria_p90'],
             antes['rosado_pct'], despues['rosado_pct']))
    json.dump(hecho, open(hecho_p, 'w', encoding='utf-8'), indent=1)


# 7 nov: los registros nuevos de la luz y el grade que no neutraliza
REG_GRADE = {'aire': 'dia', 'contra_ext': 'contraluz'}


def graduar_da(origen, destino, registro='dia', techo=False, semilla=7):
    """`graduar_registro.graduar` con la MISMA curva para los tres canales
    (sacada de la luma) y sin `neutralizar_entorno`: el objetivo, el techo,
    el alisado y el tramado son los de la serie; el verde y el ocre que la
    limpieza dejo, se quedan."""
    import numpy as np
    from PIL import Image
    import graduar_registro as GR
    import graduar_serie as GS
    import grade_placas as G
    import suave
    reg = REG_GRADE.get(registro, registro)
    obj = GR.REGISTRO[reg]
    if techo:
        m = GR.medir(origen)
        if m[1] < obj[1] - GR.TOLERANCIA and m[2] < obj[2] * GR.BLANCO_MINIMO:
            obj = (obj[0], int(round(m[1])), obj[2])
    viejo = (G.OBJETIVO, GS.anclas.__defaults__, G.curva.__defaults__, GS.POR_PENDIENTE)
    try:
        G.OBJETIVO = obj
        GS.anclas.__defaults__ = (obj,)
        G.curva.__defaults__ = (obj,)
        GS.POR_PENDIENTE = bool(techo)
        a = np.asarray(Image.open(origen).convert('RGB')).astype(np.float32)
        a, _ = suave.alisar(a, GS.pendiente_de(a))
        a, _ = suave.alisar_croma(a)
        lum = 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]
        p2, p50, p98 = (float(np.percentile(lum, p)) for p in (2, 50, 98))
        xf, yf = GS._lut_float(p2, p50, p98)
        out = np.interp(a, xf, yf)
        rng = np.random.default_rng(semilla)
        d = rng.random(out.shape, dtype=np.float32) - rng.random(out.shape, dtype=np.float32)
        Image.fromarray(np.clip(out + d * 0.5, 0, 255).astype(np.uint8)).save(destino)
    finally:
        G.OBJETIVO, GS.anclas.__defaults__, G.curva.__defaults__, GS.POR_PENDIENTE = viejo
    return obj


def gradua(L, o, g, reg, ac, ge, etiqueta, techo=True):
    """La placa limpia -> graduada en su registro, con las dos relimpiezas
    (rosado y frio despues del grade). Es lo que `construir` hacia en linea;
    sale a funcion para graduar tambien las placas EXTRA."""
    import graduar_registro as GR
    c = GR.medir(o)
    graduar_da(o, g, reg, techo=techo)
    mc = medir_color(g)
    fr = mc['fria_p90']
    if mc['rosado_pct'] > 0.3:
        w('%s rosado despues del grade %.2f%% -> %.2f%%'
          % (etiqueta, mc['rosado_pct'], limpia(g, g, ac, ge)['rosado_pct']))
        fr = medir_color(g)['fria_p90']
    if fr > 0.05:
        w('%s frio despues del grade %.3f -> %.3f'
          % (etiqueta, fr, limpia(g, g, ac, ge)['fria_p90']))
    return c, GR.medir(g)


def hornea(cam_base, fuente, salida, frames, extra_cam):
    """camara.render con el riel de la placa (2560 de ancho -> ventana >= 0,752)."""
    import camara
    cam = dict(cam_base)
    cam.update({'fuente': fuente, 'salida': salida, 'frames': frames})
    cam.update(extra_cam or {})
    from PIL import Image as _Im
    piso = 1920.0 / _Im.open(fuente).size[0] * 1.002 + 0.002
    emp = max(0.0, float(cam.get('empuje', 0.0)))
    if cam['encuadre'] * (1 - emp) < piso:
        cam['encuadre'] = round(piso / (1 - emp), 4)
    if cam['encuadre'] * (1 - min(0.0, float(cam.get('empuje', 0.0)))) > 1.0:
        cam['encuadre'] = round(1.0 / (1 - min(0.0, float(cam['empuje']))), 4)
    camara.render(cam)
    return cam


def construir(L, solo=None):
    import camara
    import graduar_registro as GR
    pl = R.sub(L, '01 PLANOS')
    gd = os.path.join(pl, '_grade')
    os.makedirs(gd, exist_ok=True)
    tl = R.sub(L, '10 TIMELINE SEBASTIAN')
    ran = os.path.join(tl, 'RANURAS')
    os.makedirs(ran, exist_ok=True)
    for n in sorted(E(L).R):
        if solo and n not in solo:
            continue
        largo, reg = E(L).R[n][0], E(L).R[n][1]
        nm = nombre(L, n)
        o, g = os.path.join(pl, nm + '.png'), os.path.join(gd, nm + '.png')
        if not os.path.exists(o):
            w('r%02d sin placa elegida: no se construye' % n)
            continue
        c = GR.medir(o)
        # 31 oct: SIN_TECHO (r28 del C2): la placa se lleva al medio tono de su
        # registro aunque venga oscura; con techo se quedaba en negro.
        graduar_da(o, g, reg, techo=n not in getattr(E(L), 'SIN_TECHO', set()))
        # 27 oct: el grade de contraluz le devolvio un cian a A r09 (frio p90
        # 0,02 -> 0,07; se ve en la ropa clara). Si el grade deja frio, la
        # limpieza de bandas se vuelve a pasar DESPUES del grade.
        mc = medir_color(g)
        fr = mc['fria_p90']
        if mc['rosado_pct'] > 0.3:
            ac, ge = con_acento(L, n)
            w('r%02d rosado despues del grade %.2f%% -> %.2f%%'
              % (n, mc['rosado_pct'], limpia(g, g, ac, ge, chaleco(L, n))['rosado_pct']))
            fr = medir_color(g)['fria_p90']
        if fr > 0.05:
            ac, ge = con_acento(L, n)
            w('r%02d frio despues del grade %.3f -> %.3f'
              % (n, fr, limpia(g, g, ac, ge, chaleco(L, n))['fria_p90']))
        ac, ge = con_acento(L, n)
        if ac and ((L, n) in ACENTO_AUTO or L in ACENTO):
            import numpy as np
            from PIL import Image
            antes = medir_acento(g)
            if (L, n) in ACENTO_AUTO:
                w('r%02d giro medido %s' % (n, mide_parametros_acento(L, n, g)))
            Image.fromarray(acento_serie(np.asarray(Image.open(g).convert('RGB')),
                                         L, ac, n=n)).save(g)
            w('r%02d acento de la serie %s -> %s' % (n, antes, medir_acento(g)))
        if ac:
            reinyectar_acento(o, g, 'r%02d' % n)
            nivelar_acento(L, g, 'r%02d' % n)
        if chaleco(L, n):
            # 4 nov (C3): en las placas de noche que se gradúan sin techo
            # (r02, r10) el grade dejo el chaleco blanco-gris (frio 0,37 y
            # 0,39 despues del grade, y la relimpieza del frio se lo llevo).
            # Se le devuelven tono y saturacion de la limpia, como al acento,
            # y se acota otra vez.
            reinyectar_acento(o, g, 'r%02d chaleco' % n, banda=(34, 62), piso_s=0.25,
                              perdida=0.8)
            import numpy as np
            from PIL import Image
            hsv = np.asarray(Image.open(g).convert('HSV')).astype(np.float32)
            Image.fromarray(np.clip(topes_chaleco(hsv), 0, 255).astype(np.uint8), 'HSV') \
                .convert('RGB').save(g)
        if L in CIELO:
            import numpy as np
            from PIL import Image
            Image.fromarray(cielo(np.asarray(Image.open(g).convert('RGB')), L)).save(g)
            w('r%02d cielo apagado' % n)
        piso_negro(g, 'r%02d' % n)
        gris(g, L, 'r%02d' % n)
        v = GR.medir(g)
        sal = os.path.join(ran, '%s_v%d.mp4' % (nm, largo))
        if os.path.exists(sal):
            aparta(sal, 'rehorneada_%s' % time.strftime('%H%M%S'))
        t0 = time.time()
        base = {'modo': 'camara', 'encuadre': 0.88, 'empuje': 0.0,
                'deriva': [0.0, 0.0], 'vibra': 5.0}
        propia = dict(getattr(E(L), 'REUSA', {}).get(n, (None, {}))[1])
        # 31 oct: camara propia de una ranura que no reusa (r25 del C2)
        propia.update(getattr(E(L), 'CAMARA', {}).get(n, {}))
        # 30 oct: la placa de Flash mide 2560 de ancho y el riel de `camara`
        # no deja bajar de 1920/2560 = 0,752 (`hornea` sube el encuadre lo
        # justo para que el empuje termine dentro del riel).
        partes = getattr(E(L), 'COMPUESTAS', {}).get(n)
        if not partes:
            hornea(base, g, sal, largo, propia)
        else:
            # 31 oct: ranura en dos planos pegados por corte (r04 y r12 del
            # C2). Cada parte se hornea aparte con su placa graduada y se
            # concatenan sin recodificar; la ultima toma lo que falte.
            tmp = []
            queda = largo
            for i, (quien, cu) in enumerate(partes):
                if isinstance(quien, int):
                    f, et = os.path.join(gd, nombre(L, quien) + '.png'), 'r%02d' % quien
                else:
                    ex = E(L).EXTRA[quien]
                    f = os.path.join(gd, nombre_extra(L, quien) + '.png')
                    o_ex = os.path.join(pl, nombre_extra(L, quien) + '.png')
                    acx, gex = con_acento_extra(L, quien)
                    cx, vx = gradua(L, o_ex, f, ex[1], acx, gex, quien)
                    if acx:
                        reinyectar_acento(o_ex, f, quien)
                        nivelar_acento(L, f, quien)
                    piso_negro(f, quien)
                    w('%s %-9s crudo %3.0f/%3.0f/%3.0f  final %3.0f/%3.0f/%3.0f'
                      % (quien, ex[1], cx[0], cx[1], cx[2], vx[0], vx[1], vx[2]))
                    et = quien
                cu = queda if (cu is None or i == len(partes) - 1) else cu
                assert 0 < cu <= queda, (nm, partes, cu, queda)
                queda -= cu
                t = os.path.join(ran, '_%s_parte%d_%s.mp4' % (nm, i, et))
                hornea(base, f, t, cu, propia)
                assert cuadros(t) == cu, (t, cuadros(t), cu)
                tmp.append(t)
            lista = os.path.join(ran, '_%s_partes.txt' % nm)
            with open(lista, 'w', encoding='utf-8') as fh:
                for t in tmp:
                    fh.write("file '%s'\n" % t.replace("'", "'\\''"))
            subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0',
                            '-i', lista, '-c', 'copy', sal], check=True)
            for t in tmp + [lista]:
                os.remove(t)
            w('r%02d compuesta: %s' % (n, ' + '.join('%s x%d' % (q, c if c else largo)
                                                    for q, c in partes)))
        nf = cuadros(sal)
        w('r%02d %-9s crudo %3.0f/%3.0f/%3.0f  final %3.0f/%3.0f/%3.0f  obj %3d  '
          '%4d/%4d %s  %.0f s' % (n, reg, c[0], c[1], c[2], v[0], v[1], v[2],
                                  GR.REGISTRO[REG_GRADE.get(reg, reg)][1], nf, largo,
                                  'OK' if nf == largo else 'FALLA', time.time() - t0))
        assert nf == largo, (nm, nf, largo)
    # el respiro: la r01 graduada, 48 cuadros, quieta. Si se rehacen solo
    # algunas ranuras y la r01 no esta entre ellas, el respiro no cambia y no
    # se toca (28 oct: E r03/r11 sobre la linea que Sebastian ya ajusto).
    if solo and 1 not in solo:
        return
    # 4 nov (C4): la r01 cambio (la nina en el camino) y el respiro de la
    # linea aprobada es la r01 vacia; `RESPIRO_FIJO` lo deja como esta
    if getattr(E(L), 'RESPIRO_FIJO', False):
        w('respiro fijo: no se rehace')
        return
    respiro(L)


# 3 nov, pase previo a la revision de Sebastian (como en Ley 1826). Medido
# sobre lo que el deja a mano en las lineas que aprueba (situaciones C, D, E,
# G; Derechos humanos U2): el respiro termina en un FUNDIDO A NEGRO antes del
# corte al carton blanco de cierre. Va horneado en el archivo: los ultimos
# RESPIRO_FUNDE cuadros bajan a negro. La linea no cambia.
RESPIRO_FUNDE = 16


def respiro(L):
    """El respiro: la r01 graduada, 48 cuadros, quieta, con el fundido a
    negro del final horneado. Paso aparte para rehacerlo sin tocar ranuras."""
    tl = R.sub(L, '10 TIMELINE SEBASTIAN')
    gd = os.path.join(R.sub(L, '01 PLANOS'), '_grade')
    # 7 nov (DA V06): la r01 del caso Francisco es la tala con motosierra;
    # cerrar ahi despues de «proteccion del Amazonas» dice lo contrario. Cada
    # video puede elegir la placa del respiro (escenas.RESPIRO, por defecto 1)
    g1 = os.path.join(gd, nombre(L, getattr(E(L), 'RESPIRO', 1)) + '.png')
    rd = os.path.join(tl, 'RESPIRO')
    os.makedirs(rd, exist_ok=True)
    d = os.path.join(rd, 'DA_%s_respiro_v%d.mp4' % (L, N_RESPIRO))
    if os.path.exists(d):
        aparta(d, 'rehecho_%s' % time.strftime('%H%M%S'))
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-i', g1,
                    '-vf', 'scale=1920:1080:flags=lanczos,fps=%s,'
                    'fade=t=out:s=%d:n=%d:c=black'
                    % (FPS, N_RESPIRO - RESPIRO_FUNDE, RESPIRO_FUNDE),
                    '-frames:v', str(N_RESPIRO), '-c:v', 'libx264', '-crf', '14',
                    '-preset', 'slow', '-pix_fmt', 'yuv420p', '-an', d], check=True)
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', d, '-vf',
                        'signalstats,metadata=print:key=lavfi.signalstats.YAVG',
                        '-an', '-f', 'null', '-'], capture_output=True, text=True).stderr
    ys = [float(x) for x in re.findall(r'YAVG=([0-9.]+)', r)]
    w('respiro %d/%d  luma %s -> %s -> %s' % (cuadros(d), N_RESPIRO, ys[0], ys[40], ys[-1]))


def blancos(L):
    # 3 nov, Ley 1826: el antetitulo ya viene con sus mayusculas («Unidad 2 ·
    # Estudio reverso de caso 1»); el .lower().capitalize() de la serie lo
    # dejaba en «Unidad 2 · estudio reverso...».
    import cartones_ta as C
    C.MARCA = MARCA_PNG
    cart = R.sub(L, '02 CARTONES')
    for k in ('entrada', 'cierre'):
        p = os.path.join(cart, 'DA_%s_carton_%s.mov' % (L, k))
        if os.path.exists(p):
            aparta(p, 'rehecho_%s' % time.strftime('%H%M%S'))
        C.render_carton({'ante': '%s · %s' % (ANTE, TEMAS[L][2]),
                         'titulo': TEMAS[L][3]}, N_BLANCO,
                        C.BLANCO_FONDO, False, p, con_marca=True)
        w('%s %d cuadros' % (os.path.basename(p), cuadros(p)))


# 31 oct, revision de Sebastian de la U3: «music starts getting louder at
# 3:59 and the voice is still going». Dos causas: TA05 crece hacia el final
# (se nivela antes del ducking, cama_musica._nivelar) y la cama bombeaba en
# las pausas de 0,35-1,2 s entre bloques (se unen, cama_musica._unir).
# Derechos humanos (31 oct): la leccion de la U3 de Justicia restaurativa
# va por defecto en los cinco: cama nivelada antes del ducking y tramos de
# voz unidos en las pausas cortas.
# 1 nov: la cama entra 23 cuadros antes de que acabe la intro (Sebastian, U2)
MUSICA_ABRE = N_INTRO - 23
_AJUSTE = {'nivelar': {'ventana': 3.0, 'suavizado': 4.0, 'sube': 4.0,
                       'baja': 12.0},
           'unir': 1.5}
CAMA_AJUSTES = {k: dict(_AJUSTE) for k in VIDEOS}


def musica(L):
    rej = json.load(open(os.path.join(R.voces(L), 'DA_%s_rejilla.json' % L),
                        encoding='utf-8'))
    off = CABEZA / FPS_N
    voz = [[round(off + t['entra'], 3), round(off + t['sale'], 3)] for t in rej['tramos']]
    sal = os.path.join(R.sub(L, '08 MUSICA'), 'DA_%s_MUSICA_cama.wav' % L)
    os.makedirs(os.path.dirname(sal), exist_ok=True)
    if os.path.exists(sal):
        aparta(sal, 'rehecha_%s' % time.strftime('%H%M%S'))
    # 1 nov (Sebastian): la cama no pisa el sonido de la intro ni del cierre.
    # Entra con fundido en el ultimo segundo de la intro (como la dejo el a
    # mano en la U2: cuadro 159) y termina de salir donde empieza el cierre.
    spec = [{'pista': CAMA_MUSICA.get(L, PISTA_MUSICA_FUENTE), 'salida': sal,
             'dur': round(pieza(L) / FPS_N, 3), 'voz': voz, 'objetivo': -26.0,
             'abre': round(MUSICA_ABRE / FPS_N, 3),
             'cierra': round((pieza(L) - N_INTRO) / FPS_N, 3)}]
    spec[0].update(CAMA_AJUSTES.get(L, {}))
    sp = os.path.join(TMP, 'spec_musica_da_%s.json' % L)
    json.dump(spec, open(sp, 'w', encoding='utf-8'), indent=1)
    r = subprocess.run([sys.executable, os.path.join(H, 'musica', 'cama_musica.py'), sp],
                       capture_output=True, text=True)
    w(r.stdout.strip(), r.stderr.strip()[-400:])


# ---------------------------------------------------------------- linea
def plan(L):
    import cartones_da as CS
    base = R.carpeta(L)
    tl = os.path.join(base, '10 TIMELINE SEBASTIAN')
    cart = os.path.join(base, '02 CARTONES')
    v1, t = [], 0
    v1.append((t, N_INTRO, INTRO)); t += N_INTRO
    v1.append((t, N_BLANCO, os.path.join(cart, 'DA_%s_carton_entrada.mov' % L)))
    t += N_BLANCO
    ini = t
    for n in sorted(E(L).R):
        largo = E(L).R[n][0]
        v1.append((t, largo, os.path.join(tl, 'RANURAS', '%s_v%d.mp4'
                                          % (nombre(L, n), largo))))
        t += largo
    fin = t
    v1.append((t, N_RESPIRO, os.path.join(tl, 'RESPIRO', 'DA_%s_respiro_v%d.mp4'
                                          % (L, N_RESPIRO))))
    t += N_RESPIRO
    v1.append((t, N_BLANCO, os.path.join(cart, 'DA_%s_carton_cierre.mov' % L)))
    t += N_BLANCO
    v1.append((t, N_INTRO, INTRO)); t += N_INTRO
    v4 = [(c['ini'], c['cuadros'], os.path.join(cart, c['archivo']))
          for c in CS.calcula(L)]
    v6 = [(ini, N_MARCA, MARCA), (fin - N_MARCA, N_MARCA, MARCA)]
    voz = os.path.join(R.voces(L), 'DA_%s_NARRADOR.wav' % L)
    # 4 nov (C4, «Taita»): Resolve tiene abierto el master y Windows no deja
    # reescribirlo en su sitio; la version corregida va con sufijo y manda
    # (C5: una segunda correccion va como _v3; manda la mas alta que exista)
    for k in range(9, 1, -1):
        if os.path.exists(voz[:-4] + '_v%d.wav' % k):
            voz = voz[:-4] + '_v%d.wav' % k
            break
    mus = os.path.join(base, '08 MUSICA', 'DA_%s_MUSICA_cama.wav' % L)
    return v1, v4, v6, voz, mus, ini, fin - ini, t


def capas(L):
    """V2 MOVIMIENTO, V3 DETALLE y V5 MOTION GRAPHICS: lo que exista en disco.
    Son capas que se pueden apagar: debajo, V1 tiene la pieza completa.
        V2  10 TIMELINE SEBASTIAN/MOVIMIENTO/<ranura>_mov_v<largo>.mp4
        V3  10 TIMELINE SEBASTIAN/DETALLE/<det>_v<cuadros>.mp4
        V5  09 MOTION GRAPHICS/DA_<V>_mg.json -> [{archivo, ini, cuadros}],
            ini en cuadros de la linea (desde 0)
    Devuelve las tres listas y lo que se espero y no estaba."""
    base = R.carpeta(L)
    tl = os.path.join(base, '10 TIMELINE SEBASTIAN')
    pos, t = {}, CABEZA
    for n in sorted(E(L).R):
        pos[n] = t
        t += E(L).R[n][0]
    v2, v3, v5, faltan = [], [], [], []
    for n in sorted(E(L).R):
        largo = E(L).R[n][0]
        p = os.path.join(tl, 'MOVIMIENTO', '%s_mov_v%d.mp4' % (nombre(L, n), largo))
        if os.path.exists(p):
            v2.append((pos[n], largo, p))
    sp = os.path.join(TMP, 'prompts_da_%s.json' % L)
    dets = json.load(open(sp, encoding='utf-8')).get('detalles', {}) if os.path.exists(sp) else {}
    for nm, d in sorted(dets.items()):
        p = os.path.join(tl, 'DETALLE', '%s_v%d.mp4' % (nm, d['cuadros']))
        if os.path.exists(p):
            v3.append((pos[d['ranura']] + d['entra'], d['cuadros'], p))
        else:
            faltan.append(os.path.basename(p))
    mg = os.path.join(base, '09 MOTION GRAPHICS')
    mj = os.path.join(mg, 'DA_%s_mg.json' % L)
    for d in (json.load(open(mj, encoding='utf-8')) if os.path.exists(mj) else []):
        p = os.path.join(mg, d['archivo'])
        if os.path.exists(p):
            v5.append((d['ini'], d['cuadros'], p))
        else:
            faltan.append(d['archivo'])
    return v2, v3, v5, faltan


def huecos(tl, pista=1):
    fuera, pos = [], 0
    tot = tl.GetEndFrame() - tl.GetStartFrame()
    for it in tl.GetItemListInTrack('video', pista):
        a, b = it.GetStart() - tl.GetStartFrame(), it.GetEnd() - tl.GetStartFrame()
        if a > pos:
            fuera.append((pos, a))
        pos = max(pos, b)
    if pos < tot:
        fuera.append((pos, tot))
    return fuera


def construye(resolve, L):
    pr = resolve.GetProjectManager().GetCurrentProject()
    mp = pr.GetMediaPool()
    nl = nombre_linea(L)
    existentes = [pr.GetTimelineByIndex(i) for i in range(1, int(pr.GetTimelineCount()) + 1)]
    for x in [x for x in existentes if x is not None]:
        if x.GetName() != nl:
            continue
        if x.GetItemListInTrack('video', 1):
            nombres = {pr.GetTimelineByIndex(j).GetName()
                       for j in range(1, int(pr.GetTimelineCount()) + 1)}
            k, nuevo = 1, '%s (anterior)' % nl
            while nuevo in nombres:
                k += 1
                nuevo = '%s (anterior %d)' % (nl, k)
            x.SetName(nuevo)
        else:
            mp.DeleteTimelines([x])

    v1, v4, v6, voz, mus, ini, dur_cuerpo, tot = plan(L)
    v2, v3, v5, _ = capas(L)
    assert tot == pieza(L), (tot, pieza(L))
    todos = [p for _, _, p in v1 + v2 + v3 + v4 + v5 + v6] + [voz, mus]
    falta = sorted({p for p in todos if not os.path.exists(p)})
    if falta:
        return None, 'faltan en disco: %s' % falta[:4]

    raiz = mp.GetRootFolder()

    def _hijo(f, n):
        for x in f.GetSubFolderList():
            if x.GetName() == n:
                return x
        return None

    def _asegura(f, n):
        return _hijo(f, n) or mp.AddSubFolder(f, n)

    def _baja(f, partes):
        for q in partes:
            if q:
                f = _asegura(f, q)
        return f

    comunes = None
    for x in raiz.GetSubFolderList():
        if x.GetName().strip() == '00 COMUNES':
            comunes = x
    unidad_rel = os.path.relpath(R.carpeta(L), r'E:\DAE MASTER')
    carp = _baja(raiz, unidad_rel.split(os.sep))
    sdir = R.carpeta(L)

    def _bin_de(ruta):
        r = ruta.replace('/', os.sep)
        if r.lower().startswith(sdir.lower()):
            rel = os.path.dirname(os.path.relpath(r, sdir))
            return _baja(carp, rel.split(os.sep)) if rel else carp
        if comunes is not None and '00 COMUNES' in r.upper():
            return _asegura(comunes, 'INTRO' if 'INTRO' in r.upper() else 'MARCA DE AGUA')
        return carp

    quiero = {os.path.basename(x) for x in todos if '00 COMUNES' not in x.upper()}

    def _todos(f):
        for c in f.GetClipList():
            yield c
        for sf in f.GetSubFolderList():
            for c in _todos(sf):
                yield c

    viejos = [c for c in _todos(carp)
              if os.path.basename((c.GetClipProperty('File Path') or '').replace('/', os.sep))
              in quiero]
    if viejos:
        mp.DeleteClips(viejos)

    pedidos = sorted(set(todos))
    por_bin = {}
    for x in pedidos:
        b = _bin_de(x)
        por_bin.setdefault(id(b), [b, []])[1].append(x)

    def _puestos():
        d = {}
        for b, _ in por_bin.values():
            for c in b.GetClipList():
                r = (c.GetClipProperty('File Path') or '').replace('/', os.sep)
                if r:
                    d[os.path.basename(r)] = c
        return d

    for b, lista in por_bin.values():
        mp.SetCurrentFolder(b)
        ya = _puestos()
        nuevos = [x for x in lista if os.path.basename(x) not in ya]
        if nuevos:
            mp.ImportMedia(nuevos)
    for _ in range(6):
        pool = _puestos()
        faltan = [x for x in pedidos if os.path.basename(x) not in pool]
        if not faltan:
            break
        time.sleep(0.7)
        for x in faltan:
            mp.SetCurrentFolder(_bin_de(x))
            mp.ImportMedia([x])
            time.sleep(0.15)
    pool = _puestos()
    faltan = [x for x in pedidos if os.path.basename(x) not in pool]
    if faltan:
        return None, 'no entraron al pool: %s' % faltan[:3]

    mp.SetCurrentFolder(_asegura(carp, '10 TIMELINE SEBASTIAN'))
    tl = mp.CreateEmptyTimeline(nl)
    pr.SetCurrentTimeline(tl)
    while tl.GetTrackCount('video') < len(PISTAS_V):
        tl.AddTrack('video')
    while tl.GetTrackCount('audio') < len(PISTAS_A):
        tl.AddTrack('audio', 'stereo')
    for i, n in PISTAS_V:
        tl.SetTrackName('video', i, n)
    for i, n in PISTAS_A:
        tl.SetTrackName('audio', i, n)

    for lista, pista in ((v1, 1), (v2, 2), (v3, 3), (v4, 4), (v5, 5), (v6, 6)):
        if not lista:
            continue
        items = []
        for pos, largo, p in lista:
            it = pool.get(os.path.basename(p))
            if it is None:
                return None, 'no quedo en el pool: %s' % p
            items.append({'mediaPoolItem': it, 'startFrame': 0, 'endFrame': largo,
                          'trackIndex': pista, 'recordFrame': T0 + pos, 'mediaType': 1})
        mp.AppendToTimeline(items)
    for p, largo, pos, pista in ((voz, dur_cuerpo, ini, 1),
                                 (mus, tot, 0, PISTA_MUSICA),
                                 (INTRO, N_INTRO, 0, PISTA_AMBIENTE),
                                 (INTRO, N_INTRO, tot - N_INTRO, PISTA_AMBIENTE)):
        it = pool.get(os.path.basename(p))
        if it is None:
            return None, 'no quedo en el pool: %s' % p
        mp.AppendToTimeline([{'mediaPoolItem': it, 'startFrame': 0, 'endFrame': largo,
                              'trackIndex': pista, 'recordFrame': T0 + pos,
                              'mediaType': 2}])
    h = huecos(tl)
    if h:
        return tl, 'QUEDARON HUECOS en V1: %s' % h[:6]
    largo_real = tl.GetEndFrame() - tl.GetStartFrame()
    if largo_real != tot:
        return tl, 'la linea mide %d y el plan pedia %d' % (largo_real, tot)
    return tl, None


def _resolve():
    import DaVinciResolveScript as dvr
    return dvr.scriptapp('Resolve')


def montar(L):
    resolve = _resolve()
    pm = resolve.GetProjectManager()
    pr = pm.GetCurrentProject()
    # 7 nov: tras una reconexion Resolve quedo en «Untitled Project» y en la
    # pagina Deliver (AddSubFolder devuelve None ahi): se asegura las dos cosas
    if pr is None or pr.GetName() != 'DAE MASTER - CURSOS':
        pr = pm.LoadProject('DAE MASTER - CURSOS')
    resolve.OpenPage('edit')
    w('proyecto:', pr.GetName())
    tl, err = construye(resolve, L)
    largo = (tl.GetEndFrame() - tl.GetStartFrame()) if tl else -1
    w('%s  largo %d (pieza %d)  %s' % (nombre_linea(L), largo, pieza(L), err or 'OK'))
    if err:
        raise SystemExit(err)
    v = [(i, tl.GetTrackName('video', i), len(tl.GetItemListInTrack('video', i)))
         for i in range(1, tl.GetTrackCount('video') + 1)]
    a = [(i, tl.GetTrackName('audio', i), len(tl.GetItemListInTrack('audio', i)))
         for i in range(1, tl.GetTrackCount('audio') + 1)]
    w('   ', [x for x in v if x[2]])
    w('   ', [x for x in a if x[2]])
    w('    capas que faltan en disco:', capas(L)[3] or 'ninguna')
    dest = R.sub(L, '10 TIMELINE SEBASTIAN')
    drt = os.path.join(dest, '%s.drt' % nombre_linea(L))
    if os.path.exists(drt):
        aparta(drt, 'remontada_%s' % time.strftime('%H%M%S'))
    tl.Export(drt, resolve.EXPORT_DRT)
    w('   .drt', os.path.getsize(drt) if os.path.exists(drt) else 'NO SE ESCRIBIO')
    resolve.GetProjectManager().SaveProject()


REVISION = os.path.join(TMP, 'revision')


def exportar(L, destino=None, nm=None):
    resolve = _resolve()
    pr = resolve.GetProjectManager().GetCurrentProject()
    tl = None
    for i in range(1, int(pr.GetTimelineCount()) + 1):
        t = pr.GetTimelineByIndex(i)
        if t.GetName() == nombre_linea(L):
            tl = t
    if tl is None:
        raise SystemExit('no hay linea %s' % nombre_linea(L))
    destino = destino or RENDER
    os.makedirs(destino, exist_ok=True)
    pr.SetCurrentTimeline(tl)
    pr.DeleteAllRenderJobs()
    nm = nm or 'DA_%s_master' % L
    m = os.path.join(destino, nm + '.mp4')
    if os.path.exists(m):
        aparta(m, 'rerender_%s' % time.strftime('%H%M%S'))
    ok = pr.SetRenderSettings({'SelectAllFrames': True, 'TargetDir': destino,
                               'CustomName': nm, 'FormatWidth': 1920,
                               'FormatHeight': 1080, 'VideoQuality': 80000,
                               'AudioCodec': 'lpcm', 'AudioBitDepth': 24,
                               'AudioSampleRate': 48000})
    pr.SetCurrentRenderFormatAndCodec('mp4', 'H264_NVIDIA')
    job = pr.AddRenderJob()
    w('render %s job %s settings %s' % (nm, job, ok))
    pr.StartRendering([job])
    t0 = time.time()
    while pr.IsRenderingInProgress():
        time.sleep(3)
    st = pr.GetRenderJobStatus(job)
    w('   %s %s %.0f s' % (st.get('JobStatus'), st.get('CompletionPercentage'),
                           time.time() - t0))


FISCALIA = ['-c:v', 'libx264', '-crf', '18', '-preset', 'slow', '-tune', 'animation',
            '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-level', '4.0',
            '-x264-params', 'keyint=48:min-keyint=24:scenecut=40',
            '-c:a', 'copy', '-movflags', '+faststart']
LIGERA = ['-vf', 'scale=1280:720:flags=lanczos', '-c:v', 'libx264', '-crf', '25',
          '-preset', 'medium', '-tune', 'animation', '-pix_fmt', 'yuv420p',
          '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart']


def entregas(L, version=1, solo=None):
    # `entregas=2` desde la consola: una re-entrega con su propio numero
    if solo:
        version = max(solo)
    m = os.path.join(RENDER, 'DA_%s_master.mp4' % L)
    exp = R.sub(L, '05 EXPORTS')
    os.makedirs(exp, exist_ok=True)
    f = os.path.join(exp, 'DA_%s_v%d.mp4' % (L, version))
    l = os.path.join(exp, 'DA_%s_v%d_revision_720p.mp4' % (L, version))
    for p in (f, l):
        if os.path.exists(p):
            aparta(p, 'reexportada_%s' % time.strftime('%H%M%S'))
    # 4 nov (C4): Sebastian corrio la cama 19 cuadros y la linea pasa del outro
    # (4441 contra 4422); la cola de la cama es silencio digital (medido) y el
    # video ahi es negro. Se entrega la pieza: hasta el ultimo cuadro del outro.
    corte = []
    if cuadros(m) > pieza(L):
        corte = ['-frames:v', str(pieza(L)), '-t', '%.6f' % (pieza(L) / FPS_N)]
        w('el master mide %d y la pieza %d: se entrega hasta el %d' % (cuadros(m), pieza(L), pieza(L)))
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', m] + FISCALIA + corte + [f], check=True)
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', m] + LIGERA + corte + [l], check=True)
    a, b, c = cuadros(m), cuadros(f), cuadros(l)
    w('cuadros master %d fiscalia %d ligera %d pieza %d  %s'
      % (a, b, c, pieza(L), 'OK' if b == c == pieza(L) <= a else 'NO CUADRA'))
    w('MB %d / %d / %d' % (os.path.getsize(m) >> 20, os.path.getsize(f) >> 20,
                           os.path.getsize(l) >> 20))


def verificar(L, version=1, solo=None):
    if solo:
        version = max(solo)
    exp = R.sub(L, '05 EXPORTS')
    f = os.path.join(exp, 'DA_%s_v%d.mp4' % (L, version))
    n = cuadros(f)
    w('cuadros %d / pieza %d  %s' % (n, pieza(L), 'OK' if n == pieza(L) else 'FALLA'))
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', f, '-vf',
                        'blackdetect=d=0.04:pix_th=0.06', '-an', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    negros = [l.split('blackdetect')[1].strip() for l in r.splitlines() if 'black_start' in l]
    w('negros:', negros or 'ninguno')
    r = subprocess.run(['ffmpeg', '-nostats', '-i', f, '-af', 'ebur128=peak=true',
                        '-vn', '-f', 'null', '-'], capture_output=True, text=True).stderr
    for l in r.splitlines()[-14:]:
        if l.strip().startswith(('I:', 'Peak:', 'LRA:')):
            w('   ', l.strip())
    # una hoja con un cuadro a mitad de cada ranura + entrada y cierre
    from PIL import Image
    v1, v4, v6, voz, mus, ini, dur, tot = plan(L)
    marcas = [pos + largo // 2 for pos, largo, _ in v1]
    hoja = Image.new('RGB', (4 * 480, ((len(marcas) + 3) // 4) * 270), (20, 20, 20))
    for i, q in enumerate(marcas):
        p = os.path.join(TMP, '_q_%s.png' % L)   # uno por situacion: corren a la vez
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', '%.3f' % ((q + 0.5) / FPS_N),
                        '-i', f, '-frames:v', '1', '-vf', 'scale=480:270', p], check=True)
        hoja.paste(Image.open(p), ((i % 4) * 480, (i // 4) * 270))
    hp = os.path.join(TMP, 'verif_%s.jpg' % L)
    hoja.save(hp, quality=85)
    w('hoja', hp)


def revisar(L):
    """Chequeo de la linea SIN EXPORTAR (27 oct, Sebastian: «timeline
    completa en su carpeta de DaVinci, sin exportar todavia»). Se rinde a
    D:\\DAE\\_tmp\\sit\\revision -nunca a 05 EXPORTS- y sobre ese archivo:
    cuadros = pieza, negros, loudness, y una hoja con un cuadro a mitad de
    cada ranura, de cada detalle (V3), de cada movimiento (V2) y de cada
    rotulo (V8): lo que la pista agrega se tiene que VER en la hoja."""
    nm = 'DA_%s_v%d_REVISION_INTERNA' % (L, VERSION)
    exportar(L, REVISION, nm)
    f = os.path.join(REVISION, nm + '.mp4')
    n = cuadros(f)
    w('cuadros %d / pieza %d  %s' % (n, pieza(L), 'OK' if n == pieza(L) else 'FALLA'))
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', f, '-vf',
                        'blackdetect=d=0.04:pix_th=0.06', '-an', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    negros = [l.split('blackdetect')[1].strip() for l in r.splitlines() if 'black_start' in l]
    w('negros:', negros or 'ninguno')
    r = subprocess.run(['ffmpeg', '-nostats', '-i', f, '-af', 'ebur128=peak=true',
                        '-vn', '-f', 'null', '-'], capture_output=True, text=True).stderr
    for l in r.splitlines()[-14:]:
        if l.strip().startswith(('I:', 'Peak:', 'LRA:')):
            w('   ', l.strip())
    from PIL import Image, ImageDraw
    v1, v4, v6, voz, mus, ini, dur, tot = plan(L)
    v2, v3, v5, _ = capas(L)
    marcas = [('V1', pos + largo // 2) for pos, largo, _ in v1]
    marcas += [('V2', pos + largo // 2) for pos, largo, _ in v2]
    marcas += [('V3', pos + largo // 2) for pos, largo, _ in v3]
    marcas += [('V5', pos + largo // 2) for pos, largo, _ in v5]
    marcas.sort(key=lambda x: x[1])
    hoja = Image.new('RGB', (4 * 480, ((len(marcas) + 3) // 4) * 270), (20, 20, 20))
    d = ImageDraw.Draw(hoja)
    for i, (k, q) in enumerate(marcas):
        p = os.path.join(TMP, '_q_%s.png' % L)
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', '%.3f' % ((q + 0.5) / FPS_N),
                        '-i', f, '-frames:v', '1', '-vf', 'scale=480:270', p], check=True)
        x, y = (i % 4) * 480, (i // 4) * 270
        hoja.paste(Image.open(p), (x, y))
        d.text((x + 6, y + 4), '%s %d' % (k, q), fill=(255, 255, 0))
    hp = os.path.join(TMP, 'revision_%s_v%d.jpg' % (L, VERSION))
    hoja.save(hp, quality=85)
    w('hoja', hp, ' V2 %d  V3 %d  V5 %d' % (len(v2), len(v3), len(v5)))


def inicios(L):
    """31 oct (U4, revision de Sebastian): las placas de INICIO de Kling con
    cuadro inicial y final (`escenas.INICIO`, ranura -> clave de EXTRA) se
    gradan a _grade igual que una placa EXTRA de una ranura compuesta, para
    subirlas a Magnific como cuadro inicial. La placa de la ranura es el
    cuadro final."""
    pl = R.sub(L, '01 PLANOS')
    gd = os.path.join(pl, '_grade')
    os.makedirs(gd, exist_ok=True)
    for n, k in sorted(getattr(E(L), 'INICIO', {}).items()):
        ex = E(L).EXTRA[k]
        o = os.path.join(pl, nombre_extra(L, k) + '.png')
        g = os.path.join(gd, nombre_extra(L, k) + '.png')
        if os.path.exists(g):
            aparta(g, 'regradada_%s' % time.strftime('%H%M%S'))
        ac, ge = con_acento_extra(L, k)
        c, v = gradua(L, o, g, ex[1], ac, ge, k)
        if ac:
            reinyectar_acento(o, g, k)
            nivelar_acento(L, g, k)
        piso_negro(g, k)
        w('r%02d inicio %s %-9s crudo %3.0f/%3.0f/%3.0f  final %3.0f/%3.0f/%3.0f'
          % (n, k, ex[1], c[0], c[1], c[2], v[0], v[1], v[2]))


PASOS = {'elegir': elegir, 'construir': construir, 'inicios': inicios, 'blancos': blancos,
         'respiro': respiro,
         'musica': musica, 'montar': montar, 'exportar': exportar,
         'entregas': entregas, 'verificar': verificar, 'revisar': revisar}

if __name__ == '__main__':
    # `construir=5,6,7` rehace solo esas ranuras (27 oct: un apagon corto D y E
    # a mitad del horneado; lo ya horneado y verificado no se toca).
    # `v=2` antes de los pasos: la linea se llama «... v2» (montar, revisar).
    L = sys.argv[1].upper()
    for p in sys.argv[2:]:
        if p.startswith('v='):
            VERSION = int(p[2:])
            continue
        w('===', L, p)
        t0 = time.time()
        paso, _, arg = p.partition('=')
        if arg:
            PASOS[paso](L, solo={int(x) for x in arg.split(',')})
        else:
            PASOS[paso](L)
        w('--- %s %.0f s' % (p, time.time() - t0))
    w('LISTO')
