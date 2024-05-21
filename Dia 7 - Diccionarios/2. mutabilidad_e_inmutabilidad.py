# TODOS LOS TIPOS DE OBJETOS, STRING, FLOAT, INT, LISTAS, TUPLAS, TIENEN 2 CATEGORIAS INMUTABLES(NO PUEDEN SER CAMBIADOS DESPUES DE SER CREADOS) O MUTABLES(PUEDEN CAMBIAR).

# INMUTABLES: INT, FLOAT, STRINGS, BOOLEANOS, ETC.
# edad = 19
# print(type(edad), id(edad))
# print("\n")
# edad = 20
# print(type(edad), id(edad))
# CON ESTE EJEMPLO SE VE COMO SON DIFERENTES OBJETOS YA QUE PYTHON BORRA EL OBJETO ANTERIOR Y CREA UNO NUEVO, EL ID LO DEMUESTRA, SON DIFERENTES POR LO TANTO INMUTABLES.

# print("\n")

# MUTABLES: LISTA, TUPLAS, DICCIONARIOS, ETC.
# lista = [1, 2, 3, 4, 5]
# print(lista)
# print(type(lista), id(lista))
# print("\n")
# lista.append(6)
# print(type(lista), id(lista))
# print(lista)


# EJEMPLO PARA DEMOSTRAR LA IMPORTANCIA DE CONOCER LA MUTABILIDAD E INMUTABILIDAD:

lista_estudiantes = ["Cristhian", "Cortes"]
print(lista_estudiantes)

print("\n")

lista_estudiantes_nuevos = lista_estudiantes
print(lista_estudiantes_nuevos)

lista_estudiantes_nuevos.append("Ariza")
print(f"Lista de estudiantes nuevos: {lista_estudiantes_nuevos}")

print("\n")

print(f"Lista de estudiantes originales: {lista_estudiantes}")

print("\n")
 
print("Lista original:", id(lista_estudiantes), ", Lista nueva:",id(lista_estudiantes_nuevos))

# ACA ARRIBA SE EVIDENCIA EL ERROR GIGANTE DE NO SABER QUE LA LISTA Y DEMAS OBJETOS DE ESE TIPO SON MUTABLES POR LO QUE AL ASIGNARLE EL VALOR DE UNA VARIABLE A LA OTRA, LOS CAMBIOS
# QUE SE HAGAN EN UNA SE APLICARAN EN LA OTRA, LO CUAL AFECTARA NUESTRO TRABAJO
# POR ESO ES MUY IMPORTANTE SABER CUALES OBJETOS SON MUTABLES E INMUTABLES

