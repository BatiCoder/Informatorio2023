# 10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
# una vocal o una consonante.

letra=input("Ingrese una letra: ")

if letra in "aeiouAEIOU":
    print("Es vocal")
elif letra:
    print("Es consonante") 
