# -*- coding: utf-8 -*-
"""Bienes unidades (17 nov 2026): linea de Resolve y master de cada plan de cola.txt, uno tras otro (Resolve rinde de
a uno), y la entrega x264 con su hoja de revision en paralelo (dos a la vez) apenas esta el master. Despues, copia
exclusiva a la carpeta de paso de Drive. Espera el compuesto de cada plan. La cola se puede alargar; termina con la
linea FIN. Log: lote_entrega.log"""
import importlib, os, shutil, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor
PY = sys.executable
M = 'D:/DAE/_repo/herramientas/montaje/'
sys.path.insert(0, 'D:/DAE/_repo/cursos/bienes-proceso-penal/unidades')
sys.path.insert(0, 'D:/DAE/_repo/herramientas/entrega')
from subir_exclusivo import copiar_exclusivo
T = 'D:/DAE/_tmp/bi_u/'
log = open(T + 'lote_entrega.log', 'a', encoding='utf-8')
lock = threading.Lock()


def w(*a):
    with lock:
        print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)


def cola():
    try:
        return [l.strip() for l in open(T + 'cola.txt', encoding='utf-8') if l.strip()]
    except OSError:
        return []


def entrega(p):
    try:
        P = importlib.import_module(p)
        v = getattr(P, 'VERSION', 1)
        env = dict(os.environ, DAE_PLAN=p, PYTHONUTF8='1')
        t = time.time()
        r = subprocess.run([PY, M + 'mp4_entrega.py', P.NOMBRE_LINEA, P.R, P.EXPORT % v, P.MASTER_DIR], capture_output=True, text=True, env=env, errors='replace')
        open(P.TMP + '/entrega_mp4.log', 'w', encoding='utf-8').write(r.stdout + ('\nERR ' + r.stderr[-2500:] if r.returncode else ''))
        ok = r.returncode == 0 and 'LISTO' in r.stdout and 'FALLA' not in r.stdout
        w('entrega', p, 'rc', r.returncode, ok, '%.0f s' % (time.time() - t), '|', ' ; '.join(l for l in r.stdout.splitlines() if l.startswith(('entrega', 'sonido', 'psnr', 'audio'))))
        if not ok:
            w('ENTREGA FALLO', p, r.stderr[-600:]); return
        src = '%s/05 EXPORTS/%s.mp4' % (P.R, P.EXPORT % v)
        n, md5 = copiar_exclusivo(src, 'G:/My Drive/_MA subidas/' + os.path.basename(src))
        w('copiado|%s|%s|%d|%s' % (p, os.path.basename(src), n, md5))
        r2 = subprocess.run([PY, M + 'ic_revision.py', str(v)], capture_output=True, text=True, env=env, errors='replace')
        open(P.TMP + '/revision.log', 'w', encoding='utf-8').write(r2.stdout + r2.stderr[-1500:])
        w('revision', p, 'rc', r2.returncode)
    except Exception as e:
        w('ENTREGA EXCEPCION', p, repr(e)[:400])


def uno(p):
    P = importlib.import_module(p)
    v = getattr(P, 'VERSION', 1)
    cl = P.TMP + '/cadena.log'
    t0 = time.time()
    s = ''
    while time.time() - t0 < 6 * 3600:
        s = open(cl, encoding='utf-8', errors='replace').read() if os.path.exists(cl) else ''
        if 'LOTE LISTO' in s or 'LOTE FALLO' in s:
            break
        time.sleep(5)
    if 'LOTE LISTO' not in s:
        w('SIN CADENA', p); return
    env = dict(os.environ, DAE_PLAN=p, PYTHONUTF8='1')
    # el lower third se rinde de nuevo con las medidas vigentes del plan; el anterior va a _descartes
    lt = '%s/02 CARTONES/%s_lt01.mov' % (P.R, P.PREFIJO)
    if os.path.exists(lt):
        d = '%s/02 CARTONES/_descartes' % P.R
        os.makedirs(d, exist_ok=True)
        shutil.move(lt, '%s/%s_lt01_%d.mov' % (d, P.PREFIJO, int(time.time())))
    r = subprocess.run([PY, M + 'ic_pieza.py', 'cartones', 'lt01'], capture_output=True, text=True, env=env, errors='replace')
    w('lt', p, 'rc', r.returncode, os.path.exists(lt), ' '.join(r.stdout.split())[-90:], r.stderr[-300:] if r.returncode else '')
    if not os.path.exists(lt):
        w('LT FALLO', p); return
    t = time.time()
    r = subprocess.run([PY, M + 'ic_linea_externa.py'], capture_output=True, text=True, env=env, errors='replace')
    open(P.TMP + '/linea.log', 'w', encoding='utf-8').write(r.stdout + ('\nERR ' + r.stderr[-2500:] if r.returncode else ''))
    bien = 'LINEA LISTA' in r.stdout and 'problemas ninguno' in r.stdout
    w('linea', p, bien, '%.0f s' % (time.time() - t), '|', ' ; '.join(l for l in r.stdout.splitlines() if 'fin de la' in l or 'drt' in l)[:300])
    if not bien:
        w('LINEA FALLO', p, (r.stdout[-400:] + r.stderr[-400:])); return
    t = time.time()
    code = ('import sys; sys.path.insert(0, %r); import mp4_entrega as E; print(E.master(%r, %r, %r, %r))' % (M, P.NOMBRE_LINEA, P.R, P.EXPORT % v, P.MASTER_DIR))
    r = subprocess.run([PY, '-c', code], capture_output=True, text=True, env=env, errors='replace')
    open(P.TMP + '/master.log', 'w', encoding='utf-8').write(r.stdout + ('\nERR ' + r.stderr[-2500:] if r.returncode else ''))
    w('master', p, 'rc', r.returncode, '%.0f s' % (time.time() - t), '|', ' ; '.join(r.stdout.splitlines())[-260:])
    if r.returncode:
        w('MASTER FALLO', p, r.stderr[-500:]); return
    ex.submit(entrega, p)


ex = ThreadPoolExecutor(max_workers=2)
vistos = []
while True:
    c = cola()
    nuevos = [p for p in c if p != 'FIN' and p not in vistos]
    if not nuevos:
        if 'FIN' in c:
            break
        time.sleep(10); continue
    vistos.append(nuevos[0])
    try:
        uno(nuevos[0])
    except Exception as e:
        w('LINEA EXCEPCION', nuevos[0], repr(e)[:400])
ex.shutdown(wait=True)
w('LOTE LISTO')
open(T + 'prioridad.fin', 'w').write('fin')
