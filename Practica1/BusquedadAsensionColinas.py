# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:06:54 2024

@author: jama2
"""
'''
Este código genera y evalúa horarios de clases utilizando el algoritmo de 
ascenso de colinas. Se asignan clases a franjas horarias en función de su 
disponibilidad, buscando minimizar conflictos (clases que coinciden en la misma franja). 
El código genera horarios vecinos modificados y adopta el mejor horario encontrado 
tras un número determinado de iteraciones.
'''

import random  # Importamos el módulo random para generar valores aleatorios

# Definimos las clases y sus características
classes = [
    {"name": "Control2", "duration": 2, "available_days": ["Lunes", "Miércoles"]},  # Clase Control2, duración 2 horas, disponible lunes y miércoles
    {"name": "SistemasExpertos", "duration": 1, "available_days": ["Martes", "Jueves"]},  # Clase Sistemas Expertos, duración 1 hora, disponible martes y jueves
    {"name": "MicroRobotica", "duration": 3, "available_days": ["Lunes", "Viernes"]},  # Clase MicroRobótica, duración 3 horas, disponible lunes y viernes
    {"name": "IngenieraEconomica", "duration": 2, "available_days": ["Martes", "Jueves"]},  # Clase Ingeniería Económica, duración 2 horas, disponible martes y jueves
    {"name": "Calidad", "duration": 1, "available_days": ["Miércoles", "Viernes"]}  # Clase Calidad, duración 1 hora, disponible miércoles y viernes
]

# Definimos el horario con 5 días y 3 franjas horarias por día
schedule = [
    {"day": "Lunes", "slots": [{"start": 9, "end": 11}, {"start": 11, "end": 12}, {"start": 2, "end": 4}]},  # Lunes tiene 3 franjas: 9-11, 11-12 y 2-4
    {"day": "Martes", "slots": [{"start": 9, "end": 10}, {"start": 10, "end": 12}, {"start": 2, "end": 3}]},  # Martes tiene 3 franjas: 9-10, 10-12 y 2-3
    {"day": "Miércoles", "slots": [{"start": 9, "end": 11}, {"start": 11, "end": 12}, {"start": 2, "end": 3}]},  # Miércoles tiene 3 franjas: 9-11, 11-12 y 2-3
    {"day": "Jueves", "slots": [{"start": 9, "end": 10}, {"start": 10, "end": 12}, {"start": 2, "end": 3}]},  # Jueves tiene 3 franjas: 9-10, 10-12 y 2-3
    {"day": "Viernes", "slots": [{"start": 9, "end": 12}, {"start": 2, "end": 3}]}  # Viernes tiene 2 franjas: 9-12 y 2-3
]

# Función para evaluar la calidad del horario
def evaluate_schedule(schedule):
    conflicts = 0  # Inicializamos un contador de conflictos
    for day in schedule:  # Iteramos sobre cada día en el horario
        for slot in day["slots"]:  # Iteramos sobre cada franja horaria de ese día
            # Filtramos las clases que pueden darse en esa franja y día
            classes_in_slot = [class_ for class_ in classes if class_["available_days"].count(day["day"]) > 0 and slot["start"] <= class_["duration"] <= slot["end"]]
            # Si hay más de una clase asignada a la misma franja horaria, hay un conflicto
            if len(classes_in_slot) > 1:
                conflicts += 1  # Aumentamos el número de conflictos
    return -conflicts  # Devolvemos el número negativo de conflictos para maximizar la calidad (menos conflictos es mejor)

# Función para generar un vecino del horario actual
def generate_neighbor(schedule):
    # Seleccionamos un día aleatorio
    day_index = random.randint(0, len(schedule) - 1)
    # Seleccionamos una franja horaria aleatoria de ese día
    slot_index = random.randint(0, len(schedule[day_index]["slots"]) - 1)
    # Seleccionamos una clase aleatoria
    class_index = random.randint(0, len(classes) - 1)
    new_schedule = schedule.copy()  # Hacemos una copia del horario
    # Asignamos una clase aleatoria a esa franja horaria del horario copiado
    new_schedule[day_index]["slots"][slot_index]["class"] = classes[class_index]
    return new_schedule  # Devolvemos el nuevo horario generado

# Función para realizar la búsqueda de ascenso de colinas
def hill_climbing(schedule, max_iterations=1000):
    current_schedule = schedule  # Inicializamos el horario actual con el horario proporcionado
    current_quality = evaluate_schedule(current_schedule)  # Evaluamos la calidad del horario actual
    for _ in range(max_iterations):  # Repetimos el proceso un número máximo de iteraciones
        neighbor = generate_neighbor(current_schedule)  # Generamos un horario vecino (modificado)
        neighbor_quality = evaluate_schedule(neighbor)  # Evaluamos la calidad del horario vecino
        if neighbor_quality > current_quality:  # Si el vecino es mejor, lo adoptamos
            current_schedule = neighbor  # El horario actual se actualiza con el vecino
            current_quality = neighbor_quality  # Actualizamos la calidad del horario actual
    return current_schedule  # Devolvemos el mejor horario encontrado

# Ejecutamos la búsqueda de ascenso de colinas
best_schedule = hill_climbing(schedule)  # Buscamos el mejor horario posible

# Imprimimos el horario óptimo encontrado
for day in best_schedule:  # Iteramos sobre cada día en el mejor horario encontrado
    print(f"Día: {day['day']}")  # Imprimimos el nombre del día
    for slot in day["slots"]:  # Iteramos sobre cada franja horaria de ese día
        # Imprimimos la franja horaria y la clase asignada, o 'Libre' si no hay clase asignada
        print(f"  {slot['start']}-{slot['end']}: {slot.get('class', {}).get('name', 'Libre')}")
    print()  # Añadimos una línea en blanco después de cada día
