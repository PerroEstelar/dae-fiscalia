# -*- coding: utf-8 -*-
r"""Las LÁMINAS del curso Estándares interamericanos (S02 S03 S05 S09 S10 S11),
de la candidata elegida a la entrega.

Es `lamina_lp` con el texto en PÁRRAFOS (`guion_ei.TEXTOS`), porque dos
láminas no son un solo bloque:
    'p'     cuerpo (Montserrat Medium)
    'ref'   la referencia de la lectura, en cursiva (S10)
    'cita'  el fragmento de la sentencia: cuerpo al 86 %, sangrado, con un
            filete blanco fino a la izquierda (S10, párrafos 178 y 179)
    'det'   una determinación: lo que va hasta el primer punto en negrita
            («Determinación A.»), el resto en cuerpo (S11)
Rótulo: el subtítulo del documento («SITUACIÓN DE APRENDIZAJE», «SITUACIÓN
INICIAL», «SITUACIÓN»). Panel azul (0,72,144) al 82 %, filete amarillo, marca
APRENDE CON LA DAE: la forma de Ley 1826 y de «16 situaciones».

    python lamina_ei.py S02 S10 ...     (sin claves: todas las elegidas)

Por cada clave (`elegidas_ei.json` -> `_laminas`: candidata, lado, ancho,
registro, acento):
    01 PLANOS/_candidatas/EI_<K>_img_<v>.png      la tirada escogida
    01 PLANOS/EI_<K>_ilustracion.png              limpia de color
    01 PLANOS/_grade/EI_<K>_ilustracion.png       grade por registro, con techo
    02 LAMINA/EI_<K>_lamina.png                   con el texto
    05 EXPORTS/EI_<K>_lamina.png  .jpg  _ilustracion.png
    IMAGENES\IMAGENES ENTREGA\<nombre de entrega>.png
"""
import json
import os
import shutil
import sys

H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', 'prompts', 'cartones', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageStat   # noqa: E402

import cartones_ta as C                                 # noqa: E402
import rutas_ei as R                                    # noqa: E402
from guion_ei import PIEZAS, TEXTOS, ENTREGA            # noqa: E402

W, H_ = 1920, 1080
AZUL = (0, 72, 144)
ALFA_PANEL = 209                 # 82 %, como las de 16 situaciones
AMARILLO = C.BAR_C[:3]
BLANCO = (255, 255, 255)
MARGEN_X = 86
MARGEN_Y = 110
FILETE = 10
SEP = 34
CITA = 0.86                      # cuerpo de la cita
SANGRIA = 26                     # sangria de la cita (y su filete a 6 px)
MARCA = r'E:\DAE MASTER\00 COMUNES\MARCA DE AGUA\APRENDE_CON_LA_DAE_alfa.png'
F_ITA = os.path.join(H, 'cartones', 'fuentes', 'Montserrat-Italic-VF.ttf')
ELEGIDAS = os.path.join(H, 'prompts', 'elegidas_ei.json')


def _ita(cuerpo):
    f = ImageFont.truetype(F_ITA, cuerpo)
    try:
        f.set_variation_by_axes([500])
    except Exception:                                     # noqa: BLE001
        pass
    return f


def _fuentes(cuerpo):
    return {'n': C.fuente(C.F_MED, cuerpo), 'i': _ita(cuerpo),
            'b': C.fuente(C.F_BOLD, cuerpo)}


def _palabras(estilo, texto):
    """[(palabra, tipo)] con tipo n|i|b."""
    if estilo == 'ref':
        return [(w, 'i') for w in texto.split(' ')]
    if estilo == 'det':
        cab, resto = texto.split('. ', 1)
        return ([(w, 'b') for w in (cab + '.').split(' ')]
                + [(w, 'n') for w in resto.split(' ')])
    return [(w, 'n') for w in texto.split(' ')]


def _partir(pals, fs, draw, maxw):
    lineas, act, ancho = [], [], 0.0
    for w, t in pals:
        lw = draw.textlength(w, font=fs[t])
        esp = draw.textlength(' ', font=fs[t])
        nuevo = lw if not act else ancho + esp + lw
        if act and nuevo > maxw:
            lineas.append(act)
            act, ancho = [(w, t)], lw
        else:
            act.append((w, t))
            ancho = nuevo
    if act:
        lineas.append(act)
    return lineas


