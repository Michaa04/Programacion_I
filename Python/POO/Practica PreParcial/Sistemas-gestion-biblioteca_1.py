#Sistema de gestion biblioteca 1
class Publicacion: 
    def __init__(self, titulo, autor, año_publicacion, ):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_info_adicional(self):
        pass

class Libro(Publicacion):
    def ingresar_info(self):
        print("-" * 50)
        self.titulo = input("Ingresar titulo del libro:")
        self.autor = input("Ingresar autor del libro:")
        self.año_publicacion = int(input("Ingresar año de publicacion:"))

    def mostrar_info(self):
        print("-" * 50 )
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicacion: {self.año_publicacion}")
        print("-" * 50 )
    
    def disponibilidad_libro(self):
        opcion = int(input("Ingresar disponibilidad(1 disponible - 0 para no disponible):"))
        if opcion == 1:
            print(f"El libro {self.titulo} esta disponible para prestamo.")
        elif opcion == 0:
            print(f"El libro {self.titulo}, no se encuentra disponible.")
        else: 
            print("Opcion no valida.")

    def __init__(self, titulo, autor, año_publicacion, precio, numeros_paginas):
        super().__init__(titulo, autor, año_publicacion)
        self.__precio = precio 
        self.__numeros_paginas = numeros_paginas

    def mostrar_info_adicional(self):
        super().mostrar_info_adicional()
        print(f"Precio: ${self.__precio}")
        print(f"Numeros de paginas: {self.__numeros_paginas}")

    def cambiar_precio(self, nuevo_precio):
        nuevo_precio = int(input("Ingresar nuevo precio: $"))
        self.__precio = nuevo_precio
        
class Revista(Publicacion): 
    def ingresar_info(self):
        print("-" * 50)
        self.titulo = input("Ingresar titulo del revista:")
        self.autor = input("Ingresar autor del revista:")
        self.año_publicacion = int(input("Ingresar año de publicacion:"))

    def mostrar_info(self):
        print("-" * 50)
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicacion: {self.año_publicacion}")
        print("-" * 50)
    
    def __init__(self, titulo, autor, año_publicacion, precio, numero_paginas):
        super().__init__(titulo, autor, año_publicacion)
        self.__precio = precio 
        self.__numero_paginas = numero_paginas

    def mostrar_info_adicional(self):
        super().mostrar_info_adicional()
        print(f"Precio: ${self.__precio}")
        print(f"Numeros de paginas: {self.__numero_paginas}")

    def cambiar_precio(self, nuevo_precio):
        nuevo_precio = int(input("Ingresar nuevo precio: $"))
        self.__precio = nuevo_precio
        
class Periodico(Publicacion):      
    def ingresar_info(self):
        print("-" * 50)
        self.titulo = input("Ingresar titulo del periodico:")
        self.autor = input("Ingresar autor del periodico:")
        self.año_publicacion = int(input("Ingresar año de publicacion:"))

    def mostrar_info(self):
        print("-" * 50)
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicacion: {self.año_publicacion}")
        print("-" * 50)
    
    def __init__(self, titulo, autor, año_publicacion, precio, numero_paginas):
        super().__init__(titulo, autor, año_publicacion)
        self.__precio = precio 
        self.__numero_paginas = numero_paginas

    def mostrar_info_adicional(self):
        super().mostrar_info_adicional()
        print(f"Precio: ${self.__precio}")
        print(f"Numeros de paginas: {self.__numero_paginas}")

    def cambiar_precio(self, nuevo_precio):
        nuevo_precio = int(input("Ingresar nuevo precio: $"))
        self.__precio = nuevo_precio

    def cambiar_numeros_paginas(self, nuevo_numeros_paginas):
        nuevo_numeros_paginas = int(input("Ingresar nuevo numero de paginas:"))
        self.__numero_paginas = nuevo_numeros_paginas
        

libro = Libro("El Lobo", "Michael Zarza", 2012, 200, 58)
libro.ingresar_info()
libro.mostrar_info()
libro.disponibilidad_libro()
libro.mostrar_info_adicional()
libro.cambiar_precio(0)
libro.mostrar_info_adicional()

revista = Revista("9 de oro", "Luciano Gonzalez", 2024, 400, 100)
revista.ingresar_info()
revista.mostrar_info()
revista.mostrar_info_adicional()
revista.cambiar_precio(0)
revista.mostrar_info_adicional()

periodico = Periodico("La Nacion", "Diego Gatica", 2025, 4545, 90)
periodico.ingresar_info()
periodico.mostrar_info()
periodico.mostrar_info_adicional()
periodico.cambiar_precio(0)
periodico.cambiar_numeros_paginas(0)
periodico.mostrar_info_adicional()


