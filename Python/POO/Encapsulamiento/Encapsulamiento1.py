# Sistema de gestion de estudiantes
"""
class estudiantes:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__calificaciones = [3, 5, 6]

    def mostrar_informacion(self):
        return f"El nombre es {self.__nombre} y su edad {self.__edad}"
    
    def mostrar_calificacion(self):
            ingresar_calificacion = int(input("Ingresar calificacion:"))
            self.__calificaciones.append(ingresar_calificacion)
            print(f"Su calificiacion es {ingresar_calificacion}")
            
    def mostrar_promedio(self):
        sum(self.__calificaciones)
        longitud = len(self.__calificaciones)
        promedio_calificaciones = suma_calificaciones / longitud
        return f"El promedio de calificaciones es {promedio_calificaciones}"
    

estudiante = estudiantes("Michael", 19)
print(estudiante.mostrar_informacion())
print(estudiante.mostrar_calificacion())
estudiante.mostrar_promedio()
"""
#Sistema de inventario de productos 
"""
class Productos:
    def __init__(self, nombre, precio, cantidad_en_stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad_en_stock = cantidad_en_stock
    
    def mostrar_info(self):
        return f"Nombre del producto: {self.__nombre}, Precio: ${self.__precio}, Cantidad de stock: {self.__cantidad_en_stock}"

    def Modificacion_cantidad_stock(self):
        opcion = int(input("Ingresar 1 para agregar stock o 0 para retirar stock:"))
        if opcion == 1:
            agregar_cantidad = int(input("Ingresar cantidad:"))
            self.__cantidad_en_stock = self.__cantidad_en_stock + agregar_cantidad
            print(f"Se agregaron {agregar_cantidad} unidad/des al stock. Stock actualizado: {self.__cantidad_en_stock}") 
        elif opcion == 0:
            retirar_cantidad = int(input("Ingresar cantidad:"))
            self.__cantidad_en_stock = self.__cantidad_en_stock - retirar_cantidad
            print(f"Se retiro {retirar_cantidad} del stock. Stock actualizado: {self.__cantidad_en_stock}")

Desodorante = Productos("Desodorante", 100, 20)
print(Desodorante.mostrar_info())
Desodorante.Modificacion_cantidad_stock()
"""
#Sistema de reservas de hotel

class Reserva:
    def __init__(self, nombre_cliente, numero_habitacion):
        self.__nombre_cliente = nombre_cliente
        self.__numero_habitacion = numero_habitacion
        self.__fechas_reserva = ["19/05/2004"]

    def mostrar_info(self):
        return f"Nombre del cliente: {self.__nombre_cliente}. Numero de habitacion: {self.__numero_habitacion}."

    def agregar_fecha(self):
            agregar_fecha = (input("Ingresar fecha con el siguiente formato (dd/mm/aaaa): "))
            self.__fechas_reserva.append(agregar_fecha)
            print(f"Se agrego la fecha {agregar_fecha} a la lista de fechas.")
       
    def eliminar_fecha(self):           
        print(self.__fechas_reserva)
        eliminar_reserva = input("Ingresar la fecha que desea eliminar con el siguiente formato (dd/mm/aaaa): ")
        for fecha in self.__fechas_reserva:
            if eliminar_reserva == fecha:
                self.__fechas_reserva.remove(eliminar_reserva)
                print(f"Se elimino la fecha {eliminar_reserva} de la lista de fechas.")
            else:
                print("Vuelve a intentarlo")

    def mostrar_fechas(self):
        return f"Las fechas de reserva son: {self.__fechas_reserva}"

hotel = Reserva("Michael", 43)
print(hotel.mostrar_info())
hotel.agregar_fecha()
hotel.eliminar_fecha()
