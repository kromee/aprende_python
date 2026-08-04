from .models import Contacto

class Agenda: 

    def __init__(self):
        self.contactos: list[Contacto] = []

    def agregar(self, contacto: Contacto):
        self.contactos.append(contacto)



    def eliminar_contacto(self, nombre):
        self.contactos = [c for c in self.contactos if c.nombre != nombre]

    def listar(self):
        for c in self.contactos:
            print(f"{c.nombre} | {c.telefono} | {c.email}")


    def buscar(self, nombre: str):
        return [c for c in self.contactos if nombre.lower() in c.nombre.lower()]


