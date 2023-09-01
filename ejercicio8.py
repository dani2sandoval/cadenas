#se almacena el correo en una variable
precio = input('precio: ')

#se separa el euro y los centimos a partir del punto
partes = precio.split('.')

#se asigna la parte 1 a la variable del euro
euro = partes[0]

#se asigna la parte 2 a la variable de los centimos
centimos = partes[1]

#impresion
print(euro, "euros y ", centimos, " centimos")