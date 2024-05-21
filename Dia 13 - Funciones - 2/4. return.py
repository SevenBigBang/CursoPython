# RETURN: SE UTILIZA DENTRO DE LAS FUNCIONES,

def sumar(n1, n2):
    resultado = n1 + n2
    print(f"La suma entre {n1} y {n2} es: {resultado}")

resultado = sumar(3, 3)
print(f"El resultado es {resultado}") # ==> ESTE ES EL CASO DEVUELVE NONE AL NO TENER UN RETORNO EN LA FUNCION

# EN PYTHON, LAS FUNCIONES QUE NO TIENEN UNA DECLARACION EXPLICITA DE RETORNO O AQUELLAS QUE TERMINAN SIN UNA INSTRUCCION DE RETURN AUTOMATICAMENTE DEVUELVEN
# 'None' POR DEFECTO.




# DE ESTA FORMA PODEMOS CORREGIR ESTO:

def sumar1(n1, n2):
    resultado = n1 + n2
    return resultado    # ==> DE ESTA MANERA SENCILLA PODEMOS ALMACENAR VALORES EN VARIABLES PARA QUE PODAMOS OPERAR CON ELLAS
resultado = sumar1(3, 3)
print(f"El resultado es: {resultado}")







# MULTIPLE RETURN: EN LA MAYORIA DE LENGUAJES ESTO NO ES POSIBLE, LAS FUNCIONES ESTAN DISEÑAS PARA DEVOLVER SOLO UN VALOR, ESTO EN PYTHON SI ES POSIBLE!:

def calcular_precio(nombre_producto, cantidad, precio_u, descuento=0):
    precio_final = (cantidad * precio_u) * (1-descuento)
    return nombre_producto, cantidad, precio_final # ==> EN ESTE CASO AL RETORNAR MULTIPLES VARIABLES LAS RETORNA COMO UNA TUPLA "tupla_principal = (x, y, z, ...)"
compra_final = calcular_precio('Medias', 3, 7000)  #     CON ESTAS TUPLAS PODEMOS HACER MULTIPLES COSAS COMO DESEMPAQUETARLAS, ITERARLAS ETC...
print(compra_final)

