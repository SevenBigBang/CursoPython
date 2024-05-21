# Modificar cadenas: Python tiene un conjunto de métodos integrados que puede usar en cadenas.



# 1. Mayúscula

# Ejemplo: El método devuelve la cadena en mayúsculas: upper()

a = "Hello, World!"
print(a.upper()) # ==> El metodo "upper(x), convierte la cadena dada a mayusculas "HELLO, WORLD!""




# 2. Minúsculas

# Ejemplo: El método devuelve la cadena en minúsculas:lower()

a = "Hello, World!"
print(a.lower())




# 3. Eliminar espacios en blanco: El espacio en blanco es el espacio antes y/o después del texto real, y muy a menudo desea eliminar este espacio.

# Ejemplo: El método elimina cualquier espacio en blanco del principio o del final:strip()

a = " Hello, World! "
print(a.strip()) # retornara "hello, world" (ELIMINA LOS ESPACIOS INNCESARIOS AL PRINCIPIO Y AL FINAL DE LA CADENA)




# 4. Cadena dividida: El método devuelve una lista en la que el texto entre el separador especificado se convierte en los elementos de la lista. split()

# Ejemplo: El método divide la cadena en subcadenas si encuentra instancias del separador:split()

a = "Hello, World!"
print(a.split("--")) # retornara ['Hello', 'World!'']



# NOTA POR SEVEN: ACA TE DEJO TODOS LOS METODOS EXISTENTES PARA LAS CADENAS DE TEXTO <:=)

#   METODO	                                DESCRIPCION

# capitalize()                  Convierte el primer carácter a mayúsculas
# casefold()                    Convierte la cadena a minúsculas
# center()                      Devuelve una cadena centrada
# count()                       Devuelve el número de veces que un valor especificado aparece en una cadena
# encode()                      Devuelve una versión codificada de la cadena
# endswith()                    Devuelve true si la cadena termina con el valor especificado
# expandtabs()                  Establece el tamaño de tabulación de la cadena
# find()                        Busca en la cadena un valor especificado y devuelve la posición donde se encontró
# format()                      Formatea los valores especificados en una cadena
# format_map()                  Formatea los valores especificados en una cadena
# index()                       Busca en la cadena un valor especificado y devuelve la posición donde se encontró
# isalnum()                     Devuelve True si todos los caracteres de la cadena son alfanuméricos
# isalpha()                     Devuelve True si todos los caracteres de la cadena son alfanuméricos
# isascii()                     Devuelve True si todos los caracteres de la cadena son ascii
# isdecimal()                   Devuelve True si todos los caracteres de la cadena son decimales
# isdigit()                     Devuelve True si todos los caracteres de la cadena son dígitos
# isidentifier()                Devuelve True si la cadena es un identificador
# islower()                     Devuelve True si todos los caracteres de la cadena están en minúsculas
# isnumeric()                   Devuelve True si todos los caracteres de la cadena son numéricos
# isprintable()                 Devuelve True si todos los caracteres de la cadena son imprimibles
# isspace()                     Devuelve True si todos los caracteres de la cadena son espacios en blanco
# istitle()                     Devuelve True si la cadena sigue las reglas de un título
# isupper()                     Devuelve True si todos los caracteres de la cadena son mayúsculas
# join()                        Une los elementos de un iterable al final de la cadena
# ljust()                       Devuelve una versión de la cadena justificada a la izquierda
# lower()                       Convierte una cadena a minúsculas
# lstrip()                      Devuelve una versión recortada a la izquierda de la cadena
# maketrans()                   Devuelve una tabla de traducción que se utilizará en las traducciones
# partition()                   Devuelve una tupla en la que la cadena se divide en tres partes
# replace()                     Devuelve una cadena en la que un valor especificado se sustituye por otro valor especificado
# rfind()                       Busca en la cadena un valor especificado y devuelve la última posición donde se encontró
# rindex()                      Busca en la cadena un valor especificado y devuelve la última posición en la que se encontró.
# rjust()                       Devuelve una versión justificada a la derecha de la cadena
# rpartition()                  Devuelve una tupla con la cadena dividida en tres partes
# rsplit()                      Divide la cadena en el separador especificado y devuelve una lista
# rstrip()                      Devuelve una versión recortada a la derecha de la cadena
# split()                       Divide la cadena en el separador especificado y devuelve una lista
# splitlines()                  Divide la cadena en los saltos de línea y devuelve una lista
# startswith()                  Devuelve true si la cadena empieza por el valor especificado
# strip()                       Devuelve una versión recortada de la cadena
# swapcase()                    Intercambia mayúsculas y minúsculas y viceversa
# title()                       Convierte el primer carácter de cada palabra en mayúsculas
# translate()                   Devuelve una cadena traducida
# upper()                       Convierte una cadena a mayúsculas
# zfill()                       Rellena la cadena con un número especificado de valores 0 al principio
