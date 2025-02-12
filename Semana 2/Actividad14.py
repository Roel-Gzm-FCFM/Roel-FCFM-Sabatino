print("Generar Números Aleatorios.")

n = int(input("¿Cuántos numeros aleatorios quieres generar?: "))
lista = []

from random import randint

for i in range(n):
    num_aleatorio = randint(1, 100)
    lista.append(num_aleatorio)

print(f"Los números aleatorios son: {lista}.")