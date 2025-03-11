def contar_palabras():
    texto = input("Ingresa un texto: ")
    palabras = texto.split()
    print("Cantidad de palabras:", len(palabras))

contar_palabras()