# -*- coding: utf-8 -*-
"""Bienes unidades (17 nov 2026): cadena sin After Effects (componer, titulo, cartones) de los planes de cola.txt,
tres a la vez. La cola se puede alargar mientras corre; termina cuando encuentra la linea FIN. Log: lote_cadena.log"""
import importlib, os, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor
PY = sys.executable
M = 'D:/DAE/_repo/herramientas/montaje/'
sys.path.insert(0, 'D:/DAE/_repo/cursos/bienes-proceso-penal/unidades')
T = 'D:/DAE/_tmp/bi_u/'
log = open(T + 'lote_cadena.log', 'a', encoding='utf-8')
lock = threading.Lock()


def w(*a):
    with lock:
        print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)


def cola():
    try:
        return [l.strip() for l in open(T + 'cola.txt', encoding='utf-8') if l.strip()]
    except OSError:
        return []


def cadena(p):
    try:
        P = importlib.import_module(p)
        cl = P.TMP + '/cadena.log'
        s = open(cl, encoding='utf-8', errors='replace').read() if os.path.exists(cl) else ''
        if os.path.exists(P.COMPUESTO) and os.path.exists(P.TITULO) and 'LOTE LISTO' in s:
            w('cadena', p, 'ya estaba'); return
        t = time.time()
        r = subprocess.run([PY, M + 'profe_cadena.py', p, 'componer', 'titulo', 'cartones'], capture_output=True, text=True, errors='replace')
        s = open(cl, encoding='utf-8', errors='replace').read() if os.path.exists(cl) else ''
        w('cadena', p, 'rc', r.returncode, 'LOTE LISTO' in s, '%.0f s' % (time.time() - t), '|', ' '.join(s.split())[-420:], '|', r.stderr[-300:] if r.returncode else '')
    except Exception as e:
        w('CADENA EXCEPCION', p, repr(e)[:400])


ex = ThreadPoolExecutor(max_workers=3)
vistos = []
while True:
    c = cola()
    for p in c:
        if p != 'FIN' and p not in vistos:
            vistos.append(p); ex.submit(cadena, p); w('en cola', p)
    if 'FIN' in c:
        break
    time.sleep(10)
ex.shutdown(wait=True)
w('CADENAS LISTAS')
