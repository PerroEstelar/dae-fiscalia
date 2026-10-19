# -*- coding: utf-8 -*-
"""Guion del PRIORIDAD 03 · Caso 1 «El hospedaje El Mirador».

Regla de la casa: el guion NO afirma contenido juridico que el texto fuente no
enuncie. Aqui se describe a cada persona y la circunstancia que la distingue, y
se deja la pregunta abierta. Ninguna frase dice quien responde por trata.

EL EJE DEL CASO
    El mismo hospedaje, nueve personas, y ninguna en la misma posicion. La
    frase bisagra la trae el propio caso y hay que decirla temprano: «En el
    mismo inmueble se arrendaban habitaciones a huespedes y a personas que
    trabajaban por cuenta propia. No todas estaban sometidas a las mismas
    condiciones.»

    Y la trampa que el ejercicio tiende con cuidado: «podia salir» aparece en
    Daniela, en Elena y en Paula, y significa una cosa distinta en cada una.
    El montaje tiene que dejarlo ver sin resolverlo.

LO QUE NO VA A LOCUCION
    Los mensajes de Yeimi y la frase de Cristina van a CARTON, no a voz. Es la
    regla de la biblia: el material duro va a texto en pantalla y en locucion
    queda el lenguaje concreto. Ademas son citas textuales y en pantalla se
    leen como lo que son.

LOS RESPIROS
    <break time="0.9s" /> va donde la rejilla va a cortar -a los tercios de las
    PALABRAS del bloque-, aunque caiga en mitad de una oracion. Es lo que hace
    que el iman encuentre el corte dentro de un silencio medido.
"""
BLOQUES = [
 ("b1_encargo", "Carlos",
  'Para este ejercicio, los hechos se tienen por establecidos.\n\n'
  '<break time="0.9s" />\n\n'
  'Entre enero y mayo de dos mil veinticinco, Cristina y Víctor mantuvieron un '
  'acuerdo para vincular mujeres al hospedaje El Mirador, en Bucaramanga.'),

 ("b2_acuerdo", "Pilar",
  'Cristina las conseguía con ofertas de empleo publicadas desde una cuenta de '
  'Instagram, y organizaba su llegada. Víctor las recibía y disponía las '
  'condiciones.\n\n'
  '<break time="0.9s" />\n\n'
  'Deudas impuestas por viaje y alojamiento, y ninguna decisión libre sobre '
  'cuándo terminar.\n\n'
  '<break time="0.9s" />\n\n'
  'El acuerdo no se limitaba a unas personas identificadas: pretendían '
  'mantenerlo mientras el negocio produjera ganancias.'),

 ("b3_bisagra", "Carlos",
  'En el mismo inmueble se arrendaban habitaciones a huéspedes, y a personas '
  'que trabajaban por cuenta propia.\n\n'
  '<break time="0.9s" />\n\n'
  'No todas estaban sometidas a las mismas condiciones.'),

 ("b4_daniela", "Pilar",
  'Daniela, de veintitrés años, viajó desde Cúcuta tras una oferta de empleo '
  'como mesera. Cristina sabía que Víctor no pretendía contratarla.\n\n'
  '<break time="0.9s" />\n\n'
  'Víctor guardó su documento, le informó que debía tres millones de pesos, y '
  'que tendría que atender encuentros sexuales para pagar. Cuando se negó, la '
  'amenazó con hacer agredir a su hermano.'),

 ("b5_salir", "Carlos",
  'Daniela podía salir a comprar alimentos. Pero no abandonar el lugar '
  'mientras existiera la deuda.\n\n'
  '<break time="0.9s" />\n\n'
  'Desde la terminal la había llevado Camilo, conductor particular, que cobró '
  'la tarifa habitual. Entonces desconocía el acuerdo.'),

 ("b6_paula", "Pilar",
  'Paula, de veintinueve años, ejercía trabajo sexual autónomo. Le preguntó a '
  'Cristina la dirección del hospedaje, y Cristina se limitó a dársela.\n\n'
  '<break time="0.9s" />\n\n'
  'Pagó su viaje, conservó sus documentos y administró sus ingresos. Podía '
  'rechazar personas, no trabajar, o retirarse sin penalidad.\n\n'
  '<break time="0.9s" />\n\n'
  'Permaneció diez días y se marchó.'),

 ("b7_elena", "Carlos",
  'Elena, venezolana de treinta y cinco años con residencia regular, le '
  'solicitó a Víctor trabajo de limpieza. Los primeros meses recibió la '
  'remuneración pactada.\n\n'
  '<break time="0.9s" />\n\n'
  'En abril, tras prestarle dinero para una urgencia familiar, Víctor cambió '
  'las condiciones: dieciséis horas sin descanso, y la remuneración entera a '
  'una deuda cuyo término nunca explicó.\n\n'
  '<break time="0.9s" />\n\n'
  'Retuvo sus documentos y amenazó a su familia. Elena seguía saliendo a la '
  'tienda, pero debía regresar.'),

 ("b8_permanencia", "Pilar",
  'Esa situación se mantuvo sin interrupción hasta septiembre de dos mil '
  'veintiséis.\n\n'
  '<break time="0.9s" />\n\n'
  'Cristina no intervino en esa relación, ni conoció las condiciones '
  'impuestas a Elena.'),

 ("b9_camilo", "Carlos",
  'El diez de mayo, Víctor contrató otra vez a Camilo, para llevar a Daniela a '
  'un inmueble anexo.\n\n'
  '<break time="0.9s" />\n\n'
  'Antes del trayecto le explicó que ella estaba siendo obligada, que quería '
  'retirarse, y que debía entregarla al encargado del otro lugar. Le ofreció '
  'un pago adicional.\n\n'
  '<break time="0.9s" />\n\n'
  'Daniela le pidió que la llevara a la terminal. Camilo se negó, y la '
  'entregó.'),

 ("b10_juliana", "Pilar",
  'El veinticinco de mayo llegó Juliana, de diecinueve años, tras otra oferta '
  'de Cristina desde la misma cuenta. El pasaje lo vendió Diana, de una '
  'agencia, al precio ordinario.\n\n'
  '<break time="0.9s" />\n\n'
  'Víctor la incorporó al sistema de deudas. Una intervención de las '
  'autoridades lo interrumpió ese mismo día, antes de que generara ingresos.'),

 ("b11_yeimi", "Carlos",
  'En agosto de dos mil veintiséis, Cristina contactó a Yeimi, que afirmó '
  'tener dieciocho años.\n\n'
  '<break time="0.9s" />\n\n'
  'Se representó seriamente como probable que fuera menor, decidió no '
  'verificarlo, y coordinó su llegada. Víctor advirtió lo mismo, tampoco pidió '
  'documento, y la incorporó al esquema.\n\n'
  '<break time="0.9s" />\n\n'
  'Yeimi tenía diecisiete años y once meses.'),

 ("b12_cierre", "Pilar",
  'Todos los desplazamientos ocurrieron dentro de Colombia.\n\n'
  '<break time="0.9s" />\n\n'
  'Nueve personas. Un solo hospedaje. Y ninguna en la misma situación.'),
]

