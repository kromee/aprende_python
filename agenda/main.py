from contactos.models  import Contacto
from contactos.manager import Agenda
from datetime import datetime
from data.storage import guardar, cargar



# 1. Cargar contactos existentes (si hay)
contactos_guardados = cargar()
mi_agenda = Agenda()
mi_agenda.contactos = contactos_guardados


print(f"📂 Contactos cargados: {len(mi_agenda.contactos)}")


# 2. Agregar nuevos contactos
c1 = Contacto("Ana López", "555-1234", "ana@email.com", datetime(1990, 5, 15))
c2 = Contacto("Luis Pérez", "555-5678", "luis@email.com", datetime(1985, 8, 20))


mi_agenda.agregar(c1)
mi_agenda.agregar(c2)


# 3. Listar
print("\n--- Lista de contactos ---")
mi_agenda.listar()



# 4. Buscar
print("\n--- Búsqueda 'ana' ---")
resultados = mi_agenda.buscar("ana")
for r in resultados:
    print(r.nombre)


# 5. Guardar en JSON
guardar(mi_agenda.contactos)
print("\n💾 Contactos guardados en contactos.json")



