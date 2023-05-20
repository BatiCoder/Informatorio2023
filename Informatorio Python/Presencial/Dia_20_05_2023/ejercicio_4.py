
""" Crear una funcion que reciba un numero 'x' e imprima los primeros 'x' números de la sucesión de Fibonacci."""

def fibonacci(x):
    
    fibonacci = [0, 1]  # Se empieza con los primeros dos números de la secuencia
    
    while len(fibonacci) < x:
        siguiente = fibonacci[-1] + fibonacci[-2]  # Se calcula el siguiente número de la secuencia
        fibonacci.append(siguiente)  # Se agrega el siguiente número a la lista
    
    return fibonacci


# Ejemplo de uso
numero = int(input("Ingrese la cantidad de números de Fibonacci que desea imprimir: "))
numeros_fib = fibonacci(numero)

print("La secuencia de Fibonacci de longitud", numero, "es:\n")
for num in numeros_fib:
    print(num)