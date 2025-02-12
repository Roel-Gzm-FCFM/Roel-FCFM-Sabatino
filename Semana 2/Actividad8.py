print("Encontrar el Mayor y Menor en una Lista")

cant = int(input("¿Cuántos números vas a ingresar?: "))

lista_num = []

for i in range(cant):
    num = int(input(f"Escribe el {i+1}º número: "))
    lista_num.append(num)
    i += 1

print(f"De entre los números {lista_num}\nEl número mayor es: {max(lista_num)}.\nEl número menor es: {min(lista_num)}.")
