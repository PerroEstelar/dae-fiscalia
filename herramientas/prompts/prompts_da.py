# -*- coding: utf-8 -*-
r"""Arma los prompts de las placas de Delitos ambientales (es `prompts_ei` en
corto) y deja el storyboard escrito.

Por ranura: `base_da.arma` con el reparto y los tokens de la pieza, y las
referencias en el orden del pedido:
    - la placa aprobada del MISMO lugar o persona (REF del módulo de escenas)
      -'lugar': el sitio, la luz y el dibujo; 'mismo': el mismo plano, cambia
      solo lo dicho-, que va al FINAL;
    - si no hay placa madre todavía, el ANCLA de estilo de la serie (una placa
      aprobada de otro curso: solo el dibujo).

    python prompts_da.py V01 [salida.json]
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
import base_da as S                              # noqa: E402

REF_LUGAR = ('The LAST reference image is a finished plate of this same place '
             'from this same film, already approved: use it for the place, the '
             'objects, the people\'s identity and clothes, the light and the '
             'drawing, NOT for the framing, which is described above. %sMatch '
             'its DRAWING and PALETTE exactly: a flat graphic illustration built '
             'from broad simplified tonal planes, no rendered texture anywhere, '
             'no photographic detail.')
REF_MISMO = ('The LAST reference image is the SAME SHOT from this same film, '
             'already approved: %s Match its DRAWING and PALETTE exactly.')
REF_ESTILO = ('The LAST reference image is a finished plate from this same '
              'series, of ANOTHER place and story: use it ONLY for the drawing, '
              'the treatment and the tonal values, never for the place, the '
              'people, the palette of the landscape or the framing. Match its '
              'DRAWING exactly: a flat graphic illustration built from broad '
              'simplified tonal planes, no rendered texture anywhere, no '
              'photographic detail. This picture must look like it was drawn by '
              'the same hand, not like a photograph.')
REF_PIEL = (' Match its SKIN exactly too: the same flat warm GREY, never warmer, '
            'pinker, more peach or more saturated.')
REF_GENTE = ('The LAST reference image is a finished plate from this same '
             'film showing the SAME people: use it ONLY for their faces, hair, '
             'bodies and clothes and for the drawing, NEVER for the place, the '
             'light or the framing, which are described above. %sMatch its '
             'DRAWING exactly: a flat graphic illustration built from broad '
             'simplified tonal planes, no rendered texture anywhere.')
REF_IDENTIDAD = ('The FIRST reference image shows THE PROSECUTOR of this film: '
                 'she must be the SAME woman, with exactly the same face, '
                 'straight dark jaw-length hair, thin-framed glasses and plain '
                 'dark grey blazer; use that image ONLY for her, not for the '
                 'place or the framing.')
REF_OTRO = ('The FIRST reference image shows %s of this film: he or she must '
            'be the SAME person, with exactly the same face, hair, build and '
            'clothes; use that image ONLY for %s, not for the place or the '
            'framing.')
UNA_IMAGEN = ('This is ONE single continuous picture that fills the whole frame: '
              'NOT a split screen, NOT a comic page, NO panels, NO inset '
              'pictures, NO dividing borders.')

# las anclas de la serie (placas aprobadas de Ley 1826 y Enfoque diferencial,
# subidas a la cuenta nueva; ids en placa_id_ei.json)
ANCLA = {'rural': 'lJXfZDlgv9', 'pueblo': 'LwevY09swO', 'oficina': 'DoSNkxnpcl',
         'noche_ext': 'lJXfcMmgv9', 'noche_int': 'N2E18mF6D9'}


def E(clave):
    return __import__('escenas_da_%s' % clave.lower())


def nombre(clave, n):
    return 'DA_%s_r%02d_%s' % (clave, n, E(clave).NOMBRE[n])


def tokens(mod):
    t = dict(S.TOKENS)
    t.update(getattr(mod, 'EXTRA_TOKENS', {}))
    return t


def placa_id():
    f = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'placa_id_da.json')
    return json.load(open(f, encoding='utf-8')) if os.path.exists(f) else {}


def video(clave):
    mod = E(clave)
    falla, tot, racha = mod.comprobar()
    assert not falla, (clave, falla)
    TK = tokens(mod)
    PID = placa_id()
    out = {}
    for n, (cuad, reg, gente, acento, fuego, lugar, txt) in sorted(mod.R.items()):
        esc = txt % TK if '%(' in txt else txt
        if n in getattr(mod, 'CENITALES', set()):
            esc = esc.strip() + '\n\n' + UNA_IMAGEN
        manos = n in getattr(mod, 'SOLO_MANOS', set())
        p = S.arma(esc, registro=reg, personas=gente, acento=acento,
                   lugar=lugar, con_rostro=not manos, fuego=fuego)
        refs = []
        if n in getattr(mod, 'PRESTADA', {}):
            continue          # 7 nov: la placa sale de otro video (da_pieza.elegir)
        ref = getattr(mod, 'REF', {}).get(n)
        if ref:
            madre, modo, nota = ref
            # 7 nov: la madre puede ser de OTRO video del curso: 'DA_V01_r30_la_fiscal'
            mid = PID.get(madre if isinstance(madre, str) else nombre(clave, madre))
            if mid:
                refs.append(mid)
                p += '\n\n' + ((REF_MISMO % nota) if modo == 'mismo'
                               else (REF_GENTE % ((nota + ' ') if nota else ''))
                               if modo == 'gente'
                               else (REF_LUGAR % ((nota + ' ') if nota else '')))
                if gente:
                    p += REF_PIEL
            else:
                ref = None
        if not ref:
            a = getattr(mod, 'ANCLA_DE', {}).get(n, 'rural')
            refs.append(ANCLA[a])
            p += '\n\n' + REF_ESTILO
        # 7 nov: una segunda madre, de IDENTIDAD (la fiscal del curso), va
        # PRIMERO; la de lugar o estilo sigue siendo la última
        r2 = getattr(mod, 'REF2', {}).get(n)
        # 7 nov: REF2 puede ser (madre, quien) cuando la identidad no es la
        # fiscal: 'quien' es como se nombra a esa persona en el texto
        quien = None
        if isinstance(r2, tuple):
            r2, quien = r2
        if r2 and PID.get(r2):
            refs.insert(0, PID[r2])
            p += '\n\n' + (REF_IDENTIDAD if not quien else REF_OTRO % (quien, quien))
        out[nombre(clave, n)] = {'ranura': n, 'cuadros': cuad, 'luz': reg,
                                 'gente': list(gente), 'lugar': lugar,
                                 'acento': acento, 'refs': refs,
                                 'madre': ref[0] if ref else None,
                                 'prompt': p}
    return out


if __name__ == '__main__':
    clave = sys.argv[1].upper()
    o = video(clave)
    sal = sys.argv[2] if len(sys.argv) > 2 else 'prompts_da_%s.json' % clave
    json.dump(o, open(sal, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for k, v in o.items():
        print('%-34s %4d %-9s madre %-4s refs %s  %5d car'
              % (k, v['cuadros'], v['luz'], v['madre'], v['refs'], len(v['prompt'])))
