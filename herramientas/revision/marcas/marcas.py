# -*- coding: utf-8 -*-
"""Marcas de revisión «hechas a mano» sobre los pantallazos de los Genially (círculos, tachones, flechas, notas).

Cada pantallazo (1280 × 720) viene con su JSON de cajas (pantallazos.py): textos e imágenes de la página y de cada
iframe, que acá se pasan a coordenadas de la imagen para ubicar las marcas.

Marcas (lista por diapositiva):
  ('c', blanco, nota)            círculo alrededor del blanco, con nota y flecha
  ('x', blanco, nota)            tachón (X) sobre el blanco
  ('s', blanco, nota)            subrayado
  ('f', blanco, destino, nota)   flecha del blanco hacia el destino («mover a…», «unir con…»)
  ('+', blanco, nota)            recuadro punteado: «falta…», «va aquí…»
blanco: 'texto a buscar' · 'zona:titulo|escena|ilus|todo|cabecera|pie|centro|der|izq|arriba|abajo|sig|ant'
        · (x, y, w, h) en píxeles · ['texto1', 'texto2'] (unión).
"""
import json, math, os, random, re, unicodedata
from PIL import Image, ImageDraw, ImageFont, ImageFilter

AQUI = os.path.dirname(os.path.abspath(__file__))
ROJO = (222, 29, 36)
ESC = 2                       # sobremuestreo para que el trazo salga suave
W, H = 1280, 720
FUENTE = os.path.join(AQUI, 'fuentes', 'Kalam-Bold.ttf')


