# -*- coding: utf-8 -*-
r"""Los INSERTOS DE DETALLE de las situaciones (pista V3 DETALLE).

    python detalle_sit.py placas A            candidata elegida -> placa graduada
    python detalle_sit.py conformar A [nombre ...]   crudo de Kling -> DETALLE

Biblia §12: un detalle es un plano de 3-4 s que entra DENTRO de su ranura
madre (nunca en los primeros 40-60 cuadros, nunca cruzando un corte), hecho
con la placa madre graduada como referencia, y con la piel igualada a la
madre. El movimiento es el gesto de una mano sobre su propio objeto; todo lo
demas quieto.

PLACAS
    01 PLANOS/_candidatas/<det>_<tirada>.png   (tirada en elegidas_sit.json
                                                -> "_detalles")
    01 PLANOS/DETALLE/<det>.png         limpieza de bandas de la madre
                                        (acento y gente de la madre) + piel
                                        igualada a la madre
    01 PLANOS/DETALLE/_grade/<det>.png  grade con el registro de la madre
    Esa ultima es la que se sube y va de cuadro inicial a Kling.

CONFORMAR
    D:\DAE\_tmp\sit\det\crudos\<det>.mp4  (lo que entrego Kling)
    -> cuadro 0 contra la placa (si no coincide, el clip no sirve: §8)
    -> cada cuadro: franja fria/magenta x0,08, amarillo suelto x0,15 si la
       madre no lleva acento, y la banda calida (piel) por el MISMO factor
       medido en el cuadro 0 contra la madre (un factor por clip: si se
       midiera cuadro a cuadro la piel parpadearia)
    -> retime a los cuadros del detalle (setpts) a 23,976
    -> 10 TIMELINE SEBASTIAN/DETALLE/<det>_v<cuadros>.mp4
    y una hoja: madre | cuadro 0 | medio | ultimo, para mirar.

La PIEL: la regla es gris calido, nunca rosado. Medido en las candidatas de
la A/B/C, las manos de los detalles salen mas calidas que las de la madre
(el plano cerrado le da a la mano mas area y el modelo la «colorea»). Se
toma el p90 de saturacion de la banda calida (tono PIL 0-27, solo pixeles
con s > 0,04 e iluminados) de la madre y del detalle; si el detalle pasa,
se baja por el cociente. Nunca se sube.
"""
import json
import os
import subprocess
import sys
import time

H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', 'prompts', 'cartones', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import numpy as np                                       # noqa: E402
from PIL import Image, ImageFilter                       # noqa: E402

import rutas_sit as R                                    # noqa: E402
import sit_pieza as SP                                   # noqa: E402

TMP = r'D:\DAE\_tmp\sit'
CRUDOS = os.path.join(TMP, 'det', 'crudos')

# Cuantos cuadros del crudo se usan, cuando el final no sirve. Se mira cuadro
# a cuadro y se corta ANTES del problema; el retime estira lo que queda.
#   B r05: desde el cuadro ~70 entra una SEGUNDA mano por la derecha (la
#   biblia: «no new hand enters»). Se usan 0-64 (65 cuadros -> 90, x0,72:
#   el gesto es lento de por si).
#   G r03: igual, una mano rosada asoma arriba a la izquierda desde el ~64.
#   Se usan 0-59 (60 -> 72).
CORTE = {'SIT_B_r05_el_telefono_boca_abajo_det': 65,
         'SIT_G_r03_la_mano_en_el_marco_det': 60}
FPS = '24000/1001'
W, Hh = 1920, 1080


def specs(L):
    d = json.load(open(os.path.join(TMP, 'prompts_sit_%s.json' % L), encoding='utf-8'))
    return d['detalles']


def madre_grade(L, n):
    return os.path.join(R.sub(L, '01 PLANOS'), '_grade', SP.nombre(L, n) + '.png')


def p90_calida(hsv):
    h, s, v = hsv[..., 0], hsv[..., 1] / 255.0, hsv[..., 2]
    m = (v > 40) & (s > 0.04) & (h <= 27)
    return float(np.percentile(s[m], 90)) if m.sum() > 500 else 0.0


def pesos(h, acento, gente, k_piel):
    k = np.ones_like(h)
    k = np.minimum(k, 1 - SP._peso_banda(h, 66, 262) * (1 - 0.08))
    if not acento:
        k = np.minimum(k, 1 - SP._peso_banda(h, 30, 54) * (1 - 0.15))
    if not acento and not gente:
        k = np.minimum(k, 0.15)
    if k_piel < 1.0:
        piel = SP._peso_banda(h, 0, 21, rampa=6.0)
        k = np.minimum(k, 1 - piel * (1 - k_piel))
    km = Image.fromarray(np.clip(k * 255, 0, 255).astype(np.uint8), 'L')
    km = km.filter(ImageFilter.GaussianBlur(6))
    return np.asarray(km).astype(np.float32) / 255.0


