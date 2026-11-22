# -*- coding: utf-8 -*-
r"""Ley 1826 · los 19 audios de los casos para el aula (21 nov 2026). Textos en `textos/casos_audio_lp.py`.

    python lanzar_casos_audio_lp.py                 pide los que faltan y masteriza todos
    python lanzar_casos_audio_lp.py U1-C1-A         solo ese (toma nueva: la anterior va a _descartes)
    python lanzar_casos_audio_lp.py --master        solo vuelve a masterizar lo que hay

Carpeta: E:\DAE MASTER\PRIORIDAD 1\CURSO - LEY 1826 PROCEDIMIENTO PENAL ABREVIADO\AUDIOS CASOS\
    <código>.mp3     la entrega: MP3 a 192 kb/s, 48 kHz, estéreo dual-mono, −16 LUFS, techo −1,5 dBTP
                     (el nivel de los videos de profe del aula: el participante no tiene que tocar el volumen
                     entre un video y un audio)
    crudo\           lo que devuelve ElevenLabs (mp3 44,1 kHz 192 kb/s)
    textos_tts\      el texto que se mandó, uno por tramo
    _descartes\      tomas reemplazadas

Velocidad: `DAE_SPEED` (ElevenLabs acepta 0,7 a 1,2); sin la variable la voz va a su ritmo. El pedido pide unas
140 palabras por minuto, contadas sobre el texto del documento.
"""
import glob
import json
import os
import shutil
import subprocess
import sys
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, 'textos'))
sys.path.insert(0, AQUI)
import casos_audio_lp as C          # noqa: E402
import elevenlabs as E              # noqa: E402

RAIZ = r'E:\DAE MASTER\PRIORIDAD 1\CURSO - LEY 1826 PROCEDIMIENTO PENAL ABREVIADO\AUDIOS CASOS'
FB = glob.glob(os.path.expanduser('~') + r'\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg*\*\bin')[0]
FF, FP = FB + r'\ffmpeg.exe', FB + r'\ffprobe.exe'
I, TP, LRA = -16.0, -1.5, 11.0
CADENA = 'aresample=48000:resampler=soxr:precision=28,pan=stereo|c0=c0|c1=c0'


def dur(p):
    r = subprocess.run([FP, '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def pedir(cod, voz, tts, nueva=False):
    crudo = os.path.join(RAIZ, 'crudo', cod + '.mp3')
    if os.path.exists(crudo):
        if not nueva:
            return crudo
        d = os.path.join(RAIZ, '_descartes')
        os.makedirs(d, exist_ok=True)
        shutil.move(crudo, os.path.join(d, '%s__crudo_%s.mp3' % (cod, time.strftime('%H%M%S'))))
    tx = os.path.join(RAIZ, 'textos_tts', cod + '.txt')
    with open(tx, 'w', encoding='utf-8', newline='\n') as f:
        f.write(tts)
    E.decir(tts, C.VOZ[voz], crudo)
    return crudo


def master(cod, crudo):
    sal = os.path.join(RAIZ, cod + '.mp3')
    err = subprocess.run([FF, '-nostats', '-i', crudo, '-af', '%s,loudnorm=I=%.1f:TP=%.1f:LRA=%.1f:print_format=json'
                          % (CADENA, I, TP, LRA), '-f', 'null', '-'], capture_output=True, text=True).stderr
    m = json.loads(err[err.rindex('{'):err.rindex('}') + 1])
    af = ('%s,loudnorm=I=%.1f:TP=%.1f:LRA=%.1f:measured_I=%s:measured_TP=%s:measured_LRA=%s:measured_thresh=%s:'
          'offset=%s:linear=true,aresample=48000' % (CADENA, I, TP, LRA, m['input_i'], m['input_tp'], m['input_lra'],
                                                    m['input_thresh'], m['target_offset']))
    tmp = sal + '.parcial.mp3'
    r = subprocess.run([FF, '-y', '-v', 'error', '-i', crudo, '-af', af, '-ar', '48000', '-ac', '2',
                        '-c:a', 'libmp3lame', '-b:a', '192k', '-id3v2_version', '3',
                        '-metadata', 'title=' + cod, tmp], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[-500:]
    if os.path.exists(sal):
        d = os.path.join(RAIZ, '_descartes')
        os.makedirs(d, exist_ok=True)
        shutil.move(sal, os.path.join(d, '%s__%s.mp3' % (cod, time.strftime('%H%M%S'))))
    os.replace(tmp, sal)
    err = subprocess.run([FF, '-nostats', '-i', sal, '-af', 'ebur128=peak=true', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    ls = err.splitlines()
    k = max(i for i, l in enumerate(ls) if 'Integrated loudness' in l)
    lufs = [l.split()[1] for l in ls[k:k + 4] if l.strip().startswith('I:')][0]
    pico = [l.split()[1] for l in ls[k:] if l.strip().startswith('Peak:')][0]
    return sal, float(lufs), float(pico)


if __name__ == '__main__':
    args = sys.argv[1:]
    solo_master = '--master' in args
    elegidos = [a.upper() for a in args if not a.startswith('--')]
    for s in ('crudo', 'textos_tts'):
        os.makedirs(os.path.join(RAIZ, s), exist_ok=True)
    print('velocidad', os.environ.get('DAE_SPEED', 'natural'), flush=True)
    for cod, voz, texto, tts in C.TRAMOS:
        if elegidos and cod not in elegidos:
            continue
        crudo = os.path.join(RAIZ, 'crudo', cod + '.mp3')
        if not solo_master:
            crudo = pedir(cod, voz, tts, nueva=bool(elegidos))
        if not os.path.exists(crudo):
            print(cod, 'FALTA EL CRUDO', flush=True)
            continue
        sal, lufs, pico = master(cod, crudo)
        d = dur(sal)
        n = C.palabras(texto)
        print('%-8s %-6s %5.1f s  %3d palabras  %5.1f p/min  %5.1f LUFS  pico %5.1f' % (cod, voz, d, n, n / d * 60,
                                                                                       lufs, pico), flush=True)
    print('LISTO', flush=True)
