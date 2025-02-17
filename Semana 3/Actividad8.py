def Verificacion(texto):
    txt_original = texto.lower().replace(" ", "").replace(",", "").replace(":", "").replace(".", "").replace(";", "")
    txt_reversible = txt_original[::-1]
    if (txt_reversible == txt_original):
        resultado = print(f"El texto '{texto}' es un palíndromo.")
    else:
        resultado = print(f"El texto '{texto}' no es un palíndromo.")

print("Función para Verificar Palíndromo.")
texto_verif = input("Escribe el texto a verificar: ")
Verificacion(texto_verif)