
# 12-Crea una función llamada convertir_temperatura que tome una temperatura
# en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión
# es: Fahrenheit = (Celsius * 9/5) + 32.

def convertir_temperatura(temperatura_celsius):
    # Convierte una temperatura en grados Celsius a grados Fahrenheit.

    # Fórmula de conversión: Fahrenheit = (Celsius * 9/5) + 32
    grados_fahrenheit = (temperatura_celsius * 9/5) + 32

    # Retorna la temperatura convertida en grados Fahrenheit.
    return grados_fahrenheit

# Ejemplo de uso: Convertir 25 grados Celsius a grados Fahrenheit
temperatura_fahrenheit = convertir_temperatura(25)
print(temperatura_fahrenheit)  # Imprime el resultado: 77.0

# La función convertir_temperatura toma una temperatura en grados Celsius como entrada 
# y aplica la fórmula de conversión para calcular la temperatura equivalente en grados 
# Fahrenheit. Luego, devuelve la temperatura convertida. En el ejemplo de uso, se convierten 
# 25 grados Celsius a grados Fahrenheit y se imprime el resultado, que en este caso sería 77.0

