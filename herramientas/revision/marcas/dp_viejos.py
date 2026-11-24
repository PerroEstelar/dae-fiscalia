# -*- coding: utf-8 -*-
"""Comentarios de la revisión de DP (23 nov) por lección y escena E##: {'U1 L1': {'E01': texto, ...}}."""
import json, re
R = json.load(open('/home/claude/repo/herramientas/revision/dp/revision_dp.json', encoding='utf-8'))
M = json.load(open('/tmp/claude-0/rev/mapa_celdas.json', encoding='utf-8'))
OUT = {}
for h in R['hojas']:
    u = int(h['hoja'].split()[-1])
    for celda, v in h['celdas'].items():
        col, fila = celda[0], int(celda[1:])
        l = 'BCDE'.index(col) + 1
        n = fila - 1
        OUT.setdefault('U%d L%d' % (u, l), {})['E%02d' % int(n)] = v['t']
if __name__ == '__main__':
    import sys
    lec = sys.argv[1]
    for k, v in sorted(OUT[lec].items()):
        print(k, v)
