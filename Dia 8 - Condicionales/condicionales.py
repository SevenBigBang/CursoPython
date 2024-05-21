# CONDICIONALES: DE ACUERDO CON UNA CONDICION SE DETERMINA QUE PORCION DE CODIGO SE EJECUTA O NO

edad = 28
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# if else encadenado:
edad = int(input("Cual es tu edad?: "))
if edad >= 0 and edad <= 12:
    print("Usted es un niño tonto")
elif edad >= 13 and edad <= 17:
    print("Usted es un adolescente bobo")
elif edad >= 18 and edad <= 59:
    print("Usted es un adulto")
else:
    print("Usted es un tonoto")

# CONDICIONALES AVANZADOS:

#Ejercicio 1:

#if anidado:

edad = int(input("¿Cual es tu edad?: "))  
altura = int(input("¿Cual es tu altura?: "))  

if edad >= 18:
    if altura >= 170 or edad >= 25 and altura >= 165:
        print("Puedes participar en el equipo de basquet")
    else:
        print("No cumples con los requisitos necesarios.")
else:
    print("Debes ser mayor de edad para ingresar al equipo")


# Operador ternario: Permite crear condicionales en una sola linea de codigo

edad = int(input("Por favor ingrese su edad: "))
mensaje = "Usted es mayor de edad" if edad >= 18 else "Usted es menor de edad"
print(mensaje)