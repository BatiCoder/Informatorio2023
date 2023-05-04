
# 8-Escribir un programa que pida al usuario una cadena de caracteres y muestre
# por pantalla si contiene la letra "a"

""" cadena = input("Ingresa una cadena de caracteres: ")
if "a" in cadena:
    print("La cadena contiene la letra 'a'")
else:
    print("La cadena no contiene la letra 'a'") """

# Primero, se solicita al usuario que ingrese una cadena de caracteres mediante la función input().
# Luego, se utiliza un condicional if para verificar si la letra "a" está presente en la cadena mediante el operador in.
# Si la letra "a" está en la cadena, se imprime un mensaje indicando que la cadena contiene la letra "a".
# De lo contrario, se imprime un mensaje indicando que la cadena no contiene la letra "a".

# ----------------------------------------------------------------------------------------------------------------------------------

""" La función in en Python es un operador que se utiliza para verificar si un elemento se encuentra en una secuencia,
como una lista, una cadena de caracteres o una tupla. La sintaxis básica del operador in es la siguiente:

(elemento) in (secuencia)

donde elemento es el elemento que se busca en la secuencia. El operador in devuelve un valor booleano, True si el elemento 
se encuentra en la secuencia y False en caso contrario.

Aquí hay algunos ejemplos de cómo utilizar el operador in en Python: """

# Verificar si un elemento está en una lista.

# numeros = [1, 2, 3, 4, 5]
# if 3 in numeros:
#     print("El número 3 está en la lista")

# # Verificar si un caracter está en una cadena de caracteres
# nombre = "Juan"
# if "a" in nombre:
#     print("La letra 'a' está en el nombre")

# # Verificar si una clave está en un diccionario
# telefonos = {"Juan": "1234", "Pedro": "5678", "Maria": "9101"}
# if "Pedro" in telefonos:
#     print("El teléfono de Pedro es", telefonos["Pedro"])


""" En el primer ejemplo, se verifica si el número 3 está en la lista numeros. En el segundo ejemplo, se verifica 
si la letra "a" está en la cadena de caracteres nombre. En el tercer ejemplo, se verifica si la clave "Pedro" 
está en el diccionario telefonos. En todos los casos, el operador in devuelve True si el elemento está presente 
en la secuencia y False si no lo está. """
