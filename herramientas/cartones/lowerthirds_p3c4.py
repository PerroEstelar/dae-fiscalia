#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lower thirds del Caso 4 «Puerto de salida».

CUATRO, Y NO SEIS
    Entran los cuatro a quienes la pieza presenta como personas: Nora, Iván,
    el recepcionista y Lina. No entran Inés ni Alba, por la misma razon por la
    que no aparecen en ningun plano: lo que el caso discute sobre ellas es que
    LA IMPUTACION DE LINA NO LAS INDIVIDUALIZA. Un rotulo con su nombre y un
    dato haria con la letra lo contrario de lo que el ejercicio señala que
    falto hacer con el escrito.

    Tampoco entran los roles -fiscal, investigador, jueza, juez, defensa,
    representante-. No tienen cara por decision de direccion de arte y
    tampoco tienen nombre en el documento.

NO HAY ROTULO DE FECHA NI DE LUGAR, Y NO ES UN OLVIDO
    El Caso 3 abria con «Medellín – Necoclí · abril de 2026» porque el
    documento daba las dos cosas. Este documento no da ciudad ni fecha: habla
    de «un punto de salida a Panamá» y de 2024 y 2025 dentro de la imputacion.
    Inventar un rotulo de situacion seria poner en pantalla un dato que la
    carpeta no tiene.

CADA DATO ES LO QUE EL ENUNCIADO DA POR ESTABLECIDO
    Y en este caso eso obliga a conservar los verbos del documento, que son
    verbos de atribucion y no de hecho:

      Nora   «vinculada con»        — no «captó»
      Iván   «aparece coordinando»  — no «coordina»

    Los dos se acortaron el 21 de octubre despues de componerlos sobre su
    placa: a su largo original -1.240 y 1.259 pixeles- el renglon entraba en
    la figura. Ahora los dos terminan antes de 1.000 y el rotulo queda sobre
    fondo limpio en las cuatro placas.

    De Lina se imprime que es la tercera investigada, que es lo unico que el
    documento afirma de ella sin discutirlo: todo lo demas es justamente la
    frase que la pieza pone en duda.

EL RECEPCIONISTA ES EL UNICO CON UN DATO EN AFIRMATIVO
    «Detenido sin orden» no esta atribuido ni matizado en ninguna parte del
    documento: esta afirmado. Es la misma razon por la que lleva el azul
    institucional en prenda completa mientras los otros tres llevan un
    detalle amarillo. El rotulo y el acento dicen lo mismo.
"""
import os
import sys

sys.path.insert(0, "/home/claude/lt")
import lower_third as LT

OUT = "/home/claude/p3c4/lt/out"
os.makedirs(OUT, exist_ok=True)

N = 96

#  (archivo, ranura, cuadro de entrada en la ranura, spec)
LOWERS = [
    ("lt01_nora", "r02", 12, {
        "nombre": "Nora",
        "dato": "Vinculada con la captación de Inés y Alba"}),
    ("lt02_ivan", "r05", 14, {
        "nombre": "Iván",
        "dato": "Aparece coordinando el transporte interno"}),
    ("lt03_recepcionista", "r13", 10, {
        "nombre": "El recepcionista",
        "dato": "Detenido sin orden"}),
    ("lt04_lina", "r25", 12, {
        "nombre": "Lina",
        "dato": "Tercera investigada"}),
]

if __name__ == "__main__":
    for nom, r, off, spec in LOWERS:
        LT.render(spec, N, "%s/P3C4_%s.mov" % (OUT, nom))
        print("%-20s %-5s entra en el cuadro %2d de la ranura" % (nom, r, off))
