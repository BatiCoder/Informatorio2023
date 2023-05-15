
# 7-Crea una función llamada imprimir_pares que tome un número entero como
# parámetro y imprima todos los números pares desde 1 hasta ese número.

def imprimir_pares(numero_entero):
    # Función que imprime los números pares hasta un número dado.
    
    for i in range(1, numero_entero + 1):
        # Itera desde 1 hasta el número ingresado, incluyéndolo.
        
        if i % 2 == 0:
            # Verifica si el número actual es par.
            
            print(f"{i} - ", end="")
            # Imprime el número seguido de un guion y sin salto de línea.