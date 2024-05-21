# DICCIONARIOS: FUNCIONA IGUAL QUE UN DICCIONARIO EN LA VIDA REAL, USAN UNA CLAVE Y UN VALOR RESPECTIVAMENTE

# VALOR (CONTENIDO): PUEDE SER UNA LISTA, STRING, INT, OBJETO, ETC...
# CLAVE (IDENTIFICADOR): TIENE QUE SER UN OBJETO HASHEABLE, ES DECIR UN OBJETO INMUTABLE

# BENEFICIOS: EN LA BUSQUEDA SE OPTIMIZA LA VELOCIDAD, YA QUE USAN UN HASHTABLE

# DECLARACION:

# PRIMERA FORMA:
mi_diccionario = {
    'Edward': [1.4, 4.5, 5.0],
    'Cristhian': [4.0, 3.5, 5.0],
    'Carla': [3.0, 5.0, 5.0]
}

# SEGUNDA FORMA A TRAVES DEL METODO 'Dict':
mi_diccionario_2 = dict(                 # => Como se puede observar cambia mucho, tanto que las llaves dejan de ser strings o escribirse como tal, como de ya no usar los dos puntos
    Edward = [1.4, 4.5, 5.0],            # Para definir el valor de la clave 
    Cristhian = [4.0, 3.5, 5.0],
    Carla = [3.0, 5.0, 5.0]
)

print(f"\nForma tradicional: {mi_diccionario} \n\nUsando dict(x): {mi_diccionario_2}")

# TERCERA FORMA, DECLARARLO VACIO E IR AGREGANDO LA CLAVE Y EL VALOR:
mi_diccionario_3 = {} # o tambien se puede usar el metodo "dict()", vacio
mi_diccionario_3['Edad de Edward'] = [20] # => SE LLAMA A LA VARIABLE QUE CONTIENE EL DICCIONARIO CON LLAVES PONEMOS PRIMERO LA CLAVE Y SEGUIDO DE UN IGUAL "=" EL VALOR
mi_diccionario_3['Edad de Cristhian'] = [24]
mi_diccionario_3['Edad de Carla'] = [28]
print(f"\nDiccionario vacio: {mi_diccionario_3}")



# OTRA CARACTERISITICA DE LOS DICCIONARIO ES QUE SON MUTABLES, ES DECIR, SE PUEDE MODIFICAR EL VALOR UNA VEZ HAYAN SIDO CREADOS
diccionario = {
    'primer_nombre': ['Cristhian'],
    'primer_apellido': ['Cortes'],
    'segundo_apellido': ['Ariza'],
}
diccionario['segundo_nombre'] = ['German'] # => Al ser mutable se puede modificar agregandole claves y valores

print(diccionario)

print(diccionario['primer_nombre']) # => ´Para consultar el valor de una clave de un diccionario hacemos uso de la sintaxis: "print(diccionario[x])"

# TAMBIEN SE PUEDE MODIFICAR EL DICCIONARIO:
diccionario['primer_nombre'] = ['Camilo']
print(diccionario)


# Y PARA ELIMINAR ELEMENTOS DE NUESTRO DICCIONARIO USAREMOS LA PALABRA RESERVADA 'Del': "del diccionario['clave']"

del diccionario['segundo_nombre']
print(diccionario)


# LOS DICCIONARIOS PROVEEN 3 VISTAS, ES DECIR, EXTRACCION PARCIAL DE LOS DATOS DEL DICCIONARIO, SIRVE CUANDO SE ITERA

# VISTAS:

# keys: Llamar solamente a las llaves del diccionario
print(diccionario.keys())

# values: Llamar solamente al valor de cada una de las llaves existentes en el diccionario
print(diccionario.values())

# both: Llamar ambas cosas
print(diccionario.items())
