from pokemon import Pokemon

class Squirtle(Pokemon):
    
    __tipo = "Agua"
    @property
    def tipo(self):
        return self.__tipo

    def __init__(self, nombre, nivel, salud, color, presion_agua):
        super().__init__(nombre=nombre, nivel=nivel, salud=salud, color=color)

        self.__presion_agua = presion_agua


    @property
    def presion(self):
        return self.__presion_agua
    
    @presion.setter
    def presion(self, presion):
        self.__presion_agua = presion

    
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
        self._Pokemon__salud = salud

    
    @property
    def color(self):
        return self._Pokemon__color
    

squirtle_1 = Squirtle("Jose-jose", 500, 206, "Azul", 120)

print(f"El Squirtle llamado {squirtle_1.nombre}, de color {squirtle_1.color}, con salud de {squirtle_1.salud}, de nivel {squirtle_1.nivel}, ¡Ataca! con una presion de {squirtle_1.presion} y genera {squirtle_1.nivel/4 + squirtle_1.presion} de daño!!")

squirtle_1.nivel = 600

print(f"El Squirtle llamado {squirtle_1.nombre}, de color {squirtle_1.color}, con salud de {squirtle_1.salud}, de nivel {squirtle_1.nivel}, ¡Ataca! con una presion de {squirtle_1.presion} y genera {squirtle_1.nivel/4 + squirtle_1.presion} de daño!!")

    