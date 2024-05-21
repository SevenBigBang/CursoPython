from pokemon import Pokemon

class Bulbasaur(Pokemon):

    __tipo = "Planta"
    @property
    def tipo(self):
        return self.__tipo
    
    def __init__(self, nombre, nivel, salud, color, poder_regenerativo):
        super().__init__(nombre, nivel, salud, color)

        self.__poder_regenerativo = poder_regenerativo
    

    @property
    def nombre(self):
        return self._Pokemon__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._Pokemon__nombre = nombre

    
    @property
    def nivel(self):
        return self._Pokemon__nivel
    
    @nivel.setter
    def nivel(self, nivel):
        self._Pokemon__nivel = nivel

    
    @property
    def salud(self):
        return self._Pokemon__salud 
    
    @salud.setter
    def salud(self, salud):
        if salud > 0 and salud < 3000:
            self._Pokemon__salud = salud
        else:
            print("La salud no puede ser menor a 0 o mayor de 3.000")
    

    @property
    def color(self):
        return self._Pokemon__color
    

    @property
    def curacion(self):
        return self.__poder_regenerativo
    



# CREACION DE OBJETO

bulbasaur_1 = Bulbasaur("Calabaza", 780, 3000, "Verde", 100)
print(f"El Bulbasaur de nombre {bulbasaur_1.nombre}, con salud de {bulbasaur_1.salud}, color {bulbasaur_1.color}, y nivel {bulbasaur_1.nivel}, ¡Ataca! Generado {bulbasaur_1.nivel/4} de daño!!! y se cura un total de {bulbasaur_1.curacion} por ataque...")

