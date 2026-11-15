"""mg_emb.py — motion graphics del proyecto EMB, rendidos en la nube con Pillow + ffmpeg.

Todo sale a 1920x1080, 24000/1001, H.264 CRF 14, yuv420p, etiquetado bt709.
Los elementos se dibujan una vez a 2x (antialias) y se animan por posición, escala y alfa.

Uso: python3 mg_emb.py <pieza> <salida.mp4> [json de parámetros]
Piezas: intro, titulo, comparador, escalera, columnas, actividad, outro, etiqueta_png
"""
import json, math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1920, 1080
FPS = 24000 / 1001
ROJO, AMARILLO, TINTA, AZUL = (223, 31, 21), (255, 196, 0), (33, 37, 41), (27, 65, 139)
GRIS, GRIS_MEDIO, BLANCO, FONDO = (233, 236, 239), (108, 117, 125), (255, 255, 255), (247, 247, 248)

RAIZ = os.environ.get('EMB_RAIZ', '/home/claude/emb')
F_WORK = os.path.join(RAIZ, 'fuentes', 'WorkSans[wght].ttf')
F_MONT = os.path.join(RAIZ, 'fuentes', 'Montserrat[wght].ttf')
LOGOS = os.path.join(RAIZ, 'marca', 'logos')


# ---------- utilidades ----------
def fuente(cual, peso, tam):
    f = ImageFont.truetype(F_WORK if cual == 'work' else F_MONT, tam)
    f.set_variation_by_name(peso)
    return f


def suave(t):          # easeOutCubic
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def suave_io(t):       # easeInOutCubic
    t = max(0.0, min(1.0, t))
    return 4 * t ** 3 if t < .5 else 1 - (-2 * t + 2) ** 3 / 2


def tramo(f, a, b):
    """0..1 entre los cuadros a y b."""
    return 0.0 if f <= a else 1.0 if f >= b else (f - a) / (b - a)


def tarjeta(w, h, relleno, radio=28, borde=None, sombra=True):
    """Tarjeta redondeada con antialias (dibujada a 2x) y sombra suave."""
    m = 40 if sombra else 0
    big = Image.new('RGBA', ((w + 2 * m) * 2, (h + 2 * m) * 2), (0, 0, 0, 0))
    if sombra:
        s = Image.new('RGBA', big.size, (0, 0, 0, 0))
        ImageDraw.Draw(s).rounded_rectangle([m * 2, m * 2 + 12, (m + w) * 2, (m + h) * 2 + 12],
                                            radio * 2, fill=(0, 0, 0, 38))
        big = Image.alpha_composite(big, s.filter(ImageFilter.GaussianBlur(28)))
    d = ImageDraw.Draw(big)
    d.rounded_rectangle([m * 2, m * 2, (m + w) * 2, (m + h) * 2], radio * 2, fill=relleno,
                        outline=borde, width=4 if borde else 0)
    return big.resize((w + 2 * m, h + 2 * m), Image.LANCZOS), m


def texto(img, xy, s, f, color, ancho=None, interlinea=1.18):
    """Escribe con corte de renglón por ancho. Devuelve la altura usada."""
    d = ImageDraw.Draw(img)
    lineas = []
    for parrafo in s.split('\n'):
        actual = ''
        for p in parrafo.split():
            prueba = (actual + ' ' + p).strip()
            if ancho and d.textlength(prueba, font=f) > ancho and actual:
                lineas.append(actual)
                actual = p
            else:
                actual = prueba
        lineas.append(actual)
    x, y = xy
    alto = f.size * interlinea
    for i, l in enumerate(lineas):
        d.text((x, y + i * alto), l, font=f, fill=color)
    return len(lineas) * alto


