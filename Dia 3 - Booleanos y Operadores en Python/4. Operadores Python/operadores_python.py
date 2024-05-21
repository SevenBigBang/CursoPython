# Operadores de Python: Los operadores se utilizan para realizar operaciones en variables y valores.

# En el siguiente ejemplo, usamos el operador + para sumar dos valores: 
print(10 + 5)


# Python divide los operadores en los siguientes grupos:

# Operadores aritméticos
# Operadores de asignación
# Operadores de comparación
# Operadores lógicos
# Operadores de identidad
# Operadores de membresía
# Operadores bit a bit







# 1. Operadores aritméticos de Python: Los operadores aritméticos se utilizan con valores numéricos para realizar operaciones matemáticas comunes

# Operador          Nombre              Ejemplo

#   +               Suma                 x + y	
#   -               Resta                x - y	
#   *               Multiplicación       x * y	
#   /               División             x / y	
#   %               Módulo               x % y	    ==> Sirve para saber el resto de una division, util cuando quieres saber si una operacion tiene como resultado un por o impar
#   **              Exponenciación       x ** y	    ==> Usalo cuando quieras elevar un numero
#   //              División Exacta      x // y     ==> Usala cuando quieras una division redondeada






# 2. Operadores de asignación de Python: Los operadores de asignación se utilizan para asignar valores a las variables

# Operador      Ejemplo(RECOMENDADO)        Es igual a

#   =           x = 5 I                     x = 5 x = 5	
#   +=          x += 3                      x = x + 3	
#   -=          x -= 3                      x = x - 3	
#   *=          x *= 3                      x = x * 3	
#   /=          x /= 3                      x = x / 3	
#   %=          x %= 3                      x = x % 3	
#   //=         x //= 3                     x = x // 3	
#   **=         x **= 3                     x = x ** 3	
#   &= x        &= 3                        x = x & 3	
#   |= x        |= 3                        x = x | 3	
#   ^= x        ^= 3                        x = x ^ 3	
#   >>= x       >>= 3                       x = x >> 3	
#   <<= x       <<= 3                       x = x << 3	
#   :=          print(x := 3)               x = 3
#                                           print(x)






# 3. Operadores de comparación de Python: Los operadores de comparación se utilizan para comparar dos valores

# Operador      Nombre                  Ejemplo

#   ==          Igual                   x == y	
#   !=          No igual                x != y	
#   >           Mayor que               x > y	
#   <           Menor que               x < y	
#   >=          Mayor o igual que       x >= y	
#   <=          Menor o igual que       x <= y





# 4. Operadores lógicos de Python: Los operadores lógicos se utilizan para combinar instrucciones condicionales

# Operador          Descripción                                                                     Ejemplo

#   and             Devuelve Verdadero si ambas afirmaciones son verdaderas                         x < 5 y x < 10
#   or              Devuelve True si una de las afirmaciones es cierta                              x < 5 o x < 4
#   not             Invierte el resultado, devuelve Falso si el resultado es verdadero              not(x < 5 y x < 10)




# 5. Operadores de identidad de Python: Los operadores de identidad se utilizan para comparar los objetos, no si son iguales, sino si en realidad son el mismo objeto, con la misma ubicación de memoria

# Operador          Descripción                                                         Ejemplo

#   is              Devuelve Verdadero si ambas variables son el mismo objeto           x is y	
#   is not          Devuelve True si ambas variables no son el mismo objeto             x is not y






# 6. Operadores de pertenencia a Python: Los operadores de pertenencia se utilizan para probar si se presenta una secuencia en un objeto

# Operador          Descripción                                                                                     Ejemplo

#   in              Devuelve True si una secuencia con el valor especificado está presente en el objeto             x in y	
#   not in          Devuelve True si una secuencia con el valor especificado no está presente en el objeto          x not in y





# 7. Operadores bit a bit de Python: Los operadores bit a bit se utilizan para comparar números (binarios)

# Operador        Nombre                        Descripción                                                                                                             Ejemplo

#   &              AND                          Pone cada bit a 1 si ambos bits son 1                                                                                   x & y	
#   |              OR                           Pone cada bit a 1 si uno de los dos bits es 1                                                                           x | y	
#   ^              XOR                          Pone cada bit a 1 si sólo uno de los dos bits es 1                                                                      x ^ y	
#   ~              NOT                          Invierte todos los bits                                                                                                 ~x	
#   <<             Zero fill left shift         Desplazamiento a la izquierda empujando ceros desde la derecha y dejando caer los bits más a la izquierda               x << 2	
#   >>             Signed right shift           Cambio a la derecha con signo Cambia a la derecha empujando copias del bit más a la izquierda desde la izquierda,       x >> 2
#                                               y deja que los bits más a la derecha caigan