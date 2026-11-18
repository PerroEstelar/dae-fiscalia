# -*- coding: utf-8 -*-
"""Trata, videos de profe (18 nov 2026): recorta al avatar de cada plan de recortes.txt (recorta_persona.py, por la
placa) sobre el fondo de la DAE, dos a la vez (la placa queda al 27 % con uno solo: el limite es el procesador), y a
medida que termina cada uno lo agrega a cola.txt, de donde lo toman lote_cadena.py (compuestos) y entrega_gpu.py
(linea y entrega). recortes.txt se puede alargar mientras corre; con la linea FIN termina y agrega FIN a cola.txt.
    python recorta_lote.py [a_la_vez]      Log: recorta_lote.log"""
import importlib, os, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor
PY = sys.executable
REC = 'D:/DAE/_repo/herramientas/video/recorta_persona.py'
sys.path.insert(0, 'D:/DAE/_repo/cursos/prioridad-03/profe')
sys.path.insert(0, 'D:/DAE/_repo/herramientas/montaje')
os.environ.setdefault('DAE_PRESET', 'slow')
import mp4_entrega as E
T = 'D:/DAE/_tmp/tr_p/'
log = open(T + 'recorta_lote.log', 'a', encoding='utf-8')
lock = threading.Lock()


def w(*a):
    with lock:
        print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)


def recorta(P, extra):
    r = P.RECORTE
    out = open(P.TMP + '/recorta.out', 'w', encoding='utf-8')
    rc = subprocess.run([PY, REC, P.FUENTE_CRUDA, P.FONDO, P.ORIGINAL, '--y', str(r['y']), '--x', str(r.get('x', 0)),
                         '--lado', str(r.get('lado', 1080)), '--cx', str(P.CENTRO_X)] + extra, stdout=out, stderr=subprocess.STDOUT).returncode
    out.close()
    s = open(P.TMP + '/recorta.out', encoding='utf-8', errors='replace').read()
    return rc == 0 and 'LISTO' in s and os.path.exists(P.ORIGINAL), ' '.join(s.split())[-200:]


def uno(p):
    try:
        P = importlib.import_module(p)
        os.makedirs(P.TMP, exist_ok=True)
        if os.path.exists(P.ORIGINAL):
            w('recorte', p, 'ya estaba')
        else:
            t = time.time()
            ok, cola = recorta(P, [])
            if not ok:
                w('recorte', p, 'FALLO por la placa, reintento en 60 s |', cola)
                time.sleep(60)
                ok, cola = recorta(P, [])
            if not ok:
                w('recorte', p, 'FALLO otra vez: va por procesador con mobilenetv3 |', cola)
                ok, cola = recorta(P, ['--cpu', '--modelo', 'mobilenetv3'])
            if not ok:
                w('RECORTE FALLO', p, cola); return
            n0, n1 = E.cuadros(P.FUENTE_CRUDA), E.cuadros(P.ORIGINAL)
            w('recorte', p, 'OK' if abs(n0 - n1) <= 1 else 'CUADROS DISTINTOS', '%d / %d cuadros' % (n1, n0), '%.0f s' % (time.time() - t), '|', cola[-90:])
            if abs(n0 - n1) > 1:
                return
        with lock:
            open(T + 'cola.txt', 'a', encoding='utf-8').write(p + '\n')
    except Exception as e:
        w('RECORTE EXCEPCION', p, repr(e)[:400])


def pedidos():
    try:
        return [l.strip() for l in open(T + 'recortes.txt', encoding='utf-8') if l.strip()]
    except OSError:
        return []


ex = ThreadPoolExecutor(max_workers=int(sys.argv[1]) if len(sys.argv) > 1 else 2)
vistos = []
while True:
    c = pedidos()
    for p in c:
        if p != 'FIN' and p not in vistos:
            vistos.append(p); ex.submit(uno, p); w('pedido', p)
    if 'FIN' in c:
        break
    time.sleep(10)
ex.shutdown(wait=True)
open(T + 'cola.txt', 'a', encoding='utf-8').write('FIN\n')
w('RECORTES LISTOS')
