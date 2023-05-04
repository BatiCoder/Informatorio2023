
""" 9-Escribir un programa que pida al usuario tres números y muestre por pantalla
el mayor de ellos. """

num1 = float(input("Ingrese 1er numero: "))
num2 = float(input("Ingrese 2do numero: "))
num3 = float(input("Ingrese 3er numero: "))

if num1 > num2 and num1 > num3:
    print(f"El mayor es {num1}")
elif num2 > num3:
    print(f"El mayor es {num2}")
else:
    print(f"El mayor es {num3}")


""" Primero, se pide al usuario que ingrese tres números utilizando la función input(). Los números se convierten 
en valores de punto flotante utilizando la función float(). Luego, se utiliza una serie de condicionales if y elif 
para determinar cuál de los números es el mayor.Si el primer número es mayor o igual que los otros dos, se imprime 
un mensaje indicando que el primer número es el mayor. Si el segundo número es mayor o igual que los otros dos, se 
imprime un mensaje indicando que el segundo número es el mayor. Si ninguno de los dos casos anteriores se cumple, se 
imprime un mensaje indicando que el tercer número es el mayor.
Este programa funciona para cualquier conjunto de tres números ingresados por el usuario. """

# num1 = float(input("Ingresa el primer número: "))
# num2 = float(input("Ingresa el segundo número: "))
# num3 = float(input("Ingresa el tercer número: "))

# if num1 >= num2 and num1 >= num3:
#     print("El mayor número es:", num1)
# elif num2 >= num1 and num2 >= num3:
#     print("El mayor número es:", num2)
# else:
#     print("El mayor número es:", num3)

