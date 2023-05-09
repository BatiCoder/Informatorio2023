# 12-Escribe un programa que pida al usuario una lista de números separados por
# comas y calcule su promedio.

numeros = input("Ingrese una lista de números separados por comas: ")

lista_numeros = [int(num) for num in numeros.split(",")]

promedio = sum(lista_numeros) / len(lista_numeros)

print("El promedio de la lista de números ingresada es:", promedio)