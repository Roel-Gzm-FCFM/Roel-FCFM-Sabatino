def Calif(*args):
    Prom = sum(args)/len(args)
    return Prom

print("Función para Calcular el Promedio.")
while True:
    try:
        n = int(input("¿Cuántas calificaciones vas a promediar?: "))
        if n > 0:
            break
        else:
            print("Error. Ingresa un número mayor a 0.")
    except:
        print("Ingresa un número válido.")

califcs = []
for i in range(1, n+1):
    while True:
        try:
            num_calif = int(input(f"Escribe la {i}º calificación: "))
            califcs.append(num_calif)
            break
        except:
            print("Ingresa un número válido.")

print(f"El promedio de las calificaciones:\n{califcs}\nEs {Calif(*califcs)}.")