#Farmacia: Emitir receta 

class Usuario:
    def __init__(self, DNI, nombre, receta):
        self.DNI = DNI
        self.nombre = nombre
        self.receta = receta
        self.registros = []
        
    def validacion_DNI(self):
        while True:
            try:    
                ingresar_dni = int(input("Ingresar DNI:"))   
                if self.Validar_registros_dni(ingresar_dni):
                    print("El DNI ingresado es valido.")
                    return ingresar_dni
                elif ingresar_dni == self.DNI:
                    print("es correcto.")
                    return ingresar_dni
                elif ingresar_dni != self.DNI:
                    self.validacion_opciones()
            except ValueError:
                print("Error, debe ingresar numeros")
            
    def Validar_registros_dni(self, DNI):
        for usuario in self.registros:
            if usuario["DNI"] == DNI:
                return True
            else:
                print("No se encuentra el dni.")

    def validacion_opciones(self):
        while True:
            try:
                Ingresar_opcion = int(input("No se encuentra el DNI ingresado. Desea registrarlo, ingrese [1] para registrar o [0] para salir:"))
                if Ingresar_opcion == 1:
                    self.registrar_usuario()
                    break
                elif Ingresar_opcion == 0:
                    exit()
            except ValueError:
                print("Error, debe ingresar un numero valido.")

    
    def registrar_usuario(self):
        registrar_nombre = input("Ingresar nombre: ")
        registar_dni = int(input("Ingresar DNI:"))
        registrar_reseta = input("Ingresar receta:")
        self.registros.append({"Nombre": registrar_nombre, "DNI": registar_dni, "receta": registrar_reseta})
        print("Usuario registrado correctamente.")
        

class receta(Usuario):
    def __init__(self, DNI, nombre,receta):
        super().__init__(DNI, nombre, receta) 

    def buscar_receta_por_dni(self, DNI):
        for usuario in self.registros:
            if usuario ["DNI"] == DNI:
                print("DNI con receta")
                break
            else:
                print("Documento sin receta.")
                exit()
                
    def imprimir_receta(self, DNI):
        for usuario in self.registros:
            if usuario ["DNI"] == DNI:
                print("=" * 40)
                print("Receta medica")
                print("=" * 40)
                print("Nombre: {}".format(usuario ["Nombre"]))
                print("DNI: {}".format(usuario ["DNI"]))
                print("Receta: {}".format(usuario ["receta"]))
                print("=" * 40)
            exit()

Cliente = receta(46043365, "Michael", "Ibuprofeno")
dni_validado = Cliente.validacion_DNI()
Cliente.buscar_receta_por_dni(dni_validado)
Cliente.imprimir_receta(dni_validado)

