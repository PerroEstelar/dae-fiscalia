# -*- coding: utf-8 -*-
r"""Rutas del curso «Gerencia judicial» (PRIORIDAD 2).

EL ARBOL, IGUAL EN DISCO Y EN LOS BINS DE RESOLVE
    E:\DAE MASTER\PRIORIDAD 2\CURSO - GERENCIA JUDICIAL\
      00 DOCUMENTOS FUENTE\        el documento del Drive (.docx) y su .md
      00 PERSONAJES\               hojas de personaje (+ _crudos)
      TEMA 1 - El despacho de los 2000 casos\
      TEMA 3 - Aceptar o negociar\
      TEMA 4 - Dos situaciones al comenzar la semana\

    Dentro de cada tema van las MISMAS diez carpetas de un capitulo del P3 y
    de las situaciones de Desaparicion Forzada, con los mismos numeros.

    En Resolve (proyecto DAE MASTER - CURSOS): PRIORIDAD 2 › CURSO - GERENCIA
    JUDICIAL › TEMA n › 01 PLANOS · 02 CARTONES · 03 VOCES · 04 B-ROLL ·
    05 EXPORTS · 07 MOVIMIENTO · 08 MUSICA · 10 TIMELINE SEBASTIAN (con
    RANURAS, RESPIRO, MOVIMIENTO y DETALLE). La linea de cada tema vive en su
    10 TIMELINE SEBASTIAN.
"""
import os

from guion_gj import TEMAS

MASTER = r'E:\DAE MASTER'
RAIZ = os.path.join(MASTER, 'PRIORIDAD 2', 'CURSO - GERENCIA JUDICIAL')
FUENTE = os.path.join(RAIZ, '00 DOCUMENTOS FUENTE')
PERSONAJES = os.path.join(RAIZ, '00 PERSONAJES')

SUB_VIDEO = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL', '05 EXPORTS',
             '06 GUION Y STORYBOARD', '07 MOVIMIENTO', '08 MUSICA',
             '09 A LA VOZ', '10 TIMELINE SEBASTIAN']
BINS_VIDEO = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL',
              '05 EXPORTS', '07 MOVIMIENTO', '08 MUSICA',
              '10 TIMELINE SEBASTIAN']
BIN_RAIZ = ['PRIORIDAD 2', 'CURSO - GERENCIA JUDICIAL']

TMP = r'D:\DAE\_tmp\gj'


def carpeta(clave):
    return os.path.join(RAIZ, TEMAS[clave][0])


def sub(clave, cual):
    return os.path.join(carpeta(clave), cual)


def voces(clave):
    return sub(clave, '03 VOCES')
