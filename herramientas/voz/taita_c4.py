# -*- coding: utf-8 -*-
r"""ED C4: «Taita» se dice TÁI-ta (Sebastian, marcador en 0:24,61 de su linea).

Medido en el STT de las tomas: en d02 la voz dijo «taíta» (tres silabas); en
d06 y d16 el STT oye «Taita», bien dicho. Se rehace SOLO esa palabra:

  1. toma nueva de d02 con «Táita» en el texto (ElevenLabs, Pilar, mismo
     modelo; la llave nunca se imprime);
  2. STT de la toma nueva y del master en ese tramo;
  3. en el master, entre el final de «indígena,» y el comienzo de «de», se
     apaga la palabra vieja (bordes por energia, no por el STT) y entra la
     nueva, centrada en su lugar e igualada en RMS; fundidos de 12 ms dentro
     del silencio. Las pausas del master se quedan como estaban y el master
     mide EXACTAMENTE lo mismo: la rejilla y la linea de Sebastian no se
     mueven.

    python taita_c4.py tomar      pide la toma y la transcribe
    python taita_c4.py injertar   arma ED_C4_NARRADOR_v2.wav (copia del viejo a _descartes)

Resultado (4 nov): el STT del tramo nuevo oye «Taita» (antes «tahita»), 1,64-2,04 s;
mismo numero de muestras (7.551.604).
"""
import json
import os
import shutil
import subprocess
import sys
import time

import numpy as np

H = r'D:\DAE\_repo\herramientas'
for s in ('voz', os.path.join('voz', 'textos'), 'montaje'):
    sys.path.insert(0, os.path.join(H, s))
import rutas_ed as R          # noqa: E402

V = R.voces('C4')
MASTER = os.path.join(V, 'ED_C4_NARRADOR.wav')
# Resolve tiene abierto el master (Windows: «Access is denied» al reemplazarlo)
# y el pool cachea los medios: el corregido va con otro nombre y entra a la
# linea con `cirugia_ed C4 v=2 cambiar <master> <master_v2>` (ReplaceClip).
MASTER_V2 = MASTER[:-4] + '_v2.wav'
TRABAJO = os.path.join(V, '_taita')
TOMA = os.path.join(TRABAJO, 'ED_C4_02_d02_el_taita__taita.mp3')
PILAR = 'x6LHvMgpXmty838MUqHh'
TEXTO = ('autoridad indígena, Táita, de un cabildo con una estructura política '
         'y organizativa débil y escasa capacidad de gobierno propio.')
SR = 48000
ENTRA_D02 = 10.845          # rejilla: el bloque d02 entra en el master aqui


def lee(p, sr=SR):
    o = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', '2', '-ar', str(sr),
                        '-f', 'f32le', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(o, np.float32).reshape(-1, 2).copy()


def stt(p):
    import stt_ed
    return stt_ed.stt(p)


def palabras(d):
    return [(w['text'], w['start'], w['end']) for w in d['words'] if w['type'] == 'word']


