# -*- coding: utf-8 -*-
"""
Created on tues Sep 10 09:38:50 2024

@author: jama2
"""
'''
Descipcion del codigo:
Este código implementa una solución para el problema de preparación de tacos 
utilizando una búsqueda en anchura. Define una clase Nodo que representa el 
estado actual del proceso de preparación, incluyendo las instrucciones 
realizadas y el costo acumulado.

La función preparar_tacos explora diferentes combinaciones de instrucciones 
básicas (como picar cebolla y cocinar carne) utilizando una cola (deque) para 
gestionar los nodos a procesar. A medida que se generan nuevos nodos, se 
verifica si se ha alcanzado la meta de tener un "taco_listo". 
Si se encuentra la secuencia de instrucciones adecuada, se devuelve; 
de lo contrario, se retorna None si no hay solución.

También se incluye una función calcular_costo, que establece un costo fijo 
para cada instrucción, y se definen los ingredientes, utensilios y las 
instrucciones básicas necesarias para preparar los tacos. Finalmente, el 
código ejecuta la función y muestra la solución encontrada.
'''

from collections import deque  # Importa la clase deque del módulo collections, que permite crear una cola de forma eficiente para agregar y quitar elementos desde ambos extremos.

# Definición de la clase Nodo, que representa un estado en la preparación de tacos.
class Nodo:
    def __init__(self, instrucciones, costo):
        self.instrucciones = instrucciones  # Lista de instrucciones realizadas hasta el momento
        self.costo = costo  # Costo acumulado de las instrucciones

# Función principal para preparar tacos
def preparar_tacos(ingredientes, utensilios):
    # Crear una cola (deque) para almacenar los nodos a explorar, comenzando con el nodo inicial
    cola = deque([Nodo([], 0)])  # Nodo inicial con instrucciones vacías y costo 0
    visitados = set()  # Conjunto para llevar un registro de los nodos ya visitados

    # Mientras haya nodos en la cola para procesar
    while cola:
        nodo = cola.popleft()  # Extraer el nodo del frente de la cola
        # Verificar si hemos llegado al objetivo: preparar el taco
        if nodo.instrucciones == ["taco_listo"]:
            return nodo.instrucciones  # Retornar las instrucciones que llevan a la solución

        # Iterar sobre las instrucciones básicas posibles
        for instruccion in instrucciones_basicas:
            # Crear una nueva lista de instrucciones incluyendo la instrucción actual
            nuevas_instrucciones = nodo.instrucciones + [instruccion]
            # Calcular el nuevo costo acumulado al agregar esta instrucción
            nuevo_costo = nodo.costo + calcular_costo(instruccion)
            # Crear un nuevo nodo con las instrucciones actualizadas y el nuevo costo
            nuevo_nodo = Nodo(nuevas_instrucciones, nuevo_costo)

            # Si el nuevo nodo no ha sido visitado aún
            if nuevo_nodo not in visitados:
                visitados.add(nuevo_nodo)  # Marcar el nodo como visitado
                cola.append(nuevo_nodo)  # Agregar el nuevo nodo a la cola para exploración posterior

    return None  # Retornar None si no se encuentra una solución

# Función para calcular el costo de aplicar una instrucción básica
def calcular_costo(instruccion):
    # En este caso, cada instrucción tiene un costo fijo de 1
    return 1

# Ingredientes y utensilios básicos para la preparación de tacos
ingredientes = ["carne", "cebolla", "tomate", "lechuga", "queso"]
utensilios = ["cuchillo", "sartén", "taza"]

# Lista de instrucciones básicas necesarias para preparar tacos
instrucciones_basicas = [
    "picar_cebolla",
    "cocinar_carne",
    "preparar_salsa",
    "calentar_tortilla",
    "ensamblar_taco",
    "taco_listo"
]

# Ejemplo de uso de la función para preparar tacos
solucion = preparar_tacos(ingredientes, utensilios)
print(solucion)  # Imprimir la solución óptima que lleva a la preparación del taco
