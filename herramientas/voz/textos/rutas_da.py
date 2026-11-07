# -*- coding: utf-8 -*-
r"""Rutas de las piezas de Sebastián del curso «Investigación y
judicialización de delitos contra el medio ambiente y los recursos naturales»
(PRIORIDAD 3).

EL CURSO YA EXISTÍA EN DISCO: `E:\DAE MASTER\CURSO 2 - DELITOS CONTRA EL MEDIO
AMBIENTE` tiene las introducciones de unidad (el profesor en cuadro, UNIDAD 1..5)
desde octubre. Las piezas nuevas entran ahí mismo, en su unidad, para que el
curso viva en un solo sitio (7 nov):

    CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE\
      00 DOCUMENTOS FUENTE\    el PDF del curso y los insumos
      00 PERSONAJES\           hojas de personaje
      00 ANCLAS DE ESTILO\     placas de referencia de estilo
      UNIDAD 1\VIDEO 01 - ...\
      UNIDAD 3\VIDEO 02 - ...\  VIDEO 03 - ...\
      UNIDAD 4\VIDEO 04 - ...\  VIDEO 05 - ...\  VIDEO 06 - ...\
        las diez carpetas de la serie, con 09 MOTION GRAPHICS en vez de
        09 A LA VOZ.
"""
import os

from guion_da import PIEZAS, UNIDADES

MASTER = r'E:\DAE MASTER'
RAIZ = os.path.join(MASTER, 'CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE')
FUENTE = os.path.join(RAIZ, '00 DOCUMENTOS FUENTE')
PERSONAJES = os.path.join(RAIZ, '00 PERSONAJES')
ANCLAS = os.path.join(RAIZ, '00 ANCLAS DE ESTILO')

SUB_VIDEO = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL', '05 EXPORTS',
             '06 GUION Y STORYBOARD', '07 MOVIMIENTO', '08 MUSICA',
             '09 MOTION GRAPHICS', '10 TIMELINE SEBASTIAN']
BINS_VIDEO = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL',
              '05 EXPORTS', '07 MOVIMIENTO', '08 MUSICA', '09 MOTION GRAPHICS',
              '10 TIMELINE SEBASTIAN']
BIN_RAIZ = ['CURSO 2 - DELITOS CONTRA EL MEDIO AMBIENTE']

TMP = r'D:\DAE\_tmp\da'


def unidad(n):
    return os.path.join(RAIZ, UNIDADES[n])


def carpeta(clave):
    tipo, n, nombre = PIEZAS[clave][:3]
    return os.path.join(unidad(n), nombre)


def sub(clave, cual):
    return os.path.join(carpeta(clave), cual)


def voces(clave):
    return sub(clave, '03 VOCES')


def bins(clave):
    tipo, n, nombre = PIEZAS[clave][:3]
    return BIN_RAIZ + [UNIDADES[n], nombre]
