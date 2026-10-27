# -*- coding: utf-8 -*-
r"""Vuelve a armar las cinco lineas con el armador v2.

QUE CAMBIA RESPECTO DE LO QUE SEBASTIAN VIO
    - Ya no queda un cuadro negro en cada corte: `endFrame` no es inclusivo.
    - Las ranuras vienen rehorneadas SIN empuje de camara.
    - Los cartones verbatim pasan de seis a veintinueve y cubren el 51 %% de
      la serie: cada uno dura lo que la voz tarda en decir su oracion.
    - Entran los diez lower thirds.
    - La musica va en A5, que es la unica pista que llega al bus principal.

    La linea anterior NO se borra: se le cambia el nombre y se queda en el
    proyecto por si hay algo a mano que rescatar.
"""
import json
import os
import sys

sys.path.insert(0, r"D:\DAE\_tmp\df")
sys.path.insert(0, "D:/DAE/_repo/herramientas/prompts")
import linea_df_v2 as L
import plan_camara_df as PC

import DaVinciResolveScript as dvr

resolve = dvr.scriptapp("Resolve")
pr = resolve.GetProjectManager().GetCurrentProject()

cartones = json.load(open(r"D:\DAE\_tmp\df\cartones_pieza_df.json",
                          encoding="utf-8"))
sin_archivo = [c for c in cartones if not c.get("archivo")]
if sin_archivo:
    raise SystemExit("%d cartones sin quemar" % len(sin_archivo))

# El nombre canonico sale de PC.CAPS, no de lo que haya en el proyecto:
# una corrida fallida deja la linea renombrada a '(anterior)' y entonces
# el nombre limpio ya no existe para buscarlo.
nombres = {c: 'DF C%d %s' % (c, PC.CAPS[c].split(' - ', 1)[1])
           for c in PC.CAPS}

for cap in [int(a) for a in sys.argv[1:]] or [1, 2, 3, 4, 5]:
    tl, err = L.construye(resolve, cap, nombres[cap], cartones)
    largo = (tl.GetEndFrame() - tl.GetStartFrame()) if tl else -1
    print("cap %d  %-52s largo %d  %s"
          % (cap, nombres[cap][:52], largo, err or "OK"), flush=True)
    if err:
        raise SystemExit(err)
    v = [(i, tl.GetTrackName("video", i),
          len(tl.GetItemListInTrack("video", i)))
         for i in range(1, tl.GetTrackCount("video") + 1)]
    a = [(i, tl.GetTrackName("audio", i),
          len(tl.GetItemListInTrack("audio", i)))
         for i in range(1, tl.GetTrackCount("audio") + 1)]
    print("      %s" % [x for x in v if x[2]], flush=True)
    print("      %s" % [x for x in a if x[2]], flush=True)
resolve.GetProjectManager().SaveProject()
print("MONTAJE LISTO", flush=True)
