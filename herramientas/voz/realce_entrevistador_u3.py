# -*- coding: utf-8 -*-
"""Realce suave del Entrevistador de U3 sobre el master original (Johan).
EQ +2 dB a 280 Hz (Q 1) y ganancia por bloque para que cada bloque quede
~1,5 dB arriba de como estaba, con techo de -17,8 LUFS. El resto del master
queda bit a bit igual."""
import json, os, re, subprocess, sys
sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
import rutas_dh

FF = 'ffmpeg'
V = rutas_dh.voces('U3')
ORIG = os.path.join(V, '_descartes',
                    'DH_U3_NARRADOR__antes_de_retomar_c02_otra_vez_todo_212826.wav')
SAL = r'D:\DAE\_tmp\dh\DH_U3_NARRADOR_realce2.wav'
EQ = 'equalizer=f=280:t=q:w=1.0:g=2.0'
VENT = {'c02': (15.31, 24.041), 'c04': (30.242, 38.741),
        'c06': (43.688, 51.258), 'c08': (57.851, 61.52)}
SUBE, TECHO, PICO = 1.5, -17.8, -1.5


def medir(desde, hasta, filtro=None):
    af = (filtro + ',' if filtro else '') + 'ebur128=peak=true'
    r = subprocess.run([FF, '-hide_banner', '-nostats', '-ss', '%.3f' % desde,
                        '-to', '%.3f' % hasta, '-i', ORIG, '-af', af, '-f', 'null', '-'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    t = r.stderr[r.stderr.rfind('Summary:'):]
    i = float(re.search(r'I:\s+(-?[\d.]+) LUFS', t).group(1))
    p = float(re.search(r'Peak:\s+(-?[\d.]+) dBFS', t).group(1))
    return i, p


def main():
    sr = 48000
    plan = []
    for k, (a, b) in sorted(VENT.items()):
        a, b = a - 0.06, b + 0.06
        i0, p0 = medir(a, b)
        i1, p1 = medir(a, b, EQ)
        meta = min(i0 + SUBE, TECHO)
        g = round(meta - i1, 2)
        lim = p1 + g > PICO
        plan.append(dict(k=k, a=a, b=b, i0=i0, p0=p0, ieq=i1, g=g, meta=meta, lim=lim))
    # filtro: tramos sin tocar + bloques realzados, cortes por muestra
    cortes = []
    for x in plan:
        cortes.append((int(round(x['a'] * sr)), int(round(x['b'] * sr)), x))
    partes, ultimo, n = [], 0, 0
    fc = []
    for s0, s1, x in cortes:
        if s0 > ultimo:
            fc.append('[0:a]atrim=start_sample=%d:end_sample=%d,asetpts=PTS-STARTPTS[p%d]' % (ultimo, s0, n))
            partes.append('[p%d]' % n); n += 1
        cad = '%s,volume=%.2fdB' % (EQ, x['g'])
        if x['lim']:
            cad += ',alimiter=limit=0.8414:attack=5:release=50:level=disabled:latency=1'
        fc.append('[0:a]atrim=start_sample=%d:end_sample=%d,asetpts=PTS-STARTPTS,%s[p%d]' % (s0, s1, cad, n))
        partes.append('[p%d]' % n); n += 1
        ultimo = s1
    fc.append('[0:a]atrim=start_sample=%d,asetpts=PTS-STARTPTS[p%d]' % (ultimo, n))
    partes.append('[p%d]' % n); n += 1
    fc.append('%sconcat=n=%d:v=0:a=1[s]' % (''.join(partes), n))
    r = subprocess.run([FF, '-hide_banner', '-y', '-i', ORIG, '-filter_complex', ';'.join(fc),
                        '-map', '[s]', '-c:a', 'pcm_s24le', '-ar', str(sr), SAL],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode:
        print(r.stderr[-1500:]); sys.exit(1)
    print(json.dumps(plan, indent=0))


if __name__ == '__main__':
    main()
