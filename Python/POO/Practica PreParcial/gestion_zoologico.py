# Sistema de gestion de un zoologico
class Animal:
    """Representa un animal en el zoologico con sus atributos"""
    def __init__(self, nombre, especie, edad, salud):
        """Inicializa los atributos del animal"""
        self.nombre = nombre
        self.especie = especie
        self.edad = edad 
        self.salud = salud

    def mostrar_informacion(self):
        """Muestra la informacion del animal"""
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")
        print(f"Estado de salud: {self.salud}")

    def actualizar_salud(self, nueva_salud):
        """Actualiza el estado de salud del animal"""
        self.salud = nueva_salud

class AnimalExotico(Animal):
    """Representa un animal exotico en el zoologico"""
    def __init__(self, nombre, especie, edad, salud, pais_origen, nivel_riesgo):
        """Inicializa los atributos del animal exotico"""
        super().__init__(nombre, especie, edad, salud)
        self.pais_origen = pais_origen
        self.nivel_riesgo = nivel_riesgo

    def mostrar_informacion_ad(self):
        """Muestra la informacion adicional del animal exotico"""
        super().mostrar_informacion()
        print(f"Pais de origen: {self.pais_origen}")
        print(f"Nivel de riesgo: {self.nivel_riesgo}")

class Zoologico(Animal):
    """Representa un sistema de gestion de animales en un zoologico"""
    def __init__(self, nombre, ubicacion):
        """Inicializa los atributos del zoologico"""
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.animales = []

    def menu_principal(self):
        """Muestra el menu principal del sistema de gestion del zoologico"""
        while True:
            print("Bienvenido al sistema de gestion del zoologico")
            print("-" * 50)
            print("1. Agregar animal")
            print("2. Eliminar animal")
            print("3. Buscar animal")
            print("4. Mostrar animales")
            print("5. Actualizar estado de salud de un animal.")
            print("0. Salir")
            print("-" * 50)
            opcion = int(input("Seleccione una opcion:"))
            if opcion == 1:
                self.agregar_animal()
            elif opcion == 2:
                self.eliminar_animal()
            elif opcion == 3:
                self.buscar_animal()
            elif opcion == 4:
                self.mostrar_animales()
            elif opcion == 5:
                self.actualizar_salud()
            elif opcion == 0:
                print("Hasta luego")
                exit()
            else: 
                print("Opcion no valida")
                break

    def agregar_animal(self):
        """Agrega un nuevo animal al zoologico"""
        while True:
            print("-" * 50)
            print("Agregar animal al zoologico")
            print("-" * 50)
            print("Tipo de animal")
            print("-" * 50)
            print("1. Comun")
            print("2. Exotico")
            print("-" * 50)
            tipo_animal = int(input("Ingresar el tipo de animal:"))
            self.nombre = input(f"Ingresar el nombre del animal:")
            self.especie = input(f"Ingresar la especie del animal:")
            self.edad = int(input(f"Ingresar la edad del animal:"))
            self.salud = input(f"Ingresar el estado de salud del animal (Bueno, Regular, Malo):")

            if tipo_animal == 1:
              nuevo_animal = {
                "Nombre": self.nombre,
                "Especie": self.especie,
                "Edad": self.edad, 
                "Estado de Salud": self.salud
                }
            elif tipo_animal == 2:
                self.pais_origen = input("Ingresar el pais de origen del animal:")
                self.nivel_riesgo = input("Ingresar el nivel de riesgo del animal (Alto, Medio, Bajo):")
                nuevo_animal = {
                "Nombre": self.nombre,
                "Especie": self.especie,
                "Edad": self.edad, 
                "Estado de Salud": self.salud,
                "Pais de Origen": self.pais_origen,
                "Nivel de Riesgo": self.nivel_riesgo
                }
            self.animales.append(nuevo_animal)
            print("-" * 50)
            print(f"El animal {self.nombre} ha sido agregado al zoologico.")
            print("-" * 50)
            op = int(input("Desea agregar otro animal? 1. SI/ 2. Volver al menu anterior:"))
            if op == 1:
                continue
            elif op == 2:
                self.menu_principal()
            else:
                print("Opcion no valida, por favor intente nuevamente")

    def eliminar_animal(self):
        """Elimina un animal del zoologico"""
        while True:
            print("Eliminar animal del zoologico")
            print("-" * 50)
            if not self.animales:
                print("No hay animales en el zoologico para eliminar.")
                self.menu_principal()
                return
            print("-" * 50)
            print("Animales en el zoologico")
            print("-" * 50)
            for animal in self.animales:
                print(f"Nombre: {animal['Nombre']}")
                print(f"Especie: {animal['Especie']}")
                print(f"Edad: {animal['Edad']} años")
                print(f"Estado de salud: {animal['Estado de Salud']}")
                print("-" * 50)
            nombre_animal = input("Ingresar el nombre del animal a eliminar:")
            print("-" * 50)
            for animal in self.animales:
                if animal["Nombre"] == nombre_animal.lower():
                    self.animales.remove(animal)
                    print(f"El animal {nombre_animal} ha sido eliminado del zoologico.")
                    print("-" * 50)
            op = int(input("Desea eliminar otro animal? 1. SI/ 2. Volver al menu anterior:"))
            if op == 1:
                continue
            elif op == 2:
                self.menu_principal()
            else:
                print("Opcion no valida, por favor intente nuevamente")

    def buscar_animal(self):
        """Busca un animal en el zoologico por su nombre"""
        while True:
            print("-" * 50)
            print("Buscar animal en el zoologico")
            print("-" * 50)
            nombre_animal = input("Ingresar el nombre del animal a buscar:")
            print("-" * 50)
            for animal in self.animales:
                if animal["Nombre"] == nombre_animal.lower():
                    print("Animal encontrado:")
                    print("-" * 50)
                    print(f"Nombre: {animal['Nombre']}")
                    print(f"Especie: {animal['Especie']}")
                    print(f"Edad: {animal['Edad']} años")
                    print(f"Estado de salud: {animal['Estado de Salud']}")
                    print("-" * 50)
            op = int(input("Desea buscar otro animal? 1. SI/ 2. Volver al menu anterior:"))
            if op == 1:
                continue
            elif op == 2:
                self.menu_principal()
            else:
                print("Opcion no valida, por favor intente nuevamente")

    def mostrar_animales(self):
        """Muestra todos los animales del zoologico"""
        while True:
            print("-" * 50)
            print("Seleccionar tipo de animal" )
            print("-" * 50)
            print("1. Comun")
            print("2. Exotico")
            print("-" * 50)
            op = int(input("Desea ver que tipo de animal?: "))
            if op == 1:
                print("-" * 50)
                print("Animales en el zoologico")
                print("-" * 50)
                for animal in self.animales:
                    self.mostrar_informacion()
                    print("-" * 50)
                    continue
            elif op == 2:
                print("-" * 50)
                print("Animales exoticos en el zoologico")
                print("-" * 50)
                for animal in self.animales:
                    print(f"Nombre: {animal['Nombre']}")
                    print(f"Especie: {animal['Especie']}")
                    print(f"Edad: {animal['Edad']} años")
                    print(f"Estado de salud: {animal['Estado de Salud']}")
                    print(f"Pais de origen: {animal['Pais de origen']}")
                    print(f"Nivel de riesgo: {animal['Nivel de riesgo']}")
                print("-" * 50)
            op = int(input("Presionar 1. Volver al menu anterior:"))
            if op == 1:
                self.menu_principal()  
            else:
                print("Opcion no valida, por favor intente nuevamente")

    def actualizar_salud(self):
        """Actualiza el estado de salud de un animal"""
        while True:
            print("-" * 50)
            print("Actualizar estado de salud de un animal")
            print("-" * 50)
            if not self.animales:
                print("No hay animales en el zoologico para actualizar su salud")
                self.menu_principal()
                return
            print("Animales en el zoologico:")
            print("-" * 50)
            for animal in self.animales:
                print(f"Nombre: {animal['Nombre']}")
                print(f"Especie: {animal['Especie']}")
                print(f"Edad: {animal['Edad']} años")
                print(f"Estado de salud: {animal['Estado de Salud']}")
                print("-" * 50)
            nombre_animal = input("Ingresar el nombre del animal a actualizar su salud:")
            print("-" * 50)
            for animal in self.animales:
                if animal["Nombre"] == nombre_animal.lower():
                    nueva_salud = input("Ingresar el nuevo estado de salud (Bueno, Regular, Malo):")
                    print("-" * 50)
                    animal["Estado de Salud"] = nueva_salud
                    print(f"El estado de salud del animal {nombre_animal} ha sido actualizado a {nueva_salud}.")
                    print("-" * 50)
            op = int(input("Desea actualizar el estado de salud de otro animal? 1. SI/ 2. Volver al menu anterior:"))
            if op == 1:
                continue
            elif op == 2:
                self.menu_principal()
            else:
                print("Opcion no valida, por favor intente nuevamente")


animal = Zoologico("Zoologico Central", "Ciudad Capital")
animal.menu_principal()


