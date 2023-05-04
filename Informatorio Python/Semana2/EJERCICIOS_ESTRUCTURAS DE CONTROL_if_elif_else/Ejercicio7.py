
# 7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
# es una letra mayúscula, una letra minúscula, un número o un carácter especial.

""" caracter = input("Introduce un carácter: ")

if caracter.isalpha():
     if caracter.isupper():
         print("El carácter introducido es una letra mayúscula.")
     else:
         print("El carácter introducido es una letra minúscula.")
elif caracter.isdigit():
     print("El carácter introducido es un número.")
else:
    if caracter == " ":
        print("El carácter introducido es un espacio en blanco.")
    elif caracter in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
         print("El carácter introducido es un carácter especial.")
    else:
         print("El carácter introducido no se reconoce como válido.") """


# Puedes usar la función isalpha() para determinar si el carácter es una letra,
# la función isdigit() para determinar si es un número y una serie de condiciones
# para determinar si es un carácter especial.

# En este programa, primero pedimos al usuario que introduzca un carácter y lo almacenamos
# en la variable caracter. Luego, usamos la función isalpha() para determinar si el carácter
# es una letra. Si es así, usamos la función isupper() para determinar si es una letra mayúscula
# o no. Si no es una letra, usamos la función isdigit() para determinar si es un número.

# Si no es una letra ni un número, comprobamos si es un espacio en blanco o un carácter especial
# mediante una serie de condiciones y usando el operador in para determinar si el carácter se
# encuentra en un conjunto de caracteres especiales. Si el carácter no se reconoce como válido,
# mostramos un mensaje de error.


# ----------------------------------------------------------------------------------------------------------------------------
#
# CODIGO HECHO POR KEVIN SILVA, SEGUNDA MANERA.
#

caracter = input("Introduce un carácter: ")

if caracter in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz":
    if caracter in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
        print("El carácter introducido es una letra mayúscula.")
    else:
        print("El carácter introducido es una letra minúscula.")
elif caracter in "0123456789":
    print("El carácter introducido es un número.")
else:
    if caracter == " ":
        print("El carácter introducido es un espacio en blanco.")
    elif caracter in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
        print("El carácter introducido es un carácter especial.")
    else:
        print("El carácter introducido no se reconoce como válido.")

# ----------------------------------------------------------------------------------------------------------------------------
#
# CODIGO MAGICO HECHO POR MARCOS RUBIN.(NO SE PORQUE LE TOMA LOS CARACTERES ESPECIALES.....QUE NO ESTAN)
#
# caracter = input("Introduce un carácter: ")

# if caracter.isalpha():
#     if caracter.isupper():
#         print("El carácter introducido es una letra mayúscula.")
#     else:
#         print("El carácter introducido es una letra minúscula.")
# elif caracter.isdigit():
#     print("El carácter introducido es un número.")
# else:
#     if caracter == " ":
#         print("El carácter introducido es un espacio en blanco.")
#     elif caracter == "!" or "#" or "$" or "%" or "&" or "'" or "(" or ")" or "*" or "+" or "," or "-" or "." or "/" or ":" or ";" or "<" or "=" or ">" or "?" or "@" or "[" or " \ " or "]" or "^" or "_" or "`" or "{" or "|" or "}" or "~" or ":":
#         print("El carácter introducido es un carácter especial.")
#     else:
#         print("El carácter introducido no se reconoce como válido.")
