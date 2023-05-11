# 19-Escribe un programa que pida al usuario un número y luego imprima si ese
# número es un número perfecto o no. Un número perfecto es aquel que es igual a
# la suma de sus divisores propios (excluyendo el propio número).
# Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se
# puede dividir por 1, 2 y 3, y cuando sumas esos números, el resultado es 6

numero = int(input("Introduce un número: "))

suma_divisores = 0  # inicializar la suma de divisores en 0

for i in range(1, numero):  # iterar sobre cada posible divisor propio
    if numero % i == 0:  # si el número es divisible por el divisor actual
        suma_divisores += i  # añadir el divisor a la suma de divisores
if suma_divisores == numero:  # si la suma de divisores es igual al número
    print(numero, "es un número perfecto")
else:
    print(numero, "no es un número perfecto")


# Primero, el programa pide al usuario un número que se almacena en la variable numero. Luego, se 
# inicializa la suma de divisores en 0 en la variable suma_divisores.

# A continuación, se utiliza un bucle for para iterar sobre cada posible divisor propio del número 
# ingresado por el usuario, desde 1 hasta numero-1. Dentro de este bucle, se utiliza una sentencia 
# condicional if para verificar si el número es divisible por el divisor actual (es decir, si el 
# resto de la división es 0). Si es así, se añade el divisor actual a la suma de divisores utilizando 
# el operador +=.

# Al finalizar la ejecución del bucle, se verifica si la suma de divisores es igual al número ingresado 
# por el usuario utilizando otra sentencia condicional if. Si es así, se imprime un mensaje indicando 
# que el número es perfecto. Si no, se imprime un mensaje indicando que el número no es perfecto.

# Con este código, puedes determinar si un número ingresado por el usuario es perfecto o no.