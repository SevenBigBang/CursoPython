# CONTINUE: ESTA SENTENCIA OMITE EL RESTO DE LOGICA 

# IMPRIMIR SOLO LOS PARES:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in lista: 
    if numero % 2 == 0:
        print(numero)

# CON CONTINUE:
for numero in lista: 
    if numero % 2 != 0:
        continue
    print(numero)