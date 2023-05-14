"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class CalcularFactura():
    def __init__(self, nombre, apellido, obj, c, p):
        self.nombre = nombre
        self.apellido = apellido
        self.objeto = obj
        self.cedula = c
        self.precio = p


    def calcular(self):
        self.valorFinal = (self.precio * 0.12) + self.precio

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nObjeto adquirido: {self.objeto}\n" \
               f"Cedula: {self.cedula}\nPrecio: {self.precio}\nprecio final con IVA aplicado: {self.valorFinal}\n"


# clase 02
class Cliente():
    def __init__(self, n, a, c, mc):
        self.nombre = n
        self.apellido = a
        self.cedula = c
        self.minutosConsumidos = mc

    def calcular(self):
        self.valoraPagar = (self.minutosConsumidos * 0.25)

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nCedula: {self.cedula}\n\
minutos consumindos en el mes: {self.minutosConsumidos}\nvalor a pagar: {self.valoraPagar}\n"