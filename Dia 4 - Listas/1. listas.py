# Lista: ES UNA ESTRUCTURA DE DATOS INMUTABLES, PERMITE ALMACENAR UNA SECUENCIA DE OBJETOS DE MANERA SECUENCIAL, NO NECESARIAMENTE TIENE QUE SER DEL MISMO TIPO DE OBJETO, PERO PARA ESTO SE RECOMIENDO USAR LAS TUPLAS:

# lista_numeros = [1, "Hola", True] (PARA HACER ESTO MEJOR USAR UNA TUPLA, LAS LISTAS DEJARLAS PARA SOLO UN TIPO DE DATO)
# print(lista_numeros)
# print(type(lista_numeros))

# SON MUTABLES:
lista_num = [1, 2, 3, 4] # => LAS LISTAS SE DECLARAN A TRAVES DE LLAVES CERRADAS: list = [x, y, z, ...]
print(lista_num, id(lista_num))

lista_num[0] = 69 # COMO SE PUEDEN AGRsEGAR, MODIFICAR, TAMBIEN SE PUEDEN ELIMINAR
print(lista_num, id(lista_num))


# FUNCION "list()": Podemos convertir elementos de otro tipo a listas
tupla_numeros = (1, 2, 3, 4)
print(type(tupla_numeros)) # => CREAMOS UNA TUPLA, O PODRIA SER CUALQUIER OTRO TIPO DE OBJETO

lista_numeros = list(tupla_numeros) # => CONVERTIMOS ESTA TUPLA EN UNA LISTA CON LA FUNCION: "list(x)"
print(type(lista_numeros))


# PRINCIPALES METODOS DE LAS LISTAS:
lista = [1, 2, 3, 4]
print(lista)

# ".append(x)": Permite agregar un elemento al ultimo de la fila
lista.append(5)
lista.append(5)
lista.append(5)
print(lista)


# ".count(x)": Permite contar cuantos elementos existen en la lista del mismo valor
print(lista.count(5)) # => Este print nos devolvera "3", ya que el "5", se repite 3 veces en la lista.


# ".extend(x)": Nos permite extender la lista usando otra lista
lista_extendida = [100, 101]
lista.extend(lista_extendida)
print(lista) # => A difernecia de ".append(x)", hacerlo de esta forma nos permitira agregarle a la lista mas elementos en una sola linea


# ".index(x)": Nos permite buscar en una lista un elemento y si sí existe nos devuelve el indice de dicho elemento:
print(lista.index(5)) # => Si se le pasa un valor que no este en la lista, por ejemplo, 1000, el retornara un "ValueError: 1000 is not in list"


# ".insert(x, y)": Al igual que ".append(x)", este nos permite agregar un elemento pero en cualquier parte de la lista usando el indice
print(lista)
lista.insert(0, 69) # => El primer valor corresponde al indice en la lista y el segundo al valor el cual se va a insertar, 
                    # como se puede observar, esto no remplaza, mas bien empuja a la derecha, el elemento posicionado en ese indice.
print(lista)


# ".pop(x)": Extrae elementos de mi lista y me los retorna
print(lista)
print(lista.pop(0)) # => Tambien se puede dejar el argumento de ".pop()" vacio, lo cual nos devuelve el ultimo elemento de la lista 
print(lista) # => Podemos observar como no solo imprime el elemento, tambien lo extrae de la listas


# ".remove(x)": Permite eliminar varios elementos de mi lista, esta vez no se eliminan por indice sino por valor
print(lista)
lista.remove(100)
print(lista)


# ".reverse()": Permite invertir la lista que pase de [1, 2, 3] a [3, 2, 1]
print(lista)
lista.reverse()
print(lista)


# ".clear()": Permite eliminar todos los elementos de una lista
print(lista)
lista.clear()
print(lista)


# ".sort()": Ordena una lista desordenada
lista_desordenada = [5, 25, 3, 1, 88, 69, 4, 6, 3, 100]
print(lista_desordenada)
lista_desordenada.sort()
print(lista_desordenada)