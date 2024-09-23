# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 21:01:17 2024

@author: jama2
"""
# El conocimiento proviene de expertos humanos que dominan el campo en cuestión.
# Se recopila a través de entrevistas, cuestionarios o técnicas como el análisis de tareas. 
# Este conocimiento es codificado en forma de reglas, hechos, heurísticas o modelos en la base de conocimiento.

# ¿Qué?: Extraer el conocimiento tácito y explícito que posee un experto humano.
# ¿Para qué?: Capturar la experiencia y razonamiento del experto para que el 
# sistema pueda replicar su proceso de toma de decisiones.
# ¿Cómo?: Se emplean técnicas como entrevistas estructuradas, observación 
# directa y retroalimentación constante para formalizar el conocimiento en términos computacionales.
# # Base de conocimiento (reglas proporcionadas por un experto)
def diagnostico_sistema_experto(sintomas):
    if 'fiebre' in sintomas and 'tos' in sintomas:
        return "Posible diagnóstico: Gripe"
    elif 'fiebre' in sintomas and 'dolor muscular' in sintomas:
        return "Posible diagnóstico: Dengue"
    elif 'tos' in sintomas and 'dificultad para respirar' in sintomas:
        return "Posible diagnóstico: Neumonía"
    else:
        return "Los síntomas no corresponden a un diagnóstico conocido"

# Interfaz con el usuario
sintomas = ['fiebre', 'tos']  # Ejemplo de entrada de síntomas
diagnostico = diagnostico_sistema_experto(sintomas)
print(diagnostico)

