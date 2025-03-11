def ordenar_por_longitud():
    cantidad = int(input("¿Cuántas palabras vas a ingresar?: "))
    palabras = []
    
    for i in range(cantidad):
        palabra = input(f"Ingresa la palabra {i + 1}: ")
        palabras.append(palabra)
    
    for i in range(len(palabras)):
        for j in range(i + 1, len(palabras)):
            if len(palabras[i]) > len(palabras[j]):
                palabras[i], palabras[j] = palabras[j], palabras[i]
    
    print("Palabras ordenadas por longitud:", palabras)

ordenar_por_longitud()
