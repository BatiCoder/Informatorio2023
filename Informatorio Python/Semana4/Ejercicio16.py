
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

# Resumen:

# La función eliminar_duplicados toma una lista como parámetro y crea una nueva lista sin duplicados. 
# Se recorre cada elemento de la lista original y, si el elemento no está presente en la lista 
# sin duplicados, se agrega a esta última. Al final, se retorna la lista sin duplicados.

# Ejemplo de uso.
lista_original = [1, 2, 3, 3, 4, 2, 5, 1]
lista_sin_duplicados = eliminar_duplicados(lista_original)
print(lista_sin_duplicados)  # Imprime la nueva lista sin duplicados: [1, 2, 3, 4, 5].

# Ejemplo de uso:
# Se utiliza la función eliminar_duplicados con la lista original [1, 2, 3, 3, 4, 2, 5, 1]. El resultado 
# se almacena en la variable lista_sin_duplicados. Luego, se imprime el contenido de lista_sin_duplicados, 
# que es la nueva lista sin duplicados: [1, 2, 3, 4, 5].
