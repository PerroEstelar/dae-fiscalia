# -*- coding: utf-8 -*-
r"""Rutas del curso «Enfoque diferencial en la práctica del fiscal»
(PRIORIDAD 2).

EL ARBOL, IGUAL EN DISCO Y EN LOS BINS DE RESOLVE
    E:\DAE MASTER\PRIORIDAD 2\CURSO - ENFOQUE DIFERENCIAL\
      00 DOCUMENTOS FUENTE\        los cinco documentos del Drive (.md)
      00 PERSONAJES\               hojas de personaje (+ _crudos, _piel_ref)
      VIDEOS\                      los cinco casos (no son de ninguna unidad)
        CASO 1 - Edgar Molano\ ...

    Cada caso: las MISMAS diez carpetas de toda la serie.

    En Resolve (proyecto DAE MASTER - CURSOS): PRIORIDAD 2 › CURSO - ENFOQUE
    DIFERENCIAL › VIDEOS › <caso> › los bins. «PRIORIDAD 2» ya existe con
    Gerencia judicial y Derechos humanos adentro: este curso es su vecino.

    PRIORIDAD 0X / X (Sebastián, 3 nov): si conviven «PRIORIDAD 2» y
    «PRIORIDAD 02» se funden en la de un dígito. Medido ese día en disco y en
    el pool: no hay ningún par duplicado (solo «PRIORIDAD 03», sin «3»).
"""
import os

from guion_ed import PIEZAS, UNIDADES

MASTER = r'E:\DAE MASTER'
RAIZ = os.path.join(MASTER, 'PRIORIDAD 2', 'CURSO - ENFOQUE DIFERENCIAL')
FUENTE = os.path.join(RAIZ, '00 DOCUMENTOS FUENTE')
PERSONAJES = os.path.join(RAIZ, '00 PERSONAJES')

SUB_VIDEO = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL', '05 EXPORTS',
             '06 GUION Y STORYBOARD', '07 MOVIMIENTO', '08 MUSICA',
             '09 A LA VOZ', '10 TIMELINE SEBASTIAN']
SUB_IMAGEN = []
BINS_VIDEO = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL',
              '05 EXPORTS', '07 MOVIMIENTO', '08 MUSICA',
              '10 TIMELINE SEBASTIAN']
BINS_IMAGEN = []
BIN_RAIZ = ['PRIORIDAD 2', 'CURSO - ENFOQUE DIFERENCIAL']

TMP = r'D:\DAE\_tmp\ed'


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
