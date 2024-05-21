# Booleanos de Python: Los valores booleanos representan uno de estos dos valores: True o False

# Valores booleanos: En programación, a menudo es necesario saber si una expresión es True o False
# Puede evaluar cualquier expresión en Python y obtener una de las dos respuestas, Trueo False
# Al comparar dos valores, se evalúa la expresión y Python devuelve la respuesta booleana:

print(10 > 9)  # ==> Diez es mayor a 9?: True
print(10 == 9) # ==> Diez es igual a 9?: False
print(10 < 9)  # ==> Diez es menor a 9?: False 





# Cuando se ejecuta una condición en una instrucción if, Python devuelve: True o False
# Ejemplo: Imprima un mensaje en función de si la condición es: True o False
a = 200
b = 33

if b > a:
  print("b es mas grande que a")
else:
  print("b no es mas grande que a")





# 1. Evaluar valores y variables: La función le permite evaluar cualquier valor, y le dan o a cambio,bool()TrueFalse

# Ejemplo: Evalúe dos variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))






# 2. La mayoría de los valores son verdaderos:

# Casi cualquier valor se evalúa True si es tiene algún tipo de contenido.
# Cualquier cadena es True, excepto las cadenas vacías.
# Cualquier número es True, excepto 0. 
# Cualquier lista, tupla, conjunto y diccionario son True, excepto vacíos. 

# Ejemplo: Lo siguiente devolverá True

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])





# 3. Algunos valores son falsos: De hecho, no hay muchos valores que se evalúen como , excepto los valores vacíos, como , , , , el número y el valor . Y, por supuesto, el valor se evalúa como .False()[]{}""0NoneFalseFalse

# Ejemplo: Lo siguiente devolverá False

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})