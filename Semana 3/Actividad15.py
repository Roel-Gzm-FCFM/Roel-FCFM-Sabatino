from random import randint

def Mayor_Menor(num, num_rand):
    if num > num_rand:
        result = print(f"El número aleatorio es menor a {num}.")
    elif num < num_rand:
        result = print(f"El número aleatorio es mayor a {num}.")
    else:
        result = print(f"Acertaste, el número aleatorio era {num}.")
        return True

print("Función para Encontrar el Segundo Mayor en una Lista.")
aleatorio = float(randint(1, 100))
while True:
    try:
        num_ingr = float(input("Ingresa un número: "))
        if Mayor_Menor(num_ingr, aleatorio):
            break
    except:
        print("Error. Ingresa un número válido.")