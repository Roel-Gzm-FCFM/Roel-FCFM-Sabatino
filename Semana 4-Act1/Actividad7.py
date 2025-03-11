def iniciales():
    nombre = input("Ingresa tu nombre completo: ")
    palabras = nombre.split()
    
    resultado = ""
    for palabra in palabras:
        resultado += palabra[0].upper()
    
    print("Iniciales:", resultado)

iniciales()
