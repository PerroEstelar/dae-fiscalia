# -*- coding: utf-8 -*-
r"""Motion graphics de datos de Delitos contra el medio ambiente (V5).

    python mg_da.py V01                      rinde todos, en 09 MOTION GRAPHICS
    python mg_da.py V01 aluvion ideam        solo esos
    python mg_da.py V01 --voces D --sal S    (fuera de la maquina: otra raiz)
    python mg_da.py V01 --muestra            un PNG por grafico, sin video

POR QUE GRAFICOS Y NO CARTONES
    Las cifras del V01 son lo que el espectador tiene que poder recordar
    (118.410 ha de EVOA, 75 % ilicita, 119.483 ha deforestadas, ~2 de cada 3
    en la Amazonia, 85,6 % de los municipios con grupo armado). Un carton
    las dice; un grafico las MUESTRA: la cifra cuenta, los cuadros se
    llenan, la Amazonia se ilumina en el mapa. Y la lista de los seis
    motores entra item por item mientras debajo pasa la placa de cada uno.

EL ESTILO, EL DE LA SERIE
    Montserrat blanca, filete #FEB900 de 14 px en x=175 y texto desde x=243
    (rejilla A), y un panel azul noche #002048 -el del intro oficial-, denso
    a la izquierda (0,80) y ralo a la derecha (0,32): la placa se sigue
    viendo detras. Sin mayusculas sostenidas. Las cifras con punto de mil y
    coma decimal, el % separado.

EL TIEMPO SALE DE LA VOZ
    Cada elemento entra en el cuadro en que Scribe oye su palabra (las STT de
    03 VOCES/stt): el contador arranca cuando la voz dice la cifra, los
    cuadros se llenan con «tres de cada cuatro», cada motor cuando se lo
    nombra. Entra en 10 cuadros subiendo 14 px; el grafico sale en 7.

SALIDA
    09 MOTION GRAPHICS/DA_<V>_mg_<clave>.mov (qtrle argb, como los cartones)
    09 MOTION GRAPHICS/DA_<V>_mg.json  [{clave, archivo, ini, cuadros}], ini
    en cuadros de la linea desde 0 (intro incluida). `da_pieza.capas` y
    `cartones_da` lo leen.
"""
import glob
import json
import math
import os
import re
import subprocess
import sys
import unicodedata

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1920, 1080
FPS = 24000 / 1001.0
CABEZA = 182 + 119
AZUL = (0, 32, 72)
AMARILLO = (254, 185, 0)
BLANCO = (255, 255, 255)
BARRA_X, TEXTO_X, BARRA_W = 175, 243, 14
ENTRA, SUBE, SALE = 10, 14, 7

# las de los cartones primero (`cartones/fuentes`, las tres de la serie)
FUENTES = [os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'cartones', 'fuentes'),
           r'C:\Windows\Fonts', os.path.expanduser(r'~\AppData\Local\Microsoft\Windows\Fonts'),
           '/usr/share/fonts/truetype/montserrat']


def fuente(peso, tam):
    for d in FUENTES:
        p = os.path.join(d, 'Montserrat-%s.ttf' % peso)
        if os.path.exists(p):
            return ImageFont.truetype(p, tam)
    raise SystemExit('falta Montserrat-%s' % peso)


# ------------------------------------------------------------------ tiempo
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.findall(r'[a-z0-9]+', s)


class Voz:
    def __init__(self, clave, voces):
        self.clave, self.voces = clave, voces
        rej = json.load(open(os.path.join(voces, 'DA_%s_rejilla.json' % clave), encoding='utf-8'))
        self.tr = {t['bloque']: t for t in rej['tramos']}

    def cuadro(self, bloque, palabras, n=0):
        """Cuadro de la linea en que se oye la n-esima aparicion de
        `palabras` (normalizadas) dentro del bloque."""
        f = (glob.glob(os.path.join(self.voces, 'stt', 'DA_%s_*_%s.json' % (self.clave, bloque)))
             or glob.glob(os.path.join(self.voces, 'DA_%s_*_%s.json' % (self.clave, bloque))))[0]
        ws = []
        for x in json.load(open(f, encoding='utf-8'))['words']:
            if x.get('type') == 'word':
                for tok in norm(x['text']):
                    ws.append((x['start'], tok))
        q = norm(palabras)
        hits = [k for k in range(len(ws) - len(q) + 1) if [t for _, t in ws[k:k + len(q)]] == q]
        assert len(hits) > n, (bloque, palabras, 'no esta en Scribe')
        return CABEZA + int(round((self.tr[bloque]['entra'] + ws[hits[n]][0]) * FPS))

    def ranura(self, escenas, n):
        """(ini, fin) de la ranura n en cuadros de la linea."""
        t = CABEZA
        for k in sorted(escenas.R):
            if k == n:
                return t, t + escenas.R[k][0]
            t += escenas.R[k][0]
        raise KeyError(n)


# --------------------------------------------------------------- utileria
def suave(x):
    x = min(1.0, max(0.0, x))
    return 1 - (1 - x) ** 3


def panel(denso=0.80, ralo=0.32, desde=760, hasta=1500):
    a = np.full((H, W), ralo, np.float32)
    x = np.arange(W, dtype=np.float32)
    t = np.clip((x - desde) / float(hasta - desde), 0, 1)
    t = t * t * (3 - 2 * t)
    a[:] = denso + (ralo - denso) * t
    im = np.zeros((H, W, 4), np.uint8)
    im[..., :3] = AZUL
    im[..., 3] = np.clip(a * 255, 0, 255).astype(np.uint8)
    return Image.fromarray(im, 'RGBA')


def sprite(texto, f, color=BLANCO, sombra=0.55, ancho=None, salto=None):
    """Un texto (con su sombra suave) como RGBA recortado; con `ancho` parte en
    renglones. Devuelve (imagen, (dx, dy)) con el origen del texto."""
    lineas = texto.split('\n')
    if ancho:
        d = ImageDraw.Draw(Image.new('RGBA', (8, 8)))
        todas = []
        for par in lineas:
            cur = ''
            for p in par.split():
                prueba = (cur + ' ' + p).strip()
                if d.textlength(prueba, font=f) <= ancho or not cur:
                    cur = prueba
                else:
                    todas.append(cur)
                    cur = p
            todas.append(cur)
        lineas = todas
    asc, desc = f.getmetrics()
    salto = salto or int((asc + desc) * 1.12)
    m = 24
    d0 = ImageDraw.Draw(Image.new('RGBA', (8, 8)))
    wmax = int(max(d0.textlength(l, font=f) for l in lineas)) + 2 * m
    hmax = salto * (len(lineas) - 1) + asc + desc + 2 * m
    txt = Image.new('RGBA', (wmax, hmax), (0, 0, 0, 0))
    d = ImageDraw.Draw(txt)
    for i, l in enumerate(lineas):
        d.text((m, m + i * salto), l, font=f, fill=color + (255,))
    if sombra:
        a = txt.split()[3].filter(ImageFilter.GaussianBlur(7))
        a = a.point(lambda v: int(v * sombra))
        sh = Image.new('RGBA', txt.size, (0, 16, 40, 0))
        sh.putalpha(a)
        base = Image.new('RGBA', txt.size, (0, 0, 0, 0))
        base.alpha_composite(sh, (0, 3))
        base.alpha_composite(txt)
        txt = base
    return txt, (-m, -m), len(lineas)


def pega(cuadro, spr, x, y, op, sube=0):
    im, (dx, dy), _ = spr
    if op <= 0:
        return
    if op < 1:
        im = im.copy()
        im.putalpha(im.split()[3].point(lambda v: int(v * op)))
    cuadro.alpha_composite(im, (int(x + dx), int(y + dy + sube)))


def aparece(i, t0):
    """(opacidad, desplazamiento) de un elemento que entra en t0."""
    k = suave((i - t0) / float(ENTRA))
    return k, int(round(SUBE * (1 - k)))


def miles(n):
    return '{:,}'.format(int(n)).replace(',', '.')


