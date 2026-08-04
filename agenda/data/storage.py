import json
from datetime import datetime
from contactos.models import Contacto


ARCHIVO = "contactos.json"


def guardar(contactos: list[Contacto]):
    datos = []
    for c in contactos:
        datos.append({
           "nombre": c.nombre,
            "telefono": c.telefono,
            "email": c.email,
            "nacimiento": c.nacimiento.strftime("%Y-%m-%d")
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
        contactos.append(Contacto(
            nombre=d["nombre"],
            telefono=d["telefono"],
            email=d["email"],   
            fecha_nacimiento=datetime.strptime(d["fecha_nacimiento"], "%Y-%m-%d")
        ))
    return contactos
