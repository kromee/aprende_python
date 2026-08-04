from contactos.models  import Contacto
from contactos.manager import Agenda
from datetime import datetime




mi_agenda = Agenda()

c1 = Contacto("Ana López", "555-1234", "ana@email.com", datetime(1990, 5, 15))

c2 = Contacto("Luis Pérez", "555-5678", "luis@email.com", datetime(1985, 8, 20))

mi_agenda.agregar(c1)
mi_agenda.agregar(c2)


print("--- Lista de contactos ---")
mi_agenda.listar()

print("\n--- Búsqueda 'ana' ---")

resultados = mi_agenda.buscar("ana")
for r in resultados:
    print(r.nombre)