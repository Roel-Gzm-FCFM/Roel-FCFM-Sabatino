def cifrado_cesar():
    texto = input("Ingresa el texto a cifrar: ")
    desplazamiento = int(input("Ingresa el desplazamiento (número entero): "))
    
    cifrado = ""
    for letra in texto:
        if letra.isalpha():
            if "A" <= letra <= "Z":
                base = ord("A")
            else:
                base = ord("a")
            
            nueva_letra = chr(base + (ord(letra) - base + desplazamiento) % 26)
            cifrado += nueva_letra
        else:
            cifrado += letra
    
    print("Texto cifrado:", cifrado)

cifrado_cesar()
