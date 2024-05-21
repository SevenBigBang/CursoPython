# HERENCIA DE METODOS(ACCIONES): AL IGUAL QUE LAS INSTANCIAS YA SEAN PRIVADAS O PUBLICAS, DE CLASE O INSTANCIAS, SE PUEDEN HEREDAR, LOS METODOS FUNCIONAN DE LA MISMA FORMA, EN TODOS LOS ASPECTOS


# CLASE ABUELO

class Pokemon():
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



# CLASE PADRE


class TipoElectrico(Pokemon):
    

    __tipo = "Electrico"
    @property
    def tipo(self):         
        return self.__tipo
    
    def __init__(self, nombre, nivel, salud, color, voltaje, amperaje):
        super().__init__(nombre=nombre, nivel=nivel, salud=salud, color=color)
        self.__voltaje = 0
        self.__amperaje = 0

        self.voltaje = voltaje
        self.amperaje = amperaje

    #____________________________________________________
    @property                                            #
    def voltaje(self):                                   #
        return self.__voltaje                  #
                                                         #
    @voltaje.setter                                      #
    def voltaje(self, voltaje):                          # =======> ESTAS SON LAS PROPIEDADES (SETTERS Y GETTERS), PARA ACCEDER A ESTOS (__voltaje_maximo)
        if voltaje > 0:                                  #          ATRIBUTOS DE INSTANCIA. ESTO QUE ESTAMOS HACIENDO SON INTERFACES SEGURAS, PARA HACER LAS MODIFICACIONES
            self.__voltaje = voltaje              #          DE LOS ATRIBUTOS DE LOS TIPO ELECTRICO.
        else:                                            #
            print("El voltaje no puede ser menor a 0")   #
    #____________________________________________________#

    @property
    def amperaje(self):
        return self.__amperaje
    
    @amperaje.setter
    def amperaje(self, amperaje):
        if amperaje > 0:
            self.__amperaje = amperaje
        else:
            print("El amperaje no puede ser menor a 0")
    

    # METODOS

#   ________________________________________________________________________________________
                                                                                            #
    def rayo(self):                                                                         #
        print(f"Ataca con rayo y genera {(self.voltaje + self.amperaje) / 4} de daño")      #  ===> ESTE ES UN METODO/ACCION MUY GENEREICO PARA UN POKEMON DE TIPO ELECTRICO, ENTONCES LA PODEMOS 
                                                                                            #
    def electro_voltio(self):                                                               #
        print(f"Ataca con electro voltio y genera {(self.nivel/2 + self.voltaje*0.5 )} de daño")                                                              
                                                                                            #       VOLVER UNA CARACTERISTICA QUE SE HEREDE, A DIFERENCIA DE UN METODO MAS PROPIO COMO: =># 
#   ________________________________________________________________________________________#                                                                                             #      
                                                                                                                                                                                          #  
                                                                                                                                                                                          #
                                                                                                                                                                                          #          
                                                                                                                                                                                          #  
     
     
     
     
                                                                                                                                                                                          #
                                                                                                                                                                                          #          
# CLASE HIJA                                                                                                                                                                              #  
                                                                                                                                                                                          #                                                                                                                                                                                          #  
class Pikachu(TipoElectrico): # CREAMOS LA CLASE HIJA ENTRE PARENTECIS HACEMOS LLAMADO DE LA CLASE PADRE                                                                                  #
                                                                                                                                                                                          #
                                                                                                                                                                                          #  
    def __init__(self, nombre, nivel, salud, color,  voltaje, amperaje):                                                                                                                  #  
        super().__init__(nombre=nombre,                                                                                                                           #########################  
                         nivel=nivel,                                                                                                                             #                      
                         salud=salud,                                                                                                                             #  
                         color=color,                                                                                                                             #  
                         voltaje=voltaje,                                                             #                                                           V      
                         amperaje=amperaje)     # => PARA INICIALIZAR LOS ATRIBUTOS HEREDADOS UTILIZAMOS
                                                #    "super().__init__(x=x, y=y, z=z)" 

    # METODO PROPIO DE PIKACHU:
    def cola_hierro(self):
        print(f"{pikachu_1.nombre} ataca con cola hierro y genera {pikachu_1.nivel + pikachu_1.voltaje} de daño!!!")   # ==> METODO PROPIO DE PIKACHU Y DE TODOS LOS PIKACHUS     

    
    
pikachu_1 = Pikachu('Roko', 499, 1000, 'rojo', 100, 100)

print(f"El Pikachu con nombre {pikachu_1.nombre}, de nivel {pikachu_1.nivel} y de color {pikachu_1.color} ¡ataca! con un voltage de {pikachu_1.voltaje} generando {pikachu_1.nivel/4} de daño!!")

pikachu_1.rayo()
pikachu_1.cola_hierro()
pikachu_1.electro_voltio()