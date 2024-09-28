import numpy as np

arr = np.array([1,2,3])
print(np.sum(arr))

array = np.array([[1,2,3],[4,5,6]])
print("Array original: ")
print(array)
reshape_array = array.reshape(3, 2)#Cambia la forma sin cambiar los datos
print("Array reshape: ")
print(reshape_array)



numeros_aleatorios_uniformes = np.random.rand(3)
print("Numeros aleatorios uniformes:")
print(numeros_aleatorios_uniformes)
numeros_aleatorios_enteros = np.random.randint(1, 10, size=5)
print("Numeros aleatorios enteros:")
print(numeros_aleatorios_enteros)
numeros_aleatorios_normales = np.random.randn(2, 2)
print("Numeros aleatorios normales:")
print(numeros_aleatorios_normales)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
#Sumar elemento por elemento
result = arr1 + arr2
print(result)

#Operaciones con Constantes

arr = np.array([1, 2, 3])
#Multiplicación por una constante de 2
result = 2 * arr
print(result)

#Suma de matrices

arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
result = arr3 + arr4
print(result)

arr5 = np.array([[1, 2, 3, 4, 5, 6]])
print(arr5)
reshape_arr = arr5.reshape(2, 3)
print(reshape_arr)
total_sum = arr5.sum()
print(total_sum)

#Mean calcula la media de los elementos a lo largo de un eje especifico o de todo el ndarray
arr6 = np.array([[1, 2, 3], [4, 5, 6]])
average = arr6.mean()
print(average)
min_val = arr6.min()
print(min_val)
max_val = arr6.max()
print(max_val)

