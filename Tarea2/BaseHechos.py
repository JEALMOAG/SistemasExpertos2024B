# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 21:19:47 2024

@author: jama2
"""
# La base de hechos contiene los hechos específicos de cada caso o 
# problema que se está resolviendo en un momento dado.

# ¿Qué es?: Es un almacén temporal que contiene la información relevante 
# para el problema que se está resolviendo en ese instante. A diferencia 
# de la base de conocimiento, que es estática, la base de hechos es 
# dinámica y cambia con cada problema o consulta.
# ¿Para qué sirve?: Proporciona los datos específicos sobre los cuales 
# el sistema experto aplicará las reglas de la base de conocimiento.
# ¿Cómo funciona?: Cuando un usuario interactúa con el sistema, los datos 
# proporcionados (hechos específicos) se almacenan aquí, para que luego el 
# motor de inferencia los utilice junto con la base de conocimiento para 
# llegar a una conclusión.

# Simulación de una Base de Hechos
def agregar_hechos():
    hechos = []
    
    while True:
        hecho = input("Introduce un hecho actual (ej. fiebre, tos, etc.): ")
        hechos.append(hecho)
        
        continuar = input("¿Deseas agregar otro hecho? (s/n): ")
        if continuar.lower() != 's':
            break
    
    return hechos

# Comparar los hechos con la base de conocimiento para hacer una inferencia
def inferencia(base_de_conocimiento, hechos):
    for hecho in hechos:
        for regla in base_de_conocimiento:
            if hecho == regla['condicion']:
                print(f"Se ha inferido: Si '{hecho}', entonces '{regla['conclusion']}'.")

# Agregar hechos al sistema
hechos = agregar_hechos()

# Realizar la inferencia basada en los hechos y la base de conocimiento
inferencia(base_de_conocimiento, hechos)
