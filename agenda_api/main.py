from fastapi import FastAPI
from database import inicializar, cargar, guardar
from models import Contacto

app = FastAPI()

inicializar()

@app.get("/")
def inicio():
    return {"mensaje": "Agenda API con SQLite"}

@app.get("/contactos")
def listar_contactos():
    contactos_db = cargar()
    resultado = []
    for c in contactos_db:
        resultado.append(Contacto(
            nombre=c.nombre,
            telefono=c.telefono,
            email=c.email,
            nacimiento=c.nacimiento.strftime("%Y-%m-%d")
        ))
    return resultado

@app.post("/contactos")
def crear_contacto(contacto: Contacto):
    from datetime import datetime
    from database import ContactoDB
    
    nuevo = ContactoDB(
        nombre=contacto.nombre,
        telefono=contacto.telefono,
        email=contacto.email,
        nacimiento=datetime.strptime(contacto.nacimiento, "%Y-%m-%d")
    )
    guardar(nuevo)
    return {"mensaje": f"✅ {contacto.nombre} creado correctamente"}