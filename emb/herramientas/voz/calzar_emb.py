"""calzar_emb.py — reparte los bloques de una locución sobre la voz medida.

Uso: python3 calzar_emb.py voz.wav bloques.json salida.json [--fps 23.976]
bloques.json = lista de textos, uno por bloque, en orden.
Salida: por bloque, el tiempo de inicio y fin de su voz y un mapa (carácter → segundo)
para ubicar cualquier frase dentro del bloque.

Método (el de la casa: el tiempo hablado es proporcional a los caracteres):
1. silencedetect -34 dB / 0,30 s da los tramos con voz.
2. Las fronteras entre bloques caen en la pausa más cercana a la que predice la proporción
   global de caracteres; se elige entre las pausas largas.
3. Dentro de cada bloque, los caracteres se reparten sobre su tiempo hablado (sin silencios).
"""
import json, re, subprocess, sys

def tramos(wav):
    o = subprocess.run(['ffmpeg', '-hide_banner', '-i', wav, '-af', 'silencedetect=noise=-34dB:d=0.30', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', wav],
                               capture_output=True, text=True).stdout)
    ss = [float(x) for x in re.findall(r'silence_start: ([0-9.]+)', o)]
    se = [float(x) for x in re.findall(r'silence_end: ([0-9.]+)', o)]
    sil = list(zip(ss, se + [dur] * (len(ss) - len(se))))
    habla, t = [], 0.0
    for a, b in sil:
        if a > t + 0.02: habla.append((t, a))
        t = b
    if t < dur - 0.02: habla.append((t, dur))
    return habla, sil, dur

def mapa(habla, t0, t1, n):
    """reparte n caracteres sobre el habla entre t0 y t1; devuelve pares (car, seg)"""
    seg = [(max(a, t0), min(b, t1)) for a, b in habla if b > t0 and a < t1]
    tot = sum(b - a for a, b in seg) or 1e-9
    pts, acc = [], 0.0
    for a, b in seg:
        pts.append((round(acc / tot * n, 1), round(a, 3)))
        acc += b - a
        pts.append((round(acc / tot * n, 1), round(b, 3)))
    return pts

def main():
    wav, bj, out = sys.argv[1:4]
    bloques = json.load(open(bj))
    habla, sil, dur = tramos(wav)
    t_ini, t_fin = habla[0][0], habla[-1][1]
    habla_tot = sum(b - a for a, b in habla)
    N = sum(len(b) for b in bloques)
    # tiempo real que corresponde a una fracción del habla total
    def real(frac):
        obj, acc = frac * habla_tot, 0.0
        for a, b in habla:
            if acc + (b - a) >= obj: return a + (obj - acc)
            acc += b - a
        return t_fin
    pausas = [(a, b) for a, b in sil if a > t_ini and b < t_fin]
    bordes, c = [t_ini], 0
    for blq in bloques[:-1]:
        c += len(blq)
        pred = real(c / N)
        p = min(pausas, key=lambda x: abs((x[0] + x[1]) / 2 - pred) - 0.6 * (x[1] - x[0]))
        bordes.append(p[1])           # el bloque siguiente arranca donde termina la pausa
    bordes.append(t_fin)
    res = []
    for i, blq in enumerate(bloques):
        a, b = bordes[i], bordes[i + 1]
        fin_voz = max(x for _, x in mapa(habla, a, b, len(blq)))
        res.append({'i': i, 'ini': round(a, 3), 'fin': round(fin_voz, 3), 'sig': round(b, 3), 'mapa': mapa(habla, a, b, len(blq))})
    json.dump({'dur': dur, 'bloques': res}, open(out, 'w'), ensure_ascii=False, indent=1)
    for r in res: print(r['i'], r['ini'], r['fin'], len(bloques[r['i']]), round((r['fin'] - r['ini']) * 23.976 / len(bloques[r['i']]), 2), 'c/car')

if __name__ == '__main__': main()
