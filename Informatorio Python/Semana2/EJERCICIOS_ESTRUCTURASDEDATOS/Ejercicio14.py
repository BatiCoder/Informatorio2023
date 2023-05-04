# 14-Crear una tupla con los números del 1 al 5 y mostrar la suma de todos los
# elementos de la tupla.

# Definir la tupla.
numeros = (1, 2, 3, 4, 5)

# Calcular la suma de todos los elementos de la tupla
suma = sum(numeros)

# Mostrar la suma de todos los elementos de la tupla
print(suma)

# Otra manera de hacerlo seria:

"""

#Crear una tupla con los números del 1 al 5
numeros = tuple(range(1, 6))

#Calcular la suma de todos los elementos de la tupla
suma = sum(numeros)

#Mostrar la suma de todos los elementos de la tupla
print("La suma de los números en la tupla es:", suma)

"""

# En este código, primero creamos una tupla llamada numeros utilizando tuple(range(1, 6)),
# que genera los números del 1 al 5 y los convierte en una tupla. Luego, calculamos la suma
# de todos los elementos de la tupla utilizando la función sum(numeros). Finalmente, utilizamos
# print() para mostrar la suma resultante. La salida del código será: La suma de los números
# en la tupla es: 15.
