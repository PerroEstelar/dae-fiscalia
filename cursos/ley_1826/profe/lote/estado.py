# -*- coding: utf-8 -*-
"""Ley 1826, videos de profe: en que va el lote (recortes, cadenas, entregas, discos, placa). Para run_inline."""
import glob, os, shutil, subprocess, time
T = 'D:/DAE/_tmp/lp_p/'


def ls(f):
    try:
        return open(T + f, encoding='utf-8', errors='replace').read().splitlines()
    except OSError:
        return []


print(time.strftime('%H:%M:%S'), 'E %.1f D %.1f C %.1f G %.2f' % tuple(shutil.disk_usage(x).free / 1e9 for x in ('E:/', 'D:/', 'C:/', 'G:/')))
print('recortes:', ' | '.join(' '.join(l.split()[1:8]) for l in ls('recorta_lote.log')))
for k in ('lpci', 'lpu1i', 'lpu1c', 'lpu2i', 'lpu2c', 'lpu3i', 'lpu3c', 'lpu4i', 'lpu4c', 'lpcc'):
    s = ls(k + '/recorta.out')
    if s and 'LISTO' not in s[-1]:
        print('  en curso', k, s[-1][:60])
print('cadena:', ' | '.join(' '.join(l.split()[2:7]) for l in ls('lote_cadena.log') if 'en cola' not in l))
for l in ls('lote_entrega.log'):
    p = l.split()
    if len(p) > 1 and p[1] in ('linea', 'revision', 'calibra', 'entrega_gpu:'):
        print(' '.join(p[:7]))
    else:
        print(l[:300].encode('ascii', 'backslashreplace').decode())
print('pendientes:', ls('pendientes.txt'))
for o in ('lote_cadena.out', 'entrega_gpu.out', 'recorta_lote.out'):
    s = chr(10).join(ls(o))[-300:]
    if s.strip():
        print('!!', o, s.encode('ascii', 'backslashreplace').decode())
r = subprocess.run(['nvidia-smi', '--query-gpu=utilization.gpu,memory.used', '--format=csv,noheader'], capture_output=True, text=True)
print('gpu', r.stdout.strip())
print('subidas:', [(os.path.basename(x), os.path.getsize(x)) for x in glob.glob('G:/My Drive/_MA subidas/ley1826*')])
