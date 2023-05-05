# DESAFIO 2: ANALIZADOR DE TEXTOS.

# Requisitos tecnicos:

# 1-Métodos y propiedades de string.
# 2-Indexar estructuras de datos.
# 3-Todos los tipos de datos.

# Se te pide crear un programa que le pida al usuario que ingresar un texto
# cualquiera, por ejemplo, un artículo o una frase.
# Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
# elección.
# Nuestro código va a procesar esa información para realizar los análisis
# necesarios para devolverle al usuario la siguiente información:

# 1- Cantidad de veces que aparece cada una de letras que eligió.
# Tip 1: almacenar las letras en una lista para usar algún método de contar un substring en un
# string
# Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar que se
# encuentren todas las letras, pasa tanto el texto original como las letras a buscar a
# minúscula.

# 2- Cuantas palabras hay en total en todo el texto.
# Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular su longitud.

# 3- Cual es la primera letra y cuál es la última. (Indexación)

# 4- Mostrar el texto en orden inverso.

# 5- Decir si la palabra "python" aparece en el texto.
# Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un
# string para mostrar al usuario.

# Se le pide al usuario que ingrese un fragmento de texto cualquiera por teclado.
texto_usuario = input("\nIngrese un texto cualquiera, por ej un articulo o frase: ")

# Definir una lista, para las letras ingresadas por teclado
lista_letras = []
print("\nA continuacion ingrese 3 letras a eleccion...")

for i in range(3):
    letra = input(f"Ingrese la {i+1}º letra: ")
    lista_letras.append(letra)

print("\nLa lista resultante es: ", lista_letras)
