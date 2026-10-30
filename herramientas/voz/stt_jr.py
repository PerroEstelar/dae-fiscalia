# -*- coding: utf-8 -*-
r"""Oye cada toma de Justicia restaurativa con Scribe (ElevenLabs, cuenta propia)
y la compara palabra por palabra con el `tts` que se pidio.

Por que: en el Carlos Humberto V2 una toma salio con «a, a asistir» y nadie
lo habria notado sin oirla. Aqui se marca, por bloque:
    - palabras que faltan o sobran contra el texto pedido;
    - palabras repetidas seguidas (tartamudeo);
    - los tiempos por palabra, que despues usan los cartones.

    python stt_jr.py            los tres temas
    python stt_jr.py T4         uno

Salida: <tema>/03 VOCES/stt/<toma>.json y un resumen por consola. La llave
sale de D:\DAE\_secretos\elevenlabs.txt y no se imprime.
"""
import difflib
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
from guion_jr import VIDEOS, bloques   # noqa: E402
import rutas_jr as R                # noqa: E402


def stt(path):
    """Scribe v1 con tiempos por palabra. La llave no se imprime."""
    import urllib.request
    import uuid
    key = open(r'D:\DAE\_secretos\elevenlabs.txt', encoding='utf-8').read().strip()
    b = uuid.uuid4().hex
    campos = {'model_id': 'scribe_v1', 'language_code': 'spa',
              'timestamps_granularity': 'word', 'tag_audio_events': 'false',
              'diarize': 'false'}
    body = b''
    for k, v in campos.items():
        body += ('--%s\r\nContent-Disposition: form-data; name="%s"\r\n\r\n%s\r\n'
                 % (b, k, v)).encode()
    body += ('--%s\r\nContent-Disposition: form-data; name="file"; filename="%s"\r\n'
             'Content-Type: audio/mpeg\r\n\r\n' % (b, os.path.basename(path))).encode()
    body += open(path, 'rb').read() + ('\r\n--%s--\r\n' % b).encode()
    req = urllib.request.Request('https://api.elevenlabs.io/v1/speech-to-text',
                                 data=body,
                                 headers={'xi-api-key': key,
                                          'Content-Type': 'multipart/form-data; boundary=' + b})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read().decode('utf-8'))


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.findall(r'[a-z0-9]+', s)


def revisar(clave):
    crudo = os.path.join(R.voces(clave), 'crudo')
    out = os.path.join(R.voces(clave), 'stt')
    os.makedirs(out, exist_ok=True)
    malos = []
    for i, (nom, v, _t, tts, _p) in enumerate(bloques(clave), 1):
        nm = 'JR_%s_%02d_%s' % (clave, i, nom)
        src = os.path.join(crudo, nm + '.mp3')
        dst = os.path.join(out, nm + '.json')
        if os.path.exists(dst) and os.path.getmtime(dst) > os.path.getmtime(src):
            j = json.load(open(dst, encoding='utf-8'))
        else:
            j = stt(src)
            json.dump(j, open(dst, 'w', encoding='utf-8'), ensure_ascii=False)
        oido = norm(j.get('text', ''))
        pedido = norm(tts)
        sm = difflib.SequenceMatcher(a=pedido, b=oido, autojunk=False)
        dif = [(op, ' '.join(pedido[a1:a2]), ' '.join(oido[b1:b2]))
               for op, a1, a2, b1, b2 in sm.get_opcodes() if op != 'equal']
        rep = [oido[k] for k in range(1, len(oido))
               if oido[k] == oido[k - 1] and len(oido[k]) > 1]
        ok = not dif and not rep
        print('%s %-30s %s %.3f%s%s' % (clave, nom, 'OK ' if ok else 'MIRA',
                                         sm.ratio(),
                                         ('  dif %s' % dif) if dif else '',
                                         ('  repite %s' % rep) if rep else ''),
              flush=True)
        if not ok:
            malos.append(nom)
    return malos


if __name__ == '__main__':
    claves = [x.upper() for x in sys.argv[1:]] or VIDEOS
    todo = {c: revisar(c) for c in claves}
    print('PARA MIRAR:', {k: v for k, v in todo.items() if v} or 'nada')
    print('LISTO')
