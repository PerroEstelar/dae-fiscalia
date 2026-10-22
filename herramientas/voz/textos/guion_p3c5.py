# -*- coding: utf-8 -*-
"""Guion del PRIORIDAD 03 · Caso 5 «Voces, registros y cuentas».

ESTE CASO PREGUNTA ALGO QUE LOS CUATRO ANTERIORES NO PREGUNTAN
    El Caso 1 preguntaba QUIEN responde. El Caso 2, COMO se trata a quien
    todavia no sabemos que es. El Caso 3, QUE HIPOTESIS siguen justificadas
    cuando los resultados vuelven en contra. El Caso 4, QUE TIENE QUE ESTAR
    SUSTENTADO en cada acto que restringe un derecho. Este pregunta:

        que queda probado, contra quien, y con que.

    Y no hay que deducirlo: el documento lo dice en su primera linea. «Debe
    diferenciarse el medio ofrecido de la informacion finalmente admitida y
    practicada.» Toda la pieza es la distancia entre esas dos cosas.

LA FORMA ES NUEVA: ESTE CASO TIENE UN ANTES Y UN DESPUES
    Los cuatro anteriores ocurren en un momento. Este corre en dos -audiencia
    preparatoria y juicio- sobre el MISMO expediente, y entre los dos hay un
    parrafo que el documento titula «resultado de la practica probatoria».

    Ese parrafo es el eje. Mismo juicio, mismo esfuerzo probatorio, y dos
    desenlaces opuestos: contra Oscar quedan establecidos la recepcion, el
    mantenimiento bajo amenazas, el conocimiento y el proposito; contra Tomas
    quedan la titularidad de una cuenta y un viaje interno, y nada mas.

    LA ASIMETRIA ES EL CONTENIDO. Es la misma figura del Caso 3 -tres se
    desarman y la de Teresa no- pero aqui no separa hipotesis: separa
    PERSONAS. Por eso la pieza no se puede montar como un listado de errores
    en orden: hay que llegar a ese parrafo y hacerlo pesar.

HEREDA DEL CASO 4 EL ERROR PEGADO A SU VERSION CORRECTA
    El Caso 4 dejo construido que el error se lee mejor cuando esta al lado
    de lo que si estaba sustentado. Aqui pasa igual y en casi todos los
    beats, porque el documento los escribio asi:

        el descubrimiento fue oportuno        /  la peticion es unitaria
        Andres vio entregar la habitacion     /  el telefono lo hallo otra
        la interlocutora reconoce la grabacion/  la otra voz no esta establecida
        Renata esta ubicable y acepta declarar/  «la migracion vuelve imposible»
        la perita observo afectaciones        /  y ofrece calificar credibilidad
        los extractos se descubrieron a tiempo/  la grafica no separa nada
        Lucia consulta una anotacion y recuerda/ y despues niega lo que describio
        la defensa quiere examinar el recuerdo/  y pregunta afirmando

    No es repeticion del Caso 4: alli la simetria caia sobre actos que
    restringen derechos; aqui cae sobre MEDIOS DE PRUEBA. Es la misma
    gramatica aplicada a otra materia, que es justo lo que cierra la serie.

LAS NUEVE AFIRMACIONES, LITERALES Y SIN COMENTARIO
    Van a carton, literales, y NUNCA sobre una cara. La razon es la de
    siempre: poner «debe explicar el dinero para evitar la condena» encima
    del primer plano de Tomas convierte en algo que a el le pasa lo que en
    realidad el fiscal dice.

    Son nueve y no siete porque el documento trae afirmaciones en los cuatro
    momentos. Tres de ellas -las del alegato- son el unico tramo del caso
    donde las afirmaciones se dicen DESPUES de saber que se probo, y por eso
    van juntas, en una sola secuencia.

    La ultima la hace LA DEFENSA, no la Fiscalia. Va en carton igual y en la
    misma retorica neutra: el caso no es un reparto de buenos y malos.

LO QUE NO VA A LOCUCION, Y LO QUE SI
    Las anotaciones del cuaderno -«abono», «multa por salir», «falta»- van a
    carton y tambien a voz. Son tres palabras y son el material del caso: lo
    que se discute es si un cuaderno hallado en el inmueble prueba la
    finalidad de explotacion, y esas tres palabras son lo unico concreto que
    el documento da de su contenido.

    La sustentacion de la pertinencia va TEXTUAL, en voz y en carton. Es el
    verbatim central: lo que se discute es si esa frase dice algo, y
    parafrasearla contesta la pregunta antes de hacerla.

    Los numeros van en letras -seis meses, cuatro informes, una tercera
    mujer-, que es como ElevenLabs los lee bien.

    NO SE ILUSTRA NINGUN HECHO NO PROBADO. Ni una imposicion de deuda, ni una
    amenaza en acto, ni una entrega al guia, ni un cruce de frontera. El
    documento dice en su primera linea que las decisiones se limitan a los
    hechos expresamente suministrados, y la mitad del caso consiste en que
    contra Tomas eso no se probo.

LOS RESPIROS
    <break time="0.9s" /> va a los tercios de las PALABRAS del bloque, que es
    donde la rejilla va a cortar, aunque caiga en mitad de una oracion.
"""

