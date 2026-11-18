# -*- coding: utf-8 -*-
"""Segunda escucha de un tramo dudoso de una transcripcion: Scribe sobre el recorte, a velocidad normal y al 75 %.
Uso: stt_tramo.py <video> <desde s> <hasta s> [<video> <desde> <hasta> ...]     La clave no se imprime."""
import glob, json, os, struct, subprocess, sys, urllib.request, uuid
FB = glob.glob(os.path.expanduser('~') + '/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/*/bin')[0]
KEY = open(r'D:\DAE\_secretos\elevenlabs.txt', encoding='utf-8').read().strip()


def wav(video, a, b, af):
    x = bytearray(subprocess.run([FB + '/ffmpeg.exe', '-v', 'error', '-ss', '%.3f' % a, '-t', '%.3f' % (b - a), '-i', video,
                                  '-vn', '-ac', '1', '-ar', '16000'] + (['-af', af] if af else []) +
                                 ['-c:a', 'pcm_s16le', '-f', 'wav', '-'], capture_output=True).stdout)
    i = x.find(b'data')
    x[4:8] = struct.pack('<I', len(x) - 8); x[i + 4:i + 8] = struct.pack('<I', len(x) - i - 8)
    return bytes(x)


def scribe(audio):
    b = uuid.uuid4().hex
    body = b''
    for k, v in {'model_id': 'scribe_v1', 'language_code': 'spa', 'tag_audio_events': 'false'}.items():
        body += ('--%s\r\nContent-Disposition: form-data; name="%s"\r\n\r\n%s\r\n' % (b, k, v)).encode()
    body += ('--%s\r\nContent-Disposition: form-data; name="file"; filename="a.wav"\r\nContent-Type: audio/wav\r\n\r\n' % b).encode()
    body += audio + ('\r\n--%s--\r\n' % b).encode()
    req = urllib.request.Request('https://api.elevenlabs.io/v1/speech-to-text', data=body,
                                 headers={'xi-api-key': KEY, 'Content-Type': 'multipart/form-data; boundary=' + b})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode('utf-8')).get('text', '')


a = sys.argv[1:]
for i in range(0, len(a), 3):
    v, t0, t1 = a[i], float(a[i + 1]), float(a[i + 2])
    for nombre, af in (('normal', None), ('al 75 %', 'atempo=0.75')):
        try:
            print('%s %.1f-%.1f %s: %s' % (os.path.basename(v)[:34], t0, t1, nombre, scribe(wav(v, t0, t1, af)).strip()), flush=True)
        except Exception as e:
            print('FALLA', repr(e)[:200], flush=True)
