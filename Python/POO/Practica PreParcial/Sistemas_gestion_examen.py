#Sistema de gestion de examen
import csv
def crear_archivo_csv(archivo):
    """Crea un archivo CSV"""
    with open(archivo, mode= "a", newline= "", encoding= "utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Usuario", "Examen", "Pregunta", "Respuesta", "Estado", "Puntaje"])

class Usuario:
    """Representa un usuario en el sistema con sus atributos"""
    def __init__(self, usuario, contraseña, tipo):
        """Inicializa los atributos del usuario"""
        self.usuario = usuario
        self.__contraseña = contraseña
        self.tipo = tipo
        self.perfil_alumno = []
        self.perfil_profesor = []

    def verificar_contraseña(self, contraseña):
        """Verifica si la contraseña es correcta"""
        return self.__contraseña == contraseña

class Estudiante(Usuario):
    """Representa un estudiante en el sistema"""
    def __init__(self, usuario, contraseña):
        super().__init__(usuario, contraseña, tipo="alumno")
        self.respuestas = {}
        self.puntaje_manual = {}

    def realizar_examen(self, examen):
        """Realiza el examen y guarda sus respuestas"""
        print(f"\n{self.usuario}, comenzás el examen: {examen.titulo}")
        for i, pregunta in enumerate(examen.preguntas, 1):
            print(f"\nPregunta {i}: {pregunta.enunciado}")
            if hasattr(pregunta, 'opciones'):
                for letra, texto in pregunta.opciones.items():
                    print(f"{letra}. {texto}")
            respuesta = input("Tu respuesta: ").strip()
            self.respuestas[pregunta] = respuesta

    def calcular_puntaje(self, examen):
        """Calcula el puntaje del examen"""
        puntaje_total = 0
        for pregunta in examen.preguntas:
            respuesta = self.respuestas.get(pregunta, None)
            resultado = pregunta.evaluar(respuesta)
            if resultado is True:
                puntaje_total += pregunta.puntaje
            elif resultado is None:
                puntaje_total += self.puntaje_manual.get(pregunta, 0)
        return puntaje_total
            
    def generar_reporte(self, examen):
        """Genera un reporte del examen realizado"""
        print(f"Reporte de examen")
        print("-" * 50)
        print(f"Estudiante: {self.usuario}")
        print(f"Examen: {examen.titulo}")

        puntaje_obtenido = 0
        puntaje_total = 0
        correctas = 0
        incorrectas = 0
        pendientes = 0

        print("Respuestas:")
        for i, pregunta in enumerate(examen.preguntas, 1):
            respuesta = self.respuestas.get(pregunta, "No respondida")
            resultado = pregunta.evaluar(respuesta)
            puntaje_total += pregunta.puntaje
            print(f"Pregunta {i}: {pregunta.enunciado}")
            print(f"Tu respuesta: {respuesta}")

            if resultado is True:
                print("Respuesta correcta")
                print(f"Puntaje obtenido: {pregunta.puntaje}")
                puntaje_obtenido += pregunta.puntaje
                correctas +=1
            elif resultado is False:
                print("Respuesta incorrecta")
                incorrectas += 1
            else:
                print("Pregunta abierta, pendiente de evaluacion")
                pendientes += 1
                
        print("Resumen Final:")
        print("-" * 50)
        print(f"Puntaje obtenido: {puntaje_obtenido}, Puntaje total: {puntaje_total}")
        print(f"Correctas: {correctas}")
        print(f"Incorrectas: {incorrectas}")
        print(f"Pendientes: {pendientes}")
        print("-" * 50)

    def guardar_reporte_csv(self, examen, archivo= "Reporte_examen.csv"):
        """Guarda el reporte del examen en un archivo CSV"""
        with open(archivo, mode="a", newline= "", encoding= "utf-8") as file:
            writer = csv.writer(file)
            
            for pregunta in examen.preguntas:
                respuesta = self.respuestas.get(pregunta, "No respondida")
                respuesta = pregunta.evaluar(respuesta)
                estado = "Pendiente"
                if respuesta is True:
                    estado = "Correcta"
                elif respuesta is False:
                    estado = "Incorrecta"

                writer.writerow([self.usuario,
                             examen.titulo,
                             pregunta.enunciado,
                             respuesta,
                             estado,
                             pregunta.puntaje
                             ])
