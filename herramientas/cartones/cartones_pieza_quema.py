# -*- coding: utf-8 -*-
r"""Quema los cartones verbatim de la pieza entera y los deja en 02 CARTONES\PIEZA.

EL CARTON ES DE LA FRASE, NO DEL PLANO
    Entra cuando la voz empieza la oracion y sale cuando la termina,
    cruzando los cortes que haga falta. El proponedor -cartones_pieza_df-
    ya entrego cada uno con su `ini` absoluto en cuadros de la pieza.

CORRE EN LA MAQUINA DE SEBASTIAN, NO EN EL CONTENEDOR
    27 de octubre. Con 29 cartones de hasta 453 cuadros, los .mov qtrle con
    alfa suman cientos de MB y traerlos del contenedor no es viable: el
    puente escribe 30 MB por archivo. Con `fuentes/` al lado de cartones_ta
    el mismo codigo corre en los dos sitios, y aqui no hay nada que mover.

EL CUERPO SE AJUSTA A LA FRASE, NUNCA AL REVES
    De 52 a 33 por tramos hasta que el bloque cabe en ALTO_UTIL. Cortar una
    oracion para que quepa seria reescribirla, que es lo que la regla del
    verbatim prohibe. Si ni a 33 cabe, FALLA en vez de recortar.
"""
import json
import os
import sys

from PIL import Image, ImageDraw

AQUI = r"D:\DAE\_repo\herramientas\cartones"
sys.path.insert(0, AQUI)
sys.path.insert(0, "D:/DAE/_repo/herramientas/prompts")
import cartones_ta as C

AZUL_FGN = (0, 72, 144)
C.TINTE = AZUL_FGN

import apertura_verbatim_p3c5 as V
import plan_camara_df as PC

ALTO_UTIL = 470


def medida(frase, cuerpo, salto):
    f = C.fuente(C.F_BOLD, cuerpo)
    d = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    return len(V.partir(frase, f, d)) * salto


def ajusta(frase):
    """UN SOLO CUERPO PARA TODA LA SERIE.

    27 de octubre, Sebastian: «estaba usando muchos tipos de tamanos de
    letra (...) es mejor solo usar un tamano de letra y mantenerse fiel al
    extracto». Antes el cuerpo bajaba de 52 a 33 para que cupiera una
    oracion larga; eso es al reves. El cuerpo se queda en 52 y es el TEXTO
    el que se recorta, en cartones_pieza_df.recorta.

    Si aun asi no cabe, FALLA: es que el recorte no hizo su trabajo.
    """
    cuerpo = 52
    salto = int(round(cuerpo * 1.36))
    if medida(frase, cuerpo, salto) <= ALTO_UTIL:
        return cuerpo, salto
    return None, None


if __name__ == "__main__":
    ruta_json = sys.argv[1]
    todo = json.load(open(ruta_json, encoding="utf-8"))
    k = {}
    for d in todo:
        cap = d["cap"]
        k[cap] = k.get(cap, 0) + 1
        cuerpo, salto = ajusta(d["frase"])
        if cuerpo is None:
            raise SystemExit("no cabe ni a cuerpo 33: %s" % d["frase"][:60])
        n_ren = medida(d["frase"], cuerpo, salto) // salto
        y0 = int(540 - (n_ren * salto) / 2.0) + 20
        nombre = "DF_C%d_p%02d_carton.mov" % (cap, k[cap])
        dest = os.path.join(PC.RAIZ, PC.CAPS[cap], "02 CARTONES", "PIEZA")
        os.makedirs(dest, exist_ok=True)
        salida = os.path.join(dest, nombre)
        V.verbatim([(d["frase"], 0)], d["cuadros"], salida,
                   y0=y0, cuerpo=cuerpo, salto=salto)
        d["archivo"] = nombre
        print("C%d %-26s %4d cuadros  cuerpo %2d  %d renglones  %6.1f MB"
              % (cap, nombre, d["cuadros"], cuerpo, n_ren,
                 os.path.getsize(salida) / 1048576.0), flush=True)
    json.dump(todo, open(ruta_json, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("LISTO: %d cartones" % len(todo), flush=True)
