import numpy as np

#Creación de un ndarray con valores del 0 al 9 (sin incluir el 10)
numeros_1 = np.arange(0, 10)
print(numeros_1)

#Creación de un ndarray con valores del 1 al 5 de 2 en 2
numeros_2 = np.arange(1, 6, 2)
print(numeros_2)

#Creación de un ndarray con valores del 0 al 4 (sin incluir el 4) de 0.5 en 0.5
numeros_3 = np.arange(0, 4, 0.5)
print(numeros_3)

#Creación de un ndarray con 10 valores espaciados uniformemente entre 0 y 1 
puntos_1 = np.linspace(0, 1, 10)
print(puntos_1)

#Creación de un ndarray con 5 valores espaciados uniformemente entre 2 y 10 
puntos_2 = np.linspace(2, 10, 5)
print(puntos_2)

#Creación de un ndarray de 3x3 con números aleatorios entre 0 y 1
matriz_aleatoria_1 = np.random.rand(3, 3)
print(matriz_aleatoria_1)

#Creación de un ndarray de 5 elemento