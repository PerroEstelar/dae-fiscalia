# -*- coding: utf-8 -*-
r"""Tramos nuevos de narracion para la V2 de los casos del profe Carlos
Humberto, con las MISMAS voces de la V1 (cuenta propia de ElevenLabs; huella
de voz: Carlos en 1 y 5, Elisa Maria en 2, 3, 4 y 6) y el mismo modelo.

La ortografia que se le manda a la voz es FONETICA (sicosocial, Disnei,
Yimi Carter...); en pantalla va la del documento. previous_text / next_text
son las frases vecinas de la V1, para que la entonacion empalme.

    python ch_tts_v2.py
Salida: <caso>\03 VOCES\v2\CH_U1_C0N_<id>_<toma>.mp3 y tramos_v2.json
"""
import json
import os
import urllib.request

KEY = open(r'D:\DAE\_secretos\elevenlabs.txt', encoding='utf-8').read().strip()
RAIZ = r'E:\DAE MASTER\PRIORIDAD 1\PROFE CARLOS HUMBERTO'
CARP = {1: 'CASO 01 - Santiago y Valeria', 2: 'CASO 02 - Rodman', 3: 'CASO 03 - Disney',
        4: 'CASO 04 - Arley y Susana', 5: 'CASO 05 - Juan', 6: 'CASO 06 - Lenin'}
CARLOS, ELISA = 'Y4HwpMNrBWN5dFKi5Lw8', 'Pzocg9GZr24gNfKRHiyy'
VOZ = {1: CARLOS, 5: CARLOS, 2: ELISA, 3: ELISA, 4: ELISA, 6: ELISA}

