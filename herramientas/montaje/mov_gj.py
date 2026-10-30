# -*- coding: utf-8 -*-
r"""La pista V2 MOVIMIENTO de Gerencia judicial (es `mov_sit`).

    python mov_gj.py kling T4            conforma los crudos de Kling del T4
    python mov_gj.py luz T3               las rampas de luz del T3 (sin modelo)

Es `conformar_mov.py` del caso integrador apuntado a las situaciones, con lo
que ese conformado aprendio:

KLING (biblia §8: solo accion real o placa vacia con un elemento que cruza)
    1. ENCUADRE: el crudo se recorta al 88 % -el mismo encuadre de la ranura
       horneada- ANTES del retime. Sin eso, en cada fundido el encuadre
       saltaba un 12 % (el «ligero zoom» que Sebastian vio dos veces).
    2. COLOR: cada cuadro pasa por la misma limpieza de bandas de los
       detalles (franja fria/magenta x0,08, amarillo suelto, topes de piel):
       Kling sube la saturacion y el clip tiene que caer encima de una
       ranura limpia.
    3. LARGO: retime con setpts al largo de la ranura (Kling cobra segundos
       enteros; conserva los extremos, acelera o frena un poco la brisa).
    4. BORDES: 12 cuadros de alfa de ENTRADA contra LA RANURA HORNEADA
       MISMA. De SALIDA no hay fundido, y es a proposito (27 oct): el clip
       cubre la ranura entera y sale en el corte a la ranura siguiente, asi
       que no hay nada que empatar. El fundido de salida contra la placa
       quieta hacia REAPARECER lo que cruzo: medido en la hoja, la camioneta
       de A r03 y el camion de C r05 volvian a su sitio en los ultimos doce
       cuadros, como fantasma. En el caso integrador no se vio porque los
       clips eran de gente quieta y de luz.
    Se mide y se escribe: cuadro 0 contra la ranura (si no coincide el clip
    no arranco de la placa: §8, no sirve) y cuanto se mueve (diferencia
    media entre cuadros separados 12; ~0 = Kling congelo el plano).

LUZ (cuando lo unico que cambia es la luz no se gasta modelo)
    Se parte de la ranura horneada y se baja la luz cuadro a cuadro con una
    curva suave (smoothstep). `cielo`: pesa mas en lo claro -el cielo, el
    fondo- y deja las sombras quietas. `pantalla`: solo donde la imagen es
    casi blanca (la pantalla encendida), y solo en el ultimo segundo: la
    pantalla se apaga. El cuadro 0 es la ranura exacta.
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

import rutas_gj as R                                    # noqa: E402
import gj_pieza as SP                                   # noqa: E402
import detalle_gj as DS                                 # noqa: E402

FPS = '24000/1001'
FPS_N = 24000 / 1001.0
ENCUADRE = 0.88
MEZCLA = 12
W, Hh = 1920, 1080
CRUDOS = r'D:\DAE\_tmp\gj\mov\crudos'
TMP = r'D:\DAE\_tmp\gj\mov\_retime'

# (letra, ranura): (tipo, cuanto baja la luz, zona)
#   zona de 'pantalla' = poligono de la pantalla en 1920x1080; de 'faros' =
#   caja donde estan los faros. Medidas sobre el cuadro 0 de la ranura.
#   A r09 iba a Kling («las luces lejanas cruzan y se van») y Kling movio a
#   las tres personas (de perfil a espaldas, otra escala): descartado. Lo
#   que el plano pide es que los faros se vayan, y eso es LUZ: se apagan.
#   G r04: la primera version usaba «todo lo casi blanco» y agarro un
#   reflejo del fondo en vez de la pantalla (mancha negra arriba a la
#   derecha del telefono): ahora es el poligono de la pantalla.
# (tema, ranura): (tipo, cuanto baja la luz, zona). Lo que en Gerencia
# judicial solo cambia de luz y no pide modelo.
#   T3 r04 la empresa: el cielo baja un tono (atardecer).
#   T3 r08 de noche: nada se mueve; la lampara apenas (cielo con poco).
#   T4 r20 los testigos: contraluz, el cuarto se queda quieto.
LUZ = {('T3', 4): ('cielo', 0.16, None), ('T3', 8): ('cielo', 0.08, None),
       ('T4', 20): ('cielo', 0.10, None)}


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
                             '-i', '-', '-vf', vf, '-frames:v', str(frames),
                             '-c:v', 'libx264', '-crf', str(crf), '-preset', 'medium',
                             '-pix_fmt', 'yuv420p', '-an', out], stdin=subprocess.PIPE)


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


def kling(L, solo=None):
    os.makedirs(TMP, exist_ok=True)
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
        n0 = SP.cuadros(crudo)
        rt = os.path.join(TMP, nm + '.mp4')
        wr = escritor(rt, '24', 'setpts=%.9f*PTS,fps=%s' % (float(largo) / n0, FPS), largo)
        vf = 'crop=iw*%.4f:ih*%.4f,scale=%d:%d:flags=lanczos' % (ENCUADRE, ENCUADRE, W, Hh)
        movs, prev, primero = [], [], None
        for i, fr in enumerate(cuadros_rgb(crudo, vf)):
            o = DS.aplica(fr, ac, ge, 1.0)
            # el acento del curso, igual que en la ranura horneada (SP.ACENTO)
            o = SP.acento_serie(o, L, ac, n=n)
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
        m = min(MEZCLA, max(2, largo // 6))
        dur = m / FPS_N
        subprocess.run(
            ['ffmpeg', '-y', '-v', 'error', '-i', base, '-i', rt, '-filter_complex',
             '[1:v]format=yuva420p,fade=t=in:st=0:d=%.6f:alpha=1[m];'
             '[0:v][m]overlay=format=auto,format=yuv420p[v]' % dur,
             '-map', '[v]', '-frames:v', str(largo), '-c:v', 'libx264', '-crf', '14',
             '-preset', 'slow', '-pix_fmt', 'yuv420p', '-an', d], check=True)
        n1 = SP.cuadros(d)
        SP.w('%-40s crudo %3d -> %3d/%3d %s  cuadro0 vs ranura %5.1f  movimiento %s'
             % (nm, n0, n1, largo, 'OK' if n1 == largo else 'FALLA', d0,
                ' '.join('%.1f' % x for x in movs[:12])))


def suave(x):
    x = min(1.0, max(0.0, x))
    return x * x * (3 - 2 * x)


def luz(L, solo=None):
    from PIL import ImageDraw
    for (l, n), (tipo, cuanto, zona) in sorted(LUZ.items()):
        if l != L or (solo and n not in solo):
            continue
        nm, largo, base, d = ranura(L, n)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        SP.aparta(d, 'rehecho_%s' % time.strftime('%H%M%S'))
        wr = escritor(d, FPS, 'null', largo, crf=14)
        # cuando empieza y cuando termina de bajar la luz
        ini, fin = {'cielo': (0, largo - 1),
                    'pantalla': (max(0, largo - 34), largo - 4),
                    'faros': (int(largo * 0.30), int(largo * 0.80))}[tipo]
        zm = None
        if tipo == 'pantalla':
            zm = Image.new('L', (W, Hh), 0)
            ImageDraw.Draw(zm).polygon(zona, fill=255)
            zm = np.asarray(zm.filter(ImageFilter.GaussianBlur(4))).astype(np.float32) / 255.0
        elif tipo == 'faros':
            zm = np.zeros((Hh, W), np.float32)
            x0, y0, x1, y1 = zona
            zm[y0:y1, x0:x1] = 1.0
        for i, fr in enumerate(cuadros_rgb(base)):
            a = cuanto * suave((i - ini) / float(max(1, fin - ini)))
            f = fr.astype(np.float32) / 255.0
            y = f @ np.array([0.2126, 0.7152, 0.0722], np.float32)
            if tipo == 'cielo':
                peso = np.clip((y - 0.35) / 0.40, 0, 1)
                o = f * (1.0 - a * peso)[..., None]
            else:
                # lo claro DENTRO de la zona baja hasta el gris de su entorno
                umbral = 0.55 if tipo == 'pantalla' else 0.45
                mk = Image.fromarray((np.clip((y - umbral) / 0.15, 0, 1) * zm * 255)
                                     .astype(np.uint8), 'L')
                mk = mk.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(5))
                peso = np.asarray(mk).astype(np.float32) / 255.0
                piso = 0.18 if tipo == 'pantalla' else 0.12
                o = f + a * peso[..., None] * (np.minimum(f, piso) - f)
            wr.stdin.write(np.clip(o * 255 + 0.5, 0, 255).astype(np.uint8).tobytes())
        wr.stdin.close()
        wr.wait()
        n1 = SP.cuadros(d)
        SP.w('%-40s luz %-8s -%.2f  %3d/%3d %s' % (nm, tipo, cuanto, n1, largo,
                                                   'OK' if n1 == largo else 'FALLA'))


if __name__ == '__main__':
    paso, L = sys.argv[1], sys.argv[2].upper()
    solo = {int(x) for x in sys.argv[3:]} or None
    t0 = time.time()
    SP.w('===', paso, L)
    {'kling': kling, 'luz': luz}[paso](L, solo)
    SP.w('--- %.0f s' % (time.time() - t0))
    SP.w('LISTO')
