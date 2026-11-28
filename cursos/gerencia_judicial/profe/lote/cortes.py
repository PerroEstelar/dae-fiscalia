# -*- coding: utf-8 -*-
"""Gerencia judicial, videos de profe (27 nov 2026): mide los puntos de corte de cada pieza sobre la grabacion
original. Para cada corte (las palabras [a, b) salen) busca, en el hueco antes de la palabra a y en el hueco antes
de la palabra b, el borde de cuadro (30 c/s) con menos energia de voz (RMS de 24 ms alrededor del borde), y
mide cuanto cambia la imagen entre el ultimo cuadro de antes y el primero de despues (gris 160x90, diferencia
media). Tambien da la pausa siguiente (hueco >= 0,35 s) para un plano cerrado.
Uso: gj_cortes.py <spec.json> <salida.json>"""
import glob, json, os, subprocess, sys
import numpy as np
FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
R = 'E:/DAE MASTER/PRIORIDAD 2/CURSO - GERENCIA JUDICIAL/VIDEOS PROFE/'
SRC = {'gjv1': R + 'CURSO/INICIO/01 VIDEO/VIDEO 1 GERENCIA JUDICIAL TOMA1.mp4',
       'gjv2': R + 'UNIDAD 1/INICIO/01 VIDEO/VIDEO 2 GERENCIA JUDICIAL TOMA1.mp4',
       'gjv3': R + '00 FUENTES/VIDEO 3 GERENCIA JUDICIAL TOMA- unidades guienes de apertura y cierre.mp4'}
T = 'D:/DAE/_tmp/gj_p/'
SR = 16000
spec = json.load(open(sys.argv[1], encoding='utf-8'))
_aud, _W = {}, {}


def audio(s):
    if s not in _aud:
        b = subprocess.run([FB + '/ffmpeg.exe', '-v', 'error', '-i', SRC[s], '-vn', '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
        _aud[s] = np.frombuffer(b, np.float32)
    return _aud[s]


def words(s):
    if s not in _W:
        _W[s] = [w for w in json.load(open(T + 'stt_fuente/' + s + '.json', encoding='utf-8'))['words'] if w['type'] == 'word']
    return _W[s]


def db(x):
    return 10 * np.log10(np.mean(x.astype(np.float64) ** 2) + 1e-12)


def nivel(s, t, med=0.012):
    a = audio(s); i0 = max(0, int((t - med) * SR)); i1 = int((t + med) * SR)
    return db(a[i0:i1])


_ref = {}
def ref(s):
    if s not in _ref:
        a = audio(s); ws = words(s)
        v = [db(a[int(w['start'] * SR):int(w['end'] * SR)]) for w in ws[::7] if w['end'] - w['start'] > 0.15]
        _ref[s] = float(np.median(v))
    return _ref[s]


def gris(s, k):
    b = subprocess.run([FB + '/ffmpeg.exe', '-v', 'error', '-ss', '%.4f' % ((k + 0.5) / 30), '-i', SRC[s], '-frames:v', '1', '-vf', 'scale=160:90,format=gray',
                        '-f', 'rawvideo', '-'], capture_output=True).stdout
    return np.frombuffer(b, np.uint8).astype(np.float32)


def mejor(s, lo, hi, pref, mg=0.017):
    """El borde de cuadro en [lo, hi] con menos energia; entre los que estan a 3 dB del minimo, el mas cercano a pref."""
    ks = list(range(int(np.floor((lo - mg) * 30)), int(np.ceil((hi + mg) * 30)) + 1))
    ks = [k for k in ks if lo - mg <= k / 30 <= hi + mg] or [int(round(pref * 30))]
    lv = [(nivel(s, k / 30), k) for k in ks]
    m = min(l for l, _ in lv)
    cand = [(abs(k / 30 - pref), k, l) for l, k in lv if l <= m + 3]
    _, k, l = min(cand)
    return k, l


def pausa_despues(s, t, minimo=0.35):
    ws = words(s)
    for i in range(1, len(ws)):
        if ws[i]['start'] > t and ws[i]['start'] - ws[i - 1]['end'] >= minimo and ws[i - 1]['end'] >= t:
            return int(round((ws[i - 1]['end'] + ws[i]['start']) / 2 * 30)), ws[i - 1]['text']
    return None, None


def idx(s, t):
    ws = words(s)
    return min(range(len(ws)), key=lambda i: abs(ws[i]['start'] - t))


res = []
for p in spec:
    s = p['src']; ws = words(s); r = ref(s)
    out = {'clave': p['clave'], 'src': s, 'ref_db': r, 'cortes': []}
    for c in p['cortes']:
        a = c['a'] if isinstance(c['a'], int) else idx(s, c['a'])
        b = c['b'] if isinstance(c['b'], int) else idx(s, c['b'])
        g1 = (ws[a - 1]['end'], ws[a]['start']); g2 = (ws[b - 1]['end'], ws[b]['start'])
        l1 = g1[1] - g1[0]; l2 = g2[1] - g2[0]
        mg = c.get('mg', 0.017)
        ko, lo_ = mejor(s, g1[0], g1[1], g1[0] + min(0.22, l1 / 2), mg)
        ki, li = mejor(s, g2[0], g2[1], g2[1] - min(0.18, l2 / 2), mg)
        d = float(np.mean(np.abs(gris(s, ko - 1) - gris(s, ki))))
        d0 = float(np.mean(np.abs(gris(s, ki) - gris(s, ki + 1))))
        kp, wp = pausa_despues(s, ws[b]['start'])
        out['cortes'].append({'nota': c.get('nota', ''), 'a': a, 'b': b, 'quita': ' '.join(w['text'] for w in ws[a:b]),
                              'antes': ' '.join(w['text'] for w in ws[max(0, a - 4):a]), 'despues': ' '.join(w['text'] for w in ws[b:b + 4]),
                              'k_out': ko, 'k_in': ki, 'db_out': round(lo_ - r, 1), 'db_in': round(li - r, 1), 'dif': round(d, 2), 'dif_vecinos': round(d0, 2),
                              'pausa': kp, 'pausa_tras': wp})
    if 'ini' in p:
        i0 = idx(s, p['ini']); i1 = idx(s, p['fin'])
        out['k_ini'] = int(round((ws[i0]['start'] - 0.5) * 30)); out['k_fin'] = int(round((ws[i1]['end'] + 0.8) * 30))
        out['primera'] = ws[i0]['text']; out['ultima'] = ws[i1]['text']
    res.append(out)
json.dump(res, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('LISTO')
