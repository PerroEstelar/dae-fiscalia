# -*- coding: utf-8 -*-
"""Guion del C5U3 «Eslabón Financiero».

Regla de la casa: el guion NO afirma contenido jurídico que el texto del profesor
no enuncie. Aquí se describen los cinco bienes y la circunstancia de cada uno, y
se deja la pregunta abierta. Ninguna frase dice qué medida procede.

Las marcas <break time="0.9s" /> van en los puntos de corte previstos: es lo que
hizo que en el C5U2 los 18 cortes cayeran dentro de un silencio medido.
"""
BLOQUES = [
 ("b1_hipotesis", "Carlos",
  'La Fiscalía Seccional, articulada con el CTI, adelanta una investigación por '
  'enriquecimiento ilícito de particulares, concierto para delinquir y lavado de activos.\n\n'
  '<break time="0.9s" />\n\n'
  'La hipótesis investigativa señala a Fernando Alarcón: estructura operaciones '
  'financieras ilícitas y usa empresas comerciales para canalizar y ocultar activos '
  'que vienen del delito.'),

 ("b2_diligencia", "Pilar",
  'En materialización de una orden de registro y allanamiento sobre la sede operativa '
  'de Eslabón Financiero S.A.S., y sobre otros predios vinculados, la Policía Judicial '
  'aprehende e interviene cinco grupos de bienes.\n\n'
  '<break time="0.9s" />\n\n'
  'Todos salen de la misma diligencia. Ninguno llega en la misma condición.'),

 ("b3_vehiculos", "Carlos",
  'Ocho vehículos industriales de transporte, hallados en el parqueadero de la empresa '
  'y aprehendidos físicamente durante la diligencia.\n\n'
  '<break time="0.9s" />\n\n'
  'La Policía Judicial los recauda por constituir presuntos instrumentos para la '
  'movilización de recursos no justificados.'),

 ("b4_bodega", "Pilar",
  'Un inmueble comercial, con función de bodega y centro logístico, que es propiedad '
  'raíz del investigado.\n\n'
  '<break time="0.9s" />\n\n'
  'Pero en el primer piso funciona un establecimiento de comercio de venta de repuestos, '
  'registrado a nombre de un comerciante externo.\n\n'
  '<break time="0.9s" />\n\n'
  'Un tercero, con contrato de arrendamiento vigente a hoy.'),

 ("b5_servidores", "Carlos",
  'Quince servidores de criptoactivos y minería digital, hallados en la bodega.\n\n'
  '<break time="0.9s" />\n\n'
  'Maquinaria especializada cuyo valor comercial se deprecia de manera acelerada, mes a '
  'mes, y que exige costos desproporcionados de energía y de mantenimiento.'),

 ("b6_caja", "Pilar",
  'Una caja fuerte con quinientos millones de pesos en efectivo, capturada físicamente '
  'en la oficina del investigado.\n\n'
  '<break time="0.9s" />\n\n'
  'Y a su lado, los computadores con el software contable, que almacenan la evidencia '
  'de la contabilidad paralela.\n\n'
  '<break time="0.9s" />\n\n'
  'Lo mismo recaudado en el mismo acto. Y no es lo mismo.'),

 ("b7_apartamentos", "Carlos",
  'Dos inmuebles residenciales registrados a nombre del investigado, sin ocupar.\n\n'
  '<break time="0.9s" />\n\n'
  'No se requiere su aprehensión, ni desalojar a nadie. Lo que se pretende es impedir '
  'jurídicamente que sean vendidos o gravados durante el proceso penal.'),

 ("b8_cierre", "Pilar",
  'Unos vehículos recaudados como presuntos instrumentos. Un inmueble con un tercero '
  'adentro.\n\n'
  '<break time="0.9s" />\n\n'
  'Unos equipos que pierden valor cada mes que pasan guardados. Dinero en efectivo y, '
  'junto a él, la prueba.\n\n'
  '<break time="0.9s" />\n\n'
  'Y dos apartamentos que nadie tiene que tocar. Cinco bienes, una sola diligencia.'),
]

if __name__ == "__main__":
    import re
    tot = 0
    print('%-18s %-7s %8s %8s' % ('bloque', 'voz', 'palabras', 'respiros'))
    for n, v, t in BLOQUES:
        limpio = re.sub(r'<break[^>]*/>', ' ', t)
        p = len([w for w in limpio.split() if any(c.isalnum() for c in w)])
        tot += p
        print('%-18s %-7s %8d %8d' % (n, v, p, t.count('<break')))
    print('\n%d palabras · a 135 ppm serían %.1f s' % (tot, tot / 135.0 * 60))
