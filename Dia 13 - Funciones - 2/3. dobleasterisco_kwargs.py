# KEYWORD ARGUMENTS (**kwargs): SON UTILIES CUANDO TIENES UNA FUNCION CON ARGUMENTOS OPCIONALES O CUANDO DESEAS HACER QUE EL CODIGO SEA MAS LEGIBLE
# Y EXPLICITO AL LLAMAR A LA FUNCION, YA QUE SE PUEDEN ESPECIFICAR LOS NOMBRES DE LOS ARGUMENTOS JUNTO CON SUS VALORES CORRESPONDIENTES.

def conectar_bd(**kwargs): # (**kwargs): PERMITE INGRESAR COMO ARGUMENTO UNA LLAVE Y UN VALOR, EJEMPLO: id=1 o contraseña='holacomoestas123'
      print(type(kwargs))  # ==> "(def nombre_funcion(**kwargs):" CONVIERTE TODOS LOS ARGUMENTOS EN UN DICCIONARIO, SIN OLVIDAR QUE ESTO SE PUEDE HACER LA n CANTIDAD DE VECES
      print(kwargs)


      
# PRACTICA TEORICA: CONECTARSE A UNA BASE DE DATOS

def conectar_db(**kwargs):
      # Primera opcion para acceder a los valores del diccionario (Llamar la llave y usar la funcion .get())
      nombre = kwargs['nombre_db'] # ==> EN ESTE DICCIONARIO 'kwargs', VA A BUSCAR EL VALOR DE LA LLAVE 'nombre_db', EL CUAL ES 'ferreteria_gym'
      usuario = kwargs['user']
      contrasena = kwargs['password']
      puerto = kwargs.get('port','puerto por defecto') # ==> SI QUIERO QUE ESTE ARGUMENTO SEA OPCIONAL DEBO USAR LA FUNCION '.get()', EN ESTE CASO, SE NECESITAN DOS ARGUMENTOS 
      direccion = kwargs['dir_db']                     #     EN LA FUNCION, EL PRIMERO ES LA LLAVE QUE QUEREMOS HACER OPCIONAL Y EL SEGUNDO ES EL VALOR QUE LE ASIGNAREMOS POR DEFECTO SI NO TIENE UNO.
      print(f"Conectando con la base de datos: '{nombre}', con el usuario: '{usuario}' y la contraseña: '{contrasena}' en el puerto: {puerto}.")

conectar_db(nombre_db='ferreteria_gym',
            user='root',
            password='123',
            #port='5003',
            dir_db='10.105.95.3')