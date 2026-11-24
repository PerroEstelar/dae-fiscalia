# -*- coding: utf-8 -*-
r"""Cierre de la unidad 4 de «Delitos informáticos», Humberto Suárez Gómez (24 nov 2026). **Entrega provisional** (ver
`base_hs_profe`).

Fuente: `Cierre Unidad 4.mov`.

De «Llegamos al cierre de la cuarta y última unidad…» a «…en este curso».

**Dos cortes:**
- 71,28–126,97: dos intentos de «Cada vez que la evidencia cambie de manos…» (el primero se queda en
  «exactamente…»; el segundo vuelve a «y registrarse en la cadena de custodia», se queda en «identificar…» y
  dice «Voy a pulir»), y 32,7 s de silencio. Entra la tercera toma.
- 130,45–131,03: el «ye--» de «o se analice, ye-- ese valor» (bordes en silencio, −57 y −50 dB).

**Sin rótulo (24 nov 2026):** el nombre del profe no está confirmado (ver `base_hs_profe`). La v2 va sin rótulo y
con «24NOV» en el nombre del archivo.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_hs_profe import *  # noqa: E402,F401,F403
from base_hs_profe import armar_curso, armar_unidad, rotulo  # noqa: E402,F401

globals().update(armar_unidad('dxu4c', 4, 'CIERRE', 'Cierre Unidad 4.mov',
                              [(1.41, 71.28), (126.97, 130.45), (131.03, 209.98)]))

VERSION = 2
NOMBRE_LINEA = 'DI HS - U4 - CIERRE v2'
ITEMS = rotulo(T0 + 1.5)  # noqa: F821   # vacío: sin rótulo
