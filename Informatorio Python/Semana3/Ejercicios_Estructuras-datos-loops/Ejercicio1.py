# 1-Escribe un programa que pida al usuario una palabra y luego imprima cada
# letra de la palabra en una línea separada.

# Pedir al usuario que ingrese una palabra por teclado
palabra = input("Ingrese una palabra: ")

# Convertir en una lista las letras de la palabra?.
palabra_separada = list(palabra)

for letra in palabra_separada:
    print(letra)
