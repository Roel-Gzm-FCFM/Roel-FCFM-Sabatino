print("Ejercicio 2: ¿Cuál es el precio con tu descuento?")
precio = float(input("Ingresa el precio del producto: "))
desc = float(input("Ingresa el porcentaje descuento (sin el símbolo): "))

descuento = precio*(desc/100)
precio_final = precio-descuento

print(f"El precio con el descuento es {precio_final}")