# -*- coding: utf-8 -*-
r"""Caso 2, tramo r2: las dos tomas del 28 oct tartamudean en «comprometieron
a asistir» (Scribe: «a, a asistir» / «a si-- a asistir»). Tomas nuevas con
otras semillas, y una variante con la sinalefa escrita («comprometieron
asistir», que es como se dice «a asistir» de corrido). Llave sin imprimir.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import io, contextlib     # noqa: E401,E402
with contextlib.redirect_stdout(io.StringIO()):
    import ch_tts_v2 as V     # noqa: E402  (su bucle salta lo que ya existe)
    import ch_transcribir as T     # noqa: E402

D = os.path.join(V.RAIZ, V.CARP[2], '03 VOCES', 'v2')
BASE = ('Ambos se comprometieron %s a las sesiones de acompañamiento familiar y a las '
        'actividades que disponga el programa de justicia restaurativa durante el término de '
        'la suspensión a prueba, y a vincular al adolescente a una oferta educativa.')
PREV = ('Se comprometió a fortalecer el ejercicio del rol parental y a brindar el acompañamiento y '
        'la supervisión requeridos.')
NEXT = 'Este es uno de los casos del taller de Principio de Oportunidad.'
TOMAS = [('c', 'a asistir', 31), ('d', 'a asistir', 47), ('e', 'asistir', 11), ('f', 'asistir', 59)]
out = {}
for t, frag, seed in TOMAS:
    dst = os.path.join(D, 'CH_U1_C02_r2_%s.mp3' % t)
    if not os.path.exists(dst):
        V.tts(V.VOZ[2], BASE % frag, PREV, NEXT, seed, dst)
    j = T.stt(dst)
    out[t] = ' '.join(w['text'] for w in j['words'] if w.get('type') == 'word')
    json.dump(j, open(r'D:\DAE\_tmp\ch\stt\tramos\C02_r2_%s.json' % t, 'w', encoding='utf-8'),
              ensure_ascii=False)
    print(t, frag, '|', out[t][:70], flush=True)
