# -*- coding: utf-8 -*-
r"""Clip compuesto de cada video de profe del curso SRPA y justicia restaurativa.

Entra la grabación de Teams (1280×720, 30 fps, BT.601 sin etiquetar bien) y sale
un 1920×1080 a 30 fps, Rec.709 etiquetado:
- La ventana de `srpa.VENTANA` desde `xy` (1143×643, ×1,68): el profe queda a la
  derecha y a la izquierda la caja de cartones, como en Delitos ambientales.
- Los tramos de `srpa.TRAMOS` (cortes de tomas falsas), cada uno con su ventana;
  los cortes de audio caen en silencios y llevan fundidos de 15 ms.
- Audio a −19 LUFS con una ganancia fija (`ganancia`, medida sobre el original
  con ebur128) y un limitador a −1,5 dBFS: los originales traen picos sobre 0.

    python srpa_composicion.py u3c            un video
    python srpa_composicion.py u3c 200        un cuadro de prueba en el segundo 200 (de la fuente)
    python srpa_composicion.py todos          los siete, en serie
"""
import glob
import os
import subprocess
import sys

sys.path.insert(0, r'D:\DAE\_repo\cursos\srpa-justicia-restaurativa')
import srpa as S  # noqa: E402

FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
FADE = 0.015


def original(clave):
    return '%s/01 VIDEO/%s' % (S.carpeta(clave), S.VIDEOS[clave]['original'])


def duracion(p):
    return float(subprocess.run([FB + '/ffprobe.exe', '-v', 'error', '-show_entries', 'format=duration',
                                 '-of', 'csv=p=0', p], capture_output=True, text=True).stdout)


def ventana(clave, v):
    if v:
        return v
    w, h = S.VENTANA
    x, y = S.VIDEOS[clave]['xy']
    return (x, y, w, h)


def escala(x, y, w, h):
    return ('crop=%d:%d:%d:%d,scale=1920:1080:flags=lanczos:in_color_matrix=bt601:'
            'out_color_matrix=bt709:out_range=tv,setsar=1' % (w, h, x, y))


def filtro(clave, fin_fuente):
    tr = S.tramos(clave)
    v, a = [], []
    for i, (t0, t1, win) in enumerate(tr):
        t1 = fin_fuente if t1 is None else t1
        v.append('[0:v]trim=start=%.3f:end=%.3f,setpts=PTS-STARTPTS,%s[v%d]' % (t0, t1, escala(*ventana(clave, win)), i))
        # fundido solo donde hay corte de verdad (no entre tramos contiguos)
        corte_in = i > 0 and tr[i - 1][1] != t0
        corte_out = i < len(tr) - 1 and tr[i + 1][0] != t1
        af = 'atrim=start=%.3f:end=%.3f,asetpts=PTS-STARTPTS' % (t0, t1)
        if corte_in:
            af += ',afade=t=in:d=%.3f' % FADE
        if corte_out:
            af += ',afade=t=out:st=%.3f:d=%.3f' % (t1 - t0 - FADE, FADE)
        a.append('[0:a]%s[a%d]' % (af, i))
    n = len(tr)
    pares = ''.join('[v%d][a%d]' % (i, i) for i in range(n))
    g = S.VIDEOS[clave]['ganancia']
    return ';'.join(v + a) + ';%sconcat=n=%d:v=1:a=1[vc][ac];[vc]format=yuv420p[v];' \
        '[ac]aresample=48000,volume=%.2fdB,alimiter=limit=0.84:attack=5:release=60:level=false[a]' % (pares, n, g)


def componer(clave):
    src = original(clave)
    dst = S.compuesto(clave)
    if os.path.exists(dst):
        raise SystemExit('ya existe ' + dst)
    fin = duracion(src)
    subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', src, '-filter_complex', filtro(clave, fin),
                    '-map', '[v]', '-map', '[a]', '-r', '30',
                    '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-pix_fmt', 'yuv420p',
                    '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
                    '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', dst + '.parcial.mp4'], check=True)
    os.replace(dst + '.parcial.mp4', dst)
    print('%s COMPUESTO %.2f s' % (clave, duracion(dst)), flush=True)


def prueba(clave, t):
    """Un cuadro del compuesto en el segundo t de la FUENTE (con la ventana de su tramo)."""
    win = None
    for a, b, w in S.tramos(clave):
        if t >= a and (b is None or t < b):
            win = w
    x, y, w, h = ventana(clave, win)
    out = '%s/01 VIDEO/_prueba_%s_%d.png' % (S.carpeta(clave), clave, t)
    subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-ss', str(t), '-i', original(clave),
                    '-vf', escala(x, y, w, h), '-frames:v', '1', out], check=True)
    print(out)


if __name__ == '__main__':
    if sys.argv[1] == 'todos':
        for k in S.VIDEOS:
            if not os.path.exists(S.compuesto(k)):
                componer(k)
        print('TODOS LISTOS', flush=True)
    elif len(sys.argv) > 2:
        prueba(sys.argv[1], float(sys.argv[2]))
    else:
        componer(sys.argv[1])
