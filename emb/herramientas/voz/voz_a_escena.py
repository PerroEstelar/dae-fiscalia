"""voz_a_escena.py calzado.json bloques.json salida.js [cola=40]
Convierte el calzado de la voz (calzar_emb.py) en window.VOZ para la escena.
Cada bloque queda con: i (orden), off (cuadro de su sección en que arranca la voz: 14 el primero,
8 los demás), d (duración de la sección hasta que arranca la voz del bloque siguiente) y el mapa
carácter → cuadro relativo al inicio de la sección. Las claves son los primeros 40 caracteres del
texto (pieza.js) y también B1, B2… (escena del Video 1).
Entre dos secciones con voz puede haber secciones sin voz (la ruta): cada bloque se ubica en el
cuadro de su sección, así que la voz se monta por tramos (armar_voz.py)."""
import json, sys
fps = 24000 / 1001
v = json.load(open(sys.argv[1]))['bloques']; bl = json.load(open(sys.argv[2])); out = sys.argv[3]
cola = int(sys.argv[4]) if len(sys.argv) > 4 else 40
off = [14] + [8] * (len(v) - 1)
res = {}
for i, b in enumerate(v):
    if i < len(v) - 1:
        d = round((v[i + 1]['ini'] - b['ini']) * fps) + off[i] - off[i + 1]
    else:
        d = round((b['fin'] - b['ini']) * fps) + off[i] + cola
    ent = {'i': i, 'off': off[i], 'd': d, 'ini': b['ini'], 'sig': v[i + 1]['ini'] if i < len(v) - 1 else None,
           'mapa': [[c, round(off[i] + (t - b['ini']) * fps, 1)] for c, t in b['mapa']]}
    res[bl[i][:40]] = ent; res[f'B{i + 1}'] = ent
open(out, 'w').write('window.VOZ=' + json.dumps(res, ensure_ascii=False) + ';')
print({f'B{i+1}': res[f'B{i+1}']['d'] for i in range(len(v))})
