# -*- coding: utf-8 -*-
r"""El plan para APRETAR una pieza de Derechos humanos (huecos de narracion mas
cortos, personajes un poco mas rapidos) y el mapa de tiempo con el que todo
lo demas se corre. Es lo que en la U3 se hizo a mano en la nube
(`mapa_u3.py`, `final_u3.py`), escrito una vez para todas.

    python plan_apretar_dh.py U4 plan
        -> D:\DAE\_tmp\dh\<L>_apretado\plan.json y piezas.json
    python voz\apretar_dh.py <master> piezas.json <salida.wav>
    python plan_apretar_dh.py U4 final <master_apretado.wav> <retrato_suyo.json>
        -> mapa.json (items de su linea pasados por el mapa, ranuras, cortes
           de las compuestas, detalles), nuevo\DH_<L>_rejilla.json,
           nuevo\DH_<L>_ranuras.json y nuevo\stt\*.json
    python plan_apretar_dh.py U4 instalar <master_apretado.wav>
        -> el master, la rejilla, las ranuras y los stt de antes van a
           _descartes (__antes_de_apretar_<hora>) y entran los nuevos; el
           master entra como DH_<L>_NARRADOR.wav y como _v<n> (nombre nuevo
           para la linea: la cache de Resolve)

DH U3, 1 nov (Sebastian): «we need to shorten some of the narration gaps…
it sounds glitchy, also make the other characters besides the main narrator
talk a bit faster». Lo mismo, pedido para U4 y U5 antes de revisarlas.

LAS REGLAS (las de la U3, medidas alli)
    Envolvente de la voz a -48 dB sobre el master a 16 kHz mono.
    Hueco nuevo entre el fin de habla de un bloque y el arranque del
    siguiente (nunca mas largo que el que habia):
        narrador <-> personaje        1,0 s
        mismo personaje o Carlos-Carlos 0,65 (0,9 si el viejo pasaba de 1,5)
        personaje -> otro personaje   0,45
        si el guion pedia CAPITULO (>= 1,6) el hueco no baja de 0,9; si
        pedia 2,0 o mas, no baja de 1,1
        junto a un bloque SILENCIO    1,0
    Pausas internas: de los personajes, las de 0,40 s o mas quedan en 0,34;
    de Carlos, las de 0,55 o mas, en 0,45.
    Tempo (atempo, no cambia el tono): ver TEMPO. Carlos a 1.
    Un bloque SILENCIO (la «otra silla» de la U4) es una escena sin dialogo
    con su carton encima: se queda entero.

EL MAPA
    Es lineal por tramos: dentro de un hueco o una pausa que se acorta,
    proporcional; dentro del habla, dividido por el tempo. `atempo` deja
    unos milisegundos por bloque, asi que `final` mide los arranques en el
    master armado y corrige el mapa con ellos.
"""
import glob
import json
import os
import re
import subprocess
import sys

import numpy as np

H = r'D:\DAE\_repo\herramientas'
for sub in ('montaje', 'prompts', os.path.join('voz', 'textos')):
    sys.path.insert(0, os.path.join(H, sub))

import rutas_dh as R                                    # noqa: E402
from guion_dh import bloques                            # noqa: E402

FPS = 24000 / 1001.0
TH = -48
A0 = 182 + 119
TEMPO = {'Carlos': 1.0, 'Carmen': 1.08, 'Entrevistador': 1.08, 'Sandra': 1.12,
         'Juez': 1.08, 'Quintero': 1.08, 'Salgado': 1.12, 'Andres': 1.08,
         'Julian': 1.05, 'SILENCIO': 1.0}
CAP = {'Carlos': (0.55, 0.45), 'otro': (0.40, 0.34)}


def carpeta(L):
    d = os.path.join(r'D:\DAE\_tmp\dh', '%s_apretado' % L.lower())
    os.makedirs(d, exist_ok=True)
    return d


def envolvente(wav):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', wav, '-ac', '1', '-ar', '16000',
                          '-f', 's16le', '-'], capture_output=True).stdout
    x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768
    n = len(x) // 160
    return 20 * np.log10(np.sqrt((x[:n * 160].reshape(n, 160) ** 2).mean(1) + 1e-12))


def habla(db, a, b):
    i0, i1 = max(0, int(a * 100)), int(b * 100)
    idx = np.where(db[i0:i1] > TH)[0]
    if not len(idx):
        return None, None
    return (i0 + idx[0]) / 100.0, (i0 + idx[-1] + 1) / 100.0


