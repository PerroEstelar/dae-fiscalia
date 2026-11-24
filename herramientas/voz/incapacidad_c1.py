# -*- coding: utf-8 -*-
r"""ED C1 (Édgar Molano): «con incapaz de resistir» pasa a «con incapacidad de resistir» (24 nov 2026).

Pedido de Sebastián (revisión de la Fiscalía): en el bloque a04 la voz dice «acceso carnal abusivo con incapaz
de resistir» y tiene que decir «con incapacidad de resistir». Es la cirugía de `taita_c4.py`, con una diferencia:
la palabra nueva es más larga (cinco sílabas contra tres), así que no se cambia solo la palabra sino la frase
entera «con incapacidad de resistir,», que en las dos tomas va entre dos pausas («abusivo ‖ con … resistir, ‖
artículo»). Así los empalmes caen en silencio y la frase conserva su entonación.

  1. toma nueva de a04 con el texto corregido (ElevenLabs, Carlos, mismo modelo y ajustes; la llave nunca se
     imprime);
  2. STT de la toma nueva y del master en el tramo del a04;
  3. en el master se apaga la frase vieja (bordes por energía, ventanas que dejan fuera las respiraciones) y entra
     la nueva, igualada en RMS de voz. Lo que la nueva tiene de más (0,3 s) sale de las pausas: entra 80 ms antes y
     la respiración que había antes de «artículo» se va (la toma nueva tampoco respira ahí); fundidos de 12 ms en
     silencio. El master mide EXACTAMENTE lo mismo: de «artículo» en adelante, y antes de «con», no cambia una
     muestra, así que la rejilla, el cartón y la línea de Sebastián no se mueven.

    python incapacidad_c1.py tomar      pide la toma y transcribe toma y master
    python incapacidad_c1.py injertar   arma ED_C1_NARRADOR_v2.wav (el master no se toca: lo tiene Resolve)

Después: `cirugia_ed.py C1 v=2 cambiar <master> <master_v2>`.
"""
import glob
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

FF = (sorted(glob.glob(r'C:\Users\call_\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg*\*\bin\ffmpeg.exe'))
      or ['ffmpeg'])[-1]
V = R.voces('C1')
MASTER = os.path.join(V, 'ED_C1_NARRADOR.wav')
MASTER_V2 = MASTER[:-4] + '_v2.wav'
TRABAJO = os.path.join(V, '_incapacidad')
TOMA = os.path.join(TRABAJO, 'ED_C1_04_a04_la_imputacion__incapacidad.mp3')
CARLOS = 'Y4HwpMNrBWN5dFKi5Lw8'
TEXTO = ('Con ese solo documento, formula la imputación por el delito de acceso carnal abusivo con incapacidad de '
         'resistir, artículo doscientos diez del Código Penal, sustentando toda la hipótesis de incapacidad para '
         'consentir en el diagnóstico médico.')
SR = 48000
ENTRA_A04 = 34.59           # rejilla: el bloque a04 entra en el master aquí
LARGO_A04 = 14.675
CORTE_IMAGEN = 991 / (24000 / 1001.0)   # ranura 991 de ED_C1_ranuras.json (s del master)
PAUSA_MIN = 0.22
ANTES = 0.08               # la frase nueva entra 80 ms antes que la vieja (es 0,3 s más larga)


def lee(p, sr=SR):
    o = subprocess.run([FF, '-v', 'error', '-i', p, '-ac', '2', '-ar', str(sr), '-f', 'f32le', '-'],
                       capture_output=True, check=True).stdout
    return np.frombuffer(o, np.float32).reshape(-1, 2).copy()


def stt(p):
    """Scribe sobre un WAV mono de 16 kHz (con mp3 a veces devuelve basura, CLAUDE.md)."""
    import stt_ed
    w = p.rsplit('.', 1)[0] + '__16k.wav'
    subprocess.run([FF, '-y', '-v', 'error', '-i', p, '-ac', '1', '-ar', '16000', '-c:a', 'pcm_s16le', w],
                   check=True)
    d = stt_ed.stt(w)
    n = len(palabras(d))
    assert n > 10, ('el STT devolvió %d palabras' % n, d.get('text'))
    return d


def palabras(d):
    return [(w['text'], w['start'], w['end']) for w in d['words'] if w['type'] == 'word']


def tramo_master(salida, fuente=MASTER):
    subprocess.run([FF, '-y', '-v', 'error', '-ss', '%.3f' % ENTRA_A04, '-t', '%.3f' % (LARGO_A04 + 0.3),
                    '-i', fuente, '-ac', '1', '-c:a', 'pcm_s16le', salida], check=True)


