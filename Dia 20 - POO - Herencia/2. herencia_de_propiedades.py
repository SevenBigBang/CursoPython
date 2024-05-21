# HERENCIA DE PROPIEDADES: COMO TODAS LAS CLASES ANTERIORMENTE CREADAS USABAN LOS MISMOS GETTERS Y SETTER, ENTONCES SE MOVIERON DE LAS CLASES HIJAS A UN SOLO BLOQUE
#                          DE CODIGO EN LA CLASE PADRE, LO CUAL HACE MAS FACIL EL MANEJO DE INSTANCIAS


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
    def curacion(self):
        return self.__poder_regenerativo
    
    @curacion.setter
    def curacion(self, curacion):
        self.__poder_regenerativo = curacion
    


# CREACION DE OBJETO

bulbasaur_1 = Bulbasaur("Calabaza", 499, 2999, "Verde", 100)
bulbasaur_1.curacion = 200
print(f"El Bulbasaur de nombre {bulbasaur_1.nombre}, con salud de {bulbasaur_1.salud}, color {bulbasaur_1.color}, y nivel {bulbasaur_1.nivel}, ¡Ataca! Generado {bulbasaur_1.nivel/4} de daño!!! y se cura un total de {bulbasaur_1.curacion} por ataque...")
print(bulbasaur_1.salud)