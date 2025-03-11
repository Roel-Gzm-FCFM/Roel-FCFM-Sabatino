def invertir_palabras():
    frase = input("Ingresa una frase: ")
    palabras = frase.split()
    nueva_frase = []
    
    for palabra in palabras:
        nueva_palabra = ""
        for letra in palabra:
            nueva_palabra = letra + nueva_palabra  # Invierte la palabra
        nueva_frase.append(nueva_palabra)
    
    resultado = ""
    for palabra in nueva_frase:
        resultado += palabra + " "

    print("Frase con palabras invertidas:", resultado.strip())

invertir_palabras()