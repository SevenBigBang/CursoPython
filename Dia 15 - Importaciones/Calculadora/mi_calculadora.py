# YA QUE CREAMOS NUESTROS MODULOS AHORA HAY QUE IMPORTARLOS: PARA ESTO PYTHON CUENTA CON ALIAS DE ESTA FORMA USAREMOS LA PALABRA RESERVADA "as", PARA USAR MEJOR LAS IMPORTACIONES;

import Aritmeticas.operaciones_basicas as ob # ==> "ob" COMO OPERACIONES BASICAS. PUEDE SER CUALQUIER OTRO NOMBRE
import Aritmeticas.operaciones_avanzadas as oa

#resultado = ob.sumar(2, 4, 8, 5, 6) # ==> DE ESTA FORMA ACCEDEMOS CON EL ALIAS EN ESTE CASO "ob", Y USAMOS '.' PARA ACCEDER A LAS FUNCIONES DEL MODULO, EN ESTE CASO
#print(resultado)                    #     Sumar y Restar

#resultado_2 = ob.restar(8,6)
#print(resultado_2)

#resultado_3 = oa.multiplicar(5, 5)
#print(resultado_3)

#resultado_4 = oa.dividir(8, 2)
#print(resultado_4)

# CALCULADORA:s
print("------------------------------------------")
print("           CALCULADORA MASTER             ")
print("------------------------------------------")
while True:
    try:
        decision = int(input("¿Que quieres hacer hoy?\n\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir\n\n¿Cual es tu decisión?: "))
        match decision:
            case 1:
                ob.sumar()
            case 2:
                ob.restar()
            case 3:
                oa.multiplicar()
            case 4:
                oa.dividir()
            case 5:
                break
            case _:
                print("Esa no es una opcion valida.")
    except ValueError as e:
        print(f"Error de valor, ingresa numeros unicamente")