def topes(hsv, acento):
    """Topes absolutos de piel, despues del factor relativo. El factor solo
    no basta: la madre de C r10 ya traia la mano a 0,31 y el detalle salio
    «igual de rosado». La regla es gris calido con s <= 0,20:
      - rosado/rojo (tono PIL <= 12, unos 17 grados, rampa 4): tope 0,20
        SIEMPRE -la mostaza vive arriba de 20 grados-;
      - sin acento: toda la banda calida (0-27) a tope 0,22."""
    h, s = hsv[..., 0], hsv[..., 1]
    wr = np.clip((16.0 - h) / 4.0, 0, 1)
    s = s - wr * np.clip(s - 0.20 * 255, 0, None)
    if not acento:
        wc = SP._peso_banda(h, 0, 27, rampa=4.0)
        s = s - wc * np.clip(s - 0.22 * 255, 0, None)
    hsv[..., 1] = s
    return hsv


def aplica(rgb, acento, gente, k_piel):
    hsv = np.asarray(Image.fromarray(rgb).convert('HSV')).astype(np.float32)
    hsv[..., 1] *= pesos(hsv[..., 0], acento, gente, k_piel)
    hsv = topes(hsv, acento)
    return np.asarray(Image.fromarray(np.clip(hsv, 0, 255).astype(np.uint8), 'HSV')
                      .convert('RGB'))


def tono_acento(hsv):
    """Mediana del tono del acento (mostaza/naranja: tono PIL 12-45 con
    saturacion > 0,30), o None si el acento no ocupa ni el 0,5 % del cuadro."""
    h, s = hsv[..., 0], hsv[..., 1] / 255.0
    m = (h >= 12) & (h <= 45) & (s > 0.30)
    return float(np.median(h[m])) if m.mean() > 0.005 else None


def gira_acento(rgb, delta):
    """Corre el tono del acento `delta` unidades PIL, solo en su banda y con
    rampa: la piel (tono < 12) y el resto no se tocan."""
    hsv = np.asarray(Image.fromarray(rgb).convert('HSV')).astype(np.float32)
    h, s = hsv[..., 0], hsv[..., 1] / 255.0
    w = SP._peso_banda(h, 14, 45, rampa=4.0) * np.clip((s - 0.20) / 0.10, 0, 1)
    hsv[..., 0] = h + w * delta
    return np.asarray(Image.fromarray(np.clip(hsv, 0, 255).astype(np.uint8), 'HSV')
                      .convert('RGB'))


def factor_piel(madre_hsv, det_hsv):
    a, b = p90_calida(madre_hsv), p90_calida(det_hsv)
    if b <= 0 or a <= 0 or b <= a:
        return 1.0, a, b
    return max(0.3, a / b), a, b


def hsv_de(p):
    return np.asarray(Image.open(p).convert('HSV')).astype(np.float32)


# ---------------------------------------------------------------- placas
def placas(L):
    import graduar_registro as GR
    el = json.load(open(SP.ELEGIDAS, encoding='utf-8'))['_detalles'][L]
    pl = R.sub(L, '01 PLANOS')
    dd = os.path.join(pl, 'DETALLE')
    gd = os.path.join(dd, '_grade')
    os.makedirs(gd, exist_ok=True)
    for nm, sp in sorted(specs(L).items()):
        n = sp['ranura']
        v = el.get(str(n))
        if not v:
            SP.w('%s  sin tirada elegida' % nm)
            continue
        src = os.path.join(pl, '_candidatas', '%s_%s.png' % (nm, v))
        assert os.path.exists(src), src
        dst = os.path.join(dd, nm + '.png')
        g = os.path.join(gd, nm + '.png')
        for p in (dst, g):
            SP.aparta(p, 'reemplazada_%s' % time.strftime('%H%M%S'))
        ac, ge = SP.con_acento(L, n)
        rgb = np.asarray(Image.open(src).convert('RGB').resize((W, Hh), Image.LANCZOS))
        mh = hsv_de(madre_grade(L, n))
        # la limpieza va primero (sin piel); la piel se mide despues de ella
        limpio = aplica(rgb, ac, ge, 1.0)
        k, a, b = factor_piel(mh, np.asarray(Image.fromarray(limpio).convert('HSV'))
                              .astype(np.float32))
        Image.fromarray(aplica(limpio, ac, ge, k) if k < 1 else limpio).save(dst)
        reg = SP.E(L).R[n][1]
        GR.graduar(dst, g, reg, techo=True)
        m = GR.medir(g)
        gh = hsv_de(g)
        SP.w('%s %s  acento %-5s  piel madre %.3f det %.3f -> x%.2f -> %.3f  '
             '%-9s %3.0f/%3.0f/%3.0f' % (nm, v, ac, a, b, k, p90_calida(gh), reg,
                                          m[0], m[1], m[2]))


# ---------------------------------------------------------------- conformar
def cuadros_de(p):
    return SP.cuadros(p)


