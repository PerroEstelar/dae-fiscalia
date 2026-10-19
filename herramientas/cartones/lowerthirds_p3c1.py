#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lower thirds del PRIORIDAD 03 · Caso 1 «El hospedaje El Mirador».

POR QUE EXISTEN
    Sebastian lo pidio en la revision del video 1, y pidio dos cosas
    distintas que aqui son la misma pieza:

        - toda FECHA va en pantalla como lower third, sin tinte, con la
          linea amarilla y la fecha sola;
        - cada vez que el narrador PRESENTA a alguien, el nombre se imprime.

LA REGLA DE CONVIVENCIA CON V3
    Un lower third y un carton tenido no pueden estar al tiempo: el tenido
    cubre el cuadro con 46 % de azul y los dos juntos se leen como dos
    cartones. Donde la ranura lleva los dos, el lower third va PRIMERO,
    pegado a la cabeza de la ranura, y el carton despues, con holgura.
    Donde no cabian los dos, gano el lower third y el carton se disolvio
    dentro de el -es el caso de Diana-.

LO QUE NO SE DUPLICA
    `ae06_cambio` ya dice «Elena · abril» y `ae07_linea_tiempo` ya dice
    «enero de dos mil veinticinco · septiembre de dos mil veintiseis».
    Esas dos fechas NO llevan lower third: ya estan en pantalla.

LAS FECHAS QUE SE FUNDEN CON UN NOMBRE
    Juliana y Yeimi entran en la misma frase que su fecha. En vez de dos
    piezas seguidas, la fecha baja al renglon del dato. Es lo que hace el
    documental y se lee de una sola pasada.

LOS NUMEROS VAN EN DIGITOS, NO EN LETRAS
    Peticion de Sebastian: en PANTALLA todo numero -el ano, la edad, el dia,
    las horas, la suma- va en digitos. «2025», no «dos mil veinticinco»;
    «23 anos», no «veintitres anos». Se lee de un vistazo, que es justo lo que
    un carton tiene que permitir.

    La LOCUCION no cambia: ahi el numero sigue escrito en letras, porque el
    texto de voz es lo que el sintetizador pronuncia y en digitos lo lee mal.
    Son dos escrituras del mismo dato y cada una sirve a su medio.
"""
import os
import sys

sys.path.insert(0, "/home/claude/lt")
import lower_third as LT

OUT = "/mnt/user-data/outputs/lt_p3c1"
os.makedirs(OUT, exist_ok=True)

N = 96   # el piso de comodidad de la serie; un lower third nunca pasa de ahi

#  (nombre de archivo, ranura, cuadro de entrada DENTRO de la ranura, spec)
LOWERS = [
    ("lt01_fecha_enero_mayo", "r02", 10, {
        "nombre": "Entre enero y mayo de 2025"}),
    ("lt02_cristina", "r03", 8, {
        "nombre": "Cristina",
        "dato": "Publicaba las ofertas y organizaba la llegada"}),
    ("lt03_victor", "r05", 24, {
        "nombre": "Víctor",
        "dato": "Las recibía y disponía las condiciones"}),
    ("lt04_daniela", "r08", 4, {
        "nombre": "Daniela",
        "dato": "23 años · desde Cúcuta"}),
    ("lt05_camilo", "r12", 8, {
        "nombre": "Camilo",
        "dato": "Conductor particular"}),
    ("lt06_paula", "r13", 30, {
        "nombre": "Paula",
        "dato": "29 años · trabajo sexual autónomo"}),
    ("lt07_elena", "r16", 20, {
        "nombre": "Elena",
        "dato": "35 años · trabajo de limpieza"}),
    ("lt08_fecha_diez_mayo", "r22", 22, {
        "nombre": "El 10 de mayo"}),
    ("lt09_diana", "r25", 30, {
        "nombre": "Diana",
        "dato": "Agencia de viajes · el precio ordinario y la comisión habitual"}),
    ("lt10_juliana", "r26", 4, {
        "nombre": "Juliana",
        "dato": "El 25 de mayo · 19 años"}),
    ("lt11_yeimi", "r28", 24, {
        "nombre": "Yeimi",
        "dato": "En agosto de 2026"}),
]

if __name__ == "__main__":
    for nom, r, off, spec in LOWERS:
        LT.render(spec, N, "%s/P3C1_%s.mov" % (OUT, nom))
