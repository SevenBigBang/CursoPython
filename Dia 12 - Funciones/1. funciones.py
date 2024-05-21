# FUNCIONES: SE USA PARA CONTENER LA LOGICA DE UN PROGRAMA CONTENIDA EN UNA "CAJA", LA CUAL LLAMAREMOS LAS VECES QUE QUERRAMOS PARA USAR ESA LOGICA SIN TENER QUE ESCRIBIRLA NUEVAMENTE:

def saludar_usuario(): # ==> EL NOMBRE DEBERIA SER UN VERBO, PARA QUE SEA MAS ENTENDIBLE
    nombre = input("Cual es tu nombre?: ")
    print(f"Hola, {nombre}, ¿Como te encuentras hoy?")


saludar_usuario() # ==> DE ESTA FORMA SE LLAMA A LA FUNCION PREVIAMENTE CREADA: "nombre_funcion(x)", (EL PARAMETRO ES OPCIONAL)




# PARAMETROS EN LAS FUNCIONES: CALCULADORA CON FUNCIONES (PARAMETROS PREDETERMINADOS)
def sumar(n1, n2):
    print("La suma es: ", n1 + n2)
def restar(n1, n2):
    print("La resta es: ", n1 - n2)
def multiplicar(n1, n2):
    print("La suma es: ", n1 * n2)
def dividir(n1, n2):
    print("La suma es: ", n1 / n2)


print("--------------------CALCULADORA--------------------")
decision = int(input("¿Que quieres hacer?:\n1. Sumar\n2. Restar\n3. Multiplicación\n4. División\n¿Que decides?: "))
match decision:
    case 1:
        sumar(15, 20)
    case 2:
        restar(15, 20)
    case 3:
        multiplicar(15, 20)
    case 4:
        dividir(15, 20)
    case _:
        print("Eso no era una opción tonoto")




# PARAMETROS EN LAS FUNCIONES: CALCULADORA CON FUNCIONES SIN PARAMETROS:

def sumar():
    n1 = int(input("¿Cual es tu primer numero?: "))
    n2 = int(input("¿Cual es tu segundo numero?: "))
    total = n1 + n2
    print(f"La suma es: {total}")
def restar():
    n1 = int(input("¿Cual es tu primer numero?: "))
    n2 = int(input("¿Cual es tu segundo numero?: "))
    total = n1 - n2
    print(f"La resta es: {total}")
def multiplicar():
    n1 = int(input("¿Cual es tu primer numero?: "))
    n2 = int(input("¿Cual es tu segundo numero?: "))
    total = n1 * n2
    print(f"La multiplicación es: {total}")
def dividir():
    n1 = int(input("¿Cual es tu primer numero?: "))
    n2 = int(input("¿Cual es tu segundo numero?: "))
    total = n1 / n2
    print(f"La division es: {total}")


print("--------------------CALCULADORA--------------------")
decision = int(input("¿Que quieres hacer?:\n1. Sumar\n2. Restar\n3. Multiplicación\n4. División\n¿Que decides?: "))
match decision:
    case 1:
        sumar()
    case 2:
        restar()
    case 3:
        multiplicar()
    case 4:
        dividir()
    case _:
        print("Eso no era una opción tonoto")


    

# PARAMETROS EN LAS FUNCIONES: CALCULADORA CON FUNCIONES SIN PARAMETROS Y CON CICLO WHILE:

while True:
    decision = int(input("\n¿Que quieres hacer?:\n1. Sumar\n2. Restar\n3. Multiplicación\n4. División\n5. Salir\n\n¿Que decides?: "))
    match decision:
        case 1:
            sumar()
        case 2:
            restar()
        case 3:
            multiplicar()
        case 4:
            dividir()
        case 5:
            break
        case _:
            print("Eso no era una opción tonoto")