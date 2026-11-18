# -*- coding: utf-8 -*-
"""Subtitulos .srt a partir de la transcripcion por palabra de Scribe hecha sobre el VIDEO FINAL (stt_final.py):
los tiempos son los del video entregado, intro incluida.

Uso:  srt_de_stt.py <manifiesto.json> <carpeta de los .json de Scribe> <carpeta de salida> [correcciones.json] [clave ...]

Por cada video escribe  <nombre>.srt  (UTF-8, el nombre del video), <nombre>.vtt  y  <clave>.rev.txt  (un subtitulo
por renglon con su tiempo, para leerlo de corrido al revisar). Imprime un resumen por video.

Criterio (el de subtitulado en castellano): dos renglones de hasta 42 caracteres, de 1,2 a 7 s por subtitulo, corte
en el final de la oracion o en una pausa, y nunca un renglon que termine en articulo, preposicion o conjuncion si se
puede evitar. Un subtitulo no mezcla dos hablantes.

correcciones.json:  {"_todos": [["expresion regular", "reemplazo"], ...], "<clave>": [[...], ...]}
Se aplican sobre las palabras ANTES de partir, y los tiempos del tramo corregido se reparten entre las palabras nuevas."""
import json
import math
import os
import re
import sys

CPL = 42            # caracteres por renglon
MAX_DUR = 7.0       # s
MIN_DUR = 1.2
PAUSA = 1.0         # un silencio asi de largo corta el subtitulo aunque no haya punto
COLA = 0.35         # lo que se queda el subtitulo despues de la ultima palabra
SEP = 0.084         # dos cuadros entre un subtitulo y el siguiente
OBJETIVO = 74       # largo que se busca al partir una oracion larga

FUNC = set('''a al ante bajo con contra de del desde durante en entre hacia hasta para por según sin sobre tras
el la los las un una unos unas lo y e o u ni que pero sino como si su sus mi mis tu tus se le les me te nos no es
más muy cada este esta estos estas ese esa esos esas aquel aquella cuando donde porque aunque mientras pues cuyo
cuya cuyos cuyas tan tanto ha han he hemos fue son está están era ser'''.split())
ABREV = set('art arts núm num no dr dra sr sra srta lic ing etc pág págs inc lit ord par vs cfr ej p. ss'.split())


def norm(t):
    return re.sub(r'[^\wáéíóúüñ]', '', t.lower())


def fin_oracion(t):
    s = t.rstrip('"»”’)]')
    if not s or s[-1] not in '.?!…':
        return False
    if s[-1] == '.':
        base = norm(s)
        if base in ABREV or (len(base) == 1 and base.isalpha()):
            return False
    return True


def texto(ws):
    return ' '.join(w['text'] for w in ws)


def renglones(t):
    """El texto en uno o dos renglones de hasta CPL, o None si no entra."""
    if len(t) <= CPL:
        return [t]
    ps = t.split(' ')
    mejor = None
    for k in range(1, len(ps)):
        a, b = ' '.join(ps[:k]), ' '.join(ps[k:])
        if len(a) > CPL or len(b) > CPL or ps[k] == '%':
            continue
        s = abs(len(a) - len(b))
        ult = ps[k - 1]
        if ult[-1] in ',;:':
            s -= 9
        elif fin_oracion(ult):
            s -= 12
        if norm(ult) in FUNC:
            s += 14
        if ps[k][0].isdigit():          # «artículo / 56»: el número va con su sustantivo
            s += 25
        if mejor is None or s < mejor[0]:
            mejor = (s, [a, b])
    return mejor[1] if mejor else None


def dur(ws):
    return ws[-1]['end'] - ws[0]['start']


def cabe(ws):
    return dur(ws) <= MAX_DUR and renglones(texto(ws)) is not None


def corte(ws, objetivo, paso):
    """Indice k (corta antes de ws[k]) mas cercano a `objetivo` caracteres, prefiriendo comas y pausas."""
    mejor = None
    acum = 0
    for k in range(1, len(ws)):
        acum += len(ws[k - 1]['text']) + 1
        ant = ws[k - 1]['text']
        s = abs(acum - objetivo) / float(paso) * 60.0
        if ant[-1] in ',;:':
            s -= 30
        elif ant[-1] in ')»”':
            s -= 8
        s -= min(1.0, max(0.0, ws[k]['start'] - ws[k - 1]['end'])) * 45
        if norm(ant) in FUNC:
            s += 40
        if ws[k]['text'] == '%':
            s += 1000
        elif ws[k]['text'][0].isdigit():
            s += 40
        resto = len(texto(ws[k:]))
        if acum < 14 or resto < 14:
            s += 35
        if mejor is None or s < mejor[0]:
            mejor = (s, k)
    return mejor[1] if mejor else None


