# -*- coding: utf-8 -*-
r"""Rutas de las situaciones del curso de Desaparicion Forzada.

EL ARBOL, IGUAL EN DISCO Y EN LOS BINS DE RESOLVE
    UNIDAD DESAPARICION FORZADA/
      CASO MIRIAM Y MARIANA/          el caso integrador, no se toca
      16 SITUACIONES/
        00 FUENTE/                    el documento tal como vino del Drive
        _PERSONAJES/                  hojas de personaje y referencias
        VIDEOS/
          SITUACION A - .../          las diez carpetas del caso integrador
        IMAGENES/
          SITUACION F - .../          01 PLANOS · 02 LAMINA · 05 EXPORTS ·
                                      06 GUION Y PROMPTS

    Dentro de cada video van las MISMAS diez carpetas que en un capitulo del
    caso integrador, con los mismos numeros: quien abra una situacion ya sabe
    donde esta cada cosa.
"""
import os

from guion_sit import SITUACIONES

UNIDAD = (r'E:\DAE MASTER\PRIORIDAD 03'
          '\\' r'CURSO - INVESTIGACION JUDICIAL Y FORENSE DE LA DESAPARICION FORZADA'
          '\\' r'UNIDAD DESAPARICION FORZADA')
RAIZ = os.path.join(UNIDAD, '16 SITUACIONES')
FUENTE = os.path.join(RAIZ, '00 FUENTE')
PERSONAJES = os.path.join(RAIZ, '_PERSONAJES')
VIDEOS = os.path.join(RAIZ, 'VIDEOS')
IMAGENES = os.path.join(RAIZ, 'IMAGENES')

SUB_VIDEO = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL', '05 EXPORTS',
             '06 GUION Y STORYBOARD', '07 MOVIMIENTO', '08 MUSICA',
             '09 A LA VOZ', '10 TIMELINE SEBASTIAN']
SUB_IMAGEN = ['01 PLANOS', '02 LAMINA', '05 EXPORTS', '06 GUION Y PROMPTS']

# los bins no llevan la carpeta de guion ni la de "a la voz": son texto
BINS_VIDEO = ['01 PLANOS', '02 CARTONES', '03 VOCES', '04 B-ROLL',
              '05 EXPORTS', '07 MOVIMIENTO', '08 MUSICA',
              '10 TIMELINE SEBASTIAN']
BINS_IMAGEN = ['01 PLANOS', '02 LAMINA', '05 EXPORTS']


def carpeta(letra, como=None):
    """`como` = 'video' o 'imagen' para pedir una forma en particular: la G
    existe en las dos. Sin `como`, la forma principal de la situacion."""
    tipo, nombre, _ = SITUACIONES[letra]
    tipo = como or tipo
    return os.path.join(VIDEOS if tipo == 'video' else IMAGENES, nombre)


def sub(letra, cual, como=None):
    return os.path.join(carpeta(letra, como), cual)


def voces(letra):
    return sub(letra, '03 VOCES')
