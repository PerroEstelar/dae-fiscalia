# -*- coding: utf-8 -*-
from maqueta import *

PEND = 'Texto pendiente: el DI del 10 de noviembre trae solo el título de este apartado.'
PASOS = ['Identificar si el principio de oportunidad puede aplicarse', 'Identificar la causal', 'Aplicar el test de proporcionalidad',
         'Determinar la modalidad', 'Definir las condiciones y los efectos para las víctimas', 'Adelantar las conversaciones y documentar la negociación',
         'Elaborar el FPO', 'Eventuales solicitudes de información y posibles recomendaciones, no vinculantes, del superior inmediato (seguimiento)',
         'Solicitar el control de legalidad', 'Si se trata de suspensión: hacer seguimiento al cumplimiento',
         'Si se trata de interrupción o suspensión: verificar si procede la revocatoria o modificación', 'Si procede la renuncia: verificar previamente el cumplimiento']
OBJ = ['lupa', 'carpetas', 'balanza', 'escalones', 'personas', 'telefono', 'documento', 'expediente', 'mazo', 'reloj', 'escudo', 'tribunal']


def G(a, b):
    return [limpia(re.sub(r'^\s*-\s*', '', t)) for i, t, h in parrafos(a, b) if not h]


ESCENAS = [
    ruta('3.3.1 Procedimiento: del caso a la decisión (a–f)', [('%s. %s' % ('abcdef'[k], PASOS[k]), PEND, OBJ[k]) for k in range(6)],
         com='Los doce pasos del procedimiento del DI, en dos rutas de seis para que se lean sin apretar. Texto de cada paso pendiente del DI.'),
    ruta('3.3.1 Procedimiento: del FPO al cumplimiento (g–l)', [('%s. %s' % ('ghijkl'[k], PASOS[6 + k]), PEND, OBJ[6 + k]) for k in range(6)]),
    giro('3.3.2 Participación de las víctimas', [
        ('Deber de información y consulta a la víctima', PEND, 'telefono'),
        ('Víctimas no ubicadas o que no comparecen', PEND, 'lupa'),
        ('Canales de intervención y representación', PEND, 'personas')],
        com='Tres tarjetas con los tres apartados del DI. Texto pendiente.'),
    compacta('3.3.3 Control judicial', [
        ('chequeo', [limpia(T(i)) for i in (3686, 3687, 3688, 3689, 3690, 3691)])],
        com='El DI no desarrolla el control judicial; sí trae sus preguntas en la guía (bloque F): van como lista de chequeo.'),
    rejilla('Guía para aplicar el principio de oportunidad', [
        ('A. Viabilidad', '\n'.join('• ' + x for x in G(3655, 3660)), 'lupa'),
        ('B. Modalidad', '\n'.join('• ' + x for x in G(3661, 3665)), 'escalones'),
        ('C. Víctimas', '\n'.join('• ' + x for x in G(3666, 3671)), 'personas'),
        ('D. Negociación', '\n'.join('• ' + x for x in G(3672, 3680)), 'documento'),
        ('E. Seguimiento del superior inmediato', '\n'.join('• ' + x for x in G(3681, 3685)), 'expediente'),
        ('F. Control judicial', '\n'.join('• ' + x for x in G(3686, 3692)), 'mazo')],
        com='La guía A–F del DI como acordeón de seis recuadros: cada uno abre sus preguntas. Es lo más completo que trae el DI de la unidad 3. Con botón de descarga en PDF.'),
]
