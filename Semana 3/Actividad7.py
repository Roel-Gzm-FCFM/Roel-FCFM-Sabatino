def Mediana(Lista_numeros):
    Lista_numeros.sort()
    n = len(Lista_numeros)
    if n%2 == 0:
        arriba = n//2
        abajo = n//2 - 1
        mediana = (Lista_numeros[int(arriba)] + Lista_numeros[int(abajo)])/2
    else:
        mediana = Lista_numeros[n//2]
    return mediana

print("Función para Calcular la Mediana.")
numeros = []

n = int(input("¿Cuántos números se ingresarán? "))
while n <= 0:
    print("Error. Ingresa un número válido.")
    n = int(input("¿Cuántos números se ingresarán? "))

for i in range(1, n+1):
    num = float(input(f"Ingresa el {i}º número: "))
    numeros.append(num)

print(f"\nLa mediana de\n{numeros}\nEs {Mediana(numeros)}.")