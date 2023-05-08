# 3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
# multiplicar correspondiente a ese número del 1 al 10.

num=int(input("Ingrese un numero entero: "))

for i in range (1,11):
    producto = num*i
    print(f"\n{num} x {i} = {producto}")
    