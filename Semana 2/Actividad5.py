print("Contador de Vocales.")

texto = input("Escribe la palabra: ")
cont = 0
vocales = "aeiouAEIOU"

for letra in texto:
    if letra in vocales:
        cont += 1

print(f"Hay {cont} vocales en la palabra: {texto}.")