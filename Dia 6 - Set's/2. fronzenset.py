frutas = {
    'manzana',
    'banano',
    'pera',
    'uva'
}

# FROZENSET: ES UN SET QUE NO PUEDES MODIFICAR LO CUAL LO HACE INMUTABLE, LO QUE HACE UNA MEJORA EN LA MEMORIA
mi_frozenset = frozenset(frutas) # => COMO ARGUMENTO SE PUEDE PASAR CUALQUIER ITERABLE, COMO UNA LISTA, UN SET, STRINGS, ETC...

# UNA VEZ CREADO NO SE PUEDE MODIFICAR DE NINGUNA FORMA, LOS USOS MAS COMUNES SON PARA OPTIMIZAR MEMORIA O PARA USARLOS DE LLAVE EN UN DICCIONARIO
mi_frozenset.add('naranja')
print(mi_frozenset)