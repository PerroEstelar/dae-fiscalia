# -*- coding: utf-8 -*-
r"""Transcripcion con tiempos por palabra (ElevenLabs Scribe, cuenta propia)
de lo que SE OYE en cada V1 del profe Carlos Humberto, para compararlo con
«casos para talleres» y ubicar los parches. Llave en D:\DAE\_secretos (nunca
se imprime).

    python ch_transcribir.py
Entrada  D:\DAE\_tmp\ch\audio\caso0N_v1.wav (caso 1: caso01_voz.wav)
Salida   D:\DAE\_tmp\ch\stt\caso0N.json
"""
import json
import os
import urllib.request
import uuid

KEY = open(r'D:\DAE\_secretos\elevenlabs.txt', encoding='utf-8').read().strip()
A = r'D:\DAE\_tmp\ch\audio'
OUT = r'D:\DAE\_tmp\ch\stt'


def stt(path):
    b = uuid.uuid4().hex
    campos = {'model_id': 'scribe_v1', 'language_code': 'spa',
              'timestamps_granularity': 'word', 'tag_audio_events': 'false',
              'diarize': 'false'}
    body = b''
    for k, v in campos.items():
        body += ('--%s\r\nContent-Disposition: form-data; name="%s"\r\n\r\n%s\r\n'
                 % (b, k, v)).encode()
    body += ('--%s\r\nContent-Disposition: form-data; name="file"; filename="%s"\r\n'
             'Content-Type: audio/wav\r\n\r\n' % (b, os.path.basename(path))).encode()
    body += open(path, 'rb').read() + ('\r\n--%s--\r\n' % b).encode()
    req = urllib.request.Request('https://api.elevenlabs.io/v1/speech-to-text', data=body,
                                 headers={'xi-api-key': KEY,
                                          'Content-Type': 'multipart/form-data; boundary=' + b})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read().decode('utf-8'))


os.makedirs(OUT, exist_ok=True)
for n in range(1, 7):
    src = os.path.join(A, 'caso01_voz.wav' if n == 1 else 'caso%02d_v1.wav' % n)
    dst = os.path.join(OUT, 'caso%02d.json' % n)
    if os.path.exists(dst):
        continue
    try:
        j = stt(src)
        json.dump(j, open(dst, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        print(n, len(j.get('words', [])), 'palabras', flush=True)
    except Exception as e:                                     # noqa: BLE001
        print(n, 'FALLA', str(e)[:200], flush=True)
print('LISTO')
