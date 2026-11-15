"""voz_a_escena.py calzado.json T0 salida.js [prefijo=B] [cola=40]
Convierte el calzado de la voz (calzar_emb.py) en window.VOZ para la escena: duración de cada
sección y mapa carácter → cuadro relativo a su inicio. La voz arranca 14 cuadros después del
título (T0) y cada bloque siguiente entra 8 cuadros después del inicio de su sección."""
import json, sys
fps = 24000 / 1001
v = json.load(open(sys.argv[1]))['bloques']; T0 = int(sys.argv[2]); out = sys.argv[3]
pref = sys.argv[4] if len(sys.argv) > 4 else 'B'; cola = int(sys.argv[5]) if len(sys.argv) > 5 else 40
VOFF = T0 + 14
S = [VOFF + round(b['ini'] * fps) - (14 if i == 0 else 8) for i, b in enumerate(v)]
res = {}
for i, b in enumerate(v):
    d = (S[i + 1] - S[i]) if i < len(v) - 1 else (VOFF + round(b['fin'] * fps) - S[i] + cola)
    res[f'{pref}{i + 1}'] = {'d': d, 'mapa': [[c, round(VOFF + t * fps - S[i], 1)] for c, t in b['mapa']]}
open(out, 'w').write('window.VOZ=' + json.dumps(res) + ';\nwindow.VOZ_CUADRO=' + str(VOFF) + ';')
print('voz en el cuadro', VOFF, {k: x['d'] for k, x in res.items()})