BLOQUES = [
 ("b01_apertura", "Carlos",
  'Las escenas que siguen pertenecen a dos momentos de la misma actuación: '
  'la audiencia preparatoria y el juicio.\n\n'
  '<break time="0.9s" />\n\n'
  'En cada una hay que diferenciar el medio que se ofrece de la información '
  'que finalmente se admite y se practica.\n\n'
  '<break time="0.9s" />\n\n'
  'Las decisiones evaluadas se limitan a los hechos y condiciones expresamente '
  'suministrados.'),

 ("b02_acusacion", "Pilar",
  'La acusación atribuye a Óscar haber recibido y acogido a Lucía y a Renata, '
  'ambas adultas, entre enero y marzo de dos mil veintiséis, en un '
  'alojamiento de Medellín, para obtener beneficio '
  'mediante servicios sexuales impuestos bajo deuda y amenazas.\n\n'
  '<break time="0.9s" />\n\n'
  'A Tomás le atribuye facilitar una salida irregular hacia Panamá, '
  'coordinando una entrega a un guía y cobrando comisión.'),

 ("b03_lo_que_no_se_acusa", "Carlos",
  'Los cargos individualizan episodios, sujetos y elementos.\n\n'
  '<break time="0.9s" />\n\n'
  'No se acusa a Óscar por captar a una tercera mujer. No se acusa a Tomás '
  'por pertenecer a una organización.'),

 ("b04_informe_unitario", "Pilar",
  'En la audiencia preparatoria, la Fiscalía solicita el informe con todos '
  'sus anexos: dos entrevistas, un acta de incautación firmada por Óscar, '
  'fotografías, el registro de huéspedes, extractos bancarios y una '
  'extracción de teléfono.\n\n'
  '<break time="0.9s" />\n\n'
  'La defensa admite haber recibido todos esos elementos oportunamente, y '
  'poder localizarlos.\n\n'
  '<break time="0.9s" />\n\n'
  'El problema de la petición es su tratamiento unitario, y la falta de '
  'funciones diferenciadas.'),

 ("b05_andres", "Carlos",
  'El informe mezcla percepciones del investigador Andrés con lo dicho por '
  'los migrantes.\n\n'
  '<break time="0.9s" />\n\n'
  'Andrés sí observó a Óscar entregar una habitación a Lucía. El teléfono lo '
  'halló otra funcionaria, que después se lo entregó.'),

 ("b06_cuaderno", "Pilar",
  'Entre los elementos hallados en el registro del alojamiento hay un '
  'cuaderno manuscrito. Una columna de nombres —entre ellos Lucía y '
  'Renata—, fechas, cifras diarias.\n\n'
  '<break time="0.9s" />\n\n'
  'Y anotaciones: abono, multa por salir, falta.'),

 ("b07_pertinencia", "Carlos",
  'La Fiscalía pretende introducirlo para demostrar la finalidad de '
  'explotación.\n\n'
  '<break time="0.9s" />\n\n'
  'Al sustentar la pertinencia dice únicamente que es pertinente porque fue '
  'hallado en el inmueble donde ocurrieron los hechos, y se refiere a las '
  'víctimas.'),

 ("b08_estipulacion", "Pilar",
  'Las partes acuerdan tener por probado que una cuenta bancaria estaba a '
  'nombre de Tomás.\n\n'
  '<break time="0.9s" />\n\n'
  'La Fiscalía pretende añadir, como efecto de esa estipulación, que todos '
  'los movimientos corresponden a comisiones de tráfico.'),

 ("b09_interceptaciones", "Carlos",
  'Pide también todas las interceptaciones de una línea durante seis meses, '
  'sin precisar sesiones ni contenido.\n\n'
  '<break time="0.9s" />\n\n'
  'En la carpeta hay una grabación en la que Óscar anuncia a Lucía que no '
  'puede irse sin pagar, y la propia interlocutora puede reconocerla. Otra '
  'voz habla sobre la entrega, pero aún no se ha establecido quién es ni a '
  'qué se refiere.'),

 ("b10_renata", "Pilar",
  'Renata reside ahora fuera del país. Mantiene contacto con el equipo y '
  'acepta declarar mediante un mecanismo que permita preguntas de las '
  'partes.\n\n'
  '<break time="0.9s" />\n\n'
  'La Fiscalía considera más sencillo incorporar su entrevista a través de '
  'Andrés, porque la migración vuelve imposible su comparecencia.'),

 ("b11_perita", "Carlos",
  'Una psicóloga ofrece explicar las afectaciones que observó.\n\n'
  '<break time="0.9s" />\n\n'
  'Y ofrece, además, declarar que ambas mujeres son creíbles, porque sus '
  'relatos coinciden con un perfil de víctima de trata.'),

 ("b12_financiero", "Pilar",
  'El análisis financiero presenta una gráfica de flujos, construida con '
  'extractos oportunamente descubiertos.\n\n'
  '<break time="0.9s" />\n\n'
  'La gráfica no separa remesas, gastos y comisiones.'),

 ("b13_lucia_fecha", "Carlos",
  'Durante el juicio, Lucía no recuerda al comienzo la fecha de llegada.\n\n'
  '<break time="0.9s" />\n\n'
  'Consulta una anotación previamente descubierta, y entonces la recuerda.'),

 ("b14_lucia_amenaza", "Pilar",
  'Más adelante sostiene que no recibió de Óscar una amenaza que sí había '
  'descrito antes.\n\n'
  '<break time="0.9s" />\n\n'
  'La Fiscalía intenta leer íntegra la entrevista, como si los dos incidentes '
  'permitieran la misma técnica. Y atribuye a la perita la tarea de decidir '
  'cuál versión es verdadera.'),

 ("b15_defensa_juicio", "Carlos",
  'La defensa quiere examinar las condiciones del recuerdo, y el control de '
  'los ingresos.\n\n'
  '<break time="0.9s" />\n\n'
  'Una de sus preguntas afirma que quien regresa voluntariamente a un '
  'alojamiento nunca puede estar sometido.'),

 ("b16_resultado_oscar", "Pilar",
  'Resultado de la práctica probatoria.\n\n'
  '<break time="0.9s" />\n\n'
  'Respecto de Óscar, las declaraciones admitidas de Lucía y Renata, una '
  'conversación atribuida a él y la cuenta de deuda reconocida permiten tener '
  'por establecidos la recepción, el mantenimiento bajo amenazas, el '
  'conocimiento y el propósito de obtener beneficios.\n\n'
  '<break time="0.9s" />\n\n'
  'El acta firmada no se utiliza como confesión, y la perita explica límites '
  'clínicos.'),

 ("b17_resultado_tomas", "Carlos",
  'Respecto de Tomás solo quedaron probados la titularidad de una cuenta, y '
  'un viaje interno.\n\n'
  '<break time="0.9s" />\n\n'
  'Existen usuarios compartidos de la cuenta. Los datos no identifican quién '
  'emitió la instrucción de entrega, ni quién recibió la comisión, ni que '
  'Tomás conociera el cruce irregular.\n\n'
  '<break time="0.9s" />\n\n'
  'La estipulación solo comprendió titularidad.'),

 ("b18_alegato_fiscalia", "Pilar",
  'En el alegato, la Fiscalía sostiene tres cosas.\n\n'
  '<break time="0.9s" />\n\n'
  'Que cuatro informes que reproducen las entrevistas equivalen a cuatro '
  'corroboraciones independientes. Que Tomás debe explicar el dinero para '
  'evitar la condena.\n\n'
  '<break time="0.9s" />\n\n'
  'Y que Óscar también captó a una tercera mujer, mencionada por primera vez '
  'en juicio, por lo que debe condenarse además por ese episodio.'),

 ("b19_alegato_defensa", "Carlos",
  'La defensa afirma, en sentido opuesto, que la ausencia de encierro y el '
  'pago parcial a Lucía excluyen cualquier trata.'),

 ("b20_cierre", "Pilar",
  'El equipo debe revisar, medio por medio, qué se ofreció y qué se admitió.\n\n'
  '<break time="0.9s" />\n\n'
  'Para qué servía cada elemento, y para qué se lo usó. Qué quedó probado, '
  'contra quién, y con qué.\n\n'
  '<break time="0.9s" />\n\n'
  'Y qué habría hecho falta para probar lo que se afirmó.'),
]

