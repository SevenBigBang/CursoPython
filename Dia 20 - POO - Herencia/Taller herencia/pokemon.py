# CREACION DE CLASE PADRE: La clase padre se crea de la forma mas generica posible para que sus clases hijas tengan esos atributos genericos y no tengan que repetir codigo
class Pokemon:
    def __init__(self, nombre, nivel, salud, color): # INICIALIZADOR
        self.__nombre = nombre  # => Atributo generico instancia publica
        self.__nivel = 0        # => ESTABLECESMOS ESTE ATRIBUTO EN NONE YA QUE NO ESTA HACIENDO LA RESPECTIVA VALIDACION
        self.__salud = 0
        self.__color = color    # => Atributo generico instancia privada

        self.nivel = nivel   # => PARA LOGRAR HACER LA VALIDACION, USAMOS self.nombre_de_propiedad = nombre atributo
        self.salud = salud   # => Y ASI PODEMOS LOGRAR QUE DESDE LA CREACION DEL OBJETO SE LOGRE CREAR UNA VALIDACION CORRECTA
    
    # YA QUE LOS GETTER Y SETTER SON MUY GENEREICOS Y LOS USAN TODOS LOS POKEMONES LOS ESTABLCEMOS EN LA CLASE PADRE PARA NO REPETIR CODIGO EN LAS CLASES HIJAS:
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    
    @property
    def nivel(self):
        return self.__nivel
    
    @nivel.setter
    def nivel(self, nivel):
        if nivel > 0 and nivel < 500:
            self.__nivel = nivel
        else:
            print("El nivel no puede ser menor a 0 y tampoco mayor a 500")
    
    @property
    def salud(self):
        return self.__salud 
    
    @salud.setter
    def salud(self, salud):
        if salud > 0 and salud < 3000:
            self.__salud = salud
        else:
            print("La salud no puede ser menor a 0 o mayor de 3.000")
    

    @property
    def color(self):
        return self.__color

# CREAMOS NUESTRA CLASE PADRE CON SUS INSTANCIAS CORRESPONDIENTES, LAS CUALES SE VAN A CREAR EN BASE AL VALOR QUE SE LE PASE EN SU INICIALIZADOR