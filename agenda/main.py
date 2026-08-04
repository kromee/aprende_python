from contactos.models import Contacto
from contactos.manager import Agenda
from data.storage import guardar, cargar
from datetime import datetime

# 1. Cargar contactos existentes
contactos_guardados = cargar()
mi_agenda = Agenda()
mi_agenda.contactos = contactos_guardados

print(f"📂 Contactos cargados: {len(mi_agenda.contactos)}")

# 2. Agregar nuevos (solo si no existen, para no duplicar en cada prueba)
if len(mi_agenda.contactos) == 0:
    c1 = Contacto("Ana López", "555-1234", "ana@email.com", datetime(1990, 5, 15))
    c2 = Contacto("Luis Pérez", "555-5678", "luis@email.com", datetime(1985, 8, 20))
    mi_agenda.agregar(c1)
    mi_agenda.agregar(c2)

# 3. Listar antes
print("\n--- Antes de eliminar ---")
mi_agenda.listar()

# 4. Eliminar
print("\n--- Eliminando 'Ana' ---")
mi_agenda.eliminar("Ana")

# 5. Listar después
print("\n--- Después de eliminar ---")
mi_agenda.listar()

# 6. Guardar
guardar(mi_agenda.contactos)
print("\n💾 Contactos guardados")