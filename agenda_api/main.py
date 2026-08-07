from fastapi import FastAPI, HTTPException
from database import inicializar, cargar, guardar, buscar_por_email, editar, eliminar_por_email
from models import Contacto
from datetime import datetime


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

@app.get("/contactos/{email}")
def obtener_contacto(email: str):
    c = buscar_por_email(email)
    if c is None:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    
    return Contacto(
        nombre=c.nombre,
        telefono=c.telefono,
        email=c.email,
        nacimiento=c.nacimiento.strftime("%Y-%m-%d")
    )

@app.post("/contactos")
def crear_contacto(contacto: Contacto):
    from database import ContactoDB
    
    if buscar_por_email(contacto.email):
        raise HTTPException(status_code=400, detail="Ya existe un contacto con ese email")
    
    nuevo = ContactoDB(
        nombre=contacto.nombre,
        telefono=contacto.telefono,
        email=contacto.email,
        nacimiento=datetime.strptime(contacto.nacimiento, "%Y-%m-%d")
    )
    guardar(nuevo)
    return {"mensaje": f"✅ {contacto.nombre} creado correctamente"}

@app.put("/contactos/{email}")
def actualizar_contacto(email: str, campo: str, nuevo_valor: str):
    c = buscar_por_email(email)
    if c is None:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    
    exito = editar(email, campo, nuevo_valor)
    if not exito:
        raise HTTPException(status_code=400, detail="Campo no válido")
    
    return {"mensaje": f"✅ {c.nombre} actualizado correctamente"}

@app.delete("/contactos/{email}")
def borrar_contacto(email: str):
    c = buscar_por_email(email)
    if c is None:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    
    eliminar_por_email(email)
    return {"mensaje": f"✅ {c.nombre} eliminado correctamente"}
