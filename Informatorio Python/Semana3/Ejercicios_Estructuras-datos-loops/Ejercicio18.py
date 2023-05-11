# 18-Escribe un programa que pida al usuario un número y luego imprima un
# triángulo de números como el siguiente:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

n = int(input("Introduce un número: "))
numero = 1  # inicializar el número en 1
for i in range(1, n+1):  # iterar sobre cada fila del triángulo
    for j in range(i):  # iterar sobre cada número de la fila
        print(numero, end=' ')  # imprimir el número actual
        numero += 1  # aumentar el número en 1
    print()  # imprimir un salto de línea al final de cada fila

# Primero, el programa pide al usuario un número que se almacena en la variable n. 
# Luego, se inicializa el número actual en 1 en la variable numero.

# A continuación, se utiliza un bucle for para iterar sobre cada fila del triángulo, desde 
# la primera hasta la fila n. Dentro de este bucle, se utiliza otro bucle for para iterar 
# sobre cada número de la fila actual, desde el primer número hasta el número correspondiente 
# a la fila actual. En cada iteración de este bucle interno, se imprime el número actual utilizando 
# la función print() con el argumento end=' ', que indica que se debe imprimir un espacio en lugar 
# de un salto de línea al final de cada número. Luego, se aumenta el número actual en 1 para imprimir 
# el siguiente número en la siguiente iteración del bucle interno.

# Después de imprimir todos los números de la fila actual, se imprime un salto de línea utilizando 
# la función print() sin argumentos. Esto garantiza que cada fila se imprima en una nueva línea.

# Al finalizar la ejecución del bucle externo, se habrán impreso todos los números del triángulo de 
# acuerdo al patrón indicado.