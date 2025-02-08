n = int(input("Ingresa un número entre 1 y 50: "))

while n < 1 or n > 50:
    print("Error. Debes ingresar un número entre 1 y 50.")
    n = int(input("Ingresa un número entre 1 y 50: "))

fibonacci = [0, 1]

while len(fibonacci) < n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(f"Secuencia de Fibonacci: {fibonacci[:n]}")