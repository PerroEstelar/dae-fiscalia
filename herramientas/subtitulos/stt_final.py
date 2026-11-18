# -*- coding: utf-8 -*-
"""Transcripcion por palabra (Scribe) del VIDEO FINAL de cada entrega, para sacar subtitulos con los tiempos del
video tal como se entrego (intro incluida). Pedido de Esteban y de Sebastian, 18 nov 2026.

Uso:  stt_final.py <manifiesto.json> <carpeta de salida> [clave ...]
  manifiesto: lista de {"clave", "video" (ruta local del archivo entregado), "nombre" (del .srt, sin extension),
              "carpeta" (id de la carpeta de Drive del video)}
  salida: <clave>.json con la respuesta de Scribe, y stt.log

El audio va a WAV mono de 16 kHz EN MEMORIA (con mp3 Scribe devolvio basura una vez, y D: no tiene lugar).
La clave de ElevenLabs no se imprime. Antes y despues de cada video se anota el consumo de la cuenta."""
import glob
import json
import os
import struct
import subprocess
import sys
import time
import urllib.request
import uuid

FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
MAN = json.load(open(sys.argv[1], encoding='utf-8'))
T = sys.argv[2].rstrip('/\\') + '/'
SOLO = set(sys.argv[3:])
os.makedirs(T, exist_ok=True)
KEY = open(r'D:\DAE\_secretos\elevenlabs.txt', encoding='utf-8').read().strip()
log = open(T + 'stt.log', 'a', encoding='utf-8')


def w(*a):
    print(time.strftime('%H:%M:%S'), *a, file=log, flush=True)


def uso():
    try:
        req = urllib.request.Request('https://api.elevenlabs.io/v1/user/subscription', headers={'xi-api-key': KEY})
        with urllib.request.urlopen(req, timeout=60) as r:
            j = json.loads(r.read().decode('utf-8'))
        return {k: j.get(k) for k in ('tier', 'character_count', 'character_limit')}
    except Exception as e:
        return {'error': str(e)[:120]}


def wav(video):
    """WAV mono 16 kHz en memoria. Por un tubo ffmpeg no puede volver a escribir los largos del encabezado: se
    corrigen aca."""
    b = subprocess.run([FB + '/ffmpeg.exe', '-v', 'error', '-i', video, '-vn', '-ac', '1', '-ar', '16000',
                        '-c:a', 'pcm_s16le', '-f', 'wav', '-'], capture_output=True).stdout
    b = bytearray(b)
    i = b.find(b'data')
    if b[:4] != b'RIFF' or i < 0:
        raise RuntimeError('ffmpeg no devolvio un WAV')
    b[4:8] = struct.pack('<I', len(b) - 8)
    b[i + 4:i + 8] = struct.pack('<I', len(b) - i - 8)
    return bytes(b), (len(b) - i - 8) / 32000.0


def scribe(audio):
    b = uuid.uuid4().hex
    body = b''
    campos = {'model_id': 'scribe_v1', 'language_code': 'spa', 'timestamps_granularity': 'word',
              'tag_audio_events': 'false', 'diarize': 'true'}
    for k, x in campos.items():
        body += ('--%s\r\nContent-Disposition: form-data; name="%s"\r\n\r\n%s\r\n' % (b, k, x)).encode()
    body += ('--%s\r\nContent-Disposition: form-data; name="file"; filename="audio.wav"\r\n'
             'Content-Type: audio/wav\r\n\r\n' % b).encode()
    body += audio + ('\r\n--%s--\r\n' % b).encode()
    req = urllib.request.Request('https://api.elevenlabs.io/v1/speech-to-text', data=body,
                                 headers={'xi-api-key': KEY, 'Content-Type': 'multipart/form-data; boundary=' + b})
    with urllib.request.urlopen(req, timeout=3000) as r:
        return json.loads(r.read().decode('utf-8'))


w('arranca', len(MAN), 'videos', '| cuenta', uso())
for m in MAN:
    k = m['clave']
    if SOLO and k not in SOLO:
        continue
    out = T + k + '.json'
    if os.path.exists(out):
        w(k, 'ya esta'); continue
    if not os.path.exists(m['video']):
        w(k, 'NO ESTA EL VIDEO', m['video']); continue
    try:
        t = time.time()
        a, dur = wav(m['video'])
        j = scribe(a)
        json.dump(j, open(out, 'w', encoding='utf-8'), ensure_ascii=False)
        ws = [x for x in j.get('words', []) if x.get('type') == 'word']
        hab = sorted({str(x.get('speaker_id')) for x in ws})
        # Scribe puede devolver basura con probabilidad 1,0: se mira el ritmo (unas 2 palabras por segundo de habla)
        w('%s|OK|audio %.1f s|%d palabras|primera %.2f ultima %.2f|%.2f pal/s|hablantes %s|%.0f s|cuenta %s|%s'
          % (k, dur, len(ws), ws[0]['start'] if ws else -1, ws[-1]['end'] if ws else -1,
             len(ws) / max(1.0, (ws[-1]['end'] - ws[0]['start']) if ws else 1.0), ','.join(hab), time.time() - t,
             uso().get('character_count'), (j.get('text') or '')[:90].replace('\n', ' ')))
    except Exception as e:
        w(k, 'STT FALLA', repr(e)[:300])
w('LISTO')
