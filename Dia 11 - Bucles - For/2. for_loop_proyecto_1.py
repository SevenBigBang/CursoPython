# FOR: NOS SIRVE PARA RECORRER ITERABLES, NOS FACILITAN EJECUTAR CIERTA CANTIDAD DE TAREAS (X) CANTIDAD DE VECES

# LIBRERIA TURTLE, VIENE POR PREDETERMINADO EN PYTHON:
import turtle # ==> SE APOYA EN LA INTERFAZ GRAFICA PARA ENSEÑAR PROGRAMACIONS

# CONFIGURAR LA VENTANA Y EL CURSOR:
ventana = turtle.Screen() # ==> SE UTILIZA EL METODO (.Screen), DE LA LIBRERIA TURTLE, PARA QUE NOS CREE UNA VENTANA GRAFICA Y LA GUARDE EN ESTE CASO EN LA VARIABLE "ventana"
ventana.bgcolor("white")  # ==> SE UTILIZA EL METODO (.bgcolor), PARA CAMBIAR UN ATRIBUTO, EN ESTE CASO EL COLOR DE LA VENTANA CREADA EN ESTE CASO A "Blanco"
tortuga = turtle.Turtle() # ==> SE UTILIZA EL METODO (.Turtle), DE LA LIBRERIA TURTLE, PARA CREAR UNA "Tortuga", QUE NOS SERVIRA DE CURSOR EN LA VENTANA QUE YA CREAMOS
tortuga.speed(1)          # ==> SE UTILIZA EL METODO (.speed(x)), PARA CAMBIAR UN ATRIBUTO, EN ESTE CASO LA VELOCIDAD DE NUESTRA VARIABLE ANTES CREADA (EL CURSOR)
                          # ==> BTW, LAS VELOCIDADES DISPONIBLES VAN DEL 1 AL 10.




# DIBUJAR UN CUADRADO:

# SIN FOR:
tortuga.forward(100)      # ==> UTILIZAMOS EL METODO (.forward(x)), PARA INDICAR CUANTO QUEREMOS QUE AVANCE AL FRENTE LA "Tortuga", "Forward = Adelante"
tortuga.right(90)         # ==> UTILIZAMOS EL METODO (.right(x)), PARA INDICAR QUE QUERMOS QUE GIRE A LA DERECHA CON EL VALOR DE 90, EN ESTE CASO SON GRADOS, (YA QUE ES UN GIRO)
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90) 
tortuga.forward(100)
tortuga.right(90) 
 

# CON FOR:
for _ in range(4):
    tortuga.forward(100)      
    tortuga.right(90)


# MODIFICAR EL COMPORTAMIENTO DE LA VENTANA: USAMOS EL METODO ".exitonclick()", EN NUESTRA VARIABLE "ventana", PARA QUE NO SE CIERRE AUTOMATICAMENTE
ventana.exitonclick()