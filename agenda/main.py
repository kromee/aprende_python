from contactos.models import Contacto
from contactos.manager import Agenda
from data.database import inicializar
from datetime import datetime

# Inicializar base de datos
inicializar()

mi_agenda = Agenda()

print("=" * 30)
print("📒 AGENDA DE CONTACTOS - SQLite")
print("=" * 30)

while True:
    print("\n1. Agregar contacto")
    print("2. Listar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    print("6. Editar contacto")

    opcion = input("\nElige una opción (1-6): ")

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
        except ValueError:
            print("❌ Fecha inválida. Usa el formato AAAA-MM-DD")

    elif opcion == "2":
        print("\n--- Contactos ---")
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
        print("\n💾 Datos guardados en SQLite. ¡Hasta luego!")
        break

    elif opcion == "6":
        print("\n--- Editar ---")
        nombre = input("Nombre del contacto a editar: ")
        print("Campos: nombre, telefono, email")
        campo = input("¿Qué campo quieres editar? ")
        nuevo_valor = input("Nuevo valor: ")
        mi_agenda.editar(nombre, campo, nuevo_valor)

    else:
        print("❌ Opción no válida")