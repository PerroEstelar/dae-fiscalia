#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones de narracion del C5U2 «El siniestro vial».

Del tipo que Sebastian pidio: repiten TEXTUAL lo que dice el locutor, para que
la grafica no vaya por un lado y la voz por otro.

La duracion no se calcula a ojo: 168 palabras por minuto, que es una lectura
comoda de texto denso en pantalla.  cuadros = palabras / 168 * 60 * 23,976,
o sea palabras * 8,56.  Se cuenta y se redondea hacia arriba con holgura.

Van sobre las ranuras de FOTO, nunca sobre las piezas de After Effects, que ya
son grafica.
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_c5u2"
os.makedirs(OUT, exist_ok=True)

FPS = 23.976023976
PPM = 168.0


def cuadros(spec, holgura=1.15, minimo=96):
    """Cuadros que pide el texto a 168 ppm, con holgura y un piso."""
    txt = " ".join(spec.get(k, "") for k in ("ante", "titulo", "cuerpo", "suelta"))
    n = len([w for w in txt.split() if any(ch.isalnum() for ch in w)])
    return max(minimo, int(math.ceil(n / PPM * 60 * FPS * holgura)))


# (nombre, ranura sobre la que va, spec)
NARRACION = [
    ("n01_frenos", "r01", {
        "titulo": "Un vehículo de carga pesada pierde los frenos",
        "cuerpo": "La falla es catastrófica. El siniestro es masivo."}),
    ("n02_victimas", "r02", {
        "titulo": "Tres personas muertas",
        "cuerpo": "Dos con discapacidad física permanente\n"
                  "Un menor que perdió a sus padres\n"
                  "Un adulto mayor en incapacidad absoluta"}),
    ("n03_imputacion", "r03", {
        "titulo": "Formulación de imputación contra el conductor",
        "cuerpo": "que es además el propietario del automotor"}),
    ("n04_cautelares", "r04", {
        "ante": "Lo que piden",
        "titulo": "Medidas cautelares sobre el patrimonio",
        "cuerpo": "Lo piden el apoderado de las víctimas\ny el Ministerio Público"}),
    ("n05_licito", "r06", {
        "titulo": "Todo lo que lo compone es de origen lícito",
        "cuerpo": "Frente a esa cifra hay un patrimonio."}),
    # Sebastian marco el 1:14 como confuso. El carton metia tres ideas en dos
    # lineas unidas por un punto medio -credito pagado / avaluo / ahi vive- y
    # "millones" se quedaba huerfano en una linea propia. Ahora el hecho
    # juridico va en el titulo y el cuerpo lleva una idea por linea.
    ("n06_casa", "r07", {
        "titulo": "Una casa en un sector residencial",
        "cuerpo": "Crédito hipotecario ya pagado\n"
                  "Avaluada en novecientos millones de pesos\n"
                  "Ahí vive, hoy, su familia"}),
    # "Ciento ochenta millones" a secas, sin verbo, no se leia como frase.
    ("n07_camioneta", "r08", {
        "titulo": "Una camioneta de uso personal",
        "cuerpo": "Avaluada en ciento ochenta millones de pesos"}),
    ("n08_flota", "r10", {
        "titulo": "No pide el cuarenta por ciento",
        "cuerpo": "Pide embargar las cuentas de la sociedad\n"
                  "y congelar la flota completa"}),
    # las tres ranuras mas cortas de la rejilla (149, 127 y 132 cuadros) no dan
    # para un carton de dos bloques: a 168 ppm no alcanzaria a leerse. Van de
    # una sola linea, como el "Antes, no durante." del Caso A.
    ("n09_vender", "r13", {
        "suelta": "La defensa pide autorización para vender la camioneta"}),
    ("n10_poliza", "r15", {
        "suelta": "No tienen con qué pagar una póliza judicial"}),
    ("n11_caucion", "r16", {
        "ante": "Lo que pide el Ministerio Público",
        "titulo": "Embargo y secuestro sin exigir caución"}),
    ("n12_venta", "r18", {
        "suelta": "Una caución que nadie puede pagar"}),
]

if __name__ == "__main__":
    tot = 0
    for n, ran, spec in NARRACION:
        f = cuadros(spec)
        tot += f
        C.render_carton(spec, f, None, True, "%s/C5U2_%s.mov" % (OUT, n),
                        con_tinte=True)
        print("%-18s %-4s %4d cuadros  %5.1f s" % (n, ran, f, f / FPS))
    print("%d cartones de narración" % len(NARRACION))
