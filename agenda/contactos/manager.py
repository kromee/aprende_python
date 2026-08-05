from .models import Contacto

class Agenda: 

    def __init__(self):
        self.contactos: list[Contacto] = []

    def agregar(self, contacto: Contacto):
        for c in self.contactos:
            if c.email == contacto.email:
                print(f"❌ Ya existe un contacto con el email: {contacto.email}")
                return False
        
        self.contactos.append(contacto)
        print(f"✅ {contacto.nombre} agregado correctamente")
        return True



    def eliminar_contacto(self, nombre):
        self.contactos = [c for c in self.contactos if c.nombre != nombre]

    def listar(self):
        for c in self.contactos:
            print(f"{c.nombre} | {c.telefono} | {c.email}")


    def buscar(self, nombre: str):
        return [c for c in self.contactos if nombre.lower() in c.nombre.lower()]

    def eliminar(self, nombre: str):
        encontrados = self.buscar(nombre)
        if len(encontrados) == 0:
            print(f"❌ No se encontró '{nombre}'")
            return False
        
        for e in encontrados:
            self.contactos.remove(e)
            print(f"✅ Eliminado: {e.nombre}")
        
        return True

    def editar(self, nombre: str, campo: str, nuevo_valor):
        encontrados = self.buscar(nombre)
        if len(encontrados) == 0:
            print(f"❌ No se encontró '{nombre}'")
            return False
        
        contacto = encontrados[0]
        
        if campo == "nombre":
            contacto.nombre = nuevo_valor
        elif campo == "telefono":
            contacto.telefono = nuevo_valor
        elif campo == "email":
            contacto.email = nuevo_valor
        elif campo == "nacimiento":
            contacto.nacimiento = nuevo_valor
        else:
            print("❌ Campo no válido. Opciones: nombre, telefono, email, nacimiento")
            return False
        
        print(f"✅ {contacto.nombre} actualizado correctamente")
        return True


