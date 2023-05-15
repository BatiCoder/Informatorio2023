
# 8-Crea una función llamada es_palindromo que tome una cadena de texto como
# parámetro y devuelva es palindromo si es un palíndromo (es decir, si se lee igual
# de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso
# contrario.

def es_palindromo(cadena_texto):
# Función que verifica si una cadena de texto es un palíndromo.

    cadena_texto=cadena_texto.lower()
    #Pasamos la cadena a minusculas, para que pueda distinguir minusculas de mayusculas.

    cadena_texto_inversa=cadena_texto[::-1]
    # Invierte la cadena de texto utilizando el slicing.

    if cadena_texto==cadena_texto_inversa: # Compara la cadena original con la cadena invertida.
        return "Es palindromo"
    else:
        return "No es palindromo"

print(es_palindromo("Radar"))