"""
Flujo de soporte técnico interactivo para registro de embarcaciones.
Permite registrar embarcaciones, tripulación y pasajeros,
y simular la gestión de incidencias.
"""

embarcaciones = []

def agregar_embarcacion():
    nombre = input("Nombre de la embarcación: ")
    tipo = input("Tipo de embarcación: ")
    while True:
        try:
            capacidad = int(input("Capacidad de pasajeros: "))
            break
        except ValueError:
            print("Ingresa un número válido para la capacidad.")
    embarcacion = {
        "nombre": nombre,
        "tipo": tipo,
        "capacidad": capacidad,
        "tripulacion": [],
        "pasajeros": []
    }
    embarcaciones.append(embarcacion)
    print(f"\nEmbarcación '{nombre}' agregada correctamente.\n")

def mostrar_embarcaciones():
    if not embarcaciones:
        print("\nNo hay embarcaciones registradas.\n")
        return
    print("\nListado de embarcaciones:")
    for i, e in enumerate(embarcaciones, 1):
        print(f"{i}. {e['nombre']} - Tipo: {e['tipo']} - Capacidad: {e['capacidad']}")
        print(f"   Tripulación: {', '.join(e['tripulacion']) if e['tripulacion'] else 'Ninguna'}")
        print(f"   Pasajeros: {', '.join(e['pasajeros']) if e['pasajeros'] else 'Ninguno'}")
    print("")

def agregar_tripulante():
    nombre = input("Nombre de la embarcación: ")
    tripulante = input("Nombre del tripulante: ")
    for e in embarcaciones:
        if e["nombre"].lower() == nombre.lower():
            e["tripulacion"].append(tripulante)
            print(f"\nTripulante '{tripulante}' agregado a '{nombre}'.\n")
            return
    print(f"\nNo se encontró la embarcación '{nombre}'.\n")

def agregar_pasajero():
    nombre = input("Nombre de la embarcación: ")
    pasajero = input("Nombre del pasajero: ")
    for e in embarcaciones:
        if e["nombre"].lower() == nombre.lower():
            if len(e["pasajeros"]) < e["capacidad"]:
                e["pasajeros"].append(pasajero)
                print(f"\nPasajero '{pasajero}' agregado a '{nombre}'.\n")
            else:
                print(f"\nCapacidad máxima alcanzada en '{nombre}'.\n")
            return
    print(f"\nNo se encontró la embarcación '{nombre}'.\n")

def menu():
    while True:
        print("=== MENÚ SOPORTE TÉCNICO ===")
        print("1. Agregar embarcación")
        print("2. Mostrar embarcaciones")
        print("3. Agregar tripulante")
        print("4. Agregar pasajero")
        print("5. Salir")
        opcion = input("Selecciona una opción (1-5): ")
        if opcion == "1":
            agregar_embarcacion()
        elif opcion == "2":
            mostrar_embarcaciones()
        elif opcion == "3":
            agregar_tripulante()
        elif opcion == "4":
            agregar_pasajero()
        elif opcion == "5":
            print("\nSaliendo del sistema de soporte técnico. ¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Intenta de nuevo.\n")

if __name__ == "__main__":
    menu()
