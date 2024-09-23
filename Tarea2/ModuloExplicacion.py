# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 21:35:21 2024

@author: jama2
"""
# El Módulo de Explicación es crucial para ofrecer transparencia en el proceso 
# de razonamiento del sistema experto, ya que explica por qué el sistema tomó una decisión específica.

# ¿Qué es?: Es el componente que proporciona al usuario una explicación de las 
# conclusiones del sistema experto.
# ¿Para qué sirve?: Facilita que el usuario entienda y confíe en las decisiones o 
# recomendaciones del sistema, proporcionando una descripción clara de cómo se alcanzó una solución.
# ¿Cómo funciona?: Después de que el motor de inferencia produce una conclusión, 
# el módulo de explicación utiliza las reglas aplicadas y los hechos relevantes 
# para generar una explicación detallada de cómo se llegó a esa conclusión.

# Módulo de Explicación
def modulo_de_explicacion(diagnostico):
    if diagnostico == "gripe":
        return "La gripe se diagnosticó debido a la presencia de fiebre, tos y dolor de cabeza."
    elif diagnostico == "resfriado":
        return "El resfriado se diagnosticó debido a la presencia de tos, congestión nasal y dolor de garganta."
    elif diagnostico == "alergia":
        return "La alergia se diagnosticó debido a la congestión nasal, estornudos y picazón en los ojos."
    else:
        return "No se pudo determinar un diagnóstico claro."

# Ejemplo de uso del módulo de explicación:
diagnostico = "gripe"  # Esto vendría del motor de inferencia
explicacion = modulo_de_explicacion(diagnostico)

print(f"Explicación: {explicacion}")
