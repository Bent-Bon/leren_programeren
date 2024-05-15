from fruitmand import *
gewicht = 0
def gewicht_checker():
    gewicht = 0
    for fruit in fruitmand:
        gewicht += fruit['weight']
    return(gewicht)

print(gewicht_checker())

fruitmand.append({
    "name" : "watermeloen",
    "weight" : 5000,
    "color" : "green",
    "round" : True
                  })

print(fruitmand) # checken of hij er in staat

print(gewicht_checker())