def _maqueta(clave, alto_max, ancho):
    """Elige el cuerpo mas grande (40 -> 22) con el que todo cabe y devuelve
    [(estilo, fuentes, salto, lineas, x_extra)], cuerpo, alto total."""
    d = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
    for cuerpo in range(40, 21, -1):
        bloques, alto = [], 0
        for k, (estilo, texto) in enumerate(TEXTOS[clave]):
            c = int(round(cuerpo * CITA)) if estilo == 'cita' else cuerpo
            fs = _fuentes(c)
            salto = int(round(c * 1.42))
            extra = SANGRIA if estilo == 'cita' else 0
            lineas = _partir(_palabras(estilo, texto), fs, d, ancho - extra)
            if k:
                alto += int(round(cuerpo * 0.62))           # aire entre parrafos
            bloques.append((estilo, fs, salto, lineas, extra))
            alto += salto * len(lineas)
        if alto <= alto_max:
            return bloques, cuerpo, alto
    raise SystemExit('%s: el texto no cabe ni a cuerpo 22' % clave)


def lamina(clave, fondo, salida, lado='izq', ancho=820):
    im = Image.open(fondo).convert('RGB')
    if im.size != (W, H_):
        r = max(W / im.width, H_ / im.height)
        im = im.resize((int(im.width * r + .5), int(im.height * r + .5)),
                       Image.LANCZOS)
        x, y = (im.width - W) // 2, (im.height - H_) // 2
        im = im.crop((x, y, x + W, y + H_))
    im = im.convert('RGBA')
    x0 = 0 if lado == 'izq' else W - ancho
    panel = Image.new('RGBA', (W, H_), (0, 0, 0, 0))
    ImageDraw.Draw(panel).rectangle([x0, 0, x0 + ancho, H_],
                                    fill=AZUL + (ALFA_PANEL,))
    im = Image.alpha_composite(im, panel)
    d = ImageDraw.Draw(im)
    f_rot = C.fuente(C.F_BOLD, 30)
    rotulo = PIEZAS[clave][4].upper()
    ancho_txt = ancho - MARGEN_X - FILETE - SEP - 70
    bloques, cuerpo, alto = _maqueta(clave, H_ - 2 * MARGEN_Y - 70, ancho_txt)
    total = 30 + 34 + alto
    y = (H_ - total) // 2
    xt = x0 + MARGEN_X + FILETE + SEP
    d.rectangle([x0 + MARGEN_X, y - 6, x0 + MARGEN_X + FILETE, y + total + 4],
                fill=AMARILLO + (255,))
    d.text((xt, y), rotulo, font=f_rot, fill=AMARILLO + (255,))
    y += 30 + 34
    renglones = 0
    for k, (estilo, fs, salto, lineas, extra) in enumerate(bloques):
        if k:
            y += int(round(cuerpo * 0.62))
        if estilo == 'cita':
            d.rectangle([xt + 6, y + 4, xt + 8, y + salto * len(lineas) - 6],
                        fill=BLANCO + (150,))
        for ln in lineas:
            x = xt + extra
            for w, t in ln:
                d.text((x, y), w, font=fs[t], fill=BLANCO + (255,))
                x += d.textlength(w, font=fs[t]) + d.textlength(' ', font=fs[t])
            y += salto
            renglones += 1
    if os.path.exists(MARCA):
        m = Image.open(MARCA).convert('RGBA')
        m.thumbnail((300, 200))
        mx = W - m.width - 70 if lado == 'izq' else 70
        a = m.split()[3].point(lambda v: int(v * 0.9))
        # 5 nov (S09): sobre la ventana clara la marca blanca se perdia («CON»
        # desaparecia). Si el fondo bajo la marca es claro, lleva las sombras
        # de la rejilla B (nucleo y ambiental); sobre fondo oscuro no cambia.
        fondo = im.crop((mx, 60, mx + m.width, 60 + m.height)).convert('L')
        if ImageStat.Stat(fondo, a).mean[0] > 140:
            P = 40
            base = Image.new('L', (m.width + 2 * P, m.height + 2 * P), 0)
            base.paste(a, (P, P))
            for radio, op in ((22, 0.70), (3, 0.85)):
                s = base.filter(ImageFilter.GaussianBlur(radio)).point(
                    lambda v, op=op: int(v * op))
                capa = Image.new('RGBA', base.size, (0, 0, 0, 255))
                capa.putalpha(s)
                im.alpha_composite(capa, (mx - P, 60 - P))
        m = Image.new('RGBA', m.size, BLANCO + (255,))
        m.putalpha(a)
        im.alpha_composite(m, (mx, 60))
    im.convert('RGB').save(salida)
    return cuerpo, renglones


