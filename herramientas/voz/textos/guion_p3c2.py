# -*- coding: utf-8 -*-
"""Guion del PRIORIDAD 03 · Caso 2 «El taller del segundo piso».

ESTE CASO NO ES COMO EL PRIMERO, Y LA DIFERENCIA MANDA
    El Caso 1 preguntaba QUIEN responde. Este pregunta COMO se trata a quien
    todavia no sabemos que es. La informacion es la del primer contacto y el
    propio documento lo dice en la primera linea: nada esta judicialmente
    demostrado y la calificacion del inmueble es una hipotesis.

    Entonces el guion no puede permitirse una sola frase que suene a
    conclusion. Donde el Caso 1 decia «Victor guardo su documento», aqui hay
    que decir «Mara afirma que Saul conserva su pasaporte». La diferencia es
    todo el caso.

EL MATERIAL DIDACTICO SON LAS CUATRO PROPUESTAS EQUIVOCADAS
    El documento trae, en boca de integrantes del equipo, cuatro propuestas
    concretas: condicionar la asistencia a una denuncia y usar el nombre
    registral; suplir la version de Samuel con el informe de quien trabaja
    para Saul; descartarlo por no poder comunicarse; repetirle a Elisa un
    relato ya registrado porque «se mostro tranquila». Esas propuestas van
    LITERALES y sin comentario. El video no las corrige: las pone a la vista.

LO QUE NO VA A LOCUCION
    La amenaza de divulgar imagenes y el ofrecimiento a Elisa se enuncian en
    voz una sola vez, en lenguaje concreto y sin detalle. Nada se ilustra.

LOS RESPIROS
    <break time="0.9s" /> va a los tercios de las PALABRAS del bloque, que es
    donde la rejilla va a cortar, aunque caiga en mitad de una oracion.
"""
BLOQUES = [
 ("b1_llegada", "Carlos",
  'La información que sigue es la del primer contacto. No se tiene por '
  'demostrada la responsabilidad de nadie.\n\n'
  '<break time="0.9s" />\n\n'
  'El dieciocho de marzo de dos mil veintiséis, un equipo institucional llega '
  'a un inmueble de Cúcuta donde Saúl administra un pequeño taller de '
  'confecciones con alojamiento.'),

 ("b2_seis", "Pilar",
  'Seis personas trabajan y duermen allí. Dos conservan sus documentos, cobran '
  'por prenda y afirman que pueden terminar el contrato.\n\n'
  '<break time="0.9s" />\n\n'
  'Las otras cuatro señalan jornadas de catorce horas, descuentos por '
  'alojamiento, y una deuda que Saúl modifica sin explicar los abonos.\n\n'
  '<break time="0.9s" />\n\n'
  'No hay candados. Y ninguna versión se ha contrastado con las cuentas del '
  'taller.'),

 ("b3_mara", "Carlos",
  'Mara, mujer trans venezolana de veintiséis años, afirma que Saúl conserva '
  'su pasaporte.\n\n'
  '<break time="0.9s" />\n\n'
  'Y que le anuncia que divulgará imágenes privadas y avisará a las '
  'autoridades migratorias si abandona el lugar.'),

 ("b4_mara_sale", "Pilar",
  'Antes había ejercido trabajo sexual de manera autónoma. En el taller '
  'confecciona.\n\n'
  '<break time="0.9s" />\n\n'
  'Ha salido dos domingos y ha regresado, porque no tenía dónde dormir.\n\n'
  '<break time="0.9s" />\n\n'
  'Pide ayuda para alojamiento y atención médica. No quiere denunciar mientras '
  'su hermana siga recibiendo llamadas de Saúl. Su documento aún registra otro '
  'nombre.'),

 ("b5_propuesta_mara", "Carlos",
  'Un funcionario propone no activar la asistencia hasta que ella firme una '
  'denuncia.\n\n'
  '<break time="0.9s" />\n\n'
  'Y utilizar el nombre registral en todo contacto.'),

 ("b6_samuel", "Pilar",
  'Samuel, ecuatoriano de treinta y cinco años, tiene discapacidad auditiva y '
  'del habla. Usa señas desarrolladas en su entorno familiar, y no domina la '
  'lengua de señas colombiana.\n\n'
  '<break time="0.9s" />\n\n'
  'Observó varias entregas de documentos a Saúl, y conoce cómo se manejan las '
  'cuentas.'),

 ("b7_dario", "Carlos",
  'Interviene como supuesto traductor Darío, que trabaja para Saúl y recibe '
  'parte de los pagos.\n\n'
  '<break time="0.9s" />\n\n'
  'Darío responde antes que Samuel, y afirma que este está conforme.\n\n'
  '<break time="0.9s" />\n\n'
  'Cuando se le pregunta a Samuel por separado, el equipo no logra comprender '
  'sus respuestas.'),

 ("b8_propuesta_samuel", "Pilar",
  'Se propone suplir su versión con el informe de Darío, porque resulta más '
  'rápido.\n\n'
  '<break time="0.9s" />\n\n'
  'Otro funcionario sostiene que, como Samuel no puede comunicarse, no es un '
  'testigo útil, y debe descartarse.'),

 ("b9_elisa", "Carlos",
  'Elisa, de diecisiete años, llegó por intermedio de una tía que recibe '
  'directamente parte de su remuneración.\n\n'
  '<break time="0.9s" />\n\n'
  'Refiere que Saúl también le ofreció dinero para encuentros sexuales con '
  'clientes, y que se negó.\n\n'
  '<break time="0.9s" />\n\n'
  'Ya fue escuchada, con personal capacitado y registro audiovisual íntegro.'),

 ("b10_propuesta_elisa", "Pilar",
  'Al revisar el registro, otro funcionario solicita repetir todo el relato, '
  'porque la adolescente se mostró tranquila y omitió precisar una fecha.\n\n'
  '<break time="0.9s" />\n\n'
  'La tía insiste en acompañarla e intervenir. Elisa pide no hablar delante '
  'de ella.'),

 ("b11_patricia", "Carlos",
  'Patricia, de treinta y dos años, aparece en mensajes invitando a Mara al '
  'taller y transmitiendo instrucciones de llegada.\n\n'
  '<break time="0.9s" />\n\n'
  'Sostiene que lo hizo después de que Saúl amenazara con expulsarla junto con '
  'su hija de cuatro años, y con cobrar violentamente una deuda. Afirma que no '
  'recibió comisión.\n\n'
  '<break time="0.9s" />\n\n'
  'Se conocen los mensajes. No se ha verificado la amenaza, ni lo que ella '
  'sabía de las condiciones.'),

 ("b12_cierre", "Pilar",
  'El equipo debe decidir asistencia, canales de comunicación, condiciones de '
  'entrevista, participación y líneas de investigación.\n\n'
  '<break time="0.9s" />\n\n'
  'No hay todavía evaluación de riesgos ni verificación de las condiciones '
  'de salida.\n\n'
  '<break time="0.9s" />\n\n'
  'Que el inmueble sea un lugar de trata es, por ahora, una hipótesis. Y no '
  'una conclusión común respecto de todas las personas que trabajan allí.'),
]

