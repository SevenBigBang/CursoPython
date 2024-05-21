from pokemon import Pokemon


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

    def atacar(self):
        print(f"Ataca con rayo y genera {(self.voltaje + self.amperaje) / 4} de daño")