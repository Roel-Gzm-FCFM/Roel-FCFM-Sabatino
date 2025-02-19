def Bisiesto(ano):
    if ano%4 == 0:
        if ano%100 == 0:
            if ano%400 == 0:
                bis = print(f"El año {ano} es bisiesto.")
            else:
                bis = print(f"El año {ano} no es bisiesto.")
        else:
            bis = print(f"El año {ano} es bisiesto.")
    else:
        bis = print(f"El año {ano} no es bisiesto.")
    return bis

ano = int(input("Ingresa el año a comprobar: "))

Bisiesto(ano)