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


def fin_oracion(t, sig=None):
    """`sig` es la palabra que sigue, si se conoce: «no.» es abreviatura de número solo cuando sigue una cifra
    («y cuándo no. Se trata de…» termina la oración; «el oficio No. 12» no)."""
    s = t.rstrip('"»”’)]')
    if not s or s[-1] not in '.?!…':
        return False
    if s[-1] == '.':
        base = norm(s)
        if base == 'no' and sig is not None and not sig[:1].isdigit():
            return True
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
        elif fin_oracion(ult, ps[k]):
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
        if sig is None or fin_oracion(w['text'], sig['text']) or sig['start'] - w['end'] >= PAUSA \
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


_U = dict(un=1, uno=1, una=1, dos=2, tres=3, cuatro=4, cinco=5, seis=6, siete=7, ocho=8, nueve=9)
_D = dict(diez=10, once=11, doce=12, trece=13, catorce=14, quince=15, dieciseis=16, diecisiete=17, dieciocho=18,
          diecinueve=19, veinte=20, veintiun=21, veintiuno=21, veintiuna=21, veintidos=22, veintitres=23,
          veinticuatro=24, veinticinco=25, veintiseis=26, veintisiete=27, veintiocho=28, veintinueve=29)
_T = dict(treinta=30, cuarenta=40, cincuenta=50, sesenta=60, setenta=70, ochenta=80, noventa=90)
_C = dict(cien=100, ciento=100, doscientos=200, trescientos=300, cuatrocientos=400, quinientos=500, seiscientos=600,
          setecientos=700, ochocientos=800, novecientos=900)
_C.update({k[:-2] + 'as': v for k, v in list(_C.items()) if k.endswith('os')})
_SIN = str.maketrans('áéíóúü', 'aeiouu')


def numeros(ws):
    """Los números de 11 en adelante que Scribe dejó en letras pasan a cifras («artículo ciento ochenta y siete» ->
    «artículo 187», «Ley mil noventa y ocho de dos mil seis» -> «Ley 1098 de 2006»), y «N por ciento» a «N %».
    Un «cien», «ciento» o «mil» suelto se deja. La serie se corta en cualquier signo de puntuación."""
    n = [norm(w['text']).translate(_SIN) for w in ws]

    def abierto(j):                                 # la palabra j no termina en signo: puede seguir la cifra
        return re.search(r'[\wáéíóúüñ]$', ws[j]['text']) is not None

    def grupo(i):                                   # 1 a 999 -> (valor, siguiente) o None
        v, j = 0, i
        if j < len(n) and n[j] in _C:
            v, j = _C[n[j]], j + 1
            if n[j - 1] == 'cien' or not abierto(j - 1):
                return v, j
        if j < len(n) and n[j] in _T:
            v, j = v + _T[n[j]], j + 1
            if abierto(j - 1) and j + 1 < len(n) and n[j] == 'y' and n[j + 1] in _U and ws[j]['text'] == 'y':
                v, j = v + _U[n[j + 1]], j + 2
        elif j < len(n) and n[j] in _D:
            v, j = v + _D[n[j]], j + 1
        elif j < len(n) and n[j] in _U:
            v, j = v + _U[n[j]], j + 1
        return (v, j) if j > i else None

    out, i = [], 0
    while i < len(ws):
        g, v, j = grupo(i), None, i
        if n[i] == 'mil':
            v, j = 1000, i + 1
        elif g and g[1] < len(n) and n[g[1]] == 'mil' and abierto(g[1] - 1) and g[0] > 1:
            v, j = g[0] * 1000, g[1] + 1
        if v is not None:
            r = grupo(j) if abierto(j - 1) else None
            if r:
                v, j = v + r[0], r[1]
        elif g:
            v, j = g
        suelto = j == i + 1 and n[i] in ('cien', 'ciento', 'mil')
        pct = v is not None and not suelto and j + 1 < len(n) and abierto(j - 1) and n[j] == 'por' and n[j + 1] == 'ciento'
        if v is None or suelto or (v < 11 and not pct) or not ws[i]['text'][:1].isalpha() and not ws[i]['text'][:1] in '¿¡("«':
            out.append(ws[i]); i += 1
            continue
        if pct:
            j += 2
        pre = re.match(r'[^\wáéíóúüñ]*', ws[i]['text']).group(0)
        pos = re.search(r'[^\wáéíóúüñ]*$', ws[j - 1]['text']).group(0)
        out.append(dict(ws[i], text=pre + str(v) + (' %' if pct else '') + pos, end=ws[j - 1]['end']))
        i = j
    return out


