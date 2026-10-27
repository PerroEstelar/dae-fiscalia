# -*- coding: utf-8 -*-
r"""La LAMINA de las situaciones en imagen (F a K).

QUE ES
    La ilustracion a sangre, 1920 x 1080, y encima, en su LADO LIBRE -el
    tercio de pared, cielo o penumbra que la placa se pidio dejar vacio-, un
    panel con el contexto VERBATIM de la situacion. La consigna no entra: la
    agencia la marco en el documento «No incluir esto en la IMAGEN».

EL SISTEMA ES EL DEL CARTON, ADAPTADO A UNA PAGINA QUE SE LEE QUIETA
    - el azul de la serie (#004890) y el filete amarillo de una pieza, alto
      como el bloque de texto;
    - Montserrat: el rotulo «Situación F» en Bold y amarillo, el texto en
      Medium y blanco;
    - en video el tinte va al 46 % sobre todo el cuadro porque el texto dura
      unos segundos; aqui el texto es largo y se lee con calma, asi que el
      tinte va SOLO sobre el panel y mas denso (82 %), para que la
      ilustracion quede limpia del otro lado;
    - el cuerpo se ajusta solo, de 40 hacia abajo, hasta que el texto cabe
      con aire; la H -la mas larga, 631 caracteres- es la que manda.

    Los numeros van en digitos, como en el documento: es texto que se lee,
    no que se oye.

    python lamina_sit.py --maqueta     las seis maquetas sobre un fondo neutro
    python lamina_sit.py F ilustracion.png izq|der
"""
import os
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, r'D:\DAE\_repo\herramientas\cartones')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
import cartones_ta as C                         # noqa: E402
from guion_sit import TEXTOS, IMAGENES, TAMBIEN_IMAGEN  # noqa: E402
import rutas_sit as R                           # noqa: E402

W, H = 1920, 1080
AZUL = (0, 72, 144)
ALFA_PANEL = 209                 # 82 %
AMARILLO = C.BAR_C[:3]
BLANCO = (255, 255, 255)
ANCHO_PANEL = 820
MARGEN_X = 86                    # del borde del panel al filete
MARGEN_Y = 120
FILETE = 10
SEP = 34                         # del filete al texto
MARCA = r'E:\DAE MASTER\00 COMUNES\MARCA DE AGUA\APRENDE_CON_LA_DAE_alfa.png'


def _partir(texto, font, draw, maxw):
    out = []
    for parrafo in texto.split('\n'):
        act = ''
        for w in parrafo.split():
            probe = (act + ' ' + w).strip()
            if draw.textlength(probe, font=font) <= maxw or not act:
                act = probe
            else:
                out.append(act)
                act = w
        if act:
            out.append(act)
        out.append('')           # respiro entre parrafos
    while out and out[-1] == '':
        out.pop()
    return out


def _bloque(texto, alto_max, ancho):
    d = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
    for cuerpo in range(40, 25, -1):
        f = C.fuente(C.F_MED, cuerpo)
        salto = int(round(cuerpo * 1.42))
        lineas = _partir(texto, f, d, ancho)
        alto = sum(salto if ln else salto // 2 for ln in lineas)
        if alto <= alto_max:
            return f, cuerpo, salto, lineas, alto
    raise SystemExit('el texto no cabe ni a cuerpo 26')


def lamina(letra, fondo, salida, lado='izq', ancho=ANCHO_PANEL):
    """`ancho` del panel: 820 por defecto; se angosta cuando la ilustracion
    tiene algo que no se puede tapar cerca del borde (la J, 690)."""
    if isinstance(fondo, Image.Image):
        im = fondo.convert('RGB').resize((W, H), Image.LANCZOS)
    else:
        im = Image.open(fondo).convert('RGB')
        if im.size != (W, H):
            # se cubre el cuadro sin deformar: escala y recorte al centro
            r = max(W / im.width, H / im.height)
            im = im.resize((int(im.width * r + .5), int(im.height * r + .5)),
                           Image.LANCZOS)
            x, y = (im.width - W) // 2, (im.height - H) // 2
            im = im.crop((x, y, x + W, y + H))
    im = im.convert('RGBA')
    x0 = 0 if lado == 'izq' else W - ancho
    panel = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(panel).rectangle([x0, 0, x0 + ancho, H],
                                    fill=AZUL + (ALFA_PANEL,))
    im = Image.alpha_composite(im, panel)
    d = ImageDraw.Draw(im)

    f_rot = C.fuente(C.F_BOLD, 30)
    rotulo = 'Situación %s' % letra
    ancho_txt = ancho - MARGEN_X - FILETE - SEP - 70
    f, cuerpo, salto, lineas, alto = _bloque(TEXTOS[letra],
                                             H - 2 * MARGEN_Y - 70, ancho_txt)
    total = 30 + 34 + alto
    y = (H - total) // 2
    xt = x0 + MARGEN_X + FILETE + SEP
    d.rectangle([x0 + MARGEN_X, y - 6, x0 + MARGEN_X + FILETE, y + total + 4],
                fill=AMARILLO + (255,))
    d.text((xt, y), rotulo.upper(), font=f_rot, fill=AMARILLO + (255,))
    y += 30 + 34
    for ln in lineas:
        if ln:
            d.text((xt, y), ln, font=f, fill=BLANCO + (255,))
            y += salto
        else:
            y += salto // 2

    if os.path.exists(MARCA):
        m = Image.open(MARCA).convert('RGBA')
        m.thumbnail((300, 200))
        mx = W - m.width - 70 if lado == 'izq' else 70
        # en el video la marca sale BLANCA sobre la imagen; aqui igual
        a = m.split()[3].point(lambda v: int(v * 0.9))
        m = Image.new('RGBA', m.size, BLANCO + (255,))
        m.putalpha(a)
        im.alpha_composite(m, (mx, 60))
    im.convert('RGB').save(salida)
    return cuerpo, len([x for x in lineas if x])


def maqueta(letra, lado):
    """Fondo neutro con la luz de la serie, solo para medir el texto."""
    g = Image.linear_gradient('L').rotate(90).resize((W, H))
    g = g.point(lambda v: 70 + int(v * 0.35))
    return Image.merge('RGB', (g, g, g))


if __name__ == '__main__':
    import imagenes_sit as IMG
    if '--maqueta' in sys.argv:
        for L in sorted(set(IMAGENES) | TAMBIEN_IMAGEN):
            lado = IMG.IM[L]['a'][3]
            dest = os.path.join(R.sub(L, '02 LAMINA', 'imagen'),
                                'SIT_%s_lamina_MAQUETA.png' % L)
            c, n = lamina(L, maqueta(L, lado), dest, lado)
            print('%s  lado %s  cuerpo %d  %d renglones  %s'
                  % (L, lado, c, n, os.path.basename(dest)))
    else:
        L, fondo, lado = sys.argv[1].upper(), sys.argv[2], sys.argv[3]
        dest = os.path.join(R.sub(L, '02 LAMINA', 'imagen'),
                            'SIT_%s_lamina.png' % L)
        print(lamina(L, fondo, dest, lado))
