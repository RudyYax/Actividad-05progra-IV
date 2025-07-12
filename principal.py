class Estudiante:
    def __init__(self, nombre, carnet, carrera, notaFinal):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.notaFinal = notaFinal
    def Informacion(self):
        print(f"Soy el estudiante {self.nombre}, con numero de carné {self.carnet} y curso la carrera de {self.carrera}")

    def Notafinal(self):
        print (f"La Nota Final es {self.notaFinal}")

estudiantes = []
opcion = 0
while(opcion != 5):
    print("Actividad 05")
    print("Bienvenido a nuestro programa.")
    print("1.- Registrar un nuevo estudiante")
    print("2.- Mostrar lista de todos los estudiantes registrados")
    print("3.- Buscar un estudiante por su Carné")
    print("4.- Calcular el promedio de notas de todos los estudiantes")
    opcion = int(input("Seleccione la opcion que desea "))

    match opcion:
        case 1:
            print("Ingrese el Nombre del estudiante.")
            nombre =input("Ingrese el Nombre del estudiante: ")
            print("Ingrese el nombre del estudiante")
            carnet = int(input("Ingrese el carné del estudiante: "))
            print("Ingrese la carrera del estudiante")
            carrera = input("Ingrese la carrera del estudiante: ")
            print("Ingrese la nota final del Estudiante")
            NotaFinal = int(input("Ingrese la nota final del Estudiante: "))
            estudiante = Estudiante(nombre, carnet, carrera, NotaFinal)
            estudiantes.append(estudiante)
            print("Estudiante registrado correctamente")




