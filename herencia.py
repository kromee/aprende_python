class Persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
          return f"Hola, me llamo {self.nombre} y tengo {self.edad} años"

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        return f"Hola, me llamo {self.nombre}, tengo {self.edad} años y estudio {self.carrera}"

#Pruebas 
est= Estudiante("Carlos", 20, "Ingeniería")
print(est.presentarse())
print(est.estudiar())
