import sys, json
sys.path.insert(0, '/tmp/claude-0/-home-claude/3ed68810-2da1-5d00-9607-4b64ae51b22f/scratchpad/ch')
import numpy as np, v2graf as G
S = '/mnt/user-data/uploads/DAE/_tmp/ch/seg/'
O = '/tmp/claude-0/-home-claude/3ed68810-2da1-5d00-9607-4b64ae51b22f/scratchpad/ch/out/c2/'
L = G.leer(S + 'c2_limpio_f1520.mp4')
D = 116
base = list(L[1570 - 1520:1570 - 1520 + D])
fr = G.carton_cuadros(base, ['Programa de justicia restaurativa', 'durante la suspensión a prueba'],
                      velo_in=12, velo_out=10, txt_desde=4, txt_hasta=110, txt_in=11, txt_out=9)
G.mp4(fr, O + 'CH_U1_C02_inserto_restaurativa.mp4')
json.dump([dict(archivo='CH_U1_C02_inserto_restaurativa.mp4', cuadros=D, que='inserto: sala (V1 cuadros 1570-1685, limpio) + carton justicia restaurativa')],
          open(O + 'piezas.json', 'w'), ensure_ascii=False, indent=1)
from PIL import Image
Image.fromarray(np.concatenate([np.concatenate([fr[2], fr[10]], 1), np.concatenate([fr[50], fr[108]], 1)], 0)[::2, ::2]).save(O + 'chk.png')
