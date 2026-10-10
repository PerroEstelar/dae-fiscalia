#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reparte las frases de un texto sobre los tramos de voz medidos.

El locutor no hace una pausa en cada frase, así que un tramo de `silencedetect`
puede contener varias frases y una frase puede repartirse en dos tramos. Lo que
sí se cumple con mucha precisión es que el tiempo hablado es proporcional a los
caracteres: medido en seis piezas de la serie, 1,2 a 1,4 cuadros por carácter,
constante dentro de una misma locución. Entonces: se acumulan los caracteres y
se acumulan los cuadros hablados, y cada frase se corta donde coincidan.
"""
import re, sys, json


def frases(texto):
    out = []
    for p, parr in enumerate(x.strip() for x in texto.split("\n\n") if x.strip()):
        for f in re.split(r'(?<=[.:;?!…])\s+', parr):
            f = f.strip()
            if f:
                out.append((p, f))
    return out


def calzar(texto, tramos):
    """tramos = [(ini, fin)] en cuadros. Devuelve [(parrafo, frase, ini, fin)]."""
    fs = frases(texto)
    total_ch = sum(len(f) for _, f in fs)
    hablado = sum(b - a for a, b in tramos)
    # mapa cuadro-hablado -> cuadro real
    def real(h):
        acc = 0
        for a, b in tramos:
            if h <= acc + (b - a):
                return a + (h - acc)
            acc += b - a
        return tramos[-1][1]
    out, ch = [], 0
    for p, f in fs:
        ini = real(round(ch / total_ch * hablado))
        ch += len(f)
        fin = real(round(ch / total_ch * hablado))
        out.append((p, f, ini, fin))
    return out


if __name__ == "__main__":
    d = json.load(open(sys.argv[1], encoding="utf-8"))
    r = calzar(open(d["texto"], encoding="utf-8").read(), [tuple(t) for t in d["tramos"]])
    pa = -1
    for p, f, a, b in r:
        if p != pa:
            print("\n--- párrafo %d" % p); pa = p
        print("%5d %5d  (%4d)  %s" % (a, b, b - a, f[:96]))
