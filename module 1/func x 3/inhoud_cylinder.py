import math

def calculate_cilinder_content(diameter, hoogte):
    radius = diameter / 2
    oppervlakte = radius*radius * math.pi
    return oppervlakte * hoogte

print (calculate_cilinder_content(8,5))