MULETILLAS = set('eh ehm em mmm mm hmm'.split())
_MARCADORES = set('así bueno entonces ahora además asimismo finalmente también luego pues bien igualmente adicionalmente '
                  'efecto ejemplo embargo parte lado lugar caso decir sí no tanto contrario'.split())
# palabras que no llevan coma detras: si la traen es porque seguia una muletilla
_SIN_COMA = set('a al ante con de del desde en entre hacia hasta para por sin sobre el la los las un una unos unas su sus '
                'mi mis que cualquier algún alguna ningún ninguna otro otra cada muy tan este esta estos estas ese esa'.split())


def _mayus(w):
    t = w['text']
    for i, c in enumerate(t):
        if c.isalpha():
            return dict(w, text=t[:i] + c.upper() + t[i + 1:])
    return w


_PREF = set('ex pre pos co sub no pro bi tri'.split())
_PREP = {'de': ('de', 'del'), 'a': ('a', 'al'), 'en': ('en',), 'por': ('por',), 'con': ('con',), 'para': ('para',)}


def _tartamudeo(t):
    """«compe-complejidad» -> «complejidad», «co-de» -> «de», «Ten-entendemos» -> «Entendemos». Los compuestos
    («infancia-adolescencia», «jurídico-penales», «T-142») quedan."""
    m = re.match(r'^([^\wáéíóúüñ]*)([^\W\d_]+)-([^\W\d_].*)$', t)
    if not m or re.search(r'\d', t) or m.group(2).isupper():
        return t
    pre, x, y = m.groups()
    nx, ny = norm(x).translate(_SIN), norm(re.split(r'[-\s]', y)[0]).translate(_SIN)
    com = 0
    while com < min(len(nx), len(ny)) and nx[com] == ny[com]:
        com += 1
    if ny.startswith(nx) or (com >= 2 and (len(nx) <= 4 or com >= max(3, len(nx) - 3))) \
            or (len(nx) <= 3 and nx not in _PREF) or (nx in _PREF and ny in FUNC):
        return _tartamudeo(pre + (y[0].upper() + y[1:] if x[0].isupper() else y))
    return t


