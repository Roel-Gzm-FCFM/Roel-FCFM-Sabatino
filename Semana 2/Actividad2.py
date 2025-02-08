num_dado = int(input("Ingresa un número entre 1 y 20: "))

while num_dado < 1 or num_dado > 20:
    print("Error. Debiste escribir un número entre el 1 y 20.")
    num_dado = int(input("Ingresa un número entre 1 y 20: "))

factorial = 1
num = num_dado

while num > 1:
    factorial *= num
    num -= 1

print(f"El factorial de {num_dado} es {factorial}")