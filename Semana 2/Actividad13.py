print("Contar Caracteres.")

txt = input("Escribe un texto: ")
txt_minuscula = txt.lower()

caracter = input("Escribe el caracter a contar: ")
caracter = caracter.lower()

cant = txt_minuscula.count(caracter)

print(f"Hay {cant} '{caracter}' en el texto.")
