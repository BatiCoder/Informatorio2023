
# 10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
# una vocal o una consonante.

letra=input("Ingrese una letra: ")

if letra in "aeiouAEIOU":
    print("Es vocal")
elif letra:
    print("Es consonante") 

""" Otra manera de hacerlo seria... """

# letra = input("Ingresa una letra: ").lower()

# if letra in 'aeiou':
#     print("La letra ingresada es una vocal")
# else:
#     print("La letra ingresada es una consonante")

""" Primero, se solicita al usuario que ingrese una letra utilizando la función input(). La letra ingresada se convierte
en minúscula utilizando el método lower() para facilitar la comparación. Luego, se utiliza un condicional if con el 
operador in para determinar si la letra es una vocal o una consonante.Si la letra se encuentra en el conjunto de caracteres
'aeiou', se imprime un mensaje indicando que es una vocal. De lo contrario, se imprime un mensaje indicando que es una consonante.
Este programa funciona para cualquier letra ingresada por el usuario, siempre y cuando sea una letra del alfabeto en minúscula. 
El uso del operador in simplifica la comparación y hace que el código sea más legible y fácil de entender. """