def producto_escalar():
    v1 = list(map(int, input("Ingresa los valores del primer vector separados por espacio: ").split()))
    v2 = list(map(int, input("Ingresa los valores del segundo vector separados por espacio: ").split()))
    
    if len(v1) != len(v2):
        print("Los vectores deben tener la misma longitud.")
        return
    
    producto = 0
    for i in range(len(v1)):
        producto += v1[i] * v2[i]
    
    print("Producto escalar:", producto)

producto_escalar()