class Grafico:
    """Base: panel, filete, antetitulo, fuente; las subclases dibujan."""
    ante = None
    fuente_txt = None
    denso, ralo = 0.80, 0.32

    def __init__(self, voz, escenas):
        self.v, self.E = voz, escenas
        self.ini, self.fin = self.ventana()
        self.n = self.fin - self.ini
        self.panel = panel(self.denso, self.ralo)
        self.f_ante = fuente('SemiBold', 34)
        self.f_fuente = fuente('Medium', 22)
        self.s_ante = sprite(self.ante, self.f_ante, AMARILLO) if self.ante else None
        self.s_fuente = sprite(self.fuente_txt, self.f_fuente, (225, 230, 240), 0.4) \
            if self.fuente_txt else None
        self.prepara()

    def l(self, cuadro_linea):
        return cuadro_linea - self.ini

    def global_op(self, i):
        return min(suave(i / 8.0), suave((self.n - 1 - i) / float(SALE)))

    def barra(self, c, i, y0, y1, op):
        crece = suave(i / 10.0)
        yb = int(y0 + (y1 - y0) * crece)
        d = ImageDraw.Draw(c)
        d.rectangle([BARRA_X, y0, BARRA_X + BARRA_W - 1, yb], fill=AMARILLO + (int(255 * op),))

    def cuadro(self, i):
        g = self.global_op(i)
        c = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        p = self.panel
        if g < 1:
            p = p.copy()
            p.putalpha(p.split()[3].point(lambda v: int(v * g)))
        c.alpha_composite(p)
        self.dibuja(c, i, g)
        if self.s_fuente:
            pega(c, self.s_fuente, TEXTO_X, 1000, g * 0.85)
        return c


class Aluvion(Grafico):
    """r07: 118.410 ha con evidencias de explotacion de oro de aluvion (EVOA
    2025); tres de cada cuatro, ilicitas."""
    clave = 'aluvion'
    ante = 'Colombia, 2025'
    fuente_txt = 'Fuente: Gobierno nacional y UNODC, EVOA 2025'

    def ventana(self):
        a, b = self.v.ranura(self.E, 7)
        return self.v.cuadro('d03_aluvion', '118') - 9, b

    def prepara(self):
        self.t_num = self.l(self.v.cuadro('d03_aluvion', '118'))
        self.t_ha = self.l(self.v.cuadro('d03_aluvion', 'hectareas'))
        self.t_cap = self.l(self.v.cuadro('d03_aluvion', 'con evidencias'))
        self.t_tres = self.l(self.v.cuadro('d03_aluvion', 'tres de cada'))
        self.t_cada = self.l(self.v.cuadro('d03_aluvion', 'cada cuatro'))
        self.t_cuatro = self.l(self.v.cuadro('d03_aluvion', 'cuatro'))
        self.t_ilic = self.l(self.v.cuadro('d03_aluvion', 'ilicitas'))
        self.f_num = fuente('Bold', 150)
        self.cache = {}
        self.s_ha = sprite('hectáreas', fuente('Bold', 60))
        self.s_cap = sprite('con evidencias de explotación\nde oro de aluvión',
                            fuente('Medium', 42))
        self.s_ilic = sprite('75 % ilícita', fuente('Bold', 54), AMARILLO)

    def num(self, v):
        if v not in self.cache:
            self.cache[v] = sprite(miles(v), self.f_num)
        return self.cache[v]

    def dibuja(self, c, i, g):
        self.barra(c, i, 230, 860, g)
        if self.s_ante:
            o, s = aparece(i, 0)
            pega(c, self.s_ante, TEXTO_X, 228, o * g, s)
        k = suave((i - self.t_num) / 34.0)
        o, s = aparece(i, self.t_num)
        pega(c, self.num(int(round(118410 * k / 10.0)) * 10 if k < 1 else 118410),
             TEXTO_X - 6, 280, o * g, s)
        o, s = aparece(i, self.t_ha)
        pega(c, self.s_ha, TEXTO_X, 450, o * g, s)
        o, s = aparece(i, self.t_cap)
        pega(c, self.s_cap, TEXTO_X, 540, o * g, s)
        # cuatro cuadros; se llenan tres con «tres de cada cuatro»
        d = ImageDraw.Draw(c)
        o, s = aparece(i, self.t_tres)
        if o > 0:
            for q in range(4):
                x0, y0 = TEXTO_X + q * 96, 700 + s
                d.rectangle([x0, y0, x0 + 72, y0 + 72], outline=BLANCO + (int(230 * o * g),),
                            width=4)
            for q, t in enumerate((self.t_tres + 4, self.t_cada + 2, self.t_cuatro)):
                kq = suave((i - t) / 8.0)
                if kq > 0:
                    m = int(round(36 * (1 - kq)))
                    x0, y0 = TEXTO_X + q * 96, 700 + s
                    d.rectangle([x0 + 4 + m, y0 + 4 + m, x0 + 68 - m, y0 + 68 - m],
                                fill=AMARILLO + (int(255 * g),))
        o, s = aparece(i, self.t_ilic)
        pega(c, self.s_ilic, TEXTO_X + 4 * 96 + 18, 700, o * g, s)


class Ideam(Grafico):
    """r12: 119.483 ha de bosque natural perdidas en 2025; casi dos de cada
    tres en la Amazonia. Mapa de departamentos: los seis amazonicos se
    iluminan (es un esquema de la region, no el limite biogeografico)."""
    clave = 'ideam'
    ante = 'Deforestación en Colombia, 2025'
    fuente_txt = 'Fuente: IDEAM, monitoreo de la deforestación 2025'
    ralo = 0.50
    AMAZONIA = {'Amazonas', 'Caquetá', 'Guainía', 'Guaviare', 'Putumayo', 'Vaupés'}

    def ventana(self):
        a, b = self.v.ranura(self.E, 12)
        return self.v.cuadro('d05_bosque', 'perdio') - 4, b

    def prepara(self):
        self.t_num = self.l(self.v.cuadro('d05_bosque', '119'))
        self.t_ha = self.l(self.v.cuadro('d05_bosque', 'hectareas'))
        self.t_casi = self.l(self.v.cuadro('d05_bosque', 'casi dos'))
        self.t_amaz = self.l(self.v.cuadro('d05_bosque', 'amazonia'))
        self.f_num = fuente('Bold', 150)
        self.cache = {}
        self.s_ha = sprite('hectáreas de bosque\nnatural perdidas', fuente('Bold', 50))
        self.s_casi = sprite('casi 2 de cada 3,\nen la Amazonía', fuente('Bold', 50), AMARILLO)
        self.s_lab = sprite('Amazonía', fuente('Bold', 34), (40, 30, 0), sombra=0)
        self.mapa()

    def mapa(self):
        g = json.load(open(GEO, encoding='utf-8'))
        polys = []
        for ft in g['features']:
            nm = ft['properties'].get('name') or ''
            if 'San Andr' in nm:
                continue
            geo = ft['geometry']
            cs = geo['coordinates'] if geo['type'] == 'MultiPolygon' else [geo['coordinates']]
            for poly in cs:
                r = poly[0]
                # sin islas ni cayos (Malpelo, Gorgona, los del Caribe)
                if len(r) < 12 or min(p[0] for p in r) < -79.2:
                    continue
                polys.append((nm in self.AMAZONIA, r))
        lon = [p[0] for _, r in polys for p in r]
        lat = [p[1] for _, r in polys for p in r]
        x0, x1, y0, y1 = min(lon), max(lon), min(lat), max(lat)
        caja = (1160, 120, 1760, 960)
        k = min((caja[2] - caja[0]) / (x1 - x0),
                (caja[3] - caja[1]) / ((y1 - y0) * 1.0))
        ox = caja[0] + ((caja[2] - caja[0]) - (x1 - x0) * k) / 2

        def pr(p):
            return (ox + (p[0] - x0) * k, caja[1] + (y1 - p[1]) * k)
        self.polys = [(a, [pr(p) for p in r]) for a, r in polys]
        am = [pt for a, r in self.polys if a for pt in r]
        self.centro_am = (sum(p[0] for p in am) / len(am), sum(p[1] for p in am) / len(am))
        # dos capas pre-dibujadas: el pais y la Amazonia iluminada
        base = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(base)
        for a, r in self.polys:
            d.polygon(r, fill=(255, 255, 255, 34), outline=(255, 255, 255, 170))
        luz = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(luz)
        for a, r in self.polys:
            if a:
                d.polygon(r, fill=AMARILLO + (235,), outline=(255, 236, 170, 255))
        self.l_base, self.l_luz = base, luz

    def num(self, v):
        if v not in self.cache:
            self.cache[v] = sprite(miles(v), self.f_num)
        return self.cache[v]

    def dibuja(self, c, i, g):
        self.barra(c, i, 230, 860, g)
        o, s = aparece(i, 0)
        pega(c, self.s_ante, TEXTO_X, 228, o * g, s)
        k = suave((i - self.t_num) / 34.0)
        o, s = aparece(i, self.t_num)
        pega(c, self.num(int(round(119483 * k / 10.0)) * 10 if k < 1 else 119483),
             TEXTO_X - 6, 280, o * g, s)
        o, s = aparece(i, self.t_ha)
        pega(c, self.s_ha, TEXTO_X, 450, o * g, s)
        om, _ = aparece(i, 0)
        pega(c, (self.l_base, (0, 0), 1), 0, 0, om * g)
        ol = suave((i - self.t_casi) / 18.0)
        pega(c, (self.l_luz, (0, 0), 1), 0, 0, ol * g)
        o, s = aparece(i, self.t_casi)
        pega(c, self.s_casi, TEXTO_X, 640, o * g, s)
        o, s = aparece(i, self.t_amaz)
        lw = self.s_lab[0].size[0] - 48
        pega(c, self.s_lab, self.centro_am[0] - lw / 2, self.centro_am[1] - 20, o * g, s)


