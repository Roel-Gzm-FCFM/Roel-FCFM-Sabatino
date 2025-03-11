def eliminar_espacios():
    texto = input("Ingresa un texto con espacios extra: ")
    palabras = texto.split()
    
    resultado = ""
    for palabra in palabras:
        resultado += palabra + " "

    print("Texto sin espacios extra:", resultado.strip())

eliminar_espacios()
