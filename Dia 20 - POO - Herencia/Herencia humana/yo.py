from padre import Padre

class Yo(Padre):

    def __init__(self, color_piel, color_cabello, color_ojos, altura, peso, contextura, caracter):
        super().__init__(color_piel=color_piel, color_cabello=color_cabello, color_ojos=color_ojos, peso=peso, altura=altura, caracter=caracter, contextura=contextura)


yo_1 = Yo("Blanco", "Negro", "Azules", 170, 60, "Delgado", "Dormilon")
print(yo_1.color_piel, yo_1.color_cabello, yo_1.color_ojos, yo_1.altura, yo_1.peso, yo_1.contextura, yo_1.caracter)

yo_1.caracter = "Bravo"
print(yo_1.color_piel, yo_1.color_cabello, yo_1.color_ojos, yo_1.altura, yo_1.peso, yo_1.contextura, yo_1.caracter)