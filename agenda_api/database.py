import sqlite3
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ContactoDB:
    nombre: str
    telefono: str
    email: str
    nacimiento: datetime

DB_PATH = "agenda.db"

def inicializar():
    with sqlite3.connect(DB_PATH) as conn:
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

def cargar():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("SELECT nombre, telefono, email, nacimiento FROM contactos")
        filas = cursor.fetchall()
        
        contactos = []
        for fila in filas:
            contactos.append(ContactoDB(
                nombre=fila[0],
                telefono=fila[1],
                email=fila[2],
                nacimiento=datetime.strptime(fila[3], "%Y-%m-%d")
            ))
        return contactos

def guardar(contacto: ContactoDB):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO contactos (nombre, telefono, email, nacimiento) VALUES (?, ?, ?, ?)",
            (contacto.nombre, contacto.telefono, contacto.email, contacto.nacimiento.strftime("%Y-%m-%d"))
        )
        conn.commit()

def buscar_por_email(email: str):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(
            "SELECT nombre, telefono, email, nacimiento FROM contactos WHERE email = ?",
            (email,)
        )
        fila = cursor.fetchone()
        if fila is None:
            return None
        return ContactoDB(
            nombre=fila[0],
            telefono=fila[1],
            email=fila[2],
            nacimiento=datetime.strptime(fila[3], "%Y-%m-%d")
        )

def editar(email: str, campo: str, nuevo_valor: str):
    campos_permitidos = {"nombre", "telefono", "email"}
    if campo not in campos_permitidos:
        return False
    
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            f"UPDATE contactos SET {campo} = ? WHERE email = ?",
            (nuevo_valor, email)
        )
        conn.commit()
        return True

def eliminar_por_email(email: str):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("DELETE FROM contactos WHERE email = ?", (email,))
        conn.commit()
        return cursor.rowcount > 0