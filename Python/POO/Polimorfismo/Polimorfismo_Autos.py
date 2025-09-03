import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

import tabulate

class Vehiculo:
    def __init__ (self, marca, modelo, matricula, color):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.color = color
    
    def Mostrar_informacion(self):
        pass

class Auto(Vehiculo):

    def mostrar_informacion(self):
        linea_separadora = "-" * 80
        print(linea_separadora)
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Matrícula: {self.matricula}")
        print(f"Color: {self.color}")
        print("Tipo de vehículo: Auto")
        print("Características adicionales: 4 ruedas, motor de combustión interna")
        print(linea_separadora)

class Moto(Vehiculo):

    def mostrar_informacion(self):
        linea_separadora = "-" * 80
        print(linea_separadora)
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Matrícula: {self.matricula}")
        print(f"Color: {self.color}")
        print("Tipo de vehículo: Moto")
        print("Características adicionales: 2 ruedas, motor de combustión interna")
        print(linea_separadora)

class Camion(Vehiculo):
    
    def mostrar_informacion(self):
        linea_separadora = "-" * 80
        print(linea_separadora)
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Matrícula: {self.matricula}")
        print(f"Color: {self.color}")
        print("Tipo de vehículo: Camión")
        print("Características adicionales: 6 ruedas, motor de combustión interna")
        print(linea_separadora)

def mostrar_informacion_vehiculo(vehiculo):
    vehiculo.mostrar_informacion()

def seleccionar_vehiculo():
    vehiculos = {1: "Auto", 2: "Moto", 3: "Camión"}
    print(f"Seleccione el tipo de vehículo \n{tabulate.tabulate(vehiculos.items(), headers=['Número', 'Tipo de Vehículo'], tablefmt='grid')}")
    while True:
        try:
            opcion = int(input("Ingrese el número de la opción: "))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            input("Presione Enter para continuar...")
            clear()
            continue
        if opcion in vehiculos:
            print(f"Usted ha seleccionado: {vehiculos[opcion]}")
            input("Presione Enter para continuar...")
            clear()
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            clear()
    return opcion

opcion = seleccionar_vehiculo()
if opcion == Auto: 
    auto = Auto("Toyota", "Corolla", "ABC123", "Rojo")
    mostrar_informacion_vehiculo(auto)

elif opcion == Moto:
    moto = Moto("Honda", "CBR80R", "XYZ789", "Negro")
    mostrar_informacion_vehiculo(moto)

else:
    camion = Camion("Mercedes-Benz", "Actros", "LMN456", "Blanco")
    mostrar_informacion_vehiculo(camion)
