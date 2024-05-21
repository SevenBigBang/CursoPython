# BREAK, ES LA SENTENCIA MAS USADA EN LOS CICLOS DE PYTHON, LO QUE HACE ES DEACUERDO A UNA CONDICION DE MI CICLO
# PERMITE PARAR EL CICLO ASI NO SE HAYA CUMPLIDO LA CONDICION DE SALIDA O LA CANTIDAD DE ITERACIONES
 
# IMPORT LIBRERIA PARA GENERAR NUMEROS RANDOM's
import random

x = random.randint(1, 13) # FUNCIONAMIENTO: random.randint(x, x), DE LA LIBRERIA RANDOM, LLAMAMOS AL METODO RANDOM ENTERO POR SUS SIGLAS EN INGLES (Rand-Int)
print(x) 

# CARRERA DE CARACOLES JUEGO:


# PRIMER OPCION: 
meta = 20
caracol_1 = 0
caracol_2 = 0

while caracol_1 < 20 and caracol_2 < 20:
    caracol_1 += random.randint(1, 4)
    caracol_2 += random.randint(1, 4)

    print(f"Posicion del caracol 1: {caracol_1}")
    print(f"Posicion del caracol 2: {caracol_2}")
    print("-----------------------------------------")    
if caracol_1 > caracol_2:
    print("\nEl ganador es El caracol 1\n")
elif caracol_2 > caracol_1:
    print("\nEl ganador es el caracol 2\n")
else:
    print("\nEMPATE\n")




# SEGUNDA OPCION: USANDO BREAK
while True:
    caracol_1 += random.randint(1, 4)
    caracol_2 += random.randint(1, 4)

    print(f"Posicion del caracol 1: {caracol_1}")
    print(f"Posicion del caracol 2: {caracol_2}")
    print("-----------------------------------------")

    if caracol_1 >= 20 or caracol_2 >= 20:
        break                                  # ==> SE PONE "break" PARA QUE SALGA DEL CICLO WHILE INFINITO CREADO CON "while True:" , TAMBIEN APLICA PARA EL CICLO FOR
     
if caracol_1 > caracol_2:
    print("\nEl ganador es El caracol 1\n")
elif caracol_2 > caracol_1:
    print("\nEl ganador es el caracol 2\n")
else:
    print("\nEMPATE\n")  

