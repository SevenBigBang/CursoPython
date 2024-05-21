# POO - ENCAPSULAMIENTO: ME PERMITE OCULTAR DETALLES DE IMPLEMENTACION DE UN OBJETO UNICAMENTE EXPONIENDO LO NECESARIO PARA QUE OTROS OBJETOS PUEDA INTERACTUAR EN EL, TAMBIEN NOS BRINDARA UNA INTERFAZ SEGURA

class Pikachu:
    tipo = 'Electrico'

    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud
        self.voltaje_max = voltaje_max
        self.amperaje_max = amperaje_max
        self.color = color

    def atacar(self):
        print(f"Pikachu ataca y genera {self.nivel/4} de daño.")

pikachu_1 = Pikachu('Roco', 1500, 2000, 50, 2, 'Rojo')
print(f'El pikachu llamado {pikachu_1.nombre}, tiene un nivel de {pikachu_1.nivel} y es de tipo {pikachu_1.tipo}.')

pikachu_1.nivel = 2000 # ==> De esta forma podemos acceder a variables de instancias y modificarlas, en este caso mi pikachu despues de entrenar subio de nivel
print(f'El pikachu llamado {pikachu_1.nombre}, ha entrenado ahora tiene un nivel de {pikachu_1.nivel} y es de tipo {pikachu_1.tipo}.')


pikachu_1.tipo = 'Fuego' # ESTO ESTA MAL YA QUE NUESTRO OBJETO NO ESTA PENSANDO PARA PODER CAMBIAR SU TIPO, PARA ESTO SE USA LA ENCAPSULACION

pikachu_1.nivel = -100   # ESTO TAMBIEN ESTA MAL SI BIEN QUEREMOS QUE SE PUEDA MOFICAR EL NIVEL DE NUESTRO OBJETO, NO PUEDE SER NEGATIVO DE NINGUNA MANERA

# ADICIONALMENTE TODOS LO ATRIBUTOS SEAN DE CLASE O INSTANCIA SON PUBLICOS DE FORMA PREDETERMINDA LO CUAL TAMBIEN ESTA MAL, YA QUE CUALQUIERA PUEDE ACCEDER A ELLOS
# Y DE AQUI NACE EL CONCEPTO DE ATRIBUTOS PRIVADOS.



# EN MULTIPLES LENGUAJES DE PROGRAMACION COMO C#, JAVA U OTRAS, EN LAS CUALES LAS VARIABLES DE INSTANCIA PUEDEN SER PUBLICAS O PRIVADAS, A DIFERENCIA DE PYTHON DONDE
# TODO ES PUBLICO

# PUBLICAS: SE PUEDEN ACCEDER DE LA SIGUIENTE MANERA; "nombre_objeto.variable_de_instancia = cambio_variable_instancia", ESCRIBIMOS EL NOMBRE DE NUESTRO OBJETO, SEGUIDO
#           PONEMOS UN PUNTO Y AHI NOS APARACERA TODAS LAS VARIABLES DE INSTANCIA Y METODOS QUE TENGA LA CLASE CON LA CUAL CREAMOS NUESTRO OBJETO.

# PRIVADA: COMO EL NOMBRE LO INDICA ESTAS VARIABLES O METODOS, NO PUEDEN SER MODIFICADOS DE NINGUNA MANERA, SOLO PUEDEN SER ACCEDIDOS DESDE DENTRO DE LA CLASE




# EN PYTHON: EN PYTHON NO EXISTE EL CONCEPTO DE PUBLICO O PRIVADO!!!, SOLO EXISTEN CONVENCIONES O SINTAXIS ESPECIALES PARA DAR A ENTENDER SI ES PUBLICA O PRIVADA

# AHORA VAMOS A ARREGLAR NUESTRA CLASE (Esta vez con un Charmander):

class Charmander:
    __tipo = 'Fuego' # => PARA HACER QUE NUESTRA VARIABLE DE CLASE O INSTANCIA, SEA PRIVADA DE ALGUN MODO, USAMOS DOBLE GUION AL PISO(__nombreInstancia) CON ESTO PYTHON,
                     #    NOS MOSTRARA UN ERROR EN LA CONSOLA CADA QUE INTENTEMOS MODIFICARLA

    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud
        self.__voltaje_max = voltaje_max   # => Tambien haremos privados estas variables de instancias para que no puedan ser modificadas
        self.__amperaje_max = amperaje_max # => Tambien haremos privados estas variables de instancias para que no puedan ser modificadas
        self.color = color

    def atacar(self):
        print(f"Charmander ataca y genera {self.nivel/4} de daño.")

charmander_1 = Charmander('Roco', 1500, 2000, 50, 2, 'Rojo')
print(f'El Charmander llamado {charmander_1.nombre}, tiene un nivel de {charmander_1.nivel} y es de tipo.')


