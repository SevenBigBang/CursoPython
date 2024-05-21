# CLASES Y METODOS EN POO: 

# INICIALIZADOR (def__init__(self, x, y, z):) : SON UN METODO QUE SE EJECUTA AUTOMATICAMENTE A PENAS EL OBJETO SEA CREADO * METODO MAGICO, CUANDO SE INICIA EL METODO,
#                                               CREA LAS VARIABLES DE INSTANCIA:
#                                               def __init__(self, x, y, z):  => (x, y, z) son Atributos de instancia 
#                                                   self.x = x      => Variable de instancia
#                                                   self.y = y      => Variable de instancia
#                                                   self.z = z      => Variable de instancia

class Pikachu:
    tipo = 'Electrico'
                       
    def __init__(self, nombre, nivel, salud):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud

    #CREACION DE METODOS (ACCIONES):
    def atacar(self):                  
        print(f"Pikachu ataca y genera {self.nivel/4} de daño")# => Aca se usa "self.", para acceder a los atributos de instancia,
                                                               #    de lo contrario nivel deberia ser un atributo de clase, como lo es el tipo.

# Ahora creamos objetos apartir de esta clase "Pikachu":
          # Clase  
pikachu_1 = Pikachu('Pepe', 750, 500)

          # Atributos de instancia variables:            
Pikachu_2 = Pikachu('Roco', 1000, 1000)


# LLAMAR METODOS(ACCIONES) DE LOS OBJETOS: 

print(f"El Pikachu llamado {pikachu_1.nombre}, ¡Ataca!.")
pikachu_1.atacar() # COMO EL METODO TAMBIEN ES CONSIDERADO FUNCION SE USAN ()

print(f"El Pikachu llamado {Pikachu_2.nombre}, ¡Ataca!")
Pikachu_2.atacar()