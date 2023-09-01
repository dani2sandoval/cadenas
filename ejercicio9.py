#se almacena la fecha en una variable
cumple = input('ingrese su fecha de cumpleaños: ')

#se separan los dias, meses y años en base a la diagonal
partes = cumple.split('/')

#se asigna la parte del dia a una variable
dia = partes[0]

#se asigna la parte del mes a una variable
mes = partes[1]

#se asigna la parte del año a una variable
año = partes[2]

#impresion
print("dia:", dia)
print("mes:", mes)
print("año:", año)