T = [
 (1, 'r1', 'El equipo sicosocial no encontró violencia intrafamiliar ni maltrato hacia él.',
  'Santiago vivía con su madre y su abuela materna en el barrio Mariano Ramos.',
  'Sí señaló patrones de crianza permisivos.'),
 (2, 'r1', 'El informe del equipo sicosocial describió el entorno.',
  'Fue aprehendido momentos después por integrantes de la Policía de Infancia y Adolescencia.',
  'Rodman reside en un sector de la ciudad con altos índices de conflictividad social.'),
 (2, 'r2', 'Ambos se comprometieron a asistir a las sesiones de acompañamiento familiar y a las '
           'actividades que disponga el programa de justicia restaurativa durante el término de '
           'la suspensión a prueba, y a vincular al adolescente a una oferta educativa.',
  'Se comprometió a fortalecer el ejercicio del rol parental y a brindar el acompañamiento y la '
  'supervisión requeridos.',
  'Este es uno de los casos del taller de Principio de Oportunidad.'),
 (3, 'r1', 'La mujer es Disnei, de dieciséis años.',
  'Al automotor suben dos hombres y una mujer.', 'Apenas entran, empiezan a agredir a José.'),
 (3, 'r2', 'Se procede a la captura de cinco adultos y de la menor de edad Disnei, de dieciséis años.',
  'Son las mismas personas.', 'El equipo sicosocial que valoró a Disnei estableció lo siguiente.'),
 (3, 'r3', 'El equipo sicosocial que valoró a Disnei estableció lo siguiente: convive con su madre '
           'y dos hermanos menores en una vivienda con condiciones habitacionales adecuadas.',
  'Se procede a la captura de cinco adultos y de la menor de edad Disnei, de dieciséis años.',
  'Padre ausente.'),
 (3, 'r4', 'Estaba matriculada y asistía con regularidad al colegio, sin deserción escolar, sin '
           'consumo de sustancias sicoactivas, sin anotaciones ni procesos previos ante el Sistema '
           'de Responsabilidad Penal para Adolescentes.',
  'Padre ausente.', 'La madre manifestó disposición para acompañar el proceso judicial.'),
 (3, 'i1', 'La madre manifestó disposición para acompañar el proceso judicial y el cumplimiento de '
           'los compromisos que llegaran a imponerse. El entorno familiar fue calificado por el '
           'equipo sicosocial como un factor protector, sin antecedentes de violencia '
           'intrafamiliar, negligencia o maltrato hacia la adolescente.',
  'Sin anotaciones ni procesos previos ante el Sistema de Responsabilidad Penal para Adolescentes.',
  'Un mismo hecho, tres decisiones distintas.'),
 (4, 'r1', 'Entre mediados de abril y el seis de mayo de dos mil veinticinco se presentaron dos '
           'encuentros entre ambos en la residencia de Arley, en los que sostuvieron relaciones '
           'sexuales.',
  'La conocían sus compañeros de curso y también algunos miembros de sus respectivos entornos '
  'familiares.',
  'El caso llegó a conocimiento de las autoridades cuando la situación fue advertida en el '
  'entorno familiar de Susana.'),
 (4, 'r2', 'Para el momento de los hechos, Arley vivía con su núcleo familiar y no registraba '
           'antecedentes de conductas violentas ni de otro tipo de infracciones a la ley penal.',
  'La relación había sido conocida y, en cierta medida, tolerada en su entorno escolar y de pares.',
  ''),
 (5, 'r1', 'La investigación estableció que Juan cuenta con diagnóstico de un trastorno sicótico '
           'de inicio temprano, documentado desde los doce años por su entidad prestadora de salud.',
  'Testigos del sector manifestaron que parecía responder a estímulos que nadie más percibía.',
  'Y estableció algo más.'),
 (5, 'r2', 'Y estableció algo más: que en los meses previos a los hechos había suspendido su '
           'tratamiento siquiátrico y farmacológico de manera irregular.',
  'Documentado desde los doce años por su entidad prestadora de salud.',
  'La razón: dificultades de acceso al servicio.'),
 (6, 'r1', 'En el Colegio Yimi Cárter, Lenin, de catorce años, tocó los senos de Nicol, de once.',
  'Bogotá, veintitrés de mayo de dos mil veinticinco.',
  'Ella dio muestras de dolor y de afectación frente a la acción.'),
 (6, 'r2', 'El grupo de siquiatría y sicología forenses de Bogotá rindió informe pericial sobre '
           'capacidad de comprensión y autodeterminación.',
  'El Instituto Nacional de Medicina Legal y Ciencias Forenses valoró a Lenin.',
  'El informe indica que Lenin adolece de limitada capacidad de autodeterminarse.'),
]


def tts(voz, texto, prev, nxt, seed, dst):
    body = {'text': texto, 'model_id': 'eleven_multilingual_v2', 'seed': seed,
            'voice_settings': {'stability': 0.5, 'similarity_boost': 0.8, 'style': 0.0,
                               'use_speaker_boost': True}}
    if prev:
        body['previous_text'] = prev
    if nxt:
        body['next_text'] = nxt
    req = urllib.request.Request(
        'https://api.elevenlabs.io/v1/text-to-speech/%s?output_format=mp3_44100_192' % voz,
        data=json.dumps(body).encode(), headers={'xi-api-key': KEY,
                                                 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=120) as r:
        open(dst, 'wb').write(r.read())


out = []
for n, i, texto, prev, nxt in T:
    d = os.path.join(RAIZ, CARP[n], '03 VOCES', 'v2')
    os.makedirs(d, exist_ok=True)
    for toma, seed in (('a', 11), ('b', 23)):
        dst = os.path.join(d, 'CH_U1_C%02d_%s_%s.mp3' % (n, i, toma))
        if not os.path.exists(dst):
            try:
                tts(VOZ[n], texto, prev, nxt, seed, dst)
            except Exception as e:                             # noqa: BLE001
                print(n, i, toma, 'FALLA', str(e)[:150], flush=True)
                continue
        out.append({'caso': n, 'id': i, 'toma': toma, 'archivo': dst, 'texto_voz': texto})
        print(n, i, toma, os.path.getsize(dst), flush=True)
json.dump(out, open(r'D:\DAE\_tmp\ch\tramos_v2.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('LISTO')
