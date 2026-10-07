#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-renderiza los cartones de preguntas a la duración MEDIDA de cada pregunta.

Las duraciones de antes salieron de la fórmula. Estas salen de `silencedetect`
sobre las pistas de voz reales: cada cartón dura exactamente lo que dura su
pregunta en boca del narrador, ni un cuadro más.

El mapeo silencio → pregunta se verificó contra el conteo de caracteres de cada
frase; los silencios intra-frase (comas, enumeraciones) se descartaron.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartones_ta as C
import cartones_c02 as C02
import cartones_c06 as C06
import cartones_c08 as C08

OUT = "/mnt/user-data/outputs/cartones_voz"
os.makedirs(OUT, exist_ok=True)

# cuadros medidos, en orden (intro + preguntas)
MEDIDO = {
    "02": [230, 137, 106, 83, 137, 186, 186],
    "06": [164, 122, 218, 94, 149, 128, 104, 248],
    "08": [139, 66, 123, 164, 135],
}
FUENTE = {"02": C02.PREGUNTAS, "06": C06.PREGUNTAS, "08": C08.PREGUNTAS}

if __name__ == "__main__":
    casos = sys.argv[1:] or ["02", "06", "08"]
    for caso in casos:
        lista, dur = FUENTE[caso], MEDIDO[caso]
        assert len(lista) == len(dur), (caso, len(lista), len(dur))
        for (nombre, _viejo, spec), n in zip(lista, dur):
            C.render_carton(spec, n, None, True,
                            f"{OUT}/TA{caso}_{nombre}.mov", con_tinte=True)

    if "02" in casos:
        # El gráfico A va bajo la frase de la oferta: 285 cuadros medidos.
        # Las entradas se reparten sobre la nueva duración, no sobre la vieja.
        C02.grafico(285, f"{OUT}/TA02_grafico_la_propuesta.mov", False, (8, 36, 52, 182, -1))
        # El gráfico B va bajo "¿se cumple el reintegro mínimo del 50 %?": 83.
        C02.grafico(83, f"{OUT}/TA02_grafico_el_50_por_ciento.mov", True, (2, 6, 10, 10, 30))
