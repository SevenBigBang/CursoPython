# ABSTRACCION: CAPACIDAD DE REPRESENTAR CARACTERISTICAS ESENCIALES DE UN OBJETO SIN INCLUIR DETALLES INNECESARIOS; ES FUNDAMENTAL ENFOCARSE EN LOS ASPECTOS MAS IMPORTANTES DE UN OBJETO MIENTRAS
# SE OCULTAN DETALLES MENOS RELEVANTES.


# En este ejemplo, la clase Pokemon representa la abstracción de un Pokémon.
class Pokemon:
    def __init__(self, nombre, tipo, nivel, hp):
        # Definimos atributos como nombre, tipo, nivel y hp para representar las características básicas de un Pokémon. 
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.hp = hp

    def atacar(self, ataque):
        print(f"{self.nombre} usa {ataque}!")

    def recibir_danio(self, danio):
        self.hp -= danio
        if self.hp <= 0:
            print(f"{self.nombre} ha sido derrotado...")
        else:
            print(f"{self.nombre} tiene {self.hp} HP restantes.")


pikachu = Pokemon("Pikachu", "Eléctrico", 10, 100)


print(f"Nombre: {pikachu.nombre}")
print(f"Tipo: {pikachu.tipo}")
print(f"Nivel: {pikachu.nivel}")
print(f"HP: {pikachu.hp}")


pikachu.atacar("Impactrueno")

pikachu.recibir_danio(20)
pikachu.recibir_danio(20)
pikachu.recibir_danio(20)
pikachu.recibir_danio(20)
pikachu.recibir_danio(20)
 
# LA ABSTRACCION ES LA FORMA "CORRECTA" PARA CREAR INSTANCIAS EN UNA CLASE, ES DECIR, SOLO CREAREMOS VARIABLES DE INSTANCIAS NECESARIAS Y PRACTICAS, NO VAMOS A INSTANCIAR 
# "EL TAMAÑO DE LA COLA DE PIKACHU" (ajaja), RECUERDA SOLO LO MAS NECESARIO :D



####################################################### EJERCICIO PRACTICO ##############################################################
#                                                                                                                                       #
#  - Combate contra el ordenador: Modifica la clase Batalla para que puedas combatir contra un oponente controlado por el ordenador.    #
#    Implementa una lógica simple para que el oponente elija sus movimientos de forma aleatoria.                                        #
#                                                                                                                                       #
#                                                                                                                                       #
##########################################################################################################################################