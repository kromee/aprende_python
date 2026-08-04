import json
from datetime import datetime
from contactos.models import Contacto


ARCHIVO = "contactos.json"


def guardar_contactos(contactos: list[Contacto]):
    datos = []
    for contacto in contactos:
        datos.append({
            "nombre": contacto.nombre,
            "telefono": contacto.telefono,
            "email": contacto.email,
            "fecha_nacimiento": contacto.fecha_nacimiento.strftime("%Y-%m-%d")
        })
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)

def cargar() -> list[Contacto]:
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            datos = json.load(f)
    except FileNotFoundError:
        return []
    contactos = []
    for d in datos:

    return contactos
