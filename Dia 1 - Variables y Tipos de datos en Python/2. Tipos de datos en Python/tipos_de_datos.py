# TIPOS DE DATOS: En programación, el tipo de datos es un concepto importante. Las variables pueden almacenar datos de diferentes tipos, y diferentes tipos pueden hacerlo cosas diferentes.
#                 Python tiene los siguientes tipos de datos integrados de forma predeterminada, en estas categorías:

# Tipo de texto: str
# Tipos numéricos: int, float, complex
# Tipos de secuencia: list, tuple, range
# Tipo de mapeo: dict
# Tipos de conjuntos: set, frozenset
# Tipo booleano: bool
# Tipos binarios: bytes, bytearray, memoryview
# Ninguno Tipo:	NoneType


# 1. Obtención del tipo de datos: Python puede obtener el tipo de datos de cualquier objeto mediante la función: type()
x = 5
print(type(x))



# 2. Establecer el tipo de datos: (En Python, el tipo de datos se establece cuando se asigna un valor a una variable)


# Example	                                             Data Type	

# x = "Hello World"	                                        str	
# x = 20	                                                int	
# x = 20.5	                                                float	
# x = 1j	                                                complex	
# x = ["apple", "banana", "cherry"]	                        list	
# x = ("apple", "banana", "cherry")	                        tuple	
# x = range(6)	                                            range	
# x = {"name" : "John", "age" : 36}	                        dict	
# x = {"apple", "banana", "cherry"}	                        set	
# x = frozenset({"apple", "banana", "cherry"})	            frozenset	
# x = True	                                                bool	
# x = b"Hello"	                                            bytes	
# x = bytearray(5)	                                        bytearray	
# x = memoryview(bytes(5))	                                memoryview	
# x = None	                                                NoneType





# Ejercicio:

# 1. En el siguiente ejemplo de código se imprimiría el tipo de datos de x, ¿qué tipo de datos sería?
x = 5
print(type(x))
# Tu respuesta: 

# 2. En el siguiente ejemplo de código se imprimiría el tipo de datos de x, ¿qué tipo de datos sería?
x = "Hello World"
print(type(x))
# Tu respuesta: 

# 3. En el siguiente ejemplo de código se imprimiría el tipo de datos de x, ¿qué tipo de datos sería?
x = {"name" : "John", "age" : 36}
print(type(x))
# Tu respuesta: 