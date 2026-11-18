# -*- coding: utf-8 -*-
"""Mientras corre el lote de Trata, videos de profe, deja los ffmpeg (compuestos y entregas x264) en prioridad por debajo de
lo normal, para que Resolve, que rinde los masters de a uno y es el cuello de botella, tenga procesador.
Termina cuando existe prioridad.fin (lo escribe lote_entrega al terminar)."""
import ctypes, os, subprocess, time
T = 'D:/DAE/_tmp/tr_p/'
k32 = ctypes.windll.kernel32
vistos = set()
t0 = time.time()
while time.time() - t0 < 14 * 3600 and not os.path.exists(T + 'prioridad.fin'):
    r = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq ffmpeg.exe', '/FO', 'CSV', '/NH'], capture_output=True, text=True, errors='replace').stdout
    for ln in r.splitlines():
        c = [x.strip('"') for x in ln.split(',')]
        if len(c) > 1 and c[1].isdigit() and int(c[1]) not in vistos:
            h = k32.OpenProcess(0x0200, False, int(c[1]))
            if h:
                k32.SetPriorityClass(h, 0x00004000)
                k32.CloseHandle(h)
            vistos.add(int(c[1]))
    time.sleep(15)
open(T + 'prioridad.listo', 'w').write(str(len(vistos)))
