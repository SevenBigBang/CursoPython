from objeto_celestial import ObjetoCelestial


class Asteroide(ObjetoCelestial):
    def __init__(self, ruta_imagen, distancia, vel_orbita, masa):
        super().__init__(ruta_imagen=ruta_imagen, 
                         distancia=distancia, 
                         vel_orbita=vel_orbita, 
                         masa=masa)
    
    def generar_campo_magnetico(self, screen):
        pass