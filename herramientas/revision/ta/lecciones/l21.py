# -*- coding: utf-8 -*-
from maqueta import *


def F(i, n=None, desde=0):
    return re.sub(r'^➢\s*(La reparación integral|Desistimiento|Oblación|Retractación|Pago|Resarcimiento|Amnistía)\s*', '', T(i, n, desde))


Bq = B(2393, 2500)   # muerte, cosa juzgada, prescripción, caducidad
ESCENAS = [
    compacta('Introducción a la unidad 2', [
        ('p', T(2232, 1, 1), 'clave'),
        ('sub', 'Las dos lecciones de la unidad'),
        ('lista', ['2.1. Causales de preclusión, oportunidades procesales y efectos', '2.2. Audiencia de preclusión: estructura, argumentación y actividad probatoria'])],
        video=('u2_inicio', 'Introducción a la unidad 2'), guia='Vea el video de introducción a la unidad.',
        com='Video del profe ya producido (inicio de la unidad 2) y, al lado, la pregunta que guía la unidad.'),
    esquema('¿Qué es la preclusión?', 'mazo', [
        ('Un mecanismo judicial y definitivo', T(2332), 'mazo'),
        ('Su fundamento', T(2337), 'escudo'),
        ('No es un preacuerdo ni un archivo', T(2342), 'balanza'),
        ('El artículo 331 del CPP', T(2353), 'libros'),
        ('Una valoración permanente', T(2359), 'lupa')],
        com='Mapa conceptual de entrada: qué es, para qué sirve y qué no es.'),
    ruta('Ruta de la lección', [
        ('a. Causales de preclusión', T(2366), 'carpetas'),
        ('b. Oportunidad', T(3008, 1), 'reloj'),
        ('c. Efectos', T(3061, 1), 'tribunal')]),
    compacta('a. Las siete causales del artículo 332, en dos grupos', [
        ('p', T(2996)),
        ('malla', [[('Predominantemente objetivas: 1.ª, 3.ª y 7.ª', T(2997), 'reloj'),
                    ('Exigen valoración: 2.ª, 4.ª, 5.ª y 6.ª', T(2999), 'balanza')]]),
        ('p', T(3003), 'alerta')],
        com='Organizador de dos grupos al mismo nivel; el DI advierte que es una clasificación pedagógica, y así queda.'),
    compacta('Causal 1: imposibilidad de iniciar o continuar la acción penal', [
        ('p', T(2368, 1)),
        ('p', T(2374), 'regla'),
        ('p', T(2383, 1)),
        ],
        com='La causal primera es la más extensa del DI: se abre aquí y se desarrolla en las pantallas que siguen.'),
    rejilla('Causal 1, primer grupo: causales objetivas', [
        ('Muerte del imputado o acusado', Bq[0], 'personas'),
        ('Cosa juzgada', [Bq[1], T(2411)], 'mazo'),
        ('Prescripción de la acción penal', [Bq[2], T(2448), T(2454)], 'reloj'),
        ('Caducidad de la querella', [Bq[3], T(2484), T(2497)], 'documento')],
        com='Cuatro recuadros que se abren: una figura por recuadro, con su texto completo.'),
    compacta('La cosa juzgada: la triple identidad', [
        ('p', T(2416, 2)),
        ('p', T(2421, 1), 'regla'),
        ('p', T(2421, 2, 1))]),
    esquema('Causal 1, segundo grupo: salidas alternativas al proceso', 'personas', [
        ('Desistimiento', J(T(2506).replace('➢ Desistimiento ', ''), T(2508, 2)), 'documento'),
        ('Oblación', F(2533), 'paquete'),
        ('Retractación', F(2539, 2), 'megafono'),
        ('Pago', F(2553), 'carpetas'),
        ('Resarcimiento', F(2578), 'casa'),
        ('Amnistía', J(T(2626), T(2633, 1)), 'escudo'),
        ('Reparación integral', F(2656), 'corazon')],
        com='Siete figuras como ramas de un mismo mapa, en vez de un texto seguido: cada una se abre con su definición del DI.'),
    compacta('Las figuras del segundo grupo, comparadas (1 de 2)', [
        ('tabla', ['Figura', 'Delitos', 'Intervención de la víctima', 'Requisitos', 'Mecanismo procesal y efecto'], [
            ['Desistimiento', 'Querellables', 'Necesaria, por la manifestación libre. No es indispensable la reparación', 'Manifestación voluntaria de la víctima de no tener interés en que prosiga la acción penal', 'Antes del escrito de acusación: archivo de las diligencias; después: preclusión. En ambos: extinción de la acción penal'],
            ['Oblación', 'Sancionados con pena única de multa', 'No es necesaria', 'El pago de la multa que correspondería si el proceso culmina con sentencia condenatoria', 'Preclusión. Extinción de la acción penal'],
            ['Retractación', 'Injuria y calumnia', 'Es conveniente consultar a la víctima sobre los términos de la retractación', 'Retirar o desmentir la manifestación, en condiciones equivalentes a la expresada inicialmente', 'Preclusión. Extinción de la acción penal']])],
        com='El cuadro del DI, ordenado y legible (en el PDF sus columnas salen corridas), partido en dos pantallas para que no pida scroll. Con botón para descargarlo.'),
    compacta('Las figuras del segundo grupo, comparadas (2 de 2)', [
        ('tabla', ['Figura', 'Delitos', 'Intervención de la víctima', 'Requisitos', 'Mecanismo procesal y efecto'], [
            ['Pago', 'Arts. 248 y 402 del Código Penal', 'No es necesaria en el art. 248; en el 402 se requiere el detalle de la obligación tributaria', 'Efectuar la cancelación de la cifra o suma respectiva', 'Preclusión. Extinción de la acción penal'],
            ['Resarcimiento', 'Daño en bien ajeno (art. 265 CP)', 'Es conveniente consultar a la víctima', 'Si el daño es reparado antes de la sentencia de primera instancia', 'Preclusión. Extinción de la acción penal']])]),
    compara('Amnistía propia e impropia', [
        ('Amnistía propia (art. 82.3 CP)', T(2633, 2, 1), 'escudo'),
        ('Amnistía impropia (art. 88.3 CP)', T(2638), 'mazo')],
        com='Las dos modalidades lado a lado; el ejemplo del DI va en la pantalla siguiente.'),
    compacta('Veamos un ejemplo: la amnistía en una investigación en curso', [
        ('malla', [[('Situación', T(2648, 1), 'expediente')]]),
        ('p', T(2648, 2, 1), 'clave')]),
    ruta('La reparación integral: de la indemnización a la Ley 2477 de 2025', [
        ('Ley 600 de 2000', J('Ley', T(2663)), 'libros'),
        ('2011', T(2666), 'mazo'),
        ('2016 y 2020', T(2682), 'mazo'),
        ('2024', J(T(2688), T(2689)), 'mazo'),
        ('Ley 2477 de 2025', T(2708), 'documento')],
        com='Línea de tiempo: el cambio de postura de la Corte se entiende mejor en orden que en párrafos seguidos.'),
    compacta('Lo que cambió con la Ley 2477 de 2025', [
        ('p', T(2712)),
        ('lista', [T(2713), T(2715), T(2717)], True),
        ('p', J(T(2720), T(2721)), 'alerta')]),
    compacta('Procedencia y límites de la reparación integral', [
        ('p', T(2726)),
        ('p', T(2739)),
        ('p', T(2741, 1)),
        ('p', T(2756, 1), 'alerta')]),
    compacta('La reparación integral con enfoque restaurativo', [
        ('p', T(2761, 1), 'clave'),
        ('p', T(2767, 1)),
        ('p', T(2794, 1)),
        ('p', T(2807, 1))],
        ilus='comunidad-interes-general.webp'),
    rejilla('Causales 2 a 5', [
        ('2.ª Una circunstancia que excluye la responsabilidad', [T(2842), T(2850)], 'balanza'),
        ('3.ª Inexistencia del hecho investigado', T(2863), 'lupa'),
        ('4.ª Atipicidad del hecho investigado', [T(2876), T(2878), T(2881)], 'libros'),
        ('5.ª Ausencia de intervención del imputado', T(2911), 'personas')],
        com='Cuatro causales, un recuadro cada una, con su texto completo al abrir.'),
    compacta('Causal 6: imposibilidad de desvirtuar la presunción de inocencia', [
        ('p', T(2921, 2)),
        ('p', T(2927, 1), 'regla'),
        ('p', T(2927, 1, 2), 'alerta'),
        ('p', T(2953, 1))]),
    compacta('Causal 7: vencimiento del término (preclusión-sanción)', [
        ('p', J(T(2971), T(2972, 2))),
        ('p', T(2979), 'regla'),
        ('p', T(2983, 1), 'alerta')]),
    esquema('b. Oportunidad: cuándo puede solicitarse', 'reloj', [
        ('En la indagación y la investigación', T(3008, 1), 'lupa'),
        ('En el juzgamiento', J(T(3017), T(3018, 1)), 'tribunal'),
        ('Ante el juez de conocimiento', T(3028), 'mazo'),
        ('Un escenario de contradicción', T(3033), 'personas'),
        ('Garantías para las víctimas', J(T(3039, 1), T(3052)), 'escudo')]),
    compara('c. Efectos: si se decreta o si se niega', [
        ('Si el juez decreta la preclusión', T(3061, 3), 'mazo'),
        ('Si el juez la niega', J(T(3071), T(3075, 1)), 'carpetas')],
        com='Las dos salidas posibles lado a lado.'),
    compacta('Recursos contra la decisión', [
        ('p', T(3083, 1)),
        ('p', T(3083, 1, 1), 'clave'),
        ('p', T(3083, 1, 2))]),
    compacta('Errores que deben evitarse', [
        ('p', T(3103, 1), 'alerta'),
        ('p', T(3109, 1), 'alerta'),
        ('p', T(3109, 1, 1), 'regla')]),
    compacta('Cierre de la lección', [
        ('p', T(3114, 2), 'clave'),
        ('p', T(3132))],
        ilus='comunidad-interes-general.webp'),
]
