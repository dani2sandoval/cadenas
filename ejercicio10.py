#se almacenan los productos en una variable
productos = input('productos: ')

#se separan todos los productos en base al punto y espacio
partes = productos.split(", ")

#Impresion en cadena con un for
for parte in partes:
    print(parte)