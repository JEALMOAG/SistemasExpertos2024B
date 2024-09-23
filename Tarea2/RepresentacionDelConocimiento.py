# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 21:30:21 2024

@author: jama2
"""

# Módulo de adquisición de conocimiento
def adquirir_conocimiento():
    base_de_conocimiento = []
    while True:
        condicion = input("Introduce la condición (ej. fiebre, tos, etc.): ")
        conclusion = input(f"Introduce la conclusión asociada a la condición '{condicion}': ")
        regla = {'condicion': condicion, 'conclusion': conclusion}
        base_de_conocimiento.append(regla)
        continuar = input("¿Deseas agregar otra regla? (s/n): ")
        if continuar.lower() != 's':
            break
    return base_de_conocimiento

# Base de conocimiento
def mostrar_base_de_conocimiento(base_de_conocimiento):
    print("\nBase de conocimiento actual:")
    for i, regla en enumerate(base_de_conocimiento, 1):
        print(f"Regla {i}: Si '{regla['condicion']}', entonces '{regla['conclusion']}'.")

# Base de hechos
def agregar_hechos():
    hechos = []
    while True:
        hecho = input("Introduce un hecho actual (ej. fiebre, tos, etc.): ")
        hechos.append(hecho)
        continuar = input("¿Deseas agregar otro hecho? (s/n): ")
        if continuar.lower() != 's':
            break
    return hechos

# Inferencia
def inferencia(base_de_conocimiento, hechos):
    for hecho in hechos:
        for regla in base_de_conocimiento:
            if hecho == regla['condicion']:
                print(f"Se ha inferido: Si '{hecho}', entonces '{regla['conclusion']}'.")

# Flujo completo del sistema experto
base_de_conocimiento = adquirir_conocimiento()
mostrar_base_de_conocimiento(base_de_conocimiento)
hechos = agregar_hechos()
inferencia(base_de_conocimiento, hechos)