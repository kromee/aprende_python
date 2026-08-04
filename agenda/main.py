from contactos.models import Contacto
from contactos.manager import Agenda
from data.storage import guardar, cargar
from datetime import datetime

# Cargar al iniciar
mi_agenda = Agenda()
mi_agenda.contactos = cargar()

print("=" * 30)
print("📒 AGENDA DE CONTACTOS")
print("=" * 30)

while True:
    print("\n1. Agregar contacto")
    print("2. Listar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    print("6. Editar contacto")

    opcion = input("\nElige una opción (1-5): ")

    if opcion == "1":
        print("\n--- Nuevo contacto ---")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        fecha_str = input("Fecha nacimiento (AAAA-MM-DD): ")
        
        try:
            nacimiento = datetime.strptime(fecha_str, "%Y-%m-%d")
            contacto = Contacto(nombre, telefono, email, nacimiento)
            mi_agenda.agregar(contacto)
            print(f"✅ {nombre} agregado correctamente")
        except ValueError:
            print("❌ Fecha inválida. Usa el formato AAAA-MM-DD")

    elif opcion == "2":
        print("\n--- Contactos ---")
        if len(mi_agenda.contactos) == 0:
            print("No hay contactos")
        else:
            mi_agenda.listar()

    elif opcion == "3":
        print("\n--- Buscar ---")
        nombre = input("Nombre a buscar: ")
        resultados = mi_agenda.buscar(nombre)
        if len(resultados) == 0:
            print("No se encontraron resultados")
        else:
            for r in resultados:
                print(f"🔍 {r.nombre} | {r.telefono} | {r.email}")

    elif opcion == "4":
        print("\n--- Eliminar ---")
        nombre = input("Nombre a eliminar: ")
        mi_agenda.eliminar(nombre)

    elif opcion == "5":
        guardar(mi_agenda.contactos)
        print("\n💾 Contactos guardados. ¡Hasta luego!")
        break
    
    elif opcion == "6":
        print("\n--- Editar ---")
        nombre = input("Nombre del contacto a editar: ")
        print("Campos: nombre, telefono, email, nacimiento")
        campo = input("¿Qué campo quieres editar? ")
        nuevo_valor = input("Nuevo valor: ")
        
        if campo == "nacimiento":
            try:
                nuevo_valor = datetime.strptime(nuevo_valor, "%Y-%m-%d")
            except ValueError:
                print("❌ Fecha inválida")
                continue
        
        mi_agenda.editar(nombre, campo, nuevo_valor)

    else:
        print("❌ Opción no válida")