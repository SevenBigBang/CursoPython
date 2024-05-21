from hijo import Hijo

class Nieto(Hijo):
    def __init__(self, color_piel, color_cabello, color_ojos, altura, peso, contextura, caracter):
        super().__init__(color_piel, color_cabello, color_ojos, altura, peso, contextura, caracter)


nieto_1 = Nieto("Blanco", "Rubio", "Azules", 170, 65, "Gruesa", "Dormilon")

print(f"El primer nieto tiene un color de piel {nieto_1.color_piel}, un color de cabello {nieto_1.color_cabello}, unos ojos color {nieto_1.color_ojos}, con una altura de {nieto_1.altura}cm, con un peso de {nieto_1.peso}kg, con una contextura {nieto_1.contextura} y un caracter {nieto_1.caracter}")