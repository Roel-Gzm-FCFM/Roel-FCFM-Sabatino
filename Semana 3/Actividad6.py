def Invert(txt):
    cadena_invertida = txt[::-1] 
    return (cadena_invertida)

print("Función para Calcular el Promedio.")

while True:
    frase = input("Escribe la frase a invertir: ").strip()
    if frase:
        break
    print("Error. No puedes dejar el campo vacío.")

print(f"Esta es la frase invertida: {Invert(frase)}.")