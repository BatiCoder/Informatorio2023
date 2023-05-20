
""" Desafío 4: La inmobiliaria """

# Requisitos técnicos:
# - Operadores.
# - Estructuras de datos.
# - Estructuras de control de flujo.
# - Funciones

"""

Una inmobiliaria de tu ciudad solicita un sistema para automatizar la gestión de sus inmuebles.
Se te pide construir un programa que permita: 

"""

#  Agregar, editar y eliminar inmuebles a la lista.
# Las funciones deben ajustarse al formato de lista y reglas de validación.

#  Cambiar el estado de un inmueble, sin modificar sus demás datos.
# Las funciones deben ajustarse al formato de lista y reglas de validación.

#  Hacer búsqueda de inmuebles en función de un presupuesto dado.
# La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con
# los inmuebles cuyo precio sea menor o igual que el dado y el estado sea Disponible o
# Reservado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada
# diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las
# reglas de precio en función de la zona.

""" Formato de lista. """

# [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
# {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
# {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
# {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
# {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

""" Reglas de validación. """

#  Inmuebles solo de zona: A, B o C.
#  Inmuebles con estado: Disponible, Reservado o Vendido.
#  No opera con inmuebles:
#  Anteriores al año 2000.
#  Menores de 60 metros cuadrados.
#  Menores de 2 habitaciones.

""" Reglas de precio. """

#  Zona A: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100)
#  Zona B: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 1.5
#  Zona C: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 2


# Función para agregar un inmueble a la lista de inmuebles
def agregar_inmueble(lista_inmuebles, inmueble):
    # Se verifica si el inmueble es válido llamando a la función validar_inmueble
    if validar_inmueble(inmueble):
        # Si el inmueble es válido, se agrega a la lista de inmuebles
        lista_inmuebles.append(inmueble)
        print("Inmueble agregado correctamente.")
    else:
        # Si el inmueble no es válido, se muestra un mensaje de error
        print("El inmueble no cumple con las reglas de validación.")
        

# Función para editar un inmueble en la lista de inmuebles
def editar_inmueble(lista_inmuebles, indice, inmueble):
    # Se verifica si el inmueble es válido llamando a la función validar_inmueble
    if validar_inmueble(inmueble):
        # Se verifica si el índice es válido dentro de la lista de inmuebles
        if indice >= 0 and indice < len(lista_inmuebles):
            # Si el inmueble y el índice son válidos, se actualiza el inmueble en la lista
            lista_inmuebles[indice] = inmueble
            print("Inmueble editado correctamente.")
        else:
            # Si el índice no es válido, se muestra un mensaje de error
            print("Índice de inmueble inválido.")
    else:
        # Si el inmueble no es válido, se muestra un mensaje de error
        print("El inmueble no cumple con las reglas de validación.")


# Función para eliminar un inmueble de la lista de inmuebles
def eliminar_inmueble(lista_inmuebles, indice):
    # Se verifica si el índice es válido dentro de la lista de inmuebles
    if indice >= 0 and indice < len(lista_inmuebles):
        # Si el índice es válido, se elimina el inmueble de la lista
        del lista_inmuebles[indice]
        print("Inmueble eliminado correctamente.")
    else:
        # Si el índice no es válido, se muestra un mensaje de error
        print("Índice de inmueble inválido.")


# Función para cambiar el estado de un inmueble en la lista de inmuebles
def cambiar_estado(lista_inmuebles, indice, nuevo_estado):
    # Se verifica si el índice es válido dentro de la lista de inmuebles
    if indice >= 0 and indice < len(lista_inmuebles):
        # Si el índice es válido, se actualiza el estado del inmueble
        lista_inmuebles[indice]['estado'] = nuevo_estado
        print("Estado del inmueble cambiado correctamente.")
    else:
        # Si el índice no es válido, se muestra un mensaje de error
        print("Índice de inmueble inválido.")


# Función para buscar inmuebles por presupuesto en la lista de inmuebles
def buscar_inmuebles_por_presupuesto(lista_inmuebles, presupuesto):
    # Se crea una lista para almacenar los inmuebles encontrados
    inmuebles_encontrados = []
    # Se recorre cada inmueble en la lista de inmuebles
    for inmueble in lista_inmuebles:
        # Se verifica si el estado del inmueble está en 'Disponible' o 'Reservado'
        if inmueble['estado'] in ['Disponible', 'Reservado']:
            # Se calcula el precio del inmueble llamando a la función calcular_precio
            precio = calcular_precio(inmueble)
            # Se compara el precio calculado con el presupuesto dado
            if precio <= presupuesto:
                # Si el precio es menor o igual al presupuesto, se crea una copia del inmueble
                # y se agrega el precio calculado como un nuevo campo 'precio' en la copia
                inmueble_con_precio = inmueble.copy()
                inmueble_con_precio['precio'] = precio
                # Se agrega el inmueble con precio a la lista de inmuebles encontrados
                inmuebles_encontrados.append(inmueble_con_precio)
    # Se devuelve la lista de inmuebles encontrados
    return inmuebles_encontrados


# Función para validar un inmueble
def validar_inmueble(inmueble):
    # Se verifican las condiciones de validación para el inmueble
    if inmueble['zona'] not in ['A', 'B', 'C']:
        return False
    if inmueble['estado'] not in ['Disponible', 'Reservado', 'Vendido']:
        return False
    if inmueble['año'] < 2000:
        return False
    if inmueble['metros'] < 60:
        return False
    if inmueble['habitaciones'] < 2:
        return False
    # Si el inmueble cumple con todas las condiciones, se considera válido
    return True


# Función para calcular el precio de un inmueble
def calcular_precio(inmueble):
    # Se obtienen los atributos necesarios del inmueble
    metros = inmueble['metros']
    habitaciones = inmueble['habitaciones']
    garaje = inmueble['garaje']
    antiguedad = 2023 - inmueble['año']
    zona = inmueble['zona']
    

    # Se calcula el precio según la zona del inmueble y otros atributos
    if zona == 'A':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100)
    elif zona == 'B':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 1.5
    else:
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100)
    
    # Se devuelve el precio calculado
    return precio
