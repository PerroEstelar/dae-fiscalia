# -*- coding: utf-8 -*-
r"""Exporta una situacion TAL COMO ESTA en su linea (sin remontar: Sebastian
ajusta las lineas a mano y eso no se toca).

    python exportar_sit.py A 2

master -> D:\DAE\_tmp\sit\render\SIT_A_master.mp4 ; entregas -> 05 EXPORTS\
SIT_A_v2.mp4 (receta Fiscalia) + SIT_A_v2_revision_720p.mp4 ; verificacion.
"""
import sys

sys.path.insert(0, r'D:\DAE\_repo\herramientas\montaje')
import sit_pieza as SP                                    # noqa: E402

L, v = sys.argv[1].upper(), int(sys.argv[2])
SP.VERSION = v
SP.w('=== exportar', L, 'v%d' % v, SP.nombre_linea(L))
SP.exportar(L)
SP.entregas(L, v)
SP.verificar(L, v)
SP.w('LISTO')
