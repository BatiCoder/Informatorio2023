# 16-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# la misma cadena pero con cada palabra al revés.

texto = input("Introduce una cadena de texto: ")
palabras = texto.split()  # dividir la cadena en palabras y convertirse en lista.
palabras_invertidas = []  # lista para almacenar las palabras invertidas.

# iterar sobre cada palabra en la lista y agregar su versión invertida a la lista palabras_invertidas
for palabra in palabras:
    invertida = palabra[::-1]  # invertir la palabra utilizando slicing
    palabras_invertidas.append(invertida)

# unir las palabras invertidas en una cadena de texto utilizando el espacio como separador
texto_invertido = ' '.join(palabras_invertidas)

# imprimir la cadena de texto con las palabras invertidas
print(texto_invertido)