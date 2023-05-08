# 6-Escribe un programa que pida al usuario una palabra y luego imprima la misma
# palabra pero con las letras en orden inverso.

palabra = input("Ingrese una palabra: ")

letras_palabra = list(palabra)
letras_palabra.reverse()
palabra_revertida="".join(letras_palabra)

print(palabra_revertida)

for i in letras_palabra:
    print(i)

print(f"\n{palabra}")

# palabra = input("Ingrese una palabra: ")

# palabra_invertida = ""

# for i in range(len(palabra)-1,-1,-1):
#     palabra_invertida+=palabra[i]


# Explicacion con un ejemplo. Supongamos que tenemos la cadena de caracteres 'hola' 
# y queremos revertirla. El código para revertirla con un for y la función range() quedaría así:

# palabra = 'hola'
# palabra_revertida = ''

# for i in range(len(palabra)-1, -1, -1):
#     palabra_revertida += palabra[i]

# print(palabra_revertida)

# El bucle for se ejecuta de la siguiente manera:

# En la primera iteración, el valor de i es 3, que es el índice del último carácter de la cadena 'hola'. 
# Por lo tanto, la variable palabra_revertida se actualiza con el último carácter de la cadena, 
# que es 'a'.

# En la segunda iteración, el valor de i es 2, que es el índice del penúltimo carácter de la cadena 'hola'. 
# Por lo tanto, la variable palabra_revertida se actualiza con el penúltimo carácter de la cadena, 
# que es 'l'.

# En la tercera iteración, el valor de i es 1, que es el índice del segundo carácter de la cadena 'hola'. 
# Por lo tanto, la variable palabra_revertida se actualiza con el segundo carácter de la cadena, 
# que es 'o'.

# En la cuarta y última iteración, el valor de i es 0, que es el índice del primer carácter de la cadena 
# 'hola'. Por lo tanto, la variable palabra_revertida se actualiza con el primer carácter de la cadena, 
# que es 'h'.
