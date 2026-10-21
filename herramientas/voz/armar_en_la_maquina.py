# -*- coding: utf-8 -*-
"""Arma el master de narracion con ffmpeg solo, en la maquina de Sebastian.

POR QUE NO SE ARMA EN LA NUBE Y SE BAJA
    El master son 96 MB de PCM de 24 bits y el puente escribe 30 MB por
    archivo. Lo que viaja son los dieciocho bloques YA NIVELADOS -7,4 MB en
    total- y el plan de pausas; el pegado se hace aqui.

POR QUE NO SE USA EL CONCAT DE MP3 DIRECTO
    El demuxer concat pega los BITSTREAMS, y cada mp3 trae su relleno de
    codificador al principio y al final. Pegados en crudo, las duraciones no
    son las que se midieron y la rejilla deja de cuadrar. Aqui cada bloque se
    DECODIFICA a PCM primero -que es lo mismo que hace `carga()` en la nube- y
    se pega ya en PCM.

EL FORMATO DEL MASTER
    48 kHz, 24 bits, estereo dual-mono. Un clip mono en una linea estereo
    suena solo por la izquierda, y esa fue una de las primeras trampas de la
    serie.
"""
import json
import os
import subprocess
import sys

SR = 48000


def ff(*a):
    q = subprocess.run(['ffmpeg', '-v', 'error', '-y'] + list(a),
                       capture_output=True, text=True)
    if q.returncode:
        raise SystemExit('ffmpeg: ' + (q.stderr or '')[-600:])


def dur(ruta):
    q = subprocess.run(['ffprobe', '-v', 'error', '-show_entries',
                        'format=duration', '-of', 'csv=p=0', ruta],
                       capture_output=True, text=True)
    return float(q.stdout.strip())


def main(carpeta, plan_json, salida):
    tmp = os.path.join(os.path.dirname(salida) or '.', '_pcm')
    os.makedirs(tmp, exist_ok=True)
    plan = json.load(open(plan_json, encoding='utf-8'))
    trozos, n = [], 0
    for p in plan:
        n += 1
        d = os.path.join(tmp, '%03d.wav' % n)
        if p['tipo'] == 'voz':
            ff('-i', os.path.join(carpeta, p['archivo']),
               '-ac', '1', '-ar', str(SR), '-c:a', 'pcm_s24le', d)
        else:
            ff('-f', 'lavfi', '-i',
               'anullsrc=r=%d:cl=mono' % SR, '-t', '%.3f' % p['dur'],
               '-c:a', 'pcm_s24le', d)
        trozos.append(d)

    lista = os.path.join(tmp, 'lista.txt')
    with open(lista, 'w', encoding='utf-8') as f:
        for t in trozos:
            f.write("file '%s'\n" % t.replace('\\', '/'))
    ff('-f', 'concat', '-safe', '0', '-i', lista,
       '-af', 'pan=stereo|c0=c0|c1=c0',
       '-c:a', 'pcm_s24le', '-ar', str(SR), salida)

    for t in trozos:
        os.remove(t)
    os.remove(lista)
    os.rmdir(tmp)
    return dur(salida)


if __name__ == '__main__':
    d = main(sys.argv[1], sys.argv[2], sys.argv[3])
    print('master %.3f s  (%d:%06.3f)  %.1f MB'
          % (d, int(d) // 60, d % 60, os.path.getsize(sys.argv[3]) / 1e6))
