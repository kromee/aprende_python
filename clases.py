class Persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
         print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")



# Crear y usar:
persona1 = Persona("Ana", 25)
persona2 = Persona("Luis", 30)

persona1.presentarse()
persona2.presentarse()