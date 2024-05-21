# CREAR FUNCIONES PARA SUMAR Y RESTAR:

def sumar():
    while True:
        num1 = int(input("¿Cual es el numero a sumar?: "))
        num2 = int(input("¿Cual es el siguiente numero a sumar?: "))
        resultado = num1 + num2
        print(f"\nEl resultado es: {resultado}.\n")
        if num1 != int or num2 != int:
            break
        


def restar():
    while True:
        num1 = int(input("¿Cual es el numero a restar?: "))
        num2 = int(input("¿Cual es el siguiente numero a restar?: "))
        resultado = num1 - num2
        print(f"\nEl resultado es: {resultado}.\n")
        if num1 != int or num2 != int:
            break
    