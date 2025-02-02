print("Ejercicio 8: ¿El año es bisiesto?")
año = int(input("Ingrese un año: "))

if(año%4 == 0 and año%100!=0) or (año%400 == 0):
    print(f"El año {año} es bisiesto.")

else:
    print(f"El año {año} no es bisiesto.")