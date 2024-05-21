# ARGUMENTOS OPCIONALES: PYTHON NOS DA LA POSIBLIDAD DE DARLE O NO ARGUMENTOS A UNA FUNCION LO CUAL LO HACE MUY DINAMICA
# EN ESTE EJEMPLO, VEREMOS COMO PODEMOS HACER UNA FUNCION QUE CALCULE EL PRECIO FINAL DEL PRODUCTO DEPENDIENDO SI EXISTE UN DESCUENTO(OPCIONAL)

productos = ['Manzana', 'Cereal', 'Cebolla', 'Arroz']

for producto in productos:
    print(f"- {producto}")

def calcular_precio(nombre_producto, cantidad, precio_u, descuento=0): # ==> DE ESTA FORMA HACEMOS QUE UN ARGUMENTO SEA OPCIONAL, AL DARLE UN ARGUMENTO CON VALOR PREDETERMIDADO
    total = (cantidad * precio_u)                                      #     EN ESTE CASO ES 0. 
    descuento_t = (total / 100) * descuento   
    total_desc = total - descuento_t                 
    print(f"El precio total a pagar para el producto {nombre_producto} es: {total} y con descuento es: {total_desc}")

calcular_precio("Cebolla", 4, 10000, 14)