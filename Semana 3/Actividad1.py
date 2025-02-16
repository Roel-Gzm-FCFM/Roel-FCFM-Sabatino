def obtener_datos(nombre, edad=18):
    print(f"Tu nombre es {nombre}, y tienes {edad} añoss.")

print("Función con Valores por Omisión")
nombre = input("¿Cuál es tu nombre?: ")

try:
    edad = int(input("¿Qué edad tienes?: "))
    obtener_datos(nombre, edad)
except:
    obtener_datos(nombre)