def Cal_Polinomio(coef, x):
    resul = 0
    n = len(coef) - 1
    for i in range(n + 1):
        resul += coef[i] * (x**(n-i))
    return resul

coeficientes = []
coef_count = int(input("¿Cuántos coeficientes tiene el polinomio? "))
for i in range(1, coef_count+1):
    coefiente = float(input(f"Ingresa el {i}º coeficiente: "))
    coeficientes.append(coefiente)

x = float(input("Ingresa el valor de x: "))
print(Cal_Polinomio(coeficientes, x))