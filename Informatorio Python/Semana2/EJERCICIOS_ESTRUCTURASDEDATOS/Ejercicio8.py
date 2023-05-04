# 8-Crear una lista con los números del 1 al 10 y mostrarlos en orden inverso.

# Método 1: utilizando reverse() -----------------------------------------------------------

# Definir una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Invertir el orden de los elementos en la lista
numeros.reverse()

# Imprimir la lista resultante
print(numeros)

# Para imprimir por pantalla una lista de números en orden inverso en Python, puedes
# utilizar el método reverse() de las listas, que invierte el orden de los elementos
# en la lista. También puedes utilizar el slicing para obtener una nueva lista en
# orden inverso, sin modificar la lista original. Aquí te muestro el slicing:

# Método 2: utilizando slicing --------------------------------------------------------------

""""

# Definir una lista de números
numeros = [5, 2, 8, 1, 3]

# Crear una nueva lista en orden inverso utilizando slicing
numeros_inversos = numeros[::-1]

# Imprimir la lista resultante
print(numeros_inversos) 

"""

# Este código también imprimirá la lista [3, 1, 8, 2, 5].Ambos métodos logran el mismo
# resultado, pero el segundo método no modifica la lista original. Es importante tener
# esto en cuenta sinecesitas utilizar la lista original en su orden original posteriormente
# en tu programa.
