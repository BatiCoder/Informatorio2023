
# 9-Crea una función llamada promedio que tome una lista de números como
# parámetro y devuelva el promedio de esos números.

def promedio(lista_numeros):
    # Función que calcula el promedio de una lista de números.
    
    suma = 0
    
    for numero in lista_numeros:
        # Itera sobre cada número en la lista.
        
        suma += numero
        # Suma el número actual a la variable 'suma'.
    
    promedio = suma / len(lista_numeros)
    # Calcula el promedio dividiendo la suma total entre la cantidad de números en la lista.
    
    return promedio
    # Devuelve el valor del promedio calculado.

# Tambien se puede hacer asi:

# def promedio(lista_numeros):
#     # Función que calcula el promedio de una lista de números.
    
#     return sum(lista_numeros) / len(lista_numeros)
#     # Calcula la suma de los números en la lista y la divide entre la cantidad de elementos.
