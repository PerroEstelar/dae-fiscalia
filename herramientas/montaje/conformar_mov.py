# -*- coding: utf-8 -*-
r"""Conforma los clips de movimiento: los retimea a la ranura Y les funde
los bordes CONTRA LA RANURA HORNEADA.

PASO 1 - EL LARGO
    Kling cobra por segundo entero y entrega a 24 fps; las ranuras no caen
    en segundos redondos. r03 son 145 cuadros -6,05 s- y el clip mas corto
    que la cubre son 7 s, que vuelven 169 cuadros. Se retimea con `setpts`:
    conserva los dos extremos y acelera un 17 % una brisa. No se ve.

PASO 2 - LOS BORDES
    Los clips se generan con cuadro inicial y SIN cuadro final, porque el
    ancla de salida los congelaba (medido: 0,2 de movimiento entre cuadros
    contra 0,8 sin ancla). Entonces su ultimo cuadro ya no es la placa.

    La idea original era resolverlo con una disolvencia en la linea, pero
    la API de Resolve no pone transiciones ni anima la opacidad de un item:
    `GetProperty` trae Opacity y no hay `AddKeyframe`. Asi que la fundida
    se HORNEA AQUI, y mejor: no se funde contra un negro ni contra la placa
    quieta, sino contra LA RANURA HORNEADA MISMA -que lleva su movimiento
    de camara-, asi que en los primeros y ultimos doce cuadros el clip de
    V2 es identico pixel a pixel a lo que hay en V1 debajo.

    Resultado: V2 entra y sale sin salto, y apagar la pista sigue dejando
    la pieza completa. Que era todo el punto de la pista aparte.
"""
import os
import subprocess
import sys

sys.path.insert(0, 'D:/DAE/_repo/herramientas/prompts')
import movimiento_df as M                          # noqa: E402
import plan_camara_df as PC                        # noqa: E402
from armar_df import NOMBRE                        # noqa: E402

FPS = '24000/1001'
FPS_N = 23.976
ENT = r'D:\DAE\_tmp\df\mov\crudos'
TMP = r'D:\DAE\_tmp\df\mov\_retime'
os.makedirs(TMP, exist_ok=True)


def cuadros(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
                        '-count_frames', '-show_entries', 'stream=nb_read_frames',
                        '-of', 'default=nw=1:nk=1', p],
                       capture_output=True, text=True)
    return int(r.stdout.split()[0])


print('%-44s %6s %6s %6s %6s' % ('clip', 'crudo', 'ranura', 'final', 'borde'),
      flush=True)
for (cap, ran), (largo, _) in sorted(M.MOV.items()):
    nm = 'DF_C%d_r%02d_%s' % (cap, ran, NOMBRE[cap][ran])
    o = os.path.join(ENT, nm + '.mp4')
    tl = os.path.join(PC.RAIZ, PC.CAPS[cap], '10 TIMELINE SEBASTIAN')
    base = os.path.join(tl, 'RANURAS', '%s_v%d.mp4' % (nm, largo))
    if not os.path.exists(o) or not os.path.exists(base):
        print('%-44s  FALTA' % nm, flush=True)
        continue
    sal = os.path.join(tl, 'MOVIMIENTO')
    os.makedirs(sal, exist_ok=True)
    d = os.path.join(sal, '%s_mov_v%d.mp4' % (nm, largo))

    n0 = cuadros(o)
    rt = os.path.join(TMP, nm + '.mp4')
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', o,
                    '-vf', 'setpts=%.9f*PTS,fps=%s' % (float(largo) / n0, FPS),
                    '-frames:v', str(largo), '-c:v', 'libx264', '-crf', '12',
                    '-preset', 'medium', '-pix_fmt', 'yuv420p', '-an', rt],
                   check=True)

    m = min(M.MEZCLA, max(2, largo // 6))
    dur = m / FPS_N
    st = (largo - 1 - m) / FPS_N
    subprocess.run(
        ['ffmpeg', '-y', '-v', 'error', '-i', base, '-i', rt, '-filter_complex',
         '[1:v]format=yuva420p,'
         'fade=t=in:st=0:d=%.6f:alpha=1,'
         'fade=t=out:st=%.6f:d=%.6f:alpha=1[m];'
         '[0:v][m]overlay=format=auto,format=yuv420p[v]' % (dur, st, dur),
         '-map', '[v]', '-frames:v', str(largo),
         '-c:v', 'libx264', '-crf', '14', '-preset', 'slow',
         '-pix_fmt', 'yuv420p', '-an', d], check=True)

    n1 = cuadros(d)
    print('%-44s %6d %6d %6d %6d %s'
          % (nm, n0, largo, n1, m, 'OK' if n1 == largo else 'FALLA'), flush=True)
    assert n1 == largo, (nm, n1, largo)
print('LISTO', flush=True)