# La votacion la trae el propio caso: son las tres tesis del equipo, literales.
VOTACION = {
    'pregunta': '¿Responden todos por trata?',
    'opciones': [
        'a) Sí: todos los que contribuyeron al funcionamiento del hospedaje.',
        'b) No: quienes llegaron voluntariamente o podían salir quedan fuera.',
        'c) Frente a Juliana solo cabría tentativa, porque nunca fue explotada.',
    ],
    'foro': ('Escoja dos de las nueve personas y explique qué las separa. '
             'Y diga qué significa, en cada una, haber podido salir a la calle.'),
}

if __name__ == "__main__":
    import re
    tot = 0
    print('%-16s %-7s %8s %8s' % ('bloque', 'voz', 'palabras', 'respiros'))
    for n, v, t in BLOQUES:
        limpio = re.sub(r'<break[^>]*/>', ' ', t)
        p = len([w for w in limpio.split() if any(c.isalnum() for c in w)])
        tot += p
        print('%-16s %-7s %8d %8d' % (n, v, p, t.count('<break')))
    print('\n%d palabras' % tot)
    for ppm in (130, 135, 142):
        s = tot / float(ppm) * 60
        print('   a %d ppm: %5.1f s de narracion  ->  pieza de %4.1f s (%d:%02d)'
              % (ppm, s, s + 82, int(s + 82) // 60, int(s + 82) % 60))
    print('\n(los 82 s son intro 9,3 + carton de entrada 5,0 + lecho 54 + '
          'carton de cierre 5,0 + outro 9,3)')
