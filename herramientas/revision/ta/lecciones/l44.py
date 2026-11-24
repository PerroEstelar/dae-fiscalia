# -*- coding: utf-8 -*-
from maqueta import *


def R(i):
    t = limpia(re.sub(r'^\d+\.\s*', '', T(i)))
    m = re.match(r'^([^:]{3,90}):\s*(.+)$', t)
    return (m.group(1), m.group(2)) if m else (t[:60], t)


OB = ['documento', 'expediente', 'libros', 'balanza', 'carpetas', 'escalones', 'lupa', 'escudo', 'paquete', 'personas', 'huella', 'alerta' if False else 'reloj', 'mazo']
VER = [R(i) for i in (5627, 5629, 5631, 5633, 5635, 5637, 5639, 5641, 5643, 5645, 5647, 5649, 5651)]

C = [('%d. %s' % (k + 1, VER[k][0]), VER[k][1], OB[k]) for k in range(13)]

ESCENAS = [
    lamina('El control de legalidad del preacuerdo', T(5582, 1), obj='mazo', rotulo='El último filtro: el juez de conocimiento',
           com='La 4.4 no trae pregunta orientadora: abre con su primer párrafo.'),
    ruta('Del control formal al control material', [
        ('Los primeros pronunciamientos (2005)', J(T(5596), T(5597, 1)), 'mazo'),
        ('2006 a 2008', T(5597, 1, 1), 'mazo'),
        ('El punto de inflexión: radicado 34829 de 2011', T(5602), 'mazo'),
        ('Un control material', T(5606), 'lupa')],
        com='La evolución jurisprudencial como línea de tiempo: se entiende por qué hoy el control es material.'),
    compacta('Qué verifica el control material', [
        ('p', T(5610)),
        ('p', T(5615, 1), 'regla'),
        ('p', T(5620, 1), 'clave')]),
    compacta('a. La verificación del juez (1 a 7)', [
        ('malla', [[C[k] for k in range(0, 4)], [C[k] for k in range(4, 7)]])],
        com='Los trece puntos que verifica el juez en dos cuadrículas: el rótulo a la vista y el texto al abrir. El fiscal puede usarlas antes de firmar el acta; descargables como lista de chequeo en PDF.'),
    compacta('a. La verificación del juez (8 a 13)', [
        ('malla', [[C[k] for k in range(7, 10)], [C[k] for k in range(10, 13)]])]),
    compacta('Si el acuerdo no supera el control', [
        ('p', T(5653, 1), 'clave'),
        ('p', T(5658, 2)),
        ('p', J(T(5663), T(5665)), 'regla')]),
    compacta('Síntesis de la unidad 4', [
        ('p', T(5704)),
        ('p', T(5663), 'clave')],
        video=('u4_cierre', 'Síntesis de la unidad 4'), guia='Vea el video de síntesis de la unidad.',
        com='Video de cierre de la unidad 4, ya producido.'),
    lamina('Finalización de la unidad', J(T(5876).replace(' 🎉', '').replace('¡Felicitaciones por completar esta unidad! ', '')),
           obj='escalones', rotulo='¡Felicitaciones por completar esta unidad!', ilus='comunidad-interes-general.webp',
           com='La evaluación de la unidad (el caso de Andrés y Julián en la joyería) va como cuestionario del aula virtual.'),
    compacta('Cierre del curso', [
        ('p', T(5882, 2), 'clave'),
        ('sub', 'Para obtener el certificado'),
        ('lista', [T(5895), T(5897)])],
        video=('curso_cierre', 'Cierre del curso · Juan David Peña Gómez'), guia='Vea el video de cierre del curso.',
        com='El video de cierre del curso, ya producido, con el mensaje de cierre y los requisitos de certificación del DI.'),
]