class Motores(Grafico):
    """r13-r18: los seis motores de la deforestacion (U2 L4 3.1 del curso),
    uno por uno cuando la voz los nombra; debajo pasa la placa de cada uno.
    El vigente en blanco, los anteriores atenuados."""
    clave = 'motores'
    ante = 'Motores de la deforestación'
    denso, ralo = 0.70, 0.12
    ITEMS = [('el acaparamiento', 'Acaparamiento de tierras'),
             ('la ganaderia', 'Ganadería extensiva'),
             ('los cultivos', 'Cultivos de uso ilícito'),
             ('la apertura', 'Apertura de vías ilegales'),
             ('la explotacion', 'Explotación ilícita de minerales'),
             ('el aprovechamiento', 'Aprovechamiento ilegal de madera')]

    def ventana(self):
        a, b = self.v.ranura(self.E, 18)
        return self.v.cuadro('d06_motores', 'el acaparamiento') - 6, b

    def prepara(self):
        f = fuente('Bold', 50)
        self.items = [(self.l(self.v.cuadro('d06_motores', q)), sprite(t, f)) for q, t in self.ITEMS]
        self.f_n = fuente('Bold', 30)

    def dibuja(self, c, i, g):
        y0, paso = 300, 100
        self.barra(c, i, 230, y0 + paso * 6 - 20, g)
        o, s = aparece(i, 0)
        pega(c, self.s_ante, TEXTO_X, 228, o * g, s)
        d = ImageDraw.Draw(c)
        vig = max([k for k, (t, _) in enumerate(self.items) if i >= t] or [0])
        for k, (t, spr) in enumerate(self.items):
            o, s = aparece(i, t)
            if o <= 0:
                continue
            y = y0 + k * paso
            tenue = 1.0 if k == vig else 0.55
            cx, cy = TEXTO_X + 22, y + 34 + s
            d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22],
                      fill=(AMARILLO if k == vig else (150, 160, 175)) + (int(255 * o * g),))
            nn = str(k + 1)
            tw = d.textlength(nn, font=self.f_n)
            d.text((cx - tw / 2, cy - 19), nn, font=self.f_n, fill=AZUL + (int(255 * o * g),))
            pega(c, spr, TEXTO_X + 66, y, o * g * tenue, s)


class Municipios(Grafico):
    """r23: 85,6 % de los municipios con EVOA tienen presencia de al menos un
    grupo armado. Diez circulos; se llenan ocho y el 56 % del noveno."""
    clave = 'municipios'
    ante = 'Oro de aluvión y grupos armados'
    fuente_txt = 'Fuente: Gobierno nacional y UNODC, EVOA 2025'

    def ventana(self):
        return self.v.ranura(self.E, 23)

    def prepara(self):
        self.t_mas = self.l(self.v.cuadro('d08_grupos', 'mas de ocho'))
        self.t_mun = self.l(self.v.cuadro('d08_grupos', 'municipios'))
        self.f_num = fuente('Bold', 150)
        self.cache = {}
        self.s_cap = sprite('de los municipios con explotación de oro de aluvión\n'
                            'tienen presencia de al menos un grupo armado',
                            fuente('Medium', 40))

    def num(self, v):
        if v not in self.cache:
            self.cache[v] = sprite(('%.1f' % v).replace('.', ',') + ' %', self.f_num)
        return self.cache[v]

    def dibuja(self, c, i, g):
        self.barra(c, i, 230, 880, g)
        o, s = aparece(i, 0)
        pega(c, self.s_ante, TEXTO_X, 228, o * g, s)
        k = suave((i - self.t_mas) / 30.0)
        o, s = aparece(i, self.t_mas)
        pega(c, self.num(85.6 * k if k < 1 else 85.6), TEXTO_X - 6, 280, o * g, s)
        o, s = aparece(i, self.t_mun)
        pega(c, self.s_cap, TEXTO_X, 455, o * g, s)
        # los diez circulos
        d = ImageDraw.Draw(c)
        oc, sc = aparece(i, self.t_mas)
        r, paso = 34, 92
        for q in range(10):
            cx = TEXTO_X + r + (q % 5) * paso
            cy = 680 + r + (q // 5) * paso + sc
            d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=BLANCO + (int(220 * oc * g),),
                      width=4)
            lleno = 1.0 if q < 8 else (0.56 if q == 8 else 0.0)
            kq = suave((i - self.t_mas - 4 - q * 3) / 8.0) * lleno
            if kq > 0:
                capa = Image.new('RGBA', (2 * r, 2 * r), (0, 0, 0, 0))
                ImageDraw.Draw(capa).ellipse([5, 5, 2 * r - 6, 2 * r - 6],
                                             fill=AMARILLO + (int(255 * g),))
                ancho = int(round(2 * r * kq))
                if ancho > 0:
                    capa = capa.crop((0, 0, ancho, 2 * r))
                    c.alpha_composite(capa, (cx - r, cy - r))


class Cadena(Grafico):
    """r33: subir por la cadena, del eslabon visible a quien promueve,
    financia, dirige y se beneficia. Cada eslabon cuando la voz lo dice."""
    clave = 'cadena'
    ante = 'Subir por la cadena'
    denso, ralo = 0.80, 0.26

    def ventana(self):
        return self.v.ranura(self.E, 33)

    def prepara(self):
        b = 'd12_cadena'
        self.t_subir = self.l(self.v.cuadro(b, 'subir'))
        self.t_hasta = self.l(self.v.cuadro(b, 'hasta'))
        f = fuente('Bold', 52)
        self.base = sprite('el eslabón visible', fuente('Medium', 40), (215, 222, 232))
        self.nodos = [(self.l(self.v.cuadro(b, q)), sprite(t, f)) for q, t in
                      (('promueve', 'Promueve'), ('financia', 'Financia'),
                       ('dirige', 'Dirige'), ('se beneficia', 'Se beneficia'))]

    def dibuja(self, c, i, g):
        o, s = aparece(i, 0)
        pega(c, self.s_ante, BARRA_X, 228, o * g, s)
        d = ImageDraw.Draw(c)
        cx = BARRA_X + 24
        ys = [860, 720, 590, 460, 330]
        # la linea crece de abajo hacia arriba con «subir por la cadena»
        k = suave((i - self.t_subir) / float(max(12, self.t_hasta - self.t_subir + 20)))
        if k > 0:
            ytop = ys[0] - (ys[0] - ys[-1]) * k
            d.rectangle([cx - 3, ytop, cx + 3, ys[0]], fill=AMARILLO + (int(200 * g),))
        o, s = aparece(i, 0)
        d.ellipse([cx - 16, ys[0] - 16 + s, cx + 16, ys[0] + 16 + s],
                  fill=(150, 160, 175, int(255 * o * g)))
        pega(c, self.base, cx + 50, ys[0] - 26, o * g, s)
        for q, (t, spr) in enumerate(self.nodos):
            o, s = aparece(i, t)
            if o <= 0:
                continue
            y = ys[q + 1] + s
            ult = q == len(self.nodos) - 1
            rr = 24 if ult else 20
            d.ellipse([cx - rr, y - rr, cx + rr, y + rr], fill=AMARILLO + (int(255 * o * g),))
            pega(c, spr, cx + 50, y - 34, o * g, 0)


