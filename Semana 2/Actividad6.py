print("Tabla de Multiplicar.")

num = int(input("Ingresa el número para la tabla de multiplicar: "))

for i in range(1,11):
    result = num * i
    print(f"{num} x {i} = {result}")