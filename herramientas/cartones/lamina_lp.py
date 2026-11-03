# -*- coding: utf-8 -*-
r"""Las LÁMINAS del curso Ley 1826 (U1: cinco; U3: tres), de la candidata
elegida a la entrega.

Es `lamina_sit` + `imagen_sit` (las láminas de «16 situaciones»), con el
texto del curso: el rótulo «CASO DE ESTUDIO N» y el texto VERBATIM -la
«Síntesis fáctica del caso» (U1) o la «Premisa fáctica» (U3)-. Nada más.

    python lamina_lp.py U1C1 U1C4 ...     (sin claves: todas las elegidas)

Por cada clave (`elegidas_lp.json` -> `_laminas`: candidata, lado, ancho,
registro):
    01 PLANOS/_candidatas/LP_<K>_img_<v>.png      la tirada escogida
    01 PLANOS/LP_<K>_ilustracion.png              limpia de color
    01 PLANOS/_grade/LP_<K>_ilustracion.png       grade por registro, con techo
    02 LAMINA/LP_<K>_lamina.png                   con el texto
    05 EXPORTS/LP_<K>_lamina.png  .jpg  _ilustracion.png
    <UNIDAD>\IMAGENES ENTREGA\<nombre de entrega>.png   la entrega

LA CURSIVA
    En la U1 C2 el documento pone «capítulo de hechos» en cursiva: se respeta
    (Montserrat Italic variable, peso 500 = Medium).
"""
import json
import os
import shutil
import sys

H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', 'prompts', 'cartones', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

from PIL import Image, ImageDraw, ImageFont             # noqa: E402

import cartones_ta as C                                 # noqa: E402
import rutas_lp as R                                    # noqa: E402
from guion_lp import PIEZAS, TEXTOS, CURSIVA, ENTREGA   # noqa: E402

W, H_ = 1920, 1080
AZUL = (0, 72, 144)
ALFA_PANEL = 209                 # 82 %, como las de 16 situaciones
AMARILLO = C.BAR_C[:3]
BLANCO = (255, 255, 255)
MARGEN_X = 86
MARGEN_Y = 120
FILETE = 10
SEP = 34
MARCA = r'E:\DAE MASTER\00 COMUNES\MARCA DE AGUA\APRENDE_CON_LA_DAE_alfa.png'
F_ITA = os.path.join(H, 'cartones', 'fuentes', 'Montserrat-Italic-VF.ttf')
ELEGIDAS = os.path.join(H, 'prompts', 'elegidas_lp.json')


def _ita(cuerpo):
    f = ImageFont.truetype(F_ITA, cuerpo)
    try:
        f.set_variation_by_axes([500])
    except Exception:                                     # noqa: BLE001
        pass
    return f


def _palabras(clave, texto):
    """[(palabra, cursiva)] respetando las frases en cursiva del documento."""
    marcas = []
    for frase in CURSIVA.get(clave, []):
        i = texto.find(frase)
        if i >= 0:
            marcas.append((i, i + len(frase)))
    out, pos = [], 0
    for w in texto.split(' '):
        i = texto.find(w, pos)
        pos = i + len(w)
        out.append((w, any(a <= i < b for a, b in marcas)))
    return out


def _partir(pals, fn, fi, draw, maxw):
    esp = draw.textlength(' ', font=fn)
    lineas, act, ancho = [], [], 0.0
    for w, it in pals:
        lw = draw.textlength(w, font=fi if it else fn)
        nuevo = lw if not act else ancho + esp + lw
        if act and nuevo > maxw:
            lineas.append(act)
            act, ancho = [(w, it)], lw
        else:
            act.append((w, it))
            ancho = nuevo
    if act:
        lineas.append(act)
    return lineas, esp


