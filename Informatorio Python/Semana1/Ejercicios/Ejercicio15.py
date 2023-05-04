# 15-Escribe un programa que solicite al usuario una temperatura en grados
# Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
# La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.

temperatura_celsius=float(input("Ingrese la temperatura en grados Celsius: "))
temp_Farhenheit=(temperatura_celsius*1.8)+32

print(f"\nEn Farhenheit son: {temp_Farhenheit}")