def parte(ws):
    """Una oracion en subtitulos que caben."""
    if cabe(ws) or len(ws) == 1:
        return [ws]
    total = len(texto(ws))
    n = max(2, int(math.ceil(total / float(OBJETIVO))), int(math.ceil(dur(ws) / 6.0)))
    k = corte(ws, total / float(n), total / float(n))
    if k is None:
        return [ws]
    return parte(ws[:k]) + parte(ws[k:])


def oraciones(ws):
    out, act = [], []
    for i, w in enumerate(ws):
        act.append(w)
        sig = ws[i + 1] if i + 1 < len(ws) else None
        if sig is None or fin_oracion(w['text']) or sig['start'] - w['end'] >= PAUSA \
                or sig.get('speaker_id') != w.get('speaker_id'):
            out.append(act); act = []
    return out


def une(cs):
    """Junta un subtitulo muy corto con su vecino cuando los dos caben juntos y no hay pausa entre ellos."""
    i = 0
    while i < len(cs) - 1:
        a, b = cs[i], cs[i + 1]
        corto = len(texto(a)) < 28 or len(texto(b)) < 28 or dur(a) < MIN_DUR or dur(b) < MIN_DUR
        if corto and a[-1].get('speaker_id') == b[0].get('speaker_id') and b[0]['start'] - a[-1]['end'] <= 0.4 \
                and cabe(a + b):
            cs[i:i + 2] = [a + b]
            if i:
                i -= 1
        else:
            i += 1
    return cs


def corrige(ws, reglas):
    for pat, rep in reglas:
        ini, fin, pos = [], [], 0
        for w in ws:
            ini.append(pos); pos += len(w['text']); fin.append(pos); pos += 1
        t = texto(ws)
        for m in reversed(list(re.finditer(pat, t))):
            if m.start() == m.end():
                continue
            i = max(k for k in range(len(ws)) if ini[k] <= m.start())
            j = min(k for k in range(len(ws)) if fin[k] >= m.end())
            nuevo = (t[ini[i]:m.start()] + m.expand(rep) + t[m.end():fin[j]]).split()
            t0, t1 = ws[i]['start'], ws[j]['end']
            tot = float(sum(len(x) for x in nuevo)) or 1.0
            ns, c = [], 0
            for x in nuevo:
                ns.append(dict(ws[i], text=x, start=t0 + (t1 - t0) * c / tot, end=t0 + (t1 - t0) * (c + len(x)) / tot))
                c += len(x)
            ws[i:j + 1] = ns
    return ws


MULETILLAS = set('eh ehm em mmm mm hmm'.split())


def _mayus(w):
    t = w['text']
    for i, c in enumerate(t):
        if c.isalpha():
            return dict(w, text=t[:i] + c.upper() + t[i + 1:])
    return w


def tropiezos(ws):
    """Transcripcion limpia: fuera las muletillas sueltas y los arranques en falso que Scribe marca con «--».
    «de las af-- de las personas» -> «de las personas»;  «deben repe-- respetarse» -> «deben respetarse».
    Un corte que no se retoma («la convicci-- ah, voy a volver a empezar») se deja, con puntos suspensivos."""
    out = []
    i = 0
    sube = False                                   # la palabra que sigue hereda la mayuscula de lo que se quito
    while i < len(ws):
        w = ws[i]
        t = w['text']
        n = norm(t)
        ini = bool(t) and t[0].isupper() and (not out or fin_oracion(out[-1]['text']))
        if n in MULETILLAS:
            sube = sube or ini
            i += 1
            continue
        cortada = len(n) > 0 and (t.endswith('--') or (t.endswith('-') and not t.endswith('--') and len(n) > 1))
        if cortada:
            quitado = False
            for k in (4, 3, 2, 1):                 # se repite lo de antes: «de las af-- de las …»
                if len(out) >= k and i + k < len(ws) and \
                        [norm(x['text']) for x in out[-k:]] == [norm(x['text']) for x in ws[i + 1:i + 1 + k]]:
                    sube = sube or (out[-k]['text'][:1].isupper() and (len(out) == k or fin_oracion(out[-k - 1]['text'])))
                    del out[-k:]
                    quitado = True
                    break
            if not quitado and i + 1 < len(ws):
                sig = norm(ws[i + 1]['text'])
                if sig[:2] == n[:2] or sig.startswith(n) or n.startswith(sig):
                    sube = sube or ini
                    quitado = True
            if quitado:
                i += 1
                continue
            w = dict(w, text=t.rstrip('-') + '…')
        if sube:
            w = _mayus(w)
            sube = False
        out.append(w)
        i += 1
    return out