# ------------------------------------------------------------------- V02
# Plan de priorizacion de la FGN. Los textos son los del Direccionamiento
# Estrategico 2024-2028 (pilar, niveles, enfoques), los de la leccion U3 L1
# (programa metodologico, consecuencias) y el articulo 6 de la Constitucion,
# literal. Mismo estilo que los del V01.
FUENTE_DE = 'Fuente: Fiscalía General de la Nación, Direccionamiento Estratégico 2024-2028'
GRIS_TXT = (200, 208, 220)


def sprite_col(texto, f, ancho, color_de, sombra=0.55):
    """Como `sprite`, pero cada palabra con su color: color_de(k) da el color
    de la palabra k (o None para no dibujarla). Mismo reparto de renglones
    para todas las llamadas con el mismo texto."""
    d0 = ImageDraw.Draw(Image.new('RGBA', (8, 8)))
    pal = texto.split()
    esp = d0.textlength(' ', font=f)
    lineas, cur, wcur = [], [], 0
    for k, p in enumerate(pal):
        wp = d0.textlength(p, font=f)
        if cur and wcur + esp + wp > ancho:
            lineas.append(cur)
            cur, wcur = [], 0
        wcur = wcur + (esp if cur else 0) + wp
        cur.append(k)
    lineas.append(cur)
    asc, desc = f.getmetrics()
    salto = int((asc + desc) * 1.18)
    m = 24
    txt = Image.new('RGBA', (int(ancho) + 2 * m, salto * (len(lineas) - 1) + asc + desc + 2 * m),
                    (0, 0, 0, 0))
    d = ImageDraw.Draw(txt)
    for r, ks in enumerate(lineas):
        x = m
        for k in ks:
            col = color_de(k)
            if col:
                d.text((x, m + r * salto), pal[k], font=f, fill=col + (255,))
            x += d0.textlength(pal[k], font=f) + esp
    if sombra:
        a = txt.split()[3].filter(ImageFilter.GaussianBlur(7)).point(lambda v: int(v * sombra))
        sh = Image.new('RGBA', txt.size, (0, 16, 40, 0))
        sh.putalpha(a)
        base = Image.new('RGBA', txt.size, (0, 0, 0, 0))
        base.alpha_composite(sh, (0, 3))
        base.alpha_composite(txt)
        txt = base
    return txt, (-m, -m), len(lineas)


class Pilares(Grafico):
    """r03: el primer pilar del Direccionamiento Estrategico, priorizar con
    enfoque territorial."""
    clave = 'pilares'
    ante = 'Direccionamiento Estratégico 2024-2028'
    fuente_txt = FUENTE_DE
    B = 'e02_pilar'

    def ventana(self):
        return self.v.ranura(self.E, 3)

    def prepara(self):
        self.t_pilar = self.l(self.v.cuadro(self.B, 'primer pilar'))
        self.t_prio = self.l(self.v.cuadro(self.B, 'priorizar las investigaciones'))
        self.t_terr = self.l(self.v.cuadro(self.B, 'enfoque territorial'))
        self.s_pilar = sprite('Primer pilar', fuente('Bold', 76))
        self.s_prio = sprite('Priorizar las investigaciones', fuente('Medium', 48))
        self.s_terr = sprite('con enfoque territorial', fuente('Bold', 58), AMARILLO)

    def dibuja(self, c, i, g):
        self.barra(c, i, 230, 640, g)
        o, s = aparece(i, 0)
        pega(c, self.s_ante, TEXTO_X, 228, o * g, s)
        o, s = aparece(i, self.t_pilar)
        pega(c, self.s_pilar, TEXTO_X - 4, 300, o * g, s)
        o, s = aparece(i, self.t_prio)
        pega(c, self.s_prio, TEXTO_X, 450, o * g, s)
        o, s = aparece(i, self.t_terr)
        pega(c, self.s_terr, TEXTO_X, 530, o * g, s)


class Niveles(Grafico):
    """r05: los tres niveles que trabajan articulados -local, regional,
    nacional-. Un punto que crece por nivel; la linea que los une entra con
    «articulados»; el nivel que se nombra, en blanco, los otros atenuados."""
    clave = 'niveles'
    ante = 'La priorización, en tres niveles'
    fuente_txt = FUENTE_DE
    B = 'e03_niveles'
    ITEMS = [('el local', 'Local', 'En cada Dirección Seccional'),
             ('el regional', 'Regional', 'Varias seccionales y direcciones especializadas'),
             ('el nacional', 'Nacional', 'Fenómenos de impacto en todo el país')]

    def ventana(self):
        return self.v.ranura(self.E, 5)

    def prepara(self):
        self.t_art = self.l(self.v.cuadro(self.B, 'articulados'))
        ft, fs = fuente('Bold', 54), fuente('Medium', 36)
        self.items = [(self.l(self.v.cuadro(self.B, q)), sprite(t, ft), sprite(sub, fs, GRIS_TXT))
                      for q, t, sub in self.ITEMS]

    def dibuja(self, c, i, g):
        y0, paso = 310, 165
        self.barra(c, i, 230, y0 + paso * 3 - 40, g)
        o, s = aparece(i, 0)
        pega(c, self.s_ante, TEXTO_X, 228, o * g, s)
        d = ImageDraw.Draw(c)
        cx = TEXTO_X + 26
        k = suave((i - self.t_art) / 18.0)
        if k > 0:
            ya, yb = y0 + 38, y0 + 38 + int(2 * paso * k)
            d.rectangle([cx - 2, ya, cx + 2, yb], fill=AMARILLO + (int(200 * g),))
        vig = max([q for q, (t, _, _) in enumerate(self.items) if i >= t] or [0])
        for q, (t, st, ss) in enumerate(self.items):
            o, s = aparece(i, t)
            if o <= 0:
                continue
            y = y0 + q * paso
            r = 12 + 6 * q
            tenue = 1.0 if q == vig else 0.55
            col = AMARILLO if q == vig else (150, 160, 175)
            d.ellipse([cx - r, y + 38 - r + s, cx + r, y + 38 + r + s], fill=col + (int(255 * o * g),))
            pega(c, st, TEXTO_X + 76, y, o * g * tenue, s)
            pega(c, ss, TEXTO_X + 78, y + 72, o * g * tenue, s)


