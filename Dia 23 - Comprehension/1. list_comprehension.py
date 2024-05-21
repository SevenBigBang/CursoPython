# COMPRENSION DE LISTAS: NO TE CONFUNDAS POR SU NOMBRE ESTO NO ES MAS QUE UNA FORMA DE ESCRIBIR LISTAS APARTIR DE OPERACIONES SOBRE LOS ELEMENTOS DE OTRAS LISTAS:

# EXPLICACION: La comprensión de listas es una forma elegante de crear listas en Python. Piensa en ello como una forma rápida y poderosa de crear listas a partir de otras listas, iterando sobre ellas.


# EN ESTOS DOS EJEMPLOS COMPAREMOS LA FORMA TRADICIONAL DE OPERAR CON LISTAS (BUCLE FOR) O LA FORMA MAS EFECTIVA (LIST COMPREHENSION)

lista = [1, 2, 3, 4, 5, 6]


# 1. NOS PIDEN QUE APARTIR DE LA LISTA POR CADA ELEMENTO CREEMOS UNA NUEVA LISTA CON LOS ELEMENTOS ELEVADOS AL CUADRADO, 1 al cuadrado, 2 al cuadrado, 3 al cuadrado, etc...

# USANDO UN BUCLE FOR:
cuadrados = []
for x in lista:
    cuadrados.append(x**2)

print(lista)
print(cuadrados)


print("\n\n")
# LIST COMPREHENSION:
elevados_a_la_2 = [x**2 for x in lista] # DE ESTA FORMA HACEMOS USO DEL LIST COMPREHENSION PRIMERO CREAMOS UNA VARIABLE A LA CUAL LE VAMOS ASIGNAR PRIMERO LA OPERACION Y DESPUES EL BUCLE FOR
print(lista)                                                                                                                        # variable_creada = [operacion for x in lista_variable]
print(elevados_a_la_2)

# COMO PODEMOS VER USANDO LA COMPRENSION DE LISTAS RESUMIMOS MUCHO MAS CODIGO Y LO DEJAMOS MAS ENTENDIBLE QUE USANDO UN SIMPLE FOR, ENTONCES EMPIEZA A USARLO :D

print("\n\n")

# 2. APLIQUE LOS CUADRADOS UNICAMENTE A LOS NUMEROS QUE SEAN PAR:

# BUCLE FOR:
cuadrados_solo_a_los_pares = []
for x in lista:
    if x % 2 == 0:
        cuadrados_solo_a_los_pares.append(x**2)
print(cuadrados_solo_a_los_pares)



print("\n\n")
# LIST COMPREHENSION:
cuadrados_solo_a_los_pares = [x**2 for x in lista if x % 2 == 0] # LO SE ES MUY CONFUNSO; PRIMERO LA OPERACION A REALIZAR, DESPUES EL CICLO FOR Y DESPUES UN CONDICIONAL
print(cuadrados_solo_a_los_pares)                                 # ALGO ASI: variable_creada = [operacion for in x in lista_variable if x condicion]

# SE QUE ES COMPLEJO PERO SE QUE PUEDES HACERLO >:D




# AHORA SI VEAMOS EL ULTIMO NIVEL, LOS LIST COMPREHENSION ANIDADOS :?


# CREA UNA MATRIZ DE ELEMENTOS:


# BUCLE FOR:
matriz = []
for _ in range(3):
    lista_interna = []
    for i in range(1, 4):
        lista_interna.append(i)
    matriz.append(lista_interna)
print(matriz)



# USANDO FOR ANIDADOS CON LIST COMPREHENSION:

matriz = [[i for i in range(1, 4)]for _ in range(3)] # TE TRATARE DE EXPLICAR DE UNA FORMA DIFERENTE ESTA VEZ JAJA, EMPEZAMOS COMO SIEMPRE DECLARANDO UNA VARIABLE EN FORMA DE LISTA, DESPUES
#                                                      EN LA PARTE DERECHA PONEMOS EL FOR MAS EXTERNO, DEPUES DEFINIMOS LAS OPERACIONES REALIZADAS A CADA UNA DE ESAS ITERACIONES; EN ESTE CASO
#                                                      NO VAMOS A TRABAJAR CON LA LISTA ORIGINAL LA DE NUMEROS, SINO QUE VAMOS A TRABAJAR CON LOS ELEMENENTOS QUE SE HAYAN DEFINIDO EN EL FOR MAS
#                                                      EXTERNO, (EN ESTE CASO USAMOS UN "range(3)", ES POR ESO QUE TENEMOS UNA VARIABLE TEMP _), CONTINUEMOS COMO ES UN LIST ANIDADO, TENEMOS
#                                                      QUE CREAR OTRA LISTA [], EN LA CUAL PONEMOS EL CICLO FOR INTERNO A LA DERECHA Y LAS OPERACIONES A LA IZQUIERDA. (LA OPERACION A REALIZAR
#                                                      EN ESTE CASO ES "i", ya que usamos el metodo ".append(i)") ESPERO QUE HAYA QUEDADO TOD CLARO :)

#                 DE ESTA FORMA: variable_lista_anidada = [[operacion for i in iterable] for x in iterable] => NO ES TAN COMPLEJO SI LO MIRAS DE ESTA FORMA :D  ♦♣♥♠                         
print(matriz)





# Y COMO SIEMPRE USANDO LIST COMPREHENSION PODREMOS SIMPLIFICAR EL USO DE LISTAS Y OPERACION DE LISTAS MUCHOOOOOOOOOOOO; ESPERO LAS PRACTIQUES Y TE VUELVAS CRACK CON ELLAS PORQUE SON MUY IMPORTANES






# EJERCICIOS: USANDO LIST COMPREHENSION REALIZAR
# 1. Lista de números pares del 0 al 10:

# 2. Lista de cuadrados de los números del 1 al 10:

# 3. Lista de palabras que empiezan con una vocal en una lista de palabras: