
# 11-Escribir un programa que pida al usuario dos números y muestre por pantalla
# la suma de ellos solo si ambos son pares.

num1=float(input("Ingrese el 1er numero: "))
num2=float(input("Ingrese el 2do numero: "))

suma=num1+num2

if num1%2==0 and num2%2==0:
    print(f"\nLa suma es {suma}") 