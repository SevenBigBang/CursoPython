import pygame
from objeto_celestial import ObjetoCelestial

class Planeta(ObjetoCelestial):

    def __init__(self, nombre, ruta_imagen, distancia, vel_orbita, masa, estado_nucleo):
        super().__init__(nombre=nombre,
                         ruta_imagen=ruta_imagen, 
                         distancia=distancia, 
                         vel_orbita=vel_orbita, 
                         masa=masa)
        
        self.estado_nucleo = estado_nucleo



    def generar_campo_magnetico(self, screen):
        if self.estado_nucleo == 'Activo' and self.masa < 30000:
            width = self.rectangulo.width + 20
            height = self.rectangulo.height + 20

            blue_field = pygame.image.load('C:/Users/ccortes/Desktop/SEVEN/Dia 2/POO - ABSTRACCION/Ejemplo practico de POO/imagenes/campo_azul.png')
            blue_field_resized = pygame.transform.scale(blue_field, (width, height))

            blue_field_resized_rectangulo = blue_field_resized.get_rect()
            blue_field_resized_rectangulo.centerx = self.rectangulo.centerx
            blue_field_resized_rectangulo.centery = self.rectangulo.centery

            screen.blit(blue_field_resized, blue_field_resized_rectangulo)