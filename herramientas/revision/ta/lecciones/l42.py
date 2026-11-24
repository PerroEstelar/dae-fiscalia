# -*- coding: utf-8 -*-
from maqueta import *


def N(i, n=None):
    """Párrafo numerado del DI sin su número («1.»)."""
    return T(i, n, 1)


def M_(i):
    return limpia(re.sub(r'^\d+\.\s*', '', T(i)))


OB = ['lupa', 'libros', 'documento', 'balanza', 'escalones', 'reloj', 'personas', 'carpetas', 'mazo', 'tribunal', 'expediente', 'megafono']


def R(i):
    t = limpia(re.sub(r'^\d+\.\s*', '', T(i)))
    m = re.match(r'^([^:]{3,60}):\s*(.+)$', t)
    return (m.group(1), m.group(2)) if m else (t[:40], t)


R12 = [('%d. %s' % (k + 1, R(i)[0]), R(i)[1], OB[k]) for k, i in enumerate((5079, 5082, 5084, 5085, 5087, 5089, 5091, 5093, 5095, 5097, 5099, 5101))]

ESCENAS = [
    lamina('Pregunta orientadora de la lección', T(4693, 1), obj='personas', rotulo='¿Cómo negociar sin comprometer la legalidad?'),
    ruta('Ruta de la lección', [
        ('a. Límites a la negociación', T(4707, 1), 'escudo'),
        ('b. Criterios estratégicos', N(4821, 1), 'lupa'),
        ('c. La negociación como proceso', 'Apertura, intercambio y cierre.', 'escalones'),
        ('d. Sugerencias para preparar un preacuerdo', T(5077), 'documento')]),
    compacta('a. Calibrar la negociación según la fortaleza probatoria', [
        ('p', T(4713, 1), 'regla'),
        ('lista', [N(4716, 1), N(4721, 1), N(4726, 1)], True)],
        com='Tres tipos de caso en lista numerada; el detalle de cada uno, en el caso de los tres escenarios que sigue.'),
] + ejemplo('Los tres escenarios probatorios', J(T(4735), T(4742, 1), *[N(i) for i in (4745, 4751)], N(4757), T(4759), T(4763, 1)), T(4763, 1, 1), B(4764, 4776),
            [T(4778), J(T(4784), T(4786), T(4790), T(4794), T(4797)), T(4800)],
            video=('c01', 'Caso: Los tres escenarios probatorios'),
            com='Caso animado ya producido (Alejandro): la misma propuesta en tres escenarios probatorios.') + [
    ruta('Cinco preguntas para preparar la negociación', [
        ('1. ¿Qué está probado?', N(4806), 'lupa'),
        ('2. ¿Qué cargos se están formulando?', N(4808), 'documento'),
        ('3. ¿Qué puede negociarse?', N(4810), 'balanza'),
        ('4. ¿Qué puede ofrecerse y qué debe exigirse?', N(4812), 'personas'),
        ('5. ¿Qué ocurrirá si no se alcanza el convenio?', N(4815), 'reloj')],
        com='Las cinco preguntas del DI como ruta: es una herramienta para usar antes de cada negociación.'),
    esquema('b. Criterios estratégicos (1 a 6)', 'lupa', [
        ('1. La teoría del caso', N(4821), 'expediente'),
        ('2. El beneficio', J(N(4832), T(4839), T(4843)), 'balanza'),
        ('3. El momento de la admisión', N(4848), 'reloj'),
        ('4. La calificación jurídica', J(N(4857), T(4864)), 'libros'),
        ('5. La redacción del acta', J(N(4867), T(4872)), 'documento'),
        ('6. La víctima', N(4878), 'personas')],
        com='Los doce criterios del DI en dos mapas de seis: así caben las tarjetas sin apretar el texto.'),
    esquema('b. Criterios estratégicos (7 a 12)', 'escudo', [
        ('7. El Ministerio Público', J(N(4889), T(4894)), 'escudo'),
        ('8. La buena fe', N(4899), 'corazon'),
        ('9. Irrevocabilidad y confianza', N(4908), 'mazo'),
        ('10. Prohibición de doble beneficio', J(N(4918), T(4928)), 'alerta' if False else 'carpetas'),
        ('11. Prohibición de doble incriminación', J(N(4932), T(4948)), 'balanza'),
        ('12. Otras prohibiciones', T(4954), 'lupa')]),
    rejilla('12. Otras prohibiciones legales', [
        ('Ley 1098 de 2006, art. 199', T(4960).lstrip('- '), 'personas'),
        ('Terrorismo y delitos conexos (Ley 1121 de 2006)', J(T(4969).lstrip('- '), T(4971)), 'escudo'),
        ('Feminicidio (Ley 1761 de 2015, art. 5)', T(4980).lstrip('- '), 'corazon')],
        com='Tres recuadros, uno por prohibición legal, con su texto completo al abrir.'),
    ruta('c. La negociación como proceso', [
        ('1. Apertura', N(4989), 'personas'),
        ('2. Intercambio', N(4991), 'balanza'),
        ('3. Cierre', N(4995), 'documento')]),
] + ejemplo('La negociación paso a paso', J(T(5001), T(5006), T(5011, 2), T(5022, 2)), T(5042), B(5043, 5048),
            [T(5050), J(T(5055), T(5060), T(5065)), J(T(5070), T(5073))],
            video=('c05', 'Caso: La negociación paso a paso'),
            com='Caso animado ya producido (Laura): apertura, intercambio y cierre en un mismo caso.') + [
    compacta('d. Matriz para preparar un preacuerdo', [
        ('malla', [[R12[k] for k in range(f, f + 4)] for f in (0, 4, 8)])],
        com='La matriz de doce pasos del DI como cuadrícula: el rótulo de cada paso a la vista y su texto al abrirlo. Descargable como lista de chequeo en PDF.'),
    compacta('Cierre de la lección', [
        ('p', T(5114, 1), 'clave'),
        ('p', T(5106, 1, 2))],
        ilus='comunidad-interes-general.webp'),
]
