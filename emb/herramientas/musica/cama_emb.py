"""cama_emb.py — cama de música con el ducking horneado, para los videos del EMB.

cama(pista, total_s, tramos_voz, salida)
- La pista se normaliza a −26 LUFS (dos pasadas de loudnorm).
- Si el video es más largo que la pista, se repite el cuerpo (desde el segundo 20) con un
  fundido cruzado de 4 s; el final real de la pista no se usa: la cama cierra con fundido de 3 s.
- Bajo la voz baja 6 dB (−32 LUFS), con rampas de 0,5 s antes y 0,7 s después de cada tramo.
- Entra con fundido de 1,5 s.
"""
import json, subprocess, numpy as np

SR = 48000

def _decod(path):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', path, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()

def _norm(path, out, I=-26):
    m = subprocess.run(['ffmpeg', '-hide_banner', '-i', path, '-af', f'loudnorm=I={I}:TP=-2:LRA=11:print_format=json', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    j = json.loads(m[m.rindex('{'):m.rindex('}') + 1])
    f = (f"loudnorm=I={I}:TP=-2:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}"
         f":measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true,aresample={SR}")
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', path, '-af', f, '-ar', str(SR), '-ac', '2', out], check=True)

def cama(pista, total, tramos, salida, tmp='/tmp/_cama_norm.wav'):
    _norm(pista, tmp)
    x = _decod(tmp); n = int(total * SR)
    xf = 4 * SR; inicio_bucle = 20 * SR; fin_util = len(x) - 6 * SR
    y = x[:min(len(x), fin_util)].copy()
    while len(y) < n:
        seg = x[inicio_bucle:fin_util]
        r = np.linspace(0, 1, xf)[:, None]
        y[-xf:] = y[-xf:] * (1 - r) + seg[:xf] * r
        y = np.concatenate([y, seg[xf:]])
    y = y[:n]
    g = np.ones(n, np.float32)
    duck = 10 ** (-6 / 20)
    t = np.arange(n) / SR
    env = np.zeros(n, np.float32)
    for a, b in tramos:
        a0, b1 = a - 0.5, b + 0.7
        up = np.clip((t - a0) / 0.5, 0, 1); dn = np.clip((b1 - t) / 0.7, 0, 1)
        env = np.maximum(env, np.minimum(up, dn))
    g = 1 - env * (1 - duck)
    g *= np.clip(t / 1.5, 0, 1) * np.clip((total - t) / 3.0, 0, 1)
    y = (y * g[:, None]).astype(np.float32)
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', '-c:a', 'pcm_s24le', salida],
                   input=y.tobytes(), check=True)
    return salida
