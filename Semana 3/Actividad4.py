def Factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

print("Función para Calcular el Factorial.")
num = int(input("Ingresa un número: "))
print(f"El factorial de {num} es {Factorial(num)}.")