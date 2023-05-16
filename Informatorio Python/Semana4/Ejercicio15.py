
# 15-Crea una función llamada contar_palabras que tome una cadena de texto
# como parámetro y devuelva el número de palabras que contiene. Se considera
# que las palabras están separadas por espacios.

def contar_palabras(cadena_texto):
    
    # Divide la cadena en palabras usando espacios como separadores
    lista_palabras = cadena_texto.split()
    
    # Devuelve el número de palabras en la lista
    return len(lista_palabras)

# El método .split() utilizado en el código divide una cadena de texto en una 
# lista de palabras utilizando los espacios como separadores. En este caso, al 
# llamar cadena_texto.split(), se crea una lista lista_palabras que contiene 
# todas las palabras individuales de la cadena original.

# Esto es útil para contar el número de palabras, ya que luego se utiliza len(lista_palabras) 
# para obtener la longitud de la lista, es decir, el número total de palabras en la cadena 
# de texto.