def pegar(base, spr, x, y, alfa=1.0, escala=1.0):
    if alfa <= 0.003:
        return
    s = spr
    if abs(escala - 1) > 1e-3:
        s = spr.resize((max(1, int(spr.width * escala)), max(1, int(spr.height * escala))), Image.LANCZOS)
        x += (spr.width - s.width) / 2
        y += (spr.height - s.height) / 2
    if alfa < 0.999:
        s = s.copy()
        a = s.getchannel('A').point(lambda v: int(v * alfa))
        s.putalpha(a)
    base.alpha_composite(s, (int(round(x)), int(round(y))))


class Escritor:
    def __init__(self, ruta, alfa=False):
        self.alfa = alfa
        if alfa:   # QuickTime Animation con alfa, como los cartones de la casa
            args = ['-c:v', 'qtrle', '-pix_fmt', 'argb']
            fmt = 'rgba'
        else:
            args = ['-c:v', 'libx264', '-preset', 'medium', '-crf', '14', '-pix_fmt', 'yuv420p',
                    '-vf', 'scale=out_color_matrix=bt709:out_range=tv',
                    '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
            fmt = 'rgb24'
        self.p = subprocess.Popen(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-f', 'rawvideo',
                                   '-pix_fmt', fmt, '-s', f'{W}x{H}', '-r', '24000/1001', '-i', '-'] + args + [ruta],
                                  stdin=subprocess.PIPE)
        self.n = 0

    def cuadro(self, img):
        self.p.stdin.write(img.convert('RGBA' if self.alfa else 'RGB').tobytes())
        self.n += 1

    def cerrar(self):
        self.p.stdin.close()
        self.p.wait()
        return self.n


def lienzo(color=FONDO):
    return Image.new('RGBA', (W, H), color + (255,))


def logo_capas(ancho):
    caps = {}
    for c in ('emblema', 'metro', 'bogota'):
        im = Image.open(os.path.join(LOGOS, f'capa_{c}.png')).convert('RGBA')
        caps[c] = im.resize((ancho, int(im.height * ancho / im.width)), Image.LANCZOS)
    return caps


def curva(t, x0=-80, x1=2000, y0=760, y1=520):
    """Línea de viaducto: sube suave de izquierda a derecha."""
    x = x0 + (x1 - x0) * t
    y = y0 + (y1 - y0) * (1 - math.cos(math.pi * t)) / 2
    return x, y


