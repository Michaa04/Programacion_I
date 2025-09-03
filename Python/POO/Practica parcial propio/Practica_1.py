#Practica 1: Clase simple
"""
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def ingresar_producto(self):
        self.nombre = input("Ingresar nombre del producto:")
        self.precio = int(input("Ingresar precio:"))
        return self.nombre, self.precio
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, y su precio: ${self.precio}.")
    

Perfume = Producto("micha", 34)
Perfume.ingresar_producto()
Perfume.mostrar_info()
"""

#Practica 2: Encapsulamiento
"""
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self):
        monto = int(input("Ingresar monto a depositar: $"))
        if monto > 0:
            self.__saldo = self.__saldo + monto
            print(f"Se deposito ${monto} y su nuevo saldo es: ${self.__saldo}.")
        else: 
            print("Monto no valido.")
    
    def retirar(self):
        monto = int(input("Ingresa monto a retirar: $"))
        if monto <= self.__saldo:
            self.__saldo = self.__saldo - monto
            print(f"Se retiro ${monto} y su nuevo saldo es: ${self.__saldo}.")
        else: 
            print("Saldo insuficiente.")

    def ver_saldo(self):
        print("Visualizar saldo")
        print(f"Saldo disponible: ${self.__saldo}")

macro = CuentaBancaria(12000)
macro.depositar()
macro.retirar()
macro.ver_saldo()
"""

# Practica 3: Herencia
"""
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def Ingresar_empleado(self):
        self.nombre = input("Ingresar nombre:")
        self.salario = int(input("Ingresar salario: $"))
        if self.salario > 0:
            return self.nombre, self.salario 
        else:
            print("No valido.")
    
    def mostrar_info(self):
        print("Empleado")
        print(f"Nombre: {self.nombre}")
        print(f"Salario: ${self.salario}")

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def Ingresar_departamento(self):
        self.departamento = input("Ingresar departamento:")
        return self.departamento
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Departamento: {self.departamento}")

    
persona = Gerente("Micha", 120000, "Ventas")
persona.Ingresar_empleado()
persona.mostrar_info()
persona.Ingresar_departamento()
persona.mostrar_info()
"""
#Practica 4: Herencia + Polimorfismo
"""
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.animales = []

    def ingresar_animal(self):
        self.nombre = input("Ingresar nombre del animal:")
        self.edad = int(input("Ingresar edad:"))
        nuevo_animal = {
            "Nombre": self.nombre,
            "Edad": self.edad
        }
        self.animales.append(nuevo_animal)
        return self.animales
    
    def hacer_sonido(self):
        print(f"El animal {self.nombre} hace un ruido.")

    def mostrar_info(self):
        print("Animal")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

class Perro(Animal):
    def hacer_sonido(self):
        super().hacer_sonido()
        print("Guau")

class Gato(Animal):
    def hacer_sonido(self):
        super().hacer_sonido()
        print("Miuau")

marco = Perro("Micha", 13)
marco.ingresar_animal()
marco.mostrar_info()
marco.hacer_sonido()

marca = Gato("MIMI", 12)
marca.ingresar_animal()
marca.mostrar_info()
marca.hacer_sonido()
"""

