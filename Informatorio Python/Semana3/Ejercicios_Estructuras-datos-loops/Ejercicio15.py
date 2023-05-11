# 15-Escribe un programa que pida al usuario una cadena de texto y determine
# cuántas veces aparece cada letra en la cadena.

cadena_texto=input("Ingrese un fragmento de texto: ")
cant_letras={}

for letra in cadena_texto:
    if letra in cant_letras:
        cant_letras[letra]+=1
    else:
        cant_letras[letra]=1

print("Frecuencias de letras en el texto:")
for letra, cant_letra in cant_letras.items():
    print(letra, "->", cant_letra)

# El diccionario frecuencias se va llenando a medida que el bucle for va recorriendo cada 
# letra de la cadena de texto ingresada por el usuario.En cada iteración del bucle for, la 
# variable letra toma el valor de la siguiente letra de la cadena de texto. Luego, se utiliza 
# una estructura if-else para verificar si la letra actual (letra) ya está en el diccionario 
# frecuencias. Si la letra ya está en el diccionario, se incrementa su frecuencia en 1 utilizando 
# la siguiente línea de código:

# frecuencias[letra] += 1

# En cambio, si la letra no está en el diccionario, se agrega al diccionario con una frecuencia inicial 
# de 1 utilizando la siguiente línea de código:

# frecuencias[letra] = 1

# Entonces, cada vez que se encuentra una letra que aún no está en el diccionario frecuencias, se agrega esa 
# letra como una nueva clave en el diccionario con una frecuencia inicial de 1. Y cada vez que se encuentra 
# una letra que ya está en el diccionario, se incrementa su frecuencia en 1.Al final del bucle for, 
# el diccionario frecuencias contiene todas las letras que aparecen en la cadena de texto y su frecuencia 
# correspondiente. 
# Por ejemplo, si la cadena de texto ingresada es "hola mundo", el diccionario frecuencias se vería así:

# {'h': 1, 'o': 2, 'l': 1, 'a': 1, ' ': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}