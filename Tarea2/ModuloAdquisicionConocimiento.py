# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 21:10:14 2024

@author: jama2
"""
# Este módulo se encarga de obtener, estructurar y almacenar el conocimiento 
# que el sistema utilizará para realizar inferencias.

# ¿Qué es?: Es la parte del sistema encargada de interactuar con el experto 
# humano o con fuentes automáticas de datos (cognimático) para capturar el conocimiento necesario.
# ¿Para qué sirve?: Se utiliza para garantizar que el sistema disponga del 
# conocimiento más preciso y actualizado.
# ¿Cómo funciona?: El módulo de adquisición puede involucrar entrevistas, 
# análisis de datos históricos o incluso algoritmos de machine learning. 
# Los expertos humanos proporcionan las reglas y hechos que son convertidos 
# en una representación formal que el sistema puede usar.

# Simulación de adquisición de conocimiento desde un experto humano
def adquirir_conocimiento():
    base_de_conocimiento = []

    # Ejemplo de entrada manual del conocimiento (reglas)
    while True:
        condicion = input("Introduce la condición (ej. fiebre, tos, etc.): ")
        conclusion = input(f"Introduce la conclusión asociada a la condición '{condicion}': ")
        regla = {'condicion': condicion, 'conclusion': conclusion}
        
        base_de_conocimiento.append(regla)

        continuar = input("¿Deseas agregar otra regla? (s/n): ")
        if continuar.lower() != 's':
            break

    return base_de_conocimiento

# Llamada al módulo de adquisición de conocimiento
base_de_conocimiento = adquirir_conocimiento()
print("Base de conocimiento adquirida:", base_de_conocimiento)
