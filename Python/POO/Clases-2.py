#Herencia simple
"""
class Pokemon:
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):
        return "{} es un pokemon de tipo {}".format(self.nombre,self.tipo)

class Pikachu(Pokemon): #Clase hijo de Pokemon
    def ataque(self, tipoataque):
        return "{} tipo de ataque: {}".format(self.nombre,tipoataque)
    
class Charmander(Pokemon): #Clase hijo de Pokemon
    def ataque(self, tipoataque):
        return "{} tipo de ataque: {}".format(self.nombre,tipoataque)
    
nuevo_pokemon1 = Pikachu("Body", "Electrico") #Toma los parametros de la clase padre, Pokemon 
print(nuevo_pokemon1.descripcion()) #Metodo descripcion de la clase Pokemon (padre)
print(nuevo_pokemon1.ataque("Impacto trueno"))

nuevo_pokemon2 = Charmander("Mar", "Fuego")
"""
"""
class Auto:
    pass
    def __init__(self, auto, marca, modelo, placa):
        self.auto = auto
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
    
    def descripcion(self):
        return "El {} es marca {}, modelo {} y su placa es {}.".format(self.auto, self.marca, self.modelo, self.placa)
    
taxi= Auto("Taxi", "Nissan", "2004", "123-ABC")
print(taxi.descripcion())

patrullero = Auto("Patrullero", "Toyota", "2017", "XYZ-781")
print(patrullero.descripcion())
"""
"""
#Calculadora
class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
#Coloco un algoritmo para definir el dato

    def ingresardato(self):
        self.datos = [int(input("Ingresar dato " + str(i+1) + "=")) for i in range(self.n)]

class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)
    
    def suma(self):
        a,b, = self.datos
        s = a + b 
        print(f"El resultado es: {s}")

    def resta(self):
        a,b, = self.datos
        r = a - b 
        print(f"El resultado es: {r}")
    
    def multiplicacion(self):
        a,b, = self.datos
        m = a * b
        print(f"El resultado es: {m}")

    def division(self):
        a,b, = self.datos
        d = a / b 
        print(f"El resultado es: {d}")
    
ejemplo = op_basicas()
print(ejemplo.ingresardato())
print(ejemplo.suma())
print(ejemplo.resta())
print(ejemplo.multiplicacion())
print(ejemplo.division())

#Raiz cuadrada
class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)
    
    def cuadrada(self):
        import math
        a, = self.datos
        print(f"el resultado es: {math.sqrt(a)}")

ejemplo = Raiz()
print(ejemplo.ingresardato())
print(ejemplo.cuadrada())

#Potencia
class Potencia(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)
    
    def potencia(self):
        import math
        a, = self.datos
        print(f"El resultado es: {math.pow(3, a)}")

ejemplo = Potencia()
print(ejemplo.ingresardato())
print(ejemplo.potencia())

objecto = op_basicas()
#Comprobamos si esta trabajando con la funcion indicada
print(isinstance(objecto, op_basicas))
print(isinstance(objecto, Raiz))
#Verifica la herencia de clases
print(issubclass(Calculadora, op_basicas)) #Falso, porque estamos preguntando al reves, tenemos que preparar si la sub clase es hija.
print(issubclass(op_basicas, Calculadora)) #True
print(issubclass(Potencia, Calculadora)) #True
print(issubclass(Raiz, Calculadora)) #True

#Herencia Multiple
class Telefono:
    def __init__(self):
        pass

    def llamar(self):
        print("Llamando...")

    def ocupado(self):
        print("Ocupado...")

class Camara:
    def __init__(self):
        pass

    def fotografia(self):
        print("Tomando fotos...")
    
class Reproduccion:
    def __init__(self):
        pass

    def reproduccionmusica(self):
        print("Reproducciendo musica...")

    def reproduccionvideo(self):
        print("Reproducir un video...")

#herencia multiple
class Smartphone(Telefono,Camara,Reproduccion): #Heredo las clases
    def __del__(self): #DESTRUCTOR 
        #usamos el metodo del para limpiar los recursos, los objectos
        # y las clases se eliminan de la memoria cuando no se usan con el estamos indicando que la clase
        # smartphone ya no es necesaria
        print("Telefono apagado") #a modo de refencia

movil = Smartphone()
#print(dir(movil)) #directorio de acciones que puedo aplicar directamente a este objecto.
print(movil.fotografia())
print(movil.llamar())
print(movil.ocupado())
print(movil.reproduccionmusica())
print(movil.reproduccionvideo()) """
