# Strings (str) o Cadenas de texto: Las cadenas en python están rodeadas por comillas simples o dobles.

# "hola" es lo mismo que 'hola'.

# Puede mostrar un literal de cadena con la función: print(x) # X o x = Variable
print("Hello")
print('Hello')
# LA IMPRESION ES LA MISMA SIN IMPORTAR QUE COMILLAS ELIJAS :D




# 1. COMILLAS dentro de COMILLAS ("''"): Puede usar comillas dentro de una cadena, siempre y cuando no coincidan con las comillas que rodean la cadena

# Ejemplo
print("Esto esta 'bien'")
print('A él le dicen "El loco".')





# 2. ASIGNAR CADENA A UNA VARIABLE: La asignación de una cadena a una variable se realiza con el nombre de la variable seguido de un signo igual y la cadena

a = "Hola"
print(a)







# 3. CADENA MULTILINEA: Puede asignar una cadena de varias líneas a una variable mediante tres comillas.

# Ejemplo: Puedes usar tres comillas dobles o tres comillas simples:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)






# 4. LAS CADENAS SON ARRAYS (ARRAY: Un array, es un tipo de dato estructurado que permite almacenar un conjunto de datos homogeneo, es decir, todos ellos del mismo tipo y relacionados.)

# Al igual que muchos otros lenguajes de programación populares, las cadenas en Python son matrices/array's de bytes que representan caracteres Unicode.
# Sin embargo, Python no tiene un tipo de datos de carácter, un solo carácter es simplemente una cadena con una longitud de 1.
# Los corchetes se pueden utilizar para acceder a los elementos de la cadena.

# Ejemplo: Consigue el carácter en la posición 1 (recuerda que el primer carácter tiene el atributo posición 0):

a = "Hello, World!"
print(a[1])


# Bucle a través de una cadena: Dado que las cadenas son matrices, podemos recorrer los caracteres de una cadena, con un bucle. for

for x in "banana":
    print(x)






# 5. Longitud de la cadena: Para obtener la longitud de una cadena, use la función. len()

# Ejemplo: La función devuelve la longitud de una cadena: len()

a = "Hello, World!" # => Cuenta cada uno de los caracteres que estan en el array (incluyendo espacios) y notaras que son 13
print(len(a))






# 6. Cadena de comprobación: Para comprobar si una determinada frase o carácter está presente en una cadena, podemos usar La palabra clave . in


# Ejemplo: Compruebe si "gratis" está presente en el siguiente texto:

txt = "Las mejores cosas en la vida son gratis!"
print("gratis" in txt) # ==> SE IMPRIMIRA TRUE YA QUE GRATIS SI ESTA PRESENTE DE LO CONTRARIO SE IMPRIMIRIA FALSE

# Úsalo en una declaración: if
# Ejemplo: Imprima solo si "gratis" está presente:

txt1 = "Las mejores cosas en la vida son gratiss!" # EN ESTE CASO COMO NO ESTA PRESENTE "gratis", sino "gratiss", no imprimira nada :)
if "gratis" in txt1:
  print("Si, 'gratis' esta presente.")


# Marque si NO es: Para comprobar si una determinada frase o carácter NO está presente en una cadena, podemos usar La palabra clave . "not in"

# Ejemplo: Compruebe si "caro" NO está presente en el siguiente texto:

txt2 = "Las mejores cosas en la vida son gratis!"
print("caro" not in txt2) # ==> Devolvera "True" Ya que caro no se encuentra en el txt2
