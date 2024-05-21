# COMPRENSION DE DICCIONARIOS: FUNCIONA IGUAL QUE LOS LIST COMPREHENSION

# EJERCICIO: A PARTIR DE LA LISTA, CREAR UN DICCIONARIO QUE TENGA COMO LLAVE EL ELEMENTO DE LA LISTA Y COMO VALOR EL ELEMENTO DE LA LISTA ELEVADO A LA DOS:

lista = [1, 2, 3, 4, 5, 6]
cuadrados_diccionario = {}


# BUCLE FOR:
for x in lista:
    cuadrados_diccionario[x] = x**2
print(cuadrados_diccionario)


print("\n\n")       # CUANDO TU DEFINES UN DICCIONARIO TIENES QUE PONER:
# dict comprehension:   clave : valor
cuadrados_diccionario = {x : x ** 2 for x in lista} # primero se crea una varible con diccionario, despues a la derecha pones el bucle for con su iterable correspondiente y por ultimo a la izq
#                                                     pones la operacion en este caso; el numero por defecto al iterar : y despues x (variable que guarda la elevacion a la 2), y todo esto 
#                                                     se hace en base a cada iteracion.
#                                                     nombre_diccionario = {llave : valor operacion for x in iterable}; => PLANTILLA BASICA
print(cuadrados_diccionario)


# LA COMPRENSION DE DICCIONARIO FUNCIONA EXACTAMENTE IGUAL QUE LA COMPRENSION DE LA LISTA, TODO LO QUE SE PUEDE HACER EN LIST COMPREHENSION SE PUEDE Y SE PODRA HACER EN DICT Y SET COMPREHENSION:



# EJERCICIOS:

# 1. solicita al usuario ingresar un número y luego imprime su tabla de multiplicar del 1 al 10.


# 2. toma una lista de palabras y las convierte en una sola cadena, separadas por comas y con "y" antes de la última palabra.




# ESTOS EJERCICIOS TIENEN MAS DIFICULTAD NO OLVIDES REVISAR APUNTES ANTERIORES 