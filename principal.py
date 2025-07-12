class Estudiante:
    def __init__(self, nombre, carnet, carrera, notaFinal):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.notaFinal = notaFinal
    def Informacion(self):
        print(f"Soy el estudiante {self.nombre}, con numero de carné {self.carnet} y curso la carrera de {self.carrera}" )



print("Actividad 05")
print("Bienvenido a nuestro programa.")
print("1.- Registrar un nuevo estudiante")
print("2.- Mostrar lista de todos los estudiantes registrados")
print("3.- Buscar un estudiante por su Carné")
print("4.- Calcular el promedio de notas de todos los estudiantes")
print("Seleccione la opcion que deseea ")
