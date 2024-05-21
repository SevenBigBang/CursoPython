# LAS VARIABLES SON CONTENEDORES PARA ALMACENAR DATOS EN PYTHON. 
# (A DIFERENCIA DE OTROS LENGUAJES NO NECESITAS DECLARAR EXPLICITAMENTE LAS VARIABLES).

# EN PYTHON NO EXISTE UN COMANDO PARA CREAR VARIABLES, UNA VARIABLE ES CREADA EN EL MOMENTO EN EL QUE TU LE ASIGNAS UN VALOR CON EL OPERADOR "="



# 1. VARIABLES:

x = 5
y = "Cristhian"
print(x) # => METODO "print()", SE USA PARA IMPRIMIR EN CONSOLA
print(y)

# AHORA VE A LA PARTE SUPERIOR DERECHA DE TU PANTALLA Y DALE CLICK AL ICONO DE PLAY (TRIANGULO MIRANDO HACIA LA DERECHA), SE TE ABRE UNA CONSOLA DE COMANDOS DONDE VERAS
# LA IMPRESION 



# 2. ¿COMO DEBE SER EL NOMBRE DE LAS VARIABLES?:

# Una variable puede tener un nombre corto (como x e y) o un nombre más descriptivo (edad, nombreDeCar, total_volume). 
# Reglas para variables de Python:

# El nombre de una variable debe comenzar con una letra o el carácter de subrayado
# El nombre de una variable no puede comenzar con un número
# Un nombre de variable solo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9 y _ )
# Los nombres de las variables distinguen entre mayúsculas y minúsculas (edad, edad y edad son tres variables diferentes)
# El nombre de una variable no puede ser ninguna de las palabras clave de Python.

# Nombres de variables legales:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar, my_var, _my_var, myVar, MYVAR, myvar2) # => AL IMPRIMIRLAS NO NOS SALE NINGUN ERROR :D


# Nombres de variables no válidos:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# DESDE YA VISUAL ESTUDIO NOS HACE SABER QUE ESTAN MAL :C





# 3. NOMBRES EN VARIABLES DE VARIAS PALABRAS:


# Los nombres de variables con más de una palabra pueden ser difíciles de leer.
# Hay varias técnicas que puedes utilizar para hacerlos más legibles:


# Camel Case: (Cada palabra, excepto la primera, comienza con una letra mayúscula)

myVariableName = "John"



# Snake Case: (Cada palabra está separada por un carácter de subrayado)

my_variable_name = "John"





# 4. ASIGNANDO VARIABLES:

# 4.1 Muchos valores para múltiples variables: (Python le permite asignar valores a múltiples variables en una línea)

x, y, z = "Naranja", "Banano", "Cereza"
print(x)
print(y)
print(z)


# 4.2 Un valor para varias variables: Y puede asignar el mismo valor a varias variables en una línea:

x = y = z = "Orange"
print(x)
print(y)
print(z)


# 4.3 Desempaquetar una colección: Si tiene una colección de valores en una lista, tupla, etc. Python le permite extraer los valores en variables. A esto se le llama desempaquetar.
#Descomprimir una lista:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)





# EJERCICIOS: BASANDOSE EN LO VISTO.

# 1. Cree una variable denominada x asígnele el valor Volvo

# 2. Cree una variable denominada x asígnele el valor 50

# 3. Muestre en la consola la suma de "5 + 10", utilizando dos variables: x e y

# 5. Cree una variable llamada z, asígnele x + y, y muestre el resultado.
