# -*- coding: utf-8 -*-
"""Gerencia judicial, videos de profe (27 nov 2026), recorte en paralelo (segunda version del lote).
Cada recorte de recorta_cuadro.py usa un solo nucleo de la CPU (Python + numpy) y la placa queda al 20 %: con dos a
la vez iba a 2,4 c/s cada uno y la bienvenida (44.876 cuadros) tardaba mas de 5 h. Aqui van cuatro a la vez, y la
bienvenida se parte en cuatro tramos de cuadros (--desde/--cuadros) que despues se pegan sin recodificar (concat)
con el sonido de la grabacion original. Lo que ya existe no se rehace. Log: recorta_lote.log"""
import os, subprocess, sys, threading, time, queue
from glob import glob
PY = sys.executable
FB = glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
REC = 'D:/DAE/_repo/herramientas/video/recorta_cuadro.py'
T = 'D:/DAE/_tmp/gj_p/'
R = 'E:/DAE MASTER/PRIORIDAD 2/CURSO - GERENCIA JUDICIAL/VIDEOS PROFE/'
FONDO = R + '00 FONDOS/FONDO 4 V2.png'
V1 = R + 'CURSO/INICIO/01 VIDEO/VIDEO 1 GERENCIA JUDICIAL TOMA1.mp4'
PARTES = R + 'CURSO/INICIO/01 VIDEO/_partes/'
CI = R + 'CURSO/INICIO/01 VIDEO/gj_curso_inicio_recortado.mp4'
N1 = 44876
CORTES = [0, 11220, 22440, 33660, N1]
log = open(T + 'recorta_lote.log', 'a', encoding='utf-8')
lock = threading.Lock()
env = {k: v for k, v in os.environ.items() if not k.startswith('PYTHON')}


def w(*a):
    with lock:
        print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)


def cuadros(p):
    r = subprocess.run([FB + '/ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries',
                        'stream=nb_read_packets', '-of', 'csv=p=0', p], capture_output=True, text=True)
    return int(r.stdout.strip().split(',')[0] or 0)


def recorta(clave, fu, sa, extra, esperados):
    if os.path.exists(sa):
        w('ya estaba', clave); return True
    t = time.time(); w('empieza', clave)
    os.makedirs(T + clave, exist_ok=True)
    with open(T + clave + '/recorta.out', 'w', encoding='utf-8') as out:
        rc = subprocess.run([PY, '-X', 'utf8', REC, fu, FONDO, sa, '--escala', '0.85', '--cx', '1220'] + extra, stdout=out,
                            stderr=subprocess.STDOUT, env=env).returncode
    s = open(T + clave + '/recorta.out', encoding='utf-8', errors='replace').read()
    ok = rc == 0 and 'LISTO' in s and os.path.exists(sa)
    a = esperados if esperados else cuadros(fu)
    b = cuadros(sa) if ok else 0
    w('RECORTE', clave, 'OK' if ok and a == b else 'FALLA', 'cuadros', a, b, '%.0f min' % ((time.time() - t) / 60), ' '.join(s.split())[-120:])
    return ok and a == b


def parte(i):
    k0, k1 = CORTES[i], CORTES[i + 1]
    extra = ['--cuadros', str(k1 - k0)] + (['--desde', '%.4f' % (k0 / 30 - 0.005)] if k0 else [])
    return recorta('gjci_p%d' % (i + 1), V1, PARTES + 'gj_ci_parte%d.mp4' % (i + 1), extra, k1 - k0)


def pegar():
    if os.path.exists(CI):
        return
    for suf in ('', '_mate'):
        lst = PARTES + 'lista%s.txt' % suf
        filas = ['file ' + chr(39) + PARTES + 'gj_ci_parte%d%s.mp4' % (i + 1, suf) + chr(39) for i in range(4)]
        open(lst, 'w', encoding='utf-8').write(chr(10).join(filas) + chr(10))
        dst = CI.replace('.mp4', suf + '.mp4')
        cmd = [FB + '/ffmpeg.exe', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst]
        cmd += (['-i', V1, '-map', '0:v', '-map', '1:a'] if not suf else ['-map', '0:v'])
        cmd += ['-c', 'copy', '-movflags', '+faststart', dst + '.parcial.mp4']
        r = subprocess.run(cmd, capture_output=True, text=True, errors='replace')
        if r.returncode:
            w('PEGAR FALLA', suf, r.stderr[-300:]); return
        os.replace(dst + '.parcial.mp4', dst)
    n = cuadros(CI)
    w('PEGADO gjci', 'OK' if n == N1 else 'FALLA', 'cuadros', n, N1)


U = [(k, R + c + '/01 VIDEO/gj_%s_fuente.mp4' % k, R + c + '/01 VIDEO/gj_%s_recortado.mp4' % k) for k, c in
     [('u2i', 'UNIDAD 2/INICIO'), ('u2c', 'UNIDAD 2/CIERRE'), ('u3i', 'UNIDAD 3/INICIO'), ('u3c', 'UNIDAD 3/CIERRE'),
      ('u4i', 'UNIDAD 4/INICIO'), ('u4c', 'UNIDAD 4/CIERRE'), ('u1i', 'UNIDAD 1/INICIO')]]
q = queue.Queue()
q.put(('u', U[0]))
for i in range(4):
    q.put(('p', i))
for x in U[1:]:
    q.put(('u', x))
partes_ok = []


def obrero():
    while True:
        try:
            tipo, x = q.get_nowait()
        except queue.Empty:
            return
        if tipo == 'p':
            ok = parte(x)
            with lock:
                partes_ok.append((x, ok))
                listas = len(partes_ok) == 4 and all(o for _, o in partes_ok)
            if listas:
                pegar()
        else:
            recorta(x[0], x[1], x[2], [], 0)


os.makedirs(PARTES, exist_ok=True)
w('lote 2: arranca (cuatro a la vez)')
h = [threading.Thread(target=obrero) for _ in range(4)]
for x in h: x.start()
for x in h: x.join()
w('LOTE DE RECORTES 2 LISTO')
