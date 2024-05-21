from tipo_electrico import TipoElectrico # IMPORTAMOS


class Pikachu(TipoElectrico): # CREAMOS LA CLASE HIJA ENTRE PARENTECIS HACEMOS LLAMADO DE LA CLASE PADRE

    
    def __init__(self, nombre, nivel, salud, color,  voltaje, amperaje):
        super().__init__(nombre=nombre,
                         nivel=nivel, 
                         salud=salud, 
                         color=color, 
                         voltaje=voltaje, 
                         amperaje=amperaje)     # => PARA INICIALIZAR LOS ATRIBUTOS HEREDADOS UTILIZAMOS
                                                #    "super().__init__(x=x, y=y, z=z)" 


    # @property                            #
    # def nombre(self):                    # => USAMOS ESTA SINTAXIS PARA DEFINIR UN "GETTER", Y PODER VER EL VALOR.              
    #     return self._Pokemon__nombre     #   
    
    # @nombre.setter                       #   
    # def nombre(self, nombre):            # => USAMOS ESTA SINTAXIS PARA DEFINIR UN "SETTER" Y PODER MODIFICAR SU VALOR. (SE DEFINE UN SETTER PORQ ESTA ENCAPSULADA)
    #     self._Pokemon__nombre = nombre   #


    

    

    
    
pikachu_1 = Pikachu('Roko', 499, 1000, 'rojo', 100, 100)


print(f"El Pikachu con nombre {pikachu_1.nombre}, de nivel {pikachu_1.nivel}, de salud de {pikachu_1.salud} puntos de vida y de color {pikachu_1.color} ¡ataca! con un voltaje de {pikachu_1.voltaje} generando {pikachu_1.nivel/4 + pikachu_1.voltaje} de daño!!, su tipo es {pikachu_1.tipo}")
# pikachu_1.voltage = 100
# pikachu_1.nombre = "Pokocho"
# pikachu_1.nivel = -100
# pikachu_1.salud = -10
# pikachu_1.__color = 'Azul'

print(f"El Pikachu con nombre {pikachu_1.nombre}, de nivel {pikachu_1.nivel} y de color {pikachu_1.color} ¡ataca! con un voltage de {pikachu_1.voltaje} generando {pikachu_1.nivel/4} de daño!!")


# EN LA CLASE PIKACHU HEREDAMOS DE LA CLASE POKEMON MEDIANTE LA SINTAXIS "class Pikachu(Pokemon):" Y PARA INICIALIZAR LOS ATRIBUTOS HEREDADOS UTILIZAMOS
# "super().__init__(x=x, y=y, z=z)" 

pikachu_1.atacar()