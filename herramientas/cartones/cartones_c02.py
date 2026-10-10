#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cartones del Caso 02 · el doble beneficio y el reintegro, versión verbatim.

Las preguntas son literales del guion del profesor, con sus cifras tal como él
las escribió. Los dos gráficos muestran únicamente números que están en su texto.
"""
import os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import cartones_ta as C

OUT = "/mnt/user-data/outputs/cartones_c02"
os.makedirs(OUT, exist_ok=True)

PREGUNTAS = [
    ("p0_el_fiscal_determina", 243, {
        "titulo": "El o la fiscal debe determinar si es procedente celebrar el preacuerdo",
        "cuerpo": "Para ello debe contestar las siguientes preguntas:"}),
    ("p1_es_viable", 132, {
        "titulo": "¿Es viable, para la Fiscalía, celebrar el preacuerdo propuesto en esos términos?"}),
    ("p2_esta_acreditado", 91, {
        "titulo": "¿Está acreditado el incremento patrimonial de $400 millones?"}),
    ("p3_reintegro_minimo", 91, {
        "titulo": "¿Se cumple el reintegro mínimo del 50 %?"}),
    ("p4_la_garantia", 111, {
        "titulo": "¿La garantía ofrecida permite asegurar razonablemente el recaudo del remanente?"}),
    ("p5_puede_negociar", 172, {
        "titulo": "¿Puede el fiscal negociar a partir de ese momento consecuencias jurídicas más beneficiosas susceptibles de negociación?"}),
    ("p6_reintegro_inferior", 213, {
        "titulo": "¿Podría el fiscal aceptar un reintegro inferior al 50 % a cambio de una anuencia de responsabilidad más amplia?"}),
]


# Cartones sobre la narración, calzados al tramo de voz medido con
# `silencedetect` sobre TA02_NARRADOR.wav. Eran tres y los alargaste a mano
# cortándolos en pedazos porque la animación vieja se comía los extremos; con
# la animación corta ya no hace falta: cada cartón mide lo que mide su frase.
# Los dos cartones de cifra entran en el cuadro en que se dice la cifra, no al
# principio de la frase —eso lo tomé de cómo colocaste tú el de $120 millones.
# El último párrafo no lleva cartón: ahí va el gráfico de la propuesta en V1.
NARRACION = [
    ("n1_los_dos", 132, {
        "titulo": "Carlos, funcionario de una entidad pública",
        "cuerpo": "Andrés, representante de una empresa contratista"}),
    ("n2_medios", 91, {
        "titulo": "De acuerdo con los medios cognoscitivos recaudados"}),
    ("n3_la_posicion", 179, {
        "titulo": "Carlos habría utilizado su posición para favorecer la adjudicación de un contrato de suministro de equipos médicos"}),
    ("n4_120_millones", 112, {"suelta": "$120 millones"}),
    ("n5_concertada", 166, {
        "titulo": "Como consecuencia de la actuación concertada, la empresa contratista obtuvo un incremento patrimonial ilícito"}),
    ("n6_400_millones", 82, {"suelta": "$400 millones"}),
    ("n7_la_defensa", 147, {
        "titulo": "La defensa de Andrés manifiesta a la Fiscalía su interés en celebrar un preacuerdo"}),
    ("n8_propone", 160, {
        "titulo": "Propone aceptar responsabilidad a cambio de negociar una consecuencia jurídica más favorable"}),
]

def grafico(nframes, salida, con_marca_50, entradas):
    """La aritmética de la propuesta. Solo cifras que están en el texto del profesor.

    `entradas` son los frames en que entra cada cosa, medidos contra la locución.
    """
    X0, X1 = 249, 1670
    BY, BH = 596, 92
    ANCHO = X1 - X0
    OFRECIDO = ANCHO // 4
    MITAD = ANCHO // 2
    GRIS = (226, 229, 233)
    NAVY = C.AZUL_NOCHE

    f_barra, f_ofrecido, f_lab_izq, f_lab_der, f_marca = entradas

    f_cif = C.fuente(C.F_BOLD, 40)
    f_pie = C.fuente(C.F_MED, 32)
    f_mar = C.fuente(C.F_BOLD, 34)

    pr = subprocess.Popen(
        ["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
         "-s", f"{C.W}x{C.H}", "-r", C.FPS, "-i", "-", "-c:v", "libx264", "-preset", "veryfast",
         "-crf", "14", "-pix_fmt", "yuv420p", "-g", "600", "-keyint_min", "600",
         "-sc_threshold", "0", salida], stdin=subprocess.PIPE)

    def ap(f, inicio, dur=12):
        return 0.0 if f < inicio or inicio < 0 else min(1.0, C.ease_out_cubic((f - inicio) / dur))

    for f in range(nframes):
        im = Image.new("RGB", (C.W, C.H), C.BLANCO_FONDO)
        d = ImageDraw.Draw(im, "RGBA")
        fuera = max(0.0, 1 - (f - (nframes - 12)) / 12) if f > nframes - 12 else 1.0

        def col(rgb, a):
            return rgb + (int(255 * max(0.0, min(1.0, a * fuera))),)

        k = C.ease_out_cubic(min(1.0, max(0.0, (f - 2) / 10)))
        if k > 0:
            d.rectangle([C.BAR_X, BY - 150, C.BAR_X + C.BAR_W - 1, BY - 150 + int(290 * k)],
                        fill=col(C.BAR_C[:3], 1))

        a = ap(f, f_barra, 14)
        if a > 0:
            d.rectangle([X0, BY, X0 + int(ANCHO * a), BY + BH], fill=col(GRIS, 1))
            d.text((X0, BY - 112), "Incremento patrimonial ilícito · $400 millones",
                   font=f_pie, fill=col(NAVY, a * 0.85))

        a = ap(f, f_ofrecido, 16)
        if a > 0:
            d.rectangle([X0, BY, X0 + int(OFRECIDO * a), BY + BH], fill=col(NAVY, 1))

        a = ap(f, f_lab_izq)
        if a > 0:
            d.text((X0, BY + BH + 26), "$100 millones", font=f_cif, fill=col(NAVY, a))
            d.text((X0, BY + BH + 76), "que ofrece reintegrar", font=f_pie, fill=col(NAVY, a * 0.75))

        a = ap(f, f_lab_der)
        if a > 0:
            d.text((X0 + OFRECIDO + 40, BY + BH + 26), "$300 millones", font=f_cif, fill=col(NAVY, a))
            d.text((X0 + OFRECIDO + 40, BY + BH + 76), "en un plazo de cinco años",
                   font=f_pie, fill=col(NAVY, a * 0.75))

        if con_marca_50:
            a = ap(f, f_marca, 16)
            if a > 0:
                x = X0 + MITAD
                d.rectangle([x - 3, BY - 54, x + 3, BY - 54 + int((BH + 70) * a)],
                            fill=col(C.BAR_C[:3], 1))
                d.text((x + 22, BY - 58), "reintegro mínimo", font=f_pie, fill=col(NAVY, a * 0.8))
                d.text((x + 22, BY - 22), "50 %", font=f_mar, fill=col(NAVY, a))

        pr.stdin.write(im.tobytes())

    pr.stdin.close(); pr.wait()
    print(os.path.basename(salida), nframes, "f", os.path.getsize(salida) // 1024, "KB")


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "todo"

    if modo in ("todo", "preguntas"):
        for nombre, n, spec in PREGUNTAS:
            C.render_carton(spec, n, None, True, f"{OUT}/TA02_{nombre}.mov", con_tinte=True)

    if modo in ("todo", "blancos"):
        C.render_carton({"ante": "Caso:", "titulo": "“El doble beneficio y el reintegro”"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA02_carton_entrada.mov", con_marca=True)
        C.render_carton({"suelta": "¿Podría el fiscal aceptar un reintegro inferior al 50 %?"},
                        119, C.BLANCO_FONDO, False, f"{OUT}/TA02_carton_cierre.mov", con_marca=True)

    if modo in ("todo", "graficos"):
        # A · bajo la narración. La marca del 50 % todavía no: esa es una pregunta.
        grafico(320, f"{OUT}/TA02_grafico_la_propuesta.mov", False, (8, 40, 58, 205, -1))
        # B · bajo la pregunta del reintegro mínimo. La barra ya existe para el espectador.
        grafico(91, f"{OUT}/TA02_grafico_el_50_por_ciento.mov", True, (2, 6, 10, 10, 34))
