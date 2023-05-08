# 2-Escribe un programa que pida al usuario un número y calcule la suma de todos
# los números naturales del 1 hasta ese número.

num = int(input("Ingrese un numero: "))

for x in range(1,num):
    num += x

print(f"\nLa suma de todos los numeros naturales hasta el que eligio es: {num}")

