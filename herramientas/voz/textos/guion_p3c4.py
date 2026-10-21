# -*- coding: utf-8 -*-
"""Guion del PRIORIDAD 03 · Caso 4 «Puerto de salida».

ESTE CASO TIENE UNA FORMA QUE LOS TRES ANTERIORES NO TIENEN
    El Caso 1 preguntaba QUIEN responde. El Caso 2, COMO se trata a quien
    todavia no sabemos que es. El Caso 3, QUE HIPOTESIS siguen justificadas
    cuando los resultados vuelven en contra. Este pregunta:

        que tiene que estar sustentado, caso por caso, en cada acto que
        restringe un derecho.

    Y la forma sale del documento sin que haya que forzarla: son seis escenas
    de actuaciones SUCESIVAS, y en cada una hay un acto bien sustentado al
    lado de uno que no lo esta. Eso es nuevo. En los tres casos anteriores lo
    que se ponia a la vista era el error; aqui el error se lee porque esta
    pegado a su version correcta, en la misma escena y sobre el mismo
    expediente.

    La captura de Nora se hace con orden vigente, hora real y control dentro
    del termino; la del recepcionista, sin orden y sin acto descrito. La
    Fiscalia pide la medida sobre Nora con la inferencia desarrollada y
    reconociendo lo que NO demostro; la jueza la decide por alarma social. La
    imputacion de Ivan individualiza conducta, irregularidad y finalidad; la
    de Lina cabe en una frase. Esa simetria es el material didactico y hay
    que dejarla ver: el guion narra siempre primero lo sustentado.

LAS SIETE PROPUESTAS Y DECISIONES, LITERALES Y SIN COMENTARIO
    Son mas que las cuatro del Caso 2 y las tres del Caso 3, porque el
    documento trae una o dos por escena. Van LITERALES a carton y NUNCA sobre
    una cara, por la misma razon de siempre: poner «no puede oirse porque yo
    ya presente la mia» encima del primer plano de Ivan convierte en algo que
    a el le pasa lo que en realidad el fiscal dice.

    1 incluir todas las cuentas de los familiares de Ivan durante cinco anios
    2 ordenar el registro del segundo inmueble invocando la gravedad
    3 fundar la legalizacion unicamente en que la trata puede ser permanente
    4 imponer intramural por alarma social, y la domiciliaria como sustituto
    5 esa peticion no puede oirse porque yo ya presente la mia
    6 el silencio previo de la defensa sana el defecto
    7 las tres modificaciones son simples precisiones

    La 4 la dice una JUEZA, no un integrante del equipo. Es la unica de la
    serie que no es una propuesta sino una decision tomada, y va en carton
    igual, en la misma retorica neutra. Ver personajes_p3c4.md para por que
    ni ella ni ningun otro rol se dibuja con cara.

LO QUE NO VA A LOCUCION, Y LO QUE SI
    La imputacion de Lina va TEXTUAL, en voz y en carton. Es el unico
    verbatim del caso y es justamente el objeto del ejercicio: lo que se
    discute es si esa frase individualiza algo. Parafrasearla seria contestar
    la pregunta antes de hacerla.

    Los numeros van a los cartones, no a la voz, salvo los que la frase
    necesita para existir -seis meses, cinco anios, treinta y seis horas-, y
    esos van en letras, que es como ElevenLabs los lee bien.

    No se ilustra ningun hecho: ni una captacion, ni una imposicion de deuda,
    ni una amenaza en acto, ni una captura. Nada de eso esta demostrado y el
    documento lo dice en su primera linea.

LOS RESPIROS
    <break time="0.9s" /> va a los tercios de las PALABRAS del bloque, que es
    donde la rejilla va a cortar, aunque caiga en mitad de una oracion.
"""
BLOQUES = [
 ("b01_apertura", "Carlos",
  'Las escenas que siguen pertenecen a actuaciones sucesivas de la misma '
  'investigación. Las calificaciones preliminares no convierten en demostrados '
  'los hechos que se debaten.\n\n'
  '<break time="0.9s" />\n\n'
  'La investigación vincula a Nora con la captación de Inés y Alba, ambas '
  'adultas, mediante ofertas de trabajo.\n\n'
  '<break time="0.9s" />\n\n'
  'Y con su recepción en un alojamiento donde se les impondrían servicios '
  'sexuales y deuda.'),

 ("b02_las_dos_lineas", "Pilar",
  'Existen entrevistas, conversaciones atribuidas a Nora, y registros de '
  'viaje.\n\n'
  '<break time="0.9s" />\n\n'
  'En otra línea, Iván aparece coordinando transporte interno hacia un punto '
  'de salida a Panamá, con instrucciones para evitar controles y cobro de '
  'comisión.\n\n'
  '<break time="0.9s" />\n\n'
  'La identidad de los pasajeros, y la regulación migratoria aplicable a ese '
  'episodio, ya fueron individualizadas en la carpeta.'),

 ("b03_solicitud", "Carlos",
  'Primera actuación. El fiscal dispone una búsqueda de información financiera '
  'sobre una cuenta vinculada con cobros de la ruta.\n\n'
  '<break time="0.9s" />\n\n'
  'Y propone pedir autorización por seis meses.'),

 ("b04_prop_cuentas", "Pilar",
  'El investigador sugiere incluir todas las cuentas de los familiares de Iván '
  'durante cinco años.\n\n'
  '<break time="0.9s" />\n\n'
  'Porque, dice, las redes suelen usar terceros.'),

 ("b05_prop_registro", "Carlos",
  'Sobre un inmueble distinto solo existe un comentario de barrio: allí se ven '
  'extranjeros.\n\n'
  '<break time="0.9s" />\n\n'
  'El fiscal pretende ordenar el registro de ese segundo inmueble invocando la '
  'gravedad de la trata.\n\n'
  '<break time="0.9s" />\n\n'
  'Sin otra información que lo conecte con el delito.'),

 ("b06_captura_nora", "Pilar",
  'Segunda actuación. Nora es capturada en ejecución de una orden judicial '
  'vigente.\n\n'
  '<break time="0.9s" />\n\n'
  'Se registra la hora real de la aprehensión, se le informan sus derechos, y '
  'el control se realiza dentro de las treinta y seis horas.'),

 ("b07_recepcionista", "Carlos",
  'Un recepcionista que llega después al alojamiento es detenido sin orden, '
  'porque su nombre aparece en un informe sobre hechos de dos meses antes.\n\n'
  '<break time="0.9s" />\n\n'
  'No se describen actos delictivos que estuviera realizando. Ni una hipótesis '
  'concreta de flagrancia.'),

 ("b08_prop_permanente", "Pilar",
  'El investigador propone fundar la legalización únicamente en que la trata '
  'puede ser permanente.'),

 ("b09_medida_nora", "Carlos",
  'Tercera actuación. Tras una imputación individualizada, la Fiscalía '
  'desarrolla con detalle la inferencia de intervención, y pide detención en '
  'residencia.\n\n'
  '<break time="0.9s" />\n\n'
  'Invoca riesgo de reiteración mediante coordinación remota, explica por qué '
  'considera insuficientes las medidas no privativas, y propone condiciones '
  'para contenerlo.\n\n'
  '<break time="0.9s" />\n\n'
  'Reconoce que no ha demostrado fuga ni obstrucción.'),

 ("b10_decision_jueza", "Pilar",
  'La defensa controvierte la actualidad del riesgo, y ofrece datos de cese de '
  'la actividad.\n\n'
  '<break time="0.9s" />\n\n'
  'La jueza impone detención intramural por la alarma social que genera el '
  'delito. Y porque estima que la domiciliaria solo puede existir como '
  'sustituto.\n\n'
  '<break time="0.9s" />\n\n'
  'No anuncia previamente un posible apartamiento, ni permite discutirlo.'),

 ("b11_medida_ivan", "Carlos",
  'Cuarta actuación. Sobre Iván, la Fiscalía solicita únicamente una medida no '
  'privativa, para asegurar comparecencia.\n\n'
  '<break time="0.9s" />\n\n'
  'La representante de una persona afectada aporta mensajes nuevos, atribuidos '
  'a Iván, que contienen amenazas posteriores a la denuncia. Y solicita una '
  'cautela privativa por protección.'),

 ("b12_prop_no_se_oye", "Pilar",
  'El fiscal sostiene que esa petición no puede oírse, porque él ya presentó '
  'la suya.\n\n'
  '<break time="0.9s" />\n\n'
  'La defensa pide conocer los mensajes, y controvertir su atribución antes de '
  'la decisión.'),

 ("b13_imputacion_lina", "Carlos",
  'Quinta actuación, en audiencia distinta. La imputación de una tercera '
  'investigada, Lina, se formula únicamente así:\n\n'
  '<break time="0.9s" />\n\n'
  '«Durante dos mil veinticuatro y dos mil veinticinco usted captó, trasladó y '
  'acogió a varias mujeres con fines de explotación sexual en esta ciudad».\n\n'
  '<break time="0.9s" />\n\n'
  'Se cita el artículo ciento ochenta y ocho A. Pero no se individualizan '
  'víctimas, episodios, actos, ni finalidad concreta. El juez le imparte '
  'legalidad.'),

 ("b14_prop_silencio", "Pilar",
  'Al preparar la acusación, otra fiscal propone detallar por primera vez los '
  'actos atribuidos a Lina respecto de Inés y Alba, con apoyo en entrevistas '
  'que ya estaban en la carpeta.\n\n'
  '<break time="0.9s" />\n\n'
  'Y considera que el silencio previo de la defensa sana el defecto.'),

 ("b15_imputacion_ivan", "Carlos",
  'Sexta actuación. La imputación de Iván sí describió suficientemente un '
  'episodio de facilitación ocurrido en febrero, respecto de cuatro '
  'pasajeros.\n\n'
  '<break time="0.9s" />\n\n'
  'Con conducta, irregularidad y finalidad individualizadas.'),

 ("b16_tres_modificaciones", "Pilar",
  'El proyecto de acusación agrega dos viajes realizados en junio, respecto de '
  'personas distintas.\n\n'
  '<break time="0.9s" />\n\n'
  'Corrige la dirección del lugar de entrega del episodio de febrero, sin '
  'cambiar el sitio material ni la conducta comunicada.\n\n'
  '<break time="0.9s" />\n\n'
  'Y añade la circunstancia de agravación del numeral diez del artículo ciento '
  'ochenta y ocho B, por la coordinación mediante una aplicación de '
  'mensajería.'),

 ("b17_prop_precisiones", "Carlos",
  'El equipo trata las tres modificaciones como simples precisiones.\n\n'
  '<break time="0.9s" />\n\n'
  'Y pretende descubrir toda la información en una sola carpeta rotulada '
  '«informe de policía judicial y anexos». Sin índice, y sin separación de '
  'entrevistas, registros y extracciones.'),

 ("b18_cierre", "Pilar",
  'El equipo debe revisar, una por una, las seis actuaciones.\n\n'
  '<break time="0.9s" />\n\n'
  'Qué se pidió, con qué sustento y con qué alcance. Qué se decidió, y sobre '
  'qué se apoyó esa decisión.\n\n'
  '<break time="0.9s" />\n\n'
  'Y qué se descubre, en qué orden y con qué separación, para que pueda ser '
  'controvertido.'),
]

