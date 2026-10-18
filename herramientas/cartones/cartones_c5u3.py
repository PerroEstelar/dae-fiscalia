#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones de narracion del C5U3 «Eslabon Financiero».

Del tipo que repite textual al locutor. Van sobre las ranuras de FOTO, nunca
sobre las piezas de After Effects, que ya son grafica.

Duracion por la regla de 168 palabras por minuto, con holgura y piso de 96.
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_c5u3"
os.makedirs(OUT, exist_ok=True)

FPS = 23.976023976
PPM = 168.0


def cuadros(spec, holgura=1.15, minimo=96):
    txt = " ".join(spec.get(k, "") for k in ("ante", "titulo", "cuerpo", "suelta"))
    n = len([w for w in txt.split() if any(ch.isalnum() for ch in w)])
    return max(minimo, int(math.ceil(n / PPM * 60 * FPS * holgura)))


# (nombre, ranura, cuadros de la ranura, spec)
NARRACION = [
    ("n01_investigacion", "r01", 173, {
        "titulo": "La Fiscalía Seccional y el CTI",
        "cuerpo": "adelantan una investigación"}),
    ("n02_allanamiento", "r04", 193, {
        "titulo": "Orden de registro y allanamiento",
        "cuerpo": "Eslabón Financiero S.A.S."}),
    ("n03_diligencia", "r06", 146, {
        "suelta": "Todos salen de la misma diligencia"}),
    ("n04_vehiculos", "r07", 188, {
        "titulo": "Ocho vehículos industriales de transporte",
        "cuerpo": "aprehendidos físicamente durante la diligencia"}),
    ("n05_instrumentos", "r08", 187, {
        "titulo": "Presuntos instrumentos",
        "cuerpo": "para la movilización de recursos no justificados"}),
    ("n06_bodega", "r09", 161, {
        "titulo": "Bodega y centro logístico",
        "cuerpo": "Propiedad raíz del investigado"}),
    ("n07_repuestos", "r10", 207, {
        "titulo": "En el primer piso, un local de repuestos",
        "cuerpo": "registrado a nombre de un comerciante externo"}),
    ("n08_servidores", "r12", 238, {
        "titulo": "Quince servidores de criptoactivos y minería digital",
        "cuerpo": "hallados en la bodega"}),
    ("n09_efectivo", "r14", 174, {
        "titulo": "Quinientos millones en efectivo",
        "cuerpo": "capturados en la oficina del investigado"}),
    ("n10_contabilidad", "r15", 186, {
        "titulo": "Los computadores con el software contable",
        "cuerpo": "La evidencia de la contabilidad paralela"}),
    ("n11_apartamentos", "r17", 202, {
        "titulo": "Dos inmuebles residenciales, sin ocupar",
        "cuerpo": "registrados a nombre del investigado"}),
    ("n12_disponer", "r18", 165, {
        "suelta": "Impedir jurídicamente que sean vendidos o gravados"}),
    ("n13_valor", "r20", 193, {
        "titulo": "Pierden valor cada mes que pasan guardados",
        "cuerpo": "Dinero en efectivo y, junto a él, la prueba"}),
]

if __name__ == "__main__":
    print("%-20s %-4s %6s %6s %7s" % ("carton", "ran", "carton", "ranura", "margen"))
    mal = 0
    for n, r, rf, spec in NARRACION:
        f = cuadros(spec)
        m = rf - f
        if m < 24:
            mal += 1
        print("%-20s %-4s %6d %6d %+7d %s" % (n, r, f, rf, m, "" if m >= 24 else "*** APRETADO ***"))
        C.render_carton(spec, f, None, True, "%s/C5U3_%s.mov" % (OUT, n), con_tinte=True)
    print("%d cartones de narración, %d apretados" % (len(NARRACION), mal))
