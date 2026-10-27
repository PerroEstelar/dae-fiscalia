# -*- coding: utf-8 -*-
r"""Las situaciones en IMAGEN, de la candidata elegida a la entrega.

    python imagen_sit.py F G H I J K

Por cada letra (`elegidas_sit.json` -> `_imagenes`: idea, tirada, lado libre,
ancho del panel):

    01 PLANOS/_candidatas/SIT_X_img_<idea>_<tirada>.png   la tirada escogida
    01 PLANOS/SIT_X_ilustracion.png       limpia de color (sit_pieza.limpia)
    01 PLANOS/_grade/SIT_X_ilustracion.png  grade por registro, con techo
    02 LAMINA/SIT_X_lamina.png            con el contexto verbatim
    05 EXPORTS/SIT_X_lamina.png  .jpg     la entrega
    05 EXPORTS/SIT_X_ilustracion.png      la ilustracion sola, 1920 x 1080

La limpieza y el grade son los mismos de los videos: una lamina y un video
de la misma situacion tienen que verse de la misma serie. La G existe en las
dos formas y aqui va su forma de IMAGEN.
"""
import json
import os
import shutil
import sys

H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', 'prompts', 'cartones', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

from PIL import Image                                    # noqa: E402

import rutas_sit as R                                    # noqa: E402
import sit_pieza as SP                                   # noqa: E402
import lamina_sit as LM                                  # noqa: E402
import imagenes_sit_creativas as IC                      # noqa: E402
import base_sit as S                                     # noqa: E402

EL = json.load(open(os.path.join(H, 'prompts', 'elegidas_sit.json'),
                    encoding='utf-8'))['_imagenes']


def topa_rojos(p, tope=0.14, h_max=14, rampa=6):
    """Las yemas y nudillos rosados. `limpia` deja entera la banda calida
    (0-27) porque ahi vive la piel; pero en la J salieron dedos con la punta
    ROJA (tono 0-10, saturacion 0,32) y la regla de piel es gris calido,
    nunca rosado. En las laminas SIN acento se topa la saturacion de los
    rojos (tono <= 14 en escala PIL, unos 20 grados) a `tope`, con rampa; la
    mostaza vive arriba de 20 grados y no se toca."""
    import numpy as np
    from PIL import ImageFilter
    im = Image.open(p).convert('RGB')
    hsv = np.array(im.convert('HSV')).astype(np.float32)
    h, s = hsv[..., 0], hsv[..., 1]
    w = np.clip((h_max + rampa - h) / float(rampa), 0, 1)
    w = np.array(Image.fromarray((w * 255).astype(np.uint8))
                 .filter(ImageFilter.GaussianBlur(3))).astype(np.float32) / 255
    hsv[..., 1] = s - w * np.clip(s - tope * 255, 0, None)
    Image.fromarray(np.clip(hsv, 0, 255).astype(np.uint8), 'HSV').convert('RGB').save(p)
    return float((w > 0.5).mean())


def una(L):
    idea, tirada, lado, ancho = EL[L]
    var = idea.split('_')[1]
    reg, gente, ext, lado_p, txt = IC.IM[L][var]
    assert lado == lado_p, (L, lado, lado_p)
    pl = R.sub(L, '01 PLANOS', 'imagen')
    src = os.path.join(pl, '_candidatas', 'SIT_%s_%s_%s.png' % (L, idea, tirada))
    assert os.path.exists(src), src
    ilus = os.path.join(pl, 'SIT_%s_ilustracion.png' % L)
    if os.path.exists(ilus):
        SP.aparta(ilus, 'reemplazada')
    acento = any(p in S.CON_ACENTO for p in gente) or 'mustard' in txt.lower()
    c = SP.limpia(src, ilus, acento, bool(gente))
    if not acento:
        c['rojos_topados'] = round(topa_rojos(ilus), 3)
    gd = os.path.join(pl, '_grade')
    os.makedirs(gd, exist_ok=True)
    g = os.path.join(gd, 'SIT_%s_ilustracion.png' % L)
    import graduar_registro as GR
    GR.graduar(ilus, g, reg, techo=True)
    # el grade SUBE la saturacion (medido en la J: yemas 0,15 -> 0,27 rojo):
    # el tope de rojos se vuelve a pasar sobre la graduada. Con acento se
    # topa solo el rojo/rosado (la mostaza vive arriba de 20 grados).
    c['rojos_post_grade'] = round(topa_rojos(g, tope=0.12 if not acento else 0.20,
                                             h_max=12), 3)
    m = GR.medir(g)
    lam = os.path.join(R.sub(L, '02 LAMINA', 'imagen'), 'SIT_%s_lamina.png' % L)
    if os.path.exists(lam):
        SP.aparta(lam, 'rehecha')
    cuerpo, renglones = LM.lamina(L, g, lam, lado, ancho)
    ex = R.sub(L, '05 EXPORTS', 'imagen')
    os.makedirs(ex, exist_ok=True)
    for nombre in ('SIT_%s_lamina.png' % L, 'SIT_%s_lamina.jpg' % L,
                   'SIT_%s_ilustracion.png' % L):
        p = os.path.join(ex, nombre)
        if os.path.exists(p):
            SP.aparta(p, 'reexportada')
    shutil.copy2(lam, os.path.join(ex, 'SIT_%s_lamina.png' % L))
    Image.open(lam).convert('RGB').save(os.path.join(ex, 'SIT_%s_lamina.jpg' % L),
                                        quality=92, subsampling=0)
    im = Image.open(g).convert('RGB')
    if im.size != (LM.W, LM.H):
        im = im.resize((LM.W, LM.H), Image.LANCZOS)
    im.save(os.path.join(ex, 'SIT_%s_ilustracion.png' % L))
    print('%s  %s/%s  %-9s acento %-5s  color %s  grade %3.0f/%3.0f/%3.0f  '
          'lamina cuerpo %d, %d renglones, panel %s %d'
          % (L, idea, tirada, reg, acento, c, m[0], m[1], m[2], cuerpo,
             renglones, lado, ancho), flush=True)


if __name__ == '__main__':
    for L in [a.upper() for a in sys.argv[1:]] or sorted(EL):
        una(L)
    print('LISTO')
