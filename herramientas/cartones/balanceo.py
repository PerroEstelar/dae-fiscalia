# -*- coding: utf-8 -*-
"""Renglones equilibrados para los cartones de caja (14 nov 2026).

`cartones_ma.componer` corta los renglones a lo voraz: llena cada uno hasta el ancho
y deja lo que sobre para el siguiente. Con los títulos en negrita a 46 px (unos 22
caracteres por renglón) eso deja muchas veces una palabra sola abajo («Conclusión de
la unidad / 3», «¿Qué se hace con los / bienes…»).

`piezas` reparte las palabras en la misma cantidad de renglones que el corte voraz,
pero parejos: lo más cerca posible del largo medio. Devuelve un trozo por renglón,
con el formato de las líneas de `componer`: `(texto, peso, px, gap)`, donde el
primero lleva el gap pedido y los demás 0. Así `componer` los apila con el mismo
interlineado y no los vuelve a cortar.
- El alto no cambia, porque son los mismos renglones.
- La cima medida antes sigue valiendo.

Las fuentes son las del repositorio (`fuentes/`), las mismas Montserrat que usan
los cartones en la máquina.
"""
import os

from PIL import Image, ImageDraw, ImageFont

FUENTES = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fuentes')
TTF = {'bold': os.path.join(FUENTES, 'Montserrat-Bold.ttf'),
       'med': os.path.join(FUENTES, 'Montserrat-Medium.ttf')}
_d = ImageDraw.Draw(Image.new('RGB', (8, 8)))
_cache = {}


def _fuente(peso, px):
    k = (peso, px)
    if k not in _cache:
        _cache[k] = ImageFont.truetype(TTF[peso], px)
    return _cache[k]


def voraz(texto, peso, px, ancho):
    f = _fuente(peso, px)
    out, ln = [], ''
    for w in texto.split():
        p = (ln + ' ' + w).strip()
        if _d.textlength(p, font=f) <= ancho or not ln:
            ln = p
        else:
            out.append(ln)
            ln = w
    if ln:
        out.append(ln)
    return out


def equilibrar(texto, peso, px, ancho):
    """Los renglones del corte voraz, repartidos para que queden parejos: se minimiza la
    suma de los cuadrados de lo que cada renglón se aparta del largo medio. (Minimizar
    solo el renglón más largo dejaba a veces un primer renglón de dos palabras.)"""
    k = len(voraz(texto, peso, px, ancho))
    ws = texto.split()
    if k <= 1:
        return [' '.join(ws)]
    f = _fuente(peso, px)
    n = len(ws)
    largo = {}

    def lw(i, j):
        if (i, j) not in largo:
            largo[(i, j)] = _d.textlength(' '.join(ws[i:j]), font=f)
        return largo[(i, j)]

    medio = lw(0, n) / k
    mejor = {}      # (i, r) -> (costo, cortes) para ws[i:] en r renglones

    def resolver(i, r):
        if (i, r) in mejor:
            return mejor[(i, r)]
        res = None
        if r == 1:
            x = lw(i, n)
            if x <= ancho:
                res = ((x - medio) ** 2, [n])
        else:
            for j in range(i + 1, n - r + 2):
                x = lw(i, j)
                if x > ancho:
                    break
                sub = resolver(j, r - 1)
                if sub is None:
                    continue
                costo = (x - medio) ** 2 + sub[0]
                if res is None or costo < res[0]:
                    res = (costo, [j] + sub[1])
        mejor[(i, r)] = res
        return res

    sol = resolver(0, k)
    if sol is None:
        return voraz(texto, peso, px, ancho)
    out, i = [], 0
    for j in sol[1]:
        out.append(' '.join(ws[i:j]))
        i = j
    return out


def piezas(texto, peso, px, gap, ancho):
    """Un trozo `(texto, peso, px, gap)` por renglón equilibrado. Un salto de línea
    explícito en el texto separa párrafos, y cada uno se equilibra por su cuenta."""
    out = []
    for parrafo in texto.split('\n'):
        for ln in equilibrar(parrafo, peso, px, ancho):
            out.append((ln, peso, px, gap if not out else 0))
    return out
