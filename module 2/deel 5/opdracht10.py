from fruitmand import *

gewicht = []

for fruit in fruitmand:
    gewicht.append(fruit['weight'])

gewicht.sort(reverse=True)

index_zero = -1
if 0 in gewicht:
    index_zero = gewicht.index(0)

for fruit in fruitmand:
    adjusted_weight = fruit['weight'] / 1000 if fruit['weight'] != 0 else index_zero / 1000
    print(f"{fruit['name']} {adjusted_weight}kg")