class Enfoques(Grafico):
    """r10: los dos enfoques transversales de los planes de priorizacion.
    Entran los dos con «dos enfoques»; con «comprender» se queda el primero
    (la r11, el analista con el extracto, cuenta el segundo)."""
    clave = 'enfoques'
    ante = 'Dos enfoques transversales'
    fuente_txt = FUENTE_DE
    denso, ralo = 0.80, 0.22
    B = 'e05_enfoques'

    def ventana(self):
        return self.v.ranura(self.E, 10)

    def prepara(self):
        self.t_dos = self.l(self.v.cuadro(self.B, 'dos enfoques'))
        self.t_comp = self.l(self.v.cuadro(self.B, 'comprender'))
        ft = fuente('Bold', 54)
        self.s1 = sprite('Delincuencia organizada', ft)
        self.s2 = sprite('Componente financiero', ft)
        self.s1b = sprite('Comprender la criminalidad\nen su relación con ella', fuente('Medium', 38),
                          GRIS_TXT)
        self.f_n = fuente('Bold', 30)

    def dibuja(self, c, i, g):
        self.barra(c, i, 230, 700, g)
        o, s = aparece(i, 0)
        pega(c, self.s_ante, TEXTO_X, 228, o * g, s)
        d = ImageDraw.Draw(c)
        ys = (310, 560)
        for q, (spr, t) in enumerate(((self.s1, self.t_dos), (self.s2, self.t_dos + 8))):
            o, s = aparece(i, t)
            if o <= 0:
                continue
            foco = 1.0 if (i < self.t_comp or q == 0) else 0.45
            cx, cy = TEXTO_X + 22, ys[q] + 34 + s
            col = AMARILLO if (q == 0 or i < self.t_comp) else (150, 160, 175)
            d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=col + (int(255 * o * g),))
            nn = str(q + 1)
            tw = d.textlength(nn, font=self.f_n)
            d.text((cx - tw / 2, cy - 19), nn, font=self.f_n, fill=AZUL + (int(255 * o * g),))
            pega(c, spr, TEXTO_X + 66, ys[q], o * g * foco, s)
        o, s = aparece(i, self.t_comp)
        pega(c, self.s1b, TEXTO_X + 68, ys[0] + 80, o * g, s)


class Programa(Grafico):
    """r13: lo que lleva el programa metodologico, cada casilla con su
    palabra; cierra «Planear, en lugar de improvisar»."""
    clave = 'programa'
    ante = 'Programa metodológico'
    denso, ralo = 0.82, 0.30
    B = 'e06_programa'
    ITEMS = [('hipotesis claras', 'Hipótesis claras'), ('tareas', 'Tareas'),
             ('responsables', 'Responsables'), ('plazos', 'Plazos'),
             ('objetivos probatorios', 'Objetivos probatorios')]

    def ventana(self):
        return self.v.ranura(self.E, 13)

    def prepara(self):
        f = fuente('Bold', 48)
        self.items = [(max(0, self.l(self.v.cuadro(self.B, q))), sprite(t, f)) for q, t in self.ITEMS]
        self.t_plan = self.l(self.v.cuadro(self.B, 'planear'))
        self.s_plan = sprite('Planear, en lugar de improvisar.', fuente('Bold', 54), AMARILLO)

    def dibuja(self, c, i, g):
        y0, paso = 300, 86
        self.barra(c, i, 230, 860, g)
        o, s = aparece(i, 0)
        pega(c, self.s_ante, TEXTO_X, 228, o * g, s)
        d = ImageDraw.Draw(c)
        for q, (t, spr) in enumerate(self.items):
            o, s = aparece(i, t)
            if o <= 0:
                continue
            y = y0 + q * paso + s
            a = int(230 * o * g)
            d.rectangle([TEXTO_X, y + 8, TEXTO_X + 44, y + 52], outline=BLANCO + (a,), width=4)
            # el visto se dibuja en 8 cuadros, despues de la casilla
            k = suave((i - t - 4) / 8.0)
            if k > 0:
                p0, p1, p2 = (TEXTO_X + 9, y + 30), (TEXTO_X + 19, y + 42), (TEXTO_X + 38, y + 16)
                if k < 0.4:
                    u = k / 0.4
                    pts = [p0, (p0[0] + (p1[0] - p0[0]) * u, p0[1] + (p1[1] - p0[1]) * u)]
                else:
                    u = (k - 0.4) / 0.6
                    pts = [p0, p1, (p1[0] + (p2[0] - p1[0]) * u, p1[1] + (p2[1] - p1[1]) * u)]
                d.line(pts, fill=AMARILLO + (int(255 * g),), width=7, joint='curve')
            pega(c, spr, TEXTO_X + 74, y - s, o * g, s)
        o, s = aparece(i, self.t_plan)
        pega(c, self.s_plan, TEXTO_X, y0 + 5 * paso + 40, o * g, s)


class Articulo6(Grafico):
    """r16: el articulo 6 de la Constitucion, literal. La primera oracion
    atenuada; la segunda en blanco con «servidores publicos», y «por omision
    o extralimitacion» se enciende en amarillo cuando la voz lo dice."""
    clave = 'articulo6'
    ante = 'Constitución Política de Colombia, artículo 6'
    B = 'e08_disciplinario'
    O1 = ('Los particulares sólo son responsables ante las autoridades por infringir '
          'la Constitución y las leyes.')
    O2 = ('Los servidores públicos lo son por la misma causa y por omisión o '
          'extralimitación en el ejercicio de sus funciones.')

    def ventana(self):
        return self.v.ranura(self.E, 16)

    def prepara(self):
        self.t_serv = self.l(self.v.cuadro(self.B, 'servidores publicos'))
        self.t_omi = self.l(self.v.cuadro(self.B, 'omision'))
        f1, f2 = fuente('Medium', 40), fuente('SemiBold', 46)
        self.s1 = sprite('«' + self.O1, f1, GRIS_TXT, ancho=1180)
        pal = self.O2.split()
        res = {k for k, p in enumerate(pal) if k >= pal.index('omisión') - 1 and k <= pal.index('extralimitación')}
        self.s2 = sprite_col(self.O2 + '»', f2, 1180, lambda k: BLANCO)
        self.s2r = sprite_col(self.O2 + '»', f2, 1180, lambda k: AMARILLO if k in res else None, sombra=0)
        self.alto1 = self.s1[0].size[1] - 48

    def dibuja(self, c, i, g):
        y2 = 300 + self.alto1 + 40
        self.barra(c, i, 230, y2 + self.s2[0].size[1] - 30, g)
        o, s = aparece(i, 0)
        pega(c, self.s_ante, TEXTO_X, 228, o * g, s)
        pega(c, self.s1, TEXTO_X, 300, o * g, s)
        o, s = aparece(i, self.t_serv)
        pega(c, self.s2, TEXTO_X, y2, o * g, s)
        k = suave((i - self.t_omi) / 10.0)
        if k > 0:
            pega(c, self.s2r, TEXTO_X, y2, k * g, s)


class Consecuencias(Grafico):
    """r20: las cuatro consecuencias de investigar mal, cada una con su
    palabra. La r21 (la fiscal en la sala) entra con «en el juicio oral»."""
    clave = 'consecuencias'
    ante = 'Las consecuencias de investigar mal'
    B = 'e10_consecuencias'
    ITEMS = [('evidencia excluida', 'Evidencia excluida'),
             ('cadenas de custodia', 'Cadenas de custodia rotas'),
             ('nulidades', 'Nulidades'),
             ('hipotesis', 'Hipótesis que no se sostienen en el juicio')]

    def ventana(self):
        return self.v.ranura(self.E, 20)

    def prepara(self):
        f = fuente('Bold', 50)
        self.items = [(max(0, self.l(self.v.cuadro(self.B, q))), sprite(t, f, ancho=1150))
                      for q, t in self.ITEMS]
        self.t_sin = self.l(self.v.cuadro(self.B, 'sin respetar'))
        self.s_sin = sprite('obtenida sin respetar los derechos fundamentales',
                            fuente('Medium', 36), GRIS_TXT)

    def dibuja(self, c, i, g):
        ys = (300, 450, 560, 670)
        self.barra(c, i, 230, 800, g)
        o, s = aparece(i, 0)
        pega(c, self.s_ante, TEXTO_X, 228, o * g, s)
        d = ImageDraw.Draw(c)
        for q, (t, spr) in enumerate(self.items):
            o, s = aparece(i, t)
            if o <= 0:
                continue
            y = ys[q] + s
            d.rectangle([TEXTO_X, y + 28, TEXTO_X + 30, y + 36], fill=AMARILLO + (int(255 * o * g),))
            pega(c, spr, TEXTO_X + 52, ys[q], o * g, s)
        o, s = aparece(i, self.t_sin)
        pega(c, self.s_sin, TEXTO_X + 54, ys[0] + 70, o * g, s)


