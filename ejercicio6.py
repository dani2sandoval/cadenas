#primero almacenamos una frase a una variable
frase1 = input("ingresa una frase: ")

#se almacena la vocal que se introduce en una varible
vocal = input("ingresa una vocal: ")

#se convierte la vocal introducida a mayusculas con .upper()
vocalenmayusculas = vocal.upper()

#se reemplaza las vocales minusculas por mayusculas con .replace()
frase2 = frase1.replace(vocal, vocalenmayusculas)

#impresion
print("la frase con las vocales en mayuscula es: ", frase2)