# -*- coding: utf-8 -*-
from maqueta import *


def N(i, n=None):
    return T(i, n, 1)


def R(i):
    """Ítem numerado «1. Rótulo: texto» → (rótulo, texto)."""
    t = limpia(re.sub(r'^\d+\.\s*', '', T(i)))
    m = re.match(r'^([^:]{3,90}):\s*(.+)$', t)
    return (m.group(1), m.group(2)) if m else (t[:60], t)


MOD = [R(i) for i in (5156, 5159, 5162, 5165, 5168, 5171, 5176)]
MET = [R(i) for i in (5476, 5478, 5482, 5485, 5489, 5492, 5495, 5497)]
ERR = [R(i) for i in (5502, 5507, 5510, 5513, 5515, 5518)] + [('Régimen especial', limpia(re.sub(r'^\d+\.\s*', '', T(5521)))), R(5525)]
OBJ = ['documento', 'balanza', 'mazo', 'reloj', 'libros', 'lupa', 'escalones', 'escudo']

ESCENAS = [
    lamina('Pregunta orientadora de la lección', T(5135, 1), obj='balanza', rotulo='¿Cómo determinar una pena negociada?'),
    ruta('Ruta de la lección', [
        ('a. Fijación de una pena concreta', T(5297, 1), 'documento'),
        ('b. Los concursos de conductas punibles', T(5314, 1), 'carpetas'),
        ('c. La negociación no es ficción', T(5338, 2), 'escudo'),
        ('d. Una metodología de dosificación', MET[0][1], 'escalones'),
        ('e. Errores frecuentes', ERR[0][1], 'lupa')]),
    ruta('Tres momentos de la pena', [
        ('1. La pena legalmente prevista', N(5142), 'libros'),
        ('2. La pena individualizada', N(5145), 'balanza'),
        ('3. La pena negociada', N(5150), 'personas')],
        com='La distinción de base de la lección, en tres pasos que se recorren en orden.'),
    esquema('Las modalidades de negociación', 'personas', [(m[0], m[1], OBJ[k]) for k, m in enumerate(MOD)],
            com='Siete modalidades como ramas de un mapa; la regla que las une va en la pantalla siguiente.'),
    compacta('Primero qué se negocia; después cuánto', [
        ('p', T(5180), 'clave'),
        ('p', T(5183, 1), 'regla'),
        ('p', T(5183, 2, 1))]),
] + ejemplo('Carlos y la adjudicación del contrato', J(T(5198), T(5204), T(5208), T(5212), T(5219), T(5227)), T(5233), B(5234, 5241),
            [T(5243), J(T(5248), T(5254)), J(T(5259), T(5265))]) + [
    compacta('La gravedad del delito no se valora dos veces', [
        ('p', T(5267, 2)),
        ('p', T(5275, 1), 'alerta'),
        ('p', J(T(5275, 1, 2), T(5280)), 'regla')]),
    compara('El momento procesal y el beneficio', [
        ('Desde la imputación hasta antes de la acusación', N(5283), 'reloj'),
        ('Después de presentada la acusación', N(5291), 'tribunal')],
        com='Dos columnas: el incentivo cambia según la etapa.'),
    compacta('a. Fijación de una pena concreta en el preacuerdo', [
        ('p', T(5297, 2)),
        ('p', T(5305)),
        ('p', J(T(5310), T(5312)), 'regla')],
        com='La cita de la Corte en cursiva, separada de la explicación del autor.'),
    compacta('b. Los concursos de conductas punibles', [
        ('p', T(5314, 1)),
        ('p', T(5318, 2)),
        ('p', T(5318, 1, 2), 'alerta')]),
    compacta('c. La negociación no es ficción', [
        ('p', T(5340)),
        ('p', T(5350, 1, 1), 'regla'),
        ('p', T(5350, 1, 2))]),
    compacta('Calificación para efectos punitivos: qué se puede y qué no', [
        ('p', T(5355, 2)),
        ('p', T(5345)),
        ('p', T(5355, 1, 2), 'alerta')]),
] + ejemplo('Coautoría, complicidad y subrogados', J(T(5384), T(5390), T(5396), T(5402), T(5408), T(5413)), T(5419), B(5420, 5429),
            [T(5431), J(T(5440), T(5444)), J(T(5449), T(5453))],
            video=('c03', 'Caso: Coautoría, complicidad y subrogados'),
            com='Caso animado ya producido (Andrés y Julián en la joyería).') + [
    compacta('No todo lo matemáticamente posible es admisible', [
        ('p', T(5457, 2), 'clave'),
        ('p', T(5457, 1, 2), 'regla'),
        ('p', T(5467, 1), 'alerta'),
        ('p', T(5472, 1, 1))]),
    ruta('d. Una metodología de dosificación (1 a 4)', [('%d. %s' % (k + 1, m[0]), m[1], OBJ[k]) for k, m in enumerate(MET[:4])],
         com='La metodología de ocho pasos del DI en dos rutas de cuatro: se sigue en orden.'),
    ruta('d. Una metodología de dosificación (5 a 8)', [('%d. %s' % (k + 5, m[0]), m[1], OBJ[k + 4]) for k, m in enumerate(MET[4:])]),
    rejilla('e. Errores frecuentes en la dosificación', [(m[0], m[1], OBJ[k]) for k, m in enumerate(ERR)],
            com='Un recuadro por error. Ojo: en el DI la lista salta del 7 al 9 (no hay 8) y el 7 no tiene rótulo; aquí van ocho, sin número.'),
] + ejemplo('Carlos y la pena concreta de 90 meses', J(T(5528), T(5530), T(5531), T(5534)), T(5538), B(5539, 5547),
            [T(5549), J(T(5555), T(5559)), T(5563)]) + [
    compacta('Cierre de la lección', [
        ('p', T(5574, 1), 'clave'),
        ('p', T(5568, 1, 2))],
        ilus='comunidad-interes-general.webp'),
]
