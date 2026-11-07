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


GRAFICOS = [Aluvion, Ideam, Motores, Municipios, Cadena]
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
    for G in GRAFICOS:
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
