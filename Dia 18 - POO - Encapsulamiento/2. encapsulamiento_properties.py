# ENCAPSULAMIENTO - PROPIEDADES: SIMILARES A LOS GETTERS Y SETTERS DE JAVA, LAS PROPIEDADES EN PYTHON TIENEN EL MISMO FUNCIONAMIENTO

class Bulbasour:

    __tipo = 'Planta'

    def __init__(self, nombre, nivel, salud, color):
        self.__nombre = nombre
        self.nivel = nivel
        self.salud = salud
        self.__color = color
    
    def atacar(self):
        print(f"Bulbasour ataca y genera ¡{self.nivel/4}! de daño.")


bulbasour_1 = Bulbasour("Cactus", 5000, 2500, 'verde')
print(f"El Bulbasour de nombre {bulbasour_1.__nombre}, de nivel {bulbasour_1.nivel} y de tipo {bulbasour_1.__tipo}") # => ACA HAY UN PROBLEMA SI BIEN HICIMOS PRIVADAS ALGUNAS 
                                                                                                                     #    VARIABLES DE INSTANCIA, AHORA NO LAS PODEMOS NI MOSTRAR



# AHORA VEREMOS DOS FORMAS DE SIMULAR ESOS GETTERS Y SETTERS EN PYTHON PARA QUE NO OCURRAN ESTOS ERRORES:


# FORMA 1:

class Bulbasour:

    __tipo = 'Planta'
    def get_tipo(self):  # => ACA DEFINIMOS UN GET PARA PODER MOSTRAR SU TIPO SIN PROBLEMA ALGUNO
        return self.__tipo # => ACA RETORNAMOS EL TIPO 

    def __init__(self, nombre, nivel, salud, color):
        self.__nombre = nombre
        self.nivel = nivel
        self.salud = salud
        self.__color = color
    
    # CREANDO UN GETTER (Obtener/Mostrar/Ver...) EN PYTHON:
    def get_nombre(self): # => Se usa la palabra reservada "def" y seguido por convencion "get_nombreDeLaInstancia(self):"
        return self.__nombre # => Aca retornamos el valor que queremos poder ver en este caso el nombre      

    # CREANDO UN SETTER (Establecer/Ingresar/Modificar...) EN PYTHON:
    def set_nombre(self, nombre): # => EN ESTE CASO AL QUERER TENER UN METODO PARA ESTABLECERLE UN NUEVO VALOR A NUESTRA VARIABLE DE INSTANCIA PRIVADA, NECESITAMOS UN RECIBIR UN PARAMETRO 
        self.__nombre = nombre
        if nombre == str:           # => CON ESTE CONDICIONAL ESTABLECEMOS QUE EL NOMBRE SOLO PUEDE CONTENER LETRAS (STRINGS) Y NO NUMEROS
            self.__nombre = nombre  # => SI ES IGUAL A UN STRING GUARDAMOS EN LA VARIABLE PRIVADA
        else:
            print("El nombre no permite numeros o caracteres especiales") # => DE LO CONTRARIO IMPRIME MENSAJE DE ADVERTENCIA

    # METODO/ACCION
    def atacar(self):
        print(f"Bulbasour ataca y genera ¡{self.nivel/4}! de daño.")


# USANDO LOS GET Y SET:

# CREACION DEL OBJETO PARA INTERACTUAR CON EL:
bulbasour_1 = Bulbasour("Cactus", 5000, 2500, 'Verde')

# PARA OBTENER/VER/MOSTRAR SU NOMBRE USAREMOS ESTA SINTAXIS "nombre_objeto.get_variable()"
print(bulbasour_1.get_nombre())

# PARA ESTABLECER/MODIFICAR SU NUEVO NOMBRE USAREMOS ESTA SINTAXIS "nombre_objeto.set_variable(x)"
bulbasour_1.set_nombre("Pepe")  # => ACA INGRESAMOS OTRO VALOR A LA VARIABLE PRIVADA
print(bulbasour_1.get_nombre()) # => ACA PODEMOS VER COMO SU VARIABLE AHORA CONTIENE OTRO NOMBRE






# FORMA 2:
# FORMA PYTHONICA USANDO @Property

class Bulbasour:

    __tipo = 'Planta'
    def get_tipo(self):  # => ACA DEFINIMOS UN GET PARA PODER MOSTRAR SU TIPO SIN PROBLEMA ALGUNO
        return self.__tipo # => ACA RETORNAMOS EL TIPO 

    def __init__(self, nombre, nivel, salud, color):
        self.__nombre = nombre
        self.nivel = nivel
        self.salud = salud
        self.__color = color


    # CREANDO UN GET(MOSTRAR/VER/OBTENER...) PYTHONICAMENTE "@property":
    @property             # => usamos el decorador property
    def nombre(self):     # => definimos la funcion, con "def" seguido el nombre del atributo (Lo mas recomendado es que se llame como el atributo pero sin los dos 
                          #    guiones bajos(__) y entre parentecis "(self)"
                                  
        return self.__nombre # => Y ahora aca retornamos el valor que exista en esa variable de instancia privado
     
    # CREANDO UN SET (MOSTRAR/VER/OBTENER...) PYTHONICAMENTE "@nombre_variable.setter":
    @nombre.setter
    def nombre(self, nombre): # => EN ESTE CASO AL QUERER TENER UN METODO PARA ESTABLECERLE UN NUEVO VALOR A NUESTRA VARIABLE DE INSTANCIA PRIVADA, NECESITAMOS UN RECIBIR UN PARAMETRO 
        self.__nombre = nombre
        if nombre == str:           # => CON ESTE CONDICIONAL ESTABLECEMOS QUE EL NOMBRE SOLO PUEDE CONTENER LETRAS (STRINGS) Y NO NUMEROS
            self.__nombre = nombre  # => SI ES IGUAL A UN STRING GUARDAMOS EN LA VARIABLE PRIVADA
        else:
            print("El nombre no permite numeros o caracteres especiales") # => DE LO CONTRARIO IMPRIME MENSAJE DE ADVERTENCIA


    # METODO/ACCION
    def atacar(self):
        print(f"Bulbasour ataca y genera ¡{self.nivel/4}! de daño.")


# USANDO LOS GET Y SET CREADOS PYTHONICAMENTE:

# CREACION DEL OBJETO PARA INTERACTUAR CON EL:
bulbasour_1 = Bulbasour("Cactus", 5000, 2500, 'Verde')

# PARA OBTENER/VER/MOSTRAR SU NOMBRE USAREMOS ESTA SINTAXIS "nombre_objeto.variable"
print(bulbasour_1.nombre)

# PARA ESTABLECER/MODIFICAR SU NUEVO NOMBRE USAREMOS ESTA SINTAXIS "nombre_objeto.variable = x"
bulbasour_1.nombre = "Pepe"  # => ACA INGRESAMOS OTRO VALOR A LA VARIABLE PRIVADA
print(bulbasour_1.nombre) # => ACA PODEMOS VER COMO SU VARIABLE AHORA CONTIENE OTRO NOMBRE