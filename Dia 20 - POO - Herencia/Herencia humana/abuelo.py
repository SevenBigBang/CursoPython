class Abuelo():

    __caracter = "Bravo"
    @property
    def caracter(self):
        return self.__caracter
    @caracter.setter
    def caracter(self, caracter):
        if caracter == str:
            self.__caracter = caracter
        else:
            print("No puede ser un numero")


    def __init__(self, color_piel, color_cabello, color_ojos, altura, peso, contextura):

        self.__color_piel = color_piel
        self.__color_cabello = color_cabello
        self.__color_ojos = color_ojos
        self.__altura = None
        self.__peso = None
        self.__contextura = contextura

        self.altura = altura
        self.peso = peso

    
    @property
    def color_piel(self):
        return self.__color_piel
    
    @property
    def color_cabello(self):
        return self.__color_cabello
    
    @property
    def color_ojos(self):
        return self.__color_ojos
    
    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura):
        if altura > 0 and altura < 220:
            self.__altura = altura
        else:
            print("La altura no puede ser negativa")
    
    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso):
        if peso > 0 and peso < 200:
            self.__peso = peso
        else:
            print("El peso no puede ser negativo")
    
    @property
    def contextura(self):
        return self.__contextura