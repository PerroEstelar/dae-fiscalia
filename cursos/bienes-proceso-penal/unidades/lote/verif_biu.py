# -*- coding: utf-8 -*-
"""Bienes unidades: compara byte a byte cada entrega local con su copia de servidor en la carpeta de verificacion de
Drive (argumento 1: nombre de la carpeta bajo _MA subidas), esperando a que existan las dos. Log: verif_biu.log"""
import os, sys, time
R = 'D:/DAE MASTER/CURSO 5 - Bienes en el proceso penal/'
V = 'G:/My Drive/_MA subidas/%s/' % sys.argv[1]
T = 'D:/DAE/_tmp/bi_u/'
log = open(T + 'verif_biu.log', 'a', encoding='utf-8')
pend = {}
for u in (1, 2, 3, 4):
    for pz in ('INICIO', 'CIERRE'):
        pend['biu%d%s' % (u, pz[0].lower())] = R + 'UNIDAD %d/%s/05 EXPORTS/bienes - U%d - %s-v1.mp4' % (u, pz, u, pz)
CH = 1 << 20
t0 = time.time()
while pend and time.time() - t0 < 14 * 3600 and not os.path.exists(T + 'verif.fin'):
    for k, local in list(pend.items()):
        copia = V + k + '.mp4'
        if not (os.path.exists(local) and os.path.exists(copia)):
            continue
        n = os.path.getsize(local)
        if os.path.getsize(copia) != n:
            continue
        time.sleep(3)
        malos, ceros, i = [], 0, 0
        try:
            with open(local, 'rb') as a, open(copia, 'rb') as c:
                while True:
                    x, y = a.read(CH), c.read(CH)
                    if not x and not y:
                        break
                    if x != y:
                        malos.append(i)
                        if y.count(0) == len(y):
                            ceros += 1
                    i += 1
        except OSError:
            continue
        if malos:
            print('MAL', k, len(malos), 'MiB distintos (%d todo ceros)' % ceros, file=log, flush=True)
        else:
            print('OK ', k, n, file=log, flush=True)
        del pend[k]
    time.sleep(10)
print('SIN TERMINAR', sorted(pend), file=log, flush=True)
print('LISTO', file=log, flush=True)
