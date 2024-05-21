# WHILE: SE UTILIZA PARA REPETIR N CANTIDAD DE TAREAS N CANTIDAD DE VECES MIENTRAS SE CUMPLA UNA CONDICION

# SE USA SIEMPRE Y CUANDO NO ESTES SEGURO DE CUANTAS VECES VAS A ITERAR UNA TAREA, SI YA CONOCES CUANTAS VECES LO HARAS USAR MEJOR UN CICLO FOR

# EJEMPLO DE USO WHILE ENVIANDO MENSAJES:
condicion_salida = "CONTINUE"

while condicion_salida == "CONTINUE":
    nombre = input("Cual es tu nombre?: ")
    correo = input("Cual es tu correo electronico?: ")
    mensaje = input("Cual es tu mensaje?: ")

    print(f"""
        Mensaje enviado a: {nombre}

        Destinatario: {correo}

        Mensaje enviado: {mensaje}
        """)
    
    condicion_salida = input('En caso de querer continuar con el programa escriba "CONTINUE": ')