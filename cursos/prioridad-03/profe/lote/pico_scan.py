# -*- coding: utf-8 -*-
"""Busca muestras fuera de escala (|x| > 1.0) en el audio de las entregas: un cuadro AAC roto de Resolve
se oye como un chasquido. Log: pico_scan.log"""
import glob, os, subprocess, sys, time
import numpy as np
FF = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
log = open('D:/DAE/_tmp/tr_p/pico_scan.log', 'a', encoding='utf-8')
def w(*a):
    print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)
def scan(f):
    p = subprocess.Popen([FF + '/ffmpeg.exe', '-v', 'error', '-i', f, '-vn', '-ac', '2', '-ar', '48000', '-f', 'f32le', '-'], stdout=subprocess.PIPE)
    n = 0; mx = 0.0; reg = []
    while True:
        b = p.stdout.read(48000 * 8 * 10)
        if not b:
            break
        a = np.frombuffer(b[:len(b) // 8 * 8], dtype=np.float32).reshape(-1, 2)
        m = np.abs(a).max(axis=1)
        mx = max(mx, float(m.max()) if len(m) else 0.0)
        idx = np.where(m > 1.0)[0]
        for i in idx:
            t = (n + int(i)) / 48000.0
            if reg and t - reg[-1][1] < 0.2:
                reg[-1][1] = t; reg[-1][2] = max(reg[-1][2], float(m[i]))
            else:
                reg.append([t, t, float(m[i])])
        n += len(a)
    p.wait()
    return n / 48000.0, mx, reg
fs = sys.argv[1:]
for f in fs:
    try:
        d, mx, reg = scan(f)
        w('%s|dur %.1f|max %.3f|%s' % (os.path.basename(f), d, mx, 'LIMPIO' if not reg else 'ROTO ' + ' ; '.join('%.2f-%.2f s x%.1f' % (a, b, c) for a, b, c in reg[:20])))
    except Exception as e:
        w('EXCEPCION', os.path.basename(f), repr(e)[:200])
w('FIN')
