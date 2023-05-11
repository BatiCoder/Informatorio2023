# 17-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# la misma cadena pero con las palabras en orden inverso.

cadena = input("Ingrese un fragmento de texto: ")

palabras = cadena.split()  # dividir la cadena en palabras
palabras_invertidas = palabras[::-1]  # invertir el orden de la lista de palabras utilizando slicing
cadena_inversa = ' '.join(palabras_invertidas)  # unir las palabras invertidas en una cadena de texto

print(cadena_inversa)

