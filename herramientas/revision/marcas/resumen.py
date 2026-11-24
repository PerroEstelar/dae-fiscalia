# -*- coding: utf-8 -*-
"""Resumen compacto de una lección capturada: por página, el nombre y los textos visibles con su posición."""
import json, glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import marcas
cur, lec = sys.argv[1], sys.argv[2]
for f in sorted(glob.glob('/home/claude/marcas/cap/%s/%s/*.json' % (cur, lec))):
    js = json.load(open(f, encoding='utf-8'))
    tex, img, marcos = marcas.cajas(js)
    p = js['pagina']
    print('## %02d %s  marcos=%s' % (p[0], p[2], [tuple(int(v) for v in m) for m in marcos]))
    for t in tex:
        if t['b'][1] < 105 and not t['marco']:
            continue
        if not t['marco'] and t['b'][1] > 630:
            continue
        if t['marco'] and (len(t['t'].split()) < 2 or t['t'] in ('Pantalla completa', 'Clic para texto fijo', 'Clic aquí')):
            continue
        if re.match(r'^(Recorra el camino|Elija cada|Exploración|Ponga el cursor|Transcripción|Automática)', t['t']):
            continue
        b = [int(v) for v in t['b']]
        print('   %s%-4d%-4d%-4d%-4d %4.1f %s' % ('i' if t['marco'] else 'g', b[0], b[1], b[2], b[3], t['fs'], t['t'][:90]))
