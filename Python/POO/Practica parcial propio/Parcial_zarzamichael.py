#Parcial: Sistema de gestion de inventario en una tienda

#Seudocodigo
"""Inicio
1. Menu interactivo con distintas opciones
2. Registrar Producto con sus atributos (hasta 10 veces).
3. Buscar el producto por nombre.
4. Evaluar que el producto este en el inventario.
5. Calcular valor total del inventario 
6. Mostrar todos los productos 
Fin
"""

class Producto:
    """Representa el objecto producto con sus atributos."""
    def __init__(self, nombre, cantidad,precio_unitario):
        self.nombre = nombre
        self.cantidad = cantidad
        self.__precio_unitario = precio_unitario
    
    def info_producto(self):
        """Muestra la informacion del producto"""
        print("-" * 50)
        print(f"Nombre {self.nombre}")
        print(f"Cantidad en stock: {self.cantidad}")
        print(f"Precio: ${self.__precio_unitario}")
        print("-" * 50)

class GestionProductos(Producto):
    """Representa la gestion de los productos en el inventario"""
    def __init__(self):
        self.inventario = []
                
    def registrar_producto(self):
        """Registra cada producto"""
        while True:
            try:
                if len(self.inventario) > 10:
                    print("Ya se alcanzo el maximo de ingreso de producto")
                    break
                else:
                    for i in range(11):
                        print("Ingresar un producto")
                        print("-" * 50)
                        print(f"Producto {i}")
                        nombre = input("Ingresar nombre:")
                        cantidad = int(input("Ingresar cantidad:"))
                        precio_unitario = float(input("Ingresar precio: $"))
                        producto_nuevo = Producto(nombre, cantidad, precio_unitario)
                        self.inventario.append(producto_nuevo)
                        print("-" * 50)
                        print(f"Se agrego el producto {nombre} al inventario.")
                        print("-" * 50)
                        op = int(input("Desea volver a ingresar un producto (1.SI/2.NO):"))
                        if op == 1:
                            continue
                        elif op == 2:
                            menu_principal()
            except ValueError:
                print("Error, ingresar correctamente los datos.")
    def buscar_producto(self):
        """Busca el producto en el inventario"""
        while True:
            try:
                if not self.inventario:
                    print("No hay productos en el inventario")
                    break
                else:
                    print("Buscar el producto")
                    print("-" * 50)
                    nombre_intento = input("Ingresar nombre:")
                    for producto in self.inventario:
                        print(self.inventario)
                        if producto.nombre == nombre_intento:
                            print("-" * 50)
                            Producto.info_producto(producto)
                            continue
                        else:
                            print("Producto no encontrado.")
            except ValueError:
                print("Error, ingresar correctamente los datos.")
                op = int(input("¿Desea volver a buscar otro producto? (1.SI/2.NO):"))
                if op == 1:
                    continue
                elif op == 2:
                    menu_principal()

    def calcular_valor_total(self):
        """Calcula el valor total del inventario"""
        while True:
            if not self.inventario:
                print("-" * 50)
                print("No hay productos en el inventario")
                break
            else:
                print("-" * 50)
                print("Valor total de cada producto")
                print("-" * 50)
                valor_total_general = 0
                for producto in self.inventario:
                    valor_total_producto = producto.cantidad * producto._Producto__precio_unitario
                    print(f"{producto.nombre}: ${valor_total_producto}")
                    valor_total_general += valor_total_producto
                    print("-" * 50)
                print(f"Valor total del inventario: ${valor_total_general}")
                print("-" * 50)
                op = int(input("¿Desea volver al menu principal? (1.SI/2.NO):"))
                if op == 1:
                    menu_principal()
                elif op == 2:
                    exit()
        
    def mostrar_productos(self):
        """Muestra todos los productos del inventario"""
        while True:
            if not self.inventario:
                print("-" * 50)
                print("No hay producto en el inventario.")
                break  
            else:
                print("Lista de productos")
                for producto in self.inventario:
                    Producto.info_producto(producto)
            op = int(input("¿Desea volver al menu principal? (1.SI/2.NO):"))
            if op == 1:
                menu_principal()
            elif op == 2:
                exit()   

sistema = GestionProductos()
def menu_principal():
        """Muestra el menu principal con distintas opciones"""
        while True:
            print("-" * 50)
            print("Menu principal")
            print("-" * 50)
            print("1. Registrar producto")
            print("2. Buscar producto.")
            print("3. Calcular valor total del inventario.")
            print("4. Mostrar todos los productos.")
            print("0. Salir")
            print("-" * 50)
            op = int(input("Ingresar una opcion:"))
            if op == 1: 
                GestionProductos.registrar_producto(sistema)
            elif op == 2:
                GestionProductos.buscar_producto(sistema)
            elif op == 3:
                GestionProductos.calcular_valor_total(sistema)
            elif op == 4:
                GestionProductos.mostrar_productos(sistema)
            elif op == 0:
                exit()
            else:
                print("Opcion no valida")

menu_principal()
        

    
        

