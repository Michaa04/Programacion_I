#Practica 1: sistema de gestion de vehiculos(Contiene todos los pilares)

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca 
        self.modelo = modelo
        self.año = año 
        self.vehiculos = []

    def mostrar_info(self):
        print("Vehiculo")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")

    def sonido(self):
        return f"Sonido de motor."

class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas

    def ingresar_auto(self):
        print("Ingresar auto")
        self.marca = input("Ingresar marca:")
        self.modelo = input("Ingresar modelo:")
        self.año = int(input("Ingresar año:"))
        self.puertas = int(input("Ingresar cantidad de puertas:"))
        auto1 = {
            "Marca": self.marca,
            "Modelo": self.modelo,
            "Año": self.año,
            "Puertas": self.puertas
        }
        self.vehiculos.append(auto1)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Puertas {self.puertas}")

    def sonido(self):
        super().sonido()
        print("Bum bum.")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def ingresar_moto(self):
        print("Ingresar auto")
        self.marca = input("Ingresar marca:")
        self.modelo = input("Ingresar modelo:")
        self.año = int(input("Ingresar año:"))
        self.cilindrada = int(input("Ingresar cantidad de puertas:"))
        motito1 = {
            "Marca": self.marca,
            "Modelo": self.modelo,
            "Año": self.año,
            "Cilindrada": self.cilindrada
        }
        self.vehiculos.append(motito1)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindrada: {self.cilindrada}")

    def sonido(self):
        super().sonido()
        print("RUN RUN")

def menu_principal():
    while True:
        print("Menu principal")
        print("1.Registrar auto")
        print("2.Registrar moto:")
        print("3.Mostrar info de auto")
        print("4.Mostrar info de moto")
        print("5.Sonido de auto")
        print("6.Sonido de moto")
        print("0.Salir")
        opcion1 = int(input("Ingrese una opcion:"))
        if opcion1 == 1:
            Auto.ingresar_auto()
            continue
        elif opcion1 == 2:
            Moto.ingresar_moto()
            continue
        elif opcion1 == 3:
            Auto.mostrar_info()
            continue
        elif opcion1 == 4:
            Moto.mostrar_info()
            continue
        elif opcion1 == 5:
            Auto.sonido()
            continue
        elif opcion1 == 6:
            Moto.sonido()
            continue
        elif opcion1 == 0:
            exit()
        else: 
            print("Opcion incorrecta.")

menu_principal()