def limpia(ws):
    """Arreglos de tipografia que valen siempre: un signo suelto se pega a la palabra anterior, y una pregunta que
    sigue a dos puntos empieza con mayuscula (las preguntas de los casos son una lista)."""
    out = []
    for w in tropiezos(ws):
        if out and not re.search(r'[\wáéíóúüñ%]', w['text']):
            out[-1] = dict(out[-1], text=out[-1]['text'] + w['text'], end=w['end'])
            continue
        if out and out[-1]['text'].endswith(':') and w['text'].startswith('¿') and len(w['text']) > 1:
            w = dict(w, text='¿' + w['text'][1].upper() + w['text'][2:])
        out.append(w)
    return out


def cues(j, reglas=()):
    ws = [dict(text=w['text'].strip(), start=float(w['start']), end=float(w['end']), speaker_id=w.get('speaker_id'))
          for w in j.get('words', []) if w.get('type') == 'word' and w.get('text', '').strip()]
    ws = limpia(corrige(ws, reglas))
    cs = []
    for o in oraciones(ws):
        cs += parte(o)
    cs = une(cs)
    out = []
    for i, c in enumerate(cs):
        sig = cs[i + 1][0]['start'] if i + 1 < len(cs) else None
        a = c[0]['start']
        b = c[-1]['end'] + COLA
        if b - a < MIN_DUR:
            b = a + MIN_DUR
        if sig is not None:
            b = min(b, sig - SEP)
        b = max(b, a + 0.3)
        out.append((a, b, renglones(texto(c)) or [texto(c)]))
    return out


def marca(t, sep):
    ms = int(round(t * 1000))
    return '%02d:%02d:%02d%s%03d' % (ms // 3600000, ms // 60000 % 60, ms // 1000 % 60, sep, ms % 1000)


def srt(cs):
    return ''.join('%d\r\n%s --> %s\r\n%s\r\n\r\n' % (i + 1, marca(a, ','), marca(b, ','), '\r\n'.join(r))
                   for i, (a, b, r) in enumerate(cs))


def vtt(cs):
    return 'WEBVTT\n\n' + ''.join('%d\n%s --> %s\n%s\n\n' % (i + 1, marca(a, '.'), marca(b, '.'), '\n'.join(r))
                                 for i, (a, b, r) in enumerate(cs))


def main():
    man = json.load(open(sys.argv[1], encoding='utf-8'))
    S, O = sys.argv[2].rstrip('/') + '/', sys.argv[3].rstrip('/') + '/'
    resto = sys.argv[4:]
    corr = {}
    if resto and resto[0].endswith('.json'):
        corr = json.load(open(resto.pop(0), encoding='utf-8'))
    os.makedirs(O, exist_ok=True)
    for m in man:
        k = m['clave']
        if resto and k not in resto:
            continue
        if not os.path.exists(S + k + '.json'):
            print(k, 'SIN TRANSCRIPCION'); continue
        j = json.load(open(S + k + '.json', encoding='utf-8'))
        cs = cues(j, list(corr.get('_todos', [])) + list(corr.get(k, [])))
        open(O + m['nombre'] + '.srt', 'w', encoding='utf-8', newline='').write(srt(cs))
        open(O + m['nombre'] + '.vtt', 'w', encoding='utf-8', newline='').write(vtt(cs))
        open(O + k + '.rev.txt', 'w', encoding='utf-8').write(
            ''.join('%d:%04.1f  %s\n' % (int(a // 60), a % 60, ' / '.join(r)) for a, b, r in cs))
        largos = [len(x) for _a, _b, r in cs for x in r]
        cps = [sum(len(x) for x in r) / (b - a) for a, b, r in cs]
        print('%-6s %4d subtitulos | %s a %s | renglon mas largo %d | de mas de 2 renglones %d | cortos (<1 s) %d | '
              'mas de 20 car/s %d | %s'
              % (k, len(cs), marca(cs[0][0], ',')[3:8], marca(cs[-1][1], ',')[3:8], max(largos),
                 sum(1 for _a, _b, r in cs if len(r) > 2 or max(len(x) for x in r) > CPL),
                 sum(1 for a, b, _r in cs if b - a < 1.0), sum(1 for x in cps if x > 20), m['nombre']))


if __name__ == '__main__':
    main()
