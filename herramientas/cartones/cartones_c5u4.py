#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones de narracion del C5U4 «Los Ilustres».

Del tipo que repite textual al locutor. Van sobre las ranuras de FOTO, nunca
sobre las piezas de After Effects, que ya son grafica: de las 23 ranuras del
caso, 15 son de foto y 8 son de AE.

Duracion por la regla de 168 palabras por minuto, con holgura y piso de 96.
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_c5u4"
os.makedirs(OUT, exist_ok=True)

FPS = 23.976023976
PPM = 168.0


def cuadros(spec, holgura=1.15, minimo=96):
    txt = " ".join(spec.get(k, "") for k in ("ante", "titulo", "cuerpo", "suelta"))
    n = len([w for w in txt.split() if any(ch.isalnum() for ch in w)])
    return max(minimo, int(math.ceil(n / PPM * 60 * FPS * holgura)))


# (nombre, ranura, cuadros de la ranura, spec)
NARRACION = [
    # r01 mide 131 cuadros: con el cuerpo encima el carton se comia la ranura
    # entera y quedaba con dos cuadros de margen. Va solo el titulo.
    ("n01_direccion", "r01", 131, {
        "titulo": "Dirección Especializada contra la Extinción del Derecho de Dominio"}),
    ("n02_lavado", "r03", 201, {
        "titulo": "Lavado de activos y contrabando a gran escala",
        "cuerpo": "La herramienta es financiera"}),
    ("n03_medidas", "r04", 122, {
        "suelta": "Medidas sobre cinco activos"}),
    ("n04_comerciante", "r06", 208, {
        "titulo": "Un comerciante reconocido, sin antecedentes",
        "cuerpo": "Compró el hotel hace tres años"}),
    ("n05_buena_fe", "r08", 210, {
        "titulo": "Tercero de buena fe exenta de culpa",
        "cuerpo": "Y le compró a un testaferro"}),
    ("n06_setenta", "r09", 150, {
        "titulo": "Cinco estaciones de servicio, operando",
        "cuerpo": "Setenta por ciento, empresa fachada"}),
    ("n07_empleos", "r11", 183, {
        "titulo": "Ochenta empleos directos",
        "cuerpo": "Detrás de la orden sobre la totalidad"}),
    ("n08_hectareas", "r12", 139, {
        "suelta": "Ciento cincuenta hectáreas, centro de acopio"}),
    ("n09_titular", "r13", 121, {
        "suelta": "El titular murió hace veinte años"}),
    ("n10_sucesion", "r14", 151, {
        "titulo": "Nunca se abrió sucesión",
        "cuerpo": "Nadie ha respondido las citaciones"}),
    ("n11_urgencia", "r15", 159, {
        "titulo": "Doce tractocamiones afectados de urgencia",
        "cuerpo": "Suspensión del poder dispositivo y secuestro material"}),
    ("n12_legalidad", "r17", 163, {
        "titulo": "Control judicial de legalidad",
        "cuerpo": "Alegan falta de necesidad y desproporcionalidad"}),
    ("n13_colaboracion", "r18", 168, {
        "titulo": "Un plan de colaboración efectiva",
        "cuerpo": "Cuatro inmuebles que la Fiscalía no ha identificado"}),
    ("n14_testaferrato", "r19", 114, {
        "suelta": "Y delatar la red de testaferrato"}),
    ("n15_oferta", "r22", 138, {
        "suelta": "Una oferta sobre la mesa"}),
]

if __name__ == "__main__":
    print("%-20s %-6s %6s %6s %7s" % ("carton", "ranura", "carton", "ranura", "margen"))
    apretados = 0
    for n, r, fr, spec in NARRACION:
        f = cuadros(spec)
        m = fr - f
        if m < 0:
            apretados += 1
        print("%-20s %-6s %6d %6d %+7d %s" % (n, r, f, fr, m, "<-- NO CABE" if m < 0 else ""))
        C.render_carton(spec, f, None, True, "%s/C5U4_%s.mov" % (OUT, n),
                        con_tinte=True)
    print("\n%d cartones de narración, %d apretados" % (len(NARRACION), apretados))