def norm(s):
    s = unicodedata.normalize('NFKC', s or '').lower()
    s = re.sub(r'[«»"“”\'‘’…\.\,\:\;]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


# ---------------------------------------------------------------- cajas
def cajas(js):
    """Textos e imágenes en coordenadas de la imagen."""
    tex, img, marcos = [], [], []
    for fr in js.get('frames', []):
        if 'w' not in fr:
            continue
        if fr.get('quad'):
            xs, ys = fr['quad'][0::2], fr['quad'][1::2]
            ox, oy = min(xs), min(ys)
            sc = (max(xs) - min(xs)) / max(1, fr['w'])
            marcos.append((ox, oy, max(xs) - ox, max(ys) - oy))
        else:
            ox = oy = 0
            sc = 1
        for t in fr.get('t', []):
            if re.match(r'^Page \d+ of \d+', t['t']):
                continue
            b = (ox + t['x'] * sc, oy + t['y'] * sc, t['w'] * sc, t['h'] * sc)
            if b[0] > W or b[1] > H or b[0] + b[2] < 0 or b[1] + b[3] < 0:
                continue
            tex.append(dict(t=t['t'], b=b, fs=t.get('fs', 12) * sc, marco=bool(fr.get('quad'))))
        for i in fr.get('im', []):
            b = (ox + i['x'] * sc, oy + i['y'] * sc, i['w'] * sc, i['h'] * sc)
            img.append(dict(k=i['k'], b=b, src=i.get('src', ''), marco=bool(fr.get('quad'))))
    return tex, img, marcos


def union(bs):
    x0 = min(b[0] for b in bs); y0 = min(b[1] for b in bs)
    x1 = max(b[0] + b[2] for b in bs); y1 = max(b[1] + b[3] for b in bs)
    return (x0, y0, x1 - x0, y1 - y0)


def recorta(b, m=0):
    x0, y0 = max(m, b[0]), max(m, b[1])
    x1, y1 = min(W - m, b[0] + b[2]), min(H - m, b[1] + b[3])
    return (x0, y0, max(8, x1 - x0), max(8, y1 - y0))


ZONAS = {'todo': (40, 120, 1200, 520), 'cabecera': (0, 0, 1280, 108), 'pie': (20, 630, 1240, 85),
         'centro': (320, 180, 640, 360), 'der': (700, 130, 540, 480), 'izq': (40, 130, 560, 480),
         'arriba': (40, 115, 1200, 220), 'abajo': (40, 400, 1200, 220)}


def blanco(b, tex, img, marcos):
    if isinstance(b, (tuple, list)) and len(b) == 4 and all(isinstance(v, (int, float)) for v in b):
        return tuple(b)
    if isinstance(b, list):
        bs = [blanco(x, tex, img, marcos) for x in b]
        bs = [x for x in bs if x]
        return union(bs) if bs else None
    if b.startswith('zona:'):
        z = b[5:]
        if z in ZONAS:
            return ZONAS[z]
        if z == 'escena':
            ms = [m for m in marcos if m[2] > 300]
            return recorta(max(ms, key=lambda m: m[2] * m[3]), 6) if ms else ZONAS['todo']
        if z == 'video':
            c = [i for i in img if i['k'] == 'video' and i['b'][2] > 150] or \
                [i for i in img if i['k'] == 'iframe' and i['b'][2] > 150]
            return recorta(max(c, key=lambda i: i['b'][2] * i['b'][3])['b'], 6) if c else None
        if z == 'titulo':
            enc = [t for t in tex if not t['marco'] and 108 < t['b'][1] < 165 and 90 < t['b'][0] < 140]
            if enc:
                return union([t['b'] for t in enc])
            c = [t for t in tex if 110 < t['b'][1] < 600 and t['b'][2] > 40]
            if not c:
                return None
            fs = max(t['fs'] for t in c)
            tops = [t for t in c if t['fs'] >= fs * 0.9]
            return union([t['b'] for t in tops])
        if z == 'ilus':
            c = [i for i in img if i['k'] in ('img', 'svg') and 110 < i['b'][1] + i['b'][3] / 2 < 640
                 and 60 < i['b'][2] < 900 and i['b'][3] > 80]
            return max(c, key=lambda i: i['b'][2] * i['b'][3])['b'] if c else None
        if z == 'sig':
            return (1150, 300, 110, 120)
        if z == 'ant':
            return (20, 300, 110, 120)
        return None
    q = norm(b)
    hall = [t for t in tex if q in norm(t['t'])]
    if not hall:
        # coincidencia por palabras (por si el texto quedó partido en dos cajas)
        pal = q.split()
        hall = [t for t in tex if len(pal) > 1 and norm(t['t']).startswith(' '.join(pal[:2]))]
    if not hall:
        return None
    fuera_cab = [t for t in hall if t['marco'] or t['b'][1] > 105]
    hall = fuera_cab or hall
    hall.sort(key=lambda t: (t['b'][1], t['b'][0]))
    t = hall[0]
    bx = t['b']
    # si el texto buscado es una parte de una caja larga, achicar a la línea aproximada
    return recorta(bx, 2)


# ---------------------------------------------------------------- trazos
def _linea(d, pts, w):
    d.line([(x * ESC, y * ESC) for x, y in pts], fill=ROJO + (255,), width=int(w * ESC), joint='curve')
    r = w * ESC / 2
    for x, y in (pts[0], pts[-1]):
        d.ellipse((x * ESC - r, y * ESC - r, x * ESC + r, y * ESC + r), fill=ROJO + (255,))


def recuadro(d, b, rnd, w=5):
    """Rectángulo redondeado a mano, para blancos grandes (una elipse se saldría del cuadro)."""
    x, y, bw, bh = b
    m = 8
    x0, y0 = max(6, x - m), max(6, y - m)
    x1, y1 = min(W - 6, x + bw + m), min(H - 6, y + bh + m)
    r = min(28, (x1 - x0) / 6, (y1 - y0) / 6)
    pts = []
    def arco(cx, cy, a0):
        for i in range(7):
            a = a0 + math.pi / 2 * i / 6
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    def lado(p, q):
        for i in range(1, 12):
            t = i / 12
            pts.append((p[0] + (q[0] - p[0]) * t + rnd.gauss(0, 0.8), p[1] + (q[1] - p[1]) * t + rnd.gauss(0, 0.8)))
    arco(x0 + r, y0 + r, math.pi); lado((x0 + r, y0), (x1 - r, y0))
    arco(x1 - r, y0 + r, -math.pi / 2); lado((x1, y0 + r), (x1, y1 - r))
    arco(x1 - r, y1 - r, 0); lado((x1 - r, y1), (x0 + r, y1))
    arco(x0 + r, y1 - r, math.pi / 2); lado((x0, y1 - r), (x0, y0 + r))
    pts += [(x0 + r * 0.3, y0 + 3), (x0 + r + 40, y0 - 4)]       # el trazo se pasa un poco al cerrar
    _linea(d, pts, w)
    return (x0, y0, x1 - x0, y1 - y0)


def elipse(d, b, rnd, w=5):
    x, y, bw, bh = b
    cx, cy = x + bw / 2, y + bh / 2
    rx = bw / 2 * 1.12 + 12
    ry = bh / 2 * 1.25 + 10
    ini = rnd.uniform(0, 2 * math.pi)
    tot = 2 * math.pi * rnd.uniform(1.08, 1.16)
    rot = rnd.uniform(-0.05, 0.05)
    ph = rnd.uniform(0, 6)
    pts = []
    n = 120
    for i in range(n + 1):
        t = ini + tot * i / n
        k = 1 + 0.035 * math.sin(2 * t + ph) + 0.07 * i / n
        px, py = rx * k * math.cos(t), ry * k * math.sin(t)
        pts.append((cx + px * math.cos(rot) - py * math.sin(rot), cy + px * math.sin(rot) + py * math.cos(rot)))
    _linea(d, pts, w)
    return (cx, cy, rx * 1.07, ry * 1.07)


def curva(p0, p1, rnd, comba=0.12, n=40):
    (x0, y0), (x1, y1) = p0, p1
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1
    s = rnd.choice((-1, 1)) * comba * L
    cx, cy = (x0 + x1) / 2 - dy / L * s, (y0 + y1) / 2 + dx / L * s
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append(((1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t * t * x1 + rnd.gauss(0, 0.35),
                    (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t * t * y1 + rnd.gauss(0, 0.35)))
    return pts


def flecha(d, p0, p1, rnd, w=4.5):
    pts = curva(p0, p1, rnd)
    _linea(d, pts, w)
    (xa, ya), (xb, yb) = pts[-4], pts[-1]
    ang = math.atan2(yb - ya, xb - xa)
    for s in (1, -1):
        a = ang + math.pi - s * rnd.uniform(0.42, 0.55)
        L = rnd.uniform(17, 22)
        _linea(d, [(xb, yb), (xb + L * math.cos(a), yb + L * math.sin(a))], w)


def tachon(d, b, rnd, w=5):
    x, y, bw, bh = b
    m = 6
    _linea(d, curva((x - m, y - m), (x + bw + m, y + bh + m), rnd, 0.04), w)
    _linea(d, curva((x + bw + m, y - m), (x - m, y + bh + m), rnd, 0.04), w)


def subraya(d, b, rnd, w=5):
    x, y, bw, bh = b
    _linea(d, curva((x - 4, y + bh + 5), (x + bw + 6, y + bh + 3), rnd, 0.03), w)
    _linea(d, curva((x + 6, y + bh + 11), (x + bw - 4, y + bh + 10), rnd, 0.02), w * 0.8)


def punteado(d, b, rnd, w=4):
    x, y, bw, bh = b
    lados = [((x, y), (x + bw, y)), ((x + bw, y), (x + bw, y + bh)), ((x + bw, y + bh), (x, y + bh)), ((x, y + bh), (x, y))]
    for p0, p1 in lados:
        L = math.hypot(p1[0] - p0[0], p1[1] - p0[1])
        k = max(1, int(L / 22))
        for i in range(k):
            if i % 2:
                continue
            a, bb = i / k, min(1, (i + 1) / k)
            q0 = (p0[0] + (p1[0] - p0[0]) * a + rnd.gauss(0, .6), p0[1] + (p1[1] - p0[1]) * a + rnd.gauss(0, .6))
            q1 = (p0[0] + (p1[0] - p0[0]) * bb, p0[1] + (p1[1] - p0[1]) * bb)
            _linea(d, [q0, q1], w)
    cx, cy = x + bw / 2, y + bh / 2
    s = min(22, bw / 4, bh / 4)
    _linea(d, [(cx - s, cy), (cx + s, cy)], 6)
    _linea(d, [(cx, cy - s), (cx, cy + s)], 6)


# ---------------------------------------------------------------- notas
def _envolver(texto, f, ancho):
    pal, lin, act = texto.split(), [], ''
    for p in pal:
        prueba = (act + ' ' + p).strip()
        if f.getlength(prueba) <= ancho or not act:
            act = prueba
        else:
            lin.append(act); act = p
    if act:
        lin.append(act)
    return lin


def nota_img(texto, rnd, tam=28, ancho=360):
    texto = texto.replace('«', '“').replace('»', '”').replace('→', '>')
    f = ImageFont.truetype(FUENTE, tam * ESC)
    lin = _envolver(texto, f, ancho * ESC)
    asc, desc = f.getmetrics()
    lh = int((asc + desc) * 0.92)
    tw = int(max(f.getlength(l) for l in lin))
    pad = 12 * ESC
    im = Image.new('RGBA', (tw + 2 * pad + 8 * ESC, lh * len(lin) + 2 * pad - int(desc * .4)), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((2, 2, im.width - 3, im.height - 3), radius=14 * ESC, fill=(255, 255, 255, 238),
                        outline=ROJO + (255,), width=3 * ESC)
    for i, l in enumerate(lin):
        d.text((pad, pad - int(desc * .25) + i * lh), l, font=f, fill=ROJO + (255,))
    ang = rnd.uniform(-2.2, 2.2)
    return im.rotate(ang, resample=Image.BICUBIC, expand=True)


def solapa(a, b):
    w = min(a[0] + a[2], b[0] + b[2]) - max(a[0], b[0])
    h = min(a[1] + a[3], b[1] + b[3]) - max(a[1], b[1])
    return max(0, w) * max(0, h)


def ubicar(nw, nh, objetivo, ocupado, tex):
    """Lugar para la nota (nw × nh px) cerca del objetivo, sin pisar otras notas y tapando poco texto."""
    x, y, bw, bh = objetivo
    cx, cy = x + bw / 2, y + bh / 2
    m = 26
    cand = []
    for px, py in [(cx - nw / 2, y - nh - m - 14), (cx - nw / 2, y + bh + m + 14), (x + bw + m + 22, cy - nh / 2),
                   (x - nw - m - 22, cy - nh / 2), (x + bw + m, y - nh - m), (x - nw - m, y - nh - m),
                   (x + bw + m, y + bh + m), (x - nw - m, y + bh + m), (cx - nw / 2, cy - nh / 2)]:
        px = min(max(8, px), W - nw - 8)
        py = min(max(8, py), H - nh - 8)
        cand.append((px, py))
    def coste(p):
        r = (p[0], p[1], nw, nh)
        c = sum(solapa(r, o) for o in ocupado) * 50
        c += solapa(r, (x - 10, y - 10, bw + 20, bh + 20)) * 3
        c += sum(solapa(r, t['b']) for t in tex)
        c += math.hypot(p[0] + nw / 2 - cx, p[1] + nh / 2 - cy) * 4
        return c
    return min(cand, key=coste)


def borde_elipse(e, p):
    cx, cy, rx, ry = e
    a = math.atan2((p[1] - cy) / ry, (p[0] - cx) / rx)
    return (cx + rx * math.cos(a), cy + ry * math.sin(a))


def borde_caja(r, p):
    x, y, w, h = r
    cx, cy = x + w / 2, y + h / 2
    dx, dy = p[0] - cx, p[1] - cy
    if dx == 0 and dy == 0:
        return (cx, cy)
    s = min(w / 2 / abs(dx) if dx else 1e9, h / 2 / abs(dy) if dy else 1e9)
    return (cx + dx * s, cy + dy * s)


# ---------------------------------------------------------------- dibujo
def marcar(png, js, marcas, salida, semilla=0):
    base = Image.open(png).convert('RGBA')
    if base.size != (W, H):
        base = base.resize((W, H), Image.LANCZOS)
    tex, img, marcos = cajas(js)
    capa = Image.new('RGBA', (W * ESC, H * ESC), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    rnd = random.Random(semilla)
    notas, ocupado, faltan = [], [], []
    for m in marcas:
        tipo = m[0]
        b = blanco(m[1], tex, img, marcos)
        if b is None:
            faltan.append(m[1])
            b = ZONAS['centro']
        nota = m[-1] if len(m) > 2 else None
        b = recorta(b, 4)
        if tipo == 'c' and (b[2] > 620 or b[3] > 300):
            r = recuadro(d, b, rnd)
            obj, ancla = r, ('r', r)
        elif tipo == 'c':
            e = elipse(d, b, rnd)
            obj, ancla = (e[0] - e[2], e[1] - e[3], 2 * e[2], 2 * e[3]), ('e', e)
        elif tipo == 'x':
            tachon(d, b, rnd)
            obj, ancla = b, ('r', b)
        elif tipo == 's':
            subraya(d, b, rnd)
            obj, ancla = (b[0], b[1], b[2], b[3] + 12), ('r', (b[0], b[1] + b[3], b[2], 12))
        elif tipo == '+':
            punteado(d, b, rnd)
            obj, ancla = b, ('r', b)
        elif tipo == 'f':
            if m[2] in ('zona:sig', 'zona:ant'):
                cy = b[1] + b[3] / 2
                dst = (W - 60, cy - 22, 44, 44) if m[2] == 'zona:sig' else (16, cy - 22, 44, 44)
                if m[2] == 'zona:sig' and b[0] + b[2] > W - 150:
                    dst = (W - 60, min(H - 60, b[1] + b[3] + 60), 44, 44)
            else:
                dst = blanco(m[2], tex, img, marcos) or ZONAS['centro']
            if b[2] > 620 or b[3] > 300:
                r = recuadro(d, b, rnd, 4)
                p0 = borde_caja(r, (dst[0] + dst[2] / 2, dst[1] + dst[3] / 2))
                p1 = borde_caja(recorta(dst, 6), (r[0] + r[2] / 2, r[1] + r[3] / 2))
                obj, ancla = r, ('r', r)
            else:
                e = elipse(d, b, rnd, 4)
                p0 = borde_elipse(e, (dst[0] + dst[2] / 2, dst[1] + dst[3] / 2))
                p1 = borde_caja(recorta(dst, 6), (e[0], e[1]))
                obj, ancla = (e[0] - e[2], e[1] - e[3], 2 * e[2], 2 * e[3]), ('e', e)
            flecha(d, p0, p1, rnd, 5)
        else:
            continue
        ocupado.append(obj)
        if nota:
            notas.append((nota, obj, ancla))
    capa_n = Image.new('RGBA', (W * ESC, H * ESC), (0, 0, 0, 0))
    for texto, obj, ancla in notas:
        ni = nota_img(texto, rnd)
        nw, nh = ni.width / ESC, ni.height / ESC
        px, py = ubicar(nw, nh, obj, ocupado, tex)
        r = (px, py, nw, nh)
        ocupado.append(r)
        centro = (px + nw / 2, py + nh / 2)
        pa = borde_elipse(ancla[1], centro) if ancla[0] == 'e' else borde_caja(ancla[1], centro)
        if solapa(r, obj) < 0.2 * nw * nh and math.hypot(pa[0] - centro[0], pa[1] - centro[1]) > 40:
            pn = borde_caja((px - 4, py - 4, nw + 8, nh + 8), pa)
            flecha(d, pn, pa, rnd, 4)
        capa_n.alpha_composite(ni, (int(px * ESC), int(py * ESC)))
    sombra = capa.split()[3].filter(ImageFilter.GaussianBlur(3 * ESC)).point(lambda v: int(v * 0.35))
    halo = Image.new('RGBA', capa.size, (255, 255, 255, 0))
    halo.putalpha(sombra)
    todo = Image.alpha_composite(halo, capa)
    todo.alpha_composite(capa_n)
    todo = todo.resize((W, H), Image.LANCZOS)
    out = Image.alpha_composite(base, todo).convert('RGB')
    out.save(salida, optimize=True)
    return faltan
