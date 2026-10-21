# -*- coding: utf-8 -*-
"""Piel y acentos del Caso 4, sobre el set ya graduado.

LA PIEL SE CORRIGE AQUI PORQUE EL PROMPT NO LA FIJA
    Medido en las 36: pedir "saturacion alrededor de 0,20" entrega 0,10-0,15,
    por debajo de la banda aprobada (0,16-0,28). Se intento con "no higher
    than" y con "around ... between", y el numero casi no se movio. El tono
    SI responde al prompt; el nivel no. Lo pone piel.py, con ganancia.

LA PIEL SOLO DONDE LA HAY, Y SIN MANCHAR UNA MANO CLARA
    Leccion del Caso 3: `piel.py` manchó una mano casi gris al multiplicar su
    saturacion por 1,57. Aqui se mide primero: si la placa ya esta dentro de
    banda, se salta.

EL ACENTO VA DESPUES DEL GRADE Y DESPUES DE LA PIEL
    El grade por canal dejo la neutralizacion en 0,91 de media, asi que el
    acento llega casi intacto. Solo seis placas lo tienen.
"""
import os
import shutil
import sys

sys.path.insert(0, '.')
import piel
import acentos

# LAS DIEZ PLACAS QUE NO TIENEN UNA SOLA MANO, POR DISENIO.
#
# El detector de piel de piel.py busca pixeles calidos de saturacion media, y
# en este set eso TAMBIEN describe el papel y el carton de las carpetas. En la
# primera pasada "corrigio" cuatro placas sin una mano dentro -r18, r26, r33 y
# r39-, girando el tono de todo lo calido del cuadro. Es la misma trampa del
# Caso 3, donde manchó una mano casi gris, con el sujeto cambiado.
#
# La comprobacion no puede ser "los numeros estan fuera de banda": un papel
# calido tambien lo esta. Tiene que ser "aqui hay piel", y eso lo sabe el
# repertorio, no la imagen. La lista sale de escenas.py, leida a mano porque
# un regex se traga las negaciones -"no hand beyond the pen"-.
SIN_PIEL = {'r09_fachada_vecina', 'r14_sin_orden', 'r18_dos_casillas',
            'r20_estrado_vacio', 'r21_microfono_apartado',
            'r26_una_sola_linea', 'r29_silla_de_la_defensa',
            'r31_tres_marcas', 'r33_direccion_corregida',
            'r39_seis_carpetas_separadas'}
ACENTO = {
    'r02_nora_umbral': 'amarillo',
    'r05_ivan_telefono': 'amarillo',
    'r13_recepcionista_llega': 'azul',
    'r19_nora_escucha': 'amarillo',
    'r22_ivan_sentado': 'amarillo',
    'r25_lina_de_pie': 'amarillo',
}
BANDA_SAT = (0.16, 0.28)
BANDA_TONO = (12.0, 37.0)


def main(ent, sal):
    os.makedirs(sal, exist_ok=True)
    print('%-28s %-22s %-22s %s' % ('placa', 'piel antes', 'piel despues', 'que se hizo'))
    tocadas, saltadas, sin_piel = [], [], []
    for f in sorted(os.listdir(ent)):
        if not f.endswith('.png'):
            continue
        o, d = os.path.join(ent, f), os.path.join(sal, f)
        from PIL import Image
        if f[:-4] in SIN_PIEL:
            shutil.copyfile(o, d); sin_piel.append(f[:-4])
            print('%-28s %-22s %-22s %s'
                  % (f[:-4][:28], '-', '-', 'sin manos, por disenio'))
            continue
        antes = piel.medir(Image.open(o).convert('RGB'))
        if antes is None:
            shutil.copyfile(o, d); sin_piel.append(f[:-4])
            print('%-28s %-22s %-22s %s' % (f[:-4][:28], '-', '-', 'sin piel'))
            continue
        en_banda = (BANDA_SAT[0] <= antes['satur'] <= BANDA_SAT[1]
                    and BANDA_TONO[0] <= antes['tono'] <= BANDA_TONO[1])
        if en_banda:
            shutil.copyfile(o, d); saltadas.append(f[:-4])
            print('%-28s %-22s %-22s %s'
                  % (f[:-4][:28],
                     'T%.1f S%.2f V%.2f' % (antes['tono'], antes['satur'], antes['valor']),
                     '(igual)', 'ya en banda, se salta'))
            continue
        r = piel.fijar(o, d)
        de = r['despues']
        tocadas.append(f[:-4])
        print('%-28s %-22s %-22s giro %+.1f  satur x%.2f  valor x%.2f'
              % (f[:-4][:28],
                 'T%.1f S%.2f V%.2f' % (antes['tono'], antes['satur'], antes['valor']),
                 'T%.1f S%.2f V%.2f' % (de['tono'], de['satur'], de['valor']) if de else '-',
                 r['giro'], r['escala'], r['ganancia']))
    print('\npiel corregida en %d · ya en banda %d · sin piel %d'
          % (len(tocadas), len(saltadas), len(sin_piel)))

    print('\nACENTOS')
    for n, color in sorted(ACENTO.items()):
        p = os.path.join(sal, n + '.png')
        r = acentos.fijar(p, p, color)
        if 'aviso' in r:
            print('%-28s %-9s %s' % (n[:28], color, r['aviso']))
            continue
        a, de = r['antes'], r['despues']
        print('%-28s %-9s #%02X%02X%02X -> #%02X%02X%02X  satur %.2f -> %.2f  (%.2f%% del cuadro)'
              % (n[:28], color, a['rgb'][0], a['rgb'][1], a['rgb'][2],
                 de['rgb'][0], de['rgb'][1], de['rgb'][2],
                 a['satur'], de['satur'], a['porcentaje']))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