# Nueve, y van las nueve a carton, literales. La novena la hace la DEFENSA.
# Las tres del alegato (6, 7, 8) van juntas porque son el unico tramo donde
# se afirma DESPUES de saber que se probo.
PROPUESTAS = [
    ('prop1_informe', 'b04_informe_unitario', 'la Fiscalía',
     'El informe con todos sus anexos, como una sola petición'),
    ('prop2_pertinencia', 'b07_pertinencia', 'la Fiscalía',
     'Es pertinente porque fue hallado en el inmueble donde ocurrieron los '
     'hechos y se refiere a las víctimas'),
    ('prop3_estipulacion', 'b08_estipulacion', 'la Fiscalía',
     'Que todos los movimientos de la cuenta corresponden a comisiones de '
     'tráfico'),
    ('prop4_interceptaciones', 'b09_interceptaciones', 'la Fiscalía',
     'Todas las interceptaciones de una línea durante seis meses, sin '
     'precisar sesiones ni contenido'),
    ('prop5_renata', 'b10_renata', 'la Fiscalía',
     'La migración vuelve imposible su comparecencia'),
    ('prop6_credibilidad', 'b11_perita', 'la psicóloga',
     'Que ambas mujeres son creíbles porque sus relatos coinciden con un '
     'perfil de víctima de trata'),
    ('prop7_cuatro_informes', 'b18_alegato_fiscalia', 'la Fiscalía',
     'Cuatro informes que reproducen las entrevistas equivalen a cuatro '
     'corroboraciones independientes'),
    ('prop8_explicar', 'b18_alegato_fiscalia', 'la Fiscalía',
     'Tomás debe explicar el dinero para evitar la condena'),
    ('prop9_sin_encierro', 'b19_alegato_defensa', 'la defensa',
     'La ausencia de encierro y el pago parcial excluyen cualquier trata'),
]

