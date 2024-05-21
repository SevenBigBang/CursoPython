import pygame
from objeto_celestial import ObjetoCelestial

class Estrella(ObjetoCelestial):
    
    def __init__(self, nombre, ruta_imagen, masa, estado_nucleo):
        super().__init__(nombre=nombre, ruta_imagen=ruta_imagen, masa=masa)
        
        self.estado_nucleo = estado_nucleo


    def generar_campo_magnetico(self, screen):
        if self.estado_nucleo == 'Activo' and self.masa > 30000:
            width = self.rectangulo.width + 80
            height = self.rectangulo.height + 80
            red_field = pygame.image.load('C:/Users/ccortes/Desktop/SEVEN/Dia 2/POO - ABSTRACCION/Ejemplo practico de POO/imagenes/campo_rojo.png')
            red_field_resized = pygame.transform.scale(red_field, (width, height))
            
            red_field_resized_rectangulo = red_field_resized.get_rect()
            red_field_resized_rectangulo.centerx = self.rectangulo.centerx
            red_field_resized_rectangulo.centery = self.rectangulo.centery
            screen.blit(red_field_resized, red_field_resized_rectangulo)