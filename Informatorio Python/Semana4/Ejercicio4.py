
# 4-Crea una función llamada es_capicua que tome un número como parámetro y
# devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
# derecha a izquierda) y False en caso contrario.

def es_capicua(numero):  
# Definición de una función llamada "es_capicua" que recibe un parámetro llamado "numero"
    
    numero_inverso = int(str(numero)[::-1])  
    # Convierte el número en una cadena, invierte la cadena y lo convierte de nuevo en un entero
    
    if numero_inverso == numero:  # Compara el número invertido con el número original
        return True
    else:
        return False

