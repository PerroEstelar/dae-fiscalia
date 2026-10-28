import sys, json
sys.path.insert(0, '/tmp/claude-0/-home-claude/3ed68810-2da1-5d00-9607-4b64ae51b22f/scratchpad/ch')
import numpy as np, v2graf as G
S = '/mnt/user-data/uploads/DAE/_tmp/ch/seg/'
O = '/tmp/claude-0/-home-claude/3ed68810-2da1-5d00-9607-4b64ae51b22f/scratchpad/ch/out/c3/'
FPS = 24000 / 1001
I1 = 95.68
T = 2233
piezas = json.load(open(O + 'piezas_a.json'))
# 1) carton captura sobre la patrulla limpia (1522 -> 1645, corte)
base = list(G.leer(S + 'c3_limpio_f1500.mp4', n=123, desde=22))
fr = G.carton_cuadros(base, ['Se procede a la captura', 'de cinco adultos y de la menor', 'de edad Disney, de dieciséis años'],
                      velo_in=10, velo_out=8, txt_desde=5, txt_hasta=118, txt_in=11, txt_out=9)
G.mp4(fr, O + 'CH_U1_C03_carton_captura_f1522.mp4')
piezas.append(dict(archivo='CH_U1_C03_carton_captura_f1522.mp4', en=1522, cuadros=123, pista=2))
del base
# 2) sofa limpio (V1 1770..1903) entre las placas: V2 2474 -> 2607, carton entorno familiar
base = list(G.leer(S + 'c3_limpio_f1740.mp4', n=133, desde=30))
fr = G.carton_cuadros(base, ['El entorno familiar fue calificado', 'como un factor protector'],
                      velo_in=10, velo_out=8, txt_desde=4, txt_hasta=125, txt_in=11, txt_out=9)
G.mp4(fr, O + 'CH_U1_C03_inserto_2_sofa.mp4')
piezas.append(dict(archivo='CH_U1_C03_inserto_2_sofa.mp4', en=T + 241, cuadros=133, pista=1))
del base
# 3) placa B otra vez, con fundido a blanco al final (como la V1 antes del rotulo)
B = [G.con_marca(b) for b in G.leer(S + 'CH_U1_C03_placaB_cocina_iGCjkUa3uK.mp4', n=100)]
inicioB = T + 241 + 133
tb = int(round((I1 + 13.26) * FPS)) - inicioB
fr = list(G.carton_cuadros(B, ['Sin antecedentes de violencia', 'intrafamiliar, negligencia o maltrato'],
                           velo_desde=0, velo_hasta=92, velo_in=10, velo_out=8,
                           txt_desde=max(2, tb - 2), txt_hasta=90, txt_in=10, txt_out=8))
for i in range(12):
    k = G.ease((i + 1) / 12)
    j = 88 + i
    fr[j] = (fr[j].astype(np.float32) * (1 - k) + 253 * k + 0.5).astype(np.uint8)
G.mp4(fr, O + 'CH_U1_C03_inserto_3_placaB.mp4')
json.dump(piezas, open(O + 'piezas.json', 'w'), indent=1, ensure_ascii=False)
print(piezas)
from PIL import Image
def uno(p, k): return G.leer(O + p, n=1, desde=k)[0]
sel = [uno('CH_U1_C03_carton_captura_f1522.mp4', k) for k in (3, 20, 100, 121)] + [uno('CH_U1_C03_inserto_2_sofa.mp4', k) for k in (2, 30, 120, 131)] + [uno('CH_U1_C03_inserto_3_placaB.mp4', k) for k in (10, 50, 92, 99)]
o = Image.new('RGB', (640 * 4, 360 * 3))
for i, f in enumerate(sel): o.paste(Image.fromarray(f).resize((640, 360)), ((i % 4) * 640, (i // 4) * 360))
o.save(O + 'chk_b.jpg')
