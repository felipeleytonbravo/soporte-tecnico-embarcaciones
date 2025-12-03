# Soporte Técnico Embarcaciones

Proyecto en Python para gestionar embarcaciones: permite registrar embarcaciones, agregar tripulación y pasajeros, y ver el estado mediante un menú interactivo en terminal.

## Qué hace

- Registrar embarcaciones con nombre, tipo y capacidad.  
- Agregar tripulantes a una embarcación.  
- Agregar pasajeros a una embarcación (respetando la capacidad).  
- Ver listado de todas las embarcaciones registradas, con su tripulación y pasajeros.  
- Menú interactivo simple desde terminal.

## Estructura del proyecto

- `soporte_tecnico.py` — script principal con menú interactivo.  
- `README.md` — documentación con instrucciones y ejemplo de uso.

## Cómo usar

1. Asegúrate de tener Python 3.8 o superior.  
2. Ejecuta desde la terminal:

```bash
python soporte_tecnico.py
Sigue el menú interactivo para registrar embarcaciones, tripulantes y pasajeros.

Ejemplo de ejecución
=== MENÚ SOPORTE TÉCNICO ===
1. Agregar embarcación
2. Mostrar embarcaciones
3. Agregar tripulante
4. Agregar pasajero
5. Salir
Selecciona una opción (1-5):


Luego de agregar una embarcación y un pasajero, la salida sería:

Nombre de la embarcación: Navega Uno
Tipo de embarcación: Yate
Capacidad de pasajeros: 5

Embarcación 'Navega Uno' agregada correctamente.

Nombre de la embarcación: Navega Uno
Nombre del pasajero: Pedro

Pasajero 'Pedro' agregado a 'Navega Uno'.

Listado de embarcaciones:
1. Navega Uno — Tipo: Yate — Capacidad: 5
   Tripulación: Ninguna
   Pasajeros: Pedro

Requisitos

Python 3.8+

Librerías estándar de Python (ninguna externa)

Autor

Felipe Leyton Bravo
