# -*- coding: utf-8 -*-
r"""Aprieta un master de narracion de Derechos humanos: huecos mas cortos,
pausas internas mas cortas y los personajes un poco mas rapidos.

    python apretar_dh.py <master.wav> <piezas.json> <salida.wav>

DH U3, 1 nov (Sebastian): «we need to shorten some of the narration gaps…
it sounds glitchy, also make the other characters besides the main narrator
talk a bit faster, it's like they are dragging the video».

`piezas.json` lo arma el plan (`mapa_u3.py`, en la nube, sobre la envolvente
de la voz a -48 dB): una lista ordenada de piezas
    {"tipo": "copia",  "rangos": [[a, b], ...]}              tal cual
    {"tipo": "bloque", "tempo": 1.08, "rangos": [[a, b], ...]}
en segundos del master. Un hueco que se acorta se queda con sus dos orillas
(la cola de la frase anterior y el aire antes de la siguiente) y pierde el
medio; una pausa interna igual. Todos los cortes caen en silencio. El bloque
de un personaje se pega y despues pasa por `atempo` (WSOLA: cambia el ritmo,
no el tono). Carlos va a tempo 1.

Cada rango lleva 3 ms de fundido en sus dos bordes para que ningun corte
haga clic. El nivel no se toca: el master ya estaba nivelado y con el
realce del entrevistador.
"""
import json
import subprocess
import sys

SR = 48000
FUNDE = 0.003


def main(entrada, plan, salida):
    pz = json.load(open(plan, encoding='utf-8'))['piezas']
    fc, etiquetas, k = [], [], 0
    for i, p in enumerate(pz):
        partes = []
        for a, b in p['rangos']:
            s0, s1 = int(round(a * SR)), int(round(b * SR))
            if s1 <= s0:
                continue
            d = (s1 - s0) / float(SR)
            f = min(FUNDE, d / 4)
            fc.append('[0:a]atrim=start_sample=%d:end_sample=%d,asetpts=PTS-STARTPTS,'
                      'afade=t=in:d=%.4f,afade=t=out:st=%.6f:d=%.4f[r%d]'
                      % (s0, s1, f, d - f, f, k))
            partes.append('[r%d]' % k)
            k += 1
        if not partes:
            continue
        t = p.get('tempo', 1.0)
        cola = ',atempo=%.4f' % t if abs(t - 1.0) > 1e-6 else ''
        if len(partes) == 1 and not cola:
            etiquetas.append(partes[0])
            continue
        fc.append('%sconcat=n=%d:v=0:a=1%s[p%d]' % (''.join(partes), len(partes), cola, i))
        etiquetas.append('[p%d]' % i)
    fc.append('%sconcat=n=%d:v=0:a=1[s]' % (''.join(etiquetas), len(etiquetas)))
    # ffmpeg 8+ ya no tiene -filter_complex_script: el grafo se lee con
    # «-/filter_complex <archivo>» (el grafo de la U3 pasa de 20 mil caracteres)
    guion = salida + '.filtro.txt'
    open(guion, 'w', encoding='utf-8').write(';\n'.join(fc))
    r = subprocess.run(['ffmpeg', '-hide_banner', '-y', '-i', entrada,
                        '-/filter_complex', guion, '-map', '[s]',
                        '-c:a', 'pcm_s24le', '-ar', str(SR), salida],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode:
        print(r.stderr[-2000:])
        sys.exit(1)
    q = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=duration_ts',
                        '-of', 'csv=p=0', salida], capture_output=True, text=True).stdout.strip()
    esperado = json.load(open(plan, encoding='utf-8')).get('dur_nuevo')
    print('%s: %s muestras = %.3f s (plan %.3f s), %d rangos'
          % (salida, q, int(q) / float(SR), esperado or 0, k))


if __name__ == '__main__':
    main(*sys.argv[1:4])