def dibujar_curva(base, hasta, color=ROJO, grosor=10, desde=0.0, **kw):
    if hasta <= desde:
        return
    capa = Image.new('RGBA', (W * 2, H * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    pts = [curva(desde + (hasta - desde) * i / 120, **kw) for i in range(121)]
    d.line([(x * 2, y * 2) for x, y in pts], fill=color + (255,), width=grosor * 2, joint='curve')
    base.alpha_composite(capa.resize((W, H), Image.LANCZOS))


# ---------- piezas ----------
def intro(salida, p):
    """3,5 s: la línea del viaducto se dibuja, cruza el tren, se arma el logo."""
    n = p.get('cuadros', 84)
    caps = logo_capas(900)
    lx, ly = (W - 900) // 2, (H - caps['emblema'].height) // 2 - 30
    tren, _ = tarjeta(300, 54, ROJO + (255,), radio=27, sombra=False)
    e = Escritor(salida)
    for f in range(n):
        im = lienzo(BLANCO)
        # la línea se dibuja y luego se retira
        dibujar_curva(im, suave_io(tramo(f, 0, 26)), desde=suave_io(tramo(f, 30, 52)))
        # el tren recorre la curva
        t = suave_io(tramo(f, 6, 40))
        if 0 < t < 1:
            x, y = curva(t)
            pegar(im, tren, x - 150, y - 27 - 40)
        # el emblema crece
        a = suave(tramo(f, 30, 50))
        pegar(im, caps['emblema'], lx, ly, a, 0.82 + 0.18 * a)
        # METRO entra desde la izquierda con máscara
        a = suave(tramo(f, 40, 58))
        if a > 0:
            m = caps['metro'].copy()
            corte = int(m.width * (0.40 + 0.60 * a))
            m = m.crop((0, 0, corte, m.height))
            pegar(im, m, lx - 30 * (1 - a), ly, a)
        a = suave(tramo(f, 50, 66))
        pegar(im, caps['bogota'], lx, ly + 18 * (1 - a), a)
        e.cuadro(im)
    return e.cerrar()


def titulo(salida, p):
    n = p.get('cuadros', 96)
    ante, tit, curso = p['ante'], p['titulo'], p.get('curso', '')
    f_ante, f_tit, f_curso = fuente('mont', 'SemiBold', 34), fuente('work', 'Bold', 96), fuente('mont', 'Medium', 28)
    capa_txt = Image.new('RGBA', (1400, 420), (0, 0, 0, 0))
    texto(capa_txt, (0, 0), ante, f_ante, GRIS_MEDIO + (255,))
    texto(capa_txt, (0, 64), tit, f_tit, TINTA + (255,), ancho=1350, interlinea=1.05)
    caps = logo_capas(300)
    logo = caps['emblema'].copy(); logo.alpha_composite(caps['metro']); logo.alpha_composite(caps['bogota'])
    e = Escritor(salida)
    for f in range(n):
        im = lienzo()
        h = suave(tramo(f, 0, 14))
        ImageDraw.Draw(im).rectangle([200, 430 - 150 * h, 214, 430 + 150 * h], fill=ROJO)
        a = suave(tramo(f, 6, 22))
        pegar(im, capa_txt, 260 - 40 * (1 - a), 330, a)
        a = suave(tramo(f, 14, 30))
        pegar(im, logo, W - 300 - 120, 100, a)
        if curso:
            d = ImageDraw.Draw(im)
            a = suave(tramo(f, 20, 36))
            if a > 0:
                c = Image.new('RGBA', (1600, 60), (0, 0, 0, 0))
                texto(c, (0, 0), curso, f_curso, GRIS_MEDIO + (255,))
                pegar(im, c, 200, 900, a)
        # salida: todo se desliza a la izquierda en los últimos 8 cuadros
        if f >= n - 8:
            k = suave_io(tramo(f, n - 8, n))
            im = Image.alpha_composite(lienzo(), im.transform(im.size, Image.AFFINE, (k * 240, 0, 0, 0, 1, 0)))
            im = Image.blend(im, lienzo(), k)
        e.cuadro(im)
    return e.cerrar()


def _tarjeta_concepto(w, h, nombre, linea, activa, color_activo):
    fondo = (color_activo if activa else BLANCO) + (255,)
    spr, m = tarjeta(w, h, fondo, borde=None if activa else GRIS + (255,))
    tinta = (BLANCO if color_activo == ROJO else TINTA) if activa else TINTA
    sub = (BLANCO if color_activo == ROJO else TINTA) if activa else GRIS_MEDIO
    texto(spr, (m + 44, m + 48), nombre, fuente('work', 'Bold', 54), tinta + (255,), ancho=w - 88)
    texto(spr, (m + 44, m + 140), linea, fuente('mont', 'Medium', 32), sub + (255,), ancho=w - 88, interlinea=1.3)
    return spr, m


def comparador(salida, p):
    """Tarjetas en fila; cada una se activa en su cuadro 'activa_en'."""
    items, n = p['items'], p['cuadros']
    k = len(items)
    gap, w = 40, (W - 2 * 140 - (k - 1) * 40) // k
    h = p.get('alto', 420)
    y0 = (H - h) // 2 - 20
    sprs = [(_tarjeta_concepto(w, h, it['nombre'], it['linea'], False, ROJO),
             _tarjeta_concepto(w, h, it['nombre'], it['linea'], True, ROJO if i % 2 == 0 else AMARILLO))
            for i, it in enumerate(items)]
    rot = None
    if p.get('rotulo'):
        f = fuente('mont', 'SemiBold', 26)
        tw = int(ImageDraw.Draw(lienzo()).textlength(p['rotulo'], font=f))
        rot, rm = tarjeta(tw + 48, 52, GRIS + (255,), radio=26, sombra=False)
        texto(rot, (rm + 24, rm + 11), p['rotulo'], f, TINTA + (255,))
    titulo_txt = p.get('titulo')
    e = Escritor(salida)
    for f in range(n):
        im = lienzo()
        if titulo_txt:
            a = suave(tramo(f, 0, 12))
            c = Image.new('RGBA', (1600, 80), (0, 0, 0, 0))
            texto(c, (0, 0), titulo_txt, fuente('work', 'Bold', 52), TINTA + (255,))
            pegar(im, c, 140 - 30 * (1 - a), 120, a)
        activa = max([i for i, it in enumerate(items) if f >= it['activa_en']], default=-1)
        for i, ((inact, m), (act, _)) in enumerate(sprs):
            a = suave(tramo(f, 4 + i * 5, 18 + i * 5))
            x = 140 + i * (w + gap) - m - 60 * (1 - a)
            y = y0 - m
            pegar(im, inact, x, y, a)
            if i == activa:
                t0 = items[i]['activa_en']
                b = suave(tramo(f, t0, t0 + 8))
                pegar(im, act, x, y - 14 * b, b, 1 + 0.03 * b)
        if rot:
            pegar(im, rot, 140 - rm, H - 150 - rm, suave(tramo(f, 10, 22)))
        if f >= n - 8:
            im = Image.blend(im, lienzo(), suave_io(tramo(f, n - 8, n)))
        e.cuadro(im)
    return e.cerrar()


def escalera(salida, p):
    """Peldaños que suben de izquierda a derecha; cada uno se activa en su cuadro."""
    items, n = p['items'], p['cuadros']
    k = len(items)
    w, h, paso = 390, 300, 70
    x0 = (W - (k * w + (k - 1) * 24)) // 2
    colores = p.get('colores', [AMARILLO, AMARILLO, ROJO, ROJO])
    sprs = [(_tarjeta_concepto(w, h, it['nombre'], it['linea'], False, colores[i]),
             _tarjeta_concepto(w, h, it['nombre'], it['linea'], True, colores[i])) for i, it in enumerate(items)]
    e = Escritor(salida)
    for f in range(n):
        im = lienzo()
        activa = max([i for i, it in enumerate(items) if f >= it['activa_en']], default=-1)
        for i, ((inact, m), (act, _)) in enumerate(sprs):
            a = suave(tramo(f, 2 + i * 4, 16 + i * 4))
            x = x0 + i * (w + 24) - m
            y = 640 - i * paso - h - m + 40 * (1 - a)
            pegar(im, inact, x, y, a)
            if i <= activa:
                t0 = items[i]['activa_en']
                b = suave(tramo(f, t0, t0 + 8))
                pegar(im, act, x, y - (10 * b if i == activa else 0), b)
        # flecha de gravedad
        a = suave(tramo(f, 10, 30))
        if a > 0:
            d = ImageDraw.Draw(im)
            xa = x0 + (k * w + (k - 1) * 24) * a
            d.line([(x0, 720), (xa, 720)], fill=GRIS_MEDIO, width=4)
            c = Image.new('RGBA', (900, 50), (0, 0, 0, 0))
            texto(c, (0, 0), p.get('eje', 'De lo más leve a lo más grave'), fuente('mont', 'Medium', 28), GRIS_MEDIO + (255,))
            pegar(im, c, x0, 740, a)
        if f >= n - 8:
            im = Image.blend(im, lienzo(), suave_io(tramo(f, n - 8, n)))
        e.cuadro(im)
    return e.cerrar()


def columnas(salida, p):
    p = dict(p)
    p.setdefault('alto', 300)
    return comparador(salida, p)


def actividad(salida, p):
    n = p['cuadros']
    f_et, f_tx = fuente('mont', 'SemiBold', 32), fuente('work', 'SemiBold', 58)
    e = Escritor(salida)
    capa = Image.new('RGBA', (1500, 700), (0, 0, 0, 0))
    texto(capa, (0, 0), p['etiqueta'], f_et, TINTA + (255,))
    texto(capa, (0, 80), p['texto'], f_tx, TINTA + (255,), ancho=1450, interlinea=1.22)
    for f in range(n):
        im = lienzo(BLANCO)
        a = suave_io(tramo(f, 0, 14))
        d = ImageDraw.Draw(im)
        d.rectangle([0, 0, int(W * a), H], fill=AMARILLO)
        b = suave(tramo(f, 10, 26))
        pegar(im, capa, 200 - 40 * (1 - b), 300, b)
        if f >= n - 8:
            im = Image.blend(im, lienzo(BLANCO), suave_io(tramo(f, n - 8, n)))
        e.cuadro(im)
    return e.cerrar()


def outro(salida, p):
    n = p.get('cuadros', 108)
    altos = {'logo_metro.svg': 150, 'logo_alcaldia_bogota.svg': 150, 'logo_gobierno_potencia.svg': 120}
    sprs = []
    for nombre in p.get('logos', list(altos)):
        tmp = f'/tmp/_{nombre}.png'
        subprocess.run(['rsvg-convert', '-h', str(altos.get(nombre, 140) * 2), os.path.join(LOGOS, nombre), '-o', tmp], check=True)
        im = Image.open(tmp).convert('RGBA')
        sprs.append(im.resize((im.width // 2, im.height // 2), Image.LANCZOS))
    total = sum(s.width for s in sprs) + 120 * (len(sprs) - 1)
    e = Escritor(salida)
    for f in range(n):
        im = lienzo(BLANCO)
        dibujar_curva(im, suave_io(tramo(f, 0, 30)), grosor=8, y0=1000, y1=860)
        x = (W - total) // 2
        for i, s in enumerate(sprs):
            a = suave(tramo(f, 16 + i * 8, 34 + i * 8))
            pegar(im, s, x, (H - s.height) // 2 - 20 + 20 * (1 - a), a)
            if i < len(sprs) - 1 and a > 0:
                sep = Image.new('RGBA', (3, 140), GRIS + (255,))
                pegar(im, sep, x + s.width + 60, H // 2 - 90, a)
            x += s.width + 120
        if f >= n - 10:
            im = Image.blend(im, lienzo(BLANCO), suave_io(tramo(f, n - 10, n)))
        e.cuadro(im)
    return e.cerrar()


def etiqueta_png(salida, p):
    """Etiqueta fija de caso: PNG con alfa para superponer a las placas."""
    f = fuente('mont', 'Medium', 26)
    t = p.get('texto', 'Situación hipotética con fines pedagógicos')
    tw = int(ImageDraw.Draw(lienzo()).textlength(t, font=f))
    spr, m = tarjeta(tw + 56, 56, (255, 255, 255, 225), radio=28, sombra=False)
    d = ImageDraw.Draw(spr)
    d.ellipse([m + 22, m + 22, m + 34, m + 34], fill=AMARILLO)
    texto(spr, (m + 44, m + 12), t, f, TINTA + (255,))
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    im.alpha_composite(spr, (80 - m, 64 - m))
    im.save(salida)
    return 1


PIEZAS = dict(intro=intro, titulo=titulo, comparador=comparador, escalera=escalera, columnas=columnas,
              actividad=actividad, outro=outro, etiqueta_png=etiqueta_png)

if __name__ == '__main__':
    pieza, salida = sys.argv[1], sys.argv[2]
    params = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
    n = PIEZAS[pieza](salida, params)
    print(pieza, salida, n, 'cuadros')