# Siete, y van las siete a carton, literales. La cuarta es una DECISION
# tomada por una jueza, no una propuesta de un integrante del equipo; va
# igual, en la misma retorica neutra, y sin cara debajo.
PROPUESTAS = [
    ('prop1_cuentas', 'b04_prop_cuentas', 'el investigador',
     'Incluir todas las cuentas de los familiares de Iván durante cinco años'),
    ('prop2_registro', 'b05_prop_registro', 'el fiscal',
     'Ordenar el registro del segundo inmueble invocando la gravedad de la '
     'trata'),
    ('prop3_permanente', 'b08_prop_permanente', 'el investigador',
     'Fundar la legalización únicamente en que la trata puede ser permanente'),
    ('prop4_alarma', 'b10_decision_jueza', 'la jueza',
     'Imponer detención intramural por la alarma social que genera el delito'),
    ('prop5_no_se_oye', 'b12_prop_no_se_oye', 'el fiscal',
     'Esa petición no puede oírse porque él ya presentó la suya'),
    ('prop6_silencio', 'b14_prop_silencio', 'otra fiscal',
     'El silencio previo de la defensa sana el defecto'),
    ('prop7_precisiones', 'b17_prop_precisiones', 'el equipo',
     'Las tres modificaciones son simples precisiones'),
]

