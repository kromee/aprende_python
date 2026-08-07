import sqlite3
from dataclasses import dataclass
from datetime import datetime

# Definición interna (solo para usar dentro de este archivo)
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