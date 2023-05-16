
# 16-Crea una función llamada eliminar_duplicados que tome una lista como
# parámetro y devuelva una nueva lista sin duplicados, conservando el orden
# original.

def eliminar_duplicados(lista):
    # Crea una lista vacía para almacenar los elementos sin duplicados.
    lista_sin_duplicados = []

    # Recorre cada elemento de la lista original.
    for elemento in lista:
        # Si el elemento no está en la lista sin duplicados, lo agrega.
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)

    # Retorna la lista sin duplicados.
    return lista_sin_duplicados

# Ejemplo de uso.
lista_original = [1, 2, 3, 3, 4, 2, 5, 1]
lista_sin_duplicados = eliminar_duplicados(lista_original)
print(lista_sin_duplicados)  # Imprime la nueva lista sin duplicados: [1, 2, 3, 4, 5].




