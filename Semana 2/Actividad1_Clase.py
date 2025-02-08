Otravariable = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

for variable in Otravariable:
    print(variable)
from random import randint
ctrl = True
mensajes = ["Estas seguro", "estás advertido?", "Borrando historial de chrome"]
while ctrl:
    print("1. Hola!\n2. Genera un número\n3. Salir")
    op = int(input("Opción: "))
    if op == 1:
        print("Hola guapa!")
    elif op == 2:
        print("Tu número es ", randint(1,100))
    else:
        print("Adios")
        ctrl = False

lisat1 = []
lista2 = list()



lisat1.append(12)
lisat1.append(None)

lisat1.clear()
lisat1.copy()

lista2 = lisat1.copy()

lista2.append("Cola")


lisat1.count()
lisat1.extend(lista2)

lista2 = lista2 + lisat1

lisat1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6]

lisat1.index(6)
lisat1.pop()
lisat1.remove("\n")
lisat1.reverse() #Hola aloH
lista2.sort() #ordena la lista

sum()
max()
min()
abs()
