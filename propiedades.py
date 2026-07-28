class Persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

## vamos a trabajar con propiedades, para ello vamos a crear un método que nos permita obtener la edad de la persona y otro método que nos permita establecer la edad de la persona.

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if len(valor) > 0:
            self._nombre = valor
        else:
            raise ValueError("El nombre no puede estar vacío")

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor >= 0:
            self._edad = valor
        else:
            raise ValueError("La edad no puede ser negativa")


p = Persona("Carlos", 25)

# Leer propiedades (como atributos, no métodos):
print(p.nombre)   # Debe imprimir: Carlos
print(p.edad)     # Debe imprimir: 25

    # Modificar propiedades:
p.nombre = "Ana"
p.edad = 30
print(p.nombre)   # Debe imprimir: Ana
print(p.edad)     # Debe imprimir: 30

# Esto debe fallar (descomenta y prueba):
 p.edad = -5     # ValueError: La edad no puede ser negativa
