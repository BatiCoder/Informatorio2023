
# 6-Escribir un programa que pida al usuario un número entero y muestre por
# pantalla si es múltiplo de 2 y de 3 a la vez.

num=int(input("Ingrese un numero entero: "))

if num%2 == 0 and num%3 == 0:
    print("\nEs multiplo de 2 y de 3 a la vez.")
else:
    print("No es multiplo de 2 y de 3 a la vez.")

"""Múltiplos de 2: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 
30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 
66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100"""

"""Múltiplos de 3: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 
48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 
105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144, 147, 150"""

