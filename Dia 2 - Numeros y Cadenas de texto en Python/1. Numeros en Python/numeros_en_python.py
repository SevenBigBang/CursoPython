# Python Numbers 

# Hay tres tipos numéricos en Python:
# 1. int
# 2. float
# 3. complex

# Las variables de tipos numéricos se crean cuando se les asigna un valor:
x = 1    # int
y = 2.8  # float
z = 1j   # complex


# Para verificar el tipo de cualquier objeto en Python, use la función: type()
print(type(x))
print(type(y))
print(type(z))




# 1. Int: Int, o entero, es un número entero, positivo o negativo, sin decimales, de longitud ilimitada.
# Enteros:
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


# 2. Float: Float, o "número de coma flotante" es un número, positivo o negativo, que contiene uno o más decimales.
# Flotadores:
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


# 3. Complejo: Los números complejos se escriben con una "j" como parte imaginaria
#Complejo:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))




# 4. Conversión de tipos: Puede convertir de un tipo a otro con los métodos  :int(), float() y complex()
# Convertir de un tipo a otro:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Nota: No se pueden convertir números complejos en otro tipo de número.


# EXTRA POR SEVEN :D Número aleatorio: Python no tiene una función para hacer un número aleatorio, pero Python tiene 
#                                      un módulo incorporado llamado "random" que se puede usar para hacer números aleatorios: random()

# Ejemplo
# Importe el módulo aleatorio y muestre un número aleatorio entre 1 y 9:
import random

print(random.randrange(1, 10))




# EJERCICIOS :P 

# 1. Inserte la sintaxis correcta para convertir x en un número de coma flotante.
x = 5
x = ...(x) # ==> TU CODIGO VA EN LOS 3 PUNTOS REMPLAZALO :D


# 2. Inserte la sintaxis correcta para convertir x en un número entero.
x = 5.5
x = ...(x)


# 3. Inserte la sintaxis correcta para convertir x en un número complejo.
x = 5
x = ...(x)
