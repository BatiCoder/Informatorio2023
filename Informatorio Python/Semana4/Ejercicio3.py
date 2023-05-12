
# 3-Crea una función llamada invertir_cadena que tome una cadena de texto como
# parámetro y devuelva la cadena invertida.

def invertir_cadena(cadena_texto):
    # Esta función toma una cadena de texto y la imprime invertida palabra por palabra.

    # Parámetros:
    # - cadena_texto: La cadena de texto a invertir.

    palabras = cadena_texto.split()  
    # Dividir la cadena en palabras utilizando el espacio como separador
    palabras_invertidas = palabras[::-1]  
    # Invertir el orden de las palabras utilizando slicing
    cadena_inversa = ' '.join(palabras_invertidas)  
    # Unir las palabras invertidas en una cadena de texto separadas por espacio
    print(cadena_inversa)  
    # Imprimir la cadena invertida palabra por palabra


