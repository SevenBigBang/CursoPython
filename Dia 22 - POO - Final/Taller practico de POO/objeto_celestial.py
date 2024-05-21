import pygame # ==> IMPORTAMOS PYGAME PARA VERLOS GRAFICAMENTE
import math
from abc import ABC, abstractmethod

pygame.init()


class ObjetoCelestial(ABC):
    def __init__(self, nombre, ruta_imagen, masa, distancia=0, vel_orbita=0):
        self.nombre = nombre
        self.ruta_imagen = ruta_imagen
        self.imagen = pygame.image.load(ruta_imagen) # ==> Utilizamos pygame libreria para poder cargar imagenes reales mediante paths "rutas"
        self.rectangulo = self.imagen.get_rect() # ==> Se crea una nueva variable de instancia para que pygame almacene el rectangulo de cada imagen para ubicar los elementos(imagenes) cargados
        self.angulo = 0 # ==> Definimos la variable angulo, y la incializamos en 0, ya que esta va a aumentar de 0 a 360 lo cual le dara movimiento a nuestras imagenes
        self.distancia = distancia
        self.__vel_orbita = 0
        self.__masa = 0

        self.vel_orbita = vel_orbita
        self.masa = masa

        # zoom
        self.zoom_escala = 1.0



    # PROPIEDADES A ENCAPSULAR:
    @property
    def vel_orbita(self):
        return self.__vel_orbita
    @vel_orbita.setter
    def vel_orbita(self, valor):
        if valor >=0 and valor <=10:
            self.__vel_orbita = valor
        else:
            raise ValueError('Velocidad de orbita poco probable.')
    
    @property
    def masa(self):
        return self.__masa
    @masa.setter
    def masa(self, masa):
        if masa >= 3375 and masa <= 33000:
            self.__masa = masa
        else:
            raise ValueError('La masa es poco probable')

    

    # METODO PARA EL MOVIMIENTO DE LOS PLANETAS EN BASE AL ANGULO Y SU VELOCIDAD DE ORBITA
    def movimiento(self):
        self.angulo += self.vel_orbita

    
    def dibuja(self, pantalla):
        x = (pantalla.get_width() // 2) + (self.distancia * math.cos(math.radians(self.angulo))) # ==> Para la cordenada x vamos a ubicarnos en la mitada de nuestra pantalla, le vamos a 
                                                                                                 #     sumar la distancia con la cual venga definida el objeto, multiplicado por le circulo 
                                                                                                 #     unitario para obtener una sensacion de angulo

        y = (pantalla.get_height() // 2) + (self.distancia * math.sin(math.radians(self.angulo)))# TODA ESTA LOGICA ES PARA QUE NUESTRO OBJETO PUEDA GIRAR EN CIRCULOS
        # print(f"Objeto: {self.ruta_imagen}\ncordenada x: {x}\ncordenada y: {y}")

        ancho = int(self.rectangulo.width * self.zoom_escala)
        alto = int(self.rectangulo.height * self.zoom_escala)
        imagen_escalada = pygame.transform.scale(self.imagen, (ancho, alto))
        rectangulo_escalado = imagen_escalada.get_rect()

        # PARA QUE LOS VALORES QUE CALCULAMOS SEAN ASIGNADOS A ESA IMAGEN A TRAVES DE SU RECTANGULO DE AREA MINIMA
        self.rectangulo.centerx = x
        self.rectangulo.centery = y

        rectangulo_escalado.centerx = x
        rectangulo_escalado.centery = y

        # LE DECIMOS A LA PANTALLA DONDE SE VA A DIBUJAR NUESTRA IMAGEN SEGUN SU RECTANGULO Y SUS CORDENADAS
        pantalla.blit(self.imagen, self.rectangulo)

        pantalla.blit(imagen_escalada, rectangulo_escalado)



        
        font = pygame.font.SysFont(None, 24)  
        texto = font.render(self.nombre, True, (255, 255, 255))  
        texto_rect = texto.get_rect(center=(self.rectangulo.centerx, self.rectangulo.centery - 20))  
        pantalla.blit(texto, texto_rect)  


    def zoom(self):
        llaves = pygame.key.get_pressed()
        if llaves[pygame.K_q] > 0:
            self.zoom_escala += 0.1
        elif llaves[pygame.K_e] > 0:
            self.zoom_escala -= 0.1
        # elif llaves[pygame.K_q] or llaves[pygame.K_e] >= 0:
        #     print("Limite")

    
    @abstractmethod
    def generar_campo_magnetico(self, screen):
        pass
            
            

