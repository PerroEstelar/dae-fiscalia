# -*- coding: utf-8 -*-
r"""Rutas del curso «Justicia restaurativa» (PRIORIDAD 1).

EL ARBOL, IGUAL EN DISCO Y EN LOS BINS DE RESOLVE
    E:\DAE MASTER\PRIORIDAD 1\CURSO - JUSTICIA RESTAURATIVA\
      00 DOCUMENTOS FUENTE\        los cinco documentos del Drive (.md) y el .pptx
      00 PERSONAJES\               hojas de personaje (+ _crudos)
      CASO 1 - Una discusion en un sitio publico\
      CASO 2 - Fase 1 La historia\
      UNIDAD 1 - El encuentro en la carretera\
      UNIDAD 2 - La situacion reflexiva\
      UNIDAD 3 - Prosigue la situacion reflexiva\
      UNIDAD 4 - Culminamos la situacion\

    Dentro de cada pieza van las MISMAS diez carpetas de Gerencia judicial,
    del P3 y de las situaciones de Desaparicion Forzada.

    En Resolve (proyecto DAE MASTER - CURSOS): PRIORIDAD 1 › CURSO - JUSTICIA
    RESTAURATIVA › <pieza> › 01 PLANOS · 02 CARTONES · 03 VOCES · 04 B-ROLL ·
    05 EXPORTS · 07 MOVIMIENTO · 08 MUSICA · 10 TIMELINE SEBASTIAN. La linea
    de cada pieza vive en su 10 TIMELINE SEBASTIAN.

    «PRIORIDAD 1» ya existe en disco con «PROFE CARLOS HUMBERTO» adentro (los
    seis casos del SRPA que se corrigieron el 28 oct): este curso es su
    vecino, no lo toca.
"""
import os

from guion_jr import TEMAS

MASTER = r'E:\DAE MASTER'
RAIZ = os.path.join(MASTER, 'PRIORIDAD 1', 'CURSO - JUSTICIA RESTAURATIVA')
FUENTE = os.path.join(RAIZ, '00 DOCUMENTOS FUENTE')
PERSONAJES = os.path.join(RAIZ, '00 PERSONAJES')

SUB_VIDEO = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL', '05 EXPORTS',
             '06 GUION Y STORYBOARD', '07 MOVIMIENTO', '08 MUSICA',
             '09 A LA VOZ', '10 TIMELINE SEBASTIAN']
BINS_VIDEO = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL',
              '05 EXPORTS', '07 MOVIMIENTO', '08 MUSICA',
              '10 TIMELINE SEBASTIAN']
BIN_RAIZ = ['PRIORIDAD 1', 'CURSO - JUSTICIA RESTAURATIVA']

TMP = r'D:\DAE\_tmp\jr'


def carpeta(clave):
    return os.path.join(RAIZ, TEMAS[clave][0])


def sub(clave, cual):
    return os.path.join(carpeta(clave), cual)


def voces(clave):
    return sub(clave, '03 VOCES')
