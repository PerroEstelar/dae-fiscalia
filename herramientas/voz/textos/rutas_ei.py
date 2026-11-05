# -*- coding: utf-8 -*-
r"""Rutas del curso «Estándares interamericanos · graves violaciones a los
derechos humanos» (PRIORIDAD 3).

EL ARBOL, IGUAL EN DISCO Y EN LOS BINS DE RESOLVE
    E:\DAE MASTER\PRIORIDAD 03\CURSO - ESTANDARES INTERAMERICANOS\
      00 DOCUMENTOS FUENTE\        el documento del Drive (.md)
      00 PERSONAJES\               hojas de personaje (+ _crudos, _piel_ref)
      VIDEOS\                      S01 S04 S06 S07 S08
        SITUACION 01 - ...\        las MISMAS diez carpetas de toda la serie
      IMAGENES\                    S02 S03 S05 S09 S10 S11
        SITUACION 02 - ...\        las cuatro de las láminas (01 PLANOS ·
                                   02 LAMINA · 05 EXPORTS · 06 GUION Y PROMPTS)
        IMAGENES ENTREGA\          las láminas con su nombre de entrega

    PRIORIDAD 0X / X (Sebastián, 3 nov: si conviven las dos se funden en la de
    un dígito). Medido el 5 nov: en disco y en el pool solo existe «PRIORIDAD
    03» (los cinco casos P3 y Desaparición forzada), sin «PRIORIDAD 3». El
    curso entra en la que existe: crear «PRIORIDAD 3» abriría el par y
    obligaría a mover (y reenlazar) todo lo de la serie P3.

    En Resolve (proyecto DAE MASTER - CURSOS): PRIORIDAD 03 › CURSO -
    ESTANDARES INTERAMERICANOS › VIDEOS|IMAGENES › <situación> › los bins.
"""
import os

from guion_ei import PIEZAS, UNIDADES

MASTER = r'E:\DAE MASTER'
RAIZ = os.path.join(MASTER, 'PRIORIDAD 03', 'CURSO - ESTANDARES INTERAMERICANOS')
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
BIN_RAIZ = ['PRIORIDAD 03', 'CURSO - ESTANDARES INTERAMERICANOS']

TMP = r'D:\DAE\_tmp\ei'


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
