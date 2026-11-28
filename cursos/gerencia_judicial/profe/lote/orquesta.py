# -*- coding: utf-8 -*-
"""Gerencia judicial, videos de profe (27 nov 2026): pone cada plan en cola.txt recien cuando su recortado existe
(las unidades primero, la bienvenida al curso al final) y cierra la cola con FIN."""
import os, time
T = 'D:/DAE/_tmp/gj_p/'
R = 'E:/DAE MASTER/PRIORIDAD 2/CURSO - GERENCIA JUDICIAL/VIDEOS PROFE/'
P = [('plan_gju1c', 'UNIDAD 1/CIERRE/01 VIDEO/gj_u1c'), ('plan_gju2i', 'UNIDAD 2/INICIO/01 VIDEO/gj_u2i'),
     ('plan_gju2c', 'UNIDAD 2/CIERRE/01 VIDEO/gj_u2c'), ('plan_gju3i', 'UNIDAD 3/INICIO/01 VIDEO/gj_u3i'),
     ('plan_gju3c', 'UNIDAD 3/CIERRE/01 VIDEO/gj_u3c'), ('plan_gju4i', 'UNIDAD 4/INICIO/01 VIDEO/gj_u4i'),
     ('plan_gju4c', 'UNIDAD 4/CIERRE/01 VIDEO/gj_u4c'), ('plan_gju1i', 'UNIDAD 1/INICIO/01 VIDEO/gj_u1i'),
     ('plan_gjci', 'CURSO/INICIO/01 VIDEO/gj_curso_inicio')]
hechos = set()
while len(hechos) < len(P):
    for p, b in P:
        if p not in hechos and os.path.exists(R + b + '_recortado.mp4') and os.path.exists(R + b + '_recortado_mate.mp4'):
            open(T + 'cola.txt', 'a', encoding='utf-8').write(p + '\n'); hechos.add(p)
            print(time.strftime('%H:%M:%S'), 'a la cola', p, flush=True)
    time.sleep(20)
open(T + 'cola.txt', 'a', encoding='utf-8').write('FIN\n')
print('ORQUESTA LISTA', flush=True)
