"""Activaciones provisionales por proporción de caracteres (1,6 cuadros/carácter).
Se reemplazan por las medidas sobre la voz real (rejilla/calzar.py de la casa)."""
import json, sys
FPC = 1.6
def plan(texto, claves, cola=36):
    n = int(len(texto) * FPC) + cola
    return n, [int(texto.index(k) * FPC) + 6 for k in claves]
if __name__ == '__main__':
    t, claves = sys.argv[1], json.loads(sys.argv[2])
    print(json.dumps(plan(t, claves)))
