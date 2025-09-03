"""#Clase 1
class auto:
    marca = ""
    modelo = 2004
    placa = ""

taxi = auto()
print(taxi.modelo)

#Otra clase
class jugadores_A:
    j1 = "Messi"
    j2 = "C.ronaldo"

class jugadores_B:
    j3 = "Marcelo"
    j1 = "Falcao"

print(jugadores_B.j1)

#Otra clase
class auto_taxi:
    marca = "nissan"
    modelo = 2004
    placa = "123-ABC"


class auto_patrullero:
    marca = "toyota"
    modelo = 2017
    placa = "789-XYZ"

"""
"""
#
class Nombre:
    pass

victor = Nombre()
maria = Nombre()

victor.edad = 30
victor.sexo = "Masculino"
victor.pais = "Bolivia"

maria.edad = 25
maria.sexo = "Femenino"
maria.pais = "Colombia"

print(victor.edad)
print(maria.edad)

class Auto():
    pass

taxi = Auto()
patrullero = Auto()

taxi.marca = "nissan"
taxi.modelo = 2004
taxi.placa = "123-ABC"

patrullero.marca = "toyota"
patrullero.modelo = 2017
patrullero.placa = "789-XYZ"

print(f"El taxi es marca {taxi.marca}, modelo {taxi.modelo}, y su placa es {taxi.placa}")
print(f"El patrullero es marca {patrullero.marca}, modelo {patrullero.modelo} y su placa es {patrullero.placa}.")
"""
"""
#Metodos
class Matematica:
    def suma (self):
        self.n1 = 2
        self.n2 = 3

S = Matematica()

S.suma()

print(S.n1 + S.n2)

class Matematica:
    def resta (self):
        self.n1 = 10
        self.n2 = 5

S = Matematica()

S.resta()

print(S.n1 - S.n2)

class Auto():
    def caracteristicas(self):
        self.marca = "nissan"
        self.modelo = 2004
        self.placa = "123-ABC"

taxi = Auto()
taxi.caracteristicas()
print(f"El taxi es marca {taxi.marca}, modelo {taxi.modelo}, y su placa es {taxi.placa}.")

class Auto():
    def caracteristicas(self):
        self.marca = "toyota"
        self.modelo = 2017
        self.placa = "789-XYZ"

patrullero = Auto()
patrullero.caracteristicas()
print(f"El patrullero es marca {patrullero.marca}, modelo {patrullero.modelo}, y su placa es {patrullero.placa}.")
"""
"""
#Metodo constructor 
class Ropa:
    def __init__(self):
        self.marca = "Willow"
        self.talla = "M"
        self.color = "rojo"

camisa = Ropa()
print(camisa.marca)
print(camisa.talla)
print(camisa.color)

class auto():
    def __init__(self):
        self.marca = "nissan"
        self.modelo = 2004
        self.placa = "123-ABC"

taxi = auto()
print(f"El taxi es marca {taxi.marca}, modelo {taxi.modelo} y su placa es {taxi.placa}")

class auto():
    def __init__(self):
        self.marca = "toyota"
        self.modelo = 2017
        self.placa = "789-XYZ"

patrullero = auto()
print(f"El patrullero es marca {patrullero.marca}, modelo {patrullero.modelo} y su placa es {patrullero.placa}")

"""
"""
#Metodo constructor con parametros
class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.multiplicacion = n1 * n2
        self.division = n1 / n2

operacion = Calculadora(4,6)
print(f"La suma es: {operacion.suma}")
"""
"""
class Auto:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo 
        self.placa = placa
        
    def saludar(self):
        print(f"Hola, mi taxi es marca {self.marca}, modelo {self.modelo} y su placa es {self.placa}.")

taxi = Auto("nissan", 2004, "123-ABC") 
taxi.saludar()     

 
class Auto:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo 
        self.placa = placa
        
    def saludar(self):
        print(f"Hola, mi patrullero es marca {self.marca}, modelo {self.modelo} y su placa es {self.placa}.")

patrullero = Auto("toyota", 2017, "789-XYZ") 
patrullero.saludar()     
"""
"""
#Funciones con atributos
class Persona:
    edad = 27
    nombre = "Victor"
    pais = "Brazil"

doctor = Persona()
print("La edad es: ",doctor.edad)
print("La edad es: ",getattr(doctor, "edad"))

print("El doctor tiene una edad?", hasattr(doctor, "edad"))
print("El doctor tiene una edad?", hasattr(doctor, "apellido"))

print("Antes era: ", doctor.nombre)
setattr(doctor, "nombre", "Hector")
print("Ahora se llama: ",doctor.nombre)

delattr(Persona, "pais")
print(doctor.pais)
"""
"""
#Constructores
class Persona:
    pass
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año

    def descripcion(self):
        return "{} tiene {} años".format(self.nombre, self.año)
    
    def comentario(self, frase):
        return "{} dice: {}".format(self.nombre, frase)

doctor = Persona("Michael", 20)
print(doctor.nombre)
print(doctor.descripcion())
print(doctor.comentario("Esta es la frase que yo dije"))
        
class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

mi_correo = Email()
print(mi_correo.enviado)

mi_correo.enviar_correo()
print(mi_correo.enviado)
"""
"""
#Metodos de clase
class Contador:
    cuenta = 0
    @classmethod
    def incrementar(cls):
        cls.cuenta += 1

Contador.incrementar()
print(Contador.cuenta)

#Metodo estaticos
class Matematicas:
    @staticmethod
    def sumar (a,b):
        return a, b
Resultado = Matematicas.sumar(5,7)
print(Resultado)"""