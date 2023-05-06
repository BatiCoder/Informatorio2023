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
texto_usuario = input(
    "\nIngrese un texto cualquiera, por ej un articulo o frase: ")

# Definir una lista, para las letras ingresadas por teclado.
lista_letras = []
print("\nA continuacion ingrese 3 letras a eleccion...")

# Estructura for para cargar las letras en la lista lista_letras[].
for i in range(3):
    letra = input(f"Ingrese la {i+1}º letra: ")
    lista_letras.append(letra)

# Convertir el texto y las letras dentro de la lista de letras en minusculas.
texto_usuario = texto_usuario.lower()
lista_letras = [letra.lower() for letra in lista_letras]

# Para contar la cantidad de veces que aparecen las letras de una lista en un texto.
# Se definde un diccionario para contar la cantidad de veces que aparece cada letra en el texto.
contador = {}

# Estructura for que recorre los substrings de la lista de letras en el texto.
for letra in lista_letras:
    contador[letra] = texto_usuario.count(letra)

# Imprimir el contador.
print(
    f"\nAqui se muestra la cantidad de letras que ingresaste, existentes en el texto: {contador}")

# Separar el texto en una lista de palabras.
palabras = texto_usuario.split()
# Contar la cantidad de palabras en la lista.
cantidad_palabras = len(palabras)

# Imprimir la cantidad de palabras en el texto.
print("\nLa cantidad de palabras en el texto es:", cantidad_palabras)

# Puedes obtener la primera letra de un texto utilizando la indexación con corchetes y el índice 0
primera_letra = texto_usuario[0]
# De manera similar, puedes obtener la última letra de un texto utilizando la indexación con corchetes y el índice -1
segunda_letra = texto_usuario[-1]

# La indexación de una cadena comienza desde 0 y se extiende hasta n-1, donde n es la longitud de la cadena.

# Invertir el texto.
texto_inverso = ''.join(reversed(texto_usuario))

# Imprimir el texto invertido.
print("\nAsi queda el texto invertido: ")
print(f"{texto_inverso}")

# Identificar si la palabra Python existe en el texto, e imprimir por pantalla si lo esta o no.
if "PYTHON" in texto_usuario or "python" in texto_usuario:
    print("\nLa palabra Python existe en el texto.")
else:
    print("\nLa palabra Python no existe en el texto.")
