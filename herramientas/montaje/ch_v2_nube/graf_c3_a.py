import sys, json
sys.path.insert(0, '/tmp/claude-0/-home-claude/3ed68810-2da1-5d00-9607-4b64ae51b22f/scratchpad/ch')
import numpy as np, v2graf as G
S = '/mnt/user-data/uploads/DAE/_tmp/ch/seg/'
O = '/tmp/claude-0/-home-claude/3ed68810-2da1-5d00-9607-4b64ae51b22f/scratchpad/ch/out/c3/'
FPS = 24000 / 1001
I1 = 95.68                     # V2: entra la narracion nueva (i1_a)
T = 2233                       # V1/V2: cuadro del inserto
# 1) carton «psicoactivas» sobre Disney de pie (V1 2111-2176; antes del inserto, V2 = V1)
import os
base = list(G.leer(S + 'c3_full_f2060.mp4', n=66, desde=2111 - 2060))
if not os.path.exists(O + 'CH_U1_C03_carton_psicoactivas_f2111.mp4'):
  fr = G.carton_cuadros(base, ['Sin consumo de sustancias', 'psicoactivas'], velo_in=10, velo_out=12,
                      txt_desde=3, txt_hasta=len(base) - 6, txt_in=9, txt_out=9)
  G.mp4(fr, O + 'CH_U1_C03_carton_psicoactivas_f2111.mp4')
piezas = [dict(archivo='CH_U1_C03_carton_psicoactivas_f2111.mp4', en=2111, cuadros=len(base), pista=2)]
del base
# 2) placa A (caminata) 241 cuadros desde T, entra desde blanco; carton madre
A = list(G.leer(S + 'CH_U1_C03_placaA_caminata_tCyn2TAmZJ.mp4', n=241))
A = [G.con_marca(a) for a in A]
for i in range(8):
    k = G.ease((i + 1) / 8)
    A[i] = (A[i].astype(np.float32) * k + 253 * (1 - k)).astype(np.uint8)
def f2(t): return int(round(t * FPS))
t0 = f2(I1 + 0.0) - T          # indice dentro de la placa
v0 = t0 - 10
fr = G.carton_cuadros(A, ['La madre manifestó disposición', 'para acompañar el proceso judicial'],
                      velo_desde=v0, velo_hasta=f2(I1 + 4.6) - T, velo_in=12, velo_out=12,
                      txt_desde=t0, txt_hasta=f2(I1 + 4.4) - T, txt_in=11, txt_out=9)
G.mp4(fr, O + 'CH_U1_C03_inserto_1_placaA.mp4')
piezas.append(dict(archivo='CH_U1_C03_inserto_1_placaA.mp4', en=T, cuadros=241, pista=1))
# 3) placa B (cocina) 100 cuadros desde T+241+133; carton antecedentes
B = [G.con_marca(b) for b in G.leer(S + 'CH_U1_C03_placaB_cocina_iGCjkUa3uK.mp4', n=100)]
inicioB = T + 241 + 133
tb = f2(I1 + 13.26) - inicioB
fr = G.carton_cuadros(B, ['Sin antecedentes de violencia', 'intrafamiliar, negligencia o maltrato'],
                      velo_desde=0, velo_hasta=100, velo_in=10, velo_out=8,
                      txt_desde=max(2, tb - 2), txt_hasta=94, txt_in=10, txt_out=8)
G.mp4(fr, O + 'CH_U1_C03_inserto_3_placaB.mp4')
piezas.append(dict(archivo='CH_U1_C03_inserto_3_placaB.mp4', en=inicioB, cuadros=100, pista=1))
json.dump(piezas, open(O + 'piezas_a.json', 'w'), indent=1)
print(piezas, 't0', t0, 'tb', tb)
from PIL import Image
def uno(p, k): return G.leer(O + p, n=1, desde=k)[0]
sel = [uno('CH_U1_C03_inserto_1_placaA.mp4', 3), uno('CH_U1_C03_inserto_1_placaA.mp4', 90), uno('CH_U1_C03_inserto_1_placaA.mp4', 200),
       uno('CH_U1_C03_inserto_3_placaB.mp4', 5), uno('CH_U1_C03_inserto_3_placaB.mp4', 50), uno('CH_U1_C03_carton_psicoactivas_f2111.mp4', 30)]
o = Image.new('RGB', (960 * 2, 540 * 3))
for k, f in enumerate(sel): o.paste(Image.fromarray(f).resize((960, 540)), ((k % 2) * 960, (k // 2) * 540))
o.save(O + 'chk_a.jpg')
