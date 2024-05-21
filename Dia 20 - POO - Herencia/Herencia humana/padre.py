from abuelo import Abuelo

class Padre(Abuelo):

    def __init__(self, color_piel, color_cabello, color_ojos, altura, peso, contextura, caracter):
        super().__init__(color_piel, color_cabello, color_ojos, altura, peso, contextura)

        self.__caracter = caracter
    @property
    def caracter(self):
        return self.__caracter
    @caracter.setter
    def caracter(self, caracter):
        if isinstance(caracter, str):  # ==> "isinstance(x, y)" Sirve para que si el contenido es un tipo realiza la accion de lo contrario no
            self.__caracter = caracter
        else:
            print("No puede ser un numero")
    

