#Gestion de control de stock 

class Stock:
    def __init__(self):
        self.stock = []

    def mostrar_stock(self):
        if self.stock:
            print("-" * 50)
            print("Stock de productos:")
            for producto in self.stock:
                print("-" * 50)
                print(f"ID Producto: {producto['ID']}")
                print(f"Nombre: {producto['Nombre']}")
                print(f"Cantidad: {producto['Cantidad']}")
                print(f"Fecha de vencimiento: {producto['Fecha de vencimiento']}")
                print(f"Precio: ${producto['Precio']}")
                print("-" * 50)
        else:
            print("No hay productos en el stock.")

class Producto(Stock):
    def __init__(self, nombre, cantidad, precio, id_producto, fecha_vencimiento):
        super().__init__()
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio 
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento

    def ingresar_producto(self):  
        while True:
            if len(self.stock) >= 10:
                print("Ya se alcanzo el maximo de productos en el stock.")
            print("Ingresar producto al stock")
            print("-" * 50)
            self.nombre = input ("Ingresar nombre del producto:")
            for producto in self.stock:
                if producto["Nombre"] == self.nombre.lower():
                    print(f"El producto {self.nombre} ya existe en el stock.")
                    break
            self.cantidad = int(input("Ingresar cantidad del producto:"))
            self.fecha_vencimiento = input("Ingresar fecha de vencimiento del producto (DD/MM/AAAA):")
            self.precio = int(input("Ingresar precio del producto: $"))
            self.id_producto = int(input("Ingresar ID del producto:"))
            for producto in self.stock:
                if producto["ID"] == self.id_producto:
                    print(f"El ID ya existe en el stock.")
                    return
            nuevo_producto = {
                "ID": self.id_producto,
                "Nombre": self.nombre,
                "Cantidad": self.cantidad,
                "Fecha de vencimiento": self.fecha_vencimiento,
                "Precio": self.precio 
                } 
            self.stock.append(nuevo_producto)
            print(f"El producto {self.nombre} ha sido ingresado al stock.")
            opcion = int(input("¿Desea ingresar otro producto?: 1. SI/ 2. NO: "))
            if opcion == 1:
                continue
            elif opcion == 2:
                break
            else:
                print("Opcion no valida")
                break
            
    def buscar_producto(self):
        print("-" * 50)
        print("Buscar producto por ID")
        print("-" * 50)
        while True:
            self.id_producto = int(input("Ingresar ID del producto a buscar:"))
            for producto in self.stock:
                if producto["ID"] == self.id_producto:
                    print("Producto encontrado")
                    print("-" * 50)
                    print(f"ID Producto: {producto['ID']}")
                    print(f"Nombre: {producto['Nombre']}")
                    print(f"Cantidad: {producto['Cantidad']}")
                    print(f"Fecha de vencimiento: {producto['Fecha de vencimiento']}")
                    print(f"Precio: ${producto['Precio']}")
                    print("-" * 50)
                else:
                    print("Producto no encontrado.")
            opcion = int(input("¿Desea buscar otro producto? 1. SI/ 2. NO:"))
            if opcion == 1:
                continue
            elif opcion == 2:
                break
            else: 
                print("Opcion no valida")
    
    def mostrar_stock(self):
        opcion = int(input("¿Desea ver el stock de productos? 1. SI/ 2. NO:"))
        if opcion ==1: 
            super().mostrar_stock()
        elif opcion == 2:
            print("Hasta luego.")
        else:
            print("Opcion no valida.")

caramelo= Producto("Producto1", 10, 100, 0, "12/12/2023")
caramelo.ingresar_producto()
caramelo.buscar_producto(1)
caramelo.mostrar_stock()
