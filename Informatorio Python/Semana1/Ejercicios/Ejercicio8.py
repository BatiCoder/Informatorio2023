
# 8-Crea un programa que pida al usuario el radio de un círculo y muestre su
# diámetro, su circunferencia y su área.
# Supón que pi es aproximadamente 3.14159.

radio=float(input("Ingrese el radio del cirulo: "))

pi=3.14159
diametro=2*radio
circunferencia=2*pi*radio
area=pi*radio**2

print("Aqui estan los resultados obtenidos con el radio:\n")
print(f"Diametro:{diametro}   Circunferencia:{circunferencia}   Area:{area}\n")
