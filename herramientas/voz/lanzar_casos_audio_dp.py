# -*- coding: utf-8 -*-
r"""Derecho de petición revisado · audio de la situación de cada caso (ElevenLabs, voz de Pilar Durán, la de los casos de Ley 1826).

    python lanzar_casos_audio_dp.py <casos_tts.json>      pide los que faltan y masteriza (MP3 192 kb/s, 48 kHz, −16 LUFS, −1,5 dBTP)
Carpeta: E:\DAE MASTER\CURSO DERECHOS DE PETICION\Revision\AUDIOS CASOS\  (crudo\, textos_tts\, _descartes\)
"""
import json, os, shutil, subprocess, sys, time
sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
import elevenlabs as E
import casos_audio_lp as C
import lanzar_casos_audio_lp as LP

RAIZ = r'E:\DAE MASTER\CURSO DERECHOS DE PETICION\Revision\AUDIOS CASOS'
LP.RAIZ = RAIZ

if __name__ == '__main__':
    casos = json.load(open(sys.argv[1], encoding='utf-8'))
    for s in ('crudo', 'textos_tts'):
        os.makedirs(os.path.join(RAIZ, s), exist_ok=True)
    for c in casos:
        cod = c['id']
        crudo = os.path.join(RAIZ, 'crudo', cod + '.mp3')
        if not os.path.exists(crudo):
            with open(os.path.join(RAIZ, 'textos_tts', cod + '.txt'), 'w', encoding='utf-8', newline='\n') as f:
                f.write(c['tts'])
            E.decir(c['tts'], C.VOZ['Mujer'], crudo)
        sal, lufs, pico = LP.master(cod, crudo)
        d = LP.dur(sal)
        print('%-8s %5.1f s  %4d palabras  %5.1f LUFS  pico %5.1f' % (cod, d, c['palabras'], lufs, pico), flush=True)
    print('LISTO', flush=True)
