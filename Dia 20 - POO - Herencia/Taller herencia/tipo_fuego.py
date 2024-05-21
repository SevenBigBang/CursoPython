from pokemon import Pokemon

class TipoFuego(Pokemon):

    __tipo = "Fuego"
    @property
    def tipo(self):
        return self.__tipo

    def __init__(self, nombre, nivel, salud, color, temperatura):
        super().__init__(nombre, nivel, salud, color)

        self.__temperatura = 0
        self.temperatura = temperatura
    
    @property
    def temperatura(self):
        return self.__temperatura
    @temperatura.setter
    def temperatura(self, temperatura):
        if temperatura > 0: 
            self.__temperatura = temperatura
        else:
            print("La temperatura debe ser mayor a 0")
