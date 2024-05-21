# POLIMORFISMO: PERMITE QUE OBJETOS DE DIFERENTES CLASES PUEDEN SER TRATADOS DE MANERA UNIFORME (UNICAMENTE SI COMPARTEN UNA CLASE BASE)

# PARA EXPLICAR EL POLIMORFISMO CON POKEMONES, CONSIDERAMOS DIFERENTES TIPOS DE ATAQUES QUE PUEDEN TENER LOS POKEMON. CADA ATAQUE PUEDE TENER UN EFECTO DIFERENTE, COMO INFLIGIR
# DAÑO, CAUSAR UNA CONDICION ESPECIAL (PARALISIS, ENVENENAMIENTO, ETC...), O CURAR AL POKEMON QUE LO USA.


# PARA LOGRAR UN POLIMORFISMO TENEMOS QUE TENER EN CUENTA LAS "CLASES ABSTRACTAS": ES UNA CLASE QUE NO VA PODER SER INSTANCIADA DIRECTAMENTE; EN ESTE CASO EL METODO ATACAR TENDRIA QUE FUNCIONAR
# EN LA CLASE PADRE COMO UNA PLANTILLA

# EJEMPLO: 
# Para declarar una clase abstracta tenemos que importar "from abc import ABC, abstractmethod"
from abc import ABC, abstractmethod

# Creamos la clase:
class Pokemon(ABC): # Para definir que nuestra clase "Pokemon", es abstracta, hacemos que herede de "ABC"; Con esto logramos que sea abstracta y que no se pueda instancciar directamente :D

    # Definimos los inicializadores de instancia
    def __init__(self, nombre, nivel, salud, color):
        self.__nombre = None
        self.__nivel = None
        self.__salud = None

        # Hacemos que los parametros (nivel y salud) pasen primero por un metodo, para que se ejecuten sin problemas
        self.salud = salud
        self.nivel = nivel
        self.nombre = nombre
        self.color = color

    
    # Creamos los decoradores Getter y Setter correspondientes a cada parametro
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str): # => "isinstance(x, str)": Sirve para comprobar si la variable es de este tipo en este caso "str", pero puede ser modificada a cualquier tipo
            self.__nombre = nombre
        else:
            print("El nombre no puede ser un numero")
    
    @property
    def nivel(self):
        return self.__nivel
    @nivel.setter
    def nivel(self, nivel):
        if nivel > 0 and nivel < 5000:
            self.__nivel = nivel
        else:
            print("El nivel no puede ser menos a cero o superior a 5000")
    
    @property
    def salud(self):
        return self.__salud
    @salud.setter
    def salud(self, salud):
        if salud > 0 and salud < 101:
            self.__salud = salud
        else:
            print("El pokemon {self.nombre} ha sido abatido!!! D:")
    
    # @property
    # def color(self):
    #     return self.__color
    

    # Ahora crearemos el metodo "Plantilla", o metodo(Accion) en comun para nuestros herederos en este caso un ataque (ES UNA PLANTILLA QUE DEBEN CUMPLIR SI O SI LAS CLASES HIJAS):
    @abstractmethod # ==> PARA DEFINIR QUE NUESTRO METODO(ACCION) ES ABSTRACTO(PLANTILLA)
    def atacar(self):
        pass  # ==> Tenemos que dejar el metodo vacio porq cada hijo de esta clase padre "Pokemon", podra darle diferentes acciones a este metodo >:D



    # AHORA, VOLVAMOS ATRAS, VOY A OMITIR LO QUE YA HEMOS TRABAJADO QUE SERIAN LAS CLASES HIJAS DE HIJAS, ME REFIERO A LA CREACION DE "TIPO FUEGO, TIPO ELECTRICO" Y SOLO CREAREMOS DOS CLASES
    # PIKACHU Y CHARMANDER PARA MOSTRAR TODO EN POCAS LINEAS :P


# CREACION CLASE HIJA (PIKACHU):
class Pikachu(Pokemon):
    # DEFINIMOS LOS INICIALIZADORES DE LA CLASE: 
    def __init__(self, nombre, nivel, salud, color, carga): # =>Carga max pertenece a una instancia de la clase Pikachu (No es heredada)
        super().__init__(nombre, nivel, salud, color) # ==> PERO ESTABLECEMOS QUE DICHOS INICIALIZADORES PERTENECEN A NUESTRO PADRE "Pokemon" con el metodo "super().__init__(x, y, z, ...)"

        #INICIALIZADORES PROPIOS DE PIKACHU:
        self.__carga = None
        self.carga = carga
    
    @property
    def carga(self):
        return self.__carga
    @carga.setter
    def carga(self, carga):
        if carga > 0 and carga < 10001:
            self.__carga = carga
        else:
            print("La carga no puede ser menor a cero ni mayor a 10000")

    # DEFINIMOS EL METODO USANDO LA PLANTILLA HEREDADA "atacar(self)" en la linea 69:

    def atacar(self): # ==> USAMOS EL MISMO NOMBRE QUE USO EL METODO PADRE PARA REMPLAZARLO
        print(f"{self.nombre} ataca con electricidad y genera {self.nivel + self.carga /4} de daño!")



# CREACION CLASE HIJA (CHARMANDER):
class Charmander(Pokemon):

    def __init__(self, nombre, nivel, salud, color, temperatura):
        super().__init__(nombre, nivel, salud, color)

        self.__temperatura = 0
        self.temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura
    @temperatura.setter
    def temperatura(self, temperatura):
        if temperatura > 0 and temperatura < 1001:
            self.__temperatura = temperatura
        else:
            print("La temperatura no puede ser menor a 0 ni mayor a 1000 grados centigrados")

    # HACEMOS LO MISMO LLAMAMOS AL METODO HEREDADO POR NUESTRO PADRE 
    def atacar(self):
        print(f"{self.nombre} ataca con fuego y genera {self.nivel + self.temperatura / 4} de daño!")








# CREAMOS NUESTROS OBJETOS DE CADA CLASE HIJA CREADA:

pika_1 = Pikachu("Ramon", 250, 100, "Amarillo", 250)
charma_1 = Charmander("Chorizard", 300, 80, "Rojo", 250)

# ESTA ES LA PRUEBA DEL POLIMORFISMO:
pika_1.atacar()
charma_1.atacar()

# COMO TE DISTE CUENTA, LOS DOS USAN DIFERENTES LOGICAS APARTIR DE UN MISMO METODO, ESTO ES POLIMORFISMO NUESTRA CLASE PADRE NOS HEREDA UNA PLANTILLA DE ATAQUE PARA QUE CADA HIJO PUEDA,
#                                                                                   ATACAR A SU PARTICULARIDAD :D (MAS CLARO IMPOSIBLE XD)

# POLIMORFO (RAE): Que tiene o puede tener distintas formas. ESPERO HAYAS APRENDIDO >:D