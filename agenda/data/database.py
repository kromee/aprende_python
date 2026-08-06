import sqlite3
from contactos.models import Contacto
from datetime import datetime

DB_PATH = "agenda.db"

def _conectar():
    return sqlite3.connect(DB_PATH)

def inicializar():
    with _conectar() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS contactos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                telefono TEXT,
                email TEXT UNIQUE,
                nacimiento TEXT
            )
        """)
        conn.commit()

def guardar(contacto: Contacto):
    with _conectar() as conn:
        conn.execute(
            "INSERT INTO contactos (nombre, telefono, email, nacimiento) VALUES (?, ?, ?, ?)",
            (contacto.nombre, contacto.telefono, contacto.email, contacto.nacimiento.strftime("%Y-%m-%d"))
        )
        conn.commit()

def cargar() -> list[Contacto]:
    with _conectar() as conn:
        cursor = conn.execute("SELECT nombre, telefono, email, nacimiento FROM contactos")
        filas = cursor.fetchall()
        
        contactos = []
        for fila in filas:
            contactos.append(Contacto(
                nombre=fila[0],
                telefono=fila[1],
                email=fila[2],
                nacimiento=datetime.strptime(fila[3], "%Y-%m-%d")
            ))
        return contactos

def buscar(nombre: str) -> list[Contacto]:
    with _conectar() as conn:
        cursor = conn.execute(
            "SELECT nombre, telefono, email, nacimiento FROM contactos WHERE nombre LIKE ?",
            (f"%{nombre}%",)
        )
        filas = cursor.fetchall()
        
        contactos = []
        for fila in filas:
            contactos.append(Contacto(
                nombre=fila[0],
                telefono=fila[1],
                email=fila[2],
                nacimiento=datetime.strptime(fila[3], "%Y-%m-%d")
            ))
        return contactos

def eliminar_por_email(email: str):
    with _conectar() as conn:
        cursor = conn.execute("DELETE FROM contactos WHERE email = ?", (email,))
        conn.commit()
        return cursor.rowcount  # Devuelve cuántos se eliminaron

def editar(email: str, campo: str, nuevo_valor: str):
    with _conectar() as conn:
        # Validar que el campo sea seguro (evitar SQL injection en el nombre de columna)
        campos_permitidos = {"nombre", "telefono", "email"}
        if campo not in campos_permitidos:
            return False
        
        conn.execute(
            f"UPDATE contactos SET {campo} = ? WHERE email = ?",
            (nuevo_valor, email)
        )
        conn.commit()
        return True