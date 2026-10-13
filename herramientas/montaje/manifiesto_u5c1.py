# -*- coding: utf-8 -*-
import json

B = ("E:\\DAE MASTER\\CURSO 1 - SRPA\\UNIDAD 1 - PROFE CARLOS HUMBERTO\\"
     "UNIDAD 5\\cASO 1")
P, M, R = B + "\\01 PLANOS", B + "\\07 MOVIMIENTO", B + "\\10 TIMELINE SEBASTIAN\\RANURAS"

ARCH = {"kf01_avenida":"U5C1_kf01_avenida.png","kf02_grupo":"U5C1_kf02_grupo.png",
 "kf03_acera":"U5C1_kf03_acera.png","kf04_bolsillo":"U5C1_kf04_bolsillo.png",
 "kf05_telefono":"U5C1_kf05_telefono.png","kf06_evidencias":"U5C1_kf06_evidencias.png",
 "kf07_archivo":"U5C1_kf07_archivo.png","kf08_noche":"U5C1_kf08_noche.png",
 "kf09_pasaje":"U5C1_kf09_pasaje.png","kf10_yos":"U5C1_kf10_yos.png",
 "kf11_yefry":"U5C1_kf11_yefry.png","kf12_juanes":"U5C1_kf12_juanes.png",
 "kf13_audiencia":"U5C1_kf13_audiencia.png","kf14_expedientes":"U5C1_kf14_expedientes.png",
 "kf15_corredor":"U5C1_kf15_corredor.png"}
CON_MOV = {"kf01_avenida","kf02_grupo","kf03_acera","kf10_yos","kf11_yefry",
           "kf12_juanes","kf13_audiencia"}

# ranura -> inicio dentro del clip de movimiento
INICIO = {1:20, 2:30, 3:150, 4:150, 5:40, 10:60, 16:60, 17:120, 18:150,
          19:100, 21:20, 22:0, 24:20, 26:30}
# ranura -> camara (encuadre, empuje, derivaX, centroX, centroY, fase)
CAM = {6:(0.90,0.050,0.0,0.50,0.50,1.3), 7:(0.88,-0.040,0.0,0.50,0.50,4.8),
 8:(0.92,0.055,0.0,0.50,0.50,7.2), 9:(0.88,0.035,0.03,0.50,0.50,2.6),
 11:(0.82,-0.045,0.0,0.52,0.50,11.4), 12:(0.90,0.040,0.0,0.50,0.52,5.9),
 13:(0.86,-0.050,0.0,0.50,0.50,9.7), 14:(0.80,0.035,0.0,0.47,0.52,14.1),
 15:(0.92,0.060,0.0,0.50,0.50,3.4), 20:(0.90,0.045,0.0,0.50,0.50,6.5),
 23:(0.80,-0.040,0.0,0.53,0.49,12.8), 25:(0.91,0.050,0.0,0.50,0.50,8.3),
 27:(0.82,-0.055,0.0,0.50,0.50,15.6)}

filas = json.load(open("rejilla.json"))
trab = []
for i, (nom, ini, n) in enumerate(filas, 1):
    sal = "%s\\U5C1_r%02d_%s_v%d.mov" % (R, i, nom, n)
    if nom in CON_MOV:
        trab.append({"fuente": "%s\\U5C1_mov_%s.mp4" % (M, nom), "modo": "loop",
                     "frames": n, "inicio": INICIO[i], "salida": sal})
    else:
        enc, emp, dx, cx, cy, fa = CAM[i]
        trab.append({"fuente": "%s\\%s" % (P, ARCH[nom]), "modo": "camara",
                     "frames": n, "salida": sal, "encuadre": enc, "empuje": emp,
                     "deriva": [dx, 0.0], "centro": [cx, cy], "vibra": 6.0,
                     "fase": fa})
json.dump(trab, open("planos_u5c1.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

CLIP = {"kf01_avenida":241,"kf02_grupo":241,"kf03_acera":241,"kf10_yos":241,
        "kf11_yefry":241,"kf12_juanes":241,"kf13_audiencia":289}
avisos = [ "r%02d %s: faltan %d" % (i, nom, n - (CLIP[nom] - INICIO[i]))
           for i, (nom, ini, n) in enumerate(filas, 1)
           if nom in CON_MOV and n > CLIP[nom] - INICIO[i] ]
print("\n".join(avisos) if avisos else "todas las ventanas de movimiento caben")
print("%d ranuras: %d con movimiento, %d con camara, %d cuadros"
      % (len(trab), sum(1 for t in trab if t["modo"] == "loop"),
         sum(1 for t in trab if t["modo"] == "camara"), sum(x[2] for x in filas)))
