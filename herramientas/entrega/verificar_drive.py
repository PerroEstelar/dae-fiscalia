# -*- coding: utf-8 -*-
r"""Comprueba que lo que guarda Drive es, byte a byte, la entrega local (17 nov 2026).

    python verificar_drive.py <mapa.json> <log> [carpeta en G:]

El tamaño no alcanza: la entrega del cierre de la U5 de Enfoque diferencial tenía en Drive el
mismo tamaño que la local y el último 22 % en ceros.

Cómo se usa:
1. Con el conector, `copy_file` de cada entrega de la carpeta compartida a una carpeta de
   «Mi unidad» (por defecto `_MA subidas/_verif entregas`), con el nombre `<clave>.mp4`. Es una
   copia de servidor: son los bytes que guarda Drive, los mismos que ve quien abre el enlace.
2. `mapa.json` = {clave: ruta de la entrega local}.
3. Este script espera a que Drive para escritorio baje cada copia completa y la compara por
   bloques de 1 MiB con la local. Escribe «OK» o «MAL» con los MiB distintos y cuántos son
   todo ceros.
4. Después, la carpeta de copias va a la papelera con el conector.

El 17 nov se verificaron así las 11 entregas de profe de Derechos humanos y las 12 de Enfoque
diferencial: solo el cierre de la U5 de ED estaba dañado.
"""
import json
import os
import sys
import time

mapa = json.load(open(sys.argv[1], encoding='utf-8'))
log = open(sys.argv[2], 'w', encoding='utf-8')
V = sys.argv[3] if len(sys.argv) > 3 else 'G:/My Drive/_MA subidas/_verif entregas/'
CH = 1 << 20
pend = dict(mapa)
t0 = time.time()
while pend and time.time() - t0 < 3600:
    for clave, local in list(pend.items()):
        copia = V + clave + '.mp4'
        n = os.path.getsize(local)
        if not (os.path.exists(copia) and os.path.getsize(copia) == n):
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
            print('MAL', clave, len(malos), 'MiB distintos (%d todo ceros)' % ceros,
                  '%d-%d MiB de %d' % (malos[0], malos[-1], i), file=log, flush=True)
        else:
            print('OK ', clave, n, file=log, flush=True)
        del pend[clave]
    time.sleep(10)
print('SIN TERMINAR', sorted(pend), file=log, flush=True)
print('LISTO', file=log, flush=True)
