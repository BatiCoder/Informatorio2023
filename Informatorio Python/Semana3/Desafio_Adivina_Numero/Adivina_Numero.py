
# Desafío 3: Adivina el número
# Requisitos técnicos:

# - Operadores lógicos.
# - Operadores de comparación.
# - Control de flujo - Condicionales.
# - Control de Flujo - Repetitivas.

# Vamos a crear un juego completamente funcional.
# Para ello el programa debe:

#  Pedir al usuario que ingrese su nombre.
#  Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos para adivinarlo.
#  Generar aleatoriamente un número entero entre 1 y 100.

# tip 1: importar de la biblioteca random la función randint (Tu profe te explicará en clase cómo hacerlo)
#  Informarle al usuario cuántos intentos le quedan y solicitarle que ingrese un número.
# El "número" ingresado por el usuario puede:
#  No ser un número entero, en éste caso avisarle que no es un número entero el que ingresó.

# tip 2: con el método isdigit() puedes saber si es posible convertir a entero
#  Ser menor al que tiene que adivinar, en éste caso informarle que el número a adivinar es mayor.
#  Ser mayor al que tiene que adivinar, en éste caso informarle que el número a adivinar es menor.
#  Igual al que tiene que adivinar, en éste caso informarle que ha ganado y decirle en cuál intento
# lo adivinó.
#  Si el usuario no ingresa un número entero no debes descontarle un intento, en los demás casos si
# debes descontarle un intento.
#  En cada intento debes informarle al usuario los intentos que le quedan disponibles y solicitarle que
# ingrese otro número.
#  Si el usuario no acierta en los 8 intentos, debes informarle que se agotaron los intentos y cuál era el
# número que tenía que adivinar.

from random import randint
# Importar la función randint de la biblioteca random.

nombre_usuario = input("\nIngrese su nombre: ")
# Solicitar al usuario que ingrese su nombre y guardarlo en la variable nombre_usuario.

numero_aleatorio = randint(1, 100)
# Generar un número aleatorio entre 1 y 100 y guardarlo en la variable numero_aleatorio.

print(f"\nJuguemos un juego {nombre_usuario}, intenta adivinar el número entero que puede ir del 1 al 100")
# Imprimir un mensaje de bienvenida y las instrucciones del juego.

numero_intentos = 8
# Establecer el número de intentos disponibles para el usuario.

while numero_intentos > 0:
    # Iniciar un ciclo while que se repetirá hasta que se agoten los intentos.

    print(f"\nIntentos disponibles: {numero_intentos}")
    # Mostrar al usuario cuántos intentos le quedan.

    num_ingresado = input("\nElige un número: ")
    # Solicitar al usuario que ingrese un número.

    if not num_ingresado.isdigit():
        # Verificar si la entrada no es un número entero.
        print("\nERROR 404 NOT FOUND: No ingresaste un número entero...")
        continue
        # Si no es un número entero, mostrar un mensaje de error y volver al principio del ciclo while.

    num_usuario = int(num_ingresado)
    # Convertir la entrada del usuario a un número entero y guardarlo en la variable num_usuario.

    if num_usuario > numero_aleatorio:
        # Verificar si el número ingresado por el usuario es mayor que el número aleatorio.
        print("\nEl número a adivinar es menor")
        # Mostrar un mensaje indicando que el número a adivinar es menor.

    elif num_usuario < numero_aleatorio:
        # Verificar si el número ingresado por el usuario es menor que el número aleatorio.
        print("\nEl número a adivinar es mayor")
        # Mostrar un mensaje indicando que el número a adivinar es mayor.

    else:
        # Si ninguno de los casos anteriores se cumple, significa que el usuario ha adivinado el número.
        print(f"\n¡BIEN AHIIII {nombre_usuario}! Adivinaste en el intento número {9 - numero_intentos}.")
        break
        # Mostrar un mensaje de felicitaciones y salir del ciclo while.

    numero_intentos -= 1
    # Descontar un intento después de cada intento del usuario

    if numero_intentos == 0:
        # Verificar si se agotaron los intentos disponibles
        print(f"\nSe agotaron los intentos. El número a adivinar era: {numero_aleatorio}")
        # Mostrar un mensaje indicando que se agotaron los intentos y cuál era el número a adivinar







