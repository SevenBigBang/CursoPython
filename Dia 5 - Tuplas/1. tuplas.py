# ES UNA ESTRUCTURA DE DATOS INMUTABLES, PERMITE ALMACENAR UNA SECUENCIA DE OBJETOS Y ACCEDER A ELLOS A TRAVES DE SU INDICE 

#mi_tupla = (1, True, 'Cristhian', 0.14)
# AL SER INMUTABLE NO SE PUEDE MODIFICAR:
# mi_tupla[0] = 5
# print(mi_tupla)

# Tambien se puede declarar una tupla sin paretencis (no son necesarios, pero las comas si!)
mi_tupla = 1, True, 'Cristhian', 0.14
print(type(mi_tupla))


# Una caracteristica importante de una tupla es que permite devolver mas de un elemento en una funcion:
def retornar_estudiante():
    return 'Cristhian', 20, 8.6
tupla_estudiante = retornar_estudiante()
print(tupla_estudiante, type(tupla_estudiante))

# Creacion de multivariables en una sola linea:             
nombre_estudiante, edad_estudiante, promedio_estudiante = retornar_estudiante() # => DESEMPAQUETADO CADA INDICE EMPEZANDO DE CERO, SE VA A DESEMPAQUETAR EN CADA VARIABLE EN ESE ORDEN
print(f"Nombre: {nombre_estudiante}, Edad: {edad_estudiante}, Promedio: {promedio_estudiante}")

# One-line swapping o INTERCAMBIO DE LINEAS

variable_1 = 1.0
variable_2 = 2.0
print(variable_1, variable_2)
# variable_1 = 2.0
# variable_2 = 1.0

# GRACIAS A LAS TUPLAS PODEMOS HACER ONE-LINE SWAPPING, INTERCAMBIO DE VARIABLES EN UNA SOLA LINEA DE CODIGO:

variable_1, variable_2 = (variable_2, variable_1) # => Creamos una tupla con las variables y las desempaquetamos en las variables que querramos
print(variable_1, variable_2)