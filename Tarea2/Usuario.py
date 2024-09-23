# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 22:29:05 2024

@author: jama2
"""

# El usuario es la persona que interactúa con el sistema experto para obtener 
# soluciones o recomendaciones. La interacción se basa en un ciclo continuo de 
# entrada y salida de información, donde el usuario proporciona hechos o datos 
# específicos, y el sistema devuelve conclusiones basadas en esos datos.

# ¿Qué es?: El usuario es el receptor de los resultados del sistema experto y 
# también el proveedor de los hechos necesarios para que el sistema funcione.
# ¿Para qué sirve?: El usuario utiliza el sistema para resolver problemas específicos. 
# Dependiendo del tipo de sistema experto, el usuario podría ser un médico, un ingeniero, 
# un abogado, o cualquier persona que necesite asistencia en la toma de decisiones.
# ¿Cómo funciona?: El usuario interactúa con el sistema ingresando hechos o datos 
# específicos (como síntomas, situaciones o condiciones), y el sistema utiliza ese 
# conocimiento para hacer inferencias basadas en la base de conocimiento. Luego, el 
# usuario recibe una recomendación o conclusión acompañada, en muchos casos, de una 
# explicación de cómo se llegó a esa respuesta


# Función que simula la interacción con el usuario
def interfaz_usuario():
    print("Bienvenido al sistema de diagnóstico médico.")
    print("Por favor, ingrese sus síntomas (separados por comas):")
    
    # Leer los síntomas del usuario
    entrada_usuario = input().lower().strip()
    
    # Procesar la entrada y devolver una lista de síntomas
    sintomas = [sintoma.strip() for sintoma in entrada_usuario.split(",")]
    
    return sintomas

# Ejemplo de uso de la interfaz de usuario
sintomas_ingresados = interfaz_usuario()

# Mostrar los síntomas ingresados
print(f"Síntomas ingresados: {sintomas_ingresados}")
