import sqlite3
from .models import Contacto
from data import database

class Agenda:
    def agregar(self, contacto: Contacto):
        try:
            database.guardar(contacto)
            print(f"✅ {contacto.nombre} agregado correctamente")
            return True
        except sqlite3.IntegrityError:
            print(f"❌ Ya existe un contacto con el email: {contacto.email}")
            return False
        except Exception as e:
            print(f"❌ Error al agregar: {e}")
            return False

    def listar(self):
        contactos = database.cargar()
        if len(contactos) == 0:
            print("No hay contactos")
            return
        
        for c in contactos:
            print(f"{c.nombre} | {c.telefono} | {c.email}")

    def buscar(self, nombre: str):
        return database.buscar(nombre)

    def eliminar(self, nombre: str):
        encontrados = self.buscar(nombre)
        if len(encontrados) == 0:
            print(f"❌ No se encontró '{nombre}'")
            return False
        
        for e in encontrados:
            database.eliminar_por_email(e.email)
            print(f"✅ Eliminado: {e.nombre}")
        
        return True

    def editar(self, nombre: str, campo: str, nuevo_valor):
        encontrados = self.buscar(nombre)
        if len(encontrados) == 0:
            print(f"❌ No se encontró '{nombre}'")
            return False
        
        contacto = encontrados[0]
        email_objetivo = contacto.email
        
        if campo == "nacimiento":
            print("❌ Para editar fecha, usa el email directamente")
            return False
        
        database.editar(email_objetivo, campo, nuevo_valor)
        print(f"✅ {contacto.nombre} actualizado correctamente")
        return True