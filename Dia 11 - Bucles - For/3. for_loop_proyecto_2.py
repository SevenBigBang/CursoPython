# EN EL PROYECTO 2 DIBUJAREMOS UN ESTRELLA DE 5 PUNTAS, USAREMOS CONOCIMIENTOS VISTOS PREVIAMENTES EN EL PROYECTO 1:
import turtle

ventana = turtle.Screen()
ventana.bgcolor("white")  
tortuga = turtle.Turtle() 
tortuga.speed(1)

for _ in range(5):
    tortuga.forward(300)
    tortuga.right(144)

ventana.exitonclick()