# 10-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# la misma cadena pero con todas las vocales en mayúscula.

texto=input("Ingrese un fragmento de texto: ")

vocales = "aeiouAEIOU"

cadena_vocales_mayus=""

for letra in texto:
    if letra in vocales:
        cadena_vocales_mayus+=letra.upper()
    else:
        cadena_vocales_mayus+=letra

print(f"\n{cadena_vocales_mayus}")
