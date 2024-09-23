# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 21:40:01 2024

@author: jama2
"""
# El Motor de Inferencia es el núcleo lógico del sistema experto, 
# responsable de razonar y aplicar las reglas almacenadas en la base de conocimiento.

# ¿Qué es?: Es el componente encargado de aplicar las reglas de la 
# base de conocimiento sobre los hechos proporcionados por el usuario, generando nuevas conclusiones.
# ¿Para qué sirve?: El motor de inferencia realiza el procesamiento 
# de la información, haciendo deducciones o inferencias que simulan el razonamiento de un experto humano.
# ¿Cómo funciona?: El motor de inferencia puede trabajar de dos maneras:
# Encadenamiento hacia adelante (Forward Chaining): Parte de los hechos proporcionados por 
# el usuario y aplica las reglas para deducir conclusiones.
# Encadenamiento hacia atrás (Backward Chaining): Comienza con una posible conclusión o 
# hipótesis y trabaja hacia atrás para verificar si los hechos y reglas apoyan esa conclusión.

# Base de conocimiento: reglas
reglas = {
    "gripe": ["fiebre", "tos", "dolor de cabeza"],
    "resfriado": ["tos", "congestion nasal", "dolor de garganta"],
    "alergia": ["congestion nasal", "estornudos", "picazon en los ojos"]
}

# Motor de Inferencia
def motor_de_inferencia(sintomas):
    diagnostico = None
    for enfermedad, sintomas_enfermedad in reglas.items():
        if all(sintoma in sintomas for sintoma in sintomas_enfermedad):
            diagnostico = enfermedad
            break
    return diagnostico

# Ejemplo de uso del motor de inferencia:
sintomas = ["fiebre", "tos", "dolor de cabeza"]
diagnostico = motor_de_inferencia(sintomas)

print(f"Diagnóstico sugerido: {diagnostico.capitalize() if diagnostico else 'No se encontró un diagnóstico.'}")
