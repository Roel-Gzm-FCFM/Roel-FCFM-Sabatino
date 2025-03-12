import math

def polares_a_cartesianas():
    r = float(input("Ingresa el radio (r): "))
    theta = float(input("Ingresa el ángulo en grados (θ): "))
    
    theta_rad = math.radians(theta)
    x = r * math.cos(theta_rad)
    y = r * math.sin(theta_rad)
    
    print("Coordenadas cartesianas:", (x, y))

polares_a_cartesianas()