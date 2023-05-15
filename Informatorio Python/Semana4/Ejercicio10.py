
# 10-Crea una función llamada calcular_factorial que tome un número entero como
# parámetro y devuelva el factorial de ese número. El factorial de un número
# entero positivo n se define como el producto de todos los números enteros
# positivos desde 1 hasta n.

def calcular_factorial(numero):
    # Función que calcula el factorial de un número entero.
    
    factorial = 1
    # Inicializa el valor del factorial en 1.
    
    for i in range(1, numero + 1):
        # Itera desde 1 hasta el número ingresado, incluyéndolo.
        
        factorial *= i
        # Multiplica el valor actual del factorial por el número actual.
    
    return factorial
    # Devuelve el valor del factorial calculado.

print(calcular_factorial(8))
