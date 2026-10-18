# -*- coding: utf-8 -*-
"""Guion del C5U4 «Los Ilustres».

Regla de la casa: el guion NO afirma contenido juridico que el texto del profesor
no enuncie. Aqui se describen los cinco activos y la circunstancia de cada uno, y
se deja la pregunta abierta. Ninguna frase dice que medida procede ni como se
resuelve la buena fe exenta de culpa.

Contenido verificado contra la fuente (`4 CASOS COMPLETOS.docx`, «Caso Practico -
Unidad Cuarta»): los cinco activos, el 70/30, los ochenta empleos, los veinte
anos del titular fallecido, los doce tractocamiones y el tres por ciento salen
todos del texto del profesor.

LAS MARCAS <break>
    Van donde la rejilla va a CORTAR -a los tercios de las PALABRAS del bloque-,
    no al final de cada frase. Esa fue la leccion del C5U3: con el respiro al
    final de la frase el corte aritmetico quedaba a 3,2 s de la pausa mas
    cercana, fuera del radio de 3,0 del iman, y partia frase.

    Donde el tercio cae sobre puntuacion natural se usa esa; donde no, se pone
    el respiro en mitad de la oracion, que es donde un locutor tomaria aire.
    La columna «tercio» de la salida de este script mide cuanto se desvia cada
    respiro del tercio exacto: todos por debajo de 4 palabras.
"""
BLOQUES = [
 ("b1_entramado", "Carlos",
  'La Dirección Especializada contra la Extinción del Derecho de Dominio, con la Policía Judicial,\n\n'
  '<break time="0.9s" />\n\n'
  'investiga el entramado económico de una estructura criminal dedicada al lavado de activos\n\n'
  '<break time="0.9s" />\n\n'
  'y al contrabando a gran escala. La herramienta es financiera: trazabilidad, cruce tributario, '
  'levantamiento de velos corporativos.'),

 ("b2_resolucion", "Pilar",
  'Con eso, el Fiscal Especializado decreta medidas sobre cinco activos:\n\n'
  '<break time="0.9s" />\n\n'
  'suspensión del poder dispositivo, embargo, secuestro y toma de posesión. '
  'Cinco activos, y en cada uno alguien distinto al frente.'),

 ("b3_comprador", "Carlos",
  'Un hotel. Lo compró hace tres años un comerciante reconocido, sin antecedentes y sin vínculo '
  'alguno con la organización.\n\n'
  '<break time="0.9s" />\n\n'
  'Revisó el certificado de tradición, que no tenía gravámenes. Hizo promesa de compraventa. '
  'Pagó el valor comercial por el banco. Inscribió el título.\n\n'
  '<break time="0.9s" />\n\n'
  'Hizo todo lo que se le puede pedir a un comprador. Y le compró a un testaferro.'),

 ("b4_socios", "Pilar",
  'Una cadena de cinco estaciones de servicio, operando. El setenta por ciento de las acciones\n\n'
  '<break time="0.9s" />\n\n'
  'es de una empresa fachada investigada. El treinta por ciento restante es de dos socios que '
  'aportaron capital de origen comprobadamente lícito.\n\n'
  '<break time="0.9s" />\n\n'
  'La orden inicial recae sobre la totalidad. Detrás de la totalidad hay ochenta empleos directos.'),

 ("b5_finca", "Carlos",
  'Una finca de ciento cincuenta hectáreas, usada durante años como centro de acopio.\n\n'
  '<break time="0.9s" />\n\n'
  'En el registro figura como titular una persona que murió hace veinte años.\n\n'
  '<break time="0.9s" />\n\n'
  'Nunca se abrió sucesión. Nadie ha respondido las citaciones.'),

 ("b6_antes", "Pilar",
  'Doce tractocamiones afectados de urgencia, con suspensión del poder dispositivo y secuestro material,\n\n'
  '<break time="0.9s" />\n\n'
  'decretados antes de que se presentara la demanda. Los afectados responden de inmediato:\n\n'
  '<break time="0.9s" />\n\n'
  'piden control judicial de legalidad y alegan que la medida no era necesaria ni proporcional.'),

 ("b7_oferta", "Carlos",
  'El afectado principal presenta por escrito un plan de colaboración efectiva. Ofrece revelar '
  'dónde están cuatro inmuebles\n\n'
  '<break time="0.9s" />\n\n'
  'que la Fiscalía no ha identificado, y delatar la red de testaferrato.\n\n'
  '<break time="0.9s" />\n\n'
  'A cambio pide conservar el tres por ciento de sus bienes, o una retribución equivalente.'),

 ("b8_cierre", "Pilar",
  'Un comprador que hizo todo bien. Dos socios con capital limpio. Un titular que lleva veinte '
  'años muerto.\n\n'
  '<break time="0.9s" />\n\n'
  'Unos afectados que reclaman antes de la demanda. Y una oferta sobre la mesa.\n\n'
  '<break time="0.9s" />\n\n'
  'La extinción recae sobre el bien. Encima del bien hay personas.'),
]

if __name__ == '__main__':
    import re
    tot = 0
    print('%-16s %-7s %9s %9s  %s' % ('bloque', 'voz', 'palabras', 'respiros', 'desvio del tercio'))
    for n, v, t in BLOQUES:
        partes = re.split(r'<break[^>]*/>', t)
        pal = [len([w for w in p.split() if any(c.isalnum() for c in w)]) for p in partes]
        total = sum(pal)
        tot += total
        k = len(partes)
        acum, desv = 0, []
        for i in range(k - 1):
            acum += pal[i]
            desv.append(round(acum - total * (i + 1) / k, 1))
        print('%-16s %-7s %9d %9d  %s   reparto %s'
              % (n, v, total, k - 1, desv, pal))
    print('\n%d palabras · estimado %.1f s a 0,444 s por palabra + pausas'
          % (tot, tot * 0.4436 + 6.6))