#Practica 5: Composicion(clase dentro de clase)
"""
class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def mostrar_info(self):
        print("Libros")
        print(f"Titulo: {self.titulo}.")
        print(f"Autor: {self.autor}.")
        print(f"Año: {self.año}")

class Biblioteca:
    def __init__(self):
        self.libros = [] 
        pass

    def agregar_libro(self):
        Titulo = input("Ingresar titulo del libro:")
        Autor = input("Ingresar autor del libro:")
        Año = input("Ingresar año del libro:")
        nuevo_libro = Libro(Titulo, Autor, Año)
        self.libros.append(nuevo_libro)

    def mostrar_libros(self):
        print("Libros en la biblioteca")
        for libro in self.libros:
            libro.mostrar_info()

biblioteca1 = Biblioteca()
biblioteca1.agregar_libro()
biblioteca1.mostrar_libros()
"""
#Practica 6: Encapsulamiento + metodos de acesso(getter y setter)
#Sistema de gestion de usuario
"""
class Usuario:
    def __init__(self, nombre, email, clave):
        self.__nombre = nombre
        self.__email = email
        self.__clave = clave

    def ver_info(self):
        print("Información del usuario:")
        print(f"Nombre: {self.__nombre}")
        print(f"Email: {self.__email}")

    def verificar_clave(self, intento):
        return self.__clave == intento

    def cambiar_clave(self, clave_actual, nueva_clave):
        if self.__clave == clave_actual:
            self.__clave = nueva_clave
            print("Clave actualizada correctamente.")
        else:
            print(" Clave incorrecta. No se pudo actualizar.")


usuarios = []

nombre = input("Ingresar nombre:")
email = input("Ingresar email:")
clave = int(input("Ingresar clave:"))

usuario1 = Usuario(nombre,email, clave)
usuarios.append(usuario1)

usuario1.ver_info()
 
print("Verificar clave")
intento = int(input("Ingresar clave (solo numerico):"))
if  usuario1.verificar_clave(intento):
    print("Clave correcta")
else:
    print("Clave incorrecta")

clave_actual = int(input("Ingresar clave (solo numerico):"))
nueva_clave = int(input("Ingresar nueva clave (solo numerico):"))
usuario1.cambiar_clave(clave_actual, nueva_clave)
"""
#Practica 7: Composición de Clases: Usuario y Tarjeta
"""
class Tarjeta:
    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo

    def Ver_saldo(self):
        print(f"Saldo Disponible: {self.__saldo}")

    def cargar_saldo(self):
        print("Ingresar saldo")
        monto = int(input("Ingresar monto a despositar:"))
        if monto >= 0:
            self.__saldo = self.__saldo + monto
            print(f"Se deposito {monto}.")
        else:
            print("Monto no valido.") 

    def pagar(self):
        print("Realiza un pago")
        monto = int(input("Ingresar monto a pagar:"))
        if monto <= self.__saldo:
            self.__saldo = self.__saldo - monto
            print(f"Se realizo el pago, queda disponible: {self.__saldo}")

class Usuario:
    def __init__(self, nombre, email, tarjeta):
        self.nombre = nombre
        self.email = email
        self.tarjeta = tarjeta

    def Ingresar_datos(self):
        print("Ingresar datos")
        self.nombre = input("Ingresar nombre:")
        self.email = input("Ingresar email:")
        return self.nombre, self.email
    
    def ver_info(self):
        print("Ver usuario")
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")

    def ver_tarjeta(self):
        print("Ver tarjeta")
        print(f"n°: {self.tarjeta}")

class Tarjeta:
    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo

    def Ver_saldo(self):
        print(f"Saldo Disponible: {self.__saldo}")

    def cargar_saldo(self):
        print("Ingresar saldo")
        monto = int(input("Ingresar monto a despositar:"))
        if monto >= 0:
            self.__saldo = self.__saldo + monto
            print(f"Se deposito {monto}.")
        else:
            print("Monto no valido.") 

    def pagar(self):
        print("Realiza un pago")
        monto = int(input("Ingresar monto a pagar:"))
        if monto <= self.__saldo:
            self.__saldo = self.__saldo - monto
            print(f"Se realizo el pago, queda disponible: {self.__saldo}")

class Usuario:
    def __init__(self, nombre, email, tarjeta):
        self.nombre = nombre
        self.email = email
        self.tarjeta = tarjeta

    def Ingresar_datos(self):
        print("Ingresar datos")
        self.nombre = input("Ingresar nombre:")
        self.email = input("Ingresar email:")
        return self.nombre, self.email
    
    def ver_info(self):
        print("Ver usuario")
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")

    def ver_tarjeta(self):
        print("Ver tarjeta")
        
macro = Tarjeta("235", 100000)

usuario = Usuario("fsdf", "ff", macro)
usuario.Ingresar_datos()
usuario.ver_info()
usuario.ver_tarjeta()
usuario.tarjeta.cargar_saldo()
usuario.tarjeta.Ver_saldo()
usuario.tarjeta.pagar()
usuario.tarjeta.Ver_saldo()
"""
#Practica 8: Sistema de Cursos y Estudiantes (Composicion + encapsulamiento)
class Curso:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def mostrar_info(self):
        print("Mostrar info")
        print(f"Nombre: {self.nombre}")
        print(f"Codigo: {self.codigo}")

class Estudiante(Curso):
    def __init__(self, nombre, legajo):
        self.nombre = nombre
        self.legajo = legajo
        self.cursos = []

    def Incribirse(self):
        print("Incribir alumno")
        nombre = input("Ingresar nombre:")
        legajo = input("Ingresar legajo:")
        Estudiante1 = Estudiante(nombre, legajo)
        return Estudiante1

    def mostrar_cursos(self):
        print("Mostrar cursos")
        for curso in self.cursos:
            print(curso)

    
ark = Estudiante()
ark.mostrar_info()

 


