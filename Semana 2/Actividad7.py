print("Suma de Elementos en una Lista")

cant = int(input("¿Cuántos números son los que quieres sumar?: "))
numeros = []

for i in range(cant):
    num = int(input(f"Escribe el {i+1}º número: "))
    numeros.append(num)
    i += 1

suma = 0
for num_suma in numeros:
    suma += num_suma

print(f"El total de la suma de la lista de números {numeros} es: {suma}")