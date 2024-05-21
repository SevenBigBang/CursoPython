from yo import Yo

class Hijo(Yo):
    def __init__(self, color_piel, color_cabello, color_ojos, altura, peso, contextura, caracter):
        super().__init__(color_piel, color_cabello, color_ojos, altura, peso, contextura, caracter)


hijo_1 = Hijo("Cafe", "Negro", "Verdes", 200, 120, "Delgada", "Bravo")
print(hijo_1.color_piel, hijo_1.color_cabello, hijo_1.color_ojos, hijo_1.altura, hijo_1.peso, hijo_1.contextura, hijo_1.caracter)