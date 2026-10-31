# -*- coding: utf-8 -*-
r"""Vuelve a pedir UNA toma de Justicia restaurativa y la mete EN SU SITIO en
el master, sin mover nada de lo demas (31 oct, Sebastian: «Jairo Ortiz ...
Cuéllar» con una pausa de un segundo y el acento en la a).

    python retomar_jr.py C2 n10_perfil_procesados candidatos
        pide N variantes (--n 4) y las oye con Scribe: duracion, la pausa
        mas larga entre dos palabras de un mismo nombre (--par Ortiz Cuéllar)
        y una medida de acento sobre --palabra (F0 y energia de la primera
        mitad contra la segunda: en «Cué-llar» la primera tiene que ganar).
        --variante "Cuéllar=Cuéyar" cambia esa grafia en la mitad de los
        candidatos (la ll a la española es lo que el modelo lee raro).
    python retomar_jr.py C2 n10_perfil_procesados poner <k>
        toma el candidato k: la toma vieja (mp3 y stt) va a _descartes, la
        nueva toma su nombre; el master se reescribe con la toma nueva en la
        MISMA ventana (nivelada al mismo short-term de la toma vieja en el
        master y rellenada con silencio al final; si no cabe, para); el
        stt del bloque se rehace; rejilla y ranuras NO cambian (las ventanas
        son las mismas). Despues toca rehacer los cartones del tema
        (`cartones_jr.py C2 --quemar`): entran por palabra.

Ventana = tramo del bloque en JR_<T>_rejilla.json (entra, sale). Se corta
el master en esos dos puntos y se pega: [antes] + [toma nueva nivelada +
silencio] + [despues]. El largo total queda identico al cuadro.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import time

H = r'D:\DAE\_repo\herramientas'
sys.path.insert(0, os.path.join(H, 'voz'))
sys.path.insert(0, os.path.join(H, 'voz', 'textos'))

import numpy as np                                        # noqa: E402

from guion_jr import bloques                              # noqa: E402
import rutas_jr as R                                      # noqa: E402
import armar_jr as A                                      # noqa: E402
import lanzar_voz_jr as LV                                # noqa: E402
import stt_jr as ST                                       # noqa: E402

FF = A.FF
SR = A.SR


def w(*a):
    print(*a, flush=True)


def bloque_de(clave, nom):
    for i, b in enumerate(bloques(clave), 1):
        if b[0] == nom:
            return i, b
    raise SystemExit('no hay bloque %s en %s' % (nom, clave))


def carpeta_cand(clave, nom):
    d = os.path.join(R.voces(clave), 'crudo', '_retomas', nom)
    os.makedirs(d, exist_ok=True)
    return d


def pcm(ruta, t0=None, t1=None):
    cmd = [FF, '-v', 'error']
    if t0 is not None:
        cmd += ['-ss', '%.4f' % t0]
    if t1 is not None:
        cmd += ['-to', '%.4f' % t1]
    cmd += ['-i', ruta, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-']
    b = subprocess.run(cmd, capture_output=True).stdout
    return np.frombuffer(b, np.float32)


def f0_rms(x):
    """F0 por autocorrelacion y RMS de un trozo de voz (mono, SR)."""
    if len(x) < SR // 20:
        return None, float(np.sqrt(np.mean(x ** 2)) + 1e-9)
    x = x - x.mean()
    ac = np.correlate(x, x, 'full')[len(x) - 1:]
    lo, hi = SR // 400, SR // 70            # 70..400 Hz
    if hi >= len(ac):
        return None, float(np.sqrt(np.mean(x ** 2)) + 1e-9)
    k = lo + int(np.argmax(ac[lo:hi]))
    return SR / float(k), float(np.sqrt(np.mean(x ** 2)) + 1e-9)


def acento(mp3, j, palabra):
    """(F0_1a, F0_2a, rms_1a_dB, rms_2a_dB) de la palabra: primera mitad contra
    la segunda. Para un esdrujulo/llano con tilde en la primera silaba, la
    primera mitad tiene que ir mas alta y mas fuerte."""
    ws = [x for x in j.get('words', []) if x.get('type', 'word') == 'word']
    cand = [x for x in ws if ST.norm(x['text']) == ST.norm(palabra)]
    if not cand:
        return None
    x = cand[0]
    a = pcm(mp3, x['start'], x['end'])
    if len(a) < SR // 10:
        return None
    m = len(a) // 2
    f1, r1 = f0_rms(a[:m])
    f2, r2 = f0_rms(a[m:])
    return (f1, f2, 20 * np.log10(r1), 20 * np.log10(r2))


def pausa_par(j, a, b):
    ws = [x for x in j.get('words', []) if x.get('type', 'word') == 'word']
    na, nb = ST.norm(a), ST.norm(b)
    for k in range(len(ws) - 1):
        if ST.norm(ws[k]['text']) == na and ST.norm(ws[k + 1]['text']) == nb:
            return ws[k + 1]['start'] - ws[k]['end']
    return None


def candidatos(clave, nom, n, variante, par, palabra):
    i, (_, voz, _texto, tts, _p) = bloque_de(clave, nom)
    d = carpeta_cand(clave, nom)
    rej = json.load(open(os.path.join(R.voces(clave), 'JR_%s_rejilla.json' % clave),
                         encoding='utf-8'))
    tr = {t['bloque']: t for t in rej['tramos']}[nom]
    ventana = tr['sale'] - tr['entra']
    w('ventana del bloque en el master: %.2f s (entra %.2f)' % (ventana, tr['entra']))
    env = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONUTF8='1')
    textos = []
    for k in range(n):
        t = tts
        if variante and k % 2 == 1:
            a, b = variante.split('=')
            t = t.replace(a, b)
        textos.append(t)
    for k, t in enumerate(textos):
        mp3 = os.path.join(d, '%s_%d.mp3' % (nom, k))
        if os.path.exists(mp3):
            continue
        tx = os.path.join(d, '%s_%d.txt' % (nom, k))
        open(tx, 'w', encoding='utf-8', newline='\n').write(t)
        q = subprocess.run([sys.executable, LV.ELEVEN, 'decir', tx, LV.VOZ[voz], mp3],
                           capture_output=True, text=True, encoding='utf-8',
                           errors='replace', env=env)
        w('   %d %s' % (k, (q.stdout or q.stderr).strip()[-120:]))
    # la toma vieja, como referencia
    viejo = os.path.join(R.voces(clave), 'crudo', LV.nombre(clave, i, nom) + '.mp3')
    filas = [('vieja', viejo, os.path.join(R.voces(clave), 'stt',
                                            LV.nombre(clave, i, nom) + '.json'))]
    for k in range(n):
        mp3 = os.path.join(d, '%s_%d.mp3' % (nom, k))
        js = mp3[:-4] + '.json'
        if not os.path.exists(js):
            json.dump(ST.stt(mp3), open(js, 'w', encoding='utf-8'), ensure_ascii=False)
        filas.append((str(k), mp3, js))
    w('%-6s %6s %6s  %-8s  %s' % ('toma', 'dur', 'cabe', 'pausa', 'acento (F0 1a/2a, dB 1a/2a)'))
    for et, mp3, js in filas:
        j = json.load(open(js, encoding='utf-8'))
        dur = A.duracion(mp3)
        pa = pausa_par(j, par[0], par[1]) if par else None
        ac = acento(mp3, j, palabra) if palabra else None
        oido = ' '.join(ST.norm(j.get('text', '')))
        pedido = ' '.join(ST.norm(tts))
        w('%-6s %6.2f %6s  %-8s  %s  %s' % (
            et, dur, 'si' if dur <= ventana else 'NO',
            ('%.2f' % pa) if pa is not None else '-',
            ('%s/%s Hz  %.1f/%.1f dB' % (
                ('%.0f' % ac[0]) if ac[0] else '-', ('%.0f' % ac[1]) if ac[1] else '-',
                ac[2], ac[3])) if ac else '-',
            'OK' if oido == pedido else 'DIF: ' + j.get('text', '')[:80]))


def repartir(mp3, js, ventana, tope=0.4, minimo=0.45, cola=0.8):
    """La toma nueva suele ser mas corta que la ventana (31 oct: 16,5 s en
    20,6). Si todo el sobrante fuera al final quedarian cinco segundos de
    silencio antes del bloque siguiente. Se reparte: hasta `tope` s mas en
    cada pausa interna de `minimo` s o mas (las de coma y dos puntos), y
    lo que quede al final. Devuelve (wav con las pausas estiradas, stt
    con los tiempos corridos)."""
    import wave
    j = json.load(open(js, encoding='utf-8'))
    ws = [x for x in j['words'] if x.get('type', 'word') == 'word']
    dur = A.duracion(mp3)
    sobra = ventana - dur - cola
    gaps = [(ws[k]['end'], ws[k + 1]['start']) for k in range(len(ws) - 1)
            if ws[k + 1]['start'] - ws[k]['end'] >= minimo]
    extra = min(tope, sobra / len(gaps)) if gaps and sobra > 0 else 0.0
    x = pcm(mp3)
    partes, corr, prev = [], 0.0, 0
    corrido = []
    for a, b in gaps:
        m = int(((a + b) / 2.0) * SR)
        partes.append(x[prev:m])
        partes.append(np.zeros(int(extra * SR), np.float32))
        prev = m
        corrido.append(((a + b) / 2.0, extra))
    partes.append(x[prev:])
    y = np.concatenate(partes)
    for w_ in j['words']:
        d = sum(e for t, e in corrido if w_.get('start', 0) >= t)
        for key in ('start', 'end'):
            if key in w_:
                w_[key] = round(w_[key] + d, 3)
    sal = mp3[:-4] + '_repartida.wav'
    with wave.open(sal, 'wb') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(SR)
        f.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes())
    sj = sal[:-4] + '.json'
    json.dump(j, open(sj, 'w', encoding='utf-8'), ensure_ascii=False)
    w('repartido: %d pausas de %.2f s o mas, +%.2f s cada una; toma %.2f -> %.2f s en ventana de %.2f'
      % (len(gaps), minimo, extra, dur, len(y) / float(SR), ventana))
    return sal, sj


def poner(clave, nom, k, reparte=True):
    i, (_, voz, _texto, tts, _p) = bloque_de(clave, nom)
    d = carpeta_cand(clave, nom)
    nuevo = os.path.join(d, '%s_%s.mp3' % (nom, k))
    assert os.path.exists(nuevo), nuevo
    nuevo_js = nuevo[:-4] + '.json'
    voces = R.voces(clave)
    master = os.path.join(voces, 'JR_%s_NARRADOR.wav' % clave)
    rej_p = os.path.join(voces, 'JR_%s_rejilla.json' % clave)
    rej = json.load(open(rej_p, encoding='utf-8'))
    tr = {t['bloque']: t for t in rej['tramos']}[nom]
    t0, t1 = tr['entra'], tr['sale']
    ventana = t1 - t0
    if reparte:
        nuevo, nuevo_js = repartir(nuevo, nuevo_js, ventana)
    dur = A.duracion(nuevo)
    assert dur <= ventana + 0.02, 'la toma nueva (%.2f s) no cabe en la ventana (%.2f s)' % (dur, ventana)
    # nivel: el short-term de la toma vieja EN EL MASTER contra el de la nueva
    objetivo = tr.get('habla_master')
    s_nuevo, m_nuevo = A.habla(nuevo)
    nivel_nuevo = s_nuevo if s_nuevo is not None else (m_nuevo + rej.get('corrimiento_s_m', 0))
    g = (objetivo - nivel_nuevo) if objetivo is not None else 0.0
    sello = time.strftime('%H%M%S')
    desc = os.path.join(voces, '_descartes')
    os.makedirs(desc, exist_ok=True)
    tmp = master + '.retoma.wav'
    # [antes] + [nueva nivelada + silencio hasta la ventana] + [despues]
    fc = ('[0:a]atrim=0:%.6f,asetpts=PTS-STARTPTS[a];'
          '[1:a]aresample=%d,aformat=sample_fmts=fltp:channel_layouts=stereo,'
          'volume=%.4fdB,alimiter=limit=%.4f:attack=5:release=50:level=disabled,'
          'apad=whole_dur=%.6f,atrim=0:%.6f,asetpts=PTS-STARTPTS[b];'
          '[0:a]atrim=%.6f,asetpts=PTS-STARTPTS[c];'
          '[a][b][c]concat=n=3:v=0:a=1[out]'
          % (t0, SR, g, 10 ** (A.LIMITE / 20.0), ventana, ventana, t1))
    q = subprocess.run([FF, '-y', '-v', 'error', '-i', master, '-i', nuevo,
                        '-filter_complex', fc, '-map', '[out]', '-c:a', 'pcm_s24le',
                        '-ar', str(SR), '-ac', '2', tmp],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    if q.returncode:
        raise SystemExit('ffmpeg: ' + (q.stderr or '')[-1200:])
    d_antes, d_despues = A.duracion(master), A.duracion(tmp)
    assert abs(d_antes - d_despues) < 0.002, (d_antes, d_despues)
    shutil.move(master, os.path.join(desc, 'JR_%s_NARRADOR__antes_de_retomar_%s_%s.wav'
                                     % (clave, nom, sello)))
    os.replace(tmp, master)
    # la toma cruda y su stt: la vieja a _descartes, la nueva con su nombre
    nm = LV.nombre(clave, i, nom)
    viejo = os.path.join(voces, 'crudo', nm + '.mp3')
    dc = os.path.join(voces, 'crudo', '_descartes')
    os.makedirs(dc, exist_ok=True)
    if os.path.exists(viejo):
        shutil.move(viejo, os.path.join(dc, nm + '__toma_%s.mp3' % sello))
    # la toma cruda con su nombre: mp3 si es la original, wav->mp3 si se
    # repartio (stt_jr compara mtimes: el json nuevo queda mas nuevo)
    if nuevo.endswith('.wav'):
        subprocess.run([FF, '-y', '-v', 'error', '-i', nuevo, '-c:a', 'libmp3lame',
                        '-b:a', '192k', viejo], check=True)
    else:
        shutil.copyfile(nuevo, viejo)
    js = os.path.join(voces, 'stt', nm + '.json')
    if os.path.exists(js):
        shutil.move(js, os.path.join(desc, nm + '__stt_%s.json' % sello))
    shutil.copyfile(nuevo_js, js)
    os.utime(js, None)
    # medida de la ventana en el master nuevo
    s = subprocess.run([FF, '-nostats', '-ss', '%.3f' % t0, '-t', '%.3f' % ventana,
                        '-i', master, '-af', 'ebur128=framelog=info', '-f', 'null', '-'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace').stderr
    st = [float(x) for x in re.findall(r'\bS:\s*(-?\d+\.\d+)', s)]
    st = [x for x in st if x > -70]
    hecho = A._mediana([x for x in st if x >= max(st) - 20]) if st else None
    tr['habla_master_antes_de_retomar'] = objetivo
    tr['habla_master'] = round(hecho, 2) if hecho is not None else objetivo
    tr['dur_toma'] = round(dur, 3)
    tr['retomada'] = sello
    json.dump(rej, open(rej_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    lufs, pico = A.medir(master)
    w('%s %s: toma %.2f s en ventana de %.2f s, ganancia %+.2f dB, short-term %s -> %s; '
      'master %.1f LUFS pico %.1f dBFS, largo %.3f s (igual)'
      % (clave, nom, dur, ventana, g, objetivo, tr['habla_master'], lufs, pico, d_despues))


if __name__ == '__main__':
    clave, nom, paso = sys.argv[1].upper(), sys.argv[2], sys.argv[3]
    args = sys.argv[4:]

    def opt(k, default=None):
        return args[args.index(k) + 1] if k in args else default
    if paso == 'candidatos':
        par = opt('--par')
        par = (par, args[args.index('--par') + 2]) if par else None
        candidatos(clave, nom, int(opt('--n', 4)), opt('--variante'), par, opt('--palabra'))
    elif paso == 'poner':
        poner(clave, nom, args[0], reparte='--sin-repartir' not in args)
    w('LISTO')
