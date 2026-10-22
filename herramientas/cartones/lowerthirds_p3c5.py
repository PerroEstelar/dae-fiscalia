#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lower thirds del Caso 5 «Voces, registros y cuentas».

CINCO: EL SITIO Y LA FECHA, Y LOS CUATRO CON CARA
    Oscar, Lucia, Renata y Tomas. No entran Andres ni la psicologa, que son
    funcionarios y van sin cara por la regla SRPA; no entra la tercera mujer,
    que no se dibuja de ninguna forma; no entran el guia ni la voz de «la
    entrega», que no estan establecidos.

SI HAY ROTULO DE FECHA Y LUGAR, AL REVES QUE EN EL CASO 4
    Alli no se puso porque el documento no daba ciudad ni fecha. Este si: «en
    un alojamiento de Medellin» y «entre enero y marzo de 2026». Los dos
    salen de la acusacion y van tal cual.

CADA DATO ES LO QUE EL ENUNCIADO DA POR ESTABLECIDO
    De Oscar y de Tomas se imprime la ATRIBUCION, con el verbo del documento
    -«se le atribuye»-, nunca el hecho. Es la misma correccion que el Caso 3
    hizo con el rotulo de Nidia: la atribucion la carga el verbo.

    De Lucia y de Renata se imprime lo que hacen en el proceso, que es lo
    unico que el documento afirma de ellas sin discutirlo. Lo demas -si el
    relato es cierto, si la amenaza existio- es exactamente lo que el
    ejercicio pone a examinar.

EL DE RENATA ES EL QUE MAS IMPORTA
    «Reside fuera del pais y acepta declarar» es, literalmente, la respuesta
    a la afirmacion de que la migracion vuelve imposible su comparecencia. El
    rotulo y la placa dicen lo mismo: esta ubicable.
"""
import os
import sys

sys.path.insert(0, "/home/claude/lt")
import lower_third as LT

OUT = "/home/claude/p3c5/lt/out"
os.makedirs(OUT, exist_ok=True)

N = 96

#  (archivo, ranura, cuadro de entrada en la ranura, spec)
LOWERS = [
    ("lt01_fecha_lugar", "r04", 14, {
        "nombre": "Medellín · enero – marzo de 2026"}),
    ("lt02_oscar", "r03", 12, {
        "nombre": "Óscar",
        "dato": "Se le atribuye recibir y acoger a Lucía y a Renata"}),
    ("lt03_tomas", "r05", 12, {
        "nombre": "Tomás",
        "dato": "Se le atribuye facilitar una salida irregular"}),
    ("lt04_lucia", "r21", 10, {
        "nombre": "Lucía",
        "dato": "Declara en el juicio"}),
    ("lt05_renata", "r23", 12, {
        "nombre": "Renata",
        "dato": "Reside fuera del país y acepta declarar"}),
]

if __name__ == "__main__":
    for nom, r, off, spec in LOWERS:
        LT.render(spec, N, "%s/P3C5_%s.mov" % (OUT, nom))
        print("%-20s %-5s entra en el cuadro %2d de la ranura" % (nom, r, off))
