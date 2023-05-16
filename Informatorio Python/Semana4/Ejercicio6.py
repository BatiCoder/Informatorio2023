
# 6-Crea una función llamada es_par que tome un número como parámetro y
# devuelva Es par si el numero cumple con dichas condiciones y en caso contrario
# devuelva Es impar o No es par.

def es_par(num):
# Función que verifica si un número es par o impar.
    
    if num % 2 == 0:
        return "Es par"
    else:
        return "Es impar"
