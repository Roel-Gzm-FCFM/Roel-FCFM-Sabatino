print("Ordenar una Lista.")

cant = int(input("¿Cuántos números vas a ingresar?: "))

lista_num = []

for i in range(cant):
    num = int(input(f"Escribe el {i+1}º número: "))
    lista_num.append(num)
    i += 1

lista_num.sort()

print(f"La lista ordenada de los numeros dados es: {lista_num}")
