def Suma(*args):
    print(f"La suma de los números es {sum(args)}")

print("Número Arbitrario de Argumentos.")

lista_suma = []
n = int(input("¿Cuántos números vas a sumar?"))
for num in range(1, n+1):
    num_ingresado = int(input(f"Escribe el {num}º número: "))
    lista_suma.append(num_ingresado)
    num += 1

Suma(*lista_suma)