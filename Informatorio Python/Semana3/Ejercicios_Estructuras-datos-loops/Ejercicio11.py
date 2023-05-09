# 11-Escribe un programa que pida al usuario un número y calcule su factorial.
# Un factorial es el producto que resulta de multiplicar un número entero positivo
# dado por todos los enteros inferiores a él hasta el uno. Por ejemplo, el factorial
# de 4 es 4! = 4 × 3 × 2 × 1 = 24.

num = int(input("Ingrese un numero: "))

factorial = 0

for n in range (1, num):
    factorial += num*n

print(f"\nEl factorial de {num} es: {factorial}")

