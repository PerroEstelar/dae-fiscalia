# -*- coding: utf-8 -*-
r"""De cada master salen las dos entregas.

ENTREGA FISCALIA
    x264 crf 18, preset slow, tune animation, yuv420p, high@4.0, GOP fijo
    de 48 con min 24, scenecut 40, audio copiado y faststart. Es la receta
    que ya quedo escrita en `Entrega_MP4_Fiscalia_Receta`.

COPIA PARA REVISAR
    720p lanczos, crf 25, preset medium, tune animation, AAC 128k,
    faststart. Es para mirar los cinco capitulos en el telefono, no para
    entregar.

SE MIDE LO QUE SALIO
    Cuadros y duracion de los tres archivos. Un master y una entrega con
    distinto numero de cuadros es un corte perdido, y eso no se ve en el
    tamano del archivo.
"""
import os
import subprocess
import sys

sys.path.insert(0, 'D:/DAE/_repo/herramientas/prompts')
import plan_camara_df as PC                        # noqa: E402

REN = r'D:\DAE\_tmp\df\render'
FISCALIA = ['-c:v', 'libx264', '-crf', '18', '-preset', 'slow',
            '-tune', 'animation', '-pix_fmt', 'yuv420p',
            '-profile:v', 'high', '-level', '4.0',
            '-x264-params', 'keyint=48:min-keyint=24:scenecut=40',
            '-c:a', 'copy', '-movflags', '+faststart']
LIGERA = ['-vf', 'scale=1280:720:flags=lanczos', '-c:v', 'libx264',
          '-crf', '25', '-preset', 'medium', '-tune', 'animation',
          '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '128k',
          '-movflags', '+faststart']


def mide(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
                        '-count_frames', '-show_entries',
                        'stream=nb_read_frames,width,height',
                        '-show_entries', 'format=duration',
                        '-of', 'default=nw=1:nk=1', p],
                       capture_output=True, text=True).stdout.split()
    return r


print('%-28s %10s %10s %10s' % ('', 'master', 'fiscalia', 'ligera'), flush=True)
CAPS = [int(a) for a in sys.argv[1:]] or [1, 2, 3, 4, 5]
for cap in CAPS:
    m = os.path.join(REN, 'DF_C%d_master.mp4' % cap)
    if not os.path.exists(m):
        print('cap %d: no hay master' % cap, flush=True)
        continue
    exp = os.path.join(PC.RAIZ, PC.CAPS[cap], '05 EXPORTS')
    os.makedirs(exp, exist_ok=True)
    f = os.path.join(exp, 'DF_C%d_v1.mp4' % cap)
    l = os.path.join(exp, 'DF_C%d_v1_revision_720p.mp4' % cap)
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', m] + FISCALIA + [f],
                   check=True)
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', m] + LIGERA + [l],
                   check=True)
    a, b, c = mide(m), mide(f), mide(l)
    print('cap %d cuadros           %10s %10s %10s %s'
          % (cap, a[2], b[2], c[2], 'OK' if a[2] == b[2] == c[2] else 'NO CUADRA'),
          flush=True)
    print('       MB                %10d %10d %10d'
          % (os.path.getsize(m) // 1048576, os.path.getsize(f) // 1048576,
             os.path.getsize(l) // 1048576), flush=True)
    print('       duracion s        %10.2f %10.2f %10.2f'
          % (float(a[3]), float(b[3]), float(c[3])), flush=True)
    assert a[2] == b[2] == c[2], (cap, a[2], b[2], c[2])
print('LISTO', flush=True)
