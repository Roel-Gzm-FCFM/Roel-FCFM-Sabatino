def eliminar_impares():
    lista = list(map(int, input("Ingresa los números separados por espacio: ").split()))
    
    resultado = []
    for num in lista:
        if num % 2 == 0:
            resultado.append(num)
    
    print("Lista sin números impares:", resultado)

eliminar_impares()
