# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:23:29 2024

@author: jama2
"""
'''
Este código implementa un chatbot que utiliza un archivo de base de datos local
para almacenar preguntas y respuestas. El chatbot busca coincidencias entre la
entrada del usuario y las preguntas en la base de datos, y agrega nueva información
si no se encuentra una coincidencia.'''
# Importar bibliotecas
import random  # Importar aleatorio
import re  # Importar expresiones regulares

# Archivo de base de datos local
database_file = "knowledge.txt"  # Archivo de base de datos local

# Función para leer la base de datos
def read_database():
    try:
        with open(database_file, "r") as f:  # Abrir archivo en modo de lectura
            data = f.readlines()  # Leer todas las líneas del archivo
            return [line.strip().split("|") for line in data]  # Procesar cada línea y dividir en pregunta y respuesta
    except FileNotFoundError:  # Capturar excepción si archivo no existe
        return []  # Devolver lista vacía si archivo no existe

# Función para escribir en la base de datos
def write_database(data):
    with open(database_file, "w") as f:  # Abrir archivo en modo de escritura
        for item in data:  # Iterar sobre lista de preguntas y respuestas
            f.write("|".join(item) + "\n")  # Escribir cada pregunta y respuesta en archivo

# Función para procesar la entrada del usuario
def process_input(user_input):
    user_input = user_input.lower()  # Convertir entrada del usuario a minúsculas
    user_input = re.sub(r'[^\w\s]', '', user_input)  # Eliminar caracteres especiales de la entrada del usuario
    for key, value in read_database():  # Iterar sobre lista de preguntas y respuestas de la base de datos local
        if key in user_input:  # Verificar si pregunta coincide con entrada del usuario
            return value  # Devolver respuesta correspondiente a la pregunta
    return ask_for_new_knowledge(user_input)  # Pedir conocimiento nuevo al usuario si no se encuentra coincidencia

# Función para pedir conocimiento nuevo
def ask_for_new_knowledge(user_input):
    print("No tengo una respuesta para esa pregunta. ¿Puedes proporcionarme más información sobre eso?")  # Imprimir mensaje para pedir más información
    new_knowledge = input("Tú: ")  # Pedir al usuario que proporcione más información
    add_new_knowledge(user_input, new_knowledge)  # Agregar nueva información a la base de datos local
    return "Gracias por la información. Ahora puedo responder a esa pregunta."  # Devolver mensaje de agradecimiento y confirmación

# Función para agregar conocimiento nuevo
def add_new_knowledge(key, value):
    data = read_database()  # Leer base de datos local
    data.append([key, value])  # Agregar nueva pregunta y respuesta a la lista
    write_database(data)  # Escribir lista actualizada en archivo de base de datos local

# Función para ejecutar el chatbot
def run_chatbot():
    print("Hola! Soy un chatbot de higiene en el trabajo. ¿En qué puedo ayudarte?")  # Imprimir mensaje de bienvenida
    while True:  # Bucle infinito para interactuar con el usuario
        user_input = input("Tú: ")  # Pedir entrada del usuario
        response = process_input(user_input)  # Procesar entrada del usuario
        print("Chatbot: " + response)  # Imprimir respuesta del chatbot

# Ejecutar el chatbot
run_chatbot()  # Llamar a la función para ejecutar el chatbot