def _bloque(clave, alto_max, ancho):
    d = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
    pals = _palabras(clave, TEXTOS[clave])
    for cuerpo in range(40, 25, -1):
        fn, fi = C.fuente(C.F_MED, cuerpo), _ita(cuerpo)
        salto = int(round(cuerpo * 1.42))
        lineas, esp = _partir(pals, fn, fi, d, ancho)
        alto = salto * len(lineas)
        if alto <= alto_max:
            return fn, fi, esp, cuerpo, salto, lineas, alto
    raise SystemExit('%s: el texto no cabe ni a cuerpo 26' % clave)


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
    fn, fi, esp, cuerpo, salto, lineas, alto = _bloque(
        clave, H_ - 2 * MARGEN_Y - 70, ancho_txt)
    total = 30 + 34 + alto
    y = (H_ - total) // 2
    xt = x0 + MARGEN_X + FILETE + SEP
    d.rectangle([x0 + MARGEN_X, y - 6, x0 + MARGEN_X + FILETE, y + total + 4],
                fill=AMARILLO + (255,))
    d.text((xt, y), rotulo, font=f_rot, fill=AMARILLO + (255,))
    y += 30 + 34
    for ln in lineas:
        x = xt
        for j, (w, it) in enumerate(ln):
            f = fi if it else fn
            d.text((x, y), w, font=f, fill=BLANCO + (255,))
            x += d.textlength(w, font=f) + esp
        y += salto
    if os.path.exists(MARCA):
        m = Image.open(MARCA).convert('RGBA')
        m.thumbnail((300, 200))
        mx = W - m.width - 70 if lado == 'izq' else 70
        a = m.split()[3].point(lambda v: int(v * 0.9))
        m = Image.new('RGBA', m.size, BLANCO + (255,))
        m.putalpha(a)
        im.alpha_composite(m, (mx, 60))
    im.convert('RGB').save(salida)
    return cuerpo, len(lineas)


def una(clave, el):
    import sit_pieza as SP
    import graduar_registro as GR
    from imagen_sit import topa_rojos
    cand, lado, ancho, reg = el['candidata'], el['lado'], el['ancho'], el['registro']
    acento = el.get('acento', False)
    pl = R.sub(clave, '01 PLANOS')
    src = os.path.join(pl, '_candidatas', cand + '.png')
    assert os.path.exists(src), src
    ilus = os.path.join(pl, 'LP_%s_ilustracion.png' % clave)
    if os.path.exists(ilus):
        SP.aparta(ilus, 'reemplazada')
    c = SP.limpia(src, ilus, acento, True)
    if not acento:
        c['rojos_topados'] = round(topa_rojos(ilus), 3)
    gd = os.path.join(pl, '_grade')
    os.makedirs(gd, exist_ok=True)
    g = os.path.join(gd, 'LP_%s_ilustracion.png' % clave)
    if os.path.exists(g):
        SP.aparta(g, 'reemplazada')
    GR.graduar(ilus, g, reg, techo=True)
    c['rojos_post_grade'] = round(topa_rojos(g, tope=0.12 if not acento else 0.20,
                                             h_max=12), 3)
    m = GR.medir(g)
    lam = os.path.join(R.sub(clave, '02 LAMINA'), 'LP_%s_lamina.png' % clave)
    if os.path.exists(lam):
        SP.aparta(lam, 'rehecha')
    cuerpo, renglones = lamina(clave, g, lam, lado, ancho)
    ex = R.sub(clave, '05 EXPORTS')
    for nombre in ('LP_%s_lamina.png' % clave, 'LP_%s_lamina.jpg' % clave,
                   'LP_%s_ilustracion.png' % clave):
        p = os.path.join(ex, nombre)
        if os.path.exists(p):
            SP.aparta(p, 'reexportada')
    shutil.copy2(lam, os.path.join(ex, 'LP_%s_lamina.png' % clave))
    Image.open(lam).convert('RGB').save(os.path.join(ex, 'LP_%s_lamina.jpg' % clave),
                                        quality=92, subsampling=0)
    im = Image.open(g).convert('RGB')
    r = max(W / im.width, H_ / im.height)
    im = im.resize((int(im.width * r + .5), int(im.height * r + .5)), Image.LANCZOS)
    x, y = (im.width - W) // 2, (im.height - H_) // 2
    im.crop((x, y, x + W, y + H_)).save(os.path.join(ex, 'LP_%s_ilustracion.png' % clave))
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
