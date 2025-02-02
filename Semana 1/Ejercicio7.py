print("Ejercicio 7: ¿Cuál es tu IMC?")
peso = float(input("¿Cuál es tu peso?: "))
alt = float(input("¿Cuál es tu altura (metros)?: "))

imc = peso/(alt**2)

print(f"Tu IMC es: {imc}")