# Dos verbatim. El cuaderno porque son lo unico concreto que el documento da
# de su contenido; la sustentacion porque es el objeto del ejercicio.
VERBATIM = {
    'cap01_cuaderno': '«abono» · «multa por salir» · «falta»',
    'cap02_pertinencia': (
        '«Es pertinente porque fue hallado en el inmueble donde ocurrieron '
        'los hechos y se refiere a las víctimas»'),
}

# Tres graficas de motion, y cada una se gana el lugar.
GRAFICAS = {
    'g1_dos_momentos': (
        'La barra de la actuacion: preparatoria y juicio, con el resultado de '
        'la practica probatoria entre los dos. Orienta en siete segundos una '
        'pieza que corre en dos tiempos, que es lo que la distingue de las '
        'otras cuatro.'),
    'g2_oscar_y_tomas': (
        'ES el caso. Dos columnas, Oscar y Tomas: que se atribuyo y que quedo '
        'probado. Del lado de Oscar la columna derecha se llena; del de Tomas '
        'quedan dos lineas. La asimetria es el contenido y no hay que '
        'comentarla.'),
    'g3_un_relato_cuatro_informes': (
        'Los cuatro informes del alegato. Cuatro documentos que se abren y '
        'se ve que los cuatro apuntan a la MISMA entrevista. Una fuente '
        'repetida cuatro veces sigue siendo una fuente, y eso en dos '
        'renglones de locucion se pierde.'),
}

# No hay cartones de pregunta en la pieza: formato nuevo. Esto es para la
# implementacion web.
VOTACION = {
    'pregunta': '¿Qué permite tener por probada la comisión que se atribuye a Tomás?',
    'opciones': [
        'a) La estipulación, que tuvo por probada la cuenta a su nombre.',
        'b) La gráfica de flujos del análisis financiero.',
        'c) Nada de lo practicado: la cuenta tiene usuarios compartidos y los '
        'datos no identifican quién dio la instrucción ni quién cobró.',
    ],
    'foro': ('Escoja uno de los medios ofrecidos en la preparatoria y diga '
             'para qué servía y para qué se lo quiso usar. Y diga qué habría '
             'hecho falta para que sirviera para eso segundo.'),
}

if __name__ == "__main__":
    import re
    tot = 0
    print('%-26s %-7s %8s %8s' % ('bloque', 'voz', 'palabras', 'respiros'))
    for n, v, t in BLOQUES:
        limpio = re.sub(r'<break[^>]*/>', ' ', t)
        p = len([w for w in limpio.split() if any(c.isalnum() for c in w)])
        tot += p
        print('%-26s %-7s %8d %8d' % (n, v, p, t.count('<break')))
    voces = {}
    for n, v, t in BLOQUES:
        voces[v] = voces.get(v, 0) + 1
    print('\n%d palabras  ·  %d bloques  ·  %s' % (
        tot, len(BLOQUES), ', '.join('%s %d' % kv for kv in sorted(voces.items()))))
    print('%d propuestas a carton  ·  %d verbatim  ·  %d graficas' % (
        len(PROPUESTAS), len(VERBATIM), len(GRAFICAS)))
    for ppm in (130, 137, 145):
        s = tot / float(ppm) * 60
        print('   a %d ppm: %5.1f s de narracion  ->  pieza de %5.1f s (%d:%02d)'
              % (ppm, s, s + 50, int(s + 50) // 60, int(s + 50) % 60))
