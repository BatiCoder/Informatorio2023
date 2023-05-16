
# 17-Crea una función llamada es_anagrama que tome dos cadenas de texto como
# parámetros y devuelva True si son anagramas (es decir, si tienen las mismas
# letras pero en distinto orden), o False en caso contrario.

def es_anagrama(cadena1, cadena2):
    
    # Verifica si las cadenas tienen la misma longitud
    if len(cadena1) != len(cadena2):
        return False

    # Convierte ambas cadenas a minúsculas
    cadena1 = cadena1.lower()
    cadena2 = cadena2.lower()

    # Crea diccionarios para contar la frecuencia de cada caracter en cada cadena
    frecuencia1 = {}
    frecuencia2 = {}

    # Contabiliza la frecuencia de caracteres en la primera cadena
    for caracter in cadena1:
        frecuencia1[caracter] = frecuencia1.get(caracter, 0) + 1

    # Contabiliza la frecuencia de caracteres en la segunda cadena
    for caracter in cadena2:
        frecuencia2[caracter] = frecuencia2.get(caracter, 0) + 1

    # Compara los diccionarios de frecuencia
    if frecuencia1 == frecuencia2:
        return True
    else:
        return False
    
# De esta manera, se verifica primero si las cadenas tienen la misma longitud, antes de realizar 
# la comparación, se convierten ambas cadenas a minúsculas utilizando el método lower(). Esto 
# garantiza que las mayúsculas y las minúsculas sean tratadas de la misma manera al contar la 
# frecuencia de cada caracter y realizar la comparación.    

# Ejemplo de uso de la funcion.
cadena_1 = "roma"
cadena_2 = "amor"
resultado = es_anagrama(cadena_1, cadena_2)
print(resultado)  # Imprime True, ya que "roma" y "amor" son anagramas
