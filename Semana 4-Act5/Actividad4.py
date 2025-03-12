def transpuesta():
    matriz = []
    
    print("Ingresa los valores de la matriz 3x3:")
    for i in range(3):
        fila = list(map(int, input().split()))
        matriz.append(fila)
    
    transpuesta = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila.append(matriz[j][i])
        transpuesta.append(fila)
    
    print("Matriz transpuesta:")
    for fila in transpuesta:
        print(fila)

transpuesta()