"""

"""
# Crear dos objetos de la clase 02

# objeto 01

# crear

# Presentar objeto; usar el método __st__

# objeto 02

# crear ingresando valores por teclado

# Presentar objeto; usar el método __st__

from mis_clases import CalcularFactura

print("\nIngrese datos para el segundo Objeto")
nombre = input("Ingrese sus nombres: ")
apellido = input("Ingrese sus apellidos: ")
objeto = input("ingrese el nombre del objeto comprado: ")
cedula = input("Ingrese su identificacion: ")
precio = int(input("Ingrese el precio del producto: "))



cliente = CalcularFactura(nombre, apellido, objeto,  cedula, precio)
cliente.calcular()

print(cliente)