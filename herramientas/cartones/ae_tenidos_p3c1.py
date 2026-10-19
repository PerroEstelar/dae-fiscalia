#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Los cartones `ae` del Caso 1, ahora TEÑIDOS sobre una cama.

LA CORRECCION
    En la version 1 estos diez tramos eran losas blancas a cuadro completo.
    Sebastian lo marco como el cambio grande de la revision: el fondo blanco
    es, casi siempre, SOLO el titulo general de la pieza. Lo demas es carton
    teñido sobre imagen o video sostenido, lower third, o grafica de motion.

    Asi que estos ocho dejan de ocupar su ranura y pasan a V3: alfa + tinte,
    encima de una cama que corre en V1 por la ranura entera. Y los otros dos
    -la linea de tiempo y el mapa- se vuelven grafica de motion, que es la
    cuarta familia y la que Sebastian pidio expresamente («si hablan de una
    trayectoria sobre el mapa de Colombia, muestre el mapa»).

LAS CAMAS, Y POR QUE CADA UNA
    r01  calle            el enunciado de apertura, sobre la calle
    r04  manos y telefono el acuerdo se hizo por mensajes
    r07  fachada          la frase bisagra es sobre el inmueble: va sobre el
                          inmueble, con un horneado distinto al de r02
    r10  documento cajon  el documento retenido de Daniela, literal
    r15  paula se va      Paula pudo retirarse: la cama lo muestra
    r18  elena trapea     el trabajo de limpieza que cambio de condiciones
    r27  juliana umbral   entra y la interrumpen el mismo dia
    r29  manos y telefono los mensajes de Yeimi, otro horneado

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

sys.path.insert(0, "/home/claude/cartones")
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_p3c1"
os.makedirs(OUT, exist_ok=True)

# (nombre, ranura, cuadros de la ranura, spec) — mismo texto que la v1
TENIDOS = [
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
        "titulo": "Documento retenido, deuda de $3.000.000",
        "cuerpo": "Y una amenaza contra su hermano"}),
    ("ae05_paula", "r15", 195, {
        "ante": "Paula",
        "titulo": "Pagó su viaje, conservó sus documentos, administró sus ingresos",
        "cuerpo": "Podía rechazar personas, no trabajar o retirarse sin penalidad"}),
    ("ae06_cambio", "r18", 154, {
        "ante": "Elena · abril",
        "titulo": "16 horas, sin descansos",
        "cuerpo": "La remuneración entera a una deuda sin término explicado"}),
    ("ae09_interrumpido", "r27", 226, {
        "ante": "Juliana",
        "titulo": "Incorporada al sistema de deudas",
        "cuerpo": "Interrumpido el mismo día, antes de que realizara acto sexual "
                  "alguno o generara ingresos"}),
    ("ae10_mensajes", "r29", 170, {
        "ante": "Yeimi",
        "titulo": "«salió del colegio hace poco»\n«mi mamá no sabe que estoy en esto»",
        "cuerpo": "Sin cédula «todavía»"}),
]

if __name__ == "__main__":
    for nom, r, fr, spec in TENIDOS:
        C.render_carton(spec, fr, None, True,
                        "%s/P3C1_%s.mov" % (OUT, nom), con_tinte=True)
        print("%-20s %-5s %4d cuadros" % (nom, r, fr))
