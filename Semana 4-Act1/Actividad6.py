def contar_subcadena():
    texto = input("Ingresa el texto completo: ")
    subcadena = input("Ingresa la subcadena a buscar: ")
    
    contador = 0
    pos = texto.find(subcadena)
    while pos != -1:
        contador += 1
        pos = texto.find(subcadena, pos + 1)
    
    print(f"La subcadena '{subcadena}' aparece {contador} veces.")

contar_subcadena()
