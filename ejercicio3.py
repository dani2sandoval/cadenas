#variable a la que el usuario le atribuye el valor con su nombre
nombre = input("ingresa tu primer nombre: ")

#transformamos el nombre a mayusculas con .upper()
mayusculas = nombre.upper()

#para contar cuantas letras tiene un nombre se usa la funcion len() que cuenta los caracteres incluidos los espacios
caracteres = len(mayusculas)

#impresion
print(mayusculas, "tiene", caracteres, "letras")