# La votacion es la unica discusion que el documento trae con DOS posiciones
# expresas enfrentadas, y por eso es la que se vota. Las otras tres propuestas
# quedan en el cuerpo de la pieza y en la tarea del foro.
VOTACION = {
    'pregunta': '¿Cómo se trata la intervención de Patricia?',
    'opciones': [
        'a) Es coautora de trata desde ya: los mensajes de invitación están.',
        'b) Ser también víctima excluye cualquier examen de su intervención.',
        'c) No se califica todavía: falta verificar la amenaza y qué sabía.',
    ],
    'foro': ('Escoja una de las cuatro personas y diga qué hace el equipo '
             'primero con ella, y por qué. Y diga qué haría falta saber antes '
             'de calificar el inmueble.'),
}

if __name__ == "__main__":
    import re
    tot = 0
    print('%-22s %-7s %8s %8s' % ('bloque', 'voz', 'palabras', 'respiros'))
    for n, v, t in BLOQUES:
        limpio = re.sub(r'<break[^>]*/>', ' ', t)
        p = len([w for w in limpio.split() if any(c.isalnum() for c in w)])
        tot += p
        print('%-22s %-7s %8d %8d' % (n, v, p, t.count('<break')))
    print('\n%d palabras' % tot)
    for ppm in (130, 137, 145):
        s = tot / float(ppm) * 60
        print('   a %d ppm: %5.1f s de narracion  ->  pieza de %4.1f s (%d:%02d)'
              % (ppm, s, s + 82, int(s + 82) // 60, int(s + 82) % 60))
