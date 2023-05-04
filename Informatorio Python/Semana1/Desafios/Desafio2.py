#Desafio2

# Escribe un programa que solicite al usuario su información personal, incluyendo

# su nombre completo, edad, estatura, peso, dirección y número de teléfono.
# A continuación, el programa deberá imprimir un mensaje con los datos
# ingresados por el usuario en el siguiente formato:
# La información ingresada es la siguiente:

# Nombre completo: [nombre completo]
# Edad: [edad]
# Estatura: [estatura] cm
# Peso: [peso] kg
# Dirección: [dirección]
# Número de teléfono: [número de teléfono]

nombre_completo=input("\nIngrese su nombre completo: ")
edad=int(input("Ingrese su edad: "))
estatura=float(input("Ingrese su estatura: "))
peso=float(input("Ingrese su peso: "))
direccion=input("Ingrese su direccion:")
num_telefono=input("Ingrese su numero de teléfono: ")

print("\nNombre completo:",nombre_completo)
print("Edad:",edad)
print("Estatura:",estatura)
print("Peso:",peso)
print("Direccion:",direccion)
print("Número de teléfono:",num_telefono)


