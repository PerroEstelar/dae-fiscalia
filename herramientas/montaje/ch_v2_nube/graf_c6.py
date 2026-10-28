import sys, json
sys.path.insert(0, '/tmp/claude-0/-home-claude/3ed68810-2da1-5d00-9607-4b64ae51b22f/scratchpad/ch')
import numpy as np, v2graf as G
S = '/mnt/user-data/uploads/DAE/_tmp/ch/seg/'
O = '/tmp/claude-0/-home-claude/3ed68810-2da1-5d00-9607-4b64ae51b22f/scratchpad/ch/out/c6/'
piezas = []
# 1-2 rotulos «Caso Lenin»
for nm, f0 in (('c6_full_f185', 185), ('c6_full_f1925', 1925)):
    fr = G.leer(S + nm + '.mp4')
    out, log, sz = G.titulo_cambiar(fr, 'Lenin', x0=481, sz=66)
    idx = [i for i, l in log if isinstance(l, int)]
    a, b = idx[0], idx[-1] + 1
    dst = O + 'CH_U1_C06_rotulo_Lenin_f%d.mp4' % (f0 + a)
    G.mp4(out[a:b], dst)
    piezas.append(dict(archivo=dst.split('/')[-1], cuadro_v1=f0 + a, cuadros=b - a, que='rotulo Caso Lenin'))
    print(nm, 'cambiados', a, b, 'dy', [l for l in log if l[1] not in ('-', 0)][:12], sz)
# 3 etiqueta colegio
L = G.leer(S + 'c6_limpio_f300.mp4')
texto, barra = G.etiqueta_capa(['Colegio Jimmy Carter,', 'Bogotá D.C.,', '23 de mayo de 2025'], 84, 251, 887, 103,
                               sombra=(2, 4, 7, 0.30))
texto[..., :3] = np.where(texto[..., 3:4] > 0, np.minimum(texto[..., :3], 253), texto[..., :3])
seg = []
for f in range(316, 412):
    k_in = (f - 322) / 4.0
    k_out = (f - 404) / 6.0 if f >= 404 else 0
    base = L[f - 300]
    if f < 322:
        seg.append(base)
        continue
    seg.append(G.sobre(base, G.etiqueta_cuadro(texto, barra, k_in, min(1, k_out))))
dst = O + 'CH_U1_C06_etiqueta_colegio_f316.mp4'
G.mp4(seg, dst)
piezas.append(dict(archivo=dst.split('/')[-1], cuadro_v1=316, cuadros=len(seg), que='etiqueta Colegio Jimmy Carter'))
# 4 etiqueta Nicol
L = G.leer(S + 'c6_limpio_f495.mp4')
texto, barra = G.etiqueta_capa(['Nicol'], 81, 265, 754, 0, sombra=(2, 4, 7, 0.30))
seg = []
for f in range(519, 563):
    base = L[f - 495]
    if f < 523:
        seg.append(base)
        continue
    k_in = (f - 523) / 2.0
    k_out = (f - 557) / 4.0 if f >= 557 else 0
    seg.append(G.sobre(base, G.etiqueta_cuadro(texto, barra, k_in, min(1, k_out))))
dst = O + 'CH_U1_C06_etiqueta_Nicol_f519.mp4'
G.mp4(seg, dst)
piezas.append(dict(archivo=dst.split('/')[-1], cuadro_v1=519, cuadros=len(seg), que='etiqueta Nicol'))
json.dump(piezas, open(O + 'piezas.json', 'w'), indent=1, ensure_ascii=False)
print(piezas)
