# Sistemas de gestion de vehiculos
"""
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo 

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}.")
    
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_de_puertas):
        super().__init__(marca, modelo)
        self.numero_de_puertas = numero_de_puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Numero de puertas: {self.numero_de_puertas}.")

Auto = Automovil("Toyota", "Corolla", "3 puertas")
print(Auto.mostrar_info())
"""

#Sistema de gestion de empleados

class Empleado: 
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_informacion(self):
        self.nombre = input("Ingresar nombre:")
        self.salario = int(input("Ingresar salario: $"))
        print(f"Nombre: {self.nombre}, Salario: {self.salario}.")
    
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_informacion(self):
        super().mostrar_informacion()
        self.departamento = input("Ingresar departamento:")
        print(f"Nombre: {self.nombre}, Salario: {self.salario}, Departamento: {self.departamento}")
    
Persona = Gerente("Michael", 4000, "Ventas")
Persona.mostrar_informacion()
    