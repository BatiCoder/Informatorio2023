# 7-Escribe un programa que pida al usuario una palabra y determine si es un
# palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
# izquierda).

palabra = input("Ingrese una palabra: ")

palabra_reves = ""

for i in range(len(palabra)-1, -1, -1):
    palabra_reves += palabra[i]

if palabra == palabra_reves:
    print("Es un palindromo")
else:
    print("No es palindromo")
    

