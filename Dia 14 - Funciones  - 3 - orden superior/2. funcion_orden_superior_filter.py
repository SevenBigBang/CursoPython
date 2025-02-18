# FUNCION DE ORDEN SUPERIOR - FILTER: LA SEGUNDA MAS UTILIZADA, SE UTILIZA PARA FILTRAR ELEMENTOS DE UNA SECUENCIA, COMO UNA LISTA, TUPLA O CULAQUIER OTRO ITERABLE,
#                                     BASANDOSE EN UNA FUNCION CONDICIONAL QUE SE PROPORCIONA.

# LA PRINCIPAL CARACTERISTICA DE LAS FUNCIONES DE ORDEN SUPERIOR EN PROGRAMACION ES QUE PUEDEN RECIBIR FUNCIONES COMO ARGUMENTOS Y/O DEVOLVER FUNCIONES COMO RESULTADOS.



# EJEMPLO PRACTICO 1: DE ACUERDO AL ITERABLE 'numeros' GENERAR UN NUEVO ITERABLE CON SOLO PARES:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# DECLARAR FUNCION:
# def pares(num):
#     return num % 2 == 0 # ==> AL APLICAR ESTA LOGICA, EL RETURN NOS DEVOLVERA UN 'TRUE' SI ES PAR Y UN 'FALSE' SI ES IMPAR, COMBINANDO CON filter(funcion_x, iterable_x),
                        #     FILTER TRABAJA ACEPTANDO TRUE's, Y EXCLUYENDO FALSE's, LO CUAL NOS SIRVE MUCHO EN ESTE CASO.

# COMO ES EVIDENTE ESTA FUNCION ES MUY ESPECIFICA Y PUNTUAL ASIQ CREAREMOS UNA FUNCION LAMBDA:
# lambda num : num % 2 == 0
                    
lista_pares = list(filter(lambda x : x % 2 == 0, numeros)) # ==> DE IGUAL MANERA TENEMOS QUE CASTEAR DE FILTER A ALGUN ITERABLE PARA PODER VISUALIZARLO CORRECTAMENTE, EN ESTE CASO UNA LISTA
print(lista_pares)



# EJEMPLO PRACTICO 2: TENEMOS UNA LISTA DE NOMBRES APLICA UN FILTRADO PARA RETORNAR LOS NOMBRES QUE EMPICEN CON LETRA A:
nombres = ["Alice", "Bob", "Anna", "David", "Amelia", "Charlie", "Cristhian"]

# DECLARAR FUNCION:
# def nombres_a(nombre):
#     return nombre[0] == 'A'

# FUNCION EN LAMBDA:
# lambda nombre: nombre[0] == 'A'

lista_nombres_a = list(filter(lambda x: x[0] == 'A', nombres))
print(lista_nombres_a)