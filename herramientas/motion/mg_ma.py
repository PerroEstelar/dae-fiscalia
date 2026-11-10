# -*- coding: utf-8 -*-
r"""Motion graphics de las introducciones U2-U5 de Medio Ambiente, en After Effects.

Corre en la máquina de Sebastián y habla con el controlador de aftr por REST
(http://127.0.0.1:8787/command); el panel de aftr tiene que estar abierto en AE.
Lee los items `mg_lista` y `mg_act` de `cursos/medio-ambiente/plan_intros.py` y
arma una composición por item en el proyecto
`00 MOTION GRAPHICS\MA_intros_mg.aep`. Después `render` las rinde con aerender
(no bloquea AE) a `UNIDAD n\02 CARTONES\mg\<comp>.mov` con alfa.

El dibujo es el de los cartones de caja (cartones_v3): barra #FEB900 de 14 px en
x=86, texto Montserrat blanco desde x=170, bloque anclado abajo en y=690, ancho
615; la sombra es la misma idea (ambiental ancha + contacto) en una capa de
ajuste. Lo que agregan: íconos blancos (Magnific, `00 MOTION GRAPHICS\iconos`)
que entran con un pop cuando ella nombra cada cosa.

    python mg_ma.py armar            todas
    python mg_ma.py armar 2          una unidad
    python mg_ma.py render [2]       aerender de lo armado
"""
import json
import os
import subprocess
import sys
import time
import urllib.request

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, r'D:\DAE\_repo\cursos\medio-ambiente')
import plan_intros as P  # noqa: E402

API = 'http://127.0.0.1:8787/command'
FD = os.path.expanduser('~') + '/AppData/Local/Microsoft/Windows/Fonts/'
TTF = {'bold': FD + 'Montserrat-Bold.ttf', 'med': FD + 'Montserrat-Medium.ttf'}
PS = {'bold': 'Montserrat-Bold', 'med': 'Montserrat-Medium'}
CURSO = 'E:/DAE MASTER/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE'
ICONOS = CURSO + '/00 MOTION GRAPHICS/iconos'
AEP = CURSO + '/00 MOTION GRAPHICS/MA_intros_mg.aep'
AERENDER = 'C:/Program Files/Adobe/Adobe After Effects 2024/Support Files/aerender.exe'
OM = 'High Quality with Alpha'

FPS = 24000 / 1001
TEXT_X, BAR_X, BAR_W, BASE_Y, BAR_PAD, MAXW = 170, 86, 14, 690, 28, 615
INTERLINEA = 1.30
BAR_C = [254 / 255, 185 / 255, 0]
ICON_ACT, GAP_ICON = 64, 16          # tarjeta de actividad: ícono a la izquierda de «Actividad n»
ICON_FILA, GAP_FILA, SEP_FILA = 64, 20, 18   # lista
TXT_IN, TXT_OUT, RET_IN, RET_OUT, SUBE_IN, SUBE_OUT = 14, 10, 3, 2, 14, 8

_d = ImageDraw.Draw(Image.new('L', (10, 10)))


def cmd(c, p, timeout=120):
    req = urllib.request.Request(API, data=json.dumps({'command': c, 'params': p}).encode('utf-8'),
                                 headers={'Content-Type': 'application/json'})
    j = json.loads(urllib.request.urlopen(req, timeout=timeout).read().decode('utf-8'))
    if not j.get('ok'):
        raise RuntimeError('%s: %s' % (c, json.dumps(j)[:600]))
    return j.get('result')


def batch(cmds):
    r = cmd('batch', {'commands': cmds, 'stopOnError': True, 'undoName': 'mg_ma'})
    if r.get('failed'):
        raise RuntimeError(json.dumps([x for x in r['results'] if not x['ok']][:3])[:800])
    return r


def wrap(text, font, maxw):
    out, line = [], ''
    for w in text.split():
        probe = (line + ' ' + w).strip()
        if _d.textlength(probe, font=font) <= maxw or not line:
            line = probe
        else:
            out.append(line)
            line = w
    if line:
        out.append(line)
    return out


def maquetar(lineas, maxw):
    """Como cartones_v3.componer: (texto, peso, px, gap) -> renglones con su
    tope y su línea base relativos, y el alto total del bloque."""
    laid, y = [], 0
    for text, peso, px, gap in lineas:
        ft = ImageFont.truetype(TTF[peso], px)
        asc = ft.getmetrics()[0]
        y += gap
        for ln in wrap(text, ft, maxw):
            laid.append({'text': ln, 'peso': peso, 'px': px, 'top': y, 'base': y + asc})
            y += int(px * INTERLINEA)
    total = y - int(lineas[-1][2] * (INTERLINEA - 1.0))
    return laid, total


def t(f):
    return round(f / FPS, 5)


