#Herencia de clase simple (Concesionario de vehiculos)

class auto:
    def __init__(self, marca, modelo, placa, tipo_gasolina, motor, precio):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.tipo_gasolina = tipo_gasolina
        self.motor = motor
        self.precio = precio
        
    def descripcion(self):
        return "El vehiculo es marca {}, modelo {}, su placa es {}, su tipo de gasoil es {}, con un motor {} con un precio de ${}".format(self.marca, self.modelo, self.placa, self.tipo_gasolina, self.motor, self.precio)

    
Corolla = auto("Toyota", 2009, "123-ABC", "Naftero", 1.8, 1000000)
print(Corolla.descripcion())
