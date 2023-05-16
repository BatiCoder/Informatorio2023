
# 11-Crea una función llamada contar_vocales que tome una cadena de texto como
# parámetro y devuelva el número de vocales que contiene.

def contar_vocales(cadena_texto):
# Función que cuenta la cantidad de vocales en una cadena de texto.
    
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # Lista de vocales en minúsculas y mayúsculas.
    
    cant_vocales = 0
    # Inicializa el contador de vocales en 0.
    
    for caracter in cadena_texto:
        # Itera sobre cada caracter en la cadena de texto.
        
        if caracter in vocales:
            # Verifica si el caracter actual está presente en la lista de vocales.
            
            cant_vocales += 1
            # Incrementa el contador de vocales en 1.
    
    return cant_vocales
    # Devuelve la cantidad total de vocales encontradas en la cadena de texto.

print(contar_vocales("Bienvenidos a Ushuaia"))
