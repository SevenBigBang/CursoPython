# LINEA DE HERENCIA: HACE REFERENCIA A LA POSIBILIDAD DE QUE MI CLASE PADRE A SU VEZ SEA CLASE HIJA DE OTRA CLASE, EN PALABRAS MAS ACERTADAS, ES COMO TENER UN PADRE, UN ABUELO
#                    UN BISABUELO, ETC...

# EN TODOS NUESTRAS CLASES CREADAS HEMOS PASADO POR UNA CLASE PADRE Y MULTIPLES CLASES HIJAS, PERO AHORA, SI PENSAMOS EN UNA LINEA DE HERENCIA Y LO LLEVAMOS AL MUNDO 
# POKEMON COMO LO HEMOS ESTADO HACIENDO ENTONCES NOS DAMOS CUENTA QUE LOS POKEMONES CUENTAN CON UN PATRON DE ATRIBUTOS EN BASE A SU TIPO, EJEMPLO:
# LOS POKEMON TIPO ELECTRICO, SIEMPRE VAN A CONTAR CON UN VOLTAJE MAXIMO, UN NIVEL DE ENERGIA, ETC..., OTRO EJEMPLO SERIAN LOS POKEMON DE TIPO FUEGO LOS CUALES 
# CONTARIAN CON SU TEMPERATURA MAXIMA POR EJEMPLO, ESAS CARACTERISTICAS PROPIAS DE UN TIPO, LAS PODEMOS ALCANZAR SI CREAMOS UNA CLASE INTERMEDIA ENTRE POKEMON Y PIKACHU,
# ESPERO ENTIENDAS A LO QUE ME REFIERO:
#
#                              ____________________________ CLASE PADRE(Pokemon)____________________________ 
#                             |                                                                            |      
#               CLASE HIJA(TIPO - ELECTRICO)                                                    CLASE HIJA(TIPO FUEGO)
#                            |                                                                            |
#       CLASE HIJA(PIKACHU) - CLASE HIJA(JOLTEON)                                 CLASE HIJA(CHARMANDER) - CLASE HIJA(TORCHIC)




#
# DE ESTA FORMA ES MAS ENTENDIBLE ENTONCES VAMOS A CREAR UN ARCHIVO.PY PARA CREAR LA CLASE DE PADRE/HIJA (tipo_electrico.py) PARA QUE ENTIENDAS COMO FUNCIONARIAN 
# EN CONJUNTO Y COMO PODER SEGUIR AGREGANDO MAS CLASES PADRE/HIJAS, COMO CUANDO UN POKEMON ES ELECTRICO-VOLADOR.