def tomar():
    os.makedirs(TRABAJO, exist_ok=True)
    txt = os.path.join(TRABAJO, 'd02_taita.txt')
    open(txt, 'w', encoding='utf-8').write(TEXTO)
    if os.path.exists(TOMA):
        shutil.move(TOMA, TOMA.replace('.mp3', '__%s.mp3' % time.strftime('%H%M%S')))
    q = subprocess.run([sys.executable, os.path.join(H, 'voz', 'elevenlabs.py'), 'decir',
                        txt, PILAR, TOMA], capture_output=True, text=True,
                       encoding='utf-8', errors='replace',
                       env=dict(os.environ, PYTHONUTF8='1'))
    print((q.stdout + q.stderr)[-400:])
    d = stt(TOMA)
    json.dump(d, open(TOMA.replace('.mp3', '.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('toma nueva:', d['text'])
    print(palabras(d)[:6])
    # el master en ese tramo
    tramo = os.path.join(TRABAJO, 'master_d02_tramo.mp3')
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', '%.3f' % ENTRA_D02, '-t', '4.0',
                    '-i', MASTER, '-ac', '1', '-c:a', 'libmp3lame', '-b:a', '192k', tramo],
                   check=True)
    m = stt(tramo)
    json.dump(m, open(tramo.replace('.mp3', '.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('master:', m['text'])
    print(palabras(m)[:6])


def busca(ps, inicio):
    for i, (t, a, b) in enumerate(ps):
        if t.lower().startswith(inicio):
            return i
    raise SystemExit('no encuentro %r en %s' % (inicio, ps[:8]))


def voz_en(x, a, b):
    """La palabra dentro de [a, b) (muestras): el primer y el ultimo tramo de
    10 ms por encima del umbral. Entre «indigena,» y «de» solo hay pausa,
    palabra y pausa, asi que lo que suena ES la palabra. El STT da los bordes
    con +-30 ms; la energia los da al tramo."""
    m = x[a:b].mean(axis=1)
    h = int(0.010 * SR)
    n = len(m) // h
    db = 20 * np.log10(np.sqrt((m[:n * h].reshape(n, h) ** 2).mean(axis=1)) + 1e-9)
    piso, pico = np.percentile(db, 10), db.max()
    umbral = max(piso + 15, pico - 38)
    on = np.where(db > umbral)[0]
    w0 = a + on[0] * h - int(0.020 * SR)
    w1 = a + (on[-1] + 1) * h + int(0.035 * SR)
    return max(a, w0), min(b, w1), piso, pico


def injertar():
    d = json.load(open(TOMA.replace('.mp3', '.json'), encoding='utf-8'))
    m = json.load(open(os.path.join(TRABAJO, 'master_d02_tramo.json'), encoding='utf-8'))
    pn, pm = palabras(d), palabras(m)
    # en las dos: «indígena,» -> la palabra -> «de»
    i_n, i_m = busca(pn, 'ind'), busca(pm, 'ind')
    assert pn[i_n + 2][0].lower().startswith('de') and pm[i_m + 2][0].lower().startswith('de'), (pn[:6], pm[:6])
    mas = lee(MASTER)
    nue = lee(TOMA)
    S = lambda t: int(round(t * SR))
    # tramo entre «indígena,» y «de», en el master y en la toma nueva
    a_m, b_m = S(ENTRA_D02 + pm[i_m][2] + 0.02), S(ENTRA_D02 + pm[i_m + 2][1] - 0.02)
    a_n, b_n = S(pn[i_n][2] + 0.02), S(pn[i_n + 2][1] - 0.02)
    v0, v1, piso_m, pico_m = voz_en(mas, a_m, b_m)      # la palabra vieja
    n0, n1, piso_n, pico_n = voz_en(nue, a_n, b_n)      # la nueva
    pal = nue[n0:n1].copy()
    vieja = mas[v0:v1]
    g = float(np.sqrt((vieja ** 2).mean()) / max(1e-9, np.sqrt((pal ** 2).mean())))
    pal *= g
    f = int(0.012 * SR)
    rampa = np.linspace(0, 1, f, dtype=np.float32)[:, None]
    pal[:f] *= rampa
    pal[-f:] *= rampa[::-1]
    # se apaga la vieja (fundidos de 12 ms dentro de sus margenes de silencio)
    sal = mas.copy()
    env = np.zeros((v1 - v0, 1), np.float32)
    env[:f] = rampa[::-1]
    env[-f:] = rampa
    sal[v0:v1] *= env
    # la nueva, centrada donde estaba la vieja y sin salirse del tramo
    ini = (v0 + v1) // 2 - len(pal) // 2
    ini = max(a_m, min(ini, b_m - len(pal)))
    assert ini >= a_m and ini + len(pal) <= b_m, ('la palabra nueva no cabe', len(pal) / SR, (b_m - a_m) / SR)
    sal[ini:ini + len(pal)] += pal
    assert len(sal) == len(mas)
    pk = float(np.abs(sal).max())
    d_ = os.path.join(V, '_descartes')
    os.makedirs(d_, exist_ok=True)
    shutil.copy2(MASTER, os.path.join(d_, 'ED_C4_NARRADOR__taita_de_tres_silabas_%s.wav'
                                      % time.strftime('%H%M%S')))
    tmp = MASTER[:-4] + '__nuevo.wav'
    p = subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '2',
                        '-i', '-', '-c:a', 'pcm_s24le', tmp], input=sal.astype(np.float32).tobytes())
    assert p.returncode == 0
    os.replace(tmp, MASTER_V2)
    # el tramo nuevo, para oirlo y para el STT de comprobacion
    oir = os.path.join(TRABAJO, 'master_d02_tramo_nuevo.mp3')
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', '%.3f' % ENTRA_D02, '-t', '4.0',
                    '-i', MASTER_V2, '-ac', '1', '-c:a', 'libmp3lame', '-b:a', '192k', oir],
                   check=True)
    print('tramo %.3f-%.3f s | vieja %.3f-%.3f (%.3f s) | nueva %.3f s en %.3f | '
          'ganancia %+.2f dB | piso %.1f/%.1f dB | pico %.3f | muestras %d = %d'
          % (a_m / SR, b_m / SR, v0 / SR, v1 / SR, (v1 - v0) / SR, len(pal) / SR, ini / SR,
             20 * np.log10(g), piso_m, piso_n, pk, len(sal), len(lee(MASTER_V2))))
    c = stt(oir)
    print('STT del tramo nuevo:', c['text'])
    print(palabras(c)[:6])


if __name__ == '__main__':
    {'tomar': tomar, 'injertar': injertar}[sys.argv[1]]()
