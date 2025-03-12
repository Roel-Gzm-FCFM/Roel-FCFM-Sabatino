def suma_matrices():
    matriz1 = []
    matriz2 = []
    
    print("Ingresa los valores de la primera matriz 3x3:")
    for i in range(3):
        fila = list(map(int, input().split()))
        matriz1.append(fila)
    
    print("Ingresa los valores de la segunda matriz 3x3:")
    for i in range(3):
        fila = list(map(int, input().split()))
        matriz2.append(fila)
    
    resultado = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila)
    
    print("Suma de matrices:")
    for fila in resultado:
        print(fila)

suma_matrices()