class Comp:
    def __init__(self, nombre, n):
        self.nombre, self.n = nombre, n
        self.c = [{'command': 'createComp', 'params': {
            'name': nombre, 'width': 1920, 'height': 1080, 'duration': n / FPS, 'frameRate': FPS}}]
        self.k = 0

    def add(self, c, **p):
        p['compName'] = self.nombre
        self.c.append({'command': c, 'params': p})

    def key(self, layer, prop, frames, values):
        self.add('setKeyframes', layer=layer, property=prop, times=[t(f) for f in frames],
                 values=values, easyEase=True)

    def texto(self, x, base, ln, f_in, f_out):
        self.k += 1
        nm = 'txt%02d' % self.k
        self.add('addTextLayer', text=ln['text'], name=nm)
        self.add('setTextDocument', layer=nm, font=PS[ln['peso']], fontSize=ln['px'],
                 fillColor=[1, 1, 1], justification='left', tracking=0)
        self.key(nm, 'position', [f_in, f_in + TXT_IN, f_out, f_out + TXT_OUT],
                 [[x, base + SUBE_IN], [x, base], [x, base], [x, base - SUBE_OUT]])
        self.key(nm, 'opacity', [f_in, f_in + TXT_IN, f_out, f_out + TXT_OUT], [0, 100, 100, 0])

    def icono(self, archivo, cx, cy, lado, f_in, f_out):
        self.k += 1
        nm = 'ico%02d' % self.k
        self.add('addFootageLayer', itemName='ico_' + archivo, name=nm)
        s = 100.0 * lado / 512
        self.add('setLayerProperty', layer=nm, property='position', value=[cx, cy])
        self.key(nm, 'scale', [f_in, f_in + 8, f_in + 13],
                 [[0, 0], [s * 1.14, s * 1.14], [s, s]])
        self.add('setKeyframes', layer=nm, property='opacity',
                 times=[t(f_in), t(f_in + 5), t(f_out), t(f_out + TXT_OUT)], values=[0, 100, 100, 0])
        self.key(nm, 'position', [f_out, f_out + TXT_OUT], [[cx, cy], [cx, cy - SUBE_OUT]])

    def barra(self, top, alto):
        self.add('addShape', shape='rectangle', size=[BAR_W, alto], fillColor=BAR_C, name='barra')
        self.add('setLayerProperty', layer='barra', property='anchorPoint', value=[0, -alto / 2.0])
        self.add('setLayerProperty', layer='barra', property='position', value=[BAR_X + BAR_W / 2.0, top])
        n = self.n
        self.key('barra', 'scale', [0, 10, n - 10, n], [[100, 0], [100, 100], [100, 100], [100, 0]])

    def sombra(self):
        self.add('addAdjustmentLayer', name='sombra')
        self.add('addEffect', layer='sombra', matchName='ADBE Drop Shadow', name='ambiental')
        self.add('addEffect', layer='sombra', matchName='ADBE Drop Shadow', name='contacto')
        for ef, op, dist, soft in (('ambiental', 0.62, 0, 34), ('contacto', 0.66, 4, 10)):
            for prm, v in (('Shadow Color', [0, 0, 0]), ('Opacity', 255 * op), ('Direction', 180),
                           ('Distance', dist), ('Softness', soft)):
                self.add('setEffectParam', layer='sombra', effect=ef, param=prm, value=v)


def salidas(n, cuantos):
    """Cuadro de salida de cada elemento, como cartones_v3 (escalonado 2 f)."""
    return [n - TXT_OUT - (cuantos - 1) * RET_OUT + i * RET_OUT for i in range(cuantos)]


def mg_act(nombre, n, d):
    """Ícono + «Actividad n» en una fila (como las filas de la lista), y debajo
    el título y el cuerpo con la maqueta de los cartones."""
    resto, total = maquetar([(d['titulo'], 'bold', P.TIT, 0),
                             (d['cuerpo'], 'med', P.CUE, P.GAP_CUE + 8)], MAXW)
    alto = ICON_ACT + P.GAP_ANTE + total
    off = BASE_Y - alto
    c = Comp(nombre, n)
    c.barra(off - BAR_PAD, alto + 2 * BAR_PAD)
    out = salidas(n, 2 + len(resto))
    c.icono(d['icono'], TEXT_X + ICON_ACT / 2.0, off + ICON_ACT / 2.0, ICON_ACT, 3, out[0])
    ft = ImageFont.truetype(TTF['med'], P.ANTE)
    alto_mayus = -ft.getbbox('A', anchor='ls')[1]
    ante = {'text': d['ante'], 'peso': 'med', 'px': P.ANTE}
    c.texto(TEXT_X + ICON_ACT + GAP_ICON, off + ICON_ACT / 2.0 + alto_mayus / 2.0, ante, 6, out[1])
    y0 = off + ICON_ACT + P.GAP_ANTE
    for i, ln in enumerate(resto):
        c.texto(TEXT_X, y0 + ln['base'], ln, 9 + i * RET_IN, out[2 + i])
    c.sombra()
    return c, off - BAR_PAD


