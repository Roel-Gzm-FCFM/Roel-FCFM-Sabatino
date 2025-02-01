print("Ejercicio 2: ¿Cuál es tu edad")
edad = int(input("Ingrese la edad: "))

if (edad<12):
    print("Es un niño.")
elif (edad<18):
    print("Es un adolescente.")
elif (edad<60):
    print("Es un adulto.")
else:
    print("Es un adulto mayor.")