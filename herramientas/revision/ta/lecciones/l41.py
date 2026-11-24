# -*- coding: utf-8 -*-
from maqueta import *

FIN = [T(4157, None, 1), T(4162), T(4167), T(4172), T(4178)]
ESCENAS = [
    compacta('Introducción a la unidad 4', [
        ('p', J(T(4011), T(4012, 1)), 'clave'),
        ('sub', 'Las cuatro lecciones de la unidad'),
        ('lista', ['4.1. Marco normativo, finalidades y límites', '4.2. Técnicas de negociación', '4.3. Dosificación punitiva', '4.4. Control de legalidad'])],
        video=('u4_inicio', 'Introducción a la unidad 4'), guia='Vea el video de introducción a la unidad.',
        com='Video del profe ya producido (inicio de la unidad 4) y la pregunta que orienta la unidad.'),
    lamina('Pregunta orientadora de la lección', T(4108, 1, 1), obj='balanza', rotulo='¿Cómo construir un preacuerdo válido?'),
    ruta('Ruta de la lección', [
        ('a. Finalidades', T(4153, 1), 'escalones'),
        ('b. El reintegro patrimonial', T(4239, 1), 'paquete'),
        ('c. Circunstancias de atenuación', T(4305), 'balanza'),
        ('d. Ficciones jurídicas', T(4377, 1), 'libros'),
        ('e. Allanamiento y preacuerdo', T(4458, 1), 'documento'),
        ('f. Víctimas y procesado', T(4523, 1), 'personas'),
        ('g. El juez de conocimiento', T(4585, 1), 'mazo')],
        com='Siete temas en una ruta: es el índice de la lección y permite volver a cualquiera.'),
    compacta('Justicia consensuada, no libre disposición', [
        ('p', T(4131, 1)),
        ('p', T(4138, 2, 1)),
        ('p', T(4144, 1), 'alerta')]),
    giro('a. Las cinco finalidades del preacuerdo (art. 348 CPP)', [
        ('1. Humanizar la actuación procesal y la pena', FIN[0], 'corazon'),
        ('2. Obtener pronta y cumplida justicia', FIN[1], 'reloj'),
        ('3. Activar la solución de los conflictos sociales', FIN[2], 'personas'),
        ('4. Propiciar la reparación integral', FIN[3], 'escudo'),
        ('5. La participación del imputado en la definición de su caso', FIN[4], 'balanza')],
        com='Cinco tarjetas que se giran, una por finalidad: se leen de a una y se recuerdan mejor que en párrafo.'),
    compacta('Lo que ha dicho la Corte Constitucional', [
        ('p', T(4188, 1)),
        ('p', T(4207, 1), 'clave')],
        com='La cita de la Corte en cursiva y aparte; la conclusión del autor, resaltada.'),
    compacta('Un margen reglado y una negociación ética', [
        ('p', T(4211, 2)),
        ('p', T(4224, 1), 'regla'),
        ('p', T(4229, 1, 1))]),
    compacta('b. El reintegro patrimonial (art. 349 CPP)', [
        ('p', T(4239, 2)),
        ('p', T(4253, 1), 'regla'),
        ('p', T(4253, 2, 1))]),
] + ejemplo('El doble beneficio y el reintegro', J(T(4261), T(4267), T(4269), T(4272)), T(4274), B(4275, 4284), [T(4286), T(4293), T(4300)],
            video=('c02', 'Caso: El doble beneficio y el reintegro'),
            com='Caso animado ya producido (Carlos y Andrés).') + [
    compacta('c. Circunstancias de atenuación punitiva', [
        ('p', J(T(4305), T(4307, 2, 1))),
        ('p', T(4313, 1)),
        ('p', T(4325, 1, 1), 'regla')],
        com='La cita de la Corte (C-1260 de 2005, según el DI) va en cursiva; la regla, resaltada.'),
] + ejemplo('La marginalidad alegada sin sustento', J(T(4331), T(4336), T(4341), T(4344, 1)), T(4344, 2, 1), B(4345, 4357), [T(4359), T(4367), T(4372)],
            video=('c04', 'Caso: La marginalidad alegada sin sustento'),
            com='Caso animado ya producido (Miguel).') + [
    compacta('d. Las ficciones jurídicas', [
        ('p', T(4377, 2, 1)),
        ('p', T(4383, 1)),
        ('p', T(4394, 1, 2), 'alerta')]),
] + ejemplo('Julián y la calificación más favorable', J(T(4405), T(4413), T(4419)), T(4423), B(4424, 4436), [T(4437).lstrip('¿ '), T(4445), T(4452)],
            com='En el DI la primera respuesta abre con un «¿» suelto (renglón «¿ El caso permite…»); aquí va sin él.') + [
    ruta('e. Allanamiento y preacuerdo: la línea jurisprudencial', [
        ('Primera etapa (2006)', J(T(4462), T(4464, 1)), 'mazo'),
        ('Segunda etapa', J(T(4472), T(4476, 1)), 'mazo'),
        ('SP-14496-2017', T(4485, 2), 'mazo'),
        ('SP-1901-2024 y SP3252-2024', J(T(4490), T(4491)), 'mazo')],
        com='La evolución de la jurisprudencia como línea de tiempo.'),
    compara('Allanamiento frente a preacuerdo', [
        ('El allanamiento a cargos', T(4502, 3), 'documento'),
        ('El preacuerdo', T(4510, 2, 2), 'personas')]),
    compacta('f. La participación de las víctimas', [
        ('p', T(4523, 1, 2)),
        ('p', T(4549), 'alerta'),
        ('p', T(4551, 1), 'clave')]),
    compacta('El procesado y la prohibición de retractarse', [
        ('p', T(4557, 2, 1)),
        ('p', T(4574, 2), 'regla')]),
    compacta('g. El juez de conocimiento: no es un notario', [
        ('p', T(4585, 2)),
        ('p', T(4600, 2), 'clave')]),
] + ejemplo('Andrés, la marginalidad y la entidad afectada', J(T(4617), T(4622), T(4625), T(4630), T(4634)), T(4640), B(4641, 4654),
            [T(4656), J(T(4661), T(4667)), J(T(4671), T(4673))],
            com='Ejemplo integrador del DI: reúne los límites de toda la lección.') + [
    compacta('Cierre de la lección', [
        ('p', T(4612, 2), 'clave'),
        ('p', T(4612, 1, 2))],
        ilus='comunidad-interes-general.webp'),
]
