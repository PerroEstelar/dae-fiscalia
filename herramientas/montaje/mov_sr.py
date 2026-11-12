# -*- coding: utf-8 -*-
r"""La pista V2 MOVIMIENTO de los CASOS del curso SRPA (es `mov_da`/`mov_ei`).

    python mov_sr.py jpg NICO            las placas graduadas de escenas.KLING
                                         a JPEG de 2048 (D:\DAE\_tmp\sr\up\kling),
                                         para subirlas desde la nube
    python mov_sr.py kling NICO [n ...]  conforma los crudos de Kling

LO DE SIEMPRE (mov_da, mov_ei)
    1. ENCUADRE: el crudo se recorta al 88 % -el de la ranura horneada- antes
       del retime. Las caminatas hacia camara (`ABRE`) abren el encuadre del
       0,88 al 1,00 con smoothstep: la cabeza no se sale por arriba.
    2. LARGO: retime con setpts al largo de la ranura. Una ranura mas corta
       que el crudo NO se acelera: `crudos.json` trae `hasta` y el crudo llega
       ya cortado a (largo + 2) / 24 s (bajar_mov_sr).
    3. BORDES: corte seco (MEZCLA = 0). Ningun fundido contra una ranura que
       se mueve.
    4. COLOR: la limpieza por bandas de la placa, cuadro a cuadro
       (`sr_pieza.limpia_rgb`, con el chaleco acotado en las ranuras de los
       patrulleros).

LO NUEVO EN ESTE CURSO (12 nov)
    5. SATURACION IGUALADA A LA PLACA. Kling devuelve el clip 1,2-1,9x mas
       saturado que su placa (medido en DA). Se mide la saturacion media del
       cuadro 0 ya limpio contra la de la placa graduada y se aplica ese
       factor (tope 1,0: nunca se satura) a todo el clip, en RGB alrededor de
       la luminancia, para que el corte entre placa y clip no salte.
    6. Rec.709 ETIQUETADO, como las ranuras (`sr_pieza.BT709`).
    No se vuelve a pasar la curva GRIS: el cuadro inicial de Kling es la placa
    graduada, que ya la lleva.
"""
import os
import subprocess
import sys
import time

H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', 'prompts', 'cartones', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import numpy as np                                       # noqa: E402
from PIL import Image                                    # noqa: E402

import rutas_sr as R                                    # noqa: E402
import sr_pieza as SP                                   # noqa: E402

FPS = '24000/1001'
FPS_N = 24000 / 1001.0
ENCUADRE = 0.88
MEZCLA = 0
W, Hh = 1920, 1080
CRUDOS = r'D:\DAE\_tmp\sr\mov\crudos'
TMP = r'D:\DAE\_tmp\sr\mov\_retime'
UP = r'D:\DAE\_tmp\sr\up\kling'
# caminatas hacia camara: r42 el patrullero y Nico por el pasillo del CIP,
# r43 el defensor por el pasillo
ABRE = {('NICO', 42), ('NICO', 43)}
LUMA = np.array([0.2126, 0.7152, 0.0722], np.float32)


def ranura(L, n):
    largo = SP.E(L).R[n][0]
    nm = SP.nombre(L, n)
    tl = R.sub(L, '10 TIMELINE SEBASTIAN')
    return nm, largo, os.path.join(tl, 'RANURAS', '%s_v%d.mp4' % (nm, largo)), \
        os.path.join(tl, 'MOVIMIENTO', '%s_mov_v%d.mp4' % (nm, largo))


