def MODA(lista):
    contador = {}
    for i in lista:
        if i in contador:
            contador[i] += 1
        else:
            contador[i] = 1
    
    moda_lista = max(contador, key=lambda num: contador[num])
    return print(f"La moda es {moda_lista} y se repite {contador[moda_lista]} veces.")

print("Cálculo de la Moda.")

numeros = []
cant_num = int(input("¿Cuántos números vas a ingresar? "))

for i in range(1, cant_num + 1):
    num = float(input(f"Ingresa el {i}º número: "))
    numeros.append(num)

MODA(numeros)