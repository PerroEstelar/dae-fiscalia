# -*- coding: utf-8 -*-
from maqueta import *

PEND = 'Texto pendiente: el DI del 10 de noviembre trae solo el título de este apartado.'
ESCENAS = [
    lamina('Causales de aplicación', 'Las causales del artículo 324 del CPP se estudian en cuatro grupos: de interés nacional; de colaboración con la justicia y desarticulación criminal; de intervención mínima del derecho penal; y de reparación de las víctimas y justicia restaurativa.',
           obj='carpetas', rotulo='Cuatro grupos de causales',
           com='El DI del 10 nov trae solo los títulos de los cuatro grupos; la frase de apertura los enumera tal como están en la estructura del curso.'),
    rejilla('Los cuatro grupos de causales', [
        ('a. Causales de interés nacional', PEND, 'escudo'),
        ('b. Colaboración con la justicia y desarticulación criminal', PEND, 'personas'),
        ('c. Intervención mínima del derecho penal', PEND, 'balanza'),
        ('d. Reparación de las víctimas y justicia restaurativa', PEND, 'corazon')],
        com='Organizador de los cuatro grupos de causales, como pidió la revisión. Texto pendiente del DI.'),
    compacta('Antes de aplicar una causal: viabilidad', [
        ('chequeo', [limpia(T(i)) for i in (3655, 3656, 3658, 3659)])],
        com='Las preguntas de viabilidad de la guía del DI (bloque A) como lista de chequeo con simulación.'),
]
