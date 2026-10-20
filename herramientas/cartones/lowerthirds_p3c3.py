#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lower thirds del Caso 3 «Ruta del Golfo».

LAS SEIS
    La fecha y el lugar, y la entrada de cada persona que el relato presenta:
    Luis, Marta, Omar, Teresa y Nidia.

CADA DATO ES LO QUE EL ENUNCIADO DA POR ESTABLECIDO, NO LO QUE SE DISCUTE
    Es la misma regla que fija el color del acento, aplicada a la letra. De
    Marta se imprime que recibe cinco giros en una cuenta a su nombre, que es
    un hecho del documento; no se imprime qué significan, que es exactamente
    lo que la reunión de evaluación pone en duda. De Omar, que conduce. De
    Luis, que aparece como usuario de la cuenta —«aparece como», que es el
    verbo del documento—.

NIDIA LLEVA LA PALABRA «ATRIBUIDO», Y ESTÁ MEDIDA
    El documento dice «en otro episodio, atribuido a una mujer llamada
    Nidia». Imprimir su nombre sin esa palabra convertiría en hecho lo que el
    texto marca como atribución, que es justo el error que la pieza enseña.

LOS CUATRO VIAJEROS NO LLEVAN
    El documento no les da nombre y el caso los trata como grupo. Un lower
    third les daría una individualidad que el enunciado no les da.

LOS NÚMEROS, EN DÍGITOS
    5 giros, abril de 2026. En locución siguen en letras, porque es lo que el
    sintetizador pronuncia bien.
"""
import os
import sys

sys.path.insert(0, "/home/claude/lt")
import lower_third as LT

OUT = "/mnt/user-data/outputs/lt_p3c3"
os.makedirs(OUT, exist_ok=True)

N = 96

#  (archivo, ranura, cuadro de entrada en la ranura, spec)
LOWERS = [
    ("lt01_fecha_lugar", "r02", 14, {
        "nombre": "Medellín – Necoclí · abril de 2026"}),
    ("lt02_luis", "r05", 10, {
        "nombre": "Luis",
        "dato": "Aparece como usuario de la cuenta Enlace Norte"}),
    ("lt03_marta", "r06", 10, {
        "nombre": "Marta",
        "dato": "Recibe 5 giros en una cuenta bancaria a su nombre"}),
    ("lt04_omar", "r09", 8, {
        "nombre": "Omar",
        "dato": "Conduce el vehículo que lleva al grupo"}),
    ("lt05_teresa", "r10", 12, {
        "nombre": "Teresa",
        "dato": "Administra el alojamiento donde se quedan"}),
    ("lt06_nidia", "r15", 12, {
        "nombre": "Nidia",
        "dato": "Otro episodio, atribuido"}),
]

if __name__ == "__main__":
    for nom, r, off, spec in LOWERS:
        LT.render(spec, N, "%s/P3C3_%s.mov" % (OUT, nom))
        print("%-18s %-5s entra en el cuadro %2d de la ranura" % (nom, r, off))
