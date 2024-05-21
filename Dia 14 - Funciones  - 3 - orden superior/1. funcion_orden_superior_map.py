# FUNCION DE ORDEN SUPERIOR: ES MUY COMUN QUE PREGUNTEN SOBRE LAS FUNCIONES DE ORDEN SUPERIOR, SON FUNCIONES QUE ACEPTAN A OTRA FUNCION (DE ´REFEROEMCOA QIE SEA FUNCION LAMBDA) 
#                            COMO ARGUMENTO, LA CUAL APLICARA AL ALGURMENTO QUE LE PASEN, PUEDEN RETORNAR FUNCIONES O LISTAS


# FUNCION DE ORDEN SUPERIOR - MAP: LA MAS UTILIZADA, APLICA UN CONJUNTO DE REGLAS A VARIOS ELEMENTOS DE UN ITERABLE
# "map()": SE UTILIZA PARA APLICAR UNA FUNCION A TODOS LOS ELEMENTOS DE UNA O MAS SECUENCIAS, COMO LISTAS, TUPLAS O ITERABLES SIMILARES. TOMA DOS ARGUMENTOS PRINCIPALES:
#          LA FUNCION QUE SE APLICARA Y UNA O MAS SECUENCIAS DE DATOS SOBRE LAS QUE SE APLICARAN LA FUNCION.
lista_nombre = ['cristhian', 'cortes', 'ariza']

# TAREA 1: CONVERTIR LA LISTA DE NOMBRES A MAYUSCULA:   # USAMOS LA FUNCION INTENGRADA DE PYTHON. str.upper, YA QUE NOS VIENE DE ANILLO AL DEDO PARA LA TAREA A REALIZAR
lista_nombre_mayus = list(map(str.upper, lista_nombre)) # ==> primero declaramos una variable 'lista_nombre_mayus', para empezar usamos 'map(funcion_x, iterable_x)' la cual nos aplicara
                                                        #     la funcion a cada elemento del iterable, despues de esto tenemos que hacer un casteo (convertir de map() a list[]), 
                                                        #     ya que, si imprimimos map(), nos retornara un objeto tipo map, entonces es muy importar castear map a otro tipo de 
                                                        #     formas para que podamos visualizarla correctamente, list, tuple, dict, etc...
print(lista_nombre_mayus)




# TAREA: AGREGAR UN SUBFIJO A CADA ELEMENTO DE LA LISTA DE FRUTAS, EL SUFIJO ES (_fruta); USAR MAP() CON UNA FUNCION CREADA POR NOSOTROS
lista_frutas = ['banano', 'pera', 'manzana', 'uva']
sufijo = '_fruta'

# FUNCION PARA AGREGAR SUFIJO:
# def add_sufix(fruta):
#     return fruta + sufijo

# FUNCION LAMBDA YA QUE LA FUNCION ANTERIOR ES MUY SIMPLE:
# lambda fruta : fruta + sufijo

lista_frutas_sufijo = list(map(lambda x : x + sufijo, lista_frutas))
print(lista_frutas_sufijo)