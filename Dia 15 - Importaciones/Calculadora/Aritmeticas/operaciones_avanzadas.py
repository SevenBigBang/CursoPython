# CREAR FUNCIONES PARA MULTIPLICAR Y DIVIDIR:
def multiplicar():
    while True:
        num1 = int(input("¿Cual es el numero a multiplicar?: "))
        num2 = int(input("¿Cual es el siguiente numero a multiplicar?: "))
        resultado = num1 * num2
        print(f"\nEl resultado es: {resultado}.\n")
        if num1 != int or num2 != int:
            break

def dividir():
    while True:
        num1 = int(input("¿Cual es el numero a dividir?: "))
        num2 = int(input("¿Cual es el siguiente numero a dividir?: "))
        resultado = num1 / num2
        print(f"\nEl resultado es: {resultado}.\n")
        if num1 != int or num2 != int:
            break