# -*- coding: utf-8 -*-
r"""Rutas del curso «Derechos humanos aplicados a la función judicial»
(PRIORIDAD 2).

EL ARBOL, IGUAL EN DISCO Y EN LOS BINS DE RESOLVE
    E:\DAE MASTER\PRIORIDAD 2\CURSO - DERECHOS HUMANOS APLICADOS A LA FUNCION JUDICIAL\
      00 DOCUMENTOS FUENTE\        los cinco guiones del Drive (.md)
      00 PERSONAJES\               hojas de personaje (+ _crudos)
      UNIDAD 1 - Llega la noticia\
      UNIDAD 2 - La defensa invoca un tratado\
      UNIDAD 3 - Dos versiones de la misma entrevista\
      UNIDAD 4 - La medida de aseguramiento\
      UNIDAD 5 - La decision integral y el giro\

    Dentro de cada pieza van las MISMAS diez carpetas de Justicia
    restaurativa, Gerencia judicial, el P3 y Desaparicion Forzada.

    En Resolve (proyecto DAE MASTER - CURSOS): PRIORIDAD 2 › CURSO - DERECHOS
    HUMANOS APLICADOS A LA FUNCION JUDICIAL › <pieza> › 01 PLANOS · 02
    CARTONES · 03 VOCES · 04 B-ROLL · 05 EXPORTS · 07 MOVIMIENTO · 08 MUSICA ·
    10 TIMELINE SEBASTIAN.

    «PRIORIDAD 2» ya existe con «CURSO - GERENCIA JUDICIAL» adentro: este
    curso es su vecino y no lo toca.
"""
import os

from guion_dh import TEMAS

MASTER = r'E:\DAE MASTER'
RAIZ = os.path.join(MASTER, 'PRIORIDAD 2',
                    'CURSO - DERECHOS HUMANOS APLICADOS A LA FUNCION JUDICIAL')
FUENTE = os.path.join(RAIZ, '00 DOCUMENTOS FUENTE')
PERSONAJES = os.path.join(RAIZ, '00 PERSONAJES')

SUB_VIDEO = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL', '05 EXPORTS',
             '06 GUION Y STORYBOARD', '07 MOVIMIENTO', '08 MUSICA',
             '09 A LA VOZ', '10 TIMELINE SEBASTIAN']
BINS_VIDEO = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL',
              '05 EXPORTS', '07 MOVIMIENTO', '08 MUSICA',
              '10 TIMELINE SEBASTIAN']
BIN_RAIZ = ['PRIORIDAD 2', 'CURSO - DERECHOS HUMANOS APLICADOS A LA FUNCION JUDICIAL']

TMP = r'D:\DAE\_tmp\dh'


def carpeta(clave):
    return os.path.join(RAIZ, TEMAS[clave][0])


def sub(clave, cual):
    return os.path.join(carpeta(clave), cual)


def voces(clave):
    return sub(clave, '03 VOCES')
