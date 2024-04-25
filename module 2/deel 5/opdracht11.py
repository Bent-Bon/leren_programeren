from fruitmand import *

color = input("noem een kleur: ")
kleur_lijst = []
round_round = 0
not_round = 0

for fruit in fruitmand:
    if fruit["color"] not in kleur_lijst:
        kleur_lijst.append(fruit["color"])

for fruit in fruitmand:
    if color not in kleur_lijst:
        print(f"De kleur {color} zit er niet in de fruitmand")
        break
    elif color == fruit["color"]:
        if fruit['round'] == True: 
            round_round += 1
        else:
            not_round += 1

verschil = abs(round_round - not_round)
if color in kleur_lijst:
    if verschil > 0:
        print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {color}")
    elif verschil < 0:
        print(f"Er zijn {verschil} minder ronde vruchten dan niet ronde vruchten in de kleur {color}")
    else:
        print(f"Er zijn {round_round} ronde vruchten en {not_round} niet ronde vruchten in de kleur {color}")