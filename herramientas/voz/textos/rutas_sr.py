# -*- coding: utf-8 -*-
r"""Rutas de los CASOS del curso «Sistema de responsabilidad penal para
adolescentes y justicia restaurativa» (PRIORIDAD 1).

EL CURSO YA EXISTE EN DISCO (11 nov, videos de profes):
    E:\DAE MASTER\PRIORIDAD 1\CURSO - SRPA Y JUSTICIA RESTAURATIVA\
      00 MOTION GRAPHICS\        el AEP del curso (SRPA_mg.aep)
      PRESENTACION DEL CURSO\  UNIDAD 1\BIENVENIDA\  UNIDAD 3\...  (profes)
Los casos entran en su unidad, al lado de los videos de profes, con las diez
carpetas de la serie de casos (09 MOTION GRAPHICS en vez de 09 A LA VOZ):
      00 DOCUMENTOS FUENTE\    el documento del Drive (.md)
      00 PERSONAJES\           hojas de personaje (+ _crudos)
      UNIDAD 1\CASO NICO - Principio de culpabilidad\
En Resolve (DAE MASTER - CURSOS): CURSO - SRPA Y JUSTICIA RESTAURATIVA ›
UNIDAD 1 › CASO NICO - Principio de culpabilidad › los bins.
"""
import os

from guion_sr import PIEZAS, UNIDADES

MASTER = r'E:\DAE MASTER'
RAIZ = os.path.join(MASTER, 'PRIORIDAD 1', 'CURSO - SRPA Y JUSTICIA RESTAURATIVA')
FUENTE = os.path.join(RAIZ, '00 DOCUMENTOS FUENTE')
PERSONAJES = os.path.join(RAIZ, '00 PERSONAJES')
MOTION = os.path.join(RAIZ, '00 MOTION GRAPHICS')

SUB_VIDEO = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL', '05 EXPORTS',
             '06 GUION Y STORYBOARD', '07 MOVIMIENTO', '08 MUSICA',
             '09 MOTION GRAPHICS', '10 TIMELINE SEBASTIAN']
BINS_VIDEO = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL',
              '05 EXPORTS', '07 MOVIMIENTO', '08 MUSICA', '09 MOTION GRAPHICS',
              '10 TIMELINE SEBASTIAN']
BIN_RAIZ = ['CURSO - SRPA Y JUSTICIA RESTAURATIVA']

TMP = r'D:\DAE\_tmp\sr'


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
