
# 9-Escribe un programa que pida al usuario un número y luego imprima la
# secuencia de Fibonacci correspondiente a ese número.

numero = int(input("Ingrese un número: "))

fibonacci = [0, 1]  # Se empieza con los primeros dos números de la secuencia

while len(fibonacci) < numero:
    siguiente = fibonacci[-1] + fibonacci[-2]  # Se calcula el siguiente número de la secuencia
    fibonacci.append(siguiente)  # Se agrega el siguiente número a la lista

print(fibonacci)


