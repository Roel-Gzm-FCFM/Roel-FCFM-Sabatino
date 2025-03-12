def buscar_elemento():
    n = int(input("Número de filas: "))
    m = int(input("Número de columnas: "))
    
    matriz = []
    for i in range(n):
        fila = list(map(int, input().split()))
        matriz.append(fila)
    
    elemento = int(input("Elemento a buscar: "))
    
    for i in range(n):
        for j in range(m):
            if matriz[i][j] == elemento:
                print(f"Elemento encontrado en fila {i}, columna {j}")
                return
    
    print("Elemento no encontrado.")

buscar_elemento()