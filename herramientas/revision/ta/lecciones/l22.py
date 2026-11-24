# -*- coding: utf-8 -*-
from maqueta import *

ESCENAS = [
    lamina('La audiencia de preclusión', T(3136, 1), obj='tribunal', rotulo='Un escenario judicial, no un trámite',
           com='La 2.2 no trae pregunta orientadora en el DI: abre con su primer párrafo, que dice qué es la audiencia.'),
    ruta('La audiencia, paso a paso', [
        ('1. Instalación y solicitud', T(3151, 1), 'tribunal'),
        ('2. Sustentación del fiscal', T(3178, 1, 1), 'documento'),
        ('3. Contradictorio', T(3189, 1), 'personas'),
        ('4. Elementos de conocimiento', T(3253, 1, 1), 'expediente'),
        ('5. Decisión', T(3340, 2), 'mazo'),
        ('6. Recursos', T(3357, 1), 'escalones')],
        com='La estructura de la audiencia como ruta de seis pasos: sirve de índice de la lección y de guía para el despacho.'),
    compacta('La sustentación: una proposición jurídica completa', [
        ('p', T(3159, 1, 2)),
        ('p', T(3183, 1), 'alerta'),
        ('p', T(3186), 'regla')]),
    compacta('Lo que ha dicho la Corte Suprema', [
        ('p', T(3166, 2)),
        ('p', T(3178, 1), 'clave')],
        com='La cita de la Corte, en cursiva y separada del texto del autor.'),
    rejilla('Los intervinientes en la audiencia', [
        ('La víctima', [T(3195), T(3198), T(3202, 3)], 'personas'),
        ('El Ministerio Público', [T(3214), T(3216)], 'escudo'),
        ('La defensa', [T(3222, 3)], 'balanza'),
        ('El juez de conocimiento', [T(3245, 3)], 'mazo')],
        com='Un recuadro por interviniente: qué aporta cada uno al control de la solicitud.'),
    compacta('Sin práctica de pruebas, pero con elementos de conocimiento', [
        ('p', T(3253, 2, 1)),
        ('p', T(3263, 2), 'regla'),
        ('p', T(3263, 1, 2))]),
    compacta('El estándar de decisión', [
        ('p', T(3285, 2)),
        ('p', T(3296, 1, 1)),
        ('p', T(3303, 2), 'alerta')]),
    compara('Preclusión no es juicio anticipado', [
        ('No es un juicio anticipado', T(3316, 3), 'tribunal'),
        ('Lo que debe distinguir el fiscal', T(3325), 'lupa')],
        com='Dos columnas que se despliegan; la regla de la causal sexta queda en la pantalla siguiente.'),
    compacta('La causal sexta y la preclusión en el juzgamiento', [
        ('p', T(3308, 2)),
        ('p', T(3308, 1, 2), 'alerta'),
        ('p', T(3332, 2))]),
    compara('La decisión: si se decreta o si se niega', [
        ('Si se decreta', T(3340), 'mazo'),
        ('Si se niega o se rechaza', T(3349), 'carpetas')]),
    compacta('Preparar una audiencia de preclusión', [
        ('p', T(3364, 1)),
        ('p', T(3364, 1, 2), 'clave')]),
    compacta('Cierre de la lección', [
        ('p', T(3374), 'clave'),
        ('p', T(3376, 1))],
        ilus='comunidad-interes-general.webp',
        com='La 2.2 no trae actividad en el DI; la evaluación de la unidad va como cuestionario del aula.'),
    compacta('Síntesis de la unidad 2', [
        ('p', T(3465)),
        ('p', T(3132), 'clave')],
        video=('u2_cierre', 'Síntesis de la unidad 2'), guia='Vea el video de síntesis de la unidad.',
        com='Video de cierre de la unidad 2, ya producido.'),
    lamina('Finalización de la unidad', J(T(3586).replace(' 🎉', '').replace('¡Felicitaciones por completar esta unidad! ', ''), T(3589)),
           obj='escalones', rotulo='¡Felicitaciones por completar esta unidad!', ilus='comunidad-interes-general.webp',
           com='La evaluación de la unidad (cinco preguntas de selección múltiple) va como cuestionario del aula virtual.'),
]
