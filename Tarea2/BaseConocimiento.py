# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 21:14:02 2024

@author: jama2
"""
# La base de conocimiento es el almacén de todas las reglas, hechos y heurísticas 
# que el sistema experto utiliza para razonar.

# ¿Qué es?: Es el núcleo del sistema experto, donde se almacenan las reglas y 
# procedimientos necesarios para resolver problemas en un dominio específico.
# ¿Para qué sirve?: Permite que el sistema experto tenga acceso a las reglas y 
# conocimiento experto estructurado, lo que le permite realizar inferencias.
# ¿Cómo funciona?: La base de conocimiento generalmente contiene dos tipos de información:
# Conocimiento declarativo: Información sobre hechos (e.g., “si hay fiebre, puede ser gripe”).
# Conocimiento procedimental: Instrucciones sobre cómo hacer algo 
# (e.g., “para diagnosticar la enfermedad, primero verificar la temperatura del paciente”).

# Simulación de una Base de Conocimiento
def mostrar_base_de_conocimiento(base_de_conocimiento):
    print("\nBase de conocimiento actual:")
    for i, regla en enumerate(base_de_conocimiento, 1):
        print(f"Regla {i}: Si '{regla['condicion']}', entonces '{regla['conclusion']}'.")

# Mostrar la base de conocimiento adquirida
mostrar_base_de_conocimiento(base_de_conocimiento)
