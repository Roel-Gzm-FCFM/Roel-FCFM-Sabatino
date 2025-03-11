def contar_vocales_consonantes():
    palabra = input("Ingresa una palabra: ")
    vocales = "aeiouAEIOU"
    num_vocales = 0
    num_consonantes = 0

    for letra in palabra:
        if letra in vocales:
            num_vocales += 1
        elif letra.isalpha():
            num_consonantes += 1

    print("Vocales:", num_vocales)
    print("Consonantes:", num_consonantes)

contar_vocales_consonantes()
