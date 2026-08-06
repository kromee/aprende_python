from data.database import inicializar, guardar, cargar
from contactos.models import Contacto
from datetime import datetime

inicializar()  # Crea la tabla si no existe

c1 = Contacto("Ana López", "555-1234", "ana@email.com", datetime(1990, 5, 15))
guardar(c1)

contactos = cargar()
for c in contactos:
    print(f"{c.nombre} | {c.email}")