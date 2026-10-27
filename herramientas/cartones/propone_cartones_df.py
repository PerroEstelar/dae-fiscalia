# -*- coding: utf-8 -*-
"""Corre el proponedor sobre los cinco capitulos y deja el JSON."""
import json
import os
import sys

sys.path.insert(0, r"D:\\DAE\\_tmp\\df")
sys.path.insert(0, "D:/DAE/_repo/herramientas/prompts")
sys.path.insert(0, "D:/DAE/_repo/herramientas/voz/textos")
import cartones_pieza_df as CP

sys.path.insert(0, r'D:\\DAE\\_repo\\herramientas\\cartones')
from PIL import Image, ImageDraw
import cartones_ta as C
import apertura_verbatim_p3c5 as V

_F = C.fuente(C.F_BOLD, CP.CUERPO)
_D = ImageDraw.Draw(Image.new('RGBA', (10, 10)))


def renglones(t):
    """Cuantos renglones ocupa, al cuerpo fijo de la serie."""
    return len(V.partir(t, _F, _D))
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
    #  SI LA FRASE ES CORTA EN BOCA PERO LARGA EN PANTALLA, SE LE DA AIRE
    #      Tres cartones caian en ventanas de 116 a 147 cuadros y pedian 17
    #      caracteres por segundo. El carton puede durar un poco mas que la
    #      oracion -los del C5U4 duraban la ranura entera-, asi que se
    #      estira hasta donde deje el siguiente, con su respiro.
    elegidas.sort(key=lambda d: d['ini'])
    for k, e in enumerate(elegidas):
        tope = (elegidas[k + 1]['ini'] - CP.RESPIRO) if k + 1 < len(elegidas) \
            else e['ini'] + e['cuadros'] + 90
        comodo = int(round(len(e['frase']) / 10.0 * CP.FPS))
        e['cuadros'] = max(e['cuadros'],
                           min(comodo, tope - e['ini'], e['cuadros'] + 90))
    for e in elegidas:
        corto = CP.recorta(e['frase'], renglones, e['cuadros'])
        if corto is None:
            corto = e['frase']
        e['frase_larga'] = e['frase']
        e['frase'] = corto
        e['renglones'] = renglones(corto)
        e['densidad'] = round(len(corto) / (e['cuadros'] / CP.FPS), 1)
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
    w("C%d  %5d +%4d  %4.1f car/s  %d renglones  %3d car%s"
      % (d["cap"], d["ini"], d["cuadros"], d["densidad"], d["renglones"],
         len(d["frase"]), "  ARREGLADO" if d["arreglado"] else ""))
    w("      %s" % d["frase"])
w("")
for cap, nf, ne, fuera in resumen:
    w("--- cap %d, fuera (%d):" % (cap, len(fuera)))
    for ini, motivo, trozo in fuera:
        w("    %5d  %-34s %s" % (ini, motivo, trozo))
