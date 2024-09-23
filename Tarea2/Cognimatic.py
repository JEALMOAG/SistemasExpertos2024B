# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 21:06:19 2024

@author: jama2
"""
# El concepto "Cognimatic" es menos común, pero podría hacer referencia a 
# herramientas automáticas o algoritmos que permiten la adquisición de 
# conocimiento de manera automática o semi-automática a partir de datos. 
# Este proceso utiliza algoritmos de machine learning o minería de datos 
# para descubrir patrones, reglas o relaciones ocultas que se pueden incorporar en la base de conocimiento.
# ¿Qué?: Emplear sistemas automáticos para adquirir y estructurar conocimiento de grandes conjuntos de datos.
# ¿Para qué?: Generar conocimiento actualizado y dinámico que pueda adaptarse a 
# nuevas situaciones sin la intervención constante de expertos humanos.
# ¿Cómo?: Utilizando técnicas de inteligencia artificial como algoritmos de 
# clasificación, clustering, aprendizaje supervisado y no supervisado.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

# Cargar el dataset
iris = load_iris()
X = iris.data  # Características
y = iris.target  # Clases

# Dividir el dataset en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Crear el modelo usando un árbol de decisión
clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

# Hacer predicciones
y_pred = clf.predict(X_test)

# Mostrar la precisión del modelo
print(f"Precisión del modelo: {metrics.accuracy_score(y_test, y_pred)}")

# Ejemplo de cómo usar el modelo para predecir una nueva instancia
nueva_flor = [[5.1, 3.5, 1.4, 0.2]]  # Características de la flor
prediccion = clf.predict(nueva_flor)
print(f"Predicción para la nueva flor: {iris.target_names[prediccion][0]}")