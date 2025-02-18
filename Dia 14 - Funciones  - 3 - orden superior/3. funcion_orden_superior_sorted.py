# FUNCION DE ORDEN SUPERIOR - SORTED(): ESTA FUNCION PERMITE ORDENAR LOS ELEMENTOS DE UN ITERABLE, EN BASE UNA LLAVE.

# SORTED: LA FUNCION SORTED TOMA COMO MINIMO UN ITERABLE (POR EJEMPLO, UNA LISTA) Y DEVUELVE UNA NUEVA LISTA QUE CONTIENE LOS ELEMENTOS ORDENADOS.

estudiantes = [
    ('Cristhian', 22, 95, '3132356659'),
    ('Cortes', 20, 15, '3172485549'),
    ('Ariza', 11, 99, '3154685433')
]

# EJERCICIO: CREAR UN ITERABLE APARTIR DE LA LISTA ESTUDIANTES, Y QUE LO ORDENE EN BASE A LA LLAVE EDAD DE MENOR A MAYOR

# DECLARAR FUNCION:
# def ordenar_por_edad(estudiante):
#     return estudiante[1]

# FUNCION LAMBDA:
#lambda estudiante : estudiante[1]  # ==> EN ESTA FUNCION SE PLANEA BUSCAR EN EL INDICE 1 EL CUAL EN LA LISTA REPRESENTA LA EDAD, PARA ASI ORDENARLOS DE MENOR A MAYOR


lista_estudiantes_ordenados = list(sorted(estudiantes, key=lambda x : x[1])) # ==> COMO SIEMPRE SE CASTEA A LISTA EN ESTE CASO, PERO PUEDE SER CUALQUIER ITERABLE.
print(lista_estudiantes_ordenados)

# LA FUNCION SORTED: ACEPTA EL ITERABLE PRIMERO Y DESPUES EN UNA LLAVE LA FUNCION, (ORDENAR UN CONJUNTO DE ELEMNTOS EN BASE A UNA LLAVE)