# ------------------------------------------------------------ V03-V06
# Tres familias genericas, parametrizadas por video:
#   Lista    antetitulo + renglones que entran con su palabra (marca: visto,
#            punto, numero); opcional una cifra grande arriba
#   Rotulo   el rotulo-enlace de una tecnica (V03): un circulo sobre la placa
#            que late y el nombre con su articulo en una caja arriba a la
#            izquierda, sin panel (virtualizacion lo vuelve clic)
#   Tarjeta  el titulo de un paso (V06), con su subtitulo del libreto; las
#            del rompecabezas, las preguntas y la balanza agregan lo suyo


def ventana_de(v, E, n, hasta=None):
    a, b = v.ranura(E, n)
    if hasta:
        b = v.ranura(E, hasta)[1]
    return a, b


class Lista(Grafico):
    B = None            # bloque de voz
    N = None            # ranura (o (desde, hasta))
    ITEMS = []          # [(palabras, texto, sub o None)]
    MARCA = 'punto'     # 'visto' | 'punto' | 'num'
    CIFRA = None        # (palabras, texto) grande arriba, opcional
    CIERRE = None       # (palabras, texto) en amarillo al final, opcional
    TAM = 50
    PASO = 96
    denso, ralo = 0.80, 0.26

    def ventana(self):
        n = self.N if isinstance(self.N, tuple) else (self.N, None)
        return ventana_de(self.v, self.E, *n)

    def t(self, palabras, n=0):
        b, p = palabras if isinstance(palabras, tuple) else (self.B, palabras)
        return max(0, self.l(self.v.cuadro(b, p, n)))

    def prepara(self):
        f, fs = fuente('Bold', self.TAM), fuente('Medium', 34)
        self.items = [(self.t(q), sprite(t, f, ancho=1150), sprite(s, fs, GRIS_TXT) if s else None)
                      for q, t, s in self.ITEMS]
        self.cifra = (self.t(self.CIFRA[0]), sprite(self.CIFRA[1], fuente('Bold', 96), AMARILLO)) \
            if self.CIFRA else None
        self.cierre = (self.t(self.CIERRE[0]), sprite(self.CIERRE[1], fuente('Bold', 52), AMARILLO)) \
            if self.CIERRE else None
        self.f_n = fuente('Bold', 30)

    def dibuja(self, c, i, g):
        y = 300
        if self.cifra:
            o, s = aparece(i, self.cifra[0])
            pega(c, self.cifra[1], TEXTO_X - 4, 280, o * g, s)
            y = 420
        alto = y + self.PASO * len(self.items) + (90 if self.cierre else 0)
        self.barra(c, i, 230, alto - 20, g)
        o, s = aparece(i, 0)
        pega(c, self.s_ante, TEXTO_X, 228, o * g, s)
        d = ImageDraw.Draw(c)
        yy = y
        for q, (t, spr, sub) in enumerate(self.items):
            o, s = aparece(i, t)
            if o > 0:
                a = int(255 * o * g)
                if self.MARCA == 'visto':
                    d.rectangle([TEXTO_X, yy + 8 + s, TEXTO_X + 44, yy + 52 + s], outline=BLANCO + (a,), width=4)
                    k = suave((i - t - 4) / 8.0)
                    if k > 0:
                        p0, p1, p2 = (TEXTO_X + 9, yy + 30 + s), (TEXTO_X + 19, yy + 42 + s), (TEXTO_X + 38, yy + 16 + s)
                        pts = [p0, (p0[0] + (p1[0] - p0[0]) * min(1, k / 0.4), p0[1] + (p1[1] - p0[1]) * min(1, k / 0.4))]
                        if k > 0.4:
                            u = (k - 0.4) / 0.6
                            pts = [p0, p1, (p1[0] + (p2[0] - p1[0]) * u, p1[1] + (p2[1] - p1[1]) * u)]
                        d.line(pts, fill=AMARILLO + (int(255 * g),), width=7, joint='curve')
                elif self.MARCA == 'num':
                    cx, cy = TEXTO_X + 22, yy + 34 + s
                    d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=AMARILLO + (a,))
                    nn = str(q + 1)
                    tw = d.textlength(nn, font=self.f_n)
                    d.text((cx - tw / 2, cy - 19), nn, font=self.f_n, fill=AZUL + (a,))
                else:
                    d.rectangle([TEXTO_X, yy + 28 + s, TEXTO_X + 30, yy + 36 + s], fill=AMARILLO + (a,))
                pega(c, spr, TEXTO_X + 70, yy, o * g, s)
                if sub:
                    pega(c, sub, TEXTO_X + 72, yy + spr[2] * int(self.TAM * 1.2) + 4, o * g, s)
            yy += self.PASO + (spr[2] - 1) * int(self.TAM * 1.2) + (44 if sub else 0)
        if self.cierre:
            o, s = aparece(i, self.cierre[0])
            pega(c, self.cierre[1], TEXTO_X, yy + 20, o * g, s)


class Rotulo(Grafico):
    """V03: el rotulo-enlace de una tecnica. Sin panel: un circulo que late
    sobre lo que la placa muestra de esa tecnica, y arriba a la izquierda una
    caja azul noche con el nombre y el articulo."""
    B = None
    N = None
    PALABRAS = None
    NOMBRE = ''
    ARTICULO = ''
    PUNTO = (960, 540)
    DURA = 150
    denso, ralo = 0.0, 0.0

    def ventana(self):
        a, b = self.v.ranura(self.E, self.N)
        t0 = self.v.cuadro(self.B, self.PALABRAS) - 4
        return max(a, t0), min(b, t0 + self.DURA)

    def prepara(self):
        self.s_nom = sprite(self.NOMBRE, fuente('Bold', 44), ancho=760)
        self.s_art = sprite(self.ARTICULO, fuente('SemiBold', 30), AMARILLO)
        w = max(self.s_nom[0].size[0], self.s_art[0].size[0]) - 48 + 80
        h = self.s_nom[0].size[1] - 48 + 40 + 60
        self.caja = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        ImageDraw.Draw(self.caja).rounded_rectangle([0, 0, w - 1, h - 1], 14, fill=AZUL + (215,))

    def dibuja(self, c, i, g):
        o, s = aparece(i, 0)
        x0, y0 = BARRA_X, 110
        if o > 0:
            cj = self.caja.copy()
            cj.putalpha(cj.split()[3].point(lambda v: int(v * o * g)))
            c.alpha_composite(cj, (x0, y0 + s))
            d = ImageDraw.Draw(c)
            d.rectangle([x0, y0 + s, x0 + BARRA_W - 1, y0 + s + self.caja.size[1] - 1],
                        fill=AMARILLO + (int(255 * o * g),))
            pega(c, self.s_art, x0 + 40, y0 + 18, o * g, s)
            pega(c, self.s_nom, x0 + 40, y0 + 62, o * g, s)
        # el circulo: entra creciendo y despues late despacio
        k = suave((i - 6) / 12.0)
        if k > 0:
            d = ImageDraw.Draw(c)
            px, py = self.PUNTO
            lat = 1 + 0.08 * math.sin((i - 6) / 24.0 * 2 * math.pi)
            for rr, w, a in ((46, 6, 255), (64, 3, 130)):
                r = rr * k * lat
                d.ellipse([px - r, py - r, px + r, py + r], outline=AMARILLO + (int(a * g),), width=w)
            d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=AMARILLO + (int(255 * k * g),))


