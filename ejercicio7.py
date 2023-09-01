#se almacena el correo en una variable
correo = input("ingresa tu correo electrónico: ")

#se separa el correo en dos partes a partir del arroba
partes = correo.split("@")

#se define el dominio nuevo
dominio = "miumg.edu.gt"

#se crea un nuevo correo en la variable correo2 pero que reemplzará la segunda parte
#con el nuevo dominio
correo2 = correo.replace(partes[1], dominio)

#impresion
print("su correo es: ", correo2)