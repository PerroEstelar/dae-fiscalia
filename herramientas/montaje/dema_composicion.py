# -*- coding: utf-8 -*-
r"""Composición base del conversatorio «Articulación DEMA y DECOC».

Entra la grabación de Teams (1280×720, 30 fps, los dos mosaicos de 640×360 en
y 180–540) y sale un 1920×1080 a 30 fps:
- Fondo plano azul institucional #002048, sin degradé.
- La franja de los dos mosaicos escalada a 1,5× (1920×540) en y=140.
- Ni las franjas negras ni los rótulos de Teams.
- Color convertido de BT.601 (así viene la fuente) a Rec.709 y etiquetado.

El audio sale con una ganancia por turno para dejar a los dos a −19 LUFS.
Medido sobre sus tramos de voz en Scribe: Ana −14,8 y Camilo −16,8, así que
llevan −4,2 y −2,2 dB. El cambio de ganancia cae a mitad del silencio entre
turnos.

    python dema_composicion.py          la composición entera
    python dema_composicion.py 300      un cuadro de prueba en el segundo 300
"""
import glob
import json
import os
import subprocess
import sys

FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
R = ('E:/DAE MASTER/CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE/UNIDAD 1/'
     'CONVERSATORIO - Articulacion DEMA y DECOC')
SRC = R + '/01 VIDEO/Video articulacion DEMA y DECOC.mp4'
STT = R + '/03 VOCES/stt/DEMA_DECOC_stt.json'
DST = R + '/01 VIDEO/DEMA_DECOC_composicion_v1.mp4'
Y = 140
GANANCIA = {'speaker_0': -4.2, 'speaker_1': -2.2}


def turnos():
    w = [x for x in json.load(open(STT, encoding='utf-8'))['words'] if x.get('type', 'word') == 'word']
    out = []
    for x in w:
        if out and out[-1][2] == x['speaker_id']:
            out[-1][1] = x['end']
        else:
            out.append([x['start'], x['end'], x['speaker_id']])
    return out


def expr_volumen():
    tt = turnos()
    lim = [(a[1] + b[0]) / 2.0 for a, b in zip(tt, tt[1:])]
    g = [10 ** (GANANCIA[t[2]] / 20.0) for t in tt]
    e = '%.5f' % g[-1]
    for b, gi in zip(reversed(lim), reversed(g[:-1])):
        e = 'if(lt(t,%.3f),%.5f,%s)' % (b, gi, e)
    return e


def filtro(audio=True):
    v = ('color=c=0x002048:s=1920x1080:r=30[bg];'
         '[0:v]crop=1280:360:0:180,scale=1920:540:flags=lanczos[tiles];'
         '[bg][tiles]overlay=0:%d:shortest=1,'
         'scale=out_color_matrix=bt709:out_range=tv,format=yuv420p[v]' % Y)
    if not audio:
        return v
    return v + ";[0:a]aresample=48000,volume=eval=frame:volume='%s'[a]" % expr_volumen()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        t = sys.argv[1]
        subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-ss', t, '-i', SRC, '-filter_complex', filtro(False),
                        '-map', '[v]', '-frames:v', '1', R + '/01 VIDEO/_prueba_%s.png' % t], check=True)
        print('prueba lista')
        sys.exit()
    subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', SRC, '-filter_complex', filtro(),
                    '-map', '[v]', '-map', '[a]', '-r', '30',
                    '-c:v', 'libx264', '-crf', '16', '-preset', 'medium', '-pix_fmt', 'yuv420p',
                    '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
                    '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', DST], check=True)
    print('COMPOSICION LISTA', flush=True)
