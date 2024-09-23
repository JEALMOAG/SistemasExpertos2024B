# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 21:45:01 2024

@author: jama2
"""

# La Interfaz de Usuario es esencial para la interacción entre el sistema y el 
# usuario, permitiendo al usuario proporcionar hechos y recibir conclusiones de manera clara y amigable.

# ¿Qué es?: Es el medio a través del cual el usuario interactúa con el sistema, 
# ingresando hechos y recibiendo respuestas.
# ¿Para qué sirve?: Facilita la comunicación entre el sistema experto y el usuario, 
# permitiendo que el usuario ingrese información relevante (hechos) y reciba los 
# resultados del razonamiento del sistema.
# ¿Cómo funciona?: La interfaz puede ser gráfica (GUI) o basada en texto, y 
# permite que el usuario introduzca hechos (por ejemplo, síntomas médicos) 
# para que el sistema realice inferencias y devuelva una conclusión junto con una explicación.

# Interfaz de Usuario
def interfaz_usuario():
    print("Bienvenido al sistema de diagnóstico médico.")
    print("Por favor, ingrese sus síntomas (separados por comas):")
    
    # Leer los síntomas del usuario
    entrada_usuario = input().lower().split(", ")
    sintomas = [sintoma.strip() for sintoma in entrada_usuario]
    
    # Retorna los síntomas ingresados
    return sintomas

# Ejemplo de uso de la interfaz de usuario:
sintomas_ingresados = interfaz_usuario()

print(f"Síntomas ingresados: {sintomas_ingresados}")
