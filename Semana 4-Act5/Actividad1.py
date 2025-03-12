def matriz_ajedrez():
    n = int(input("Ingresa el número de filas: "))
    m = int(input("Ingresa el número de columnas: "))
    
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append((i + j) % 2)
        matriz.append(fila)
    
    for fila in matriz:
        print(fila)

matriz_ajedrez()