# -*- coding: utf-8 -*-
"""Gerencia judicial, videos de profe (27 nov 2026): saca de las grabaciones largas el _fuente.mp4 de cada pieza
(2 s antes de la primera palabra y 2,5 s despues de la ultima, sin pasar a la pieza vecina), a 30 c/s parejos,
H.264 CRF 12, BT.709, AAC 320k. El inicio de la U1 es la toma completa de VIDEO 2 y, pegada detras, la frase de
la evaluacion de VIDEO 3 (en VIDEO 2 dice 'al cierre de cada unidad de los tres temas')."""
import glob, json, os, subprocess, sys
FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
R = 'E:/DAE MASTER/PRIORIDAD 2/CURSO - GERENCIA JUDICIAL/VIDEOS PROFE/'
V2 = R + 'UNIDAD 1/INICIO/01 VIDEO/VIDEO 2 GERENCIA JUDICIAL TOMA1.mp4'
V3 = R + '00 FUENTES/VIDEO 3 GERENCIA JUDICIAL TOMA- unidades guienes de apertura y cierre.mp4'
T = 'D:/DAE/_tmp/gj_p/'
W = {k: [w for w in json.load(open(T + 'stt_fuente/' + k + '.json', encoding='utf-8'))['words'] if w['type'] == 'word'] for k in ('gjv2', 'gjv3')}
VENT = {'u1c': ('gjv3', 179, 332), 'u2i': ('gjv3', 348, 493), 'u2c': ('gjv3', 508, 655), 'u3i': ('gjv3', 672, 843),
        'u3c': ('gjv3', 861, 1010), 'u4i': ('gjv3', 1036, 1190), 'u4c': ('gjv3', 1207, 1356),
        'u1ia': ('gjv2', 45, 206), 'u1ib': ('gjv3', 142.0, 154.9)}
CARP = {'u1c': 'UNIDAD 1/CIERRE', 'u2i': 'UNIDAD 2/INICIO', 'u2c': 'UNIDAD 2/CIERRE', 'u3i': 'UNIDAD 3/INICIO',
        'u3c': 'UNIDAD 3/CIERRE', 'u4i': 'UNIDAD 4/INICIO', 'u4c': 'UNIDAD 4/CIERRE', 'u1i': 'UNIDAD 1/INICIO'}
DUR = {'gjv2': 206.62, 'gjv3': 1373.18}


def rango(k):
    s, a, b = VENT[k]
    ws = W[s]
    sel = [i for i, w in enumerate(ws) if a - 0.3 <= w['start'] <= b]
    i0, i1 = sel[0], sel[-1]
    lo = ws[i0 - 1]['end'] + 0.3 if i0 > 0 else 0.0
    hi = ws[i1 + 1]['start'] - 0.3 if i1 + 1 < len(ws) else DUR[s]
    t0 = max(ws[i0]['start'] - 2.0, lo, 0.0)
    t1 = min(ws[i1]['end'] + 2.5, hi, DUR[s])
    # en cuadros enteros de 30 c/s
    f0 = int(t0 * 30); f1 = int(t1 * 30 + 0.999)
    return s, f0, f1


ENC = ['-c:v', 'libx264', '-crf', '12', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-colorspace', 'bt709',
       '-color_primaries', 'bt709', '-color_trc', 'bt709', '-c:a', 'aac', '-b:a', '320k', '-ar', '48000', '-movflags', '+faststart']
src = {'gjv2': V2, 'gjv3': V3}
man = {}
solo = sys.argv[1:]
for k in ('u1c', 'u2i', 'u2c', 'u3i', 'u3c', 'u4i', 'u4c'):
    if solo and k not in solo: continue
    s, f0, f1 = rango(k)
    out = R + CARP[k] + '/01 VIDEO/gj_%s_fuente.mp4' % k
    man[k] = {'src': os.path.basename(src[s]), 'cuadro0': f0, 'cuadro1': f1, 'out': out}
    if os.path.exists(out): continue
    vf = 'trim=start_frame=%d:end_frame=%d,setpts=PTS-STARTPTS' % (f0, f1)
    af = 'atrim=start=%.6f:end=%.6f,asetpts=PTS-STARTPTS' % (f0 / 30, f1 / 30)
    subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', src[s], '-filter_complex', '[0:v]%s[v];[0:a]%s[a]' % (vf, af),
                    '-map', '[v]', '-map', '[a]', '-r', '30'] + ENC + [out + '.parcial.mp4'], check=True)
    os.replace(out + '.parcial.mp4', out)
# U1 inicio: VIDEO 2 entera desde la toma buena + la frase de VIDEO 3
if not solo or 'u1i' in solo:
    sa, a0, a1 = rango('u1ia'); sb, b0, b1 = rango('u1ib')
    out = R + CARP['u1i'] + '/01 VIDEO/gj_u1i_fuente.mp4'
    man['u1i'] = {'src_a': os.path.basename(V2), 'a': [a0, a1], 'src_b': os.path.basename(V3), 'b': [b0, b1], 'offset_b': a1 - a0, 'out': out}
    if not os.path.exists(out):
        g = ('[0:v]trim=start_frame=%d:end_frame=%d,setpts=PTS-STARTPTS[va];[0:a]atrim=start=%.6f:end=%.6f,asetpts=PTS-STARTPTS[aa];'
             '[1:v]trim=start_frame=%d:end_frame=%d,setpts=PTS-STARTPTS[vb];[1:a]atrim=start=%.6f:end=%.6f,asetpts=PTS-STARTPTS[ab];'
             '[va][aa][vb][ab]concat=n=2:v=1:a=1[v][a]' % (a0, a1, a0 / 30, a1 / 30, b0, b1, b0 / 30, b1 / 30))
        subprocess.run([FB + '/ffmpeg.exe', '-y', '-v', 'error', '-i', V2, '-i', V3, '-filter_complex', g, '-map', '[v]', '-map', '[a]', '-r', '30'] + ENC + [out + '.parcial.mp4'], check=True)
        os.replace(out + '.parcial.mp4', out)
prev = json.load(open(T + 'fuentes_piezas.json', encoding='utf-8')) if os.path.exists(T + 'fuentes_piezas.json') else {}
prev.update(man)
json.dump(prev, open(T + 'fuentes_piezas.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('LISTO', json.dumps(man))