class Tarjeta(Grafico):
    """V06: el titulo de un paso, con su subtitulo del libreto. Dura lo que
    tarde en leerse (DURA) o la ranura, lo que sea menos."""
    B = None
    N = None
    PASO = 1
    TITULO = ''
    SUB = ''
    DURA = 130
    HASTA = None
    denso, ralo = 0.78, 0.22

    def ventana(self):
        a, b = ventana_de(self.v, self.E, self.N, self.HASTA)
        return a, (b if self.HASTA else min(b, a + self.DURA))

    def t(self, palabras, n=0):
        return max(0, self.l(self.v.cuadro(self.B, palabras, n)))

    def prepara(self):
        self.s_paso = sprite('Paso %d' % self.PASO, fuente('SemiBold', 34), AMARILLO)
        self.s_tit = sprite(self.TITULO, fuente('Bold', 64), ancho=1100)
        self.s_sub = sprite(self.SUB, fuente('Medium', 40), GRIS_TXT, ancho=1100)
        self.alto = 300 + (self.s_tit[2]) * 76 + 20
        self.extra()

    def extra(self):
        pass

    def dibuja_extra(self, c, i, g, y):
        return y

    def dibuja(self, c, i, g):
        o, s = aparece(i, 0)
        pega(c, self.s_paso, TEXTO_X, 228, o * g, s)
        pega(c, self.s_tit, TEXTO_X - 4, 290, o * g, s)
        o2, s2 = aparece(i, 6)
        pega(c, self.s_sub, TEXTO_X, self.alto, o2 * g, s2)
        y = self.dibuja_extra(c, i, g, self.alto + self.s_sub[2] * 48 + 46)
        self.barra(c, i, 230, max(y, self.alto + 60), g)


def lista(clave_, base=Lista, **kw):
    return type('G_' + clave_, (base,), dict(clave=clave_, **kw))


# --- V03
class Control(Lista):
    """r04: el control del juez de garantias, antes o inmediatamente despues."""
    clave = 'control'
    ante = 'Ley 906 de 2004'
    B = 'g02_control'
    N = 4
    MARCA = 'num'
    ITEMS = [('juez de control', 'Control del juez de garantías', None),
             ('antes', 'Antes de la ejecución', None),
             ('inmediatamente', 'O inmediatamente después', None)]


TECNICAS = [  # clave, ranura, bloque, palabras, nombre, articulo, punto en 1920x1080
    ('t239', 7, 'g04_personas', 'la vigilancia', 'Vigilancia y seguimiento de personas', 239, (1090, 356)),
    ('t240', 9, 'g05_cosas', 'la vigilancia', 'Vigilancia de cosas', 240, (1125, 620)),
    ('t241', 11, 'g06_analisis', 'el analisis', 'Análisis e infiltración de organización criminal', 241, (956, 190)),
    ('t242', 13, 'g07_encubierto', 'agentes encubiertos', 'Actuación de agentes encubiertos', 242, (845, 560)),
    ('t243', 15, 'g08_entrega', 'la entrega', 'Entrega vigilada', 243, (940, 710)),
    ('t233', 17, 'g09_correspondencia', 'la retencion', 'Retención de correspondencia', 233, (900, 845)),
    ('t235', 18, 'g10_interceptacion', 'la interceptacion', 'Interceptación de comunicaciones', 235, (1690, 700)),
    ('t236', 20, 'g11_internet', 'la recuperacion', 'Recuperación de información en internet', 236, (1460, 710)),
    ('t244', 21, 'g12_bases', 'la busqueda', 'Búsqueda selectiva en bases de datos', 244, (880, 770)),
]
V03 = [Control] + [type('R_' + k, (Rotulo,), dict(clave=k, N=n, B=b, PALABRAS=p, NOMBRE=nm,
                                                   ARTICULO='Ley 906 de 2004 · artículo %d' % a, PUNTO=pt))
                   for k, n, b, p, nm, a, pt in TECNICAS]

# --- V04
V04 = [
 lista('lesion', ante='Corte Suprema de Justicia', B='h03_lesion', N=6, MARCA='punto',
       CIFRA=('delito de lesion', 'Delito de lesión'),
       ITEMS=[('el dano a los recursos', 'El daño a los recursos naturales', None)]),
 lista('oxigeno', ante='Dictamen técnico de la autoridad ambiental', B='h06_medicion', N=11,
       MARCA='punto', CIFRA=('30', '−30 % de oxígeno'),
       ITEMS=[('a partir del tubo', 'A partir del tubo de desagüe de la empresa', None),
              ('disminuyo', 'El nivel de oxígeno del agua disminuyó', 'adicional a la contaminación de la mina')]),
 lista('plan', ante='Plan de reparación proporcional al daño', B='h09_plan', N=(15, 16),
       MARCA='num', denso=0.72, ralo=0.18,
       ITEMS=[('primero', 'Planta de tratamiento de aguas residuales', 'construcción inmediata, en la fábrica'),
              ('segundo', 'Repoblamiento de las dos especies afectadas', 'bajo supervisión de la autoridad ambiental')]),
 lista('medir', ante='Para reparar, primero hay que medir', B='h10_medir', N=18, MARCA='visto',
       ITEMS=[('que se afecto', 'Qué se afectó', None), ('cual era', 'Cuál era su estado previo', None),
              ('que alteracion', 'Qué alteración se produjo', None),
              ('vinculo causal', 'Cuál es su vínculo causal con la conducta', None)]),
]

# --- V05: las cuatro preguntas y las dos firmas
def pregunta(k, n, b, num, palabras, texto, cifra=None):
    return lista(k, ante='Pregunta %d de 4' % num, B=b, N=n, MARCA='punto', TAM=56,
                 CIFRA=cifra, ITEMS=[(palabras, texto, None)])


V05 = [
 pregunta('q1', 9, 'k05_quienes', 1, 'quienes fueron', '¿Quiénes fueron afectados?',
          cifra=('120', '120 familias')),
 pregunta('q2', 12, 'k07_como', 2, 'como afecto', '¿Cómo afectó el daño su territorio y su forma de vida?'),
 pregunta('q3', 16, 'k09_medidas', 3, 'que medidas', '¿Qué medidas son necesarias para restaurar el daño?'),
 pregunta('q4', 20, 'k12_guardia', 4, 'como participa', '¿Cómo participa la comunidad en la implementación y el seguimiento?'),
 lista('firmas', ante='El informe final lleva dos firmas', B='k13_firmas', N=23, MARCA='visto',
       ITEMS=[('la del perito', 'Perito de la autoridad ambiental', None),
              ('el aval', 'Aval del Cabildo Gobernador', None)]),
]

# --- V06: los ocho pasos del libreto
PASOS = [  # clave, ranura, bloque, n, titulo, subtitulo
    ('paso1', 1, 'm01_noticia', 1, 'Lectura de la noticia criminal', 'El punto de partida: la flagrancia'),
    ('paso2', 4, 'm02_norma', 2, 'Selección normativa', 'El molde jurídico: la tipificación inicial'),
    ('paso3', 8, 'm03_hipotesis', 3, 'Construcción de la hipótesis delictiva', 'El rompecabezas de la teoría del delito: la fractura de la culpabilidad'),
    ('paso4', 12, 'm04_objeto', 4, 'Objeto de prueba', 'Las grandes preguntas: el giro de la investigación'),
    ('paso5', 15, 'm05_utilidad', 5, 'Utilidad', 'El arsenal probatorio: la caracterización humana'),
    ('paso6', 18, 'm06_legalidad', 6, 'Legalidad', 'El escudo de los derechos: la articulación institucional'),
    ('paso7', 20, 'm07_suficiencia', 7, 'Suficiencia', 'La balanza judicial: la causal 7 y el principio de oportunidad'),
    ('paso8', 23, 'm08_viabilidad', 8, 'Viabilidad', 'El ajuste final del camino: el acuerdo restaurativo'),
]


class Rompecabezas(Tarjeta):
    """Paso 3: las tres piezas de la hipotesis; la del reproche de culpabilidad
    no encaja: entra con «se quiebra» corrida y en gris."""
    HASTA = None
    DURA = 10 ** 6

    def extra(self):
        f = fuente('Bold', 36)
        self.piezas = [sprite('Tiempo y lugar: Amazonas', f), sprite('Acción: talar', f),
                       sprite('Reproche de culpabilidad', f, AMARILLO)]
        self.t_p = [self.t('al construir'), self.t('al construir') + 10, self.t('se quiebra')]

    def dibuja_extra(self, c, i, g, y):
        d = ImageDraw.Draw(c)
        x = TEXTO_X
        for q, (spr, t0) in enumerate(zip(self.piezas, self.t_p)):
            o, s = aparece(i, t0)
            if o <= 0:
                continue
            w = spr[0].size[0] - 48 + 40
            dx = 0 if q < 2 else int(18 * suave((i - t0) / 10.0))
            dy = 0 if q < 2 else int(14 * suave((i - t0) / 10.0))
            col = (60, 90, 140) if q < 2 else (110, 110, 120)
            d.rounded_rectangle([x + dx, y + s + dy, x + dx + w, y + s + dy + 70], 10,
                                fill=col + (int(220 * o * g),), outline=AMARILLO + (int(255 * o * g),), width=3)
            pega(c, spr, x + dx + 20, y + 14 + dy, o * g, s)
            x += w + 18
        return y + 90


