"""
Created on Wed Oct 20 10:10:52 2024

@author: Jesus Montes
"""

import tkinter as tk  # Importa la biblioteca tkinter para crear interfaces gráficas
from tkinter import messagebox, simpledialog  # Importa elementos específicos de tkinter
import random  # Importa la biblioteca random para generar selecciones aleatorias
import json  # Importa la biblioteca json para trabajar con archivos JSON
import os  # Importa la biblioteca os para interactuar con el sistema operativo

# Cargar la base de datos de países desde un archivo JSON
def cargar_paises():
    # Verifica si el archivo 'Paises.json' existe
    if os.path.exists('Paises.json'):
        # Abre el archivo en modo lectura y carga su contenido como un objeto JSON
        with open('Paises.json', 'r', encoding='utf-8') as f:
            return json.load(f)  # Retorna los datos cargados
    else:
        return {}  # Retorna un diccionario vacío si no existe el archivo

# Guardar la base de datos de países en un archivo JSON
def guardar_paises():
    # Abre el archivo en modo escritura, lo crea si no existe
    with open('Paises.json', 'w', encoding='utf-8') as f:
        json.dump(paises, f, ensure_ascii=False, indent=4)  # Guarda los datos en formato JSON

# Cargar países desde el archivo JSON
paises = cargar_paises()  # Llama a la función para cargar los países al iniciar el programa

# Lista de preguntas posibles
preguntas_generales = {
    "continente": "¿Está el país en el continente {}?",  # Pregunta sobre el continente
    "idioma": "¿El idioma principal del país es {}?",  # Pregunta sobre el idioma
    "moneda": "¿La moneda del país es {}?",  # Pregunta sobre la moneda
    "capital": "¿La capital del país es {}?",  # Pregunta sobre la capital
    "comida_tipica": "¿La comida típica del país es {}?",  # Pregunta sobre la comida típica
    "frontera": "¿El país tiene frontera con {}?",  # Pregunta sobre las fronteras
    "clima": "¿El clima del país es {}?",  # Pregunta sobre el clima
    "deporte_popular": "¿El deporte más popular en el país es {}?",  # Pregunta sobre el deporte
    "exportacion_principal": "¿La principal exportación del país es {}?"  # Pregunta sobre exportaciones
}

# Variables de control
pais_posibles = list(paises.keys())  # Lista de países posibles a adivinar
pregunta_actual = None  # Inicializa la pregunta actual
caracteristica_actual = None  # Inicializa la característica actual
intentos = 0  # Contador de intentos
max_intentos = 20  # Máximo de intentos permitidos
preguntas_hechas = set()  # Conjunto para registrar preguntas ya realizadas

# Función para generar la siguiente pregunta
def generar_pregunta():
    global pregunta_actual, caracteristica_actual  # Define variables globales
    if pais_posibles:  # Verifica si hay países posibles
        pais = random.choice(pais_posibles)  # Selecciona un país aleatorio
        caracteristica_actual = random.choice(list(paises[pais].keys()))  # Selecciona una característica aleatoria

        # Asegurarse de que la pregunta no se haya hecho antes
        while f"{pais}:{caracteristica_actual}" in preguntas_hechas:
            pais = random.choice(pais_posibles)  # Selecciona otro país si ya se hizo la pregunta
            caracteristica_actual = random.choice(list(paises[pais].keys()))  # Selecciona otra característica

        valor = paises[pais][caracteristica_actual]  # Obtiene el valor de la característica seleccionada
        pregunta_actual = preguntas_generales[caracteristica_actual].format(valor)  # Formatea la pregunta
        preguntas_hechas.add(f"{pais}:{caracteristica_actual}")  # Registra la pregunta
        label_pregunta.config(text=pregunta_actual)  # Actualiza el texto de la pregunta en la interfaz
    else:
        messagebox.showinfo("Fin del juego", "¡No quedan más países posibles!")  # Mensaje cuando no hay países
        reiniciar_juego()  # Reinicia el juego

