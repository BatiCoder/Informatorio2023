
# 8-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# el número de palabras que contiene.

# Se pide al usuario que ingrese por teclado un fragmento de texto.
cadena_texto=input("Ingrese un fragmento de texto: ")

# Se define al texto en una lista y luego se cuenta la cantidad de elementos de la misma, 
# que seria lo mismo que contar las palabras.
lista_cadena=cadena_texto.split()
cantidad_palabras=len(lista_cadena)

# Se imprime por pantalla la cantidad de palabras que contiene el texto.
print(f"La cantidad de palabras que contiene el texto es: {cantidad_palabras}")