def silencios(db, a, b, mind):
    i0, i1 = int(round(a * 100)), int(round(b * 100))
    s = db[i0:i1] < TH
    out, k = [], 0
    while k < len(s):
        if s[k]:
            j = k
            while j < len(s) and s[j]:
                j += 1
            if (j - k) / 100.0 >= mind:
                out.append(((i0 + k) / 100.0, (i0 + j) / 100.0))
            k = j
        else:
            k += 1
    return out


def hueco_nuevo(prev, cur, viejo, pausa):
    if 'SILENCIO' in (prev['voz'], cur['voz']):
        return min(viejo, 1.0)
    a, b = prev['voz'] == 'Carlos', cur['voz'] == 'Carlos'
    if a != b:
        n = 1.0
    elif prev['voz'] == cur['voz']:
        n = 0.9 if viejo >= 1.5 else 0.65
    else:
        n = 0.45
    if pausa >= 2.0:
        n = max(n, 1.1)
    elif pausa >= 1.6:
        n = max(n, 0.9)
    return min(viejo, n)


def plan(L):
    V = R.voces(L)
    wav = os.path.join(V, 'DH_%s_NARRADOR.wav' % L)
    db = envolvente(wav)
    rej = json.load(open(os.path.join(V, 'DH_%s_rejilla.json' % L), encoding='utf-8'))
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=duration_ts',
                                '-of', 'csv=p=0', wav], capture_output=True, text=True).stdout) / 48000.0
    pausa = {b[0]: b[4] for b in bloques(L)}
    tr = rej['tramos']
    for t in tr:
        if t['voz'] == 'SILENCIO':
            t['h0'], t['h1'] = t['entra'], t['sale']
        else:
            t['h0'], t['h1'] = habla(db, t['entra'], t['sale'])
    seg = [('cabeza', 0.0, tr[0]['h0'], tr[0]['h0'], 1.0, '')]
    for i, t in enumerate(tr):
        if i:
            p = tr[i - 1]
            viejo = t['h0'] - p['h1']
            seg.append(('hueco', p['h1'], t['h0'], hueco_nuevo(p, t, viejo, pausa.get(t['bloque'], 0)),
                        1.0, t['bloque']))
        tempo = TEMPO.get(t['voz'], 1.08)
        cur = t['h0']
        if t['voz'] != 'SILENCIO':
            umb, nuevo = CAP['Carlos' if t['voz'] == 'Carlos' else 'otro']
            for a, b in silencios(db, t['h0'], t['h1'], umb):
                seg.append(('habla', cur, a, (a - cur) / tempo, tempo, t['bloque']))
                seg.append(('pausa', a, b, nuevo / tempo, tempo, t['bloque']))
                cur = b
        seg.append(('habla', cur, t['h1'], (t['h1'] - cur) / tempo, tempo, t['bloque']))
    seg.append(('cola', tr[-1]['h1'], dur, dur - tr[-1]['h1'], 1.0, ''))
    anc = [(0.0, 0.0)]
    for s in seg:
        anc.append((s[2], anc[-1][1] + s[3]))
    # las piezas que arma apretar_dh: un hueco conserva sus orillas
    piezas, blk = [], None
    for s in seg:
        tipo, a, b, nl, tempo, bl = s
        if tipo in ('cabeza', 'cola', 'hueco'):
            if blk:
                piezas.append(blk)
                blk = None
            if tipo == 'hueco' and nl < b - a - 1e-6:
                piezas.append({'tipo': 'copia', 'rangos': [[a, a + nl / 2], [b - nl / 2, b]]})
            else:
                piezas.append({'tipo': 'copia', 'rangos': [[a, b]]})
            continue
        if blk is None or blk['bloque'] != bl:
            if blk:
                piezas.append(blk)
            blk = {'tipo': 'bloque', 'bloque': bl, 'tempo': tempo, 'rangos': []}
        if tipo == 'habla':
            blk['rangos'].append([a, b])
        else:
            keep = nl * tempo
            blk['rangos'] += ([[a, b]] if keep >= b - a else
                              [[a, a + keep / 2], [b - keep / 2, b]])
    if blk:
        piezas.append(blk)
    for pz in piezas:
        r = []
        for a, b in pz['rangos']:
            if r and abs(r[-1][1] - a) < 1e-9:
                r[-1][1] = b
            else:
                r.append([a, b])
        pz['rangos'] = [[round(a, 4), round(b, 4)] for a, b in r if b > a]
    d = carpeta(L)
    nuevo = anc[-1][1]
    json.dump({'piezas': piezas, 'dur_nuevo': nuevo}, open(os.path.join(d, 'piezas.json'), 'w'), indent=0)
    json.dump({'seg': seg, 'anc': anc, 'dur_viejo': dur, 'dur_nuevo': nuevo,
               'tramos': [dict(bloque=t['bloque'], voz=t['voz'], h0=t['h0'], h1=t['h1']) for t in tr]},
              open(os.path.join(d, 'plan.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    por = {}
    for s in seg:
        por.setdefault(s[0], [0.0, 0.0])
        por[s[0]][0] += s[2] - s[1]
        por[s[0]][1] += s[3]
    print('%s: %.2f -> %.2f s (%.1f s menos)' % (L, dur, nuevo, dur - nuevo))
    for k, (o, n) in por.items():
        print('   %-6s %.2f -> %.2f' % (k, o, n))


def final(L, master, retrato):
    d = carpeta(L)
    p = json.load(open(os.path.join(d, 'plan.json'), encoding='utf-8'))
    oldx = np.array([a for a, _ in p['anc']])
    newx = np.array([b for _, b in p['anc']])

    def m0(t):
        return float(np.interp(t, oldx, newx))
    db = envolvente(master)
    dur_n = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=duration_ts',
                                  '-of', 'csv=p=0', master], capture_output=True, text=True).stdout) / 48000.0
    cp, ca = [0.0], [0.0]
    for t in p['tramos']:
        e0, e1 = m0(t['h0']), m0(t['h1'])
        if t['voz'] == 'SILENCIO':
            a0 = e0 + (ca[-1] - cp[-1])
        else:
            a0, _ = habla(db, e0 - 0.25, e1 + 0.25)
        d0 = a0 - e0
        cp += [e0, e1]
        ca += [e0 + d0, e1 + d0]
    cp.append(p['dur_nuevo'])
    ca.append(dur_n)
    cp, ca = np.array(cp), np.array(ca)

    def M(t):
        return float(np.interp(m0(t), cp, ca))
    dur_v = p['dur_viejo']
    ret = json.load(open(retrato, encoding='utf-8'))
    a1 = [x for x in ret if x['t'] == 'a' and x['k'] == 1][0]
    fin_v = a1['e']
    fin_n = A0 + int(round(dur_n * FPS))

    def F(f):
        if f <= A0:
            return f
        if f >= fin_v:
            return f - fin_v + fin_n
        return A0 + int(round(M((f - A0) / FPS) * FPS))
    items = [dict(x, ns=F(x['s']), ne=F(x['e'])) for x in ret]
    v1 = [x for x in items if x['t'] == 'v' and x['k'] == 1
          and re.match(r'DH_%s_r\d\d_' % L, x['f'])]
    ranuras = {int(x['f'][7:9]): [x['ns'], x['ne'] - x['ns'], x['s'], x['e'] - x['s']] for x in v1}
    import importlib
    E = importlib.import_module('escenas_dh_%s' % L.lower())
    comp = {}
    for n, partes in getattr(E, 'COMPUESTAS', {}).items():
        c = partes[0][1]
        comp[n] = F(ranuras[n][2] + c) - ranuras[n][0]
    det = {}
    for (n, nm), dd in getattr(E, 'DET', {}).items():
        a, b = F(ranuras[n][2] + dd['entra']), F(ranuras[n][2] + dd['entra'] + dd['cuadros'])
        det[nm] = dict(ranura=n, entra=a - ranuras[n][0], cuadros=b - a)
    out = {'L': L, 'dur_viejo': dur_v, 'dur_nuevo': dur_n, 'A0': A0, 'fin_viejo': fin_v,
           'fin_nuevo': fin_n, 'pieza': max(x['ne'] for x in items), 'items': items,
           'ranuras': ranuras, 'compuestas': comp, 'det': det,
           'anclas': [[round(float(a), 4), round(M(float(a)), 4)] for a in oldx]}
    json.dump(out, open(os.path.join(d, 'mapa.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    # rejilla, ranuras y stt nuevos
    V = R.voces(L)
    nd = os.path.join(d, 'nuevo')
    os.makedirs(os.path.join(nd, 'stt'), exist_ok=True)
    rej = json.load(open(os.path.join(V, 'DH_%s_rejilla.json' % L), encoding='utf-8'))
    viejo = {t['bloque']: dict(t) for t in rej['tramos']}
    for t in rej['tramos']:
        t['entra_antes'], t['sale_antes'] = t['entra'], t['sale']
        e, s = M(t['entra']), M(min(t['sale'], dur_v))
        t['entra'], t['sale'], t['dur'] = round(e, 3), round(s, 3), round(s - e, 3)
    rej['dur'] = round(dur_n, 3)
    rej['apretado'] = ('apretar_dh / plan_apretar_dh: huecos y pausas internas acortados y '
                       'personajes a %s; entra/sale pasados por el mapa' %
                       ', '.join('%s %.2f' % (k, v) for k, v in sorted(TEMPO.items()) if v != 1.0))
    json.dump(rej, open(os.path.join(nd, 'DH_%s_rejilla.json' % L), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    nuevo = {t['bloque']: t for t in rej['tramos']}
    for f in sorted(glob.glob(os.path.join(V, 'stt', 'DH_%s_*.json' % L))):
        j = json.load(open(f, encoding='utf-8'))
        bl = re.sub(r'^DH_%s_\d+_' % L, '', os.path.basename(f))[:-5]
        if bl not in viejo:
            continue
        ev, en = viejo[bl]['entra'], nuevo[bl]['entra']
        for w in j.get('words', []):
            for k in ('start', 'end'):
                if k in w:
                    w[k] = round(M(ev + w[k]) - en, 3)
        j['apretado'] = 'tiempos pasados por el mapa de apretar_dh'
        json.dump(j, open(os.path.join(nd, 'stt', os.path.basename(f)), 'w', encoding='utf-8'),
                  ensure_ascii=False)
    ran = json.load(open(os.path.join(V, 'DH_%s_ranuras.json' % L), encoding='utf-8'))
    for r in ran['ranuras']:
        r['ini_antes'], r['dur_antes'] = r['ini'], r['dur']
        a, b = F(A0 + r['ini']), F(A0 + r['ini'] + r['dur'])
        r['ini'], r['dur'] = a - A0, b - a
    ran['n_ranuras'] = fin_n - A0
    ran['pieza'] = out['pieza']
    ran['apretado'] = 'ranuras pasadas por el mapa de apretar_dh'
    json.dump(ran, open(os.path.join(nd, 'DH_%s_ranuras.json' % L), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('%s: voz %d -> %d cuadros; pieza %d; compuestas %s; det %s'
          % (L, fin_v - A0, fin_n - A0, out['pieza'], comp, det))
    for n in sorted(ranuras):
        print('  r%02d %4d -> %4d' % (n, ranuras[n][3], ranuras[n][1]))


def instalar(L, master):
    import hashlib
    import shutil
    import time
    V = R.voces(L)
    D = os.path.join(V, '_descartes')
    os.makedirs(D, exist_ok=True)
    nd = os.path.join(carpeta(L), 'nuevo')
    suf = '__antes_de_apretar_' + time.strftime('%H%M%S')
    for nm in ('DH_%s_rejilla.json' % L, 'DH_%s_ranuras.json' % L):
        shutil.move(os.path.join(V, nm), os.path.join(D, nm[:-5] + suf + '.json'))
        shutil.copy2(os.path.join(nd, nm), os.path.join(V, nm))
    SD = os.path.join(V, 'stt', '_descartes')
    os.makedirs(SD, exist_ok=True)
    for f in glob.glob(os.path.join(nd, 'stt', '*.json')):
        b = os.path.basename(f)
        shutil.move(os.path.join(V, 'stt', b), os.path.join(SD, b[:-5] + suf + '.json'))
        shutil.copy2(f, os.path.join(V, 'stt', b))
    can = os.path.join(V, 'DH_%s_NARRADOR.wav' % L)
    shutil.move(can, os.path.join(D, 'DH_%s_NARRADOR%s.wav' % (L, suf)))
    n = 2
    while os.path.exists(os.path.join(V, 'DH_%s_NARRADOR_v%d.wav' % (L, n))):
        n += 1
    ver = os.path.join(V, 'DH_%s_NARRADOR_v%d.wav' % (L, n))
    md = lambda f: hashlib.md5(open(f, 'rb').read()).hexdigest()
    for t in (can, ver):
        shutil.copy2(master, t)
        assert md(t) == md(master), t
    open(os.path.join(D, 'LEEME_apretar%s.txt' % suf), 'w', encoding='utf-8').write(
        'Pieza apretada (huecos, pausas, tempo de los personajes): master, rejilla, ranuras '
        'y stt de antes con el sufijo %s. Plan y mapa en %s.\n' % (suf, carpeta(L)))
    print('%s instalado: %s y %s' % (L, os.path.basename(can), os.path.basename(ver)))
    return os.path.basename(ver)


if __name__ == '__main__':
    L, paso = sys.argv[1].upper(), sys.argv[2]
    if paso == 'plan':
        plan(L)
    elif paso == 'final':
        final(L, sys.argv[3], sys.argv[4])
    elif paso == 'instalar':
        instalar(L, sys.argv[3])
