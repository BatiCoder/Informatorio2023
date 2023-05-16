
# 18-Crea una función llamada calcular_mayor_diferencia que tome una lista de
# números como parámetro y devuelva la mayor diferencia entre el numero mas
# alto y el numero mas bajo en la lista.

def calcular_mayor_diferencia(lista_numeros):
    # Calcula el número mayor y menor en la lista de números
    mayor = max(lista_numeros)
    menor = min(lista_numeros)

    # Calcula la diferencia entre el mayor y el menor
    diferencia = mayor - menor

    # Retorna la diferencia calculada
    return diferencia

# Ejemplo.
numeros = [10, 5, 8, 12, 3, 20]
mayor_diferencia = calcular_mayor_diferencia(numeros)
print(mayor_diferencia)  # Imprime 17, que es la mayor diferencia entre los números de la lista

# En este ejemplo, se pasa la lista de números [10, 5, 8, 12, 3, 20] como argumento a la función 
# calcular_mayor_diferencia. La función determina el número mayor (20) y el número menor (3) en 
# la lista y calcula la diferencia entre ellos,que es 17. Finalmente, se imprime la mayor diferencia 
# obtenida.