def una(clave, el):
    import sit_pieza as SP
    import graduar_registro as GR
    from imagen_sit import topa_rojos
    cand, lado, ancho, reg = el['candidata'], el['lado'], el['ancho'], el['registro']
    acento = el.get('acento', False)
    pl = R.sub(clave, '01 PLANOS')
    src = os.path.join(pl, '_candidatas', cand + '.png')
    assert os.path.exists(src), src
    ilus = os.path.join(pl, 'EI_%s_ilustracion.png' % clave)
    if os.path.exists(ilus):
        SP.aparta(ilus, 'reemplazada')
    c = SP.limpia(src, ilus, acento, True)
    if not acento:
        c['rojos_topados'] = round(topa_rojos(ilus), 3)
    gd = os.path.join(pl, '_grade')
    os.makedirs(gd, exist_ok=True)
    g = os.path.join(gd, 'EI_%s_ilustracion.png' % clave)
    if os.path.exists(g):
        SP.aparta(g, 'reemplazada')
    GR.graduar(ilus, g, reg, techo=True)
    c['rojos_post_grade'] = round(topa_rojos(g, tope=0.12 if not acento else 0.20,
                                             h_max=12), 3)
    m = GR.medir(g)
    lam = os.path.join(R.sub(clave, '02 LAMINA'), 'EI_%s_lamina.png' % clave)
    if os.path.exists(lam):
        SP.aparta(lam, 'rehecha')
    cuerpo, renglones = lamina(clave, g, lam, lado, ancho)
    ex = R.sub(clave, '05 EXPORTS')
    for nombre in ('EI_%s_lamina.png' % clave, 'EI_%s_lamina.jpg' % clave,
                   'EI_%s_ilustracion.png' % clave):
        p = os.path.join(ex, nombre)
        if os.path.exists(p):
            SP.aparta(p, 'reexportada')
    shutil.copy2(lam, os.path.join(ex, 'EI_%s_lamina.png' % clave))
    Image.open(lam).convert('RGB').save(os.path.join(ex, 'EI_%s_lamina.jpg' % clave),
                                        quality=92, subsampling=0)
    im = Image.open(g).convert('RGB')
    r = max(W / im.width, H_ / im.height)
    im = im.resize((int(im.width * r + .5), int(im.height * r + .5)), Image.LANCZOS)
    x, y = (im.width - W) // 2, (im.height - H_) // 2
    im.crop((x, y, x + W, y + H_)).save(os.path.join(ex, 'EI_%s_ilustracion.png' % clave))
    ent = os.path.join(R.unidad(PIEZAS[clave][1]), 'IMAGENES ENTREGA')
    os.makedirs(ent, exist_ok=True)
    dst = os.path.join(ent, ENTREGA[clave] + '.png')
    if os.path.exists(dst):
        SP.aparta(dst, 'reexportada')
    shutil.copy2(lam, dst)
    print('%s  %s  %-9s acento %-5s  color %s  grade %3.0f/%3.0f/%3.0f  '
          'cuerpo %d, %d renglones, panel %s %d'
          % (clave, cand, reg, acento, c, m[0], m[1], m[2], cuerpo, renglones,
             lado, ancho), flush=True)


if __name__ == '__main__':
    EL = json.load(open(ELEGIDAS, encoding='utf-8'))['_laminas']
    for k in [a.upper() for a in sys.argv[1:]] or sorted(EL):
        una(k, EL[k])
    print('LISTO')
