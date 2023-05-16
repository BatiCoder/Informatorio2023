
# 13-Crea una función llamada calcular_descuento que tome dos parámetros:
# precio y porcentaje_descuento. La función debe calcular y devolver el precio
# después de aplicar el descuento.

def calcular_descuento(precio, porcentaje_descuento):

    # Calcula el descuento basado en el porcentaje proporcionado
    descuento = precio * porcentaje_descuento / 100

    # Resta el descuento al precio original para obtener el precio con descuento
    precio_con_descuento = precio - descuento

    # Devuelve el precio después de aplicar el descuento
    return precio_con_descuento


# Ejemplo de uso de la función
precio_final = calcular_descuento(100, 20)
print(precio_final)  # Imprimirá 80

    
    