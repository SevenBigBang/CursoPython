# FOOR LOOP: Se utiliza para iterar sobre un iterable (Una lista, una tupla, un set, cualquier objeto que es capaz de retornar sus elementos uno a uno.)

lista_nombre = ['Cristhian', 'Cortes', 'Ariza']
tupla_notas = ('Cristhian', 30, 4.5)
set_departamentos = {'ventas', 'compras', 'redes', 'it'}

for nombre in lista_nombre: # Se crea una variable temp para iterar cada elemento de en este caso la lista de nombres "for x in x:"
    print(nombre)
for nota in tupla_notas:
    print(nota)
for dept in set_departamentos:
    print(dept)


# FOOR LOOP - RANGE: Nuevo uso - Se usa para realizar acciones de manera repetitiva 
lista = [0, 1, 2, 3]
for iter in lista:
    print("Desde origen avanzar 10 pasos")
    print("Girar 90 grados") # ===> ESTE EJEMPLO ESTA BIEN PERO SE PUEDE MEJORAR COMO SE VE ABAJO, (ENTRE MENOS VARIABLES MEJOR)



for _ in range(4):                            # SE CREA UN RANGO DE 4 ELEMENTOS, Y SE USA _ CUANDO EL ITERABLE NO SE USA
    print("Desde origen avanzar 10 pasos")
    print("Girar 90 grados")



# FOOR LOOP - ENUMERATE: Se usa para retornar una tupla
# EXTRAR EL INDICE Y EL VALOR:

# PRIMERA FORMA:

lista_nombres = ["Cristhian", "Cortes", "Ariza"]
for indice in range(3):
    print(indice, lista_nombres[indice])



# FORMA MAS OPTIMA:

for indice, valor in enumerate(lista_nombres):    # ====> "enumerate(x)": Por cada iteracion retorna una tupla
    print(indice, valor)