# COMPRENSION DE SET's: TIENE LAS MISMAS FUNCIONES QUE EL LIST COMPREHENSION



# EJERCICIO: A PARTIR DE UNA LISTA CREAR UN SET CON LOS CUADRADOS DE CADA UNO DE LOS ELEMENTOS DE LA LISTA

lista = [1, 2, 3, 4, 5, 5]
cuadrados_set = set() # ==> set(); funcion para crear un set

# BUCLE FOR:
for x in lista:
    cuadrados_set.add(x**2)
print(cuadrados_set)


cuadrados_set = {x**2 for x in lista} # ==> SE CREA DE FORMA SIMILIAR A UN DICCIONARIO CON CORCHETES "{}", PERO COMO NO TIENE LOS DOS PUNTOS QUE ASIGNAN UN VALOR A UNA CLAVE ":", PYTHON NO LO
                                      #     TOMARA COMO DICCIONARIO SINO COMO SET:
                                      #     nombre_set = {operacion for x in iterable} ==> PLANTILLA PARA USAR SET COMPREHENSION

# COMO TE LO DIJE TODO LO QUE HICIMOS CON LAS LISTAS SE PODRA HACER CON EL DICCIONARIO Y SET; ENTONCES NO TE LIMITES A ESTE EJEMPLO QUE HAGO, SOLO NO LO REPITO POR NO REPETIR CODIGO
# PERO TU LO PODRIAS HACER :)


# EJERCICIOS:


# 1. A partir de una lista haz un filtrado de Números Pares:



# 2. toma una lista y genera un conjunto que contiene solo los elementos únicos de la lista.


# 3. Realiza las funciones de list comprehension con set comprehension: 