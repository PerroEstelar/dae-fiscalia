# -*- coding: utf-8 -*-
"""Gerencia judicial (27 nov 2026): Resolve se quedo en 0 % rindiendo mientras corrian cinco recortes por la placa
(3,4 de 4 GB de memoria de video ocupados). Este vigilante lanza entrega_gpu.py recien cuando queda a lo sumo un
recorte corriendo."""
import subprocess, sys, time
G = 'D:/DAE/_repo/cursos/gerencia_judicial/profe/lote/'
T = 'D:/DAE/_tmp/gj_p/'


def recortes():
    r = subprocess.run(['wmic', 'process', 'where', 'name="python.exe"', 'get', 'CommandLine'], capture_output=True, text=True, errors='replace')
    return sum(1 for l in r.stdout.splitlines() if 'recorta_cuadro.py' in l)


seguidas = 0
while seguidas < 2:
    seguidas = seguidas + 1 if recortes() <= 1 else 0
    time.sleep(30)
print(time.strftime('%H:%M:%S'), 'lanza entrega_gpu', flush=True)
subprocess.Popen([sys.executable, '-X', 'utf8', G + 'entrega_gpu.py'], stdout=open(T + 'entrega_gpu.out', 'w'), stderr=subprocess.STDOUT,
                 creationflags=0x00000008 | 0x00000200)
