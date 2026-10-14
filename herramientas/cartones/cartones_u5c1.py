#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones de SRPA Unidad 5 - Los Chapulines.

Misma reticula y misma animacion que `cartones_ta.py`; aqui solo va el
contenido. Los tipos penales son texto en pantalla y nunca locucion, que es la
regla de la serie para el vocabulario que trabaria los filtros de voz.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_u5c1"
os.makedirs(OUT, exist_ok=True)

# (nombre, frames, spec) - cartones de narracion, con tinte
NARRACION = [
    ("n1_hurto",      96, {"titulo": "Hurto calificado y agravado"}),
    ("n2_cifra",     120, {"ante": "Lo sustraído en el periodo",
                           "titulo": "Ciento treinta millones de pesos"}),
    ("n3_sexuales",  168, {"titulo": "Actos sexuales violentos",
                           "cuerpo": "Acceso carnal violento"}),
    ("n4_yos",        48, {"ante": "Yos", "titulo": "Dieciséis años"}),
    ("n5_yefry",      48, {"ante": "Yefry", "titulo": "Diecisiete años"}),
    ("n6_juanes",     48, {"ante": "Juanes", "titulo": "Catorce años"}),
    ("n7_eventos",   150, {"titulo": "Cinco eventos delictivos",
                           "cuerpo": "atribuidos a los tres, en el mismo periodo"}),
    ("n8_ley",       168, {"titulo": "Ley 1098 de 2006",
                           "cuerpo": "Sistema de Responsabilidad Penal para Adolescentes"}),
    ("n9_uno",       204, {"ante": "Uno", "titulo": "La edad al momento de los hechos"}),
    ("n10_dos",      162, {"ante": "Dos", "titulo": "La gravedad de las conductas atribuidas"}),
    ("n11_tres",     170, {"ante": "Tres", "titulo": "La permanencia",
                           "cuerpo": "dos años y cuatro meses"}),
]

# los dos cartones de pausa: ocupan la pantalla, sin voz.
# El cuerpo lleva saltos de linea explicitos: una opcion por renglon.
PAUSA = [
    ("p1_votacion", 192, {
        "ante": "Votación",
        "titulo": "Los mismos cinco hechos se atribuyen a Yos, de dieciséis, "
                  "a Yefry, de diecisiete, y a Juanes, de catorce. "
                  "¿Procede la misma respuesta del sistema para los tres?",
        "cuerpo": "a)  Sí: la responsabilidad es la misma porque la organización "
                  "y los hechos son los mismos.\n"
                  "b)  No: la edad al momento de los hechos modifica la respuesta aplicable.\n"
                  "c)  Depende de la conducta concreta que se le atribuya a cada uno."}),
    ("p2_foro", 192, {
        "ante": "Tarea del foro",
        "titulo": "Redacte, para uno de los tres adolescentes, el fundamento "
                  "de la respuesta que considere aplicable",
        "cuerpo": "indicando qué hechos del expediente la sostienen y qué papel "
                  "juega su edad al momento de los hechos."}),
]

if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "todo"

    if modo in ("todo", "narracion"):
        for nombre, n, spec in NARRACION:
            C.render_carton(spec, n, None, True, "%s/U5C1_%s.mov" % (OUT, nombre),
                            con_tinte=True)

    if modo in ("todo", "pausa"):
        for nombre, n, spec in PAUSA:
            C.render_carton(spec, n, None, True, "%s/U5C1_%s.mov" % (OUT, nombre),
                            con_tinte=True)

    if modo in ("todo", "blancos"):
        C.render_carton({"ante": "Caso", "titulo": "«Los Chapulines»"},
                        119, C.BLANCO_FONDO, False,
                        "%s/U5C1_carton_entrada.mov" % OUT, con_marca=True)
        C.render_carton({"ante": "Caso", "titulo": "«Los Chapulines»"},
                        119, C.BLANCO_FONDO, False,
                        "%s/U5C1_carton_cierre.mov" % OUT, con_marca=True)
