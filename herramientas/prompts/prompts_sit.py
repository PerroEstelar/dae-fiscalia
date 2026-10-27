# -*- coding: utf-8 -*-
r"""Arma todos los prompts de las situaciones y los deja donde se usan.

Por cada situacion en VIDEO:
    - una placa por ranura (`escenas_sit_<l>.R`), con las comprobaciones de
      la serie: los cuadros suman lo que dice la rejilla, y no hay mas de tres
      ranuras seguidas sin gente;
    - los insertos de detalle (`DET`) para la pista V3 DETALLE, cada uno con
      su placa -que se pide con la placa madre como referencia- y su gesto
      para Kling, con la clausula de quietud de la serie;
    - el b-roll de reserva (`BROLL`) y las notas de movimiento (`MOV`).

Por cada situacion en IMAGEN: las dos angulaciones de `imagenes_sit`.

Sale un json por situacion en D:\DAE\_tmp\sit y, en la carpeta de guion de
cada situacion, un .md legible con el guion verbatim, la rejilla y cada
prompt: es el storyboard escrito, para mirarlo antes de gastar un credito.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
import base_sit as S                            # noqa: E402
import imagenes_sit as IMG                      # noqa: E402
from guion_sit import SITUACIONES, bloques, TEXTOS   # noqa: E402

TMP = r'D:\DAE\_tmp\sit'

# La clausula de quietud de los detalles es la del caso integrador (§8 y §12
# de la biblia): el unico movimiento es el que se nombra, y nada nuevo entra.
QUIETO = ('The camera does not move at all and the framing does not change. '
          'Only the movement described happens; nothing else in the frame '
          'moves. No new hand, face or figure enters the frame. Hands keep '
          'their natural arrangement: the fingers never splay and never '
          'change in number. Skin stays a flat desaturated warm grey, never '
          'pink. The flat graphic illustration style, the light and the '
          'near-monochrome palette stay exactly unchanged.')

REFERENCIA = ('This is a CLOSER SHOT OF THE SAME SCENE as the reference '
              'image: the same person, the same clothes, the same light from '
              'the same side, the same palette and the same flat graphic '
              'style. It must be indistinguishable from it in treatment.')


def video(letra):
    mod = __import__('escenas_sit_%s' % letra.lower())
    falla, tot, racha = mod.comprobar()
    assert not falla, (letra, falla)
    out = {'situacion': letra, 'carpeta': SITUACIONES[letra][1],
           'placas': {}, 'detalles': {}, 'broll': {}, 'mov': mod.MOV}
    for n, (cuad, reg, gente, acento, sil, ext, txt) in sorted(mod.R.items()):
        cuerpo = txt % S.TOKENS if '%(' in txt else txt
        p = S.arma(cuerpo, registro=reg, personas=gente, con_acento=acento,
                   exterior=ext, silueta=sil)
        k = 'SIT_%s_r%02d_%s' % (letra, n, mod.NOMBRE[n])
        out['placas'][k] = {'ranura': n, 'cuadros': cuad, 'luz': reg,
                            'gente': list(gente), 'silueta': bool(sil),
                            'exterior': bool(ext),
                            'carton_sugerido': n in mod.CARTONES,
                            'prompt': p}
    for (n, nom), d in sorted(mod.DET.items()):
        madre = 'SIT_%s_r%02d_%s' % (letra, n, mod.NOMBRE[n])
        gente = out['placas'][madre]['gente']
        p = S.arma(d['escena'] + '\n\n' + REFERENCIA, registro=d['registro'],
                   personas=tuple(gente), exterior=False)
        out['detalles']['SIT_%s_r%02d_%s_det' % (letra, n, nom)] = {
            'ranura': n, 'madre': madre, 'cuadros': d['cuadros'],
            'entra': d['entra'], 'prompt_placa': p,
            'prompt_video': d['gesto'] + ' ' + QUIETO}
    for nom, (reg, esc) in sorted(mod.BROLL.items()):
        out['broll']['SIT_%s_broll_%s' % (letra, nom)] = {
            'luz': reg, 'prompt': S.arma(esc, registro=reg, exterior=True)}
    return out, tot, racha


def imagen(letra):
    out = {'situacion': letra, 'carpeta': SITUACIONES[letra][1],
           'texto': TEXTOS[letra], 'variantes': {}}
    for v, (reg, gente, ext, lado, txt) in sorted(IMG.IM[letra].items()):
        cuerpo = txt % S.TOKENS if '%(' in txt else txt
        cuerpo = cuerpo.strip() + '\n\n' + IMG.LADO[lado]
        p = S.arma(cuerpo, registro=reg, personas=gente, exterior=ext)
        out['variantes']['SIT_%s_%s_%s' % (letra, IMG.NOMBRE[letra], v)] = {
            'luz': reg, 'gente': list(gente), 'lado_libre': lado,
            'prompt': p}
    return out


def md_video(o, rejilla=None):
    L = o['situacion']
    s = ['# Situación %s · %s' % (L, o['carpeta'].split(' - ', 1)[1].capitalize()),
         '', 'Storyboard escrito: guion verbatim, ranuras y prompts. '
         'Generado por `prompts_sit.py`.', '', '## Guion (verbatim)', '']
    for i, v, t, tts, p in bloques(L):
        s += ['**%s** · %s · pausa %.1f s' % (i, v, p), '', t, '']
    s += ['## Ranuras', '', '| ranura | cuadros | luz | gente | carton |',
          '|---|---|---|---|---|']
    for k, v in o['placas'].items():
        s.append('| %s | %d | %s | %s | %s |'
                 % (k, v['cuadros'], v['luz'],
                    ', '.join(v['gente']) or ('siluetas' if v['silueta'] else '—'),
                    'sí' if v['carton_sugerido'] else ''))
    s += ['', '## Prompts de placa', '']
    for k, v in o['placas'].items():
        s += ['### %s' % k, '', '```', v['prompt'], '```', '']
    s += ['## Planos de detalle (V3 DETALLE)', '']
    for k, v in o['detalles'].items():
        s += ['### %s' % k, '', 'madre `%s` · %d cuadros · entra en %d'
              % (v['madre'], v['cuadros'], v['entra']), '',
              '**placa**', '', '```', v['prompt_placa'], '```', '',
              '**video (Kling, keyframe de inicio = placa)**', '', '```',
              v['prompt_video'], '```', '']
    s += ['## B-roll de reserva', '']
    for k, v in o['broll'].items():
        s += ['### %s' % k, '', '```', v['prompt'], '```', '']
    s += ['## Movimiento (candidatos)', '']
    for n, t in sorted(o['mov'].items()):
        s.append('- r%02d: %s' % (n, t))
    return '\n'.join(s) + '\n'


def md_imagen(o):
    L = o['situacion']
    s = ['# Situación %s · %s' % (L, o['carpeta'].split(' - ', 1)[1].capitalize()),
         '', '## Texto de la lámina (verbatim)', '', o['texto'], '',
         '## Ilustración: dos angulaciones', '']
    for k, v in o['variantes'].items():
        s += ['### %s · luz %s · lado libre %s' % (k, v['luz'], v['lado_libre']),
              '', '```', v['prompt'], '```', '']
    return '\n'.join(s) + '\n'


if __name__ == '__main__':
    sys.path.insert(0, r'D:\DAE\_repo\herramientas\voz\textos')
    import rutas_sit as R
    os.makedirs(TMP, exist_ok=True)
    for L, (tipo, carpeta, _) in sorted(SITUACIONES.items()):
        if tipo == 'video':
            o, tot, racha = video(L)
            dest = R.sub(L, '06 GUION Y STORYBOARD')
            md = md_video(o)
            print('%s  %2d placas  %d detalles  %d broll  %5d cuadros  racha %d'
                  % (L, len(o['placas']), len(o['detalles']), len(o['broll']),
                     tot, racha))
        else:
            o = imagen(L)
            dest = R.sub(L, '06 GUION Y PROMPTS')
            md = md_imagen(o)
            print('%s  %d variantes' % (L, len(o['variantes'])))
        json.dump(o, open(os.path.join(TMP, 'prompts_sit_%s.json' % L), 'w',
                          encoding='utf-8'), ensure_ascii=False, indent=1)
        with open(os.path.join(dest, 'SIT_%s_storyboard.md' % L), 'w',
                  encoding='utf-8') as f:
            f.write(md)
    print('LISTO')
