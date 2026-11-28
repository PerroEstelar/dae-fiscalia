# -*- coding: utf-8 -*-
"""Gerencia judicial, videos de profe (27 nov 2026; es el guion de Ley 1826 con las rutas de este curso): cadena sin After
Effects (componer, titulo, cartones) de los planes de cola.txt,
tres a la vez (o las que diga el primer argumento: con los dos recortes corriendo va de a una, porque la memoria
comprometida hace crecer el archivo de paginacion y C: se queda sin lugar). La cola se puede alargar mientras
corre; termina cuando encuentra la linea FIN. Log: lote_cadena.log"""
import importlib, os, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor
PY = sys.executable
M = 'D:/DAE/_repo/herramientas/montaje/'
sys.path.insert(0, 'D:/DAE/_repo/cursos/gerencia_judicial/profe')
T = 'D:/DAE/_tmp/gj_p/'
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


ex = ThreadPoolExecutor(max_workers=int(sys.argv[1]) if len(sys.argv) > 1 else 3)
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
