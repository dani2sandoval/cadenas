#variable a la que el ususario le atribuye el valor con su nombre
nombre = input("ingresa tu nombre: ")

#transformamos el nombre a mayusculas en una nueva variable usando .upper
mayusculas = nombre.upper()

#transformamos el nombre a minusculas en una nueva variable usando .lower
minusculas = nombre.lower()

#transformamos el nombre a tipo titulo en una nueva variable usando .title
iniciales = nombre.title()

#ipmresion de el nombre en cada una de sus formas
print("nombre en MAYUSCULAS: ", mayusculas)
print("NOMBRE EN minusculas: ", minusculas)
print("Nombre Con Las Iniciales En Mayusculas: ", iniciales)