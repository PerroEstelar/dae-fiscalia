# -*- coding: utf-8 -*-
"""Corre el proponedor sobre los cinco capitulos y deja el JSON."""
import json
import os
import sys

sys.path.insert(0, r"D:\\DAE\\_tmp\\df")
sys.path.insert(0, "D:/DAE/_repo/herramientas/prompts")
sys.path.insert(0, "D:/DAE/_repo/herramientas/voz/textos")
import cartones_pieza_df as CP
import guion_df as G
import plan_camara_df as PC

ARREGLOS = {
    "activa el Mecanismo de B\u00fasqueda Urgente, de la Ley 971 de 2005, y "
    "simult\u00e1neamente la Alerta Rosa, de la Ley 2326 de 2023 y el Decreto "
    "1428 de 2024.":
    "Se activa el Mecanismo de B\u00fasqueda Urgente, de la Ley 971 de 2005, y "
    "simult\u00e1neamente la Alerta Rosa, de la Ley 2326 de 2023 y el Decreto "
    "1428 de 2024.",
}

todo, resumen = [], []
for cap in (1, 2, 3, 4, 5):
    b = os.path.join(PC.RAIZ, PC.CAPS[cap], "03 VOCES")
    rej = json.load(open(os.path.join(b, "DF_C%d_rejilla.json" % cap), encoding="utf-8"))
    textos = G.bloques(cap)
    frases = CP.frases_de_la_pieza(rej, textos)
    elegidas, fuera = CP.escoge(frases, ARREGLOS)
    for e in elegidas:
        e["cap"] = cap
    todo += elegidas
    resumen.append((cap, len(frases), len(elegidas), fuera))

json.dump(todo, open(r"D:\\DAE\\_tmp\\df\\cartones_pieza_df.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

def w(x):
    sys.stdout.write(x.encode("ascii", "replace").decode("ascii") + "\n")

for cap, nf, ne, fuera in resumen:
    w("cap %d: %d oraciones, %d cartones" % (cap, nf, ne))
w("")
for d in todo:
    w("C%d  %5d +%4d  %4.1f car/s%s" % (d["cap"], d["ini"], d["cuadros"],
                                        d["densidad"], "  ARREGLADO" if d["arreglado"] else ""))
    w("      %s" % d["frase"])
w("")
for cap, nf, ne, fuera in resumen:
    w("--- cap %d, fuera (%d):" % (cap, len(fuera)))
    for ini, motivo, trozo in fuera:
        w("    %5d  %-34s %s" % (ini, motivo, trozo))