def lector(p, vf):
    return subprocess.Popen(['ffmpeg', '-v', 'error', '-i', p, '-vf', vf, '-f', 'rawvideo',
                             '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)


def escritor(out, entrada_fps, vf, frames, crf=12):
    return subprocess.Popen(['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo',
                             '-pix_fmt', 'rgb24', '-s', '%dx%d' % (W, Hh), '-r', entrada_fps,
                             '-i', '-', '-vf', vf + ',' + SP.BT709_VF, '-frames:v', str(frames),
                             '-c:v', 'libx264', '-crf', str(crf), '-preset', 'medium',
                             '-pix_fmt', 'yuv420p'] + SP.BT709 + ['-an', out],
                            stdin=subprocess.PIPE)


def cuadros_rgb(p, vf='null'):
    rd = lector(p, vf)
    while True:
        b = rd.stdout.read(W * Hh * 3)
        if len(b) < W * Hh * 3:
            break
        yield np.frombuffer(b, np.uint8).reshape(Hh, W, 3)
    rd.wait()


def dif(a, b):
    return float(np.abs(a.astype(np.int16) - b.astype(np.int16)).mean())


def sat_media(rgb):
    f = rgb.astype(np.float32)
    mx, mn = f.max(axis=2), f.min(axis=2)
    lit = mx > 40
    return float(((mx - mn) / np.maximum(mx, 1))[lit].mean()) if lit.any() else 0.0


def satura(rgb, k):
    if k >= 0.999:
        return rgb
    f = rgb.astype(np.float32)
    y = (f @ LUMA)[..., None]
    return np.clip(y + k * (f - y) + 0.5, 0, 255).astype(np.uint8)


def suave(x):
    x = min(1.0, max(0.0, x))
    return x * x * (3 - 2 * x)


def jpg(L, solo=None):
    """Las placas graduadas de escenas.KLING a JPEG de 2048 para Kling."""
    sal = os.path.join(UP, L)
    os.makedirs(sal, exist_ok=True)
    g = os.path.join(R.sub(L, '01 PLANOS'), '_grade')
    for n in sorted(SP.E(L).KLING):
        if solo and n not in solo:
            continue
        nm = SP.nombre(L, n)
        p = os.path.join(g, nm + '.png')
        if not os.path.exists(p):
            SP.w('FALTA %s' % nm)
            continue
        im = Image.open(p).convert('RGB')
        if im.width > 2048:
            im = im.resize((2048, int(round(im.height * 2048.0 / im.width))), Image.LANCZOS)
        d = os.path.join(sal, nm + '.jpg')
        im.save(d, 'JPEG', quality=93)
        SP.w('ok %s %d' % (nm, os.path.getsize(d)))


def kling(L, solo=None):
    os.makedirs(TMP, exist_ok=True)
    gd = os.path.join(R.sub(L, '01 PLANOS'), '_grade')
    for n in sorted(SP.E(L).R):
        if solo and n not in solo:
            continue
        nm, largo, base, d = ranura(L, n)
        crudo = os.path.join(CRUDOS, nm + '.mp4')
        if not os.path.exists(crudo):
            continue
        os.makedirs(os.path.dirname(d), exist_ok=True)
        SP.aparta(d, 'reconformado_%s' % time.strftime('%H%M%S'))
        ac, ge = SP.con_acento(L, n)
        ch = SP.chaleco(L, n)
        n0 = SP.cuadros(crudo)
        rt = os.path.join(TMP, nm + '.mp4')
        wr = escritor(rt, '24', 'setpts=%.9f*PTS,fps=%s' % (float(largo) / n0, FPS), largo)
        abre = (L, n) in ABRE
        if abre:
            vf = 'scale=%d:%d:flags=lanczos' % (W, Hh)
        else:
            vf = 'crop=iw*%.4f:ih*%.4f,scale=%d:%d:flags=lanczos' % (ENCUADRE, ENCUADRE, W, Hh)
        # la saturacion de la placa graduada, que es el cuadro inicial de Kling
        placa = np.asarray(Image.open(os.path.join(gd, nm + '.png')).convert('RGB')
                           .resize((W // 4, Hh // 4), Image.BILINEAR))
        s_placa = sat_media(placa)
        k = None
        movs, prev, primero = [], [], None
        for i, fr in enumerate(cuadros_rgb(crudo, vf)):
            if abre:
                f = ENCUADRE + (1.0 - ENCUADRE) * suave(i / float(max(1, n0 - 1)))
                cw, chh = W * f, Hh * f
                x0, y0 = (W - cw) / 2.0, (Hh - chh) / 2.0
                fr = np.asarray(Image.fromarray(fr).resize(
                    (W, Hh), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + chh)))
            o = SP.limpia_rgb(fr, ac, ge, ch)
            if k is None:
                s0 = sat_media(o[::4, ::4])
                k = min(1.0, s_placa / s0) if s0 > 0 else 1.0
            o = satura(o, k)
            if primero is None:
                primero = o
            if i % 12 == 0:
                if prev:
                    movs.append(dif(o[::4, ::4], prev[-1]))
                prev.append(o[::4, ::4].copy())
            wr.stdin.write(o.tobytes())
        wr.stdin.close()
        wr.wait()
        b0 = next(cuadros_rgb(base))
        d0 = dif(primero, b0)
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', rt,
                        '-vf', 'tpad=stop_mode=clone:stop=4', '-frames:v', str(largo),
                        '-c:v', 'libx264', '-crf', '14', '-preset', 'slow',
                        '-pix_fmt', 'yuv420p'] + SP.BT709 + ['-an', d], check=True)
        n1 = SP.cuadros(d)
        SP.w('%-40s crudo %3d -> %3d/%3d %s  sat x%.2f  cuadro0 vs ranura %5.1f  movimiento %s'
             % (nm, n0, n1, largo, 'OK' if n1 == largo else 'FALLA', k, d0,
                ' '.join('%.1f' % x for x in movs[:12])))


if __name__ == '__main__':
    paso, L = sys.argv[1], sys.argv[2].upper()
    solo = {int(x) for x in sys.argv[3:]} or None
    t0 = time.time()
    SP.w('===', paso, L)
    {'kling': kling, 'jpg': jpg}[paso](L, solo)
    SP.w('--- %.0f s' % (time.time() - t0))
    SP.w('LISTO')
