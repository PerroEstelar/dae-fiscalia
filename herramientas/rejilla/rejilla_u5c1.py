# -*- coding: utf-8 -*-
"""La rejilla de Los Chapulines: 15 planos sobre 3565 cuadros de narracion.

El reparto sale de la proporcion de caracteres de cada tramo de texto, y cada
corte se imanta al silencio real mas cercano de la locucion medida.
"""
FPS = 23.976023976
CUADROS = round(148.700590 * FPS)      # 3565

# fin de cada silencio real y su duracion, medidos sobre el master
SIL = [(7.50,0.43),(11.48,0.51),(12.00,0.51),(13.95,0.66),(16.42,0.62),(19.47,0.73),
 (24.65,0.57),(27.04,0.92),(30.37,0.75),(33.86,0.79),(36.53,0.66),(38.61,1.28),
 (44.13,1.12),(46.09,0.76),(47.71,0.37),(51.86,1.05),(54.97,1.21),(59.60,0.37),
 (62.68,0.71),(66.57,1.16),(69.18,0.74),(71.23,0.49),(73.33,1.19),(76.28,0.80),
 (77.23,0.62),(79.16,0.75),(81.70,1.25),(83.59,0.74),(90.62,0.41),(96.66,0.70),
 (103.99,0.89),(105.02,0.77),(108.52,0.58),(110.44,0.65),(113.98,1.08),(115.23,0.94),
 (119.69,0.35),(121.93,0.99),(123.31,1.00),(125.35,1.21),(129.40,0.85),(131.74,1.02),
 (134.13,0.88),(135.59,0.63),(136.82,0.99),(143.91,0.94),(148.70,0.43)]
# el centro de cada silencio es donde se puede cortar sin partir una palabra
CORTES = sorted(round((f - d / 2.0) * FPS) for f, d in SIL)

# los quince tramos, en el orden del guion, con su peso en caracteres
TRAMOS = [
 ("kf01_avenida",   "Entre el primero de enero de dos mil veinticuatro y el siete de mayo de dos mil veintiseis,"),
 ("kf02_grupo",     "en la localidad de Santa Maria, opero una organizacion conocida como Los Chapulines."),
 ("kf01_avenida",   "Al menos diez personas."),
 ("kf02_grupo",     "Entre ellas, varios adolescentes."),
 ("kf03_acera",     "Abordaban a sus victimas en la calle. Las intimidaban con armas,"),
 ("kf04_bolsillo",  "y las despojaban de sus telefonos, de su dinero y de lo que llevaran encima."),
 ("kf05_telefono",  "La Fiscalia no lo llama robo callejero."),
 ("kf06_evidencias","Lo llama hurto calificado y agravado, y la diferencia no es de palabras: es de pena."),
 ("kf07_archivo",   "Lo sustraido en ese periodo asciende a ciento treinta millones de pesos."),
 ("kf01_avenida",   "No es el valor de un hecho. Es la suma de muchos,"),
 ("kf07_archivo",   "y es lo que convierte una serie de atracos en una empresa."),
 ("kf08_noche",     "El expediente no se detiene ahi."),
 ("kf09_pasaje",    "A la organizacion se le atribuyen ademas delitos contra la libertad, la integridad y la formacion sexuales,"),
 ("kf08_noche",     "cometidos contra algunas de las mismas victimas."),
 ("kf09_pasaje",    "Eso cambia la naturaleza del caso, y cambia lo que el sistema puede hacer con el."),
 ("kf10_yos",       "Tres de los procesados son adolescentes. Yos tiene dieciseis anos."),
 ("kf11_yefry",     "Yefry tiene diecisiete."),
 ("kf12_juanes",    "Juanes tiene catorce."),
 ("kf13_audiencia", "A los tres se les atribuyen cinco eventos delictivos desarrollados por la organizacion en ese mismo periodo."),
 ("kf14_expedientes","Los mismos hechos, la misma banda, el mismo expediente. Y tres edades distintas."),
 ("kf13_audiencia", "Para el analisis en el Sistema de Responsabilidad Penal para Adolescentes hay que sopesar tres factores."),
 ("kf10_yos",       "Uno. La edad de cada procesado al momento de los hechos, que no es un dato de registro: es lo que define que respuesta cabe para cada uno."),
 ("kf14_expedientes","Dos. La gravedad de las conductas atribuidas, que dentro de esta misma organizacion no es la misma para todas."),
 ("kf12_juanes",    "Tres. La permanencia. Dos anos y cuatro meses no describen un episodio: describen una pertenencia."),
 ("kf15_corredor",  "El expediente es uno solo. Las respuestas, no."),
 ("kf11_yefry",     "Reconocer que tres adolescentes participaron de la misma organizacion es apenas el comienzo del analisis."),
 ("kf15_corredor",  "Lo que el sistema tiene que resolver despues es que corresponde a cada uno."),
]

total = sum(len(t) for _, t in TRAMOS)
acum, objetivo = 0, []
for nom, t in TRAMOS:
    acum += len(t)
    objetivo.append(round(acum / total * CUADROS))

def imantar(c, usados):
    libres = [x for x in CORTES if x not in usados and 0 < x < CUADROS]
    if not libres:
        return c
    mejor = min(libres, key=lambda x: abs(x - c))
    return mejor if abs(mejor - c) <= round(2.0 * FPS) else c

usados, bordes = set(), []
for i, c in enumerate(objetivo[:-1]):
    b = imantar(c, usados)
    usados.add(b)
    bordes.append(b)
bordes.append(CUADROS)

print("%-3s %-18s %7s %7s %7s %6s" % ("#", "plano", "entra", "sale", "cuadros", "seg"))
ini = 0
filas = []
for i, ((nom, _), fin, obj) in enumerate(zip(TRAMOS, bordes, objetivo)):
    n = fin - ini
    print("%-3d %-18s %7d %7d %7d %6.1f" % (i + 1, nom, ini, fin, n, n / FPS))
    filas.append((nom, ini, n))
    ini = fin
print("suma", sum(f[2] for f in filas), "de", CUADROS)
corto = [f for f in filas if f[2] < round(2.8 * FPS)]
print("ranuras por debajo de 2,5 s:", [(f[0], f[2]) for f in corto] or "ninguna")
import json
json.dump(filas, open("rejilla.json", "w"))
