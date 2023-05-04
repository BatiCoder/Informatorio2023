
# 10-Crea un programa que pida al usuario una cantidad en dólares y la convierta a
# euros.
# Supón que el tipo de cambio es de 0.84 euros por dólar.

dolares=float(input("Ingrese la cantidad de dolares a convertir a euros: "))
tipo_de_cambio= 0.84

euros=dolares*tipo_de_cambio

print(f"\nRecibira {euros} euros\n")