def tomar():
    os.makedirs(TRABAJO, exist_ok=True)
    txt = os.path.join(TRABAJO, 'a04_incapacidad.txt')
    open(txt, 'w', encoding='utf-8').write(TEXTO)
    if os.path.exists(TOMA):
        shutil.move(TOMA, TOMA.replace('.mp3', '__%s.mp3' % time.strftime('%H%M%S')))
    q = subprocess.run([sys.executable, os.path.join(H, 'voz', 'elevenlabs.py'), 'decir', txt, CARLOS, TOMA],
                       capture_output=True, text=True, encoding='utf-8', errors='replace',
                       env=dict(os.environ, PYTHONUTF8='1'))
    print((q.stdout + q.stderr)[-400:])
    d = stt(TOMA)
    json.dump(d, open(TOMA.replace('.mp3', '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('toma nueva:', d['text'])
    tramo = os.path.join(TRABAJO, 'master_a04_tramo.wav')
    tramo_master(tramo)
    m = stt(tramo)
    json.dump(m, open(tramo.replace('.wav', '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('master:', m['text'])


def busca(ps, inicio, desde=0):
    for i, (t, a, b) in enumerate(ps):
        if i >= desde and t.lower().startswith(inicio):
            return i
    raise SystemExit('no encuentro %r en %s' % (inicio, [p[0] for p in ps]))


def db_10ms(m):
    h = int(0.010 * SR)
    n = len(m) // h
    return 20 * np.log10(np.sqrt((m[:n * h].reshape(n, h) ** 2).mean(axis=1)) + 1e-9), h


def bordes(x, t0, t1, umbral):
    """Primer y último tramo de 10 ms sobre `umbral` (dB) dentro de [t0, t1) s: (inicio, fin) en s."""
    a, b = int(round(t0 * SR)), int(round(t1 * SR))
    db, h = db_10ms(x[a:b].mean(axis=1))
    on = np.where(db > umbral)[0]
    assert len(on), ('nada sobre %.0f dB en %.2f-%.2f' % (umbral, t0, t1))
    return (a + on[0] * h) / SR, (a + (on[-1] + 1) * h) / SR


def pico_db(x, t0, t1):
    db, _ = db_10ms(x[int(t0 * SR):int(t1 * SR)].mean(axis=1))
    return float(db.max())


def rms_voz(x, umbral):
    """RMS solo de los tramos de 10 ms con voz (las pausas entre palabras no cuentan)."""
    m = x.mean(axis=1)
    db, h = db_10ms(m)
    n = len(db)
    t = m[:n * h].reshape(n, h)[db > umbral]
    return float(np.sqrt((t ** 2).mean()))


def limitar(x, techo, ms=5.0):
    """Limitador con anticipación de `ms`: ninguna muestra pasa de `techo`. La ganancia baja y sube en rampas de
    `ms` alrededor de cada punta (mínimo deslizante + promedio, así que nunca queda por encima de lo necesario)."""
    from scipy.ndimage import minimum_filter1d, uniform_filter1d
    a = int(SR * ms / 1000)
    pk = np.abs(x).max(axis=1)
    g = np.minimum(1.0, techo / np.maximum(pk, 1e-9))
    g = uniform_filter1d(minimum_filter1d(g, size=2 * a + 1), size=a + 1)
    return (x * g[:, None]).astype(np.float32), float(g.min()), float((g < 0.999).sum()) / SR


def injertar():
    """Medido el 24 nov (perfil de 20 ms del master): «abusivo» termina en 39,17 s; una respiración de 39,25 a
    39,49; silencio; «con» en 39,63; «resistir,» termina en 41,01; silencio; otra respiración de 41,27 a 41,61; y
    «artículo» en 41,67. La frase nueva dura 0,3 s más y la toma nueva no respira antes de «artículo». Por eso:
    la frase nueva entra `ANTES` s antes que la vieja (sin tocar la primera respiración), y la segunda
    respiración se va: entre «resistir,» y «artículo» queda una pausa limpia."""
    d = json.load(open(TOMA.replace('.mp3', '.json'), encoding='utf-8'))
    m = json.load(open(os.path.join(TRABAJO, 'master_a04_tramo.json'), encoding='utf-8'))
    pn, pm = palabras(d), palabras(m)
    # en las dos: «abusivo» -> con -> incapa… -> de -> resistir -> «artículo»
    i_n, i_m = busca(pn, 'abusiv'), busca(pm, 'abusiv')
    assert pn[i_n + 2][0].lower().startswith('incapacidad'), [p[0] for p in pn[i_n:i_n + 6]]
    assert pm[i_m + 2][0].lower().startswith('incapaz'), [p[0] for p in pm[i_m:i_m + 6]]
    j_n, j_m = busca(pn, 'art', i_n), busca(pm, 'art', i_m)
    assert j_n == i_n + 5 and j_m == i_m + 5, ([p[0] for p in pn[i_n:j_n + 1]], [p[0] for p in pm[i_m:j_m + 1]])
    mas = lee(MASTER)
    nue = lee(TOMA)
    S = lambda t: int(round(t * SR))
    E = ENTRA_A04
    um = pico_db(mas, E, E + LARGO_A04) - 38           # umbral de voz del master
    un = pico_db(nue, 0, len(nue) / SR) - 38           # y de la toma nueva
    # la frase vieja: de «con» a «resistir,» (las ventanas dejan fuera las respiraciones)
    v_on, v_off = bordes(mas, E + pm[i_m + 1][1] - 0.06, E + pm[i_m + 4][2] + 0.10, um)
    art_on, _ = bordes(mas, v_off + 0.05, E + pm[j_m][1] + 0.10, um)
    # la nueva
    n_on, n_off = bordes(nue, pn[i_n + 1][1] - 0.06, pn[i_n + 4][2] + 0.10, un)
    n0, n1 = S(n_on - 0.020), S(n_off + 0.035)
    frase = nue[n0:n1].copy()
    g = rms_voz(mas[S(v_on):S(v_off)], um) / max(1e-9, rms_voz(frase, un))
    frase *= g
    # la toma nueva trae puntas 3,8 dB por encima del pico de todo el master (-5,0 dBFS, medido): se acotan al pico
    # del a04 viejo
    techo = float(np.abs(mas[S(E):S(E + LARGO_A04)]).max())
    frase, gmin, t_lim = limitar(frase, techo)
    print('limitador al pico del a04 viejo (%.2f dBFS): %.1f dB como mucho, %.0f ms en total'
          % (20 * np.log10(techo), -20 * np.log10(gmin), 1000 * t_lim))
    ini = S(v_on - 0.020 - ANTES)
    hueco = pico_db(mas, ini / SR, v_on)
    assert hueco < -60, ('la frase nueva pisaría la respiración: %.0f dB' % hueco)
    fin = ini + len(frase)
    fin_voz = (ini + S(n_off - n_on + 0.020)) / SR      # donde termina de sonar «resistir,»
    corte = S(art_on - 0.020)
    pausa = (S(art_on) - fin) / SR
    print('vieja «con…resistir,» %.3f-%.3f (%.3f s) · nueva %.3f s · entra %.3f · «resistir,» termina en %.3f · '
          '«artículo» en %.3f · pausa %.3f s (era %.3f con la respiración)'
          % (v_on, v_off, v_off - v_on, n_off - n_on, ini / SR, fin_voz, art_on, pausa, art_on - v_off))
    print('el corte de imagen de la ranura es en %.3f s: %.3f s después de «resistir,»'
          % (CORTE_IMAGEN, CORTE_IMAGEN - fin_voz))
    assert pausa >= PAUSA_MIN and fin_voz < CORTE_IMAGEN - 0.08, 'no cabe'
    f = int(0.012 * SR)
    rampa = np.linspace(0, 1, f, dtype=np.float32)[:, None]
    frase[:f] *= rampa
    frase[-f:] *= rampa[::-1]
    # se apaga todo entre la entrada de la nueva y «artículo» (frase vieja y segunda respiración)
    u0, u1 = ini, corte
    sal = mas.copy()
    env = np.zeros((u1 - u0, 1), np.float32)
    env[:f] = rampa[::-1]
    env[-f:] = rampa
    sal[u0:u1] *= env
    sal[ini:fin] += frase
    assert len(sal) == len(mas)
    pk = float(np.abs(sal).max())
    tmp = MASTER_V2[:-4] + '__nuevo.wav'
    p = subprocess.run([FF, '-y', '-v', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-',
                        '-c:a', 'pcm_s24le', tmp], input=sal.astype(np.float32).tobytes())
    assert p.returncode == 0
    if os.path.exists(MASTER_V2):
        d_ = os.path.join(V, '_descartes')
        os.makedirs(d_, exist_ok=True)
        shutil.move(MASTER_V2, os.path.join(d_, 'ED_C1_NARRADOR_v2__%s.wav' % time.strftime('%H%M%S')))
    os.replace(tmp, MASTER_V2)
    otro = lee(MASTER_V2)
    print('ganancia %+.2f dB · pico %.3f · muestras %d = %d'
          % (20 * np.log10(g), pk, len(mas), len(otro)))
    assert len(otro) == len(mas)
    # fuera del tramo tocado, el master nuevo es idéntico (salvo la cuantización a 24 bits)
    fuera = np.concatenate([np.abs(otro[:u0] - mas[:u0]).ravel(), np.abs(otro[u1:] - mas[u1:]).ravel()])
    print('fuera del tramo %.3f-%.3f s: diferencia máxima %.2e' % (u0 / SR, u1 / SR, fuera.max()))
    oir = os.path.join(TRABAJO, 'master_a04_tramo_nuevo.wav')
    tramo_master(oir, MASTER_V2)
    c = stt(oir)
    json.dump(c, open(oir.replace('.wav', '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('STT del a04 nuevo:', c['text'])
    for t, a, b in palabras(c)[10:20]:
        print('   %-14s %7.3f %7.3f' % (t, E + a, E + b))


if __name__ == '__main__':
    {'tomar': tomar, 'injertar': injertar}[sys.argv[1]]()
