#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lower thirds del Caso 2 «El taller del segundo piso».

LAS SEIS
    La fecha y el lugar, y la entrada de cada persona que el relato presenta.
    Tres de ellos eran cartones de narración que en realidad siempre fueron
    lower thirds —un nombre con un dato corto— y se mudaron de pista:
    `n01_cucuta`, `n04_mara` y `n07_dario`. El cuarto, `ae09`, era una losa
    blanca entera para decir quién es Elisa.

SAÚL NO LLEVA, Y ESA ES LA DECISIÓN
    Es el que todos nombran y nadie muestra. No aparece en ningún plano, así
    que tampoco puede aparecer su nombre impreso: imprimirlo sería darle la
    presencia en pantalla que la hoja de personajes le niega a propósito.

MARA LLEVA LO MÍNIMO, Y TAMBIÉN ES DECISIÓN
    El guion dice en locución «mujer trans venezolana de veintiséis años», y
    el caso trata justamente de cómo la institución la nombra. Sebastián
    decidió que en pantalla vaya sólo el nombre y la edad, igual que los
    demás. La identidad queda en la locución, que es donde el participante la
    necesita, y la pantalla no la subraya.

LOS NÚMEROS, EN DÍGITOS
    18 de marzo, 26 años, 35, 17, 32. En locución siguen en letras, porque es
    lo que el sintetizador pronuncia bien.
"""
import os
import sys

sys.path.insert(0, "/home/claude/lt")
import lower_third as LT

OUT = "/mnt/user-data/outputs/lt_p3c2"
os.makedirs(OUT, exist_ok=True)

N = 96

#  (archivo, ranura, cuadro de entrada en la ranura, spec)
LOWERS = [
    ("lt01_fecha_cucuta", "r02", 12, {
        "nombre": "Cúcuta · 18 de marzo de 2026"}),
    ("lt02_mara", "r06", 10, {
        "nombre": "Mara",
        "dato": "26 años"}),
    ("lt03_samuel", "r12", 8, {
        "nombre": "Samuel",
        "dato": "35 años · ecuatoriano"}),
    ("lt04_dario", "r14", 8, {
        "nombre": "Darío",
        "dato": "Trabaja para Saúl y recibe parte de los pagos"}),
    ("lt05_elisa", "r19", 28, {
        "nombre": "Elisa · 17 años",
        "dato": "Llegó por una tía que recibe parte de su remuneración"}),
    ("lt06_patricia", "r23", 30, {
        "nombre": "Patricia",
        "dato": "32 años"}),
]

if __name__ == "__main__":
    for nom, r, off, spec in LOWERS:
        LT.render(spec, N, "%s/P3C2_%s.mov" % (OUT, nom))
