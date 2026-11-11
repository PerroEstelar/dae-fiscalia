# -*- coding: utf-8 -*-
r"""Audio v2 de los videos de profes del curso SRPA y justicia restaurativa.

Sebastián, 11 nov 2026: «siento que la voz de los profes está débil, comprime el
audio a niveles óptimos y de ser necesario ecualiza».

La v1 era el original con una ganancia fija a −19 LUFS integrados y un limitador.
Con la dinámica de un micrófono de computador (LRA 5–7 LU), las frases bajas
quedaban bastante por debajo. La v2 rehace el audio desde el original, con los
mismos tramos y cortes que la composición:

1. Paso alto a 80 Hz, para quitar el retumbe de mesa y de sala.
2. −2 dB en 250 Hz (Q 1), para quitar el tono de caja de la webcam.
3. +3 dB en 3 kHz (Q 0,9), por presencia e inteligibilidad.
4. Un compresor de voz: umbral −26 dB, 3:1, ataque 8 ms, relevo 180 ms.
5. `loudnorm` en dos pasadas a −16 LUFS integrados, techo −1,5 dBTP y LRA 7. Es
   el nivel de referencia para video en línea y deja a la voz 3 LU por encima de
   la v1.

El video del compuesto v1 se copia sin recodificar (`-c:v copy`) y sale
`SRPA_<video>_compuesto_v2.mp4`, que en la línea reemplaza al v1 con `ReplaceClip`.

    python srpa_audio.py u3b            uno
    python srpa_audio.py todos          los siete
"""
import glob
import json
import os
import subprocess
import sys

sys.path.insert(0, r'D:\DAE\_repo\cursos\srpa-justicia-restaurativa')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import srpa as S  # noqa: E402
import srpa_composicion as K  # noqa: E402

FB = K.FB
CADENA = ('highpass=f=80:poles=2,'
          'equalizer=f=250:t=q:w=1:g=-2,'
          'equalizer=f=3000:t=q:w=0.9:g=3,'
          'acompressor=threshold=-26dB:ratio=3:attack=8:release=180:makeup=1:knee=4')
META = 'I=-16:TP=-1.5:LRA=7'


def v2(clave):
    return S.compuesto(clave).replace('_compuesto_v1.mp4', '_compuesto_v2.mp4')


def grafo(clave, fin):
    tr = S.tramos(clave)
    a = []
    for i, (t0, t1, _w) in enumerate(tr):
        t1 = fin if t1 is None else t1
        af = 'atrim=start=%.3f:end=%.3f,asetpts=PTS-STARTPTS' % (t0, t1)
        if i > 0 and tr[i - 1][1] != t0:
            af += ',afade=t=in:d=%.3f' % K.FADE
        if i < len(tr) - 1 and tr[i + 1][0] != t1:
            af += ',afade=t=out:st=%.3f:d=%.3f' % (t1 - t0 - K.FADE, K.FADE)
        a.append('[0:a]%s[a%d]' % (af, i))
    n = len(tr)
    return ';'.join(a) + ';%sconcat=n=%d:v=0:a=1,aresample=48000,%s' % (
        ''.join('[a%d]' % i for i in range(n)), n, CADENA)


def medir(clave, fin):
    r = subprocess.run([FB + '/ffmpeg.exe', '-hide_banner', '-nostats', '-i', K.original(clave),
                        '-filter_complex', grafo(clave, fin) + ',loudnorm=%s:print_format=json[a]' % META,
                        '-map', '[a]', '-f', 'null', '-'], capture_output=True, text=True, errors='replace').stderr
    return json.loads(r[r.rfind('{'):r.rfind('}') + 1])


def procesar(clave):
    dst = v2(clave)
    if os.path.exists(dst):
        print(clave, 'ya existe', flush=True)
        return
    fin = K.duracion(K.original(clave))
    m = medir(clave, fin)
    ln = ('loudnorm=%s:measured_I=%s:measured_TP=%s:measured_LRA=%s:measured_thresh=%s:offset=%s:linear=true'
          % (META, m['input_i'], m['input_tp'], m['input_lra'], m['input_thresh'], m['target_offset']))
    subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', K.original(clave), '-i', S.compuesto(clave),
                    '-filter_complex', grafo(clave, fin) + ',' + ln + ',aresample=48000[a]',
                    '-map', '1:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k',
                    '-movflags', '+faststart', dst + '.parcial.mp4'], check=True)
    os.replace(dst + '.parcial.mp4', dst)
    print('%s AUDIO v2  medido I %s LRA %s TP %s' % (clave, m['input_i'], m['input_lra'], m['input_tp']), flush=True)


if __name__ == '__main__':
    claves = list(S.VIDEOS) if sys.argv[1] == 'todos' else sys.argv[1:]
    for k in claves:
        procesar(k)
    print('LISTO', flush=True)
