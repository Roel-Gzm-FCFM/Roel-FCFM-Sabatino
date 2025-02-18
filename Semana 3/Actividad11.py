def Det(matriz):
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    det = (a*e*i + b*f*g + c*d*h) - (c*e*g + b*d*i + a*f*h)
    return det

matriz = []

for i in range(3):
    fila = []
    for j in range(3):
        num = int(input(f"Ingresa el número en la posición a[{i+1},{j+1}]: "))
        fila.append(num)
    matriz.append(fila)

print(f"El determinante de la matriz:")
for fila in matriz:
    print(fila)
print(f"Es {Det(matriz)}.")