# 13-Escribe un programa que pida al usuario un número y luego imprima un
# triángulo de asteriscos con esa cantidad de filas.
# *
# **
# ***
# ****
# *****

num=int(input("Ingrese un numero entero: "))
puntito="*"

for i in range(1,num+1):
    print(f"{puntito*i}")
