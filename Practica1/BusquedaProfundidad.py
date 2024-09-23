# -*- coding: utf-8 -*-
"""
Created on Thurs Sep 12 08:49:19 2024

@author: jama2
"""
'''
El código realiza una búsqueda en profundidad (DFS) para encontrar 
todas las ocurrencias de la palabra "mecatrónica" en un texto. 
Utiliza dos funciones: una que busca posiciones de la palabra 
en una línea y otra que recorre recursivamente cada línea del texto. 
Al final, imprime las líneas y posiciones donde se encuentra la palabra.
'''
def buscar_palabra_en_linea(linea, palabra):
    """Busca una palabra en una línea específica y devuelve las posiciones."""
    posiciones = []  # Lista para almacenar las posiciones donde se encuentra la palabra
    indice = linea.find(palabra)  # Busca la primera ocurrencia de la palabra en la línea
    while indice != -1:  # Mientras haya ocurrencias
        posiciones.append(indice)  # Añade la posición encontrada a la lista
        indice = linea.find(palabra, indice + 1)  # Busca la siguiente ocurrencia a partir de la posición siguiente
    return posiciones  # Devuelve la lista de posiciones encontradas


def dfs_buscar_palabra(lineas, palabra, indice=0, ocurrencias=None):
    """Realiza una búsqueda en profundidad para encontrar todas las ocurrencias de una palabra en un texto."""
    if ocurrencias is None:
        ocurrencias = {}  # Inicializa el diccionario para almacenar las ocurrencias

    if indice < len(lineas):  # Verifica si el índice está dentro de los límites
        # Busca la palabra en la línea actual
        posiciones = buscar_palabra_en_linea(lineas[indice], palabra)  
        if posiciones:  # Si se encontraron posiciones
            ocurrencias[indice + 1] = posiciones  # Almacena las posiciones en el diccionario con el número de línea como clave
        
        # Llama recursivamente a la función para la siguiente línea
        dfs_buscar_palabra(lineas, palabra, indice + 1, ocurrencias)  

    return ocurrencias  # Devuelve el diccionario con todas las ocurrencias encontradas


# Texto a analizar
texto = """Ingeniería en Mecatrónica es una carrera en donde se adquieren las habilidades para innovar y proponer soluciones a problemas en sistemas robóticos, de automatización industrial, electromecánicos, visión artificial o instrumentación y control.

El Ingeniero en Mecatrónica es capaz de vincular sus conocimientos con el sector productivo y social; para satisfacer las necesidades que surjan en su campo de acción, contribuyendo en el desarrollo regional, nacional o internacional, actuando de manera ética y responsable."""

# Palabra que deseas buscar
palabra_a_buscar = 'Mecatrónica'  # Define la palabra a buscar en el texto

# Divide el texto en líneas
lineas = texto.split('\n')  

resultados = dfs_buscar_palabra(lineas, palabra_a_buscar)  # Llama a la función para buscar la palabra en el texto

# Imprimir resultados
for linea, posiciones in resultados.items():  # Itera sobre las líneas y posiciones encontradas
    print(f'La palabra "{palabra_a_buscar}" se encontró en la línea {linea} en las posiciones: {posiciones}')  # Imprime los resultados
