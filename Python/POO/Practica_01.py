#Ejercicio 1
#Crear una clase
#Consigna: Define una clase llamada Animal con un atributo nombre. Luego, crea una
#instancia de la clase y muestra el nombre.
"""
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

Perro = Animal("Benito")
print(Perro.nombre)
"""
#Ejercicio 2
#Añadir un método
#Consigna: Añade un método llamado hacer_sonido a la clase Animal que imprima un sonido.
"""
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("Ladrido")

Perro = Animal("Benito")
print(Perro.nombre)
Perro.hacer_sonido()
"""
#Ejercicio 3: Atributos adicionales
#Consigna: Añade un atributo edad a la clase Animal y muestra tanto el nombre como la
#edad del animal.
"""
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("Ladrido")

Perro = Animal("Benito", 8)
print(Perro.nombre)
print(Perro.edad)
"""
#Ejercicio 4: Método que usa atributos
#Consigna: Añade un método llamado descripcion que devuelva una cadena con el
#nombre y la edad del animal.
"""
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("Ladrido")

    def descripcion(self):
        return "El perro llamado {} tiene la edad de {} años.".format(self.nombre, self.edad)
    
Perro = Animal("Benito", 8)
print(Perro.descripcion())
"""
#Ejercicio 5: Modificar atributos
#Consigna: Añade un método llamado cumplir_años que incremente la edad del animal en 1.
"""
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("Ladrido")

    def descripcion(self):
        return "El perro llamado {} tiene la edad de {} años.".format(self.nombre, self.edad)
    
    def cumplir_años(self):
        return "El perro en los proximos dias cumple la edad de {} años.".format(self.edad +1)

Perro = Animal("Benito", 8)
print(Perro.descripcion())
print(Perro.cumplir_años())
"""
#Ejercicio 6: Clase base y clase derivada
#Consigna: Crea una clase base Animal con un método hablar. Luego, crea una clase
#derivada Perro que herede de Animal y sobreescriba el método hablar.
"""
class Animal:
    def hablar(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def hablar(self):
        print("El perro dice: ¡Guau!")

Perro1 = Perro()
print(Perro1.hablar())
"""
#Ejercicio 7: Herencia y atributos
#Consigna: Crea una clase base Vehiculo con un atributo marca. Luego, crea una clase
#derivada Coche que herede de Vehiculo y tenga un atributo adicional modelo.
"""
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

class Coche(Vehiculo):
    def descripcion (self, modelo):
        return "El coche es marca {} y modelo {}.".format(self.marca, modelo)
    
Nuevo_vehiculo = Coche("Chevrolet")
print(Nuevo_vehiculo.descripcion(2012))
"""
#Ejercicio 8: Métodos adicionales en la clase derivada
#Consigna: Crea una clase base Persona con un método saludar. Luego, crea una clase
#derivada Estudiante que herede de Persona y tenga un método adicional estudiar.
"""
class Persona:
    def Saludar(self):
        print("Saludando...")

class Estudiante(Persona):
    def Estudiar(self):
        print("Estudiando...")

Estudiante1 = Estudiante()
Estudiante1.Saludar()
Estudiante1.Estudiar()
"""
#Ejercicio 9: Herencia y métodos sobrescritos
#Consigna: Crea una clase base Figura con un método area. Luego, crea una clase derivada
#Cuadrado que herede de Figura y sobrescriba el método area.
"""
class Figura:
    def area(self):
        print("El area despejada")
class Cuadrado:
    def area(self):
        print("El area es cuadrada")

Figura1 = Cuadrado()
Figura1.area()
"""
#Ejercicio 10: Herencia y uso de super()
#Consigna: Crea una clase base Empleado con un método trabajar. Luego, crea una clase
#derivada Gerente que herede de Empleado y use super() para llamar al método trabajar.
"""
class Empleado:
    def trabajar(self):
        return "El empleado esta trabajando"

class Gerente(Empleado):
    def trabajar(self):
        tarea_base = super().trabajar()
        return f"{tarea_base} ademas, el gerente esta supervisando al equipo."
    
Empleado1 = Empleado()
Gerente1 = Gerente()

print(Empleado1.trabajar())
print(Gerente1.trabajar())
"""
#Ejercicio 11: Herencia y inicialización de atributos
#Consigna: Crea una clase base Producto con un atributo nombre. Luego, crea una clase
#derivada Electronico que herede de Producto y tenga un atributo adicional precio.
"""
class Producto:
    def __init__(self, nombre):
        self.nombre = nombre

class Electronico(Producto):
    def precio(self, precio):
        return "El producto {} tiene un precio de {}.".format(self.nombre, precio)
    
Telefono1 = Electronico("Telefono")
print(Telefono1.precio(5000))
"""
#Ejercicio 12: Herencia y métodos adicionales
#Consigna: Crea una clase base Instrumento con un método tocar. Luego, crea una clase
#derivada Guitarra que herede de Instrumento y tenga un método adicional afinar.
"""
class Instrumento:
    def tocar(self):
        return "Se esta tocando el instrumento "
    
class Guitarra(Instrumento):
    def afinar(self):
        return "La guitarra se debe afinar"


Guitarra1 = Guitarra()
print(Guitarra1.tocar())
print(Guitarra1.afinar())
"""
#Ejercicio 13: Herencia y atributos adicionales
#Consigna: Crea una clase base Libro con un atributo titulo. Luego, crea una clase derivada
#Ebook que herede de Libro y tenga un atributo adicional formato.
"""
class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
    
class Ebook(Libro):
    def caracteristicas(self, formato):
        return "El libro tiene como titulo {} y tiene un formato {}.".format(self.titulo, formato)
    
Libro1 = Ebook("'La naturaleza'")
print(Libro1.caracteristicas("Libro"))
"""
#Ejercicio 14: Herencia y métodos sobrescritos con super()
#Consigna: Crea una clase base Vehiculo con un método moverse. Luego, crea una clase
#derivada Bicicleta que herede de Vehiculo y sobrescriba el método moverse usando
#super().
"""
class Vehiculo:
    pass
    def moverse(self):
        return "El vehiculo se esta moviendo."
    
class Bicicleta(Vehiculo):
    def moverse(self):
        accion_base = super().moverse()
        return f"{accion_base} El vehiculo en movimiento es una bicicleta."
    
Bicicleta1 = Bicicleta()
print(Bicicleta1.moverse())
"""

#Ejercicio 15: Herencia y métodos adicionales con super()
#Consigna: Crea una clase base Persona con un método presentarse. Luego, crea una
#clase derivada Profesor que herede de Persona y tenga un método adicional enseñar
#usando super().
"""
class Persona:
    pass
    def presentarse(self):
        return "La persona se presenta."
    
class Profesor(Persona):
    def enseñar(self):
        accion_base = super().presentarse
        return f"{accion_base} mientras que el profesor enseña."
    
Profesor1 = Profesor()
print(Profesor1.presentarse())
print(Profesor1.enseñar())
"""