# 9-Crear una lista con los nombres de tres países y ordenar la lista en orden
# alfabético. Mostrar la lista resultante.

# Definir la lista
paises = ['Argentina', 'Brasil', 'Canada']

# Ordenar la lista en orden alfabético
paises.sort()

# Imprimir la lista resultante
print(paises)

# Para ordenar una lista de países en orden alfabético en Python, puedes utilizar
# el método sort() de las listas. Este método ordena la lista de forma permanente,
# es decir, modifica la lista original. Si quieres mantener la lista original sin
# cambios, puedes crear una copia de la lista y ordenar la copia.

# Si quieres mantener la lista original sin cambios, puedes hacer una copia de la lista
# y ordenar la copia:

"""

# Crear una lista con los nombres de tres países
paises = ['España', 'México', 'Argentina']

# Crear una copia de la lista y ordenarla en orden alfabético
paises_ordenados = sorted(paises)

# Imprimir la lista resultante
print(paises_ordenados)

"""

# Este código imprimirá la lista ['Argentina', 'España', 'México']. La lista original
# paises permanecerá sin cambios. En ambos casos, se ha utilizado el método sort() para
# ordenar la lista de países en orden alfabético. Si se utiliza la función sorted() en lugar
# del método sort(), se crea una nueva lista ordenada sin modificar la lista original.
