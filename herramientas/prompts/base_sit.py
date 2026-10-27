# -*- coding: utf-8 -*-
r"""Clausulas y reparto de las SITUACIONES del curso de Desaparicion Forzada.

EL SISTEMA ES EL DEL CASO INTEGRADOR, SIN UNA COMA DE MAS
    Mismo curso, mismo municipio -San José de las Peñas, la vereda La
    Esperanza, El Mirador, la Finca El Vergel-, mismo Bloque Central
    Renacer. Mezclar sistemas dentro de un curso es criterio de rechazo, asi
    que todo lo que no es reparto se importa de `base_df_v1` tal cual: estilo,
    piel, rostro, los tres registros, la superficie lisa, la clausula de
    silueta, la de exterior, el acento como prenda mate.

LO QUE CAMBIA ES EL REPARTO
    Las situaciones A, F, G, H, I, J y K son la familia MORALES: Carlos
    Alberto -el desaparecido-, su madre Rosa Elena y su hermana Mariana. Rosa
    Elena y Mariana son LAS MISMAS del caso integrador: mismo token, misma
    referencia de imagen, para que el curso tenga una sola familia y no dos
    parecidas.

    Las B, C, D y E son casos de un solo protagonista cada uno: Julián David,
    Fernando, Don Manuel Antonio y Gustavo Adolfo.

EL COLOR ES DE QUIEN ES BUSCADO
    En el caso integrador el acento mostaza lo llevaba la familia de la
    victima. Aqui se generaliza la misma idea: lo lleva QUIEN DESAPARECE en
    cada situacion -una gorra, un trapo de taller, un chaleco, un sombrero,
    un panuelo- y, en la familia Morales, tambien las dos mujeres que buscan.
    Nadie mas. La institucion va en gris; los armados, en silueta.

    El sombrero de Don Manuel es el caso mas claro de por que: es lo unico
    que aparece de el, a trescientos metros rio abajo. Si es lo unico con
    color en el cuadro, el espectador lo encuentra antes que los vecinos.

QUIEN NO LLEVA CARA, Y POR QUE
    Cada situacion en video tiene un servidor que decide mal en la
    ventanilla -el comandante de guardia (A), el funcionario de atencion
    (B), el funcionario de turno (D), el fiscal de turno (E)- y en las
    imagenes el servidor que escribe la minuta (I). La regla del paso 11
    sigue: una decision equivocada no cae sobre un rostro. Se cuentan por la
    ventanilla, las manos, la espalda y el papel.

    El analista de denuncias de la C no decide mal: DUDA, y la duda es la
    pregunta del ejercicio. Aun asi va sin rostro -manos y dos carpetas-
    porque la situacion no le da nombre ni rasgos, y porque la cara de quien
    duda empuja al espectador hacia una de las dos respuestas.

    Los armados, siempre silueta y entorno, sin arma a la vista. Los
    disparos de la E y el abordaje de la A y la C NO se dibujan: estan en la
    voz, verbatim, y la imagen muestra el antes, el despues y el lugar.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, r'D:\DAE\_repo\herramientas\prompts')
import base_df_v1 as B                          # noqa: E402
from base_df_v1 import (PIEL, ROSTRO, PLANOS, REGISTRO, CAMARA, LIMPIA,  # noqa
                        SIN_ROLES, SILUETA, ESTILO, FIGURA, LUGAR, EXTERIOR,
                        ACENTO, NEG)

# ------------------------------------------------------------------ reparto
CUERPO = dict(B.CUERPO)
VIDA = dict(B.VIDA)

CUERPO.update({
 'carlosalberto': ('CARLOS ALBERTO, an Afro-Colombian man of about '
                   'thirty-four, broad-shouldered and of medium height, '
                   'short-cropped dark hair and a short trimmed beard, in a '
                   'plain mid-grey work shirt with the sleeves rolled to the '
                   'elbow over plain dark grey work trousers and grey work '
                   'boots, with a plain matte mustard-yellow cotton cap with '
                   'no marking of any kind'),
 'julian': ('JULIAN, a mestizo Colombian young man of about twenty-two, '
            'lean, short dark hair, clean-shaven, in plain mid-grey '
            "mechanic's coveralls unzipped to the waist with the sleeves "
            'tied around his hips over a plain light grey T-shirt and plain '
            'grey canvas shoes, with a plain matte mustard-yellow shop rag '
            'hanging from the back pocket of the coveralls'),
 'madrejulian': ("JULIAN'S MOTHER, a mestiza woman of about fifty, short and "
                 'sturdy, dark hair streaked with grey pulled into a low bun, '
                 'in a plain mid-grey cardigan over a plain grey dress and '
                 'flat grey shoes'),
 'companero': ('THE WORKMATE, a mestizo man of about thirty, stocky, short '
               'dark hair, in plain dark grey coveralls with the sleeves '
               'pushed up, a plain grey cloth in one hand'),
 'fernando': ('FERNANDO, a mestizo Colombian man of about forty-five, '
              'heavy-set, receding dark hair, a neat moustache, in a plain '
              'light grey short-sleeved button shirt under a plain matte '
              'mustard-yellow knitted sleeveless vest, plain grey trousers '
              'and plain dark grey shoes'),
 'esposafernando': ("FERNANDO'S WIFE, a mestiza woman of about forty-three, "
                    'medium build, shoulder-length dark hair, in a plain '
                    'mid-grey blouse over plain grey trousers and flat grey '
                    'shoes'),
 'manuel': ('DON MANUEL ANTONIO, a Colombian countryman of about fifty-eight, '
            'lean and weathered, short grey hair and a grey stubble, in a '
            'plain light grey long-sleeved work shirt, plain grey trousers '
            'tucked into plain dark grey rubber boots, and a wide-brimmed '
            'plain woven hat of muted matte mustard yellow with no band, no '
            'pattern and no ornament'),
 'mulo': ('A STURDY PACK MULE, plain grey-brown, with a plain grey pack '
          'saddle of padded cloth strapped on its back and a plain rope '
          'halter'),
 'familiamanuel': ("DON MANUEL'S FAMILY: a woman of about fifty-five in a "
                   'plain grey blouse and skirt with a plain grey shawl, and '
                   'a man of about twenty-five in a plain grey shirt and grey '
                   'trousers'),
 'gustavo': ('GUSTAVO ADOLFO, a mestizo Colombian man of about thirty-eight, '
             'tall and solid, short dark hair, in a plain light grey '
             'long-sleeved shirt over plain grey jeans and plain dark grey '
             'leather boots, with a plain matte mustard-yellow cotton '
             'kerchief knotted loosely at the open collar'),
 'testigos': ('A FEW PEOPLE OF THE AREA by the roadside: a street vendor of '
              'about sixty beside a plain grey hand cart, a man of about '
              'forty in a plain grey shirt, and a woman of about thirty-five '
              'in a plain grey blouse with a plain cloth bag'),
 'investigador': ('THE CRIMINAL INVESTIGATOR, a man of about forty, solid '
                  'build, close-cropped dark hair, in a plain dark grey zip '
                  'jacket over a plain light grey shirt and plain grey '
                  'trousers, no marking of any kind on the clothing'),
})

VIDA.update({
 'carlosalberto': ('Carlos Alberto drives the rural route every day and '
                   'everybody on it knows his truck; people stop him on the '
                   'road to talk about the community board. He keeps his '
                   'phone in the breast pocket of his shirt.'),
 'julian': ('Julián fixes motorbikes and trucks in a small workshop in town '
            'and is the friend the rural boys call when something breaks.'),
 'madrejulian': ('She has raised him alone and knows every one of his '
                 'moods.'),
 'companero': ('He has worked at the next bench for two years.'),
 'fernando': ('Fernando has sold seed, fertiliser and tools from the same '
              'shop for twenty years and knows half the vereda by name. He '
              'keeps his reading glasses in his shirt pocket.'),
 'esposafernando': ('She keeps the shop accounts and the house, and the '
                    'phone is always within reach.'),
 'manuel': ('Don Manuel has crossed the La Miel ford on the same mule for '
            'thirty years and reads the river by its colour. The hat never '
            'leaves his head.'),
 'familiamanuel': ('They know the river as well as he does.'),
 'gustavo': ('Gustavo Adolfo buys and sells cattle along the road to La '
             'Esperanza and walks it as if he owned it.'),
 'testigos': ('They have kept a stall or a doorway on this stretch of road '
              'for years.'),
 'investigador': ('He writes everything down in the order it happened and '
                  'nothing more.'),
})

# Quien lleva acento: el desaparecido de cada situacion y las dos mujeres
# Morales, que buscan. Nadie mas.
CON_ACENTO = {'carlosalberto', 'julian', 'fernando', 'manuel', 'gustavo',
              'rosaelena', 'mariana'}

# Quien no lleva rostro nunca.
SIN_ROSTRO = set(B.SIN_ROSTRO) | {'comandante', 'funcionario',
                                  'analistadenuncias', 'funcionarioturno',
                                  'fiscalturno', 'servidor'}

TOKENS = CUERPO


def arma(escena, registro='dia', personas=(), con_acento=None,
         con_lugar=True, con_rostro=True, exterior=False, silueta=False):
    """Arma el prompt final. `con_acento=None` lo decide el reparto: lleva
    acento si en el plano hay alguien de CON_ACENTO."""
    if con_acento is None:
        con_acento = any(p in CON_ACENTO for p in personas)
    p = [escena.strip()]
    if personas:
        vidas = [VIDA[x] for x in personas if x in VIDA]
        if vidas:
            p.append('WHO THESE PEOPLE ARE. ' + ' '.join(vidas))
    p.append(REGISTRO[registro])
    p.append(PLANOS)
    if silueta:
        p.append(ESTILO + FIGURA)
        p.append(SILUETA)
    else:
        con_cara = con_rostro and any(x not in SIN_ROSTRO and x != 'mulo'
                                      for x in personas)
        p.append(ESTILO + (ROSTRO if con_cara else '')
                 + (PIEL + ' ' if personas else '') + FIGURA)
    p.append(CAMARA)
    if con_acento:
        p.append(ACENTO)
    if con_lugar:
        p.append(EXTERIOR if exterior else LUGAR)
    p.append(LIMPIA)
    p.append(SIN_ROLES)
    p.append(NEG)
    return '\n\n'.join(x.strip() for x in p if x and x.strip())
