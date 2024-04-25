from fruitmand import *

length = 0
dict = {}
kleur_lijst = {
    "yellow" : "geel",
    "green" : "groen",
    "purple" : "paars",
    "pink" : "roze",
    "black" : "zwart",
    "orange" : "oranje",
    "brown" : "bruin"
}
kleur = " "

for fruit in fruitmand:
    if len(fruit["name"]) > length:
        length = len(fruit["name"])
        dict = fruit
        kleur = fruit["color"]

print(f"de {dict['name']} ({length} letter) heeft een {kleur_lijst[kleur]} en een gewicht van {dict['weight'] / 1000} kg")