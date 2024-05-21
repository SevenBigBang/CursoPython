# SCOPE O ALCANCE: DETERMINA EN QUE PARTE DE NUESTRO CODIGO UNA VARIABLE PUEDE SER ALCANZADA O NO;
# EN PYTHON HAY 3 TIPOS DE VARIABLES: 1. Locales, 2. Enclosing, 3. Globales.

nombre = "Cristhian" # ==> VARIABLE CON SCOPE GLOBAL: YA QUE ESTA FUERA DE ALGUNA FUNCION

def llamar():
    print(f"Hola como estas {nombre}")

llamar()

# GLOBAL: Las variables con scope global van a ser cualquier variable creada fuera de una funcion: por ejemplo la variable (nombre = "Cristhian") en la linea 4
#         Estas variables locales pueden ser accedidas desde cualquier otra funcion y parte del codigo al ser Globales

def imprimir_nombre():
    global nombre # ==> DE ESTA FORMA SI CAMBIAMOS EL VALOR DE LA VARIABLE GLOBAL
    nombre = "Cortes" # ==> ESTA ASIGNACION JAMAS REMPLAZARA EL VALOR DE UNA VARIABLE GLOBAL
    print(f"Hola como estas {nombre}") # ==> SOLO CREARA UNA NUEVA VARIABLE EN LA FUNCION PARA ASIGNARLE EL VALOR REQUERIDO

imprimir_nombre()
print(f"El valor de mi variable global es {nombre}")

# PERO SI QUEREMOS TRABAJAR CON LA VARIABLE GLOBAL TENEMOS QUE HACER USO DE "global variable = 'x'"

llamar() # ==> CON ESTO CONFIRMAMOS QUE LA SENTENCIA DE LA LINEA "15", CAMBIO LA VARIABLE LOCAL




# LOCAL: SON VARIABLES QUE SE CREAN EN UNA FUNCION Y SE USAN EN ESA MISMA FUNCION UNICAMENTE NO TIENEN PROPOSITO DE SER USADAS FUERA DE LA FUNCION

def imprimir_letra():
    letra = "A" # ==> ESTO ES UNA VARIABLE LOCAL, YA QUE SE CREO EN UNA FUNCION
    print(f"La letra es {letra}")

imprimir_letra()
# print(letra) # ==> Esto nos genera un error ya que esta varible "letra = A", solo esta creada en la funcion "imprimir_letra()", 
# lo cual no nos dejara usarla por fuera de esta funcion




# ENCLOSING: (No es tan utilizada), 

def imprimir_numero():
    numero_local = 5
    edad_local = 20
    print(f"Tu numero es {numero_local}")
    def edad():
        nonlocal edad_local # ==> CON "nonlocal", PODEMOS HACER QUE LA VARIABLE LOCAL EN LA FUNCION "edad()", PARA QUE SOLO TOME COMO VARIABLE LOCAL A "edad_local = 20, DE LA FUNCION "imprimir_numero()"
        edad_local = 40
        print(f"Tu edad es {edad_local}")
    edad()

imprimir_numero()