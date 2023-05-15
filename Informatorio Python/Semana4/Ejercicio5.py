
# 5-Crea una función llamada es_divisible que tome dos números enteros como
# parámetros y devuelva Es divisible si el primer número es divisible por el
# segundo número, o No es divisible en caso contrario.

def es_divisible(num1, num2):
# Definición de una función llamada "es_divisible" que recibe dos parámetros: num1 y num2
    
    if num1 % num2 == 0:  # Verifica si el residuo de la división entre num1 y num2 es igual a cero
        return "Es divisible"  # Si el residuo es cero, devuelve el mensaje "Es divisible"
    else:
        return "No es divisible"  # Si el residuo no es cero, devuelve el mensaje "No es divisible"

