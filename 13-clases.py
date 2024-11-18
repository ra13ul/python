class Vehiculo():

    def __init__(self, color, ruedas):
        self.color=color
        self.ruedas=ruedas
    
    def __str__(self):
        return 'Color: ' + self.color + ', Ruedas: ' + str(self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ', Velocidad: ' + str(self.velocidad) + ' (km/h)'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + ', tipo: ' + self.tipo + '.'

# Creamos un objeto de la clase Vehiculo   
vehiculo1 = Vehiculo('Rojo', 4)
print(vehiculo1)

# Creamos un objeto de la clase hija Coche 
coche = Coche('Azul', 4, 150)
print(coche)

# Creamos un objeto de la clase hija Bicicleta
bici = Bicicleta('Blanca', 2, 'Urbano')
print(bici)