def mg_lista(nombre, n, ini, d):
    tit, th = maquetar([(d['titulo'], 'bold', P.TIT, 0)], MAXW)
    x_lab = TEXT_X + ICON_FILA + GAP_FILA
    filas = []
    for ico, rotulo, cuadro in d['filas']:
        lab, lh = maquetar([(rotulo, 'med', P.CUE, 0)], MAXW - ICON_FILA - GAP_FILA)
        filas.append((ico, lab, lh, max(ICON_FILA, lh), max(14, cuadro - ini)))
    alto = th + P.GAP_TIT + sum(f[3] for f in filas) + SEP_FILA * (len(filas) - 1)
    off = BASE_Y - alto
    c = Comp(nombre, n)
    c.barra(off - BAR_PAD, alto + 2 * BAR_PAD)
    elementos = len(tit) + sum(1 + len(f[1]) for f in filas)
    out = salidas(n, elementos)
    k = 0
    for i, ln in enumerate(tit):
        c.texto(TEXT_X, off + ln['base'], ln, 6 + i * RET_IN, out[k]); k += 1
    y = off + th + P.GAP_TIT
    for ico, lab, lh, rh, fr in filas:
        c.icono(ico, TEXT_X + ICON_FILA / 2.0, y + rh / 2.0, ICON_FILA, fr, out[k]); k += 1
        ytxt = y + (rh - lh) / 2.0
        for j, ln in enumerate(lab):
            c.texto(x_lab, ytxt + ln['base'], ln, fr + 3 + j * 2, out[k]); k += 1
        y += rh + SEP_FILA
    c.sombra()
    return c, off - BAR_PAD


def nombre_comp(u, clave):
    return 'MA_U%d_%s' % (u, clave)


def items(unidades):
    for u in unidades:
        for clave, tipo, ini, dur, d in P.UNIDADES[u]['items']:
            if tipo in ('mg_act', 'mg_lista'):
                yield u, clave, tipo, ini, dur, d


def armar(unidades):
    info = cmd('getProjectInfo', {})
    if not info.get('path'):
        cmd('saveProject', {'path': AEP})
    r = cmd('getProjectItems', {})
    existentes = {it['name']: it for it in (r['items'] if isinstance(r, dict) else r)}
    if 'PRUEBA' in existentes:
        cmd('deleteItem', {'itemName': 'PRUEBA'})
    usados = sorted({ico for _u, _c, tipo, _i, _d, d in items(unidades)
                     for ico in ([d['icono']] if tipo == 'mg_act' else [f[0] for f in d['filas']])})
    for ico in usados:
        if 'ico_' + ico not in existentes:
            cmd('importFootage', {'path': '%s/%s.png' % (ICONOS, ico), 'name': 'ico_' + ico})
    for u, clave, tipo, ini, dur, d in items(unidades):
        nm = nombre_comp(u, clave)
        if nm in existentes:
            cmd('deleteItem', {'itemName': nm})
        if tipo == 'mg_act':
            c, cima = mg_act(nm, dur, d)
        else:
            c, cima = mg_lista(nm, dur, ini, d)
        batch(c.c)
        print('U%d %-26s %4d f  %3d capas  cima %d%s' % (
            u, clave, dur, c.k, cima, '  <-- SE SUBE DE LA ZONA' if cima < 250 else ''), flush=True)
    cmd('saveProject', {'path': AEP})
    print('ARMADO', flush=True)


def render(unidades):
    for u, clave, tipo, ini, dur, d in items(unidades):
        nm = nombre_comp(u, clave)
        dst = '%s/UNIDAD %d/02 CARTONES/mg' % (CURSO, u)
        os.makedirs(dst, exist_ok=True)
        out = '%s/%s.mov' % (dst, nm)
        t0 = time.time()
        r = subprocess.run([AERENDER, '-project', AEP.replace('/', '\\'), '-comp', nm,
                            '-OMtemplate', OM, '-output', out.replace('/', '\\')],
                           capture_output=True, text=True, errors='replace')
        ok = os.path.exists(out) and os.path.getsize(out) > 0
        print('U%d %-26s %s %.0f s %s' % (u, clave, 'OK' if ok else 'FALLA', time.time() - t0,
                                          '' if ok else r.stdout[-600:]), flush=True)
    print('RENDER LISTO', flush=True)


if __name__ == '__main__':
    accion = sys.argv[1]
    unidades = [int(x) for x in sys.argv[2:]] or [2, 3, 4, 5]
    {'armar': armar, 'render': render}[accion](unidades)
