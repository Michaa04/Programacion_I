#Sistema de gestion biblioteca 2 

class biblioteca: 
    def __init__(self):
        self.catalogo = []
        self.usuarios = []

    def agregar_libro(self, libro):
        print("Agregar libro al catalogo")
        libro = input("Ingresar libro: ")
        self.catalogo.append(libro)
        print(f"El libro {libro} ha sido agregado al catalogo.")

    def prestar_libro(self):
        print("-" * 50)
        print("Prestar libro")
        usuario = input("Ingresar usuario:")
        print("-" * 50)
        print(f"Usuario: {usuario}")
        print("Catalogo de libros:")
        print(self.catalogo)
        print("-" * 50) 
        libro = input("Ingresar libro para prestamo:")
        if libro in self.catalogo:
            self.catalogo.remove(libro)
            print(f"El libro {libro} ha sido prestado a {usuario}")
        else: 
            print(F"El libro {libro} no esta disponible.")
    
    def devolver_libro(self):
        print("-" * 50)
        print("Devolver libro")
        while True:
            usuario = input("Ingresar usuario:")
            libro = input("Ingresar libro:")
            if libro not in self.catalogo:
                self.catalogo.append(libro)
                print(f"El libro {libro} ha sido devuelto por {usuario}.")
                break
            else:
                print("Volver a ingresar libro.")   
            
    def mostrar_catalogo(self):
        if self.catalogo:
            print("Catalogo de libros")
            for libro in self.catalogo:
                print("-" * 50)
                print(libro)
                print("-" * 50)
        else:
            print("No hay libros en el catalogo.")

class libro(biblioteca):
    def __init__(self, titulo, autor):
        self.__titulo = titulo 
        self.__autor = autor

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def disponibilidad_libro(self):
        print("Verificar disponibilidad del libro")
        self.__titulo = input("Ingresar Titulo del libro:")
        for self.__titulo in self.catalogo:
            if self.__titulo == self.catalogo:
                print(f"El libro {self.__titulo} esta disponible en la biblioteca")
            else:
                print(f"El libro {self.__titulo} no esta disponible en la biblioteca.")

    def prestar_libro(self, libro, usuario):
        return super().prestar_libro(libro, usuario)
        
    def devolver_libro(self, libro, usuario):
        return super().devolver_libro(libro, usuario)
    
    def mostrar_catalogo(self):
        return super().mostrar_catalogo()
    
class usuario(biblioteca):
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros_prestados = []    

    def get_nombre(self):
        return self.__nombre 
    
    def prestar_libro(self, libro):
        return super().prestar_libro(libro)
    
    def devolver_libro(self, libro):
        return super().devolver_libro(libro)
    
class empleado (usuario):
    def agregar_libro(self, libro):
        return super().agregar_libro(libro)
    

sistema = libro("El Principito", "Michael")
sistema.agregar_libro("2002")
sistema.prestar_libro("micha", "Juan")
sistema.devolver_libro("micha", "Juan")
sistema.mostrar_catalogo() 
sistema.disponibilidad_libro()

