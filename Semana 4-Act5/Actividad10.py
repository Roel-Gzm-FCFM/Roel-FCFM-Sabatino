def interseccion_conjuntos():
    set1 = set(map(int, input("Ingresa los elementos del primer conjunto separados por espacio: ").split()))
    set2 = set(map(int, input("Ingresa los elementos del segundo conjunto separados por espacio: ").split()))
    
    interseccion = set1 & set2
    
    print("Intersección de conjuntos:", interseccion)

interseccion_conjuntos()