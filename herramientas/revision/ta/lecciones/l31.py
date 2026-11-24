# -*- coding: utf-8 -*-
from maqueta import *

PEND = 'Texto pendiente: el DI del 10 de noviembre trae solo el título de este apartado.'
ESCENAS = [
    compacta('Introducción a la unidad 3', [
        ('p', T(3601, 1), 'clave'),
        ('sub', 'Las cuatro lecciones de la unidad'),
        ('lista', ['3.1. Fundamentos constitucionales y legales', '3.2. Causales de aplicación', '3.3. Procedimiento, víctimas y control judicial', '3.4. Relación con la justicia restaurativa'])],
        video=('u3_inicio', 'Introducción a la unidad 3'), guia='Vea el video de introducción a la unidad.',
        com='Video del profe ya producido (inicio de la unidad 3).'),
    lamina('Pregunta orientadora de la unidad', T(3649), obj='balanza', rotulo='¿Cuándo suspender, interrumpir o renunciar?',
           com='En el DI la pregunta abre el desarrollo de la unidad 3.'),
    ruta('Ruta de la lección', [
        ('a. Fundamentos generales', PEND, 'libros'),
        ('b. El juicio de proporcionalidad', PEND, 'balanza'),
        ('c. Modalidades: renuncia, suspensión e interrupción', PEND, 'escalones')],
        com='Concepto → test de proporcionalidad → modalidades, en ese orden, como pidió la revisión.'),
    esquema('a. Fundamentos generales del principio de oportunidad', 'balanza', [
        ('Una herramienta excepcional y reglada', T(3601, 1), 'escudo'),
        ('Con autorización judicial', PEND, 'mazo'),
        ('Fundamento constitucional', PEND, 'libros'),
        ('Fundamento legal', PEND, 'documento')],
        com='OJO: el DI del 10 nov no trae el desarrollo de la lección 3.1 (solo sus títulos). La pantalla queda armada; el texto entra cuando llegue.'),
    ruta('b. El juicio de proporcionalidad', [
        ('1. Idoneidad', PEND, 'lupa'),
        ('2. Necesidad', PEND, 'balanza'),
        ('3. Proporcionalidad en sentido estricto', PEND, 'escalones')],
        com='El test, paso a paso. Texto pendiente del DI (la evaluación de la unidad sí lo usa: idoneidad, necesidad, proporcionalidad).'),
    giro('c. Modalidades del principio de oportunidad', [
        ('Renuncia', PEND, 'escudo'),
        ('Suspensión', PEND, 'reloj'),
        ('Interrupción', PEND, 'mazo')],
        com='Tres tarjetas, una por modalidad. Texto pendiente del DI.'),
]
