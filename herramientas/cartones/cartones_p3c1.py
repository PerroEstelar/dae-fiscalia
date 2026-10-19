#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones del PRIORIDAD 03 · Caso 1 «El hospedaje El Mirador».

TRES FAMILIAS, Y CADA UNA HACE UNA COSA DISTINTA

    GRAFICOS (`ae*`)  Fondo blanco, ocupan su propia ranura. Son los diez
        tramos en que la pieza deja de mostrar y se pone a enunciar: el
        acuerdo, la bisagra, lo que distingue a cada persona, la linea de
        tiempo y el cierre.

    NARRACION (`n*`)  Transparentes con tinte, van ENCIMA de una ranura de
        placa. Llevan el dato concreto que la imagen no puede decir -una
        tarifa, una fecha, una frase textual- sin sacar al participante de
        la escena.

    PAUSA (`p*`)  El lecho de votacion del final.

EL VERBATIM, QUE AQUI ES EL PUNTO DEL CASO
    Tres frases del documento se citan literales y entrecomilladas, porque
    son justamente lo que el participante tiene que valorar:

        «salió del colegio hace poco»
        «mi mamá no sabe que estoy en esto»
        «si pregunto, se asusta y se va»

    Las dos primeras son de Yeimi y van en su propio carton grafico. La
    tercera es de Cristina y va sobre el primer plano de Yeimi: la cara
    mientras se lee lo que la otra decidio. No se parafrasean y no se
    completan.

LO QUE NINGUN CARTON HACE
    Ninguno dice quien responde. Las opciones de la votacion son las tres
    tesis del equipo, literales del documento, y ninguna se presenta como
    la correcta.
"""
import math
import os
import sys

sys.path.insert(0, "/home/claude/cartones")
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_p3c1"
os.makedirs(OUT, exist_ok=True)

FPS = 23.976023976
PPM = 168.0


# El piso de 96 cuadros es una regla de COMODIDAD, no de velocidad de lectura:
# un carton de una linea no deberia aparecer y desaparecer. `ae01` mide 89
# cuadros porque asi quedo la ranura al imantar, y son 3,7 s para seis
# palabras -1,7 veces lo que pide el ritmo de 168 ppm-. Se acepta por debajo
# del piso y queda dicho.
PISO = {"ae01_establecidos": 89}


def cuadros(spec, holgura=1.15, minimo=96):
    txt = " ".join(spec.get(k, "") for k in ("ante", "titulo", "cuerpo", "suelta"))
    n = len([w for w in txt.split() if any(ch.isalnum() for ch in w)])
    return max(minimo, int(math.ceil(n / PPM * 60 * FPS * holgura)))


# ---------------------------------------------------------------- graficos
# (nombre, ranura, cuadros de la ranura, spec). Ocupan la ranura entera.
GRAFICOS = [
    ("ae01_establecidos", "r01", 89, {
        "suelta": "Los hechos se tienen por establecidos"}),
    ("ae02_el_acuerdo", "r04", 156, {
        "ante": "El acuerdo",
        "titulo": "Deudas impuestas por viaje, alojamiento y alimentación",
        "cuerpo": "Sin decidir libremente cuándo terminar"}),
    ("ae03_no_todas", "r07", 105, {
        "suelta": "No todas estaban sometidas a las mismas condiciones"}),
    ("ae04_deuda", "r10", 181, {
        "ante": "Daniela",
        "titulo": "Documento retenido, deuda de tres millones",
        "cuerpo": "Y una amenaza contra su hermano"}),
    ("ae05_paula", "r15", 195, {
        "ante": "Paula",
        "titulo": "Pagó su viaje, conservó sus documentos, administró sus ingresos",
        "cuerpo": "Podía rechazar personas, no trabajar o retirarse sin penalidad"}),
    ("ae06_cambio", "r18", 154, {
        "ante": "Elena · abril",
        "titulo": "Dieciséis horas, sin descansos",
        "cuerpo": "La remuneración entera a una deuda sin término explicado"}),
    ("ae07_linea_tiempo", "r20", 124, {
        "ante": "Sin interrupción",
        "titulo": "Enero de dos mil veinticinco · septiembre de dos mil veintiséis"}),
    ("ae09_interrumpido", "r27", 226, {
        "ante": "Juliana",
        "titulo": "Incorporada al sistema de deudas",
        "cuerpo": "Interrumpido el mismo día, antes de que realizara acto sexual "
                  "alguno o generara ingresos"}),
    ("ae10_mensajes", "r29", 170, {
        "ante": "Yeimi",
        "titulo": "«salió del colegio hace poco»\n«mi mamá no sabe que estoy en esto»",
        "cuerpo": "Sin cédula «todavía»"}),
    ("ae11_las_nueve", "r31", 221, {
        "ante": "Nueve personas",
        "titulo": "Un solo hospedaje",
        "cuerpo": "Y ninguna en la misma situación"}),
]

# --------------------------------------------------------------- narracion
# (nombre, ranura, cuadros de la ranura, spec). Van encima de la placa.
NARRACION = [
    ("n01_instagram", "r03", 239, {
        "titulo": "Ofrecimientos laborales desde una cuenta creada para ese fin"}),
    ("n02_mesera", "r08", 214, {
        "suelta": "Oferta de empleo de mesera"}),
    ("n03_alimentos", "r11", 150, {
        "suelta": "Podía salir a comprar alimentos"}),
    ("n04_tarifa", "r12", 224, {
        "titulo": "Cobró la tarifa habitual",
        "cuerpo": "Entonces desconocía el acuerdo"}),
    ("n05_disponible", "r17", 253, {
        "suelta": "Debía regresar y permanecer disponible"}),
    ("n06_terminal", "r24", 210, {
        "suelta": "Pidió que la llevara a la terminal"}),
    ("n07_comision", "r25", 156, {
        "titulo": "Cobró el precio ordinario y la comisión habitual"}),
    # el verbatim de Cristina, sobre la cara de Yeimi
    ("n08_si_pregunto", "r30", 233, {
        "ante": "Cristina decidió no verificarlo",
        "titulo": "«si pregunto, se asusta y se va»"}),
]

if __name__ == "__main__":
    print("%-20s %-5s %6s %6s %7s" % ("carton", "ranura", "cartón", "ranura", "margen"))
    apretados = []
    for fam, lista, alfa, tinte in (("gráfico", GRAFICOS, False, False),
                                    ("narración", NARRACION, True, True)):
        print("--- %s" % fam)
        for n, r, fr, spec in lista:
            f = fr if not alfa else cuadros(spec)
            necesita = cuadros(spec, minimo=PISO.get(n, 96))
            m = fr - necesita
            if m < 0:
                apretados.append((n, m))
            C.render_carton(spec, f, C.BLANCO_FONDO if not alfa else None, alfa,
                            "%s/P3C1_%s.mov" % (OUT, n), con_tinte=tinte)
            print("%-20s %-5s %6d %6d %+7d" % (n, r, f, fr, m))
    if apretados:
        print("\nAPRETADOS:", apretados)
    else:
        print("\ntodos con margen de lectura a 168 ppm")
