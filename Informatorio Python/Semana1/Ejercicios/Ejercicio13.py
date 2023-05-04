# 13-Escribe un programa que solicite al usuario su nombre y su edad, y luego
# imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más.

nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
edad+=10

print(f"El usuario tendra la edad de {edad} en 10 años...")