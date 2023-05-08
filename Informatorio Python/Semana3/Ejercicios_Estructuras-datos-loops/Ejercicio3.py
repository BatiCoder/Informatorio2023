# 3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
# multiplicar correspondiente a ese número del 1 al 10.

# Se ingresa un numero entero por pantalla.
num=int(input("Ingrese un numero entero: "))

# Estructura for que recorre de 1 hasta 10, se multiplica num con el incremento de i y se 
# guarda en la variable local producto, y en cada iteracion al final se imprime por pantalla.
for i in range (1,11):
    producto = num*i
    print(f"\n{num} x {i} = {producto}")
    