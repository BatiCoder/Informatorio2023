
# 4-Crea una función llamada es_capicua que tome un número como parámetro y
# devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
# derecha a izquierda) y False en caso contrario.

def es_capicua(numero):  
# Definición de una función llamada "es_capicua" que recibe un parámetro llamado "numero"
    
    numero_inverso = int(str(numero)[::-1])  
    # Convierte el número en una cadena, invierte la cadena y lo convierte de nuevo en un entero
    
    if numero_inverso == numero:  # Compara el número invertido con el número original
        print("El numero es capicua.")  # Si son iguales, imprime que el número es capicúa
    else:
        print("El numero no es capicua.")  # Si son diferentes, imprime que el número no es capicúa

es_capicua(int(input("Ingrese un numero: ")))
# Llama a la función "es_capicua" y pasa como argumento el número ingresado por el usuario


