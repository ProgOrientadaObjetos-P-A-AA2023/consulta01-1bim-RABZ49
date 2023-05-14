"""

"""
# Crear dos objetos de la clase 01

# objeto 01

# crear

# Presentar objeto; usar el método __st__

# objeto 02

# crear ingresando valores por teclado

# Presentar objeto; usar el método __st__

from mis_clases import Cliente

print("\nIngrese datos para el primer Objeto")
nombre = input("Ingrese sus nombres: ")
apellido = input("Ingrese sus apellidos: ")
cedula = input("Ingrese su identificacion: ")
minutosConsumidos =  float(input("Ingrese los minutos consumidos al mes: "))


cliente = Cliente(nombre, apellido, cedula, minutosConsumidos)
cliente.calcular()

print(cliente)