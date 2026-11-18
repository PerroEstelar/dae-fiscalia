# -*- coding: utf-8 -*-
"""Verifica las entregas de Trata que estan en la carpeta de paso de Drive contra el archivo local, por bloques
de 1 MiB. Solo vale si el archivo NO esta en la cache de Drive para escritorio (asi la lectura baja los bytes
del servidor): con C: casi lleno la cache guarda solo el ultimo archivo subido. Si esta en la cache, se hace una
copia de servidor (copy_file del conector) a una carpeta de Mi unidad con el mismo nombre y se compara la copia:
tiene otro id y nunca estuvo en la cache.
Uso: verif_tr.py [copia=<carpeta de las copias>] [nombres...]      Log: verif.log"""
import glob, os, sys, time
T = 'D:/DAE/_tmp/tr_p/'
PASO = 'G:/My Drive/_MA subidas/'
RAIZ = 'D:/DAE MASTER/PRIORIDAD 03/VIDEOS PROFE'
CACHE = glob.glob(os.path.expanduser('~') + '/AppData/Local/Google/DriveFS/*/content_cache')
log = open(T + 'verif.log', 'a', encoding='utf-8')
def w(*a):
    print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)
def en_cache(n):
    for c in CACHE:
        for r, ds, fs in os.walk(c):
            for f in fs:
                try:
                    if os.path.getsize(os.path.join(r, f)) == n:
                        return True
                except OSError:
                    pass
    return False
args = sys.argv[1:]
COPIA = bool(args and args[0].startswith('copia='))
if COPIA:
    PASO = args.pop(0)[6:].rstrip('/') + '/'
nombres = args or sorted(os.path.basename(x) for x in glob.glob(PASO + 'traficoytrata*.mp4'))
for nb in nombres:
    g = PASO + nb
    loc = glob.glob(RAIZ + '/*/*/05 EXPORTS/' + nb)
    if not os.path.exists(g) or len(loc) != 1:
        w('%s|NO ESTA (paso %s, local %d)' % (nb, os.path.exists(g), len(loc))); continue
    l = loc[0]; n = os.path.getsize(l)
    if os.path.getsize(g) != n:
        w('%s|TAMANO DISTINTO %d %d' % (nb, os.path.getsize(g), n)); continue
    if not COPIA and en_cache(n):
        w('%s|EN CACHE: no se puede verificar todavia' % nb); continue
    t = time.time(); mal = None; i = 0
    try:
        with open(g, 'rb') as a, open(l, 'rb') as b:
            while True:
                x = a.read(1 << 20); y = b.read(1 << 20)
                if x != y:
                    mal = i; break
                if not y:
                    break
                i += 1
    except Exception as e:
        w('%s|EXCEPCION %s' % (nb, repr(e)[:200])); continue
    dt = time.time() - t
    w('%s|%s|%d bytes|%.0f s (%.1f MB/s)%s' % (nb, 'IGUAL' if mal is None else 'DISTINTO en el MiB %d' % mal, n, dt, n / 1e6 / max(dt, 0.01), '|copia de servidor' if COPIA else ''))
w('FIN')
