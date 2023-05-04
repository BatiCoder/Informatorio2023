# 12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
# dd/mm/aaaa y luego imprima su edad en años.
# Utiliza la función .split()

fecha_nacimiento = input("Por favor, ingresa tu fecha de nacimiento en formato dd/mm/aaaa: ")
dia, mes, anio = fecha_nacimiento.split("/")
edad = 2023 - int(anio)

print("Tu edad es:", edad, "años")