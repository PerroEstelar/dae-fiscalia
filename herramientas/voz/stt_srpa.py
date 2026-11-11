# -*- coding: utf-8 -*-
r"""Transcripción con tiempos por palabra (ElevenLabs Scribe) de los videos de
profes del curso «Sistema de responsabilidad penal para adolescentes y justicia
restaurativa». Con diarización, para saber si habla uno o más. La llave está en
D:\DAE\_secretos (nunca se imprime).

    python stt_srpa.py
Entrada  D:\DAE\_tmp\srpa\audio\<video>.mp3
Salida   D:\DAE\_tmp\srpa\stt\<video>.json
"""
import json
import os
import urllib.request
import uuid

KEY = open(r'D:\DAE\_secretos\elevenlabs.txt', encoding='utf-8').read().strip()
A = r'D:\DAE\_tmp\srpa\audio'
OUT = r'D:\DAE\_tmp\srpa\stt'


def stt(path):
    b = uuid.uuid4().hex
    campos = {'model_id': 'scribe_v1', 'language_code': 'spa',
              'timestamps_granularity': 'word', 'tag_audio_events': 'false',
              'diarize': 'true'}
    body = b''
    for k, v in campos.items():
        body += ('--%s\r\nContent-Disposition: form-data; name="%s"\r\n\r\n%s\r\n'
                 % (b, k, v)).encode()
    body += ('--%s\r\nContent-Disposition: form-data; name="file"; filename="audio.mp3"\r\n'
             'Content-Type: audio/mpeg\r\n\r\n' % b).encode()
    body += open(path, 'rb').read() + ('\r\n--%s--\r\n' % b).encode()
    req = urllib.request.Request('https://api.elevenlabs.io/v1/speech-to-text', data=body,
                                 headers={'xi-api-key': KEY,
                                          'Content-Type': 'multipart/form-data; boundary=' + b})
    with urllib.request.urlopen(req, timeout=900) as r:
        return json.loads(r.read().decode('utf-8'))


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for f in sorted(os.listdir(A)):
        dst = os.path.join(OUT, os.path.splitext(f)[0] + '.json')
        if os.path.exists(dst):
            continue
        try:
            j = stt(os.path.join(A, f))
            json.dump(j, open(dst, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
            hab = sorted({w.get('speaker_id') for w in j.get('words', [])} - {None})
            print(f, len(j.get('words', [])), 'palabras', hab, flush=True)
        except Exception as e:                                     # noqa: BLE001
            print(f, 'FALLA', str(e)[:200], flush=True)
    print('LISTO', flush=True)
