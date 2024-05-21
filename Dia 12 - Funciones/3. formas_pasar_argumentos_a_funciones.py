def imprimir_nombre(primer_nombre,
                    segundo_nombre,
                    primer_apellido,
                    segundo_apellido):
    print(f"Hola {primer_nombre} {segundo_nombre} "\
          f"{primer_apellido} {segundo_apellido}, "\
            "bienvenido al curso de Python")




# 1. POSITION ARGUMENTS: PASAR ARGUMENTOS EN EL ORDEN EN EL QUE FUERON ESTABLECIDOS (EL METODO MAS COMUN, HAY 3 FORMAS MAS):
imprimir_nombre("Cristhian", "German", "Cortes", "Ariza") # ==> IMPORTA MUCHO EL ORDEN EN EL QUE ESTABLECES SUS ARGUMENTOS


# 2. KEYWORD ARGUMENTS: CON ESTE METODO DE POSICIONAMIENTO VAMOS A PODER PASAR VALORES EN DIFERENTE ORDEN SIEMPRE Y CUANDO DEFINIENDO SU RESPECTIVA CLAVE:
imprimir_nombre(primer_apellido="Cortes", primer_nombre="Cristhian", segundo_apellido="Ariza", segundo_nombre="German") # ==> De esta forma podemos sin importar 
                                                                                                                        #     el orden asignar correctamente los valores


# 3. ITERABLE UNPACKING: (DESEMPAQUETADO DE ITERABLES), (ITERABLES = CUALQUIER ESTRUCTURA DE DATOS QUE ES CAPAZ DE DEVOLVER SUS DATOS 1 A 1, Listas, Tuplas etc..)
estudiantes = ("Cristhian", "German", "Cortes", "Ariza")
imprimir_nombre(*estudiantes) # ==> HACIENDO "23 nombre_funcion(*nombre_iterable)", ES MUY IMPORTANTE EL ASTERISCO(*), EN ESTA FORMA YA QUE ES COMO SE DA A ENTENDER QUE
                              #     QUEREMOS DESEMPAQUETAR EL ITERABLE
                              # IMPORTANTE(Los elementos del iterable deben estar en el orden correcto, es decir, concidir con los parametros de la funcion declarada,
                              #            En este caso, primer nombre, segundo nombre, primer apellido, segundo apellido)


# 4. DICTIONARY UNPACKING: FUNCIONA DE MANERA SIMILAR AL "Iterable Unpacking", SOLO QUE CON UN DICCIONARIO
estudiante_dict = {
    'primer_nombre' : 'Cristhian',
    'primer_apellido' : 'Cortes',
    'segundo_nombre' : 'German',
    'segundo_apellido' : 'Ariza'
}
imprimir_nombre(**estudiante_dict) # ==> EN ESTE CASO SE USA EL DOBLE ASTERISCO(**), AL IGUAL QUE EN EL ITERABLE UNPACKING, PERO ESTA VEZ CON DOBLE ASTERISCO DE ESTA FORMA:
                                   #     "38 nombre_funcion(**nombre_diccionario)", DE ESTA FORMA DESEMPAQUETAMOS UN DICCIONARIO


