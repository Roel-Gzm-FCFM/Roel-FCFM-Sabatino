print("Suma de Dígitos.")

numeros = input("Escribe un número entero: ")
suma = 0

for num in numeros:
    suma += int(num)

print(f"La suma de los dígitos {numeros} es: {suma}")