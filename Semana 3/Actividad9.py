def Segundo_Mayor(Lista):
    Lista.sort()
    seg_num = Lista[-2]
    return print(f"El segundo mayor en\n{Lista}\nEs {seg_num}")

print("Función para Encontrar el Segundo Mayor en una Lista.")
Lista = []
n = int(input("¿Cuántos números vas a ingresar? "))
while n <= 1:
    print("Error. Escribe un número mayor a 1")
    n = int(input("¿Cuántos números vas a ingresar? "))

for i in range(1, n+1):
    nums = float(input(f"Escribe el {i}º número: "))
    Lista.append(nums)

Segundo_Mayor(Lista)