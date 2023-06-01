"""
Una planta que fabrica perfiles de hierro posee un lote de n piezas.Confeccionar un programa que pida ingresar 
por teclado la cantidad de piezas a procesar y luego ingrese la longitud de cada perfil; sabiendo que la pieza 
cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de piezas 
aptas que hay en el lote.

"""

lote_piezas = int(input("\nIngrese la cantidad de piezas de perfiles de hierro a procesar: "))  # Solicitamos al usuario la cantidad de piezas a procesar y la almacenamos en lote_piezas
piezas_aptas = 0  # Inicializamos la variable piezas_aptas en 0
x = 1  # Inicializamos la variable x en 1

while x <= lote_piezas:  # Mientras x sea menor o igual a lote_piezas, repetiremos el bucle
    medida_pieza = float(input(f"\nIngrese la longitud en cm. de la {x}º pieza: "))  # Solicitamos al usuario la longitud de la pieza y la almacenamos en medida_pieza
    if medida_pieza >= 1.20 and medida_pieza <= 1.30:  # Verificamos si la medida de la pieza está entre 1.20 y 1.30
        print("\nPieza apta.")
        piezas_aptas += 1  # Incrementamos el contador de piezas aptas en 1
    else:
        print("\nPieza no apta.")
        
    x += 1  # Incrementamos el valor de x en 1 en cada iteración del bucle

print(f"\nLa cantidad de piezas aptas es: {piezas_aptas}")
# Imprimimos la cantidad de piezas aptas utilizando un f-string para formatear el texto y mostrar el valor calculado.

