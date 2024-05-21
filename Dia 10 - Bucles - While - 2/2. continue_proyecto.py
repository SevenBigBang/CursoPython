import random
import turtle

ventana = turtle.Screen()
ventana.title("Carrera de Caracoles")
ventana.bgcolor("lightblue")
ventana.setup(width=800, height=600)

caracol_1 = turtle.Turtle()
caracol_1.shape("turtle")
caracol_1.color("red")
caracol_1.penup()
caracol_1.goto(-300, 50)

caracol_2 = turtle.Turtle()
caracol_2.shape("turtle")
caracol_2.color("blue")
caracol_2.penup()
caracol_2.goto(-300, -50)

meta =  500
# DIBUJAR LINEA DE META:
meta_linea = turtle.Turtle()
meta_linea.penup()
meta_linea.goto(meta, 150)
meta_linea.pendown()
meta_linea.goto(meta, -150)
meta_linea.hideturtle()

# SE MODIFICA LA CARRERA DE CARACOLES CON "continue", PARA QUE SOLO AVANCEN SI SACAN UN NUMERO IMPAR 

while True:
    avance_caracol_1 = random.randint(1, 13)
    avance_caracol_2 = random.randint(1, 13)
    if avance_caracol_1 % 2 == 0 or avance_caracol_2 % 2 == 0: # ==> EN ESTA CONDICIONAL SE ESTABLECE SI LOS AVANCES SON PARES SE OMITA 
        continue    # ==> ESTA LINEA SE APLICA "continue", LO QUE OMITE EL CODIGO
    caracol_1.forward(avance_caracol_1)
    caracol_2.forward(avance_caracol_2)

    print(f"Avance del caracol 1: {avance_caracol_1}, para un total de: {caracol_1.xcor()}")
    print(f"Avance del caracol 2: {avance_caracol_2}, para un total de: {caracol_2.xcor()}")
    print("-----------------------------------------")    

    if caracol_1.xcor() >= meta or caracol_2.xcor() >= meta:
        break

if caracol_1.xcor() > caracol_2.xcor():
    print("El caracol 1 ha ganado")
elif caracol_2.xcor() > caracol_1.xcor():
    print("El caracol 2 ha ganado")
else:
    print("Esto es un empate")

ventana.exitonclick()

