# -*- coding: utf-8 -*-
r"""Arma los prompts de las placas de los casos SRPA (es `prompts_da`) y deja
el storyboard escrito.

Referencias, en este orden:
    1. la HOJA de quien manda en el plano (REF2: identidad) -FIRST-;
    2. la hoja de la segunda persona con cara, si la hay (REF3) -SECOND-;
    3. la placa madre aprobada del MISMO lugar o persona (REF) o, si todavía
       no hay madre, el ANCLA de estilo de la serie -LAST-.

    python prompts_sr.py NICO [salida.json]
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
import base_sr as S                              # noqa: E402
from prompts_da import (REF_LUGAR, REF_MISMO, REF_ESTILO, REF_PIEL,  # noqa: E402
                        REF_GENTE, UNA_IMAGEN)

REF_ID1 = ('The FIRST reference image is the character sheet of %s of this '
           'film: he or she must be the SAME person, with exactly the same face, '
           'hair, build and clothes; use that image ONLY for %s, never for the '
           'place, the framing or the format.')
REF_ID2 = ('The SECOND reference image is the character sheet of %s of this '
           'film: the SAME person, exactly the same face, hair, build and '
           'clothes; use that image ONLY for %s.')

# anclas de estilo de la serie en la cuenta nueva (placa_id_ei.json)
ANCLA = {'rural': 'lJXfZDlgv9', 'pueblo': 'LwevY09swO', 'oficina': 'DoSNkxnpcl',
         'noche_ext': 'lJXfcMmgv9', 'noche_int': 'N2E18mF6D9',
         'pasillo': '8aPAlwKIrU', 'recepcion': '0eLy5bSTfW'}


def E(clave):
    return __import__('escenas_sr_%s' % clave.lower())


def nombre(clave, n):
    return 'SR_%s_r%02d_%s' % (clave, n, E(clave).NOMBRE[n])


def tokens(mod):
    t = dict(S.TOKENS)
    t.update(getattr(mod, 'EXTRA_TOKENS', {}))
    return t


def placa_id():
    f = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'placa_id_sr.json')
    return json.load(open(f, encoding='utf-8')) if os.path.exists(f) else {}


def video(clave, solo=None):
    mod = E(clave)
    falla, tot, racha = mod.comprobar()
    assert not falla, (clave, falla)
    TK = tokens(mod)
    PID = placa_id()
    out = {}
    for n, (cuad, reg, gente, acento, fuego, lugar, txt) in sorted(mod.R.items()):
        if solo and n not in solo:
            continue
        tk = dict(TK)
        hojas = [x for x in (getattr(mod, 'REF2', {}).get(n), getattr(mod, 'REF3', {}).get(n)) if x]
        for h, _q in hojas:
            quien = h.replace('SR_HOJA_', '')
            if quien in S.CORTO_ID and PID.get(h):
                tk[quien] = S.CORTO_ID[quien]
        esc = txt % tk if '%(' in txt else txt
        if n in getattr(mod, 'CENITALES', set()):
            esc = esc.strip() + '\n\n' + UNA_IMAGEN
        manos = n in getattr(mod, 'SOLO_MANOS', set())
        p = S.arma(esc, registro=reg, personas=gente, acento=acento,
                   lugar=lugar, con_rostro=not manos, fuego=fuego)
        refs, faltan = [], []
        r2 = getattr(mod, 'REF2', {}).get(n)
        if r2:
            if PID.get(r2[0]):
                refs.append(PID[r2[0]])
                p += '\n\n' + REF_ID1 % (r2[1], r2[1])
            else:
                faltan.append(r2[0])
        r3 = getattr(mod, 'REF3', {}).get(n)
        if r3:
            if PID.get(r3[0]):
                refs.append(PID[r3[0]])
                p += '\n\n' + (REF_ID2 % (r3[1], r3[1])).replace(
                    'SECOND', 'SECOND' if r2 else 'FIRST')
            else:
                faltan.append(r3[0])
        ref = getattr(mod, 'REF', {}).get(n)
        madre = None
        if ref:
            m, modo, nota = ref
            madre = m if isinstance(m, str) else nombre(clave, m)
            mid = PID.get(madre)
            if mid:
                refs.append(mid)
                p += '\n\n' + ((REF_MISMO % nota) if modo == 'mismo'
                               else (REF_GENTE % ((nota + ' ') if nota else ''))
                               if modo == 'gente'
                               else (REF_LUGAR % ((nota + ' ') if nota else '')))
                if gente:
                    p += REF_PIEL
            else:
                faltan.append(madre)
        if not ref:
            a = getattr(mod, 'ANCLA_DE', {}).get(n, 'pueblo')
            refs.append(ANCLA[a])
            p += '\n\n' + REF_ESTILO
        out[nombre(clave, n)] = {'ranura': n, 'cuadros': cuad, 'luz': reg,
                                 'gente': list(gente), 'lugar': lugar,
                                 'refs': refs, 'madre': madre, 'faltan': faltan,
                                 'prompt': p}
    return out


if __name__ == '__main__':
    clave = sys.argv[1].upper()
    solo = None
    if len(sys.argv) > 3:
        solo = {int(x) for x in sys.argv[3].split(',')}
    o = video(clave, solo)
    sal = sys.argv[2] if len(sys.argv) > 2 else 'prompts_sr_%s.json' % clave
    json.dump(o, open(sal, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for k, v in o.items():
        print('%-34s %4d %-9s madre %-4s refs %d faltan %s  %5d car'
              % (k, v['cuadros'], v['luz'], v['madre'], len(v['refs']), v['faltan'],
                 len(v['prompt'])))
