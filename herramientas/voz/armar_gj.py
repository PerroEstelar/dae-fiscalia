# -*- coding: utf-8 -*-
r"""Arma el master de narracion de cada caso de Gerencia judicial y deriva
sus ranuras.

Es `armar_sit` con UN cambio, que el T4 obliga: alli hablan dos voces -Pilar
narra, Carlos dice las dos citas- y el CLAUDE.md lo dejo medido en el
Curso 5: igualar bloques por LUFS integrado deja a Carlos entre 6 y 10 LU
por debajo de Pilar, porque el integrado castiga al bloque que calla mas.
Lo que el oido sigue es el nivel DURANTE el habla. Asi que cada bloque se
nivela por la MEDIANA DEL SHORT-TERM (ventana 3 s, paso 0,1 s) contando
solo las ventanas con voz -las que estan a menos de 20 LU del pico del
bloque- y despues se mide el salto entre bloques consecutivos, que es la
comprobacion que importa (por debajo de 1 LU no se percibe).

Lo demas no cambia: concatenar con las pausas que declara el guion, ganancia
al objetivo de la serie con un limitador que solo toca las puntas -19 LUFS,
techo -2 dBFS-, y en la misma corrida la rejilla con `derivar_rejilla_p3c5`
(fronteras de bloque obligatorias, el resto por la pausa mas corta primero,
tope 300 cuadros, piso 96).

Salen tres archivos por caso, en su `03 VOCES`:
    GJ_<T>_NARRADOR.wav     el master (estereo dual-mono, 48 kHz, 24 bit)
    GJ_<T>_rejilla.json     donde entra y sale cada bloque
    GJ_<T>_ranuras.json     los planos, con el `pieza` total ya calculado
"""
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\rejilla')
from guion_gj import VIDEOS, bloques            # noqa: E402
import rutas_gj as R                            # noqa: E402
import derivar_rejilla_p3c5 as DR               # noqa: E402

SR = 48000
COLA = 0.6
OBJETIVO = -19.0
LIMITE = -2.0

FF = os.environ.get('FFMPEG', 'ffmpeg')
FP = os.environ.get('FFPROBE', FF.replace('ffmpeg', 'ffprobe'))


