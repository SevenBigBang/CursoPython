# CONCEPTOS PYGAME NO EXPLICARE MUCHO A DETALLE YA QUE NO VIENE AL CASO DEL CURSO:

from estrella import Estrella
from planeta import Planeta
from asteroide import Asteroide
import pygame 




# CREAMOS LA VENTANA EN "PYGAME"

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sistema Solar")






# CREACION DE LOS OBJETOS

# CREANDO EL SOL:
sol = Estrella(nombre="                                 Sol", ruta_imagen="C:/Users/ccortes/Desktop/SEVEN/Dia 2/POO - ABSTRACCION/Ejemplo practico de POO/imagenes/sol.png", masa=30000, estado_nucleo="Activo")

# CREANDO LOS PLANETAS:
mercurio = Planeta(nombre="Mercurio", ruta_imagen="C:/Users/ccortes/Desktop/SEVEN/Dia 2/POO - ABSTRACCION/Ejemplo practico de POO/imagenes/mercurio.png", distancia= 100, vel_orbita= 1.72, masa= 4000, estado_nucleo= "Activo")
venus = Planeta(nombre="Venus", ruta_imagen="C:/Users/ccortes/Desktop/SEVEN/Dia 2/POO - ABSTRACCION/Ejemplo practico de POO/imagenes/venus.png", distancia= 200, vel_orbita= 1.26, masa= 6000, estado_nucleo= "Inactivo")
tierra = Planeta(nombre="Tierra", ruta_imagen="C:/Users/ccortes/Desktop/SEVEN/Dia 2/POO - ABSTRACCION/Ejemplo practico de POO/imagenes/tierra.png", distancia= 300, vel_orbita= 1.07, masa= 7000, estado_nucleo= "Activo")
marte = Planeta(nombre="Marte", ruta_imagen="C:/Users/ccortes/Desktop/SEVEN/Dia 2/POO - ABSTRACCION/Ejemplo practico de POO/imagenes/marte.png", distancia= 400, vel_orbita= 0.86, masa=5000, estado_nucleo= "Inactivo")
jupiter = Planeta(nombre="                           Jupiter", ruta_imagen="C:/Users/ccortes/Desktop/SEVEN/Dia 2/POO - ABSTRACCION/Ejemplo practico de POO/imagenes/jupiter.png", distancia= 550, vel_orbita= 0.47, masa= 15000, estado_nucleo= "Activo")
saturno = Planeta(nombre="                           Saturno", ruta_imagen="C:/Users/ccortes/Desktop/SEVEN/Dia 2/POO - ABSTRACCION/Ejemplo practico de POO/imagenes/saturno.png", distancia= 750, vel_orbita= 0.34, masa= 10000, estado_nucleo= "Activo")
urano = Planeta(nombre="Urano", ruta_imagen="C:/Users/ccortes/Desktop/SEVEN/Dia 2/POO - ABSTRACCION/Ejemplo practico de POO/imagenes/urano.png", distancia= 850, vel_orbita= 0.24, masa= 7000, estado_nucleo= "Activo")
neptuno = Planeta(nombre="Neptuno", ruta_imagen="C:/Users/ccortes/Desktop/SEVEN/Dia 2/POO - ABSTRACCION/Ejemplo practico de POO/imagenes/neptuno.png", distancia= 950, vel_orbita= 0.19, masa= 4000, estado_nucleo= "Activo")


# CREANDO ASTEROIDES:
#asteroide_1 = Asteroide(ruta_imagen="C:/Users/ccortes/Desktop/SEVEN/Dia 2/POO - ABSTRACCION/Ejemplo practico de POO/imagenes/asteroide.png", distancia= 320, vel_orbita= 0.10, masa= 4000)


# CARGANDO IMAGEN DE FONDO
background_imagen = pygame.image.load("C:/Users/ccortes/Desktop/SEVEN/Dia 2/POO - ABSTRACCION/Ejemplo practico de POO/imagenes/fondo.jpg").convert()
background_rectangulo = background_imagen.get_rect()

# Reloj
reloj = pygame.time.Clock()


# Tiempo de uso del programa:
funcionando = True
while funcionando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            funcionando = False
        
    # evento de zoom
    sol.zoom()
    mercurio.zoom()
    venus.zoom()
    tierra.zoom()
    marte.zoom()
    jupiter.zoom()
    saturno.zoom()
    urano.zoom()
    neptuno.zoom()
        
    
    screen.blit(background_imagen, background_rectangulo)
    sol.dibuja(screen)
    mercurio.dibuja(screen)
    venus.dibuja(screen)
    tierra.dibuja(screen)
    marte.dibuja(screen)
    jupiter.dibuja(screen)
    saturno.dibuja(screen)
    urano.dibuja(screen)
    neptuno.dibuja(screen)
    # asteroide_1.dibuja(screen)

    # llamamos al metodo de movmiento:
    # sol.movimiento()
    mercurio.movimiento()
    venus.movimiento()
    tierra.movimiento()
    marte.movimiento()
    jupiter.movimiento()
    saturno.movimiento()
    urano.movimiento()
    neptuno.movimiento()
    # asteroide_1.movimiento()

    #Llamamos metodos de crear campo magnetico
    mercurio.generar_campo_magnetico(screen)
    venus.generar_campo_magnetico(screen)
    tierra.generar_campo_magnetico(screen)
    marte.generar_campo_magnetico(screen)
    jupiter.generar_campo_magnetico(screen)
    saturno.generar_campo_magnetico(screen)
    urano.generar_campo_magnetico(screen)
    neptuno.generar_campo_magnetico(screen)


    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()