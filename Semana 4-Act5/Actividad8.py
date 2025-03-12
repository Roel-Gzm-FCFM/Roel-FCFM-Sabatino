import math

def distancia_puntos():
    x1, y1 = map(float, input("Ingresa las coordenadas del primer punto (x1 y1): ").split())
    x2, y2 = map(float, input("Ingresa las coordenadas del segundo punto (x2 y2): ").split())
    
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    print("Distancia euclidiana:", distancia)

distancia_puntos()