def medir(ruta):
    s = subprocess.run([FF, '-nostats', '-i', ruta, '-af', 'ebur128=peak=true',
                        '-f', 'null', '-'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace').stderr
    i = re.findall(r'I:\s+(-?\d+\.\d+) LUFS', s)
    p = re.findall(r'Peak:\s+(-?\d+\.\d+) dBFS', s)
    return (float(i[-1]) if i else None), (float(p[-1]) if p else None)


def habla(ruta):
    """Mediana del short-term con voz: ventanas a menos de 20 LU del pico."""
    s = subprocess.run([FF, '-nostats', '-i', ruta, '-af',
                        'ebur128=framelog=info', '-f', 'null', '-'],
                       capture_output=True, text=True, encoding='utf-8',
                       errors='replace').stderr
    st = [float(x) for x in re.findall(r'\bS:\s*(-?\d+\.\d+)', s)]
    st = [x for x in st if x > -70]
    if not st:
        return None
    tope = max(st)
    vivos = sorted(x for x in st if x >= tope - 20)
    n = len(vivos)
    return vivos[n // 2] if n % 2 else (vivos[n // 2 - 1] + vivos[n // 2]) / 2.0


def duracion(ruta):
    s = subprocess.run([FP, '-v', 'error', '-show_entries', 'format=duration',
                        '-of', 'csv=p=0', ruta], capture_output=True,
                       text=True).stdout
    return float(s.strip())


def main(clave):
    voces = R.voces(clave)
    crudo = os.path.join(voces, 'crudo')
    salida = os.path.join(voces, 'GJ_%s_NARRADOR.wav' % clave)
    jsal = os.path.join(voces, 'GJ_%s_rejilla.json' % clave)
    rsal = os.path.join(voces, 'GJ_%s_ranuras.json' % clave)

    bl = bloques(clave)
    orden = [b[0] for b in bl]
    pausa = {b[0]: b[4] for b in bl}
    voz = {b[0]: b[1] for b in bl}

    fs = sorted(f for f in os.listdir(crudo) if f.endswith('.mp3'))

    def nom(f):                      # GJ_T4_06_c06_cita -> c06_cita
        return f[:-4].split('_', 3)[3]
    hay = {nom(f): f for f in fs}
    faltan = [b for b in orden if b not in hay]
    assert not faltan, 'faltan mp3: %s' % faltan
    fs = [hay[b] for b in orden]
    rutas = [os.path.join(crudo, f) for f in fs]

    niveles = [habla(r) for r in rutas]
    duraciones = [duracion(r) for r in rutas]
    vivos = sorted(n for n in niveles if n is not None)
    med = (vivos[len(vivos) // 2] if len(vivos) % 2
           else (vivos[len(vivos) // 2 - 1] + vivos[len(vivos) // 2]) / 2.0)

    cmd = [FF, '-v', 'error', '-y']
    for r in rutas:
        cmd += ['-i', r]
    partes, etiquetas = [], []
    for i, (f, n) in enumerate(zip(fs, niveles)):
        g = (med - n) if n is not None else 0.0
        partes.append('[%d:a]aresample=%d,aformat=sample_fmts=fltp:'
                      'channel_layouts=mono,volume=%.4fdB[a%d]' % (i, SR, g, i))
        etiquetas.append('[a%d]' % i)
        if i < len(fs) - 1:
            p = pausa[orden[i + 1]]
            partes.append('aevalsrc=0:s=%d:d=%.4f,aformat=sample_fmts=fltp:'
                          'channel_layouts=mono[p%d]' % (SR, p, i))
            etiquetas.append('[p%d]' % i)
    partes.append('aevalsrc=0:s=%d:d=%.4f,aformat=sample_fmts=fltp:'
                  'channel_layouts=mono[cola]' % (SR, COLA))
    etiquetas.append('[cola]')
    partes.append('%sconcat=n=%d:v=0:a=1[out]'
                  % (''.join(etiquetas), len(etiquetas)))
    tmp = salida + '.tmp.wav'
    cmd += ['-filter_complex', ';'.join(partes), '-map', '[out]',
            '-c:a', 'pcm_s24le', '-ar', str(SR), '-ac', '1', tmp]
    q = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8',
                       errors='replace')
    if q.returncode:
        raise SystemExit('ffmpeg: ' + (q.stderr or '')[-1200:])

    antes, _ = medir(tmp)
    g = OBJETIVO - antes
    if os.path.exists(salida):
        d = os.path.join(voces, '_descartes')
        os.makedirs(d, exist_ok=True)
        import time
        os.replace(salida, os.path.join(d, 'GJ_%s_NARRADOR__rearmado_%s.wav'
                                        % (clave, time.strftime('%H%M%S'))))
    for _intento in (1, 2, 3):
        q = subprocess.run([FF, '-v', 'error', '-y', '-i', tmp,
                            '-af', 'volume=%.4fdB,alimiter=limit=%.4f:attack=5:'
                                   'release=50:level=disabled,'
                                   'aformat=channel_layouts=stereo'
                                   % (g, 10 ** (LIMITE / 20.0)),
                            '-c:a', 'pcm_s24le', '-ar', str(SR), salida],
                           capture_output=True, text=True, encoding='utf-8',
                           errors='replace')
        if q.returncode:
            raise SystemExit('ffmpeg: ' + (q.stderr or '')[-800:])
        hecho, pico = medir(salida)
        if abs(hecho - OBJETIVO) <= 0.2:
            break
        g += (OBJETIVO - hecho)
    os.remove(tmp)

    tramos, t = [], 0.0
    for i, (b, d) in enumerate(zip(orden, duraciones)):
        tramos.append({'bloque': b, 'voz': voz[b], 'entra': round(t, 3),
                       'sale': round(t + d, 3), 'dur': round(d, 3),
                       'habla_crudo': niveles[i]})
        t += d
        if i < len(orden) - 1:
            t += pausa[orden[i + 1]]
    t += COLA

    # el salto entre bloques consecutivos, medido sobre el master
    for tr in tramos:
        a, b = tr['entra'], tr['sale']
        s = subprocess.run([FF, '-nostats', '-ss', '%.3f' % a, '-t', '%.3f' % (b - a),
                            '-i', salida, '-af', 'ebur128=framelog=info',
                            '-f', 'null', '-'], capture_output=True, text=True,
                           encoding='utf-8', errors='replace').stderr
        st = [float(x) for x in re.findall(r'\bS:\s*(-?\d+\.\d+)', s)]
        st = [x for x in st if x > -70]
        if st:
            tope = max(st)
            v = sorted(x for x in st if x >= tope - 20)
            tr['habla_master'] = round(v[len(v) // 2], 2)
    saltos = [abs(tramos[i + 1].get('habla_master', 0) - tramos[i].get('habla_master', 0))
              for i in range(len(tramos) - 1)]

    info = {'tema': clave, 'dur': round(t, 3), 'tramos': tramos,
            'lufs_crudo': antes, 'ganancia_db': round(g, 2),
            'lufs_final': hecho, 'pico_dbfs': pico,
            'peor_salto_lu': round(max(saltos), 2) if saltos else 0.0}
    json.dump(info, open(jsal, 'w', encoding='utf-8'), ensure_ascii=False,
              indent=1)

    ranuras, total, pieza, ncand, nobl = DR.main(salida, jsal, rsal)
    info['ranuras'] = ranuras
    info['pieza'] = pieza
    return info


if __name__ == '__main__':
    claves = [x.upper() for x in sys.argv[1:]] or VIDEOS
    for c in claves:
        info = main(c)
        d = info['dur']
        print('%s  master %.2f s (%d:%04.1f)  %.1f LUFS  pico %.1f dBFS  '
              'peor salto %.2f LU · %d ranuras · pieza %d cuadros'
              % (c, d, int(d) // 60, d % 60, info['lufs_final'],
                 info['pico_dbfs'], info['peor_salto_lu'],
                 len(info['ranuras']), info['pieza']), flush=True)
        for t in info['tramos']:
            print('      %-26s %-6s %7.2f %7.2f %7.2f  habla %s'
                  % (t['bloque'], t['voz'], t['entra'], t['sale'], t['dur'],
                     t.get('habla_master')), flush=True)
        for i, (a, dd, b) in enumerate(info['ranuras'], 1):
            print('      r%02d %5d %4d  %s' % (i, a, dd, b), flush=True)
    print('LISTO', flush=True)