# Función para procesar la respuesta del usuario
def procesar_respuesta():
    global intentos, pais_posibles, caracteristica_actual  # Define variables globales
    respuesta = entry_respuesta.get().lower().strip()  # Obtiene la respuesta del usuario y la normaliza
    entry_respuesta.delete(0, tk.END)  # Limpia la entrada del usuario

    valor = pregunta_actual.split("es ")[-1].strip("?")  # Extrae el valor de la pregunta actual

    if respuesta in ["sí", "si"]:  # Si la respuesta es "sí"
        # Filtra los países posibles que coinciden con la característica
        pais_posibles = [pais for pais in pais_posibles if paises[pais][caracteristica_actual] == valor]
    elif respuesta == "no":  # Si la respuesta es "no"
        # Filtra los países posibles que no coinciden con la característica
        pais_posibles = [pais for pais in pais_posibles if paises[pais][caracteristica_actual] != valor]
    else:
        messagebox.showwarning("Respuesta inválida", "Por favor, responde con 'sí' o 'no'.")  # Mensaje de advertencia
        return  # Sale de la función

    intentos += 1  # Incrementa el contador de intentos
    if len(pais_posibles) == 1:  # Si queda un solo país posible
        # Pregunta al usuario si es el país
        if messagebox.askyesno("¿Adiviné?", f"¿Es el país {pais_posibles[0]}?"):
            messagebox.showinfo("¡Adiviné!", f"El país que pensaste es {pais_posibles[0]} después de {intentos} intentos.")
            reiniciar_juego()  # Reinicia el juego
        else:
            agregar_nuevo_pais()  # Llama a la función para agregar un nuevo país
    elif intentos >= max_intentos:  # Si se alcanza el máximo de intentos
        agregar_nuevo_pais()  # Llama a la función para agregar un nuevo país
    else:
        generar_pregunta()  # Genera la siguiente pregunta

# Función para agregar un nuevo país a la base de datos
def agregar_nuevo_pais():
    pais_correcto = simpledialog.askstring("Error", "No pude adivinar. ¿Cuál era el país?")  # Pregunta por el país correcto
    if pais_correcto and pais_correcto not in paises:  # Si el país no está en la base de datos
        nueva_info = {}  # Inicializa un diccionario para la nueva información del país
        for key in preguntas_generales.keys():  # Itera sobre las preguntas generales
            # Pregunta al usuario por la información del nuevo país
            nueva_info[key] = simpledialog.askstring("Nuevo País", f"¿Cuál es el {key} de {pais_correcto}?")
        paises[pais_correcto] = nueva_info  # Agrega el nuevo país a la base de datos
        guardar_paises()  # Guarda la base de datos actualizada
        messagebox.showinfo("Nuevo país", f"{pais_correcto} ha sido agregado a la base de datos.")  # Mensaje de confirmación
    elif pais_correcto:  # Si el país ya está en la base de datos
        messagebox.showwarning("Error", "El país ingresado ya está en la base de datos.")  # Mensaje de advertencia
    reiniciar_juego()  # Reinicia el juego

# Función para reiniciar el juego
def reiniciar_juego():
    global pais_posibles, intentos, preguntas_hechas  # Define variables globales
    pais_posibles = list(paises.keys())  # Reinicia la lista de países posibles
    intentos = 0  # Reinicia el contador de intentos
    preguntas_hechas.clear()  # Limpiar las preguntas realizadas
    generar_pregunta()  # Genera la primera pregunta

# Configuración de la ventana principal
root = tk.Tk()  # Crea la ventana principal
root.title("Adivina el País")  # Establece el título de la ventana
root.geometry("400x300")  # Establece el tamaño de la ventana

label_instruccion = tk.Label(root, text="Piensa en un país, y yo intentaré adivinarlo.")  # Instrucciones al usuario
label_instruccion.pack()  # Añade la etiqueta a la ventana

label_pregunta = tk.Label(root, text="", font=("Arial", 12))  # Crea una etiqueta para mostrar la pregunta
label_pregunta.pack(pady=20)  # Añade la etiqueta a la ventana

entry_respuesta = tk.Entry(root, width=20)  # Crea un campo de entrada para la respuesta del usuario
entry_respuesta.pack()  # Añade el campo de entrada a la ventana

button_responder = tk.Button(root, text="Responder", command=procesar_respuesta)  # Crea un botón para enviar la respuesta
button_responder.pack(pady=10)  # Añade el botón a la ventana

# Genera la primera pregunta
generar_pregunta()  # Llama a la función para iniciar el juego

# Ejecuta la interfaz gráfica
root.mainloop()  # Inicia el bucle principal de la interfaz gráfica