class Preguntas(Tarjeta):
    """Paso 4: las tres preguntas, literales, cada una con su voz."""
    DURA = 10 ** 6

    def extra(self):
        f = fuente('Medium', 38)
        self.qs = [(self.t('vale la pena'), sprite('¿Vale la pena llevar a juicio a un eslabón vulnerable?', f, ancho=1150)),
                   (self.t('quien es'), sprite('¿Quién es el verdadero financiador de la tala?', f, ancho=1150)),
                   (self.t('que mecanismo'), sprite('¿Qué mecanismo legal repara realmente el daño causado sin destruir aún más la vida del procesado?', f, ancho=1150))]

    def dibuja_extra(self, c, i, g, y):
        d = ImageDraw.Draw(c)
        for t0, spr in self.qs:
            o, s = aparece(i, t0)
            if o > 0:
                d.rectangle([TEXTO_X, y + 22 + s, TEXTO_X + 24, y + 30 + s], fill=AMARILLO + (int(255 * o * g),))
                pega(c, spr, TEXTO_X + 44, y, o * g, s)
            y += spr[2] * 50 + 24
        return y


class Balanza(Tarjeta):
    """Paso 7: la balanza. En un plato el juicio y la prision; en el otro la
    reparacion; con «herramienta superior» la reparacion baja. Debajo, con su
    palabra, el principio de oportunidad, causal 7."""
    DURA = 10 ** 6

    def extra(self):
        self.t_inc = self.t('herramienta superior')
        self.t_po = self.t('principio de oportunidad')
        f = fuente('SemiBold', 32)
        self.s_a = sprite('Juicio y prisión', f)
        self.s_b = sprite('Reparación', f, AMARILLO)
        self.s_po = sprite('Principio de oportunidad · causal 7', fuente('Bold', 46), AMARILLO)

    def dibuja_extra(self, c, i, g, y):
        d = ImageDraw.Draw(c)
        o, s = aparece(i, 10)
        if o <= 0:
            return y
        a = int(255 * o * g)
        cx, top = TEXTO_X + 360, y + 10
        ang = -0.16 * suave((i - self.t_inc) / 24.0)      # baja el plato derecho
        L = 260
        dx, dy = L * math.cos(ang), L * math.sin(ang)
        d.line([cx, top, cx, top + 200], fill=BLANCO + (a,), width=6)
        d.line([cx - dx, top + 20 + dy, cx + dx, top + 20 - dy], fill=BLANCO + (a,), width=6)
        for sgn, spr in ((-1, self.s_a), (1, self.s_b)):
            px, py = cx + sgn * dx, top + 20 - sgn * dy
            d.line([px, py, px - 50, py + 70], fill=BLANCO + (a,), width=3)
            d.line([px, py, px + 50, py + 70], fill=BLANCO + (a,), width=3)
            d.arc([px - 70, py + 40, px + 70, py + 110], 0, 180, fill=(AMARILLO if sgn > 0 else BLANCO) + (a,), width=6)
            w = spr[0].size[0] - 48
            pega(c, spr, px - w / 2, py + 118, o * g, 0)
        o2, s2 = aparece(i, self.t_po)
        pega(c, self.s_po, TEXTO_X, top + 230, o2 * g, s2)
        return top + 300


V06 = []
for k, n, b, num, tit, sub in PASOS:
    base = {3: Rompecabezas, 4: Preguntas, 7: Balanza}.get(num, Tarjeta)
    extra = {}
    if num == 7:
        extra['HASTA'] = 21          # la balanza sigue sobre el vivero (r21, sin gente)
    elif num == 3:
        extra['HASTA'] = n           # toda la ranura
    elif num == 4:
        # las tres preguntas caen en r12, r13 y r14: el grafico las cubre
        extra.update(HASTA=14, denso=0.70, ralo=0.15)
    V06.append(type('P_' + k, (base,), dict(clave=k, N=n, B=b, PASO=num, TITULO=tit, SUB=sub, **extra)))

GRAFICOS = {'V01': [Aluvion, Ideam, Motores, Municipios, Cadena],
            'V02': [Pilares, Niveles, Enfoques, Programa, Articulo6, Consecuencias],
            'V03': V03, 'V04': V04, 'V05': V05, 'V06': V06}
GEO = None


def rinde(gr, sal, muestra=False):
    nm = 'DA_%s_mg_%s' % (gr.v.clave, gr.clave)
    if muestra:
        p = os.path.join(sal, nm + '_muestra.png')
        i = min(gr.n - 12, max(0, gr.n * 3 // 4))
        fondo = Image.new('RGBA', (W, H), (110, 120, 110, 255))
        fondo.alpha_composite(gr.cuadro(i))
        fondo.convert('RGB').save(p)
        return p
    dest = os.path.join(sal, nm + '.mov')
    if os.path.exists(dest):
        d = os.path.join(sal, '_descartes')
        os.makedirs(d, exist_ok=True)
        k = 1
        while os.path.exists(os.path.join(d, '%s__rehecho_%d.mov' % (nm, k))):
            k += 1
        os.replace(dest, os.path.join(d, '%s__rehecho_%d.mov' % (nm, k)))
    ff = os.environ.get('FFMPEG', 'ffmpeg')
    pr = subprocess.Popen([ff, '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgba',
                           '-s', '%dx%d' % (W, H), '-r', '24000/1001', '-i', '-',
                           '-c:v', 'qtrle', '-pix_fmt', 'argb', dest], stdin=subprocess.PIPE)
    for i in range(gr.n):
        pr.stdin.write(gr.cuadro(i).tobytes())
    pr.stdin.close()
    assert pr.wait() == 0, dest
    return dest


def main():
    args = sys.argv[1:]
    clave = args[0].upper()
    opt = {}
    for k in ('--voces', '--sal', '--geo', '--escenas'):
        if k in args:
            i = args.index(k)
            opt[k] = args[i + 1]
            del args[i:i + 2]
    muestra = '--muestra' in args
    solo = [a for a in args[1:] if not a.startswith('--')]
    H_ = r'D:\DAE\_repo\herramientas'
    sys.path.insert(0, opt.get('--escenas', os.path.join(H_, 'prompts')))
    sys.path.insert(0, os.path.join(H_, 'voz', 'textos'))
    escenas = __import__('escenas_da_%s' % clave.lower())
    if '--voces' in opt:
        voces, sal = opt['--voces'], opt['--sal']
    else:
        import rutas_da as R
        voces, sal = R.voces(clave), R.sub(clave, '09 MOTION GRAPHICS')
    global GEO
    GEO = opt.get('--geo', os.path.join(H_, 'graficas', 'colombia_dptos.geojson'))
    os.makedirs(sal, exist_ok=True)
    voz = Voz(clave, voces)
    lista = []
    for G in GRAFICOS[clave]:
        gr = G(voz, escenas)
        lista.append({'clave': gr.clave, 'archivo': 'DA_%s_mg_%s.mov' % (clave, gr.clave),
                      'ini': gr.ini, 'cuadros': gr.n})
        if solo and gr.clave not in solo:
            continue
        p = rinde(gr, sal, muestra)
        print('%-11s %5d +%4d  %s' % (gr.clave, gr.ini, gr.n, p), flush=True)
    if not muestra:
        json.dump(lista, open(os.path.join(sal, 'DA_%s_mg.json' % clave), 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
    print('LISTO')


if __name__ == '__main__':
    main()
