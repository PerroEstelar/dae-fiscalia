# -*- coding: utf-8 -*-
r"""Rutas del curso «Ley 1826 de 2017: procedimiento penal especial abreviado
y acusador privado» (PRIORIDAD 1).

EL ARBOL, IGUAL EN DISCO Y EN LOS BINS DE RESOLVE
    E:\DAE MASTER\PRIORIDAD 1\CURSO - LEY 1826 PROCEDIMIENTO PENAL ABREVIADO\
      00 DOCUMENTOS FUENTE\        los cuatro documentos del Drive (.md)
      00 PERSONAJES\               hojas de personaje (+ _crudos, _piel_ref)
      UNIDAD 1 - ...\              cinco láminas (CASO DE ESTUDIO 1..5)
      UNIDAD 2 - ...\              dos videos (ESTUDIO REVERSO 1, 2)
      UNIDAD 3 - ...\              tres láminas (CASO DE ESTUDIO 1..3)
      UNIDAD 4 - ...\              tres videos (CASO DE ANALISIS 1..3)

    Video: las MISMAS diez carpetas de Derechos humanos y de toda la serie.
    Lámina: las cuatro de las láminas de «16 situaciones» (01 PLANOS ·
    02 LAMINA · 05 EXPORTS · 06 GUION Y PROMPTS).

    En Resolve (proyecto DAE MASTER - CURSOS): PRIORIDAD 1 › CURSO - LEY 1826
    PROCEDIMIENTO PENAL ABREVIADO › UNIDAD n › <pieza> › los bins. «PRIORIDAD
    1» ya existe con «CURSO - JUSTICIA RESTAURATIVA» adentro: este curso es su
    vecino y no lo toca.
"""
import os

from guion_lp import PIEZAS, UNIDADES

MASTER = r'E:\DAE MASTER'
RAIZ = os.path.join(MASTER, 'PRIORIDAD 1',
                    'CURSO - LEY 1826 PROCEDIMIENTO PENAL ABREVIADO')
FUENTE = os.path.join(RAIZ, '00 DOCUMENTOS FUENTE')
PERSONAJES = os.path.join(RAIZ, '00 PERSONAJES')

SUB_VIDEO = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL', '05 EXPORTS',
             '06 GUION Y STORYBOARD', '07 MOVIMIENTO', '08 MUSICA',
             '09 A LA VOZ', '10 TIMELINE SEBASTIAN']
SUB_IMAGEN = ['01 PLANOS', '02 LAMINA', '05 EXPORTS', '06 GUION Y PROMPTS']
BINS_VIDEO = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL',
              '05 EXPORTS', '07 MOVIMIENTO', '08 MUSICA',
              '10 TIMELINE SEBASTIAN']
BINS_IMAGEN = ['01 PLANOS', '02 LAMINA', '05 EXPORTS']
BIN_RAIZ = ['PRIORIDAD 1', 'CURSO - LEY 1826 PROCEDIMIENTO PENAL ABREVIADO']

TMP = r'D:\DAE\_tmp\lp'


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
