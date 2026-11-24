# -*- coding: utf-8 -*-
from maqueta import *

PEND = 'Texto pendiente: el DI del 10 de noviembre trae solo el título de este apartado.'
ESCENAS = [
    compara('Principio de oportunidad y justicia restaurativa', [
        ('La suspensión del procedimiento a prueba', T(3606, 1), 'reloj'),
        ('La participación de las víctimas', T(3606, 2, 1), 'personas')],
        com='La 3.4 no tiene desarrollo en el DI del 10 nov: la pantalla usa lo que dice de ella la introducción de la unidad.'),
    compacta('Relación con la justicia restaurativa', [
        ('p', T(3606, 1, 2), 'clave'),
        ('p', PEND)],
        ilus='comunidad-interes-general.webp',
        com='Pantalla reservada para el desarrollo de la 3.4 cuando llegue del autor.'),
    compacta('Síntesis de la unidad 3', [
        ('p', T(3766)),
        ('p', T(3613), 'clave')],
        video=('u3_cierre', 'Síntesis de la unidad 3'), guia='Vea el video de síntesis de la unidad.',
        com='Video de cierre de la unidad 3, ya producido.'),
    lamina('Finalización de la unidad', J(T(3964), T(3967)), obj='escalones', rotulo='¡Felicitaciones por culminar la presente unidad!',
           ilus='comunidad-interes-general.webp',
           com='La evaluación (el caso de Carlos White Ríos, con sus preguntas) va como cuestionario del aula virtual.'),
]
