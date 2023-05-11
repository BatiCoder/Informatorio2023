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