def conformar(L, solo=None):
    tl = R.sub(L, '10 TIMELINE SEBASTIAN')
    sal_d = os.path.join(tl, 'DETALLE')
    os.makedirs(sal_d, exist_ok=True)
    hojas = []
    for nm, sp in sorted(specs(L).items()):
        if solo and nm not in solo:
            continue
        n, cuad = sp['ranura'], sp['cuadros']
        largo = SP.E(L).R[n][0]
        assert sp['entra'] >= 30 and sp['entra'] + cuad <= largo, (nm, sp, largo)
        crudo = os.path.join(CRUDOS, nm + '.mp4')
        if not os.path.exists(crudo):
            SP.w('%s  FALTA crudo' % nm)
            continue
        kf = os.path.join(R.sub(L, '01 PLANOS'), 'DETALLE', '_grade', nm + '.png')
        ac, ge = SP.con_acento(L, n)
        n0 = cuadros_de(crudo)
        if nm in CORTE:
            n0 = min(n0, CORTE[nm])
        rd = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', crudo, '-vf',
                               'scale=%d:%d:flags=lanczos' % (W, Hh), '-frames:v', str(n0),
                               '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                              stdout=subprocess.PIPE)
        out = os.path.join(sal_d, '%s_v%d.mp4' % (nm, cuad))
        SP.aparta(out, 'reconformado_%s' % time.strftime('%H%M%S'))
        wr = subprocess.Popen(['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo',
                               '-pix_fmt', 'rgb24', '-s', '%dx%d' % (W, Hh), '-r', '24',
                               '-i', '-', '-vf',
                               'setpts=%.9f*PTS,fps=%s' % (float(cuad) / n0, FPS),
                               '-frames:v', str(cuad), '-c:v', 'libx264', '-crf', '12',
                               '-preset', 'medium', '-pix_fmt', 'yuv420p', '-an', out],
                              stdin=subprocess.PIPE)
        mh = hsv_de(madre_grade(L, n))
        kfa = np.asarray(Image.open(kf).convert('RGB').resize((W, Hh), Image.LANCZOS))
        i, k, d0, muestras, giro = 0, None, None, {}, 0.0
        while True:
            buf = rd.stdout.read(W * Hh * 3)
            if len(buf) < W * Hh * 3:
                break
            fr = np.frombuffer(buf, np.uint8).reshape(Hh, W, 3)
            if k is None:
                d0 = float(np.abs(fr.astype(np.int16) - kfa.astype(np.int16)).mean())
                k, a, b = factor_piel(mh, np.asarray(Image.fromarray(aplica(fr, ac, ge, 1.0))
                                                     .convert('HSV')).astype(np.float32))
                # el acento del detalle tiene que ser el MISMO color que el de
                # la madre: en A r10 la madre salio naranja y el detalle
                # mostaza, y en el corte se ve el cambio de prenda
                ta, td = tono_acento(mh), tono_acento(np.asarray(
                    Image.fromarray(fr).convert('HSV')).astype(np.float32))
                giro = (ta - td) if (ac and ta is not None and td is not None) else 0.0
                giro = float(np.clip(giro, -12, 12))
            if abs(giro) >= 1.0:
                fr = gira_acento(fr, giro)
            o = aplica(fr, ac, ge, k)
            if i in (0, n0 // 2, n0 - 1):
                muestras[i] = o
            wr.stdin.write(o.tobytes())
            i += 1
        rd.wait()
        wr.stdin.close()
        wr.wait()
        n1 = cuadros_de(out)
        ult = muestras.get(n0 - 1, muestras.get(max(muestras) if muestras else 0))
        ph = p90_calida(np.asarray(Image.fromarray(ult).convert('HSV')).astype(np.float32))
        SP.w('%s  crudo %d -> %d/%d %s  cuadro0 vs placa %.1f  piel madre %.3f '
             'crudo %.3f x%.2f -> %.3f  acento giro %+.1f  entra %d en ranura de %d'
             % (nm, n0, n1, cuad, 'OK' if n1 == cuad else 'FALLA', d0, a, b, k, ph,
                giro, sp['entra'], largo))
        fila = [Image.open(madre_grade(L, n)).convert('RGB')] + \
            [Image.fromarray(muestras[j]) for j in sorted(muestras)]
        hojas.append(fila)
    if hojas:
        tw, th = 480, 270
        hoja = Image.new('RGB', (tw * 4, th * len(hojas)), (20, 20, 20))
        for r, fila in enumerate(hojas):
            for c, im in enumerate(fila[:4]):
                hoja.paste(im.resize((tw, th)), (c * tw, r * th))
        hp = os.path.join(TMP, 'det_%s.jpg' % L)
        hoja.save(hp, quality=85)
        SP.w('hoja', hp)


if __name__ == '__main__':
    paso, L = sys.argv[1], sys.argv[2].upper()
    t0 = time.time()
    SP.w('===', paso, L)
    if paso == 'placas':
        placas(L)
    elif paso == 'conformar':
        conformar(L, set(sys.argv[3:]) or None)
    SP.w('--- %.0f s' % (time.time() - t0))
    SP.w('LISTO')
