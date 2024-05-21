# TALLER PRACTICO EN DONDE PRACTICAREMOS LOS TEMAS VISTOS, Dictionary unpacking, iterable unpacking, *args y **kwargs

# EJEMPLO PRACTICO: HACER UNA FUNCION QUE VA A CALCULAR EL PRECIO TOTAL CON LISTA DE PRODUCTOS VARIABLE, CALCULAR UN DESCUENTO(SI APLICA), Y UN IMPUESTO.
def calcular_precio_total(*args, **kwargs): # ==> ACA ESTABLECEMOS QUE VAMOS A TRABAJAR CON DOS PARAMETROS VARIABLES EN TUPLA Y DICCIONARIO RESPECTIVAMENTE.
    precio_total = sum(args) # ==> USAREMOS EL PRIMER PARAMETRO (*args), PARA CALCULAR LA SUMA TOTAL DE LOS PRODUCTOS QUE NOS PASEN Y PARA ESO NOS SERVIRIA NUESTRA TUPLA
    descuento = kwargs.get('descuento', 0) # ==> USAMOS EL PARAMETRO (**kwargs), PARA GESTIONAR EL DESCUENTO E IMPUESTO YA QUE SON PARAMETROS OPCIONALES QUE PUEDEN ESTAR O NO
    impuesto = kwargs.get('impuesto', 0)   #     AL SER UN DICCIONARIO NOS FACILITA ESTA TAREA YA QUE USA; Llave y Valor

    # CALCULOS
    precio_total -= precio_total * descuento
    precio_total += precio_total * impuesto

    # DEVOLVER EL RESULTADO: (CON RETURN PARA PODER USARLO MAS ADELANTE)

    return precio_total
                                #                 
precio_final = calcular_precio_total(200, 50, 30, 10, descuento = 0.2, impuesto= 0.01) # ==> PRIMERO CREAMOS UNA VARIABLE EN LA CUAL PODAMOS GUARDAR EL RETORNO DE NUESTRA FUNCION
print(precio_final)                                                                    # DESPUES ASIGNAREMOS LOS PRECIOS A NUESTRA TUPLA, SE DIFERENCIA YA QUE SON DEL MISMO TIPO
                                                                                       # (INT), ADEMAS DE QUE NO TIENEN LLAVE Y PARA ASIGNARLE VALORES AL PARAMETRO **kwargs,
                                                                                       # USAREMOS PRIMERO LLAVE Y DESPUES VALOR, EN ESTE CASO (descuento = 0.2, impuesto = 0.01)
                                                                                       # Y ASI DIFERENCIAMOS CUANDO ASIGNAMOS VALORES A UN PARAMETRO U OTRO 
                    
                

# AHORA VAMOS A USAR UN DESEMPAQUETADO DE ITERABLES, PARA HACERLA MAS DINAMICA (Iterable unpacking y Dictionary unpacking):
lista_productos = [200, 50, 30, 10]
dict_desc_impuest = {
    'descuento' : 0.2,  # ==> RECORDEMOS QUE ESTOS ARGUMENTOS LOS DEJAMOS COMO OPCIONALES GRACIAS A ".get('nombre_llave), valor_llave", EN ESTE CASO QUITAREMOS EL IMPUESTO
    
}
precio_final = calcular_precio_total(*lista_productos, **dict_desc_impuest) # ==> SE OBSERVA QUE TRABAJANDO EL DESEMPAQUETAMIENTO DE ITERABLES Y DICCIONARIOS 
print(precio_final)                                                         #     ES MAS LEGIBLE EN TODO ASPECTO, SE USA UN ASTERISCO(*nombre_lista), PARA DESEMPAQUETAR,
                                                                            #     UNA LISTA O UNA TUPLA
                                                                            #     Y SE USA DOBLE ASTERISCO(**nombre_diccionario), PARA DESEMPAQUETAR UN DICCIONARIO
