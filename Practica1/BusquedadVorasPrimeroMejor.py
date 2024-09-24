# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 08:49:19 2024

@author: jama2
"""
'''
Este código implementa una asignación de recursos utilizando un enfoque basado 
en la búsqueda voraz (GBFS, Greedy Best-First Search). El objetivo es asignar 
vuelos a pistas de aterrizaje en función del tiempo más corto posible para 
aterrizar, respetando la disponibilidad de las pistas.
'''
import heapq
import copy

# Definimos la función para asignar recursos con GBFS
def assign_resources(flights, runways):
    # Inicializamos la cola de prioridad con los vuelos y sus respectivos tiempos de aterrizaje
    priority_queue = [(flight['time'], flight['id'], flight['runways']) for flight in flights]
    heapq.heapify(priority_queue)

    # Inicializamos la asignación de recursos
    assignment = {}
    runway_status = {runway['id']: 0 for runway in runways}  # Tiempo disponible de cada pista

    # Mientras haya vuelos en la cola de prioridad
    while priority_queue:
        # Seleccionamos el vuelo con el menor tiempo de aterrizaje
        time, flight_id, available_runways = heapq.heappop(priority_queue)

        # Seleccionamos la pista de aterrizaje que puede recibir el vuelo más rápido
        available_runways_copy = copy.deepcopy(available_runways)
        runway = min(available_runways_copy, key=lambda x: max(runway_status[x['id']], x['time']))

        # Asignamos el vuelo a la pista de aterrizaje
        assignment[flight_id] = runway['id']

        # Actualizamos el tiempo disponible de la pista de aterrizaje
        runway_status[runway['id']] = max(runway_status[runway['id']], time) + runway['time']

    return assignment

# Definimos los vuelos y pistas de aterrizaje
flights = [
    {'id': 1, 'time': 10, 'runways': [{'id': 'A', 'time': 5}, {'id': 'B', 'time': 7}, {'id': 'C', 'time': 9}]},
    {'id': 2, 'time': 8, 'runways': [{'id': 'B', 'time': 4}, {'id': 'D', 'time': 6}, {'id': 'E', 'time': 8}]},
    {'id': 3, 'time': 12, 'runways': [{'id': 'A', 'time': 6}, {'id': 'C', 'time': 8}, {'id': 'D', 'time': 10}]},
    {'id': 4, 'time': 6, 'runways': [{'id': 'B', 'time': 3}, {'id': 'E', 'time': 5}]},
    {'id': 5, 'time': 15, 'runways': [{'id': 'A', 'time': 8}, {'id': 'C', 'time': 10}]},
    {'id': 6, 'time': 10, 'runways': [{'id': 'B', 'time': 5}, {'id': 'D', 'time': 7}]},
    {'id': 7, 'time': 8, 'runways': [{'id': 'A', 'time': 4}, {'id': 'E', 'time': 6}]},
    {'id': 8, 'time': 12, 'runways': [{'id': 'C', 'time': 6}, {'id': 'D', 'time': 8}]},
    {'id': 9, 'time': 6, 'runways': [{'id': 'B', 'time': 3}, {'id': 'C', 'time': 5}]},
    {'id': 10, 'time': 15, 'runways': [{'id': 'A', 'time': 8}, {'id': 'D', 'time': 10}]}
]

runways = [
    {'id': 'A', 'time': 0},
    {'id': 'B', 'time': 0},
    {'id': 'C', 'time': 0},
    {'id': 'D', 'time': 0},
    {'id': 'E', 'time': 0}
]

# Ejecutamos la función para asignar recursos con GBFS
assignment = assign_resources(flights, runways)

# Imprimimos la asignación de recursos
print("Asignación de recursos:")
for flight_id, runway_id in assignment.items():
    print(f"Vuelo {flight_id} asignado a pista de aterrizaje {runway_id}")
