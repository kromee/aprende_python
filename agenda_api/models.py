from pydantic import BaseModel

class Contacto(BaseModel):
    nombre: str
    telefono: str
    email: str
    nacimiento: str


