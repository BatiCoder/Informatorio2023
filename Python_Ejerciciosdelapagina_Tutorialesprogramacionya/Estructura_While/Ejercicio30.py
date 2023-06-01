"""
Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente 
la suma de los valores ingresados y su promedio.

"""

suma = 0  # Inicializamos la variable suma en 0
x = 1  # Inicializamos la variable x en 1

while x <= 10:  # Mientras x sea menor o igual a 10, repetiremos el bucle
    n = float(input(f"Ingrese el {x}º número: "))  # Solicitamos al usuario que ingrese un número y lo almacenamos en la variable n
    suma += n  # Sumamos el valor de n a la variable suma
    x += 1  # Incrementamos el valor de x en 1 en cada iteración del bucle

promedio = suma / 10  # Calculamos el promedio dividiendo la suma entre 10

print(f"\nLa suma de todos los números ingresados es: {suma} y el promedio de esa suma es: {promedio}")
# Imprimimos la suma y el promedio utilizando f-strings para formatear el texto y mostrar los valores calculados.