def tropiezos(ws):
    """Transcripcion limpia: fuera las muletillas sueltas y los arranques en falso que Scribe marca con «--».
    «de las af-- de las personas» -> «de las personas»;  «deben repe-- respetarse» -> «deben respetarse».
    Un corte que no se retoma («la convicci-- ah, voy a volver a empezar») se deja, con puntos suspensivos."""
    out = []
    i = 0
    sube = False                                   # la palabra que sigue hereda la mayuscula de lo que se quito
    while i < len(ws):
        w = ws[i]
        if '-' in w['text'].strip('-'):
            w = dict(w, text=_tartamudeo(w['text']))
        t = w['text']
        n = norm(t)
        ini = bool(t) and t[0].isupper() and (not out or fin_oracion(out[-1]['text']))
        if n in MULETILLAS:
            sube = sube or ini
            if out and out[-1]['text'].endswith(',') and (norm(out[-1]['text']) in _SIN_COMA or
                                                          (t.endswith(',') and norm(out[-1]['text']) not in _MARCADORES
                                                           and not (len(out) > 1 and out[-2]['text'].endswith(',')))):
                # «cualquier, eh, necesidad» -> «cualquier necesidad»; «el impacto, eh, de ese proceso» -> «el impacto de ese
                # proceso»: las dos comas encerraban la muletilla. Tras un marcador («Así, eh, por ejemplo») o en una lista la coma queda
                out[-1] = dict(out[-1], text=out[-1]['text'][:-1])
            i += 1
            continue
        cortada = len(n) > 0 and (t.endswith('--') or (t.endswith('-') and not t.endswith('--') and len(n) > 1))
        if cortada:
            quitado = False
            resto = [x for x in ws[i + 1:i + 10] if norm(x['text']) not in MULETILLAS]   # lo que sigue, sin muletillas
            for k in (4, 3, 2, 1):                 # se repite lo de antes: «de las af-- de las …»
                if len(out) >= k and len(resto) >= k and \
                        [norm(x['text']) for x in out[-k:]] == [norm(x['text']) for x in resto[:k]]:
                    sube = sube or (out[-k]['text'][:1].isupper() and (len(out) == k or fin_oracion(out[-k - 1]['text'])))
                    del out[-k:]
                    quitado = True
                    break
            if not quitado and resto:
                sig = norm(resto[0]['text'])
                if sig[:2] == n[:2] or sig.startswith(n) or n.startswith(sig):
                    sube = sube or ini
                    quitado = True
                elif (n in FUNC or len(n) == 1) and not resto[0]['text'][:1].isupper():
                    # un articulo o un pedacito suelto y la oracion sigue: «También la-- el artículo» -> «También el artículo»
                    sube = sube or ini
                    quitado = True
                    if n == 'del' and sig in ('la', 'las', 'los'):          # «antes del-- la entrada» -> «antes de la entrada»
                        out.append(dict(w, text=t[:t.lower().find('del')] + ('De' if t.lstrip('¿¡("«')[:1].isupper() else 'de')))
                        sube = False
                    elif out and re.search(r'[\wáéíóúüñ]$', out[-1]['text']) and sig in _PREP.get(norm(out[-1]['text']), ()):
                        sube = sube or (out[-1]['text'][:1].isupper() and (len(out) == 1 or fin_oracion(out[-2]['text'])))
                        del out[-1]                # «se tomará de la-- del principio» -> «se tomará del principio»
            if quitado:
                i += 1
                continue
            w = dict(w, text=t.rstrip('-') + '…')
        if out and n in FUNC and norm(out[-1]['text']) == n and re.search(r'[\wáéíóúüñ]$' if n == 'no' else r'[\wáéíóúüñ],?$', out[-1]['text']):
            # «a, a la comunidad», «de de justicia»: se queda la segunda (y la mayuscula de la primera)
            if out[-1]['text'][:1].isupper() and (len(out) == 1 or fin_oracion(out[-2]['text'])):
                sube = True
            del out[-1]
        if out and t in ('el', 'el,', 'el.') and out[-1]['text'] in ('de', 'a'):       # «de el sistema» -> «del sistema»
            out[-1] = dict(out[-1], text={'de': 'del', 'a': 'al'}[out[-1]['text']] + t[2:], end=w['end'])
            i += 1
            continue
        if sube:
            w = _mayus(w)
            sube = False
        out.append(w)
        if len(out) >= 4 and all(norm(x['text']) in FUNC for x in out[-4:]) and \
                [norm(x['text']) for x in out[-4:-2]] == [norm(x['text']) for x in out[-2:]] and \
                re.search(r'[\wáéíóúüñ]$', out[-4]['text']) and re.search(r'[\wáéíóúüñ],?$', out[-3]['text']):
            del out[-4:-2]                         # «de la, de la libertad» -> «de la libertad»
        i += 1
    return out


def limpia(ws):
    """Arreglos de tipografia que valen siempre: un signo suelto se pega a la palabra anterior, y una pregunta que
    sigue a dos puntos empieza con mayuscula (las preguntas de los casos son una lista)."""
    out = []
    for w in tropiezos(ws):
        if out and not re.search(r'[\wáéíóúüñ%]', w['text']):
            # Scribe a veces pone el punto varios segundos despues de la palabra: el subtitulo no se estira hasta ahi
            out[-1] = dict(out[-1], text=out[-1]['text'] + w['text'],
                           end=w['end'] if w['end'] - out[-1]['end'] <= 2.0 else out[-1]['end'])
            continue
        if out and out[-1]['text'].endswith(':') and w['text'].startswith('¿') and len(w['text']) > 1:
            w = dict(w, text='¿' + w['text'][1].upper() + w['text'][2:])
        out.append(w)
    return out


def cues(j, reglas=(), despues=()):
    ws = [dict(text=w['text'].strip(), start=float(w['start']), end=float(w['end']), speaker_id=w.get('speaker_id'))
          for w in j.get('words', []) if w.get('type') == 'word' and w.get('text', '').strip()]
    for w in ws:
        if w['end'] - w['start'] > 3.0:            # Scribe a veces estira una palabra sobre el silencio de antes (medido: la
            w['start'] = w['end'] - 1.0            # primera palabra de un video, 17 s): vale su final
    ws = limpia(corrige(numeros(corrige(ws, reglas)), despues))       # `despues`: reglas sobre el texto ya con cifras
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
        cs = cues(j, list(corr.get('_todos', [])) + list(corr.get(k, [])), list(corr.get('_despues', [])))
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
