def suma_diagonales():
    matriz = []
    
    print("Ingresa los valores de la matriz 5x5:")
    for i in range(5):
        fila = list(map(int, input().split()))
        matriz.append(fila)
    
    suma_principal = 0
    suma_secundaria = 0
    
    for i in range(5):
        suma_principal += matriz[i][i]
        suma_secundaria += matriz[i][4 - i]
    
    print("Suma de la diagonal principal:", suma_principal)
    print("Suma de la diagonal secundaria:", suma_secundaria)

suma_diagonales()