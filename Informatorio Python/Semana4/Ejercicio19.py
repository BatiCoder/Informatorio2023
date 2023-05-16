
# 19-Crea una función llamada es_bisiesto que tome un año como parámetro y
# devuelva Bisiesto si el año es bisiesto, o No es Bisiesto en caso contrario. Un año
# es bisiesto si es divisible por 4, pero no por 100, a menos que también sea
# divisible por 400.

def es_bisiesto(anio):
    # Verifica si el año es divisible por 4 y no divisible por 100,
    # o si es divisible por 400 y también divisible por 100.
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0 and anio % 100 == 0):
        return "Es año bisiesto."
    else:
        return "No es un año bisiesto."

# Ejemplo.
anio = int(input("Ingrese un año: "))  # Solicita al usuario ingresar un año.
sera_bisiesto = es_bisiesto(anio)  # Llama a la función es_bisiesto para determinar si el año es bisiesto.

print(sera_bisiesto)  # Imprime el resultado obtenido, indicando si el año es bisiesto o no.

# En este código, la función es_bisiesto recibe un año como parámetro y verifica si cumple con 
# las condiciones para ser considerado un año bisiesto. Si el año cumple las condiciones, se 
# retorna el mensaje "Es año bisiesto". De lo contrario, se retorna el mensaje "No es un año bisiesto".
# Luego, se solicita al usuario ingresar un año mediante input y se asigna el valor a la variable anio. 
# Posteriormente, se llama a la función es_bisiesto pasando el año como argumento, y el resultado se 
# almacena en la variable sera_bisiesto. Finalmente, se imprime el resultado obtenido, indicando si 
# el año es bisiesto o no.

