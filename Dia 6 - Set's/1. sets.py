# ESTRUCTURA DE DATOS MUTABLE , NO PUEDEN SER ORDENADOS, LOS OBJETOS QUE ALMACENEN LOS SETS DEBEN SER HASHEABLES, NO PERMITEN DATOS DUPLICADOS

# Declaracion {x, y, z}. Primera forma:
mi_set = {1, 3, 2, 4}
print(mi_set)

# Segunda forma: Usando la funcion "set(x)"
mi_set = set() # => Al dejarlo vacio, estamos declaranto que nuestro set estara vacio
print(mi_set)
mi_set.add(1) # => Para agregar elementos a un set, usaremos, ".add(x)"
mi_set.add(2)
print(mi_set)

# LOS SET'S NO PERMITEN ELEMENTOS DUPLICADOS, EL RETORNARA EL SET SIN ELEMENTOS DUPLICADOS

# EJEMPLO PRACTICO:
# DEVOLVER UNA LISTA SIN ELEMENTOS DUPLICADOS
lista = [1, 1, 1, 2, 3, 4, 5, 6, 6, 7]
lista_no_repetida = set(lista)
print(lista)
print(lista_no_repetida)


# CARACTERISTICAS ADICIONALES:
mi_set = set(lista)
pertenece = 10 in lista
print(pertenece)

# LOS SET's DEBEN USARSE PARA DETECTAR UNA PERTENENCIA, YA QUE ESTAN MUY OPTIMIZADOS PARA HACER ESTE TIPO DE BUSQUEDAS, MAS RAPIDO QUE HACERLO CON LA LISTA DIRECTAMENTE

frutas = {
    'manzana',
    'banano',
    'pera',
    'uva'
}

# RECORDAR QUE LOS ELEMENTOS DE LOS SET's DEBEN SER HASHEABLES ES DECIR; EL ELEMENTO U OBJETO VA A TENER UN VALOR UNICO DESDE SU CREACION HASTA SU ELIMINACION (ELEMENTOS INMUTABLES)
# ESTO CON EL FIN DE QUE UNA FUNCION LE ASIGNE UN IDENTIFICADOR UNICO
print(hash('manzana')) # => IDENTIFICADOR: -7051419524861388515

