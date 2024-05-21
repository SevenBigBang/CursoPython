# FUNCION DE ORDEN SUPERIOR - REDUCE: SE UTILIZA PARA APLICAR UNA FUNCION DE MANERA ACOMULATIVA A LOS ELEMENTOS DE UN ITERABLE, REDUCIENDOLOS A UN SOLO VALOR.


# LA FUNCION REDUCE(), LA TENEMOS QUE IMPORTAR:
from functools import reduce


# TAREA 1: APLICAR UNA SUMATORIA TOTAL DE TODOS LOS ELEMENTOS DE LA LISTA 'numeros[x, y, z, ...]'
numeros = [1, 2, 3, 4, 5]

# DECLARAR LA FUNCION:
# def sumatoria(num1, num2):
#     return num1 + num2

# FUNCION LAMBDA:
# lambda num1, num2 : num1 + num2


total = reduce(lambda x, y : x + y, numeros) # ==> EN ESTE CASO, EL RETORNO DE LA FUNCION 'reduce(funcion_x, iterable_x)', NO ES UN OBJETO, POR LO CUAL LO PODEMOS IMPRIMIR
                                             #     SIN IMPORTAR QUE, TAMBIEN FUNCIONA DE LA MISMA MANERA, (FUNCION, ITERABLE)
print(total)