class Profesor(Usuario):
    """Representa un profesor en el sistema"""
    def __init__(self, usuario, contraseña):
        """Inicializa los atributos del profesorf"""
        self.examenes_creados = []
        super().__init__(usuario, contraseña, tipo="profesor")
    
    def crear_examen(self): 
        """Crea el examen"""
        titulo = input("Ingresar titulo del examen:")
        examen = Examen(titulo)

        while True:
            print("Agregar nueva pregunta")
            print("1. Preguntas de opcion multiple")
            print("2. Preguntas de Verdadero o Falso")
            print("3. Preguntas abiertas")
            print("4. Finalizar creacion del examen")
            opcion = int(input("Ingresar una opcion:"))
            if opcion == 1:
                enunciado = input("Ingresar el enunciado de la pregunta:")
                puntaje = int(input("Ingresar puntaje de la pregunta:"))
                opciones = []
                for i in range(4):
                    opcion_texto = input(f"Opcion {i+1}:")
                    opciones.append(opcion_texto)
                respuesta_correcta = input("Ingrese el texto de la respuesta correcta:")
                pregunta = OpcionMultiple(enunciado, puntaje, opciones, respuesta_correcta)
                examen.agregar_preguntas(pregunta)

            elif opcion == 2:
                enunciado = input("Ingresar enunciado de la pregunta:")
                puntaje = int(input("Ingresar puntaje de la pregunta:"))
                respuesta = input("Ingresar 1. Verdadero(V) / 2. Falso(F)").lower()
                respuesta_correcta = True if respuesta == "V" else False
                pregunta = VerdaderoFalso(enunciado, puntaje, respuesta_correcta)
                examen.agregar_preguntas(pregunta)

            elif opcion == 3: 
                enunciado = input("Ingresar enunciado de la pregunta:")
                puntaje = input("Ingresar puntaje de la pregunta:")
                pregunta = PreguntasAbiertas(enunciado, puntaje)
                examen.agregar_preguntas(pregunta)
            
            elif opcion == 4:
                print("Examen finalizado")
                break
            else:
                print("Opcion no valida.")
        self.examenes_creados.append(examen)
        return examen

    def evaluar_preguntas_abiertas(self, examen):
        """Evalua las preguntas abiertas del examen"""
        print(f"Evaluacion de preguntas abiertas del estudiante: {Estudiante.usuario}")
        for pregunta in examen.preguntas:
            if isinstance(pregunta, PreguntasAbiertas):
                respuesta = Estudiante.respuestas.get(pregunta, None)
                if respuesta:
                    print(f"Pregunta: {pregunta.enunciado}")
                    print(f"Respuesta del estudiante: {respuesta}")
                    while True:
                        try:
                            puntaje = float(input("Ingresar puntaje (0 - 10):"))
                            if 0 <=puntaje <= 10:
                                Estudiante.puntaje_manual[pregunta] = puntaje
                                break
                            else:
                                print("El puntaje debe ser entre 0 a 10.")
                            
                        except ValueError:
                            print("Error, Ingrese un numero valido.")

                else:
                    print(f"Pregunta: {pregunta.enunciado}")
                    print("No respondida por el estudiante.")              
                                
class Login:
    """Representa el login para un usuario"""
    def __init__(self):
        self.perfil_alumno = []
        self.perfil_profesor = []

    def Registrar_usuario(self):
        """Registrar usuario"""
        while True: 
            print("Registrar usuario")
            print("-" * 50)
            self.usuario = input("Ingresar usuario:")
            self.__contraseña = input("Ingresar contraseña:")
            self.tipo = input("Ingresar tipo (alumno/profesor):")
            if self.tipo.lower() == "alumno":
                nuevo_usuario = Estudiante(self.usuario, self.__contraseña)
                self.perfil_alumno.append(nuevo_usuario)
                print("Usuario registrado como alumno.")

            elif self.tipo.lower() == "profesor":
                nuevo_usuario = Profesor(self.usuario, self.__contraseña)
                self.perfil_profesor.append(nuevo_usuario)
                print("Se añadio a lista de profesor")
            
    def inicio_sesion(self):
        "Inicio de sesion de un usuario"
        print("Inicio de sesion")
        Usuario = input("Ingresar usuario:")
        contraseña = input("Ingresar contraseña:")
        for usuario in self.perfil_alumno + self.perfil_profesor:
            if usuario.usuario == Usuario and usuario.verificar_contraseña(contraseña):
                print(f"Bienvenido {usuario.usuario}!")
                return usuario
        print("Usuario o contraseña incorrectos.")
        return None

class Pregunta:
    """Representa la pregunta del examen"""
    def __init__(self, enunciado, puntaje):
        self.enunciado = enunciado
        self.puntaje = puntaje

    def mostrar(self):
        """Muestra enunciado"""
        print(f"{self.enunciado} ({self.puntaje} pts).")

    def evaluar(self, respuesta_estudiante):
        """Evalua el examen"""
        pass

class OpcionMultiple(Pregunta):
    """Representa las preguntas de opcion multiple"""
    def __init__(self, enunciado, puntaje, opciones, respuesta_correcta):
        super().__init__(enunciado, puntaje)
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta

    def mostrar(self):
        """Muestra """
        super().mostrar()
        for i, opcion in enumerate (self.opciones, 1):
            print(f"{i}. {opcion}")

    def evaluar(self, respuesta_estudiante):
        """Evalua el examen"""
        return self.opciones[respuesta_estudiante - 1] == self.respuesta_correcta

class VerdaderoFalso(Pregunta): 
    """Representa las preguntas Verdadero/Falso"""
    def __init__(self, enunciado, puntaje, respuesta_correcta):
        super().__init__(enunciado, puntaje)
        self.respuesta_correcta = respuesta_correcta

    def mostrar(self):
        super().mostrar()
        print("1. V (Verdadero) / 2. (Falso)")

    def evaluar(self, respuesta_estudiante):
        return (respuesta_estudiante == 1 and self.respuesta_correcta is True) or (respuesta_estudiante == 2 and self.respuesta_correcta is False)
    
class PreguntasAbiertas(Pregunta):
    """Representa las preguntas abiertas"""
    def __init__(self, enunciado, puntaje):
        super().__init__(enunciado, puntaje)
        self.respuesta_estudiante = None

    def mostrar(self):
        super().mostrar()

    def evaluar(self, respuesta_estudiante):
        self.respuesta_estudiante == respuesta_estudiante
        return None

class Examen:
    """Representa el examen"""
    def __init__(self, titulo):
        self.titulo = titulo
        self.preguntas = []

    def agregar_preguntas(self, pregunta):
        """Agregar las preguntas para el examen"""
        self.preguntas.append(pregunta)

    def mostrar_examen(self):
        """Muestra el examen"""
        print(f"Examen {self.titulo}")
        for i, pregunta in enumerate(self.preguntas,1):
            print(f"Pregunta {i}:")
            pregunta.mostrar()

    
def menu_principal(usuario):
    """Muestra el menu principal"""
    while True:
        print("Sistema de examenes")
        print("-" * 50)
        print("1. Registrarse")
        print("2. Iniciar Sesion")
        print("3. Salir")
        print("-" * 50)

        opcion = input("Seleccionar una opcion:")
        if opcion == "1":
            Login.Registrar_usuario(usuario)
        elif opcion == "2":
            usuario = Login.inicio_sesion(usuario)
            if usuario:
                if usuario.tipo == "profesor":
                    menu_profesor(usuario, usuarios)
                elif usuario.tipo == "alumno":
                    menu_estudiante (usuario, usuarios)
        elif opcion == "3":
            print("Gracias por usar el sistema. Hasta luego")
            break
        else: 
            print("Opcion no valida. Intente nuevamente.")
            continue

    def menu_profesor(usuario, usuarios):
        """Muestra el menu del profesor"""
        """