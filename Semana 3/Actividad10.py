def MCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a

n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))

print(f"El MCD de {n1} y {n2} es: {MCD(n1, n2)}.")