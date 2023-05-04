
# 4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
# pantalla si está aprobado (5 o más) o no.

nota=int(input("Ingrese la nota del alumno: "))

if nota>=5:
    print("\nAprobado")
else:
    print("Desaprobado")