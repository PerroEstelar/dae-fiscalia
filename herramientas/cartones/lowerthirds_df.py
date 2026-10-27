#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Lower thirds del caso «Miriam y Mariana», los cinco capítulos.

DIEZ, Y CADA UNO TIENE QUE GANARSE EL SITIO
    El rótulo nombra a alguien que el espectador acaba de ver entrar y que la
    narración ya estableció. Si la voz no dice quién es, no hay rótulo: no se
    puede imprimir un cargo que la pieza no afirma.

    Por eso NO entran el asistente ni la psicóloga. Los dos aparecen en cuadro
    —C3 r03 y C4 r06— y los dos salen bien dibujados, pero la narración nunca
    los nombra: del asistente sólo existe la lista de roles del C3 b05, y de la
    psicóloga ni eso, apenas «se le brinda contención sicosocial». Es la misma
    decisión que tomó el P3C5 con su psicóloga y con la voz de «la entrega».

CADA DATO ES LO QUE EL DOCUMENTO DA POR ESTABLECIDO
    Nunca el hecho que el ejercicio pone a examinar. Del perito y del analista
    se imprime LO QUE HACEN —un dictamen, una matriz—, no lo que su trabajo
    busca demostrar: el analista integra la Matriz de contexto, y que exista un
    patrón macrocriminal es justamente la conclusión que el caso discute.

    De la familia se imprime el parentesco y el oficio, que la voz da literal:
    «madre de Miriam y lideresa campesina afrodescendiente», «hermana menor de
    Miriam», «su vecina Gregoria».

CADA CAPÍTULO SE PRESENTA SOLO
    Rosa Elena lleva rótulo en el C2 y otra vez en el C4, y la Fiscal en el C3
    y en el C4. No es repetición: son cinco piezas que se ven por separado, y
    quien abra el capítulo 4 no vio el 2. El dato cambia con lo que cada
    capítulo necesita —en el C2 Rosa Elena es la madre que empieza a buscar,
    en el C4 es la madre de las dos—.

EL ROTULO DE LUGAR VA, EL DE FECHA NO
    La voz da el municipio en la primera frase de la serie: «En el municipio de
    San José de las Peñas». De fecha da días y mes —el catorce de mayo, el
    veintiocho de mayo— pero NUNCA el año, así que un rótulo de fecha tendría
    que inventarlo o quedarse cojo. Se deja fuera.
"""
import os
import sys

sys.path.insert(0, "/home/claude/lt")
sys.path.insert(0, "/home/claude/cartones")
import lower_third as LT                              # noqa: E402

OUT = "/home/claude/dflt/out"

# Cinco segundos en pantalla. El P3C5 usaba 96 cuadros con una sola línea;
# aquí casi todos llevan nombre y dato, y 96 deja el dato corto de lectura.
N = 120

# Entra 14 cuadros despues de que abre la ranura: lo justo para que el corte
# se haya asentado antes de que suba la barra.
OFF = 14

#  capitulo -> [(archivo, ranura, spec)]
LOWERS = {
    1: [
        ("lt01_lugar", 1, {
            "nombre": "San José de las Peñas"}),
        ("lt02_miriam", 2, {
            "nombre": "Miriam",
            "dato": "Vende arepas en la plaza. Siete meses de embarazo."}),
        ("lt03_gregoria", 11, {
            "nombre": "Gregoria",
            "dato": "Vecina de Miriam. Reporta la desaparición."}),
    ],
    2: [
        ("lt01_rosaelena", 1, {
            "nombre": "Rosa Elena Morales",
            "dato": "Madre de Miriam. Lideresa campesina afrodescendiente."}),
        ("lt02_mariana", 2, {
            "nombre": "Mariana Morales",
            "dato": "Hermana menor de Miriam. Vocera de las familias buscadoras."}),
    ],
    3: [
        ("lt01_fiscal", 5, {
            "nombre": "Fiscal Especializada en Desaparición Forzada",
            "dato": "Asume la dirección estratégica de la investigación."}),
    ],
    4: [
        ("lt01_rosaelena", 1, {
            "nombre": "Rosa Elena Morales",
            "dato": "Madre de Miriam y de Mariana."}),
        ("lt02_fiscal", 4, {
            "nombre": "Fiscal Especializada",
            "dato": "Aplica el Protocolo de Atención Digna."}),
    ],
    5: [
        ("lt01_perito", 8, {
            "nombre": "Perito Forense",
            "dato": "Dictamen antropológico y genético."}),
        ("lt02_analista", 10, {
            "nombre": "Analista de Contexto",
            "dato": "Integra la Matriz de contexto del caso."}),
    ],
}


def archivo(cap, nom):
    return "%s/DF_C%d_%s.mov" % (OUT, cap, nom)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    caps = [int(a) for a in sys.argv[1:]] or sorted(LOWERS)
    for cap in caps:
        for nom, r, spec in LOWERS[cap]:
            LT.render(spec, N, archivo(cap, nom))
            print("   cap %d  r%02d  entra en el cuadro %d de la ranura"
                  % (cap, r, OFF))
