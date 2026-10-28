# -*- coding: utf-8 -*-
r"""Muestras cortas de cada voz colombiana de la cuenta propia de ElevenLabs,
para reconocer por huella de voz cual narro la V1 de los casos del profe
Carlos Humberto. Llave en D:\DAE\_secretos\elevenlabs.txt (nunca se imprime).

    python ch_muestras_voz.py
Salida: D:\DAE\_tmp\ch\muestras\<voice_id>.mp3
"""
import json
import os
import urllib.request

KEY = open(r'D:\DAE\_secretos\elevenlabs.txt', encoding='utf-8').read().strip()
OUT = r'D:\DAE\_tmp\ch\muestras'
VOCES = {
    'Y4HwpMNrBWN5dFKi5Lw8': 'Carlos', 'UxEeTOXgTgyv54iyYaa5': 'Alexander',
    'Ol2UUwISo9ncUTR92kGn': 'Alejandro', 'qqab7XtemzUr6wYwGSrQ': 'Jerome',
    '4uvQjLPvqApx1dVzpNfM': 'Johan', 'SsO7anq9lnFq4QW8bfch': 'Alejo',
    'OwXM764IiSDeqYNU1rbL': 'Ivan', '57D8YIbQSuE3REDPO6Vm': 'Horacio',
    'hsPqKgfWI5YayyFu0nuN': 'David', 'Ux2YbCNfurnKHnzlBHGX': 'Leo',
    'Pzocg9GZr24gNfKRHiyy': 'Elisa Maria', 'x6LHvMgpXmty838MUqHh': 'Pilar Duran',
    'oWSxI36XAKnfMWmzmQok': 'Milena', 'WZlYpi1yf6zJhNWXih74': 'Hope clear',
    'cVd39cx0VtXNC13y5Y7z': 'Hope vibrant', 'zGjIP4SZlMnY9m93k97r': 'Hope relatable',
}
TEXTO = ('Frente a las condiciones sociofamiliares del adolescente, el informe del '
         'equipo sicosocial señaló que reside en un sector de la ciudad con altos '
         'índices de conflictividad social. No obstante lo anterior, se identificó '
         'una familia garante de derechos y corresponsable.')

os.makedirs(OUT, exist_ok=True)
for vid, nom in VOCES.items():
    p = os.path.join(OUT, vid + '.mp3')
    if os.path.exists(p):
        continue
    body = json.dumps({'text': TEXTO, 'model_id': 'eleven_multilingual_v2',
                       'voice_settings': {'stability': 0.5, 'similarity_boost': 0.8,
                                          'style': 0.0, 'use_speaker_boost': True}}).encode()
    req = urllib.request.Request(
        'https://api.elevenlabs.io/v1/text-to-speech/%s?output_format=mp3_44100_128' % vid,
        data=body, headers={'xi-api-key': KEY, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            open(p, 'wb').write(r.read())
        print(nom, os.path.getsize(p))
    except Exception as e:                                     # noqa: BLE001
        print(nom, 'FALLA', str(e)[:120])
print('LISTO')
