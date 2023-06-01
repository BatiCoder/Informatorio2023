"""
Codificar un programa que solicite la carga de un valor positivo y nos muestre desde 1 hasta el valor 
ingresado de uno en uno, por ejemplo: 

Si ingresamos 30 se debe mostrar en pantalla los números del 1 al 30.

"""

n = int(input("Ingrese un valor entero positivo: "))  # Solicitamos al usuario que ingrese un valor entero positivo y lo almacenamos en la variable n
x = 1  # Inicializamos la variable x con el valor 1

while x <= n:  # Mientras x sea menor o igual a n, repetiremos el bucle
    print(x, end="-")  # Imprimimos el valor de x seguido de un guión, sin salto de línea
    x += 1  # Incrementamos el valor de x en 1 en cada iteración del bucle

# El bucle se repetirá desde x=1 hasta x=n, imprimiendo los valores de x separados por guiones.