# El unico verbatim del caso. Va en voz y en carton: lo que se discute es si
# esa frase individualiza algo, y parafrasearla contesta la pregunta.
VERBATIM = {
    'cap01_imputacion_lina': (
        '«Durante 2024 y 2025 usted captó, trasladó y acogió a varias mujeres '
        'con fines de explotación sexual en esta ciudad»'),
}

# Tres graficas de motion, y cada una se gana el lugar.
GRAFICAS = {
    'g1_seis_actuaciones': (
        'La cadena: solicitudes, capturas, medida sobre Nora, medida sobre '
        'Iván, imputación de Lina, acusación de Iván. Orienta en siete '
        'segundos una pieza que salta de audiencia en audiencia.'),
    'g2_sustento': (
        'ES el caso. Dos columnas: lo que se expuso y lo que se invocó en su '
        'lugar, actuación por actuación. La asimetría es el contenido.'),
    'g3_tres_modificaciones': (
        'Las tres de Iván. Dos viajes nuevos de junio sobre personas '
        'distintas · la dirección corregida, mismo sitio y misma conducta · '
        'la agravación del numeral diez. Una de las tres no es como las '
        'otras dos, y esa asimetría es la lección.'),
}

# No hay cartones de pregunta en la pieza: formato nuevo. Esto es para la
# implementacion web.
VOTACION = {
    'pregunta': '¿Qué sustenta la detención del recepcionista?',
    'opciones': [
        'a) Que la trata puede ser permanente, y por eso la situación continúa.',
        'b) Nada que se haya descrito: no hay orden ni acto concreto.',
        'c) El informe de hace dos meses, que ya lo vinculaba al alojamiento.',
    ],
    'foro': ('Escoja una de las seis actuaciones y diga qué quedó expuesto en '
             'ella y qué se invocó en su lugar. Y diga qué haría falta para '
             'que ese mismo acto quedara sustentado.'),
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
    for ppm in (130, 137, 145):
        s = tot / float(ppm) * 60
        print('   a %d ppm: %5.1f s de narracion  ->  pieza de %5.1f s (%d:%02d)'
              % (ppm, s, s + 50, int(s + 50) // 60, int(s + 50) % 60))
