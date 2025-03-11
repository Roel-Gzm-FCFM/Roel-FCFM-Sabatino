def fusionar_listas_ordenadas():
    lista1 = list(map(int, input("Ingresa los números de la primera lista separados por espacio: ").split()))
    lista2 = list(map(int, input("Ingresa los números de la segunda lista separados por espacio: ").split()))
    
    fusionada = lista1 + lista2

    for i in range(len(fusionada)):
        for j in range(i + 1, len(fusionada)):
            if fusionada[i] > fusionada[j]:
                fusionada[i], fusionada[j] = fusionada[j], fusionada[i]
    
    print("Lista fusionada y ordenada:", fusionada)

fusionar_listas_ordenadas()
