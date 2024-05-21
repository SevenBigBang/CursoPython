from tipo_fuego import TipoFuego

class Charmander(TipoFuego):


    def __init__(self, nombre, salud, nivel, color, temperatura):
        super().__init__(nombre=nombre, 
                         salud=salud, 
                         nivel=nivel, 
                         color=color,
                         temperatura=temperatura)

        


charmander_1 = Charmander('Coco', 100, 200, "Rojo", 100)
print(f"El Charmander llamado {charmander_1.nombre}, con salud de {charmander_1.salud} de color {charmander_1.color}, de tipo {charmander_1.tipo}, de nivel {charmander_1.nivel}, ¡Ataca! con una temperatura de {charmander_1.temperatura} y genera {charmander_1.nivel/4 + charmander_1.temperatura} de daño!!!")
# charmander_1.salud = 25000
# charmander_1.nivel = 399
# print(f"El Charmander llamado {charmander_1.nombre}, con salud de {charmander_1.salud} de color {charmander_1.color}, de tipo {charmander_1.tipo}, de nivel {charmander_1.nivel}, ¡Ataca! con una temperatura de {charmander_1.temperatura} y genera {charmander_1.nivel/4 + charmander